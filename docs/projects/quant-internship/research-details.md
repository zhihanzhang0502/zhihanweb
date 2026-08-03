# Research Details

## Input Data

The analysis used proprietary futures-market data. Factor definitions and raw datasets are therefore presented in anonymized form.

| Input | Description |
|---|---|
| Futures price data | Multi-year price and return series covering multiple futures contracts |
| Anonymized signals | Four initial signal families, represented as \(X_1\), \(X_2\), \(X_3\), and \(X_4\) |
| Contract information | Contract weights and cost-related inputs used in portfolio backtesting |
| Evaluation periods | Chronological training, validation, and out-of-sample testing windows |
| Strategy parameters | Ranking thresholds, holding periods, smoothing windows, and signal-transformation settings |

## Model

The research workflow contained five main stages.

### 1. Data Processing

- Parsed and standardized trading dates.
- Aligned factor, price, and return matrices across contracts.
- Handled missing observations and inconsistent contract coverage.
- Converted wide contract-level datasets into panel-style formats for modeling.
- Constructed forward-return targets while maintaining chronological alignment.

### 2. Feature Engineering

The initial signals were expanded using several time-series transformations:

- Lagged signal values;
- Momentum measures;
- Rolling moving averages;
- Rolling standard deviations;
- Relative Strength Index indicators;
- Polynomial and interaction terms;
- Cross-sectional and rolling z-score transformations;
- Rank, quantile, and nonlinear signal transformations.

### 3. Factor Evaluation

Candidate factors were evaluated using:

- Spearman information coefficients;
- Cross-sectional RankIC;
- Statistical significance and t-statistics;
- Stability across contracts and time periods;
- Comparisons between raw and transformed signals.

### 4. Predictive Modeling

The analysis compared several statistical and machine-learning approaches:

| Method | Purpose |
|---|---|
| Linear regression | Baseline return-prediction model |
| Regularized regression | Control overfitting and select more stable signal combinations |
| Random forest regression | Capture nonlinear relationships and interactions |
| Decision-tree models | Evaluate nonlinear prediction and classification rules |
| Logistic regression | Predict positive, negative, or neutral return directions |
| Rolling estimation | Retrain models using only information available before each test period |
| Time-series cross-validation | Evaluate models without randomly mixing past and future observations |

### 5. Portfolio Construction and Backtesting

Predicted signals were converted into portfolio positions through:

- Cross-sectional ranking;
- Top-and-bottom quantile selection;
- Multi-bucket portfolio formation;
- Continuous normalized weights;
- Long-short directional signals;
- Threshold-based filtering;
- Rolling position smoothing and holding-period rules.

The resulting positions were evaluated through a futures backtesting workflow that incorporated contract weights and trading-related adjustments.

## Output Data

| Output | Description |
|---|---|
| Factor diagnostics | IC, RankIC, statistical significance, and factor-ranking results |
| Predicted returns | Contract-level forecasts produced by statistical and machine-learning models |
| Position matrices | Long, short, and continuous portfolio weights across futures contracts |
| Backtest series | Strategy profit, cumulative profit, and net-asset-value paths |
| Performance charts | Visual comparisons of returns and drawdowns over time |
| Parameter comparisons | Results across ranking thresholds, smoothing windows, and signal transformations |
| Risk-return metrics | Sharpe ratio, recent-period Sharpe ratio, net profit, maximum drawdown, daily win rate, and a composite strategy score |