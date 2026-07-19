import streamlit as st
import plotly.express as px
from utils import load_data

# =========================================
# Load Dataset
# =========================================

df = load_data()

st.title("📊 Customer Insights Dashboard")

st.markdown("""
Explore customer behavior and churn patterns through interactive visualizations.
""")

st.divider()

# =========================================
# Churn Distribution
# =========================================

st.subheader("Customer Churn Distribution")

fig = px.pie(
    df,
    names="Churn Label",
    hole=0.5,
    color="Churn Label",
    color_discrete_sequence=["#2E86DE", "#E74C3C"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================================
# Contract vs Churn
# =========================================

st.subheader("Contract Type vs Churn")

fig = px.histogram(
    df,
    x="Contract",
    color="Churn Label",
    barmode="group",
    color_discrete_sequence=["#2E86DE", "#E74C3C"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================================
# Internet Service
# =========================================

st.subheader("Internet Service vs Churn")

fig = px.histogram(
    df,
    x="Internet Service",
    color="Churn Label",
    barmode="group",
    color_discrete_sequence=["#2E86DE", "#E74C3C"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================================
# Monthly Charges
# =========================================

st.subheader("Monthly Charges Distribution")

fig = px.box(
    df,
    x="Churn Label",
    y="Monthly Charges",
    color="Churn Label",
    color_discrete_sequence=["#2E86DE", "#E74C3C"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================================
# Tenure
# =========================================

st.subheader("Tenure Distribution")

fig = px.histogram(
    df,
    x="Tenure Months",
    color="Churn Label",
    nbins=25,
    color_discrete_sequence=["#2E86DE", "#E74C3C"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================================
# Payment Method
# =========================================

st.subheader("Payment Method")

fig = px.histogram(
    df,
    x="Payment Method",
    color="Churn Label",
    barmode="group",
    color_discrete_sequence=["#2E86DE", "#E74C3C"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================================
# Correlation
# =========================================

st.subheader("Numeric Feature Correlation")

corr = df.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Blues"
)

st.plotly_chart(fig, use_container_width=True)

# =========================================
# Dataset Preview
# =========================================

st.subheader("Dataset Preview")

st.dataframe(df.head(), use_container_width=True)