# DVC Demo

A **minimal but complete** example of Data Version Control (DVC) core features:

- **Data versioning** – track datasets without storing them in Git.
- **Pipelines** – define and reproduce ML workflows.
- **Metrics & parameters** – track model performance and hyperparameters.
- **Experiments** – run and compare different versions.

---

## Prerequisites

- Python 3.8+
- Git
- DVC (install with `pip install dvc` or via your package manager)

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/EsmailEbrahim/dvc-demo.git
cd dvc-demo

# Install Python dependencies
pip install -r requirements.txt

# Pull the data from DVC remote (if configured)
dvc pull          # or manually set remote first

# Reproduce the pipeline
dvc repro
```

---

## What's Inside

### Data
- `data/raw/employees.csv` – raw dataset with missing values.
- `data/processed/employees_clean.csv` – cleaned dataset (produced by pipeline).

### Pipeline
- **preprocess** – reads `employees.csv`, drops rows with missing salary (controlled by `params.yaml`), saves `employees_clean.csv`.
- **train** – reads cleaned data, counts rows, and saves a pickle model with that count.

### Parameters
- `params.yaml` – currently `drop_na: true`.

### Metrics
- `metrics.json` – contains the number of rows in the cleaned data.

---

## Key DVC Commands

| Command | Description |
|---------|-------------|
| `dvc init` | Initialise DVC in the repo. |
| `dvc add data/raw/employees.csv` | Track raw data. |
| `dvc remote add -d local /path/to/store` | Set up a remote for data. |
| `dvc push` / `dvc pull` | Sync data with remote. |
| `dvc repro` | Reproduce the pipeline. |
| `dvc metrics show` | View metrics. |
| `dvc params diff` | See changes in parameters. |
| `dvc exp run` | Run an experiment. |
| `dvc exp show` | List experiments. |

---

## Try It Yourself

### 1. Change a parameter
Edit `params.yaml` to set `drop_na: false`, then run:
```bash
dvc repro
dvc metrics show   # now rows = 7 (keeps Omar with missing salary)
```

### 2. Experiment with different parameters
```bash
dvc exp run --set-param drop_na=false
dvc exp show --metrics --params
```

### 3. Compare metrics between experiments
```bash
dvc exp diff
```

---

## Remote Storage (Optional)

To share data with collaborators, set up a remote:

```bash
# Local example
mkdir -p /tmp/dvc-storage
dvc remote add -d local /tmp/dvc-storage
dvc push
```

For cloud storage, replace `local` with `s3`, `gs`, `azure`, etc.

---

## Files You Should *Not* Commit

- `.dvc/cache/` – holds all data versions.
- `.dvc/tmp/` – temporary files.
- `data/raw/employees.csv` – tracked by DVC.
- `data/processed/employees_clean.csv` – tracked by DVC.
- `models/model.pkl` – tracked by DVC.

They are already in `.gitignore`.

---

## Further Reading

- [DVC Official Docs](https://dvc.org/doc)
- [Get Started Guide](https://dvc.org/doc/start)

---

## License

MIT – see [LICENSE](LICENSE).

---

## Author
- [Esmail Ebrahim Hamza - إسماعيل إبراهيم حمزة](https://github.com/EsmailEbrahim)
