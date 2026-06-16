import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("model.pkl", "rb"))

st.title("📊 Customer Churn Prediction System")

# User Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider("Tenure (Months)", 0, 72, 12)

phone_service = st.selectbox("Phone Service", ["No", "Yes"])

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)

# Convert Text to Numbers
gender = 0 if gender == "Female" else 1
senior = 0 if senior == "No" else 1
partner = 0 if partner == "No" else 1
dependents = 0 if dependents == "No" else 1
phone_service = 0 if phone_service == "No" else 1

# Default values for remaining encoded features
multiple_lines = 0
internet_service = 0
online_security = 0
online_backup = 0
device_protection = 0
tech_support = 0
streaming_tv = 0
streaming_movies = 0
contract = 0
paperless_billing = 0
payment_method = 0

if st.button("Predict Churn"):

    features = np.array([[
        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone_service,
        multiple_lines,
        internet_service,
        online_security,
        online_backup,
        device_protection,
        tech_support,
        streaming_tv,
        streaming_movies,
        contract,
        paperless_billing,
        payment_method,
        monthly_charges,
        total_charges
    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")