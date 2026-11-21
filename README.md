# 📰 News Topic Classification Using NLP

### 🚀 Intelligent News Headline Classification with Machine Learning

![Python](https://img.shields.io/badge/Python-3.15-blue?logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-93.82%25-brightgreen)
![Status](https://img.shields.io/badge/Status-Working-success)

---

## 🌟 Project Overview

In today's digital world, thousands of news articles are published every minute. Manually organizing these articles into categories can be time-consuming.

**News Topic Classification** is a Natural Language Processing (NLP) project that automatically identifies the topic of a news headline using Machine Learning.

The system analyzes the headline and predicts its most relevant category, along with a confidence score, through an interactive Streamlit web application.

🎯 **Project Goal:** Build an accurate, efficient, and user-friendly news classification system.

---

## ✨ Key Features

- 🧠 **Machine Learning Powered** — Uses Logistic Regression for multiclass classification.
- 📰 **Headline Classification** — Predicts news topics from user-provided headlines.
- 📊 **High Accuracy** — Achieves 93.82% accuracy on the test dataset.
- 🎯 **Confidence Score** — Displays the model's estimated prediction probability.
- 🧹 **Text Preprocessing** — Cleans and normalizes news headlines.
- ⚡ **TF-IDF Feature Extraction** — Converts text into numerical features.
- 🌐 **Interactive Web Application** — Built using Streamlit.
- 📈 **Model Evaluation** — Includes precision, recall, F1-score, and confusion matrix.

---

## 🗂️ News Categories

The model classifies news headlines into four categories:

| Category | Label | Description |
|---|---|---|
| 💼 Business | `b` | Finance, companies, markets, and economic developments |
| 🎬 Entertainment | `e` | Movies, celebrities, music, and entertainment news |
| 🏥 Health | `m` | Medical research, healthcare, and health-related developments |
| 💻 Technology | `t` | Software, AI, gadgets, and technological innovations |

---

## 📚 Dataset Information

**Dataset:** UCI News Aggregator Dataset

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/359/news+aggregator)

The original dataset contains **422,419 news articles**.

### 📊 Category Distribution

| Category | Number of Articles |
|---|---:|
| 🎬 Entertainment | 152,469 |
| 💼 Business | 115,967 |
| 💻 Technology | 108,344 |
| 🏥 Health | 45,639 |
| **Total** | **422,419** |

The dataset includes news headlines, URLs, publishers, categories, timestamps, and other metadata.

For model training, the project primarily uses the news headline and its corresponding category.

---

## ⚙️ Project Workflow

The complete machine learning pipeline follows these steps:

**📥 Dataset Collection**

↓

**🔍 Exploratory Data Analysis**

↓

**🧹 Data Cleaning & Text Preprocessing**

↓

**✂️ Train-Test Split (80:20)**

↓

**🔢 TF-IDF Feature Extraction**

↓

**🤖 Logistic Regression Model Training**

↓

**📊 Model Evaluation**

↓

**💾 Model Serialization**

↓

**🌐 Streamlit Web Application**

### 🧹 Text Preprocessing

The preprocessing pipeline includes:

- Converting text to lowercase
- Removing unnecessary special characters and numbers
- Removing extra whitespace
- Removing English stop words during TF-IDF vectorization
- Removing duplicate headline-category records

### 🤖 Machine Learning Algorithm

**Logistic Regression** is used for multiclass news classification.

TF-IDF (Term Frequency–Inverse Document Frequency) converts news headlines into numerical feature vectors, which are then used to train the classification model.

---

## 📈 Model Performance

The trained model achieved the following performance on **81,462 test articles**.

### 🏆 Overall Accuracy: 93.82%

| Category | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| 💼 Business | 0.92 | 0.92 | 0.92 |
| 🎬 Entertainment | 0.96 | 0.98 | 0.97 |
| 🏥 Health | 0.95 | 0.91 | 0.93 |
| 💻 Technology | 0.92 | 0.92 | 0.92 |
| **Macro Average** | **0.94** | **0.93** | **0.93** |
| **Weighted Average** | **0.94** | **0.94** | **0.94** |

### 📉 Confusion Matrix

The confusion matrix helps visualize correct and incorrect predictions across the four news categories.

It shows that the model performs particularly well on Entertainment headlines, while some confusion exists between Business and Technology.

---

## 🖥️ Web Application

The project includes a Streamlit-based interface where users can enter a news headline and instantly receive a predicted category and confidence score.

### 🔎 Example Prediction

**Input Headline:**

> Apple launches new artificial intelligence technology

**Model Output:**

- 🏷️ Predicted Category: **Technology**
- 🎯 Confidence Score: **99.15%**

*Note: The confidence score represents the model's estimated probability, not a guarantee of correctness.*

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming language |
| 🐼 Pandas | Dataset manipulation |
| 🔢 NumPy | Numerical operations |
| 🧠 Scikit-learn | Machine learning and evaluation |
| 📝 TF-IDF | Text feature extraction |
| 📊 Matplotlib | Data visualization |
| 🌐 Streamlit | Interactive web interface |
| 📓 Jupyter Notebook | Experimentation and analysis |
| 💾 Pickle | Model serialization |

---

## 📁 Project Structure

```text
news-topic-classification/
│
├── 📂 data/
│   └── newsCorpora.csv
│
├── 📂 notebooks/
│   └── news_classification.ipynb
│
├── 📂 models/
│   ├── news_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── 🐍 app.py
├── 📋 requirements.txt
└── 📖 README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/news-topic-classification.git
cd news-topic-classification
```

Replace `YOUR_USERNAME` with your GitHub username after creating the repository.

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the Environment

**Windows:**

```powershell
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit Application

```bash
python -m streamlit run app.py
```

### 6️⃣ Open the Application

Visit:

**http://localhost:8501**

Enter a news headline and click **Classify News** to view the prediction.

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Natural Language Processing fundamentals
- Text preprocessing and cleaning
- Feature extraction using TF-IDF
- Supervised machine learning
- Multiclass text classification
- Model training and testing
- Performance evaluation
- Model serialization and inference
- Interactive ML application development

---

## 🔮 Future Improvements

Potential enhancements include:

- 🤖 Transformer-based classification using BERT
- 🌍 Multilingual news classification
- 📄 Full-article classification
- 📊 Interactive category probability charts
- 🔗 Classification using news article URLs
- ☁️ Cloud deployment
- 📱 Improved mobile-responsive interface

---

## 👨‍💻 Project Team

**NLP Capstone Project — P3**

**Group 13 | K.R. Mangalam University**

| Team Member | Role |
|---|---|
| Harsh Kaushik | Team Member |
| Randeep Kaur | Team Member |
| Devansh Kumar | Team Member |

**Academic Program:** B.Tech Computer Science & Engineering (AI & ML)

---

## 📌 Project Status

✅ Dataset Collection

✅ Data Preprocessing

✅ Feature Engineering

✅ Model Training

✅ Model Evaluation

✅ Confusion Matrix

✅ Streamlit Web Application

✅ Prediction Testing

🚧 GitHub Repository & Final Documentation

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

**Built with 🐍 Python, 🧠 Machine Learning, and ❤️ for NLP.**
