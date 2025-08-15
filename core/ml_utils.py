import os
from transformers import pipeline

# Path where your model is saved (adjust to your setup)
MODEL_DIR = os.path.join(os.path.dirname(__file__), "distilbert_sentiment_model")

# Load model only once (singleton pattern)
_sentiment_pipeline = None

def load_model():
    """
    Loads the DistilBERT sentiment model from local directory.
    This will not download from the internet.
    """
    global _sentiment_pipeline
    if _sentiment_pipeline is None:
        if not os.path.exists(MODEL_DIR):
            raise FileNotFoundError(
                f"Model not found in {MODEL_DIR}. Please download and save it locally."
            )
        _sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_DIR)
    return _sentiment_pipeline

def predict_sentiment(text):
    """
    Returns sentiment label and score for a given text.
    """
    pipe = load_model()
    result = pipe(text)[0]  # {'label': 'POSITIVE', 'score': 0.99}
    return result['label'], result['score']
