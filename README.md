Here’s a nicely formatted README in Markdown based on your instructions:

````markdown
# Python Version Setup

This guide walks you through setting up a Python project using `pyenv` and `poetry` with pre-configured development tools.

## Installation Steps

1. **Install `pyenv`**:
   ```bash
   curl https://pyenv.run | bash
   ```
````

2. **Configure Poetry to Use In-Project Virtual Environments**:

   ```bash
   poetry config virtualenvs.in-project true
   ```

3. **Install Python 3.8.15 Using `pyenv`**:

   ```bash
   pyenv install 3.8.15
   pyenv local 3.8.15
   pyenv exec poetry env use 3.8.15
   ```

4. **Initialize a New Poetry Project**:

   ```bash
   poetry init
   ```

5. **Activate the Virtual Environment**:

   ```bash
   poetry shell
   ```

6. **Add Development Dependencies**:
   ```bash
   poetry add black isort prettier pre-commit commitizen loguru pydantic --group dev
   ```

## Pre-commit Hook Configuration

Create a `.pre-commit-config.yaml` file with the following content:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-toml
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v4.0.0-alpha.8
    hooks:
      - id: prettier
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v3.29.0
    hooks:
      - id: commitizen
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        name: isort (python)
```

## Git Setup

1. **Initialize Git**:

   ```bash
   git init
   ```

2. **Configure Git User Information**:

   ```bash
   git config --global user.name "Troublesis"
   git config --global user.email "bamboo5320@gmail.com"
   ```

3. **Create a `.gitignore` File**:

   ```bash
   touch .gitignore
   ```

4. **Add a Remote Repository**:
   ```bash
   git remote add origin https://github.com/Troublesis/py_init.git
   ```

## Pre-commit Setup

1. **Install Pre-commit Hooks**:

   ```bash
   pre-commit install
   ```

2. **Update Pre-commit Hooks**:

   ```bash
   pre-commit autoupdate
   ```

3. **Run Pre-commit on All Files**:
   ```bash
   pre-commit run --all-files
   ```

## Commitizen Setup

1. **Initialize Commitizen**:

   ```bash
   cz init
   ```

2. **Add Changes to Git**:

   ```bash
   git add ./path/to/file
   ```

3. **Use Commitizen for Commit Messages**:
   ```bash
   cz commit
   ```
