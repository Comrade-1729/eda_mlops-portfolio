from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATASETS_DIR = PROJECT_ROOT / "datasets"

def load_data(subdir: str, filename: str) -> pd.DataFrame:
    """
    Load CSV from datasets/ directory.

    - Automatically handles comma vs semicolon delimiters
    - Skips malformed rows (common in OpenAQ exports)
    - Centralized ingestion contract (DO NOT fix in notebooks)
    """
    path = DATASETS_DIR / subdir / filename

    # First attempt: standard CSV
    try:
        return pd.read_csv(path)
    except pd.errors.ParserError:
        # Fallback: semicolon-delimited (OpenAQ UI exports)
        return pd.read_csv(
            path,
            sep=";",
            engine="python",
            on_bad_lines="skip"
        )
