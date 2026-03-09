import pandas as pd 


def financial_metrics(df):
    """
    Calculating important financial statistics
    """

    income = df[df["Type"] == "Income"]["Amount"].sum()

    expenses = df[df["Type"] == "Expense"]["Amount"].sum()

    savings = income - expenses

    if income > 0:
        savings_rate = (savings / income) * 100
    else:
        savings_rate = 0

    # Top spending categories
    category_spending = (df[df["Type"] == "Expense"].groupby("Category")["Amount"].sum().sort_values(ascending=False))

    # Monthly spending
    monthly_spending = (df[df["Type"] == "Expense"].groupby("Month")["Amount"].sum())

    metrics = {
        "total_income": income,
        "total_expenses": expenses,
        "savings": savings,
        "savings_rate": savings_rate,
        "category_spending": category_spending,
        "monthly_spending": monthly_spending
    }

    return metrics