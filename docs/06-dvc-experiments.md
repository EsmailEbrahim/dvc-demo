# dvc experiments

Run and compare multiple variations.

```bash
# Change a parameter (e.g., drop_na: false)
dvc exp run --set-param drop_na=false

# List experiments
dvc exp show

# Compare metrics and params
dvc exp show --metrics --params
```

**Example:** Compare rows count with and without dropping nulls.
