import pandas as pd

INDICATOR_MAP = {
    "Individuals using the Internet (% of population)": "internet_users_pct",
    "GDP per capita (current US$)": "gdp_per_capita_usd",
    "Population, total": "population_total",
    "School enrollment, secondary (% gross)": "secondary_enrollment_pct"
}

def clean_wdi(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and reshape World Bank WDI data.

    Output schema:
    - country
    - country_code
    - year
    - gdp_per_capita_usd
    - internet_users_pct
    - population_total
    - secondary_enrollment_pct
    - gdp_total_usd

    Notes:
    - No imputation
    - Missing values preserved
    - GDP total is a transparent derived approximation
    """

    required_cols = {"Country Name", "Country Code", "Series Name", "Series Code"}
    missing = required_cols - set(df_raw.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Keep only valid ISO-3 country codes (drops regions & aggregates)
    df_raw = df_raw[df_raw["Country Code"].str.len() == 3].copy()

    id_cols = ["Country Name", "Country Code", "Series Name", "Series Code"]
    year_cols = [c for c in df_raw.columns if c.endswith("]")]

    # Wide → Long
    df_long = df_raw.melt(
        id_vars=id_cols,
        value_vars=year_cols,
        var_name="year_raw",
        value_name="value"
    )

    # Parse year
    df_long["year"] = (
        df_long["year_raw"]
        .str.extract(r"(\d{4})")
        .astype(int)
    )

    # Numeric enforcement
    df_long["value"] = pd.to_numeric(df_long["value"], errors="coerce")

    # Indicator normalization
    df_long["indicator"] = df_long["Series Name"].map(INDICATOR_MAP)
    df_long = df_long[df_long["indicator"].notna()].copy()

    # Pivot to analytical table
    df_pivot = (
        df_long
        .pivot_table(
            index=["Country Name", "Country Code", "year"],
            columns="indicator",
            values="value"
        )
        .reset_index()
    )

    # Derived GDP (explicitly approximate)
    df_pivot["gdp_total_usd"] = (
        df_pivot["gdp_per_capita_usd"] * df_pivot["population_total"]
    )

    return df_pivot.rename(columns={
        "Country Name": "country",
        "Country Code": "country_code"
    })
