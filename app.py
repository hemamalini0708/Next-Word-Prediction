import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# load model
model = load_model("next_words.h5")

# load tokenizer
tokenizer = pickle.load(open("token.pkl", "rb"))

max_sequence_len = model.input_shape[1]


def predict_next_word(text):
    sequence = tokenizer.texts_to_sequences([text])[0]
    sequence = pad_sequences([sequence], maxlen=max_sequence_len)

    preds = model.predict(sequence)
    predicted_index = np.argmax(preds)

    predicted_word = ""

    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            predicted_word = word
            break

    return predicted_word


st.title("Next Word Prediction")

user_input = st.text_input("Enter text (last words of sentence)")

if st.button("Predict"):
    words = user_input.split()
    words = words[-3:]
    text = " ".join(words)

    prediction = predict_next_word(text)

    st.success("Next Word: " + prediction)