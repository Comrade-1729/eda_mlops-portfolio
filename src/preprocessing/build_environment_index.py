import pandas as pd

POLLUTANTS = ["pm2.5", "pm10", "no2", "so2", "o3"]

def min_max_norm(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min())

def build_environment_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build Environmental Stress Index (ESI)
    Input:
        df: cleaned OpenAQ data (India-only)
    Output:
        country-year Environmental Stress Index (0–1)
    """
    df = df.copy()
    df["year"] = df["last_updated"].dt.year

    # Median pollutant concentration per year
    pollutant_year = (
        df[df["pollutant"].isin(POLLUTANTS)]
        .groupby(["country_label", "year", "pollutant"])["value"]
        .median()
        .reset_index()
    )

    pivot = pollutant_year.pivot_table(
        index=["country_label", "year"],
        columns="pollutant",
        values="value"
    ).reset_index()

    for p in POLLUTANTS:
        if p in pivot.columns:
            pivot[f"{p}_norm"] = min_max_norm(pivot[p])

    norm_cols = [f"{p}_norm" for p in POLLUTANTS if f"{p}_norm" in pivot.columns]

    pivot["environment_stress_index"] = pivot[norm_cols].mean(axis=1)

    return pivot[
        ["country_label", "year", "environment_stress_index"]
    ].rename(columns={"country_label": "country"})
