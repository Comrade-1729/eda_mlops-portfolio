import pandas as pd

def clean_disaster_emdat(df: pd.DataFrame) -> pd.DataFrame:
    """
    Phase 3 preprocessing — EM-DAT Natural Disasters

    Design choice:
    - Event-level retained
    - Country-year aggregation deferred to Phase 4
    """

    df_clean = df.copy()

    df_clean = df_clean[
        df_clean["ISO"].notna()
        & df_clean["Start Year"].notna()
    ]

    df_clean = df_clean[
        [
            "DisNo.", "ISO", "Country",
            "Disaster Group", "Disaster Type",
            "Start Year", "Total Deaths", "Total Affected"
        ]
    ]

    df_clean = df_clean.rename(columns={
        "DisNo.": "event_id",
        "ISO": "iso3",
        "Country": "country",
        "Start Year": "year",
        "Total Deaths": "disaster_deaths",
        "Total Affected": "disaster_affected"
    })

    return df_clean
