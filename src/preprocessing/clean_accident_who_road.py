import pandas as pd

def clean_accident_who_road(df: pd.DataFrame) -> pd.DataFrame:
    """
    Phase 3 preprocessing — WHO Road Traffic Mortality

    Canonical selection:
    - Indicator: Estimated road traffic death rate
    - ValueType: numeric
    """

    df_clean = df.copy()

    df_clean = df_clean[
        df_clean["Indicator"].str.contains(
            "road traffic death rate", case=False, na=False
        )
        & (df_clean["ValueType"] == "numeric")
    ]

    df_clean = df_clean[
        ["SpatialDimValueCode", "Location", "Period", "FactValueNumeric"]
    ]

    df_clean = df_clean.rename(columns={
        "SpatialDimValueCode": "iso3",
        "Location": "country",
        "Period": "year",
        "FactValueNumeric": "accident_road_death_rate"
    })

    return df_clean
