# Nostra Assessment

To run the code for question 2, 3 and 5, run tests in `tests/test_data_processing.py` and `tests/test_visualize.py`

## Project setup

### Install Pyenv and Python 3

```bash
brew update
```
```bash
brew install pyenv
```
```bash
pyenv install 3.9.11
```

### Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Create virtual environment

```bash
poetry env use ~/.pyenv/versions/3.9.11/bin/python
```
```bash
poetry install
```

### Set Python Interpreter (Pycharm)

1. Navigate `Settings` -> `Project Interpreter`
2. Click `Add Interpreter`
3. Click `Add Local Interpreter...`
4. Select `Virtual Environment` on the left
5. If not already selected, select `Existing` for Environment
6. The `Interpreter` path should be pointing to the `.venv` directory in the project
7. Click `Ok` twice to exit

If you've made it this far, you're ready to go!



