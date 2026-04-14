from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import joblib


@dataclass
class PredictionResult:
    rating: float
    level: str
    color: str


class PredictorService:
    def __init__(self, model_path: Path, vectorizer_path: Path) -> None:
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.model: Optional[object] = None
        self.vectorizer: Optional[object] = None
        self._load_artifacts()

    def _load_artifacts(self) -> None:
        try:
            self.model = joblib.load(self.model_path)
            self.vectorizer = joblib.load(self.vectorizer_path)
        except Exception:
            self.model = None
            self.vectorizer = None

    @property
    def is_ready(self) -> bool:
        return self.model is not None and self.vectorizer is not None

    def predict(self, ingredients: str) -> PredictionResult:
        if not self.is_ready:
            raise RuntimeError("Model artifacts are not loaded")

        ingredients_tfidf = self.vectorizer.transform([ingredients])
        prediction = float(self.model.predict(ingredients_tfidf)[0])

        if prediction >= 8:
            level, color = "Excellent", "#10b981"
        elif prediction >= 6:
            level, color = "Good", "#3b82f6"
        elif prediction >= 4:
            level, color = "Moderate", "#f59e0b"
        elif prediction >= 2:
            level, color = "Poor", "#ef4444"
        else:
            level, color = "Very Poor", "#dc2626"

        return PredictionResult(rating=round(prediction, 2), level=level, color=color)
