import pandas as pd

def clean_crime_unodc(df: pd.DataFrame) -> pd.DataFrame:
    """
    Phase 3 preprocessing — UNODC Intentional Homicide

    Canonical selection:
    - Indicator: Intentional homicide victims
    - Sex: Total
    - Age: Total
    - Unit: Rate per 100,000 population
    """

    df_clean = df.copy()

    df_clean = df_clean[
        df_clean["Indicator"].str.contains(
            "Intentional homicide", case=False, na=False
        )
        & (df_clean["Sex"] == "Total")
        & (df_clean["Age"] == "Total")
        & df_clean["Unit of measurement"].str.contains(
            "Rate", case=False, na=False
        )
    ]

    df_clean = df_clean[
        ["Iso3_code", "Country", "Region", "Subregion", "Year", "VALUE"]
    ]

    df_clean = df_clean.rename(columns={
        "Iso3_code": "iso3",
        "Country": "country",
        "Year": "year",
        "VALUE": "crime_homicide_rate"
    })

    return df_clean
