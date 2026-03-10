import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.data.loader import load
from src.data.preprocessing import preprocess
from src.analysis.financial_metrics import financial_metrics
from src.visualization.charts import plot_category_spending, plot_monthly_spending, plot_income_vs_expenses
from src.ai.advisor_model import FinancialAdvisor


st.title("AI Personal Finance Advisor")

st.write("Upload your expense dataset to get financial insights and AI advice.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])


if uploaded_file is not None:

    df = load(uploaded_file)

    df = preprocess(df)

    metrics = financial_metrics(df)

    st.subheader("Financial Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Income", f"{metrics['total_income']}")
    col2.metric("Total Expenses", f"{metrics['total_expenses']}")
    col3.metric("Savings", f"{metrics['savings']}")
    col4.metric("Savings Rate", f"{metrics['savings_rate']:.2f}%")

    st.subheader("Spending by Category")

    fig1 = plot_category_spending(metrics["category_spending"])
    st.pyplot(fig1)

    st.subheader("Monthly Spending")

    fig2 = plot_monthly_spending(metrics["monthly_spending"])
    st.pyplot(fig2)

    st.subheader("Income vs Expenses")

    fig3 = plot_income_vs_expenses(
        metrics["total_income"],
        metrics["total_expenses"]
    )

    st.pyplot(fig3)

    st.subheader("AI Financial Advice")

    advisor = FinancialAdvisor()

    advice = advisor.generate_advice(metrics)

    st.success(advice)