# Results and Demo Code

This page summarizes selected regression results and core demo code for the crypto policy, stablecoin exposure, and inflation project.

## Selected Regression Results

The preferred final model finds a negative and statistically significant association between lagged standardized stablecoin exposure and year-over-year CPI inflation.

| Model | Stablecoin exposure coefficient | t-statistic | Interpretation |
|---|---:|---:|---|
| Preferred final model | -1.966 | -2.897 | Lagged stablecoin exposure is negatively associated with inflation |
| All-mechanism robustness model | -1.733 | -2.294 | The result remains negative after adding the fiscal-monetary interaction |

## Policy Regime Heterogeneity

The regime interaction models suggest that the negative stablecoin exposure effect is mainly concentrated in Restricted countries.

| Reference group | Main effect | t-statistic | Interpretation |
|---|---:|---:|---|
| Restricted countries | -4.342 | -3.260 | Negative effect is strongest in Restricted countries |
| Legal relative to Restricted | 4.192 | 2.556 | Legal countries have a higher exposure effect relative to Restricted countries |
| Illegal relative to Restricted | 4.131 | 2.560 | Illegal countries also have a higher exposure effect relative to Restricted countries |

## Demo Code: Stablecoin Exposure Construction

```python
import numpy as np

# Scale Google Trends Bitcoin attention to a 0-1 range
panel["bitcoin_attention_scaled"] = panel["bitcoin_attention"] / 100

# Construct global USDT growth shock
panel["log_usdt_marketcap"] = np.log(panel["usdt_marketcap"])
panel["usdt_growth_shock"] = panel["log_usdt_marketcap"].diff()

# Construct country-month stablecoin exposure
panel["stablecoin_exposure"] = (
    panel["bitcoin_attention_scaled"] * panel["usdt_growth_shock"]
)

# Use lagged exposure in regressions
panel["stablecoin_exposure_l1"] = (
    panel.groupby("country")["stablecoin_exposure"].shift(1)
)
```

## Demo Code: Fixed-Effect Regression

```python
import statsmodels.formula.api as smf

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

model = smf.ols(formula=formula, data=panel_reg).fit(cov_type="HC3")

print(model.summary())
```
## Public Demo Data

The public repository does not include the private research dataset.  
Instead, I provide a synthetic country-month panel with the same variable structure as the research dataset.

The synthetic data are only used to demonstrate the code workflow.  
They should not be interpreted as real empirical evidence.

To run the demo:

```bash
python3 demo/generate_synthetic_data.py
python3 demo/run_demo_regression.py

## Code Structure

```text
notebooks/
├── 01_policy_data_construction.ipynb
├── 02_panel_construction.ipynb
├── 03_main_regressions.ipynb
├── 04_regime_heterogeneity.ipynb
```

## Reproducibility Notes

The public version of this project should include cleaned notebooks and documentation only. Private credentials, local file paths, and raw data files should not be uploaded.