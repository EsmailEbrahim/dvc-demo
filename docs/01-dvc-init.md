# dvc init

Initialises DVC in the current repository.

```bash
dvc init
```

**What happens?**
- Creates a `.dvc/` directory with internal configuration.
- Adds `.dvc/.gitignore` to exclude cache and temp files.
- Commits `.dvc/` to Git (always commit `.dvc/`).

**Why commit immediately?**
So that collaborators have the same DVC setup when they clone the repo.
