# dvc repro

Reproduce the pipeline from scratch.

```bash
dvc repro
```

- DVC checks hashes of dependencies.
- Only reruns stages where dependencies or code have changed.
- Saves results in `.dvc/cache/` and updates `dvc.lock`.

**Use case:** Reproduce results on any machine.
