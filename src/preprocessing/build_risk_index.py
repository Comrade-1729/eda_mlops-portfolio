import pandas as pd

def min_max_norm(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min())

def build_risk_index(
    df: pd.DataFrame,
    cols: list[str]
) -> pd.DataFrame:
    """
    Build Composite Risk Exposure Index (REI)
    """
    df = df.copy()

    for col in cols:
        df[f"{col}_norm"] = (
            df.groupby("year")[col]
            .transform(min_max_norm)
        )

    df["risk_exposure_index"] = df[
        [f"{c}_norm" for c in cols]
    ].mean(axis=1)

    return df[
        ["iso3", "country", "year", "risk_exposure_index"]
    ]
