# Python Project Boilerplate

# Setup

Rename src/project_name to whatever the the project is called.

You can run `python auto_setup.py` once you have pyenv and a Python version installed.

## Versioning

**Unix**:
https://github.com/pyenv/pyenv

**Windows**:
https://github.com/pyenv-win/pyenv-win

## Virtual Environment

```bash
python -m venv venv
```

## Formatting

```bash
pip install black
```

## Linting

_Configuration file included in repo._

```bash
pip install flake8 flake8-bandit flake8-black flake8-bugbear
```

## Static Typing

_Configuration file included in repo._

```bash
pip install mypy
```

## Testing

```bash
pip install pytest pytest-cov
```

## Automated Testing

```bash
pip install nox
```

## Documentation

```bash
pip install sphinx sphinx_rtd_theme sphinx-autodoc-typehints
```

## Documentation Linting

```bash
pip install darglint
```
