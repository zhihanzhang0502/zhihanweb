import numpy as np
import pandas as pd

np.random.seed(42)

countries = [
    "Argentina", "Bangladesh", "Brazil", "Canada",
    "China", "El Salvador", "India", "Japan",
    "Nepal", "Singapore", "South Africa", "Switzerland",
    "Turkey", "UAE", "UK", "Vietnam"
]

regime_map = {
    "Argentina": "Restricted",
    "Bangladesh": "Illegal",
    "Brazil": "Legal",
    "Canada": "Legal",
    "China": "Illegal",
    "El Salvador": "Legal",
    "India": "Restricted",
    "Japan": "Legal",
    "Nepal": "Illegal",
    "Singapore": "Legal",
    "South Africa": "Legal",
    "Switzerland": "Legal",
    "Turkey": "Restricted",
    "UAE": "Restricted",
    "UK": "Legal",
    "Vietnam": "Restricted",
}

dates = pd.date_range("2019-01-01", "2025-12-01", freq="MS")

rows = []

for country in countries:
    country_effect = np.random.normal(0, 2)

    for date in dates:
        year = date.year
        calendar_month = date.month
        regime = regime_map[country]

        stablecoin_exposure_l1_z = np.random.normal()
        policy_restriction_intensity_l1_z = np.random.normal()
        dlog_exchange_rate_eop_l1_z = np.random.normal()
        fiscal_deficit_pct_gdp_l1_z = np.random.normal()
        unemployment_rate_l1_z = np.random.normal()
        current_account_deficit_pct_gdp_l1_z = np.random.normal()
        broad_money_growth_l1_z = np.random.normal()

        crypto_x_fx_z = stablecoin_exposure_l1_z * dlog_exchange_rate_eop_l1_z
        fx_x_ca_deficit_z = (
            dlog_exchange_rate_eop_l1_z
            * current_account_deficit_pct_gdp_l1_z
        )
        fiscal_x_m2_z = fiscal_deficit_pct_gdp_l1_z * broad_money_growth_l1_z

        # Synthetic data-generating process.
        # This is not the real research data.
        inflation_yoy = (
            6
            - 1.8 * stablecoin_exposure_l1_z
            - 0.7 * policy_restriction_intensity_l1_z
            + 0.4 * dlog_exchange_rate_eop_l1_z
            - 0.3 * fiscal_deficit_pct_gdp_l1_z
            + 1.2 * broad_money_growth_l1_z
            - 1.5 * crypto_x_fx_z
            + country_effect
            + np.random.normal(0, 2)
        )

        rows.append({
            "country": country,
            "date": date,
            "year": year,
            "calendar_month": calendar_month,
            "regime": regime,
            "inflation_yoy": inflation_yoy,
            "stablecoin_exposure_l1_z": stablecoin_exposure_l1_z,
            "policy_restriction_intensity_l1_z": policy_restriction_intensity_l1_z,
            "dlog_exchange_rate_eop_l1_z": dlog_exchange_rate_eop_l1_z,
            "fiscal_deficit_pct_gdp_l1_z": fiscal_deficit_pct_gdp_l1_z,
            "unemployment_rate_l1_z": unemployment_rate_l1_z,
            "current_account_deficit_pct_gdp_l1_z": current_account_deficit_pct_gdp_l1_z,
            "broad_money_growth_l1_z": broad_money_growth_l1_z,
            "crypto_x_fx_z": crypto_x_fx_z,
            "fx_x_ca_deficit_z": fx_x_ca_deficit_z,
            "fiscal_x_m2_z": fiscal_x_m2_z,
        })

df = pd.DataFrame(rows)

output_path = "data/synthetic_crypto_panel.csv"
df.to_csv(output_path, index=False)

print(f"Saved synthetic demo data to {output_path}")
print(df.head())