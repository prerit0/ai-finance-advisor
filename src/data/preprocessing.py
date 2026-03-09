import pandas as pd

def preprocess(df):
    """
    Clean and preprocess expense dataset
    """

    # Converting Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Ensuring Amount is numeric
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # Handling missing values
    df = df.dropna()

    # Standardizing text columns
    df["Category"] = df["Category"].str.strip().str.title()
    df["Type"] = df["Type"].str.strip().str.title()

    # Feature Engineering: extract month
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    return df
