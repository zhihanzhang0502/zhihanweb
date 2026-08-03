# Key Findings & Outputs

## Key Findings

### Preferred Model

The preferred fixed-effects model finds a negative and statistically significant association between lagged standardized stablecoin exposure and year-over-year CPI inflation.

| Model | Exposure coefficient | Standard error | t-statistic | p-value | N | R-squared |
|---|---:|---:|---:|---:|---:|---:|
| Preferred model | -1.966 | 0.679 | -2.897 | 0.0038 | 626 | 0.804 |
| All-mechanism robustness model | -1.733 | 0.755 | -2.294 | 0.0218 | 626 | 0.885 |

Because the exposure variable is standardized while inflation remains measured in percentage points, the preferred estimate implies that a one-standard-deviation increase in lagged stablecoin exposure is associated with approximately 1.97 percentage points lower year-over-year CPI inflation, conditional on the included controls and fixed effects.

The coefficient remains negative and statistically significant after adding the fiscal-deficit × broad-money-growth interaction.

### Policy-Regime Heterogeneity

The policy-regime model uses Restricted countries as the reference group and calculates the total estimated exposure association for each regime.

| Policy regime | Estimated exposure association | Standard error | t-statistic | p-value |
|---|---:|---:|---:|---:|
| Restricted | -4.342 | 1.332 | -3.260 | 0.0011 |
| Legal | -0.150 | 0.773 | -0.194 | 0.8460 |
| Illegal | -0.211 | 0.444 | -0.476 | 0.6343 |

The estimated association is negative and statistically significant in Restricted countries, but small and statistically insignificant in Legal and Illegal countries.

The difference between Legal and Restricted countries is 4.192 with a p-value of 0.0106. The difference between Illegal and Restricted countries is 4.131 with a p-value of 0.0105. There is no statistically meaningful difference between Legal and Illegal countries.

### Macro-Financial Mechanism

In the preferred model, the standardized interaction between stablecoin exposure and exchange-rate depreciation is negative and statistically significant:

| Variable | Coefficient | t-statistic | p-value |
|---|---:|---:|---:|
| Stablecoin exposure × exchange-rate change | -2.034 | -4.399 | < 0.001 |

This result is consistent with the stablecoin-exposure relationship varying with exchange-rate conditions. However, the estimates should be interpreted as conditional associations rather than causal effects.

Monthly policy-restriction intensity is only marginally significant in the preferred model. The clearest policy-related evidence therefore comes from the cross-regime heterogeneity results rather than from the standalone monthly policy-intensity coefficient.

## Research Outputs

| Output | Description |
|---|---|
| Crypto-policy title dataset | Deduplicated GDELT policy titles classified as restrictive, supportive, or neutral |
| Country-month policy panel | Monthly policy attention, restrictiveness, and policy-regime measures |
| Integrated empirical panel | Cryptocurrency, policy, inflation, exchange-rate, fiscal, monetary, unemployment, and external-balance variables |
| Main regression analysis | Fixed-effects models with standard errors clustered by country |
| Heterogeneity analysis | Marginal stablecoin-exposure estimates for Legal, Restricted, and Illegal regimes |
| Website demonstration code | Simplified exposure-construction and regression code reflecting the actual empirical specification |

## Interpretation and Limitations

The results provide evidence of a conditional relationship between stablecoin exposure and inflation, particularly in Restricted policy environments.

The use of lagged explanatory variables helps address contemporaneous timing and reverse-causality concerns, but it does not eliminate all potential endogeneity. Google Trends attention is also an indirect proxy for local cryptocurrency exposure rather than a direct measure of stablecoin ownership or transaction use.

Accordingly, the findings should not be interpreted as establishing a definitive causal effect of stablecoin adoption on inflation.