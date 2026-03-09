from src.data.loader import load
from src.data.preprocessing import preprocess
from src.analysis.financial_metrics import financial_metrics
from src.visualization.charts import plot_category_spending, plot_monthly_spending, plot_income_vs_expenses
from src.ai.advisor_model import FinancialAdvisor

df = load("data/sample_expenses.csv")

df = preprocess(df)

metrics = financial_metrics(df)

advisor = FinancialAdvisor()

advice = advisor.generate_advice(metrics)

print("\nAI Financial Advice:\n")
print(advice)