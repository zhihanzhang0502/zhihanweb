# Research Details

## Input Data

The analysis combines high-frequency trading data from Uniswap and Binance.

| Input | Description |
|---|---|
| Data period | November 18, 2020 – February 10, 2021 |
| Frequency | Two-minute intervals |
| Decentralized exchange | Uniswap |
| Centralized exchange | Binance |
| Trading pairs | ETH–USDT, WBTC–ETH, LINK–ETH, and AAVE–ETH |
| Price data | Volume-weighted average prices within each interval |
| Trading activity | Buy volume, sell volume, total volume, trade counts, and swap counts |
| DEX net flow | Difference between DEX buy volume and sell volume |
| Congestion proxy | Number of DEX transactions or swaps within each two-minute interval |
| CEX illiquidity | Absolute CEX return divided by CEX trading volume |
| Control variable | Total trading volume on Binance |
| Fixed effects | Token-pair and date fixed effects |

The Uniswap and Binance datasets were cleaned, aggregated, and aligned to the same two-minute intervals. Current values and one- and two-period lags were then constructed within each trading pair.

## Model

The dependent variable is the Binance return in basis points:

\[
R_{i,t}^{CEX}
=
\left[
\ln(P_{i,t})-\ln(P_{i,t-1})
\right]\times 10{,}000
\]

where \(P_{i,t}\) is the volume-weighted average Binance price for token pair \(i\) during interval \(t\).

DEX net trade flow is defined as:

\[
Flow_{i,t}^{DEX}
=
BuyVolume_{i,t}^{DEX}
-
SellVolume_{i,t}^{DEX}
\]

CEX illiquidity is measured as:

\[
Illiquidity_{i,t}^{CEX}
=
\frac{
\left|
\ln(P_{i,t})-\ln(P_{i,t-1})
\right|
}{
TradingVolume_{i,t}^{CEX}
}
\]

### Baseline Price-Discovery Model

\[
R_{i,t}^{CEX}
=
\beta_0
+
\beta_1R_{i,t-1}^{CEX}
+
\beta_2R_{i,t-2}^{CEX}
+
\gamma_0Flow_{i,t}^{DEX}
+
\gamma_1Flow_{i,t-1}^{DEX}
+
\gamma_2Flow_{i,t-2}^{DEX}
+
\varepsilon_{i,t}
\]

This model tests whether current and lagged DEX flows are associated with Binance returns.

### Congestion Model

The congestion specification adds current and lagged congestion measures and interactions between DEX flow and congestion:

\[
R_{i,t}^{CEX}
=
\beta_0
+
\sum_{j=1}^{2}\beta_jR_{i,t-j}^{CEX}
+
\sum_{j=0}^{2}\delta_jCongestion_{i,t-j}
+
\sum_{j=0}^{2}\gamma_jFlow_{i,t-j}^{DEX}
+
\sum_{j=0}^{2}\lambda_j
\left(
Flow_{i,t-j}^{DEX}
\times
Congestion_{i,t-j}
\right)
+
\varepsilon_{i,t}
\]

A positive interaction coefficient indicates that DEX flow becomes more informative when the blockchain is more congested.

### CEX Illiquidity Model

The illiquidity specification adds current and lagged CEX illiquidity and their interactions with DEX flow:

\[
R_{i,t}^{CEX}
=
\beta_0
+
\sum_{j=1}^{2}\beta_jR_{i,t-j}^{CEX}
+
\sum_{j=0}^{2}\delta_jIlliquidity_{i,t-j}^{CEX}
+
\sum_{j=0}^{2}\gamma_jFlow_{i,t-j}^{DEX}
+
\sum_{j=0}^{2}\lambda_j
\left(
Flow_{i,t-j}^{DEX}
\times
Illiquidity_{i,t-j}^{CEX}
\right)
+
\varepsilon_{i,t}
\]

A negative interaction coefficient indicates that weak CEX liquidity reduces the transmission of information from DEX trading activity.

### Estimation

For each hypothesis, four specifications were estimated:

| Specification | Trading-volume control | Token-pair and date fixed effects |
|---|---:|---:|
| Baseline | No | No |
| Controls | Yes | No |
| Fixed effects | No | Yes |
| Full model | Yes | Yes |

The models were estimated using OLS with HC1 heteroskedasticity-robust standard errors.

## Output Data

| Output | Description |
|---|---|
| Two-minute panel dataset | Aligned Uniswap and Binance observations across four trading pairs |
| CEX returns | Binance returns measured in basis points |
| DEX flow variables | Current, one-period-lagged, and two-period-lagged net trade flows |
| State variables | Current and lagged congestion and illiquidity measures |
| Interaction variables | DEX flow interacted with congestion and CEX illiquidity |
| Regression estimates | Coefficients, robust standard errors, test statistics, and significance levels |
| H1 and H2 sample | 244,788 two-minute observations |
| H3 sample | 203,210 observations after applying illiquidity-data requirements |
| Research deliverables | Regression tables, research report, presentation slides, and presentation script |