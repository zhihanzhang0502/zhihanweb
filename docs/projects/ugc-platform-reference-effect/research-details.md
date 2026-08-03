# Research Details

## Input

This project develops a theoretical dynamic model rather than using an empirical dataset.

| Input | Description |
|---|---|
| UGC platform | Determines the recommendation intensity of pure content |
| Content creator | Determines the quality of pure content |
| Pure content | Non-commercial content used to attract and retain users |
| Shoppable content | Commercial content that directly generates platform revenue |
| \(c(t)\) | Recommendation intensity of pure content |
| \(1-c(t)\) | Recommendation intensity of shoppable content |
| \(q(t)\) | Quality of pure content |
| \(r(t)\) | Consumer reference quality based on previous content experience |
| \(N(t)\) | User engagement on the platform |
| \(N_0\) | Base level of user engagement |
| \(\alpha\) | Sensitivity of user engagement to pure content quality |
| \(\phi\) | Sensitivity of user engagement to the reference-quality effect |
| \(\rho\) | Consumer aversion to shoppable content |
| \(b\) | Consumer memory-decay rate |
| \(k\) | Content-quality production cost coefficient |
| \(n\) | Platform revenue per unit view of shoppable content |
| \(l\) | Creator revenue per unit view of pure content |
| \(\epsilon\) | Uncertainty level of consumer reference quality |

## Model

The project models a Stackelberg game in which the UGC platform acts as the leader and the content creator acts as the follower.

The platform first determines the recommendation intensity of pure content. After observing the platform's decision, the creator determines pure content quality.

Consumer reference quality evolves according to:

\[
dr(t)=b\bigl(q(t)-r(t)\bigr)dt
\]

User engagement is modeled as:

\[
N(t)=N_0+\alpha q(t)+\phi\bigl(q(t)-r(t)\bigr)-\rho\bigl(1-c(t)\bigr)
\]

The platform earns revenue from shoppable-content views:

\[
P_p(t)=nN(t)\bigl(1-c(t)\bigr)
\]

The content creator earns revenue from pure-content views and incurs a quality-production cost:

\[
P_c(t)=lN(t)c(t)-kq(t)^2
\]

The analysis compares three scenarios.

| Scenario | Description |
|---|---|
| **CN** | Static pure content quality and recommendation intensity |
| **DN** | Dynamic quality and recommendation intensity without reference-quality uncertainty |
| **DS** | Dynamic quality and recommendation intensity with stochastic reference-quality uncertainty |

Under the stochastic scenario, reference quality follows:

\[
dr(t)
=
b\bigl(q(t)-r(t)\bigr)dt
+
\epsilon\sqrt{r(t)}\,dW(t)
\]

The static model is solved through backward induction. The dynamic models are solved using optimal control theory, dynamic programming, Hamilton–Jacobi–Bellman equations, and differential-game analysis.

Mathematica-based numerical simulations are used to compare the optimal paths and profits across the three scenarios.

## Output

| Output | Description |
|---|---|
| Optimal recommendation intensity | Platform's optimal allocation between pure and shoppable content |
| Optimal content quality | Creator's optimal pure content quality |
| Reference-quality path | Evolution of consumer expectations over time |
| User-engagement path | Evolution of platform engagement over time |
| Platform profit | Discounted revenue generated from shoppable-content views |
| Creator profit | Discounted revenue from pure-content views minus quality costs |
| Steady-state outcomes | Long-run quality, recommendation intensity, and engagement |
| Uncertainty effects | Changes in strategies and profits as reference-quality uncertainty increases |
| Scenario comparisons | Differences among static, dynamic deterministic, and dynamic stochastic decisions |
| Robustness results | Results under alternative nonlinear user-engagement functions |