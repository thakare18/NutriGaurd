import argparse
from pathlib import Path

import joblib


ROOT_DIR = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a single ingredient prediction")
    parser.add_argument(
        "--ingredients",
        default="Corn flour, sugar, brown sugar, palm oil, coconut oil, salt, sodium citrate, artificial flavor, malic acid",
        help="Comma-separated ingredient list",
    )
    parser.add_argument(
        "--model-path",
        default=str(ROOT_DIR / "backend" / "models" / "random_forest_model.pkl"),
        help="Path to trained model file",
    )
    parser.add_argument(
        "--vectorizer-path",
        default=str(ROOT_DIR / "backend" / "models" / "tfidf_vectorizer.pkl"),
        help="Path to trained vectorizer file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = joblib.load(args.model_path)
    vectorizer = joblib.load(args.vectorizer_path)

    transformed = vectorizer.transform([args.ingredients])
    predicted_rating = float(model.predict(transformed)[0])

    print(f"Ingredient List: {args.ingredients}")
    print(f"Predicted Health Rating: {predicted_rating:.2f}")


if __name__ == "__main__":
    main()
