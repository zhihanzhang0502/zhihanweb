# Key Findings & Outputs

## Key Findings

### 1. Credit-Service Provision

By comparing the platform's equilibrium profits under the NN and IN modes, the platform launches the consumer credit service if and only if

\[
\gamma>1-\theta.
\]

Thus, consumer preference for the service must exceed the delinquency rate. If \(\gamma\leq 1-\theta\), the demand advantage created by credit is insufficient to offset default risk.

### 2. Credit-Service Sharing

Conditional on the platform having launched the service, the sharing decision depends on the service-fee rate \(\beta\), the commission rate \(\alpha\), the repayment rate \(\theta\), and consumer preference \(\gamma\).

| Service-fee condition | Equilibrium implication |
|---|---|
| \(\beta\leq 1-\alpha-\theta\) | The platform does not share the credit service |
| \(1-\alpha-\theta<\beta<(1-\alpha)(1-\theta)\) | The seller is willing to participate, while the platform shares only if \(\gamma>\dfrac{1-\theta-\beta}{\alpha}\) |
| \(\beta\geq(1-\alpha)(1-\theta)\) | The platform is willing to share, while the seller participates only if \(\gamma>\gamma_0\) |

Here, \(\gamma_0\) is the consumer-preference threshold at which the seller is indifferent between the II and IN modes. A win-win agreement is most likely when the service fee is moderate and consumer preference is sufficiently high.

### 3. Effects of Exclusive Provision

When the platform introduces credit only for product A and \(\gamma>1-\theta\), the equilibrium comparison is

\[
\begin{aligned}
p_a^{IN*} &> p_a^{NN*},
&w_a^{IN*} &> w_a^{NN*},
&p_b^{IN*} &< p_b^{NN*},\\
D_a^{IN*} &> D_a^{NN*},
&D_b^{IN*} &< D_b^{NN*},\\
\pi_W^{IN*} &> \pi_W^{NN*},
&\pi_T^{IN*} &< \pi_T^{NN*},
&CS^{IN*} &> CS^{NN*}.
\end{aligned}
\]

The platform's product gains a service advantage, while the seller lowers its price but still loses demand and profit. Consumer surplus rises because the seller's price reduction benefits consumers.

### 4. Effects of Service Sharing

When the platform and seller reach a sharing agreement, the comparison between the II and IN modes is

\[
\begin{aligned}
p_a^{II*} &> p_a^{IN*},
&w_a^{II*} &< w_a^{IN*},
&p_b^{II*} &> p_b^{IN*},\\
D_a^{II*} &< D_a^{IN*},
&D_b^{II*} &> D_b^{IN*},\\
\pi_W^{II*} &< \pi_W^{IN*},
&CS^{II*} &< CS^{IN*}.
\end{aligned}
\]

Sharing alleviates price competition and can benefit both the platform and the seller, but it reduces the wholesale supplier's profit and consumer surplus. The consumer-surplus result is counterintuitive: broader access to credit does not necessarily improve consumer welfare.

### 5. Consumer Participation Extension

The extension distinguishes consumers who use the credit service from conservative consumers who decline it. If \(\delta\) denotes the share of participating consumers, the platform launches the service only when \(\delta\) is sufficiently high. As \(\delta\) increases, the parameter region in which the platform and seller both prefer service sharing becomes smaller.

## Research Outputs

- Closed-form equilibrium outcomes for the NN, IN, and II operational modes.
- Threshold conditions for credit-service provision and sharing.
- Comparative-statics results for repayment rates, service fees, commissions, and consumer preferences.
- An extension incorporating consumers who choose not to use the credit service.
- Mathematica-based numerical simulations and strategy-region analysis.
- A peer-reviewed article published in *Managerial and Decision Economics*.