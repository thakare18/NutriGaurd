from flask import Flask

from backend.config import Settings
from backend.routes import bp
from backend.services.predictor import PredictorService


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(Settings.TEMPLATE_DIR),
        static_folder=str(Settings.STATIC_DIR),
    )

    app.config["PREDICTOR_SERVICE"] = PredictorService(
        model_path=Settings.MODEL_PATH,
        vectorizer_path=Settings.VECTORIZER_PATH,
    )

    app.register_blueprint(bp)
    return app
