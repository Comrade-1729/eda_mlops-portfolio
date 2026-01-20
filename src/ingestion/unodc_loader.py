from pathlib import Path
import pandas as pd

def load_unodc_homicide(path: Path) -> pd.DataFrame:
    """
    Load UNODC Intentional Homicide dataset (RAW).
    - No renaming
    - No filtering
    - No cleaning
    NOTE:
        This loader is Phase-1 locked.
        No filtering or schema normalization is allowed here.
    """
    if not path.exists():
        raise FileNotFoundError(f"UNODC file not found: {path}")
    
    df = pd.read_excel(path)
    return df
