import pandas as pd

def build_disaster_exposure(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate EM-DAT disasters to country–year exposure metrics
    """
    df = df.copy()

    agg = (
        df.groupby(["iso3", "country", "year"])
        .agg(
            disaster_event_count=("event_id", "count"),
            disaster_deaths=("disaster_deaths", "sum"),
            disaster_affected=("disaster_affected", "sum")
        )
        .reset_index()
    )

    return agg
