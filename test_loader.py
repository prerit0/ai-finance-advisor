from src.data.loader import load 
from src.data.preprocessing import preprocess 
df = load(r'C:\prerit\Projects\ai-finance-advisor\data\sample_expenses.csv')

df_clean = preprocess(df)

print(df_clean.head())