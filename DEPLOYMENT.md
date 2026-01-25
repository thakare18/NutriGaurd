# NutriGuard - Ingredient Health Analyzer

AI-powered Flask application to analyze food ingredients and provide health ratings.

## 🚀 Deployment Options

### Option 1: Render.com (Recommended - FREE)
1. Push your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: nutriguard
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click "Create Web Service"
7. Your app will be live at: `https://nutriguard.onrender.com`

### Option 2: Railway.app (Fast & Modern)
1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "Start a New Project" → "Deploy from GitHub"
4. Select your repository
5. Railway will auto-detect Flask and deploy!

### Option 3: Heroku
1. Install Heroku CLI
2. Run:
```bash
heroku login
heroku create nutriguard-app
git push heroku main
```

### Option 4: PythonAnywhere (Beginner-friendly)
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files
3. Configure WSGI file
4. Your app: `https://yourusername.pythonanywhere.com`

## 📦 Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Access at http://localhost:5000
```

## ⚠️ Important Note
**Netlify does NOT support Flask/Python backend apps!** Netlify is only for static sites.
Use Render, Railway, Heroku, or PythonAnywhere instead.

## 📁 Required Files for Deployment
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Tells server how to run app
- ✅ `runtime.txt` - Specifies Python version
- ✅ `app.py` - Main Flask application
- ✅ Model files (.pkl)

## 🔧 Tech Stack
- Flask (Python web framework)
- scikit-learn (Machine Learning)
- Random Forest Regression
- TF-IDF Vectorization
