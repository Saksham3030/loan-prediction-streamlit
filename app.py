import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("model/loan_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.title("Loan Prediction App")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicantincome = st.number_input("Applicant Income", min_value=0)
coapplicantincome = st.number_input("Coapplicant Income", min_value=0)
loanamount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term", min_value=0)
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Predict
if st.button("Predict"):

    data = pd.DataFrame({
        "gender": [1 if gender == "Male" else 0],
        "married": [1 if married == "Yes" else 0],
        "dependents": [{"0":0,"1":1,"2":2,"3+":3}[dependents]],
        "education": [1 if education == "Graduate" else 0],
        "self_employed": [1 if self_employed == "Yes" else 0],
        "applicantincome": [applicantincome],
        "coapplicantincome": [coapplicantincome],
        "loanamount": [loanamount],
        "loan_amount_term": [loan_amount_term],
        "credit_history": [credit_history],
        "property_area": [{"Rural":0,"Semiurban":1,"Urban":2}[property_area]]
    })

    # Feature Engineering
    data["total_income"] = data["applicantincome"] + data["coapplicantincome"]
    data["loanamount_log"] = np.log1p(data["loanamount"])
    data["total_income_log"] = np.log1p(data["total_income"])

    data = scaler.transform(data)

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")