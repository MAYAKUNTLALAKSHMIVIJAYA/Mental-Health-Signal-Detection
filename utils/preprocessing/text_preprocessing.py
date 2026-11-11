# utils/preprocessing/text_preprocessing.py
import pandas as pd
import re

# List of emotion columns in GoEmotions
EMOTION_COLUMNS = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring',
    'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval',
    'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief',
    'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization',
    'relief', 'remorse', 'sadness', 'surprise', 'neutral'
]

def load_text_data(file_path):
    """
    Load GoEmotions CSV.
    """
    df = pd.read_csv(file_path)
    # Just keep 'text' and all emotion columns
    df = df[['text'] + EMOTION_COLUMNS]
    return df

def clean_text(text):
    """
    Basic text cleaning: lowercase, remove non-alphanumeric chars
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_text(df):
    """
    Clean text and extract features and labels
    """
    # Clean text
    df['clean_text'] = df['text'].apply(clean_text)

    # X = cleaned text
    X = df['clean_text'].values

    # y = all emotion columns
    y = df[EMOTION_COLUMNS].values

    return X, y