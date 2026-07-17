import pandas as pd

df = pd.read_csv("data/raw/employees.csv")

df = df.dropna()

df.to_csv(
    "data/processed/employees_clean.csv",
    index=False
)
