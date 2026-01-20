# src/preprocessing/clean_who_ghe.py

import pandas as pd


def clean_who_ghe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean WHO GHE DALY dataset for analysis readiness.
    """

    df = df.copy()

    # Standardize column names
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )

    # Rename for clarity
    df = df.rename(columns={
        "dim_ghecause_code": "cause_code",
        "dim_ghecause_title": "cause",
        "val_daly_rate100k_numeric": "daly_rate_100k",
        "val_dths_rate100k_numeric": "death_rate_100k"
    })

    # Enforce numeric types
    df["daly_rate_100k"] = pd.to_numeric(df["daly_rate_100k"], errors="coerce")
    df["death_rate_100k"] = pd.to_numeric(df["death_rate_100k"], errors="coerce")
    df["year"] = df["year"].astype(int)

    EXPECTED_COLS = {
    "cause_code", "cause", "daly_rate_100k", "death_rate_100k", "year"
    }
    
    assert EXPECTED_COLS.issubset(df.columns)

    return df
