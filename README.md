# CAGEDFEV2025

This repository contains a Jupyter notebook (`CAGEDFEV2025PANDAS.ipynb`) used to explore **`basefev25.db`**. The database holds labor market information, and the notebook demonstrates how to load, clean, and analyze the data using Pandas and SQLite.

## Prerequisites

- Python 3.8 or newer
- [pandas](https://pandas.pydata.org/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) (part of the Python standard library)
- Optional: [Jupyter](https://jupyter.org/) or Google Colab to run the notebook

Install Pandas with:

```bash
pip install pandas
```

## Opening the Notebook

1. Launch Jupyter Notebook or open the repository in Google Colab.
2. Open `CAGEDFEV2025PANDAS.ipynb`.
3. Set the `DB_PATH` variable to the location of your `basefev25.db` file. In Colab you might mount Google Drive and point `DB_PATH` to the file inside your drive:

```python
DB_PATH = '/content/drive/MyDrive/Files/basefev25.db'
```

Run the notebook cells to execute the analysis.

## Helper Functions

The file `db_utils.py` provides two helper functions used throughout the notebook:

- `connect(db_path)` – context manager that opens a SQLite connection and closes it automatically.
- `get_first_table_name(conn)` – retrieves the name of the first table in the database.

Using these utilities keeps the notebook code concise and ensures connections are properly closed.
