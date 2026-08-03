# Research Details

## Input Data

| Variable or component | Source | Construction and role |
|---|---|---|
| `inflation_yoy` | IMF CPI data | Year-over-year CPI inflation; main dependent variable |
| `btc_attention` | Google Trends | Country-level Bitcoin search attention used as a proxy for local cryptocurrency exposure |
| `dlog_usdt_marketcap` | CoinMetrics | Monthly log growth in global USDT market capitalization |
| Crypto-policy titles | GDELT 2.0 GKG via Google BigQuery | Country-month policy-news titles used to construct policy attention and restrictiveness measures |
| `dlog_exchange_rate_eop` | IMF exchange-rate data | Monthly log change in the end-of-period exchange rate |
| `net_lending_borrowing_pct_gdp` | IMF fiscal data | Transformed into a fiscal-deficit measure, with larger positive values representing larger deficits |
| `broad_money_growth` | World Bank / IMF | Monetary expansion control |
| `unemployment_rate` | World Bank / IMF | Labor-market control |
| `current_account_pct_gdp` | World Bank / IMF | Transformed into a current-account-deficit measure |
| `baseline_crypto_status` | Research classification | Long-run classification of countries as Legal, Restricted, or Illegal |

## Sample Construction

| Sample | Coverage |
|---|---|
| Balanced merged panel | 18 countries, January 2019-December 2025 |
| Total balanced observations | 1,512 country-month observations |
| Preferred regression sample | 626 complete-case observations across 11 countries |
| Frequency | Monthly |

## Policy Variable Construction

The GDELT policy pipeline first identifies article titles containing:

- A cryptocurrency-related term.
- A policy-related term.
- A country name or country alias.

Duplicate country-month titles are removed. Each remaining title is classified as restrictive, supportive, or neutral using a predefined title-level dictionary.

| Policy variable | Construction |
|---|---|
| `policy_attention` | $\log(1 + \text{number of unique policy titles})$ |
| `avg_restrictiveness` | Average title-level restrictiveness score |
| `restrictive_policy_dummy` | Equals 1 when at least one restrictive title appears in a country-month |
| `restrictive_intensity` | `avg_restrictiveness × policy_attention` |
| `restrictive_count` | Number of titles classified as restrictive |
| `supportive_count` | Number of titles classified as supportive |

## Stablecoin Exposure Measure

The central explanatory variable combines a global stablecoin shock with local cryptocurrency attention:

$$
Exposure_{i,t-1}
=
\left(
\frac{BitcoinAttention_{i,t-1}}{100}
\right)
\times
\Delta \log(USDTMarketCap_{t-1})
$$

The exposure measure is standardized before entering the preferred regression.

A higher value indicates that a country has both relatively high local cryptocurrency attention and greater exposure to a contemporaneous global expansion in USDT market capitalization.

## Model

The preferred specification is:

$$
\begin{aligned}
Inflation_{i,t}
=&\ \beta_1 Exposure^{z}_{i,t-1}
+ \beta_2 PolicyIntensity^{z}_{i,t-1}
+ \beta_3 FXChange^{z}_{i,t-1} \\
&+ \beta_4 FiscalDeficit^{z}_{i,t-1}
+ \beta_5 Unemployment^{z}_{i,t-1}
+ \beta_6 CurrentAccountDeficit^{z}_{i,t-1} \\
&+ \beta_7 BroadMoneyGrowth^{z}_{i,t-1}
+ \beta_8 (Exposure^{z}_{i,t-1} \times FXChange^{z}_{i,t-1}) \\
&+ \beta_9 (FXChange^{z}_{i,t-1} \times CurrentAccountDeficit^{z}_{i,t-1}) \\
&+ \alpha_i + \lambda_y + \delta_m + \varepsilon_{i,t}.
\end{aligned}
$$

where:

- $\alpha_i$ represents country fixed effects.
- $\lambda_y$ represents year fixed effects.
- $\delta_m$ represents calendar-month fixed effects.
- Continuous explanatory variables are standardized.
- Standard errors are clustered by country.

The robustness specification additionally includes:

$$
FiscalDeficit^{z}_{i,t-1}
\times
BroadMoneyGrowth^{z}_{i,t-1}.
$$

## Demo Code: Exposure Construction

```python
import numpy as np

panel = panel.sort_values(["country", "month"]).copy()

panel["btc_attention_scaled"] = panel["btc_attention"] / 100

panel["btc_attention_scaled_l1"] = (
    panel.groupby("country")["btc_attention_scaled"].shift(1)
)

panel["dlog_usdt_marketcap_l1"] = (
    panel.groupby("country")["dlog_usdt_marketcap"].shift(1)
)

panel["btc_x_dlog_usdt_l1"] = (
    panel["btc_attention_scaled_l1"]
    * panel["dlog_usdt_marketcap_l1"]
)

def zscore(series):
    return (series - series.mean()) / series.std()

panel["btc_x_dlog_usdt_l1_z"] = zscore(
    panel["btc_x_dlog_usdt_l1"]
)
```

## Demo Code: Preferred Fixed-Effects Model

```python
import statsmodels.formula.api as smf

formula = """
inflation_yoy ~
    btc_x_dlog_usdt_l1_z
    + restrictive_intensity_l1_z
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

model_definition = smf.ols(
    formula=formula,
    data=panel
)

used_rows = model_definition.data.row_labels

model = model_definition.fit(
    cov_type="cluster",
    cov_kwds={
        "groups": panel.loc[used_rows, "country"]
    }
)

print(model.summary())
```

## Output Data

| Research output | Description |
|---|---|
| Balanced country-month panel | Integrated policy, cryptocurrency, inflation, exchange-rate, and macroeconomic dataset |
| Preferred fixed-effects model | Main estimate using lagged standardized exposure and country-clustered standard errors |
| All-mechanism robustness model | Adds the fiscal-deficit × broad-money-growth interaction |
| Policy-regime model | Estimates separate stablecoin-exposure relationships across Legal, Restricted, and Illegal regimes |
| Marginal-effect table | Reports the estimated exposure association and statistical test for each policy regime |