from pathlib import Path
import pandas as pd

def load_wdi_bulk(path: Path) -> pd.DataFrame:
    """
    Load World Bank WDI bulk CSV (wide format).
    No cleaning. No reshaping.
    """
    return pd.read_csv(path, engine="python", low_memory=False)
