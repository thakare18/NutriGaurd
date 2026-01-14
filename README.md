## NutriGuard

**Smart Product Label Analyzer for Health Safety**

---

### Overview

**NutriGuard** is an intelligent system that analyzes food product ingredients using Machine Learning and Natural Language Processing (NLP).
It predicts whether a product is **safe or unsafe** for consumption based on **different age categories** (children, adults, elderly).

The goal of the project is to promote **healthy and informed food choices** by helping users instantly check product safety through ingredient scanning.

---

### Features

* Ingredient analysis using machine learning.
* TF-IDF and Random Forest model for text-based predictions.
* Age-based safety prediction.
* Error handling for missing or corrupted data.
* Model persistence using `.pkl` files for reuse.

---

### Project Structure

```
NutriGuard/
│
├── .gitignore                     # Ignore unnecessary files
├── modeel.py                      # Model training with error handling
├── prddiction_of_ingred.py        # Ingredient safety prediction script
├── random_forest_model.pkl        # Trained Random Forest model
├── tfidf_vectorizer.pkl           # Saved TF-IDF vectorizer
└── README.md                      # Project documentation
```

---

### How It Works

1. **Data Preprocessing:**

   * Cleans and tokenizes ingredient text.
   * Converts text into numerical form using TF-IDF.

2. **Model Training:**

   * Trains a Random Forest Classifier on labeled datasets.
   * Classifies ingredients as safe or unsafe for specific age groups.

3. **Prediction:**

   * User inputs an ingredient list or scanned text.
   * Model predicts safety based on trained data.

---

### Technologies Used

* Python 3.x
* pandas, NumPy
* scikit-learn
* joblib
* regex, string

---

### How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/NutriGuard.git
   cd NutriGuard
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the training script:

   ```bash
   python modeel.py
   ```

4. Run the prediction script:

   ```bash
   python prddiction_of_ingred.py
   ```

---

### Example Output

**Input:**

```
Sugar, Artificial Flavors, Preservatives, Milk Solids
```

**Output:**

```
Children → Unsafe
Adults → Safe
Elderly → Use with caution (High Sugar)
```

---

### Future Enhancements

* Add OCR support to extract text from product labels.
* Build a web interface using Flask or React.
* Enable real-time camera scanning via mobile integration.

---

### Contributors

* **Prathamesh Vinayak Thakare** – ML Development & Project Leader 

---

### License

This project is licensed under the **MIT License**.
