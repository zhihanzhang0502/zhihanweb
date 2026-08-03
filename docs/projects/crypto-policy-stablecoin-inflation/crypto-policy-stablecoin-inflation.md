# Crypto Policy, Stablecoin Exposure, and Inflation

## Project Overview

This project studies whether stablecoin exposure is associated with inflation outcomes across countries.

The core idea is to combine local crypto attention with a global stablecoin expansion shock. Countries with higher Bitcoin search attention are treated as more exposed to global USDT market-cap growth.

## Research Question

Does stablecoin-driven digital dollarization affect inflation?

More specifically, this project asks:

- Whether lagged stablecoin exposure is associated with year-over-year CPI inflation.
- Whether crypto policy intensity changes the relationship.
- Whether the effect differs across Legal, Restricted, and Illegal crypto policy regimes.
- Whether exchange-rate and macro-financial channels help explain the relationship.

## Data Sources

| Component | Source | Role |
|---|---|---|
| Crypto policy news | GDELT 2.0 GKG titles | Construct policy attention and restrictiveness |
| Local crypto attention | Google Trends Bitcoin search index | Measure country-level crypto attention |
| Stablecoin shock | CoinMetrics USDT market capitalization | Measure global stablecoin expansion |
| Inflation | IMF CPI data | Main dependent variable |
| Exchange rate | IMF exchange-rate data | Exchange-rate channel |
| Macro controls | World Bank / IMF | Fiscal, monetary, unemployment, and current-account controls |

## Key Variable Construction

The main exposure variable is:

$$
StablecoinExposure_{i,t}
=
BitcoinAttentionScaled_{i,t}
\times
USDTGrowthShock_t
$$

where:

- BitcoinAttentionScaled is Google Trends Bitcoin attention divided by 100.
- USDTGrowthShock is the monthly log growth of USDT market capitalization.
- The lagged version is used in the main regressions to reduce contemporaneous reverse-causality concerns.

## Policy Variables

From GDELT title-level crypto policy news, I construct country-month policy variables:

| Variable | Meaning |
|---|---|
| Policy news attention | log(1 + number of unique crypto policy titles) |
| Average policy restrictiveness | Average tone of policy-related titles |
| Restrictive policy dummy | Whether at least one restrictive policy title appears |
| Policy restriction intensity | Average restrictiveness × policy news attention |

## Empirical Strategy

The preferred model estimates year-over-year CPI inflation as a function of lagged standardized stablecoin exposure, policy restriction intensity, macroeconomic controls, mechanism interactions, and fixed effects.

The specification includes:

- Country fixed effects
- Year fixed effects
- Calendar-month fixed effects
- Lagged macro controls
- Exchange-rate and external vulnerability interactions

## Main Results

The preferred final model finds a statistically significant negative association between lagged standardized stablecoin exposure and year-over-year CPI inflation.

The all-mechanism robustness model keeps the stablecoin exposure coefficient negative and significant, while adding the fiscal deficit × broad money growth interaction.

## Policy Regime Heterogeneity

I classify countries into three crypto policy regimes:

- Legal
- Restricted
- Illegal

The regime interaction results suggest that the negative stablecoin exposure effect is mainly concentrated in Restricted countries.




