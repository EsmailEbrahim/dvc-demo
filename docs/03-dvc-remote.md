# dvc remote

Set up a remote storage to share data.

```bash
# Local remote (for demo)
dvc remote add -d local /tmp/dvc-storage

# Or S3:
dvc remote add -d s3 mybucket/dvc-store

# Push data to remote
dvc push
```

**Why?** Collaborators can then `dvc pull` to get the data.
