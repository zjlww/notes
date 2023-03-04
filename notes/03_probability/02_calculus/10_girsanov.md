#### Girsanov's Theorem ==TODO==

##### Radon-Nikodym derivative of Normal distributions

Consider measurable space $(\R^d, \B(\R^d))$ and Gaussian distribution $P \sim \mathcal N(\mu_1, \Sigma)$ and $Q \sim \mathcal N(\mu_2, \Sigma)$.

- Suppose $m$ is the Borel measure.

- $dP/dm = \mathcal N(x; \mu_1, \Sigma)$, and $dQ/dm = \mathcal N(x; \mu_2, \Sigma)$.

- We have $dQ / dP = (dQ / dm) / (dP / dm)$.
  $$
  \frac{dQ}{dP} = \exp(x^T \Sigma^{-1} (\mu_2 - \mu_1)  - \frac{1}{2} \mu_2^T \Sigma^{-1} \mu_2 + \frac{1}{2} \mu_1^T \Sigma^{-1} \mu_1)
  $$

Consider probability space $(\Omega, \F, P)$ and random variable $X \in \L(\Omega \to \R^d)$.

Suppose $X \sim \mathcal N(0, \Sigma)$ under $P$ and $Y = X + \theta$.

There exists a measure $Q$ where $Y \sim \mathcal N(0, \Sigma)$ and $dQ/dP = g(X)$.

- Consider $g(x) = \exp(-{x^T \Sigma^{-1}\theta - \frac{1}{2}\theta^T \Sigma^{-1}}\theta)$.
  - $p(x + \theta) = g(x) p(x)$. Or $g(x) = p(x + \theta) / p(x)$.
- $\forall A \in \B(\R^d): \int_A p(x) dx = \int_{A - \theta} g(x) p(x) dx$.
  - $Q_Y(A) = Q(Y^{-1}[A]) = Q(X^{-1}[A - \theta]) = P_X(A) = P(X^{-1}[A])$.
  - $Q(A) = E^Q[1_A] = E^P[g(X) 1_A]$.
  - Therefore $dQ/dP = g(X)$.
- Now we have $Q_Y = P_X = \mathcal N(0, \Sigma)$. 

##### Review: a special martingale

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered space.

Suppose $Z \in \F_T$, then $(Z_t) = (E[Z | \F_t])$ is a martingale.

- $E[Z_t | \F_s] = E[E[Z|\F_t]| \F_s] = E[Z|\F_s]$.

Further suppose $Z = dQ / dP$ for some other probability measure $Q$ on $\F$. Then for real random variable $Y \in \F_t$ , $E^Q[Y] = E^P[Y Z_t]$.

- Suppose $Z$, $YZ$ are integrable in $P$.
  $$
  E^P[YZ_t] = E^P[YE^P[Z|\F_t]] = E^P[YZ] = E^Q[Y]
  $$

