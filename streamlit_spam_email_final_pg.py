# -*- coding: utf-8 -*-
"""STREAMLIT_SPAM_EMAIL_PG

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pzuqx3kOmhL5R9YwAVxxTw5tSVvcH5J4

CREATING MY STREAMLIT APP TO DEPLOY MY MODEL
"""

import streamlit as st
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow as tf

"""LOADING MY SPAM EMAIL CLASSIFICATION MODEL........."""

# Load the saved model and vectorizer
model = joblib.load('Rebranded_spam_email_classifier.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to predict spam or ham
def predict_spam(text):
    # Transform the text using the loaded TF-IDF vectorizer
    text_tfidf = tfidf_vectorizer.transform([text])
    # Predict using the loaded model
    prediction = model.predict(text_tfidf)
    return prediction[0]

# Streamlit app interface
st.title("Spam Email Classifier")
st.write("Enter the email text below to classify it as spam or ham.")

# Text area for user input
user_input = st.text_area("Email Text")

# Button to classify
if st.button("Classify"):
    if user_input:
        prediction = predict_spam(user_input)
        if prediction == 1:
            st.write("The email is classified as **Spam**.")
        else:
            st.write("The email is classified as **Not Spam**.")
    else:
        st.write("Please enter some text to classify.")

# Optional: Display the input text (for debugging)
# st.write("Input text:", user_input)