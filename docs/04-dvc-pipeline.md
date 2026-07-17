# dvc pipeline

Define a pipeline in `dvc.yaml` with stages.

```yaml
stages:
  preprocess:
    cmd: python src/preprocess.py
    deps:
      - data/raw/employees.csv
      - src/preprocess.py
    outs:
      - data/processed/employees_clean.csv
  train:
    cmd: python src/train.py
    deps:
      - data/processed/employees_clean.csv
      - src/train.py
    outs:
      - models/model.pkl
```

- `deps` – files that the stage depends on.
- `outs` – files the stage produces.

Visualise the pipeline with `dvc dag`.
