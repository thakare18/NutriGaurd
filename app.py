from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the trained model and vectorizer
MODEL_PATH = "random_forest_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("✅ Model and vectorizer loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    vectorizer = None

@app.route('/')
def home():
    """Render the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint to predict health rating"""
    try:
        data = request.get_json()
        ingredients = data.get('ingredients', '')
        
        if not ingredients:
            return jsonify({'error': 'No ingredients provided'}), 400
        
        if model is None or vectorizer is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        # Transform ingredients using TF-IDF vectorizer
        ingredients_tfidf = vectorizer.transform([ingredients])
        
        # Predict health rating
        prediction = model.predict(ingredients_tfidf)[0]
        
        # Determine health level
        if prediction >= 8:
            level = "Excellent"
            color = "#10b981"
        elif prediction >= 6:
            level = "Good"
            color = "#3b82f6"
        elif prediction >= 4:
            level = "Moderate"
            color = "#f59e0b"
        elif prediction >= 2:
            level = "Poor"
            color = "#ef4444"
        else:
            level = "Very Poor"
            color = "#dc2626"
        
        return jsonify({
            'rating': round(prediction, 2),
            'level': level,
            'color': color
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
