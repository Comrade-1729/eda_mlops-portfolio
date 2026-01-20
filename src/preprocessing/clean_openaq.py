import pandas as pd

def clean_openaq(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean OpenAQ raw data and enforce India-only scope.

    Strategy:
    1. Detect country using 'Country Label' OR 'Country Code'
    2. If neither exists, assume dataset is already India-only
       (common for UI-filtered exports)

    This function NEVER guesses geography beyond these rules.
    """
    df = df.copy()

    # Normalize column lookup
    col_map = {c.lower(): c for c in df.columns}
    masks = []

    if "country label" in col_map:
        col = col_map["country label"]
        masks.append(
            df[col].astype(str).str.strip().str.lower().eq("india")
        )

    if "country code" in col_map:
        col = col_map["country code"]
        masks.append(
            df[col].astype(str).str.strip().str.upper().eq("IN")
        )

    if masks:
        return df[pd.concat(masks, axis=1).any(axis=1)].copy()

    # Fallback: assume pre-filtered India-only export
    return df
