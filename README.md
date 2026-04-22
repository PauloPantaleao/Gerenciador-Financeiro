# Finance Tracker

A command-line personal finance tracker built with Python as a study project. Tracks income and expenses, persists data with SQLite, and is structured around Object-Oriented Programming principles.

## About

This project was initially built using JSON for data persistence, then fully migrated to SQLite via Python's standard `sqlite3` library. The refactor also introduced OOP — replacing standalone functions with two classes: `Transacao` and `GerenciadorFinanceiro`.

It's part of a personal learning path covering Python fundamentals, data persistence, and software design.

## Features

- Add income (`receita`) and expense (`despesa`) transactions
- View a formatted summary of all transactions grouped by type
- Real-time balance calculation (total income − total expenses)
- Remove transactions by ID
- Input validation with clear error messages
- SQL injection prevention via parameterized queries

## Project Structure

```
Finance-Tracker/
├── db.py       # Transacao and GerenciadorFinanceiro classes
├── main.py     # CLI loop and user interaction
└── write.py    # Display utilities (title, line separator)
```

## How It Works

**`Transacao`** models a single financial record. It validates `tipo` (`"receita"` or `"despesa"`) and `valor` (must be positive) on creation, raising `ValueError` for invalid input. The database ID is assigned after persistence, not on construction.

**`GerenciadorFinanceiro`** manages the SQLite connection and exposes methods to add, list, delete, and calculate totals. The connection is opened once on instantiation and closed explicitly via `fechar()`.

## Requirements

- Python 3.10+
- No external dependencies — uses only the standard library (`sqlite3`, `time`)

## Running

```bash
python main.py
```

A `banco.db` file will be created automatically on first run.

## Concepts Practiced

- Object-Oriented Programming (classes, `__init__`, `__str__`, instance methods)
- SQLite with `sqlite3` (CRUD, parameterized queries, `lastrowid`)
- Input validation and exception handling
- Module separation and single responsibility
- Type hints
