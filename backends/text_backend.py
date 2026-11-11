import joblib
import numpy as np

from utils.histogram import generate_histogram
from utils.suggestions import get_suggestions

# Load once at startup
model = joblib.load("models/text_model.pkl")
vectorizer = joblib.load("models/text_vectorizer.pkl")
emotions = [str(e) for e in joblib.load("models/text_emotions.pkl")]

def predict_text(text: str):
    # Vectorize
    X = vectorizer.transform([text])

    # Predict probabilities (multi-label)
    probabilities = model.predict_proba(X)[0]

    # Get top emotion
    top_index = int(np.argmax(probabilities))
    top_emotion = emotions[top_index]
    top_confidence = float(probabilities[top_index])

    # Generate histogram
    hist_path = generate_histogram(emotions, probabilities)

    # Suggestions
    suggestions = get_suggestions(top_emotion)

    return {
        "prediction": top_emotion,
        "confidence": top_confidence,
        "all_probabilities": dict(zip(emotions, [float(p) for p in probabilities])),
        "suggestions": suggestions,
        "histogram_path": hist_path
    }
