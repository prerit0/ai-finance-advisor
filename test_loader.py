from src.data.loader import load
from src.data.preprocessing import preprocess
from src.analysis.financial_metrics import financial_metrics
from src.visualization.charts import plot_category_spending, plot_monthly_spending, plot_income_vs_expenses


df = load("data/sample_expenses.csv")

df = preprocess(df)

metrics = financial_metrics(df)

fig1 = plot_category_spending(metrics["category_spending"])
fig2 = plot_monthly_spending(metrics["monthly_spending"])
fig3 = plot_income_vs_expenses(
    metrics["total_income"],
    metrics["total_expenses"]
)

import matplotlib.pyplot as plt
plt.show()