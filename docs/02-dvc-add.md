# dvc add

Track a data file or directory with DVC.

```bash
dvc add data/raw/employees.csv
```

**What happens?**
- Creates `data/raw/employees.csv.dvc` – a metadata file.
- Adds `data/raw/employees.csv` to `.gitignore`.
- Stores the file hash and size in the `.dvc/cache/`.

**Result:** The actual data is **not** committed to Git; only the small `.dvc` file is versioned.
