import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load model and columns
model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

st.title("Diabetes Prediction App")

# Inputs
chol = st.number_input("Cholesterol")
stab_glu = st.number_input("Stabilized Glucose")
hdl = st.number_input("HDL")
ratio = st.number_input("Chol/HDL Ratio")
age = st.number_input("Age")
height = st.number_input("Height")
weight = st.number_input("Weight")
waist = st.number_input("Waist")
hip = st.number_input("Hip")

gender = st.selectbox("Gender", ["Male", "Female"])
location = st.selectbox("Location", ["Urban", "Rural"])
frame = st.selectbox("Frame", ["Small", "Medium", "Large"])

if st.button("Predict"):
    
    # Create input dictionary
    input_dict = {
        'chol': chol,
        'stab.glu': stab_glu,
        'hdl': hdl,
        'ratio': ratio,
        'age': age,
        'height': height,
        'weight': weight,
        'waist': waist,
        'hip': hip,
        'gender_Male': 1 if gender == "Male" else 0,
        'location_Urban': 1 if location == "Urban" else 0,
        'frame_Medium': 1 if frame == "Medium" else 0,
        'frame_Large': 1 if frame == "Large" else 0
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Add missing columns (VERY IMPORTANT 🔥)
    for col in columns:
        if col not in input_df:
            input_df[col] = 0

    # Ensure correct order
    input_df = input_df[columns]

    # Prediction
    result = model.predict(input_df)

    if result[0] == 1:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Not Diabetic")