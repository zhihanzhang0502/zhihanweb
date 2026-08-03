# Overview

This project studies how stablecoin-driven digital dollarization is associated with inflation dynamics across countries.

The core empirical design combines a global stablecoin expansion shock with country-level cryptocurrency attention. Monthly log growth in USDT market capitalization represents the global stablecoin shock, while Google Trends attention to Bitcoin measures the degree to which each country may be exposed to that shock.

I independently developed the end-to-end research pipeline using Python, Google BigQuery, GDELT, pandas, and statsmodels. My contributions included:

- Collecting and integrating cryptocurrency, policy-news, inflation, exchange-rate, fiscal, monetary, unemployment, and external-balance data.
- Constructing a balanced country-month panel covering 18 countries from January 2019 to December 2025.
- Developing title-based crypto-policy measures from GDELT news data.
- Engineering lagged stablecoin-exposure and macro-financial interaction variables.
- Estimating fixed-effects panel regressions with standard errors clustered by country.
- Examining exchange-rate mechanisms and heterogeneity across Legal, Restricted, and Illegal crypto-policy regimes.

The balanced merged panel contains 1,512 country-month observations. After applying lag structures and complete-case filters for the preferred specification, the final regression sample contains 626 observations across 11 countries.

**Institution:** University of Illinois Urbana-Champaign  
**Duration:** February 2026 - Present