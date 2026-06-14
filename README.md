# 🧠 Emotion Detection System using NLP and Machine Learning

## 📌 Project Overview

This project is a Multi-Class Emotion Detection System that predicts human emotions from text using Natural Language Processing (NLP) and Machine Learning.

The model analyzes user text and classifies it into one of the following emotions:

* 😢 Sadness
* 😡 Anger
* ❤️ Love
* 😲 Surprise
* 😨 Fear
* 😊 Joy

The system was trained on a dataset containing approximately 16,000 text samples and achieved **91% accuracy** using **Bag of Words with N-Grams and Linear SVM**.

---

## 🚀 Features

* Text Cleaning and Preprocessing
* Tokenization
* Stopword Removal
* Bag of Words Vectorization
* N-Gram Feature Engineering
* Multi-Class Emotion Classification
* Linear SVM Classifier
* Streamlit Web Interface
* Real-Time Emotion Prediction

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-Learn
* Streamlit
* Pickle

---

## 📊 Model Performance

### Models Compared

| Model               | Accuracy |
| ------------------- | -------- |
| Naive Bayes         | 76%      |
| Logistic Regression | 90%      |
| Linear SVM          | 91%      |

### Vectorization Techniques Compared

| Vectorizer             | Accuracy |
| ---------------------- | -------- |
| TF-IDF                 | 86%      |
| Bag of Words           | 89%      |
| Bag of Words + N-Grams | 91%      |

### Final Model

* Vectorizer: CountVectorizer (Unigram + Bigram)
* Classifier: Linear SVM
* Accuracy: 91%

---

## 📂 Project Structure

```text
Emotion-Detection-System/
│
├── app.py
├── emotion_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── emotion_detection.ipynb
│
└── dataset/
    └── emotions.csv
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone <your-repository-link>
```

Move to project folder:

```bash
cd Emotion-Detection-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 💡 Example

Input:

```text
I am feeling very happy today.
```

Output:

```text
Joy 😊
```

---

## 🔮 Future Improvements

* Deep Learning Models (LSTM, GRU)
* BERT-based Emotion Detection
* Emotion Confidence Score
* Emotion Analytics Dashboard
* API Deployment

---

## 👨‍💻 Author

Pratham Naagar

BSc Computer Science Student | Machine Learning Enthusiast | NLP Learner
