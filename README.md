# Core-Rag

## Using uv (Python package manager)

The project is configured with `pyproject.toml` and works with `uv`.

### 1) Install uv

``` sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
`uv` will be installed at `/home/user/.local/bin`

To enable shell autocompletion for uv commands, run the following:

``` sh
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
```
Restart your shell for the changes to take effect.

### Create the environment and install deps
- First time setup: `uv sync`
  - Creates `.venv` file based on `uv.lock`.

### Add or remove dependencies
- Runtime deps: `uv add <package>`
- Dev-only deps: `uv add --group dev <package>`
- Remove: `uv remove <package>`

## Starting the app
### Setup `.env` file

``` sh
cp .env.example .env
```

### UI (Streamlit)

``` sh
cd streamlit && uv run streamlit run streamlit_app.py
```
### Backend

``` sh
uv run uvicorn src.api_server:app --host 127.0.0.1 --port 8002 --reload
```


## Pre-commit Hooks

Enable Git hooks to catch common issues before committing.

- Install hooks: `uv run pre-commit install`
- Run on all files (optional): `uv run pre-commit`

Configuration: `.pre-commit-config.yaml`. To upgrade hooks later, run
`uv run pre-commit autoupdate`.

## CI tasks (doit)

The workflow `.github/workflows/push-to-main.yml` runs checks.

- tests: `uv run doit test`
- coverage: `uv run doit coverage`
- mypy: `uv run doit mypy`

Run locally to mirror CI:
- Install dev tools: `uv sync --group dev`
- Run tests: `uv run doit test`
- Run mypy: `uv run mypy .`
- See coverage (90% threshold): `uv run doit coverage`
