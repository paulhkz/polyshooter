# Polyshooter

A simple Python-CLI hangman-like game to guess [Johnson-Solids](https://en.wikipedia.org/wiki/Johnson_solid).

## Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/paulhkz/polyshooter.git && cd polyshooter
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the game

```bash
python3 source/game.py
```

---

### Optional — tests / linting / type checking

```bash
python3 -m unittest discover tests/ # run tests
python3 -m coverage run --source=source -m unittest discover tests/ && python3 -m coverage html # coverage
pylint source/ # lint
mypy source/ # type check
```

Good luck & have fun.
