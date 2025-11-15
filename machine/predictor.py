# ml_model/predictor.py
import os, joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "machine", "ml_models", "doctor_recommender.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "machine", "ml_models", "tfidf_vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def recommend_doctor(symptom1, symptom2, symptom3, symptom4):
    combined = " ".join([symptom1, symptom2, symptom3, symptom4])
    X = vectorizer.transform([combined])
    prediction = model.predict(X)[0]
    return prediction
