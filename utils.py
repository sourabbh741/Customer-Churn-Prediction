import pickle
import pandas as pd
import streamlit as st


# ==========================================
# Load ML Model
# ==========================================

@st.cache_resource
def load_model():
    with open("models/best_logistic_regression.pkl", "rb") as file:
        model = pickle.load(file)
    return model


# ==========================================
# Load Label Encoders
# ==========================================

@st.cache_resource
def load_encoders():
    with open("models/label_encoders.pkl", "rb") as file:
        encoders = pickle.load(file)
    return encoders


# ==========================================
# Load Dataset
# ==========================================

@st.cache_data
def load_data():
    return pd.read_excel("data/Telco_customer_churn.xlsx")