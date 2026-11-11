import os
# Ensure Keras runs with torch backend and local home to avoid WDAC policy / permission conflicts
os.environ.setdefault("KERAS_BACKEND", "torch")
os.environ.setdefault("KERAS_HOME", os.path.abspath("static/temp/.keras"))

import cv2
import numpy as np
import tempfile
import joblib
import keras
import librosa

try:
    from moviepy import VideoFileClip
except ImportError:
    from moviepy.video.io.VideoFileClip import VideoFileClip

from utils.histogram import generate_histogram
from utils.suggestions import get_suggestions


# ============================
# LOAD MODELS (once)
# ============================

image_model = keras.models.load_model("models/image_model.h5")
audio_model = joblib.load("models/audio_model.pkl")
audio_label_encoder = joblib.load("models/audio_label_encoder.pkl")

IMAGE_EMOTIONS = [
    "angry",
    "disgust",
    "fear",
    "happy",
    "neutral",
    "sad",
    "surprise"
]

AUDIO_EMOTIONS = [str(cls).lower() for cls in audio_label_encoder.classes_]


# ============================
# IMAGE PROCESSING FROM VIDEO
# ============================

def preprocess_frame(frame):
    if len(frame.shape) == 3:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        gray = frame
    resized = cv2.resize(gray, (48, 48))
    normalized = resized / 255.0
    reshaped = normalized.reshape(1, 48, 48, 1).astype(np.float32)
    return reshaped


def predict_video_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_probs = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # sample every 10th frame
        if frame_count % 10 == 0:
            processed = preprocess_frame(frame)
            probs = image_model.predict(processed, verbose=0)[0]
            frame_probs.append(probs)

        frame_count += 1

    cap.release()

    if len(frame_probs) == 0:
        return np.zeros(len(IMAGE_EMOTIONS))

    avg_probs = np.mean(frame_probs, axis=0)
    return avg_probs


# ============================
# AUDIO FROM VIDEO
# ============================

def extract_audio_from_video(video_path):
    clip = None
    try:
        clip = VideoFileClip(video_path)
        if clip.audio is None:
            return None

        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        audio_path = temp_audio.name
        temp_audio.close()

        clip.audio.write_audiofile(
            audio_path,
            verbose=False,
            logger=None
        )
        return audio_path
    except Exception as e:
        print(f"Warning: Audio extraction failed or video has no sound ({e})")
        return None
    finally:
        if clip is not None:
            try:
                clip.close()
            except Exception:
                pass


def extract_audio_features(file_path):
    signal, sr = librosa.load(file_path, sr=22050)
    mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)
    return mfcc.reshape(1, -1)


def predict_video_audio(video_path):
    audio_path = extract_audio_from_video(video_path)
    if audio_path is None or not os.path.exists(audio_path):
        return None

    try:
        features = extract_audio_features(audio_path)
        probs = audio_model.predict_proba(features)[0]
        return probs
    finally:
        if audio_path and os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except Exception:
                pass


# ============================
# FINAL HYBRID PREDICTION
# ============================

def predict_video(video_path):
    # Image prediction
    image_probs = predict_video_frames(video_path)
    img_dict = {emo: float(p) for emo, p in zip(IMAGE_EMOTIONS, image_probs)}

    # Audio prediction
    audio_probs = predict_video_audio(video_path)

    if audio_probs is not None:
        aud_dict = {emo: float(p) for emo, p in zip(AUDIO_EMOTIONS, audio_probs)}
        # Map audio 'calm' into 'neutral' for fusion consistency
        if "calm" in aud_dict:
            aud_dict["neutral"] = aud_dict.get("neutral", 0.0) + aud_dict.pop("calm")

        # Combine aligned by emotion label name
        common_emotions = IMAGE_EMOTIONS
        combined_probs = []
        for emo in common_emotions:
            p_img = img_dict.get(emo, 0.0)
            p_aud = aud_dict.get(emo, 0.0)
            combined_probs.append((p_img + p_aud) / 2.0)
    else:
        # Fallback to visual probabilities if video has no audio
        common_emotions = IMAGE_EMOTIONS
        combined_probs = [img_dict.get(emo, 0.0) for emo in common_emotions]

    combined_probs = np.array(combined_probs)
    # Normalize sum to 1
    total = np.sum(combined_probs)
    if total > 0:
        combined_probs = combined_probs / total

    top_index = int(np.argmax(combined_probs))
    top_emotion = common_emotions[top_index]
    confidence = float(combined_probs[top_index])

    hist_path = generate_histogram(common_emotions, combined_probs)
    suggestions = get_suggestions(top_emotion)

    return {
        "prediction": top_emotion,
        "confidence": confidence,
        "histogram_path": hist_path,
        "suggestions": suggestions
    }
