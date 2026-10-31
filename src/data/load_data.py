"""Load and concatenate raw insurance review spreadsheets."""
from pathlib import Path
import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_reviews(raw_dir=RAW_DIR):
    files = sorted(Path(raw_dir).glob("*.xlsx"))
    if not files:
        raise FileNotFoundError(f"No Excel files in {raw_dir}; see README for dataset setup")
    return pd.concat((pd.read_excel(p) for p in files), ignore_index=True)
