# Key Findings & Outputs

## Key Findings

### DEX Net Flow and CEX Returns

DEX net buy flow has a positive and statistically significant relationship with Binance returns.

In the full specification with trading-volume controls and fixed effects:

| Variable | Coefficient | Significance |
|---|---:|---:|
| Current DEX net flow | 0.086450 | \(p<0.01\) |
| DEX net flow, lag 1 | 0.025113 | \(p<0.01\) |
| DEX net flow, lag 2 | -0.006938 | \(p<0.01\) |

The positive contemporaneous and first-lag coefficients indicate that directional trading pressure on Uniswap contains information relevant to short-horizon Binance price formation. The smaller negative second-lag coefficient suggests that part of the initial price response is subsequently reversed.

These relationships remain qualitatively stable after adding trading-volume controls and token-pair and date fixed effects.

### Effect of Blockchain Congestion

Blockchain congestion strengthens the relationship between DEX net flow and Binance returns.

In the full congestion specification:

| Interaction term | Coefficient | Significance |
|---|---:|---:|
| DEX flow × congestion | 0.002785 | \(p<0.01\) |
| DEX flow, lag 1 × congestion, lag 1 | 0.001168 | \(p<0.01\) |
| DEX flow, lag 2 × congestion, lag 2 | -0.000324 | Not significant |

The positive current and first-lag interaction coefficients support the hypothesis that DEX flow becomes more informative during periods of greater blockchain congestion.

One possible interpretation is that higher on-chain transaction costs discourage lower-value or less-informed transactions. The remaining DEX flows may therefore contain a higher concentration of informed or urgent trading activity.

### Effect of CEX Illiquidity

CEX illiquidity weakens cross-market information transmission with a one-period lag.

In the full illiquidity specification:

| Interaction term | Coefficient | Significance |
|---|---:|---:|
| DEX flow × CEX illiquidity | 0.568452 | Not significant |
| DEX flow, lag 1 × CEX illiquidity, lag 1 | -1.194935 | \(p<0.01\) |
| DEX flow, lag 2 × CEX illiquidity, lag 2 | -0.054890 | Not significant |

The significantly negative first-lag interaction provides partial support for the illiquidity hypothesis. When Binance is less liquid, the predictive effect of prior DEX flow becomes weaker.

This result is consistent with an arbitrage mechanism: wider spreads, thinner order books, and greater execution costs make it more difficult for traders to transfer information and correct price differences across exchanges.

### State-Dependent Price Discovery

The results show that DEX–CEX price discovery depends on market conditions.

- DEX net flow contains information relevant to CEX returns.
- Congestion amplifies the information contained in DEX trading activity.
- CEX illiquidity limits the incorporation of DEX information into centralized-exchange prices.
- Cross-market price discovery therefore depends on both blockchain conditions and centralized-market liquidity.

## Selected Regression Summary

| Hypothesis | Main full-model result | Adjusted \(R^2\) | Observations |
|---|---|---:|---:|
| H1: DEX flow predicts CEX returns | Current flow \(=0.086450^{***}\); lag 1 \(=0.025113^{***}\) | 0.052 | 244,788 |
| H2: Congestion strengthens transmission | Current interaction \(=0.002785^{***}\); lag-1 interaction \(=0.001168^{***}\) | 0.056 | 244,788 |
| H3: Illiquidity weakens transmission | Lag-1 interaction \(=-1.194935^{***}\) | 0.061 | 203,210 |

\(^{***}p<0.01\)

## Research Outputs

- Constructed a two-minute panel linking Uniswap and Binance trading activity.
- Engineered CEX returns, DEX net flow, blockchain-congestion, and CEX-illiquidity variables.
- Created current, one-period-lagged, and two-period-lagged model specifications.
- Estimated baseline, control, fixed-effect, and full regression models.
- Applied HC1 heteroskedasticity-robust standard errors.
- Produced publication-style regression tables for the three hypotheses.
- Interpreted the results using cross-market arbitrage and market-microstructure mechanisms.
- Prepared the final research report, regression documentation, presentation, and presentation script.