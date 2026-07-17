import pickle
import pandas as pd

df = pd.read_csv(
    "data/processed/employees_clean.csv"
)

model = {
    "rows": len(df)
}

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)
