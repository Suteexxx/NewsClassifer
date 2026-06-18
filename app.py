import streamlit as st
import joblib
import numpy as np

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="News Article Classifier",
    page_icon="📰",
    layout="centered"
)

# ------------------ LABEL MAP ------------------
label_map = {
    1: "🌍 World",
    2: "🏅 Sports",
    3: "💼 Business",
    4: "💻 Sci/Tech"
}


# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_models():
    try:
        model = joblib.load("news_classifier.pkl")
        vectorizer = joblib.load("tfidf_vectorizer.pkl")
        return model, vectorizer
    except Exception as e:
        st.error(f"Error loading model files:\n{e}")
        st.stop()


model, vectorizer = load_models()

# ------------------ TITLE ------------------
st.title("📰 News Article Classifier")

st.write(
    """
Predict whether a news article belongs to:

- 🌍 World
- 🏅 Sports
- 💼 Business
- 💻 Sci/Tech
"""
)

# ------------------ INPUT BOX ------------------
article = st.text_area(
    "Paste News Article Here",
    height=250,
    placeholder="Enter article text..."
)

# ------------------ PREDICTION ------------------
if st.button("Predict Category"):

    if article.strip() == "":
        st.warning("Please enter some text.")
    else:

        try:
            # Vectorize
            article_vector = vectorizer.transform([article])

            # Prediction
            prediction = model.predict(article_vector)[0]

            # Handle string/int labels automatically
            prediction = int(prediction)

            # Probabilities
            probabilities = model.predict_proba(article_vector)[0]

            confidence = np.max(probabilities) * 100

            # Display category
            st.success(
                f"Predicted Category: {label_map[prediction]}"
            )

            # Confidence
            st.metric(
                label="Confidence",
                value=f"{confidence:.2f}%"
            )

            # ------------------ PROBABILITY BREAKDOWN ------------------
            st.subheader("Category Probabilities")

            categories = [
                "🌍 World",
                "🏅 Sports",
                "💼 Business",
                "💻 Sci/Tech"
            ]

            for category, prob in zip(categories, probabilities):
                st.write(
                    f"{category}: {prob*100:.2f}%"
                )
                st.progress(float(prob))

        except Exception as e:
            st.error(f"Prediction Error:\n{e}")

# ------------------ SIDEBAR ------------------
st.sidebar.header("About")

st.sidebar.write(
    """
### Model
- TF-IDF Vectorizer
- Logistic Regression

### Dataset
AG News Dataset

### Classes
1. World
2. Sports
3. Business
4. Sci/Tech
"""
)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption(
    "Built with Streamlit • Scikit-Learn • AG News Dataset"
)