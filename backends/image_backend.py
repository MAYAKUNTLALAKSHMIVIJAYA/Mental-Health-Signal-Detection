import os
# Ensure Keras runs with torch backend and local home to avoid WDAC policy / permission conflicts
os.environ.setdefault("KERAS_BACKEND", "torch")
os.environ.setdefault("KERAS_HOME", os.path.abspath("static/temp/.keras"))

import keras
import numpy as np
import cv2
from utils.histogram import generate_histogram
from utils.suggestions import get_suggestions

model = keras.models.load_model("models/image_model.h5")

EMOTIONS = [
    "angry",
    "disgust",
    "fear",
    "happy",
    "neutral",
    "sad",
    "surprise"
]

def preprocess_image(image):
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    resized = cv2.resize(gray, (48, 48))
    normalized = resized / 255.0
    reshaped = normalized.reshape(1, 48, 48, 1).astype(np.float32)

    return reshaped

def predict_image(image):
    processed = preprocess_image(image)

    probabilities = model.predict(processed, verbose=0)[0]

    top_index = int(np.argmax(probabilities))
    top_emotion = EMOTIONS[top_index]
    confidence = float(probabilities[top_index])

    hist_path = generate_histogram(EMOTIONS, probabilities)
    suggestions = get_suggestions(top_emotion)

    return {
        "prediction": top_emotion,
        "confidence": confidence,
        "histogram_path": hist_path,
        "suggestions": suggestions
    }
