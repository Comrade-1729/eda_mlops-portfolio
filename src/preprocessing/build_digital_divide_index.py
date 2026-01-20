import pandas as pd

WEIGHTS = {
    "internet_users_pct": 0.4,
    "gdp_per_capita_usd": 0.4,
    "secondary_enrollment_pct": 0.2
}

def min_max_norm(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min())

def build_digital_divide_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build Digital Divide Index (DDI)
    """
    df = df.copy()

    for col in WEIGHTS:
        df[f"{col}_norm"] = min_max_norm(df[col])

    df["digital_divide_index"] = sum(
        df[f"{col}_norm"] * w
        for col, w in WEIGHTS.items()
    )

    return df[
        ["country", "country_code", "year", "digital_divide_index"]
    ]
