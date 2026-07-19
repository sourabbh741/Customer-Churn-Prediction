import streamlit as st

# -----------------------------------------
# Page
# -----------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------------------
# Header
# -----------------------------------------

st.title("📊 Customer Churn Prediction Dashboard")

st.caption(
    "Machine Learning Dashboard for Telecom Customer Retention"
)

st.divider()

# -----------------------------------------
# KPI Cards
# -----------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "👥 Customers",
    "7,043"
)

c2.metric(
    "🎯 Accuracy",
    "80.55%"
)

c3.metric(
    "📈 F1 Score",
    "61.62%"
)

c4.metric(
    "🤖 Models Tested",
    "4"
)

st.divider()

# -----------------------------------------
# About
# -----------------------------------------

left, right = st.columns([2,1])

with left:

    st.subheader("🚀 Project Overview")

    st.write("""
This application predicts whether a telecom customer is likely to leave
(churn) using Machine Learning.

The project follows a complete end-to-end ML workflow:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Streamlit Deployment

The final model is a tuned **Logistic Regression** classifier trained on the IBM Telco Customer Churn dataset.
""")

with right:

    st.info("""
### Dataset

**IBM Telco Customer Churn**

Customers : 7043

Target :

Customer Churn
""")

st.divider()

# -----------------------------------------
# Workflow
# -----------------------------------------

st.subheader("🔄 Machine Learning Workflow")

w1, w2, w3, w4 = st.columns(4)

with w1:
    st.success("1️⃣\n\nData Collection")

with w2:
    st.info("2️⃣\n\nData Preprocessing")

with w3:
    st.warning("3️⃣\n\nModel Training")

with w4:
    st.success("4️⃣\n\nPrediction")

st.divider()

# -----------------------------------------
# Technologies
# -----------------------------------------

st.subheader("💻 Technologies Used")

t1, t2, t3 = st.columns(3)

with t1:

    st.markdown("""
### Programming

- Python
- Pandas
- NumPy
""")

with t2:

    st.markdown("""
### Machine Learning

- Scikit-Learn
- Logistic Regression
- Random Forest
- Gradient Boosting
""")

with t3:

    st.markdown("""
### Deployment

- Streamlit
- GitHub
- VS Code
""")

st.divider()

# -----------------------------------------
# Model Performance
# -----------------------------------------

st.subheader("📊 Model Performance")

performance = {
    "Model": [
        "Logistic Regression",
        "Gradient Boosting",
        "Random Forest",
        "Decision Tree"
    ],

    "Accuracy":[
        80.55,
        80.06,
        79.27,
        72.88
    ],

    "Precision":[
        64.70,
        65.34,
        63.66,
        48.93
    ],

    "Recall":[
        58.82,
        52.94,
        51.07,
        49.19
    ]
}

st.dataframe(
    performance,
    use_container_width=True
)

st.divider()

# -----------------------------------------
# Developer
# -----------------------------------------

st.subheader("👨‍💻 Developer")

st.success("""
**Sourabh Awasthi**

B.Tech Electronics & Communication Engineering

Machine Learning | AI | Data Analytics

Project:
Customer Churn Prediction using Machine Learning
""")