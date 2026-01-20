from pathlib import Path
import pandas as pd

def load_who_road_mortality(path: Path) -> pd.DataFrame:
    """
    Load WHO Road Traffic Mortality dataset (RAW).
    - No cleaning
    - No aggregation
    - No renaming
    NOTE:
        This loader is Phase-1 locked.
        No filtering or schema normalization is allowed here.
    """
    if not path.exists():
        raise FileNotFoundError(f"WHO road mortality file not found: {path}")
    
    df = pd.read_csv(path)
    return df
