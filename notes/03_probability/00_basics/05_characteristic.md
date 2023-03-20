#### Characteristic Functions ==TODO==

##### Characteristic functions of real valued random variables

Suppose on probability space $(\Omega, \F, P)$, there is random variable $X \in \L(\Omega \to \R^n, \F / \B[\R^n])$.

Define the **characteristic function** $\varphi_X(\lambda):\R^n \to \C$ as
$$
\varphi_{X}(\lambda) := E\s{e^{i \lambda \cdot X}}
$$

#### Central Limit Theorem

##### Central limit theorem ==TODO==

Suppose $(X_i)_{i = 1}^\infty$ are independent identically distributed, real-valued random variables with $E[X_i] = m$ and $\var[X_i] = \sigma^2 > 0$.

Let $S_n := \sum_{i = 1}^n X_i$. So $E[S_n] = n m$ and $\var[S_n] = n\sigma^2$. Then we have
$$
\forall -\infty < a < b < \infty: \lim_{n \to \infty} P\p{a \le \frac{S_n - nm}{\sqrt{n}\sigma} \le b} = \frac{1}{\sqrt{2\pi}} \int_a^b \exp\p{-\frac{x^2}{2}} \dd x
$$
