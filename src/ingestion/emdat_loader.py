from pathlib import Path
import pandas as pd

def load_emdat_disasters(path: Path) -> pd.DataFrame:
    """
    Load EM-DAT Natural Disaster dataset (RAW).
    - Event-level records
    - No transformations
    - No cleaning
    NOTE:
        This loader is Phase-1 locked.
        No filtering or schema normalization is allowed here.
    """
    if not path.exists():
        raise FileNotFoundError(f"EM-DAT file not found: {path}")
    
    df = pd.read_excel(path)
    return df
