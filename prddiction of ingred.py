import joblib

# ✅ Load the saved model & vectorizer
loaded_rf = joblib.load("random_forest_model.pkl")
loaded_tfidf = joblib.load("tfidf_vectorizer.pkl")

# ✅ New ingredient input (comma-separated string)
new_ingredient = "Corn flour, sugar, brown sugar,palm oil, coconut oil, salt, sodium citrate, artificial flavor, malic acid"

# ✅ Transform the text using the loaded TF-IDF vectorizer
new_tfidf = loaded_tfidf.transform([new_ingredient])  # Pass as a list

# ✅ Predict the health rating
predicted_rating = loaded_rf.predict(new_tfidf)[0]  # Extract single value

print(f"Ingredient List: {new_ingredient}")
print(f"Predicted Health Rating: {predicted_rating:.2f}")
