import os
from pathlib import Path


class Settings:
    """Centralized app settings for paths and runtime configuration."""

    BASE_DIR = Path(__file__).resolve().parent.parent
    FRONTEND_DIR = BASE_DIR / "frontend"
    TEMPLATE_DIR = FRONTEND_DIR / "templates"
    STATIC_DIR = FRONTEND_DIR / "static"

    MODEL_PATH = Path(
        os.getenv("MODEL_PATH", BASE_DIR / "backend" / "models" / "random_forest_model.pkl")
    )
    VECTORIZER_PATH = Path(
        os.getenv("VECTORIZER_PATH", BASE_DIR / "backend" / "models" / "tfidf_vectorizer.pkl")
    )
