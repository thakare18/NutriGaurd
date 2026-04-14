import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


ROOT_DIR = Path(__file__).resolve().parent.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train NutriGuard ingredient health model")
    parser.add_argument(
        "--data",
        default=str(ROOT_DIR / "training_a_model" / "cleaned_ingredients_dataset.csv"),
        help="Path to CSV dataset with Ingredient and Health Rating columns",
    )
    parser.add_argument(
        "--model-output",
        default=str(ROOT_DIR / "backend" / "models" / "random_forest_model.pkl"),
        help="Output path for trained model file",
    )
    parser.add_argument(
        "--vectorizer-output",
        default=str(ROOT_DIR / "backend" / "models" / "tfidf_vectorizer.pkl"),
        help="Output path for trained TF-IDF vectorizer file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data_path = Path(args.data)
    model_output = Path(args.model_output)
    vectorizer_output = Path(args.vectorizer_output)

    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found at '{data_path}'.")

    try:
        df = pd.read_csv(data_path)
    except pd.errors.EmptyDataError as exc:
        raise ValueError("Dataset file is empty.") from exc
    except pd.errors.ParserError as exc:
        raise ValueError("Dataset file is corrupted or unreadable.") from exc

    df = df.dropna().copy()
    df["Ingredient"] = df["Ingredient"].astype(str).str.lower().str.strip()
    df["Health Rating"] = df["Health Rating"].astype(float)

    tfidf = TfidfVectorizer()
    x_data = tfidf.fit_transform(df["Ingredient"])
    y_data = df["Health Rating"]

    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Mean Absolute Error: {mae:.2f}")

    model_output.parent.mkdir(parents=True, exist_ok=True)
    vectorizer_output.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_output)
    joblib.dump(tfidf, vectorizer_output)
    print(f"Model saved to: {model_output}")
    print(f"Vectorizer saved to: {vectorizer_output}")


if __name__ == "__main__":
    main()
