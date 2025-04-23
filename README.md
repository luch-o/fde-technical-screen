# Package Sorter

A utility for sorting packages into different stacks based on dimensions and mass.

## Installation

```bash
# Clone the repository
git clone https://github.com/luch-o/fde-technical-screen.git
cd fde-technical-screen

# Install dependencies with Poetry
# If Poetry is not installed: pip install poetry
poetry install

# Activate the virtual environment
eval $(poetry env activate)
```

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v
```

## Using the CLI

```bash
# Sort a standard package
python cli.py --width 10.0 --height 10.0 --length 10 --mass 5.0

# Sort a special package (bulky by dimension)
python cli.py --width 150.0 --height 10.0 --length 10 --mass 5.0

# Sort a special package (heavy)
python cli.py --width 10.0 --height 10.0 --length 10 --mass 20.0

# Sort a rejected package (both bulky and heavy)
python cli.py --width 150.0 --height 10.0 --length 10 --mass 20.0
```
