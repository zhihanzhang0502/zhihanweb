# Research Details

## Input

This project develops an analytical game-theoretic model rather than using an empirical dataset.

| Input | Description |
|---|---|
| Manufacturer | Operates an offline channel and cooperates with an e-commerce platform online |
| E-commerce platform | Operates the online channel as either a reseller or an intermediary |
| Consumers | Choose between the offline channel, the online channel, and no purchase |
| Wholesale contract | The platform purchases from the manufacturer and resells online |
| Agency contract | The manufacturer sells directly through the platform and pays a commission |
| \(v\) | Consumer valuation of the product |
| \(\theta\) | Valuation discount caused by delayed product receipt |
| \(\gamma\) | Revenue discount caused by the cash-flow opportunity cost of deferred payment |
| \(l\) | Shopping-cost difference between the offline and online channels |
| \(\alpha\) | Pay-on-delivery service fee under the agency contract |
| \(\beta\) | Platform commission rate under the agency contract |
| \(p_f\) | Offline retail price |
| \(p_n\) | Online retail price |
| \(w\) | Wholesale price under the wholesale contract |
| \(\delta\) | Probability that an online product fits consumer needs |
| \(m\) | Consumer hassle cost associated with returning a product |
| \(c\) | Return-handling cost borne by the online seller |

## Model

Consumer utility from purchasing offline is:

\[
u_f=v-p_f-l
\]

Without pay-on-delivery, online utility is:

\[
u_n^N=\theta v-p_n
\]

With pay-on-delivery, consumers postpone payment until receiving the product:

\[
u_n^Y=\theta(v-p_n)
\]

The analysis compares four scenarios.

| Scenario | Distribution contract | Payment scheme |
|---|---|---|
| **WN** | Wholesale contract | No pay-on-delivery |
| **WY** | Wholesale contract | Pay-on-delivery |
| **AN** | Agency contract | No pay-on-delivery |
| **AY** | Agency contract | Pay-on-delivery |

The game proceeds through the following stages:

1. The manufacturer selects the wholesale or agency contract.
2. The platform decides whether to offer pay-on-delivery.
3. Under the agency contract, the manufacturer decides whether to adopt the service.
4. The manufacturer determines its relevant wholesale and offline prices.
5. The platform or manufacturer determines the online retail price, depending on the contract.

The model is solved using backward induction, equilibrium analysis, comparative statics, and Mathematica-based numerical analysis.

## Output

| Output | Description |
|---|---|
| Equilibrium prices | Wholesale, online retail, and offline retail prices |
| Channel demand | Demand in the online and offline channels |
| Total demand | Combined market demand across both channels |
| Manufacturer profit | Profit from offline sales and online-channel cooperation |
| Platform profit | Reselling margin, commission revenue, and service-fee revenue |
| Pay-on-delivery adoption | Conditions under which the platform and manufacturer adopt the service |
| Contract selection | Conditions determining wholesale versus agency selling |
| Consumer surplus | Consumer welfare under each contract and payment scenario |
| Social welfare | Combined firm profits and consumer surplus |
| Return-related outcomes | Adoption and contract decisions when product returns are included |
| Robustness outcomes | Results with different discount factors for product valuation and cash |