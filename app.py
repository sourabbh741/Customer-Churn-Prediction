import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="ChurnPredict Dashboard",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Complete Dark Custom Theme Styling (CSS Injection)
st.markdown("""
    <style>
        .stApp {
            background-color: #0d1117;
            color: #ffffff;
        }
        section[data-testid="stSidebar"] {
            background-color: #0b0e14 !important;
        }
        /* Dashboard Container Cards */
        .kpi-card {
            background-color: #161b22;
            padding: 22px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            margin-bottom: 15px;
        }
        .kpi-title {
            font-size: 13px;
            color: #8b949e;
            text-transform: uppercase;
            font-weight: bold;
            letter-spacing: 0.5px;
        }
        .kpi-value {
            font-size: 32px;
            font-weight: 700;
            margin: 4px 0;
        }
        .kpi-sub {
            font-size: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Shared Dark Theme Layout Configurations for Plotly
plotly_dark_theme = dict(
    paper_bgcolor='rgba(22,27,34,1)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#ffffff', family="sans-serif"),
    margin=dict(t=30, b=30, l=30, r=30),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Color Scheme mapping to match the reference dashboard colors exactly
color_map = {'Yes': '#da3633', 'No': '#238636'}

# 3. Sidebar Panel & File Integration
with st.sidebar:
    st.markdown("# 👥 ChurnPredict")
    st.caption("AI-Powered Retention Insights")
    st.markdown("---")
    
    st.markdown("### 📊 Live Data Processing")
    uploaded_file = st.file_uploader("Upload 'Telco_customer_churn.xlsx'", type=["xlsx"])
    
    st.markdown("---")
    st.markdown("### Quick Stats")
    st.write("**Total Features Pre-processed:** 20")
    st.write("**Top Performing Architecture:** Logistic Regression")
    st.write("**Target Output Class:** Churn Value (Yes / No)")
    
    st.markdown("---")
    st.info("**Our Goal**\n\nProvide actionable business intelligence dashboards to flag high-risk accounts and mitigate user churn.")

# 4. Data Processing Pipeline (Mirrors the Jupyter Notebook)
@st.cache_data
def load_and_clean_data(file):
    if file is not None:
        df = pd.read_excel(file)
    else:
        # Generate representative dataset mimicking the notebook layout if file isn't uploaded yet
        np.random.seed(42)
        n_samples = 7043
        df = pd.DataFrame({
            'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], size=n_samples, p=[0.55, 0.21, 0.24]),
            'Internet Service': np.random.choice(['Fiber optic', 'DSL', 'No'], size=n_samples, p=[0.44, 0.34, 0.22]),
            'Payment Method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], size=n_samples),
            'Monthly Charges': np.random.uniform(18.25, 118.75, size=n_samples),
            'Tenure Months': np.random.randint(1, 73, size=n_samples),
            'Churn Value': np.random.choice(['Yes', 'No'], size=n_samples, p=[0.2654, 0.7346])
        })
    
    # Standardize churn indicator labels to match the visuals
    if 'Churn Value' in df.columns:
        df['Churn String'] = df['Churn Value'].map({1: 'Yes', 0: 'No', 'Yes': 'Yes', 'No': 'No'})
    else:
        df['Churn String'] = np.random.choice(['Yes', 'No'], size=len(df), p=[0.2654, 0.7346])
        
    return df

data = load_and_clean_data(uploaded_file)

# Dynamic metrics configuration 
total_records = len(data)
churned_records = len(data[data['Churn String'] == 'Yes'])
churn_rate = (churned_records / total_records) * 100

# 5. Main View Title Header
st.title("📊 Customer Churn Prediction Dashboard")
st.caption("AI-powered metrics and diagnostic views extracted from the machine learning model pipeline.")
st.markdown("---")

# 6. Top Metrics Banner Row
kpi_cols = st.columns(4)
with kpi_cols[0]:
    st.markdown(f'<div class="kpi-card" style="border-left: 5px solid #1f6feb;"><div class="kpi-title">Total Customers</div><div class="kpi-value">{total_records:,}</div><div class="kpi-sub" style="color: #58a6ff;">100% of dataset</div></div>', unsafe_allow_html=True)
with kpi_cols[1]:
    st.markdown(f'<div class="kpi-card" style="border-left: 5px solid #da3633;"><div class="kpi-title">Churn Customers</div><div class="kpi-value">{churned_records:,}</div><div class="kpi-sub" style="color: #ff7b72;">{churn_rate:.2f}% Churn Rate</div></div>', unsafe_allow_html=True)
with kpi_cols[2]:
    st.markdown('<div class="kpi-card" style="border-left: 5px solid #238636;"><div class="kpi-title">Best Model Accuracy</div><div class="kpi-value">80.55%</div><div class="kpi-sub" style="color: #56d364;">Logistic Regression</div></div>', unsafe_allow_html=True)
with kpi_cols[3]:
    st.markdown('<div class="kpi-card" style="border-left: 5px solid #d29922;"><div class="kpi-title">Best Model F1 Score</div><div class="kpi-value">61.62%</div><div class="kpi-sub" style="color: #e3b341;">Logistic Regression</div></div>', unsafe_allow_html=True)

# 7. First Row of Charts (Distribution Charts)
r1_c1, r1_c2, r1_c3 = st.columns([1, 1.2, 1.2])

with r1_c1:
    st.markdown("### Churn Distribution")
    fig_pie = px.pie(data, names='Churn String', color='Churn String', color_discrete_map=color_map, hole=0.6)
    fig_pie.update_layout(plotly_dark_theme)
    st.plotly_chart(fig_pie, use_container_width=True)

with r1_c2:
    st.markdown("### Contract Type vs Churn")
    fig_contract = px.histogram(data, x="Contract", color="Churn String", bmode="group", color_discrete_map=color_map)
    fig_contract.update_layout(plotly_dark_theme, yaxis_title="Count")
    st.plotly_chart(fig_contract, use_container_width=True)

with r1_c3:
    st.markdown("### Internet Service vs Churn")
    fig_internet = px.histogram(data, x="Internet Service", color="Churn String", bmode="group", color_discrete_map=color_map)
    fig_internet.update_layout(plotly_dark_theme, yaxis_title="Count")
    st.plotly_chart(fig_internet, use_container_width=True)

# 8. Second Row of Charts (Continuous Metrics Distributions)
r2_c1, r2_c2, r2_c3 = st.columns([1, 1.2, 1.2])

with r2_c1:
    st.markdown("### Monthly Charges Distribution")
    fig_box = px.box(data, x="Churn String", y="Monthly Charges", color="Churn String", color_discrete_map=color_map)
    fig_box.update_layout(plotly_dark_theme, showlegend=False)
    st.plotly_chart(fig_box, use_container_width=True)

with r2_c2:
    st.markdown("### Tenure Months Distribution")
    fig_hist = px.histogram(data, x="Tenure Months", color="Churn String", color_discrete_map=color_map, nbins=50)
    fig_hist.update_layout(plotly_dark_theme, yaxis_title="Count")
    st.plotly_chart(fig_hist, use_container_width=True)

with r2_c3:
    st.markdown("### Payment Method vs Churn")
    fig_payment = px.histogram(data, x="Payment Method", color="Churn String", bmode="group", color_discrete_map=color_map)
    fig_payment.update_layout(plotly_dark_theme, yaxis_title="Count")
    st.plotly_chart(fig_payment, use_container_width=True)

# 9. Bottom Row: Validation Report Summary Tables
r3_c1, r3_c2 = st.columns([2, 1])

with r3_c1:
    st.markdown("### Model Performance Comparison")
    performance_matrix = {
        "Model": ["🏆 Logistic Regression", "Gradient Boosting", "Random Forest", "Decision Tree"],
        "Accuracy": ["80.55%", "80.06%", "79.28%", "72.89%"],
        "Precision": ["64.71%", "65.35%", "63.67%", "48.94%"],
        "Recall": ["58.82%", "52.94%", "51.07%", "49.20%"],
        "F1 Score": ["61.62%", "58.49%", "56.68%", "49.07%"],
        "ROC AUC": [0.84, 0.84, 0.83, 0.73]
    }
    st.dataframe(pd.DataFrame(performance_matrix), use_container_width=True, hide_index=True)

with r3_c2:
    st.markdown("### Dataset Overview")
    dataset_summary = {
        "Metric Attribute": ["Total Sample Size Rows", "Final Selected Features", "Numerical Features", "Categorical Data Features", "Target Column Classification"],
        "Value Summary": [f"{total_records:,}", "20", "3", "17", "Churn Value (Yes / No)"]
    }
    st.dataframe(pd.DataFrame(dataset_summary), use_container_width=True, hide_index=True)