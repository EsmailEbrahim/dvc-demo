import yaml
import pandas as pd

params = yaml.safe_load(open("params.yaml"))

df = pd.read_csv("data/raw/employees.csv")

if params["drop_na"]:
    df = df.dropna()

df.to_csv(
    "data/processed/employees_clean.csv",
    index=False
)
