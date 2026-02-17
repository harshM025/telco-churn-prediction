import streamlit as st
import pickle
import pandas as pd

# Load artifacts
model = pickle.load(open("models/churn_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
feature_columns = pickle.load(open("models/feature_columns.pkl", "rb"))

st.set_page_config(page_title="Telco Churn Prediction")

st.title("📊 Telco Customer Churn Prediction")

st.sidebar.header("Customer Information")

# ---------------- DEMOGRAPHIC ----------------
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])

# ---------------- PHONE ----------------
phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

# ---------------- INTERNET ----------------
internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.sidebar.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.sidebar.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.sidebar.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.sidebar.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.sidebar.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

# ---------------- CONTRACT & BILLING ----------------
contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# ---------------- NUMERIC ----------------
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 1000.0)

# ---------------- PREDICT ----------------
if st.sidebar.button("Predict Churn"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    # One-hot encode
    input_encoded = pd.get_dummies(input_data)

    # Match training columns
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

    # Scale
    input_scaled = scaler.transform(input_encoded)

    # Predict probability
    prob = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")
    st.metric("Churn Probability", f"{prob:.2%}")

    if prob >= 0.60:
        st.error("🔴 High Risk Customer")
        st.write("Recommended Action: Offer premium retention plan.")
    elif prob >= 0.35:
        st.warning("🟡 Medium Risk Customer")
        st.write("Recommended Action: Offer targeted discount or contract upgrade.")
    else:
        st.success("🟢 Low Risk Customer")
        st.write("No immediate retention action required.")
