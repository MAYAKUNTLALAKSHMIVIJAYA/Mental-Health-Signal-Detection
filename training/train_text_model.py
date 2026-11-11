import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import MultiLabelBinarizer

# -----------------------------
# 1. Load Dataset
# -----------------------------
DATA_PATH = "data/text_data/combined_goemotions.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded")
print("Total rows:", len(df))

# -----------------------------
# 2. Select Emotion Columns
# -----------------------------
emotion_columns = df.columns[9:]   # emotions start from column index 9

print("Emotions:", list(emotion_columns))

# -----------------------------
# 3. Remove unclear examples
# -----------------------------
df = df[df["example_very_unclear"] == False]

# -----------------------------
# 4. Prepare X and Y
# -----------------------------
X = df["text"]

# Convert each row into list of active emotions
y = df[emotion_columns].values

# -----------------------------
# 5. Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 6. TF-IDF Vectorizer
# -----------------------------
vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1,2),
    stop_words="english"
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("Text vectorization complete")

# -----------------------------
# 7. Multi-label Classifier
# -----------------------------
model = OneVsRestClassifier(
    LogisticRegression(max_iter=1000)
)

model.fit(X_train_vec, y_train)

print("Model training complete")

# -----------------------------
# 8. Evaluation
# -----------------------------
y_pred = model.predict(X_test_vec)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=emotion_columns))

# -----------------------------
# 9. Save Model
# -----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/text_model.pkl")
joblib.dump(vectorizer, "models/text_vectorizer.pkl")
joblib.dump(list(emotion_columns), "models/text_emotions.pkl")

print("\n✅ Model saved successfully in models/ folder")