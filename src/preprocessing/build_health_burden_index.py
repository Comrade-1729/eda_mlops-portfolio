import pandas as pd

def min_max_norm(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min())

def build_health_burden_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build Health Burden Index (HBI)
    Input:
        Processed WHO GHE DALY dataset
    Output:
        country-year health burden index (0–1)
    """
    df = df.copy()

    df["daly_norm"] = (
        df.groupby("year")["daly_rate_100k"]
        .transform(min_max_norm)
    )

    index_df = (
        df.groupby("year", as_index=False)["daly_norm"]
        .mean()
        .rename(columns={"daly_norm": "health_burden_index"})
    )

    index_df["country"] = "India"

    return index_df[["country", "year", "health_burden_index"]]
