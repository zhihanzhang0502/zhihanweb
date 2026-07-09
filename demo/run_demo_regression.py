import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("data/synthetic_crypto_panel.csv")

formula = """
inflation_yoy ~
    stablecoin_exposure_l1_z
    + policy_restriction_intensity_l1_z
    + dlog_exchange_rate_eop_l1_z
    + fiscal_deficit_pct_gdp_l1_z
    + unemployment_rate_l1_z
    + current_account_deficit_pct_gdp_l1_z
    + broad_money_growth_l1_z
    + crypto_x_fx_z
    + fx_x_ca_deficit_z
    + C(country)
    + C(year)
    + C(calendar_month)
"""

model = smf.ols(formula=formula, data=df).fit(cov_type="HC3")

print(model.summary())