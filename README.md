# Polyshooter

A simple Python-CLI hangman-like game to guess [Johnson-Solids](https://en.wikipedia.org/wiki/Johnson_solid).

- [Polyshooter](#polyshooter)
  - [Setup \& Run](#setup--run)
    - [1. Clone the repo](#1-clone-the-repo)
    - [2. Create virtual environment](#2-create-virtual-environment)
    - [3. Activate the virtual environment](#3-activate-the-virtual-environment)
    - [4. Install dependencies](#4-install-dependencies)
    - [5. Run the game](#5-run-the-game)
    - [Optional — tests / linting / type checking](#optional--tests--linting--type-checking)

## Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/paulhkz/polyshooter.git && cd polyshooter
```

### 2. Create virtual environment

```bash
python3.14 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip3.14 install -r requirements.txt
```

### 5. Run the game

```bash
python3.14 source/game.py
```

---

### Optional — tests / linting / type checking

```bash
python3.14 -m unittest discover tests/ # run tests
python3.14 -m coverage run --source=source -m unittest discover tests/ && python3.14 -m coverage html # coverage
pylint source/ # lint
mypy . # type check
```

Good luck & have fun.
