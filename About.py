import streamlit as st

st.title("ℹ️ About This Project")

st.markdown("""
# Customer Churn Prediction using Machine Learning

This project predicts whether a telecom customer is likely to leave (churn)
based on customer demographics, services, billing information, and contract details.

The application was developed using Python, Scikit-Learn, and Streamlit as an
end-to-end Machine Learning deployment project.
""")

st.divider()

# ---------------------------------------------------

st.header("📂 Dataset")

st.write("""
**Dataset:** IBM Telco Customer Churn

- Total Customers : 7043
- Features : 20
- Target Variable : Churn Value
- Missing Values handled
- Duplicate Values removed
""")

st.divider()

# ---------------------------------------------------

st.header("⚙️ Machine Learning Pipeline")

st.markdown("""

1. Data Collection

2. Data Cleaning

3. Missing Value Handling

4. Exploratory Data Analysis

5. Feature Engineering

6. Label Encoding

7. Train-Test Split

8. Model Training

9. Model Evaluation

10. Streamlit Deployment

""")

st.divider()

# ---------------------------------------------------

st.header("🤖 Models Evaluated")

st.table({

"Model":[

"Logistic Regression",

"Gradient Boosting",

"Random Forest",

"Decision Tree"

],

"Accuracy":[

"80.55%",

"80.06%",

"79.28%",

"72.89%"

]

})

st.divider()

# ---------------------------------------------------

st.header("📊 Evaluation Metrics")

st.markdown("""

The following metrics were used to compare the models:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve

""")

st.divider()

# ---------------------------------------------------

st.header("🛠️ Technologies")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""

Python

Pandas

NumPy

""")

with c2:

    st.info("""

Scikit-Learn

Logistic Regression

Random Forest

Gradient Boosting

""")

with c3:

    st.warning("""

Streamlit

VS Code

GitHub

""")

st.divider()

# ---------------------------------------------------

st.header("🚀 Future Improvements")

st.markdown("""

- XGBoost Model

- LightGBM

- SHAP Explainability

- Customer Segmentation

- Real-Time Prediction API

- Cloud Deployment

""")

st.divider()

# ---------------------------------------------------

st.header("👨‍💻 Developer")

st.success("""

Sourabh Awasthi

B.Tech Electronics & Communication Engineering

Machine Learning • Data Analytics • AI

End-to-End Customer Churn Prediction Project

""")