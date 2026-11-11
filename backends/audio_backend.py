import librosa
import numpy as np
import joblib
import os
from utils.histogram import generate_histogram
from utils.suggestions import get_suggestions

model = joblib.load("models/audio_model.pkl")
label_encoder = joblib.load("models/audio_label_encoder.pkl")

EMOTIONS = [str(cls) for cls in label_encoder.classes_]

def extract_features(file_path):
    signal, sr = librosa.load(file_path, sr=22050)
    mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)
    return mfcc.reshape(1, -1)

def predict_audio(file_path):
    features = extract_features(file_path)

    probs = model.predict_proba(features)[0]
    pred_index = int(np.argmax(probs))

    emotion = str(label_encoder.inverse_transform([pred_index])[0])
    confidence = float(probs[pred_index])

    hist_path = generate_histogram(EMOTIONS, probs)
    suggestions = get_suggestions(emotion)

    return {
        "prediction": emotion,
        "confidence": confidence,
        "histogram_path": hist_path,
        "suggestions": suggestions
    }
