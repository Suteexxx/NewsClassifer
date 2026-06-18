# 📰 News Article Classification using Machine Learning

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![License](https://img.shields.io/badge/License-MIT-green)

### Classify News Articles into World, Sports, Business, and Sci/Tech Categories using TF-IDF and Logistic Regression

</div>

---

## 📌 Overview

This project implements an end-to-end **News Article Classification System** that automatically categorizes news articles into four classes:

* 🌍 World
* 🏅 Sports
* 💼 Business
* 💻 Sci/Tech

The model is trained on the **AG News Dataset** and deployed using **Streamlit**, providing an interactive web interface where users can paste any news article and instantly receive a category prediction along with confidence scores.

---

## 🚀 Features

✅ Automatic news classification

✅ Interactive Streamlit web application

✅ Confidence score visualization

✅ Probability distribution for all categories

✅ Trained using TF-IDF vectorization

✅ Logistic Regression classifier

✅ Model saved using Pickle (.pkl)

✅ Easy deployment on Streamlit Cloud

---

## 🏗️ Project Architecture

```text
                User
                  │
                  ▼
          News Article Input
                  │
                  ▼
          Text Preprocessing
                  │
                  ▼
           TF-IDF Vectorizer
                  │
                  ▼
         Logistic Regression
                  │
                  ▼
          Category Prediction
                  │
                  ▼
        Streamlit Visualization
```

---

# 📂 Project Structure

```text
NewsClassifier/
│
├── app.py
├── train_model.ipynb
├── news_classifier.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
│
├── train.csv
└── test.csv
```

---

# 📊 Dataset

## AG News Dataset

The AG News dataset contains news articles divided into four categories:

| Label | Category |
| ----- | -------- |
| 1     | World    |
| 2     | Sports   |
| 3     | Business |
| 4     | Sci/Tech |

### Dataset Statistics

* Training Samples: **120,000**
* Test Samples: **7,600**
* Total Classes: **4**

---

## 🔗 Dataset Link

### Kaggle

https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset

### HuggingFace

https://huggingface.co/datasets/ag_news

---

# ⚙️ Tech Stack

| Component           | Technology          |
| ------------------- | ------------------- |
| Language            | Python              |
| Data Processing     | Pandas, NumPy       |
| Feature Extraction  | TF-IDF              |
| Model               | Logistic Regression |
| Evaluation          | Scikit-Learn        |
| Visualization       | Matplotlib, Seaborn |
| Model Serialization | Joblib              |
| Frontend            | Streamlit           |

---

# 🧠 Machine Learning Pipeline

## 1. Data Loading

```python
train.csv
test.csv
```

↓

## 2. Text Preprocessing

* Combine title and description
* Remove stop words
* Convert text to numerical representation

↓

## 3. Feature Extraction

TF-IDF Vectorization

↓

## 4. Model Training

Logistic Regression

↓

## 5. Evaluation

* Accuracy Score
* Classification Report
* Confusion Matrix

↓

## 6. Save Model

```python
news_classifier.pkl
tfidf_vectorizer.pkl
```

↓

## 7. Deploy with Streamlit

---

# 📈 Model Performance

### Accuracy

```text
≈ 91%
```

### Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

# 🖥️ Streamlit Web App

The web application allows users to:

* Paste any news article.
* Predict its category.
* View prediction confidence.
* See probability distribution for all classes.

---

# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/NewsClassifier.git
```

Move to the project directory:

```bash
cd NewsClassifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The app will start at:

```text
http://localhost:8501
```

---

# 📦 Requirements

```text
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
joblib
```

Install using:

```bash
pip install -r requirements.txt
```

---

# 🔍 Example Prediction

### Input

```text
Apple unveiled its latest AI-powered iPhone at a launch event in California.
```

### Output

```text
💻 Sci/Tech
Confidence: 96.32%
```

---

# 📸 Screenshots

Add screenshots of:

* Home Page
* Prediction Output
* Probability Scores

---

# 🔮 Future Improvements

* BERT-based News Classification
* Topic Modeling with BERTopic
* News Summarization
* Sentiment Analysis
* News Recommendation System
* FastAPI Backend
* HuggingFace Deployment
* Docker Support

---

# 📚 Libraries Used

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

---

# 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository and submit a pull request.

---

# ⭐ If you found this project useful, consider giving it a star!

---

## 👨‍💻 Author

**Suteekshn Manchanda**

B.Tech Electronics and Communication Engineering
Maharaja Agrasen Institute of Technology (MAIT)

GitHub: https://github.com/Suteexxx

LinkedIn: https://linkedin.com/in/suteekshn-manchanda

---
