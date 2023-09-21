# Import necessary libraries
import streamlit as st
import pickle
#import xgboost as xgb
import numpy as np
import pandas as pd
from PIL import Image

# Load the saved XGBoost model
model_path ="random_forest_model.pkl"
random_forest_model = pickle.load(open(model_path, 'rb'))

# Define the Streamlit app title
st.title("Combine Cycle Power Plant Energy Prediction Web Application")
st.header('Machine Learning Model')
image = Image.open("Rimg.jpg")
st.image(image, "")

# Add custom CSS for styling
st.markdown("""
<style>
body {
    background-color: #ffcccc; /* Background color */
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
.container {
    background-color: #ffffff; /* Container background color */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #888888;
    max-width: 500px;
    margin: auto;
    margin-top: 20px;
}
h1 {
    color: #1a1a1a; /* Header text color */
    text-align: center;
}
img {
    max-width: 100%;
}
h2 {
    color: #333; /* Subheader text color */
    margin-top: 20px;
}
label {
    font-weight: bold;
}
input[type="number"] {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    width: 100%;
    border-radius: 5px;
}
button[type="button"] {
    background-color: #0074e4; /* Button background color */
    color: #fff; /* Button text color */
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    font-weight: bold;
    margin-top: 10px; /* Adjust margin */
}
#prediction_result {
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Create input fields for user input
st.markdown('<h2 style="color: #333;">Enter Input Parameters:</h2>', unsafe_allow_html=True)
temperature = st.number_input("Temperature")
exhaust_vacuum = st.number_input("Exhaust Vacuum")
amb_pressure = st.number_input("Ambient Pressure")
r_humidity = st.number_input("Relative Humidity")

# Create a prediction button
if st.button("Predict"):
    # Make predictions
    user_input = np.array([[temperature, exhaust_vacuum, amb_pressure, r_humidity]])
    prediction = random_forest_model.predict(pd.DataFrame(user_input, columns=['temperature', 'exhaust_vacuum', 'amb_pressure', 'r_humidity']))[0]

    # Display prediction
    st.markdown('<h2 style="color: #333;">Prediction:</h2>', unsafe_allow_html=True)
    st.markdown(f'<div id="prediction_result">Predicted Energy Output: <span>{prediction:.2f} MW</span></div>', unsafe_allow_html=True)
