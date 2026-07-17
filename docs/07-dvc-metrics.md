# dvc metrics

Track metrics (e.g., model accuracy, row count).

```bash
# Show metrics
dvc metrics show

# Diff with previous version
dvc metrics diff

# Update metrics file
# The pipeline writes to metrics.json; DVC reads it.
```

**Tip:** Use `dvc metrics modify` to change which file contains metrics.
