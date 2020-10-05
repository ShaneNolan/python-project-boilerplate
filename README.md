# Python Project Boilerplate

## Version Management: pyenv

pyenv lets you easily switch between multiple versions of Python. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

### Installation

Remove any existing Python installations. Follow the below guides to install pyenv.

#### Unix

https://github.com/pyenv/pyenv

#### Windows

https://github.com/pyenv-win/pyenv-win

### Setup

```bash
pyenv install {python-version}

pyenv global {python-version}

pyenv rehash
```

### Testing

When you type python into the terminal it should come back with the Python version you requested.

```bash
python
```

## Packaging and Dependency Management: Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

### Installation

[https://python-poetry.org/docs/](https://python-poetry.org/docs/)

### Usage

[https://python-poetry.org/docs/basic-usage/](https://python-poetry.org/docs/basic-usage/)

#### Advanced Usage

[https://python-poetry.org/docs/cli/](https://python-poetry.org/docs/cli/)

## Coding Standards

### Formatting: Black

```bash
poetry add black --dev
```

### Linting: Flake8

```bash
poetry add flake8 flake8-bandit flake8-black flake8-bugbear --dev
```

## Static Typing

_Configuration file included in repo._

```bash
poetry add mypy --dev
```

## Testing

### Testing Framework: pytest

```bash
poetry add pytest pytest-cov pytest-xdist
```

### Automated Testing: nox

```bash
poetry add nox
```

#### Usage

[https://nox.thea.codes/en/stable/](https://nox.thea.codes/en/stable/)

## Documentation

### Documentation Generator: Sphinx

```bash
pip install sphinx sphinx_rtd_theme sphinx-autodoc-typehints
```

### Documentation Linting: Darglint

```bash
poetry add darglint
```

## VSCode Configuration

```json
{
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.formatting.provider": "black",
  "python.linting.pylintEnabled": false,
  "python.linting.enabled": true,
  "editor.formatOnSave": true,
  "python.linting.lintOnSave": true
}
```
