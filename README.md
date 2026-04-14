# NutriGuard

AI-powered ingredient health analyzer built with Flask, scikit-learn, and a production-oriented project layout.

Live app: https://nutrigaurd.onrender.com

## Features

- Ingredient analysis using TF-IDF + Random Forest regression
- Web UI for instant health score prediction
- Service-oriented backend structure (app factory + route layer + predictor service)
- Separate frontend asset/template directory for maintainability
- Reusable model artifacts via joblib

## Production-Style Structure

```text
Machine-learning-P1/
├── backend/
│   ├── __init__.py                # Flask app factory
│   ├── config.py                  # Runtime and path settings
│   ├── routes.py                  # HTTP routes (/ and /predict)
│   ├── models/                    # Trained ML artifacts
│   │   ├── random_forest_model.pkl
│   │   └── tfidf_vectorizer.pkl
│   └── services/
│       └── predictor.py           # ML inference service
├── frontend/
│   ├── templates/
│   │   └── index.html             # Main UI template
│   └── static/
│       ├── css/
│       │   └── style.css          # UI styles
│       └── js/
│           └── script.js          # Client-side logic
├── scripts/
│   ├── train_model.py             # Train model and save artifacts
│   └── predict_sample.py          # CLI sample prediction
├── config/
│   ├── deployment/
│   │   ├── Procfile               # Canonical deploy process file
│   │   └── runtime.txt            # Canonical Python runtime version
│   ├── docs/
│   │   └── DEPLOYMENT.md          # Deployment guide
│   └── requirements/
│       └── base.txt               # Canonical Python dependencies
├── run.py                         # WSGI entrypoint for deployment
├── app.py                         # Backward-compatible local runner
├── requirements.txt               # Root compatibility file (includes config/requirements/base.txt)
├── Procfile                       # Root compatibility file
└── runtime.txt                    # Root compatibility file
```

## Local Development

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the web app:

```bash
python run.py
```

3. Open:

```text
http://localhost:5000
```

## Model Training

Train with default dataset/output paths:

```bash
python scripts/train_model.py
```

Optional custom paths:

```bash
python scripts/train_model.py --data path/to/cleaned_ingredients_dataset.csv --model-output random_forest_model.pkl --vectorizer-output tfidf_vectorizer.pkl
```

Example with backend output location:

```bash
python scripts/train_model.py --model-output backend/models/random_forest_model.pkl --vectorizer-output backend/models/tfidf_vectorizer.pkl
```

## Sample CLI Prediction

```bash
python scripts/predict_sample.py --ingredients "oats, almonds, honey"
```

## Deployment

The app is deployment-ready with Gunicorn:

```text
web: gunicorn run:app
```

Note: canonical config copies live under `config/`, while root files are retained for platform compatibility.

## License

MIT License
