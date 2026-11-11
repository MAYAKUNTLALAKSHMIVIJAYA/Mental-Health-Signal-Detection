import os
import numpy as np
import librosa
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

DATA_PATH = "data/audio_data"

X = []
y = []

emotion_map = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fear",
    "07": "disgust",
    "08": "surprise"
}

print("Loading audio dataset...")

for actor in os.listdir(DATA_PATH):

    actor_path = os.path.join(DATA_PATH, actor)

    if not os.path.isdir(actor_path):
        continue

    for file in os.listdir(actor_path):

        if file.endswith(".wav"):

            parts = file.split("-")
            emotion_code = parts[2]

            emotion = emotion_map.get(emotion_code)
            if emotion is None:
                continue

            file_path = os.path.join(actor_path, file)

            # load audio
            signal, sr = librosa.load(file_path, sr=22050)

            # extract MFCC
            mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=40)
            mfcc = np.mean(mfcc.T, axis=0)

            X.append(mfcc)
            y.append(emotion)

print("Dataset loaded")

X = np.array(X)
y = np.array(y)

# encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print("Accuracy:", acc)

# save
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/audio_model.pkl")
joblib.dump(le, "models/audio_label_encoder.pkl")

print("✅ Audio model saved")