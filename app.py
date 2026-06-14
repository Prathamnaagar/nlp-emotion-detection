import streamlit as st
import pickle

# Load Model
model = pickle.load(open("emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Reverse Mapping
emotion_map = {
    0: "Sadness 😢",
    1: "Anger 😡",
    2: "Love ❤️",
    3: "Surprise 😲",
    4: "Fear 😨",
    5: "Joy 😊"
}

st.title("Emotion Detection System")

user_text = st.text_area(
    "Enter Your Text",
    placeholder="Type something..."
)

if st.button("Predict Emotion"):

    if user_text:

        vector = vectorizer.transform([user_text])

        prediction = model.predict(vector)[0]

        st.success(
            f"Detected Emotion: {emotion_map[prediction]}"
        )