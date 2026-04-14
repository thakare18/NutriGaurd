# NutriGuard Deployment Guide

Primary deployment documentation for the project.

## Render.com

1. Push your code to GitHub
2. Create a new Web Service in Render
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app`
4. Deploy

## Local Run

```bash
pip install -r requirements.txt
python run.py
```

## Config Files

Canonical config copies are kept in:

- `config/deployment/Procfile`
- `config/deployment/runtime.txt`
- `config/requirements/base.txt`

Root compatibility files are still present for common PaaS platforms:

- `Procfile`
- `runtime.txt`
- `requirements.txt`
