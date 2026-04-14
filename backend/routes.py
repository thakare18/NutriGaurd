from flask import Blueprint, current_app, jsonify, render_template, request

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True) or {}
        ingredients = str(data.get("ingredients", "")).strip()

        if not ingredients:
            return jsonify({"error": "No ingredients provided"}), 400

        predictor = current_app.config["PREDICTOR_SERVICE"]
        result = predictor.predict(ingredients)

        return jsonify(
            {
                "rating": result.rating,
                "level": result.level,
                "color": result.color,
            }
        )
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500
