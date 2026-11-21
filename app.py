import streamlit as st
import pickle
import re
from pathlib import Path

# Load trained model and vectorizer
BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "models" / "news_model.pkl", "rb") as f:
    model = pickle.load(f)

with open(BASE_DIR / "models" / "tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Category names
categories = {
    "b": "Business",
    "e": "Entertainment",
    "m": "Health",
    "t": "Technology"
}

# Clean headline
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Website
st.set_page_config(
    page_title="News Topic Classification",
    page_icon="📰",
    layout="centered"
)

st.title("📰 News Topic Classification")
st.write("Predict the category of a news headline using Machine Learning.")

headline = st.text_area(
    "Enter News Headline",
    placeholder="Example: Apple announces new AI technology"
)

if st.button("Classify News", type="primary"):
    if not headline.strip():
        st.warning("Please enter a news headline.")
    elif not clean_text(headline):
        st.warning("Please enter a valid headline containing letters.")
    else:
        cleaned = clean_text(headline)
        vectorized = tfidf.transform([cleaned])

        prediction = model.predict(vectorized)[0]
        confidence = model.predict_proba(vectorized).max() * 100

        st.success(f"Predicted Category: {categories[prediction]}")
        st.metric("Confidence Score", f"{confidence:.2f}%")