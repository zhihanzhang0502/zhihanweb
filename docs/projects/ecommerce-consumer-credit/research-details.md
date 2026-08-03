# Research Details

## Input

This project uses an analytical model rather than an empirical dataset.

| Input | Description |
|---|---|
| Hybrid platform | Resells product A and provides marketplace access to a third-party seller |
| Wholesale supplier | Supplies product A to the platform and determines the wholesale price |
| Third-party seller | Sells a substitute product B directly through the platform |
| Consumers | Choose between product A, product B, and no purchase |
| \(v\) | Consumer valuation of product A |
| \(\lambda\) | Product differentiation between products A and B |
| \(\alpha\) | Commission rate charged by the platform |
| \(\beta\) | Additional fee charged for sharing the consumer credit service |
| \(\gamma\) | Consumer preference for the credit service |
| \(\theta\) | Consumer repayment rate |
| \(w_a\) | Wholesale price of product A |
| \(p_a, p_b\) | Retail prices of products A and B |

## Model

The analysis compares three operational modes.

| Mode | Platform product | Third-party seller product |
|---|---|---|
| **NN** | No consumer credit service | No consumer credit service |
| **IN** | Consumer credit service provided | No consumer credit service |
| **II** | Consumer credit service provided | Consumer credit service shared |

Consumer utilities under the three modes are represented as follows:

### NN Mode

\[
u_a = v-p_a
\]

\[
u_b = \lambda v-p_b
\]

### IN Mode

\[
u_a = v-p_a+\gamma p_a
\]

\[
u_b = \lambda v-p_b
\]

### II Mode

\[
u_a = v-p_a+\gamma p_a
\]

\[
u_b = \lambda v-p_b+\gamma p_b
\]

The sequence of decisions is:

1. The wholesale supplier determines the wholesale price.
2. The platform and third-party seller simultaneously determine retail prices.
3. Consumers choose between the two products or no purchase.
4. Equilibrium prices, demand, profits, and consumer surplus are derived.
5. The three operational modes are compared to determine the optimal provision and sharing strategies.

The model is solved using backward induction, equilibrium analysis, comparative statics, and Mathematica-based numerical simulations.

## Output

| Output | Description |
|---|---|
| Equilibrium wholesale price | Optimal wholesale price selected by the supplier |
| Equilibrium retail prices | Optimal prices of products A and B |
| Product demand | Demand for each product under the NN, IN, and II modes |
| Platform profit | Profit from product sales, commissions, and service fees |
| Supplier profit | Profit earned from supplying product A |
| Third-party seller profit | Seller profit after commission and service fees |
| Consumer surplus | Consumer welfare under each operational mode |
| Provision condition | Conditions under which the platform launches the credit service |
| Sharing condition | Conditions under which the platform and seller agree to share the service |
| Extension results | Outcomes when some consumers choose not to use the credit service |