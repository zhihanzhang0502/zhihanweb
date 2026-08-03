```markdown
# State-Dependent DEX–CEX Price Discovery

This project studies how information is transmitted from decentralized exchanges (DEXs) to centralized exchanges (CEXs), and how this transmission varies across different blockchain and market conditions.

Using high-frequency trading data from Uniswap and Binance, the project examines whether net trading activity on DEXs predicts short-horizon price changes on CEXs. It further investigates whether Ethereum network congestion strengthens this relationship and whether CEX illiquidity weakens it.

## Research Questions

- Does DEX net trade flow predict short-horizon returns on CEXs?
- Does blockchain congestion strengthen the price impact of DEX trading activity?
- Does CEX illiquidity reduce the transmission of information from DEXs to CEXs?

## Data

The analysis uses two-minute trading data from November 2020 to February 2021 for four cryptocurrency trading pairs:

- ETH–USDT
- WBTC–ETH
- LINK–ETH
- AAVE–ETH

Uniswap is used as the decentralized exchange, while Binance is used as the centralized exchange.

The dataset includes:

- Trade prices
- Buy and sell volumes
- Number of swaps
- Total trading volume
- DEX net trade flow
- Blockchain congestion measures
- CEX illiquidity measures

The Uniswap and Binance datasets were cleaned, aggregated, and aligned into a common two-minute panel structure.

## Methodology

The project estimates panel regression models in which Binance returns are explained by:

- Current and lagged DEX net trade flow
- Lagged CEX returns
- Blockchain congestion
- CEX illiquidity
- Interaction terms between DEX flow and market-state variables
- CEX trading volume controls
- Date and token-pair fixed effects

DEX net trade flow is defined as the difference between buy volume and sell volume.

CEX illiquidity is measured using the absolute price return divided by trading volume.

## Main Findings

The empirical results show that DEX trading activity contains information relevant to CEX price formation.

- DEX net buy flow has a positive and statistically significant relationship with Binance returns.
- The first lag of DEX net flow also positively predicts CEX returns, indicating short-horizon information transmission from Uniswap to Binance.
- Blockchain congestion strengthens the relationship between DEX net flow and CEX returns.
- CEX illiquidity weakens the transmission of DEX information with a one-period lag.

These findings suggest that DEX–CEX price discovery is state-dependent. DEX order flow becomes more informative during periods of blockchain congestion, while weak liquidity on centralized exchanges reduces the efficiency of cross-market information transmission.

## Economic Interpretation

The results are consistent with two main mechanisms.

First, cross-market arbitrage allows price information originating on DEXs to be incorporated into CEX prices.

Second, market conditions affect the strength of this process. During congested periods, higher transaction costs may filter out less-informed trading activity, making observed DEX flows more informative. In contrast, poor CEX liquidity increases execution costs and limits arbitrage activity, weakening price adjustment across markets.

## My Contributions

- Processed and aligned high-frequency Uniswap and Binance trading data.
- Constructed a two-minute DEX–CEX panel dataset.
- Created net-flow, congestion, return, volume, and illiquidity variables.
- Designed baseline and interaction regression specifications.
- Estimated models with controls and fixed effects.
- Interpreted the results using market microstructure and cross-market arbitrage mechanisms.
- Prepared regression tables, the research report, and the final presentation.

## Skills Used

- Python
- R
- High-frequency financial data processing
- Panel data construction
- Econometric regression analysis
- Fixed-effects modeling
- Interaction-effect analysis
- Cryptocurrency market microstructure
- Academic research and presentation
```
