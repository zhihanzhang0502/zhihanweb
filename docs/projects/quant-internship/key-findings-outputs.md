# Key Findings & Outputs

## Key Findings

### Factor Predictive Power

The predictive usefulness of the anonymized signal families varied substantially across contracts and time periods.

Lagged values, momentum indicators, RSI-style transformations, rolling statistics, and interaction terms were evaluated to identify stronger candidate predictors. The factor-selection analysis showed that short-horizon transformations of some signals provided stronger cross-sectional information coefficients than their original raw values.

### Signal Transformation

Signal preprocessing had a meaningful effect on strategy performance.

The tested approaches included:

- Cross-sectional z-score normalization;
- Robust normalization;
- Quantile and rank transformations;
- Multi-bucket portfolio construction;
- Binary top-and-bottom selection;
- Continuous normalized portfolio weights.

In the recorded strategy-comparison table, a normalization-based position method produced the strongest composite score and a substantially smaller drawdown than many of the binary ranking alternatives.

### Position Smoothing

Position-smoothing and holding-period choices materially affected portfolio behavior.

Longer smoothing windows reduced abrupt changes in positions, while shorter windows responded more quickly to new information. The appropriate setting therefore required balancing signal responsiveness against portfolio stability.

### Out-of-Sample Evaluation

Results varied across evaluation periods, showing that full-sample performance alone was not sufficient for model selection.

Rolling annual estimation and time-series cross-validation were used to ensure that each forecast relied only on information available before the corresponding test period.

### Model Comparison

No single model or signal-construction method dominated every evaluation measure.

Candidate approaches involved trade-offs among profitability, Sharpe ratio, maximum drawdown, win rate, stability, and implementation complexity. Strategy evaluation therefore considered several performance measures jointly rather than selecting models using predictive accuracy alone.

## Research Outputs

- Processed and aligned multi-contract futures-market datasets.
- Constructed lagged, momentum, volatility, RSI, and interaction features.
- Evaluated factor quality using IC, RankIC, significance tests, and time-period comparisons.
- Compared linear, regularized, tree-based, and classification models.
- Implemented rolling and time-series-aware out-of-sample evaluation.
- Converted model predictions into cross-sectional long-short portfolio positions.
- Tested ranking thresholds, portfolio normalization, signal filtering, and smoothing windows.
- Produced backtest profit curves, drawdown analysis, and strategy-performance tables.
- Developed reusable Python workflows for factor testing and quantitative strategy evaluation.