#### Renewal Process

(**Renewal process: Review**)

Let $X, \p{X_k}_{k = 1}^\infty \sim_{\iid} F(x)$ where $F: \R \to \R$ is the distribution of $X$.

Now consider the renewal process with arrival intervals $X_k$.

- $F$ or $X$ is called **arithmetic**, if $X$ is discrete with atoms $\c{n d: n \in \N}$ for some $d \in (0, \infty)$. The largest possible $d$ is the **period** of $X$.

- Let $S_n = \sum_{k = 1}^n X_k$, and $N_t = N[0, t] = \sum_{k = 1}^\infty 1(S_k \le t)$.

- Let $F_n$ be the distribution function of $S_n$, $F_n(s) = P(S_n \le s)$, $s \ge 0$.

  - $P(N_t \ge n) = F_n(t)$. And $P(N_t = n) = F_{n + 1}(t) - F_n(t)$.
  - $F_n = F^{*n} = F * \cdots  * F$.

- The **renewal function** $M(t): [0, \infty) \to [0, \infty]$ is defined as:

  $$
  M(t) := E[N(t)] = E\s{\sum_{i = 1}^\infty 1(S_n \le t)} = \sum_{i = 1}^\infty F_n(t)
  $$
  
- The **renewal measure** $M(A) = E[N(A)]$ for $A \in \B[0, \infty)$.

  - $M(A)$ is a measure on $\B[0, \infty)$ called the **renewal measure**.

    - Suppose $A = +_{i = 1}^\infty A_i$ for $\p{A_i} \subset \B[0, \infty)$.
      $$
      M(A) = E\s{\sum_{i = 1}^\infty 1(S_i \in A)} = \sum_{i = 1}^\infty P(S_i \in A) = \sum_{i = 1}^\infty \sum_{k = 1}^\infty P(S_i \in A_k)
      $$

    - Also notice
      $$
      \sum_{k = 1}^\infty M(A_k) = \sum_{k = 1}^\infty E[N(A_k)] = \cdots = \sum_{i = 1}^\infty \sum_{k = 1}^\infty P(S_i \in A_k)
      $$

  - Suppose $M \ll \lambda$. $m \dd t = \dd M$, $m$ is called the **renewal density**.


(**Renewal equation**)

Consider a renewal process with interval distribution function $F$.

For $a \in \L([0, \infty) \to \R)$ locally bounded. A **renewal equation** for $u$ is defined as
$$
u(t) = a(t) + (u * \lambda_F) (t)
$$
with unknown $u \in \L([0, \infty) \to \R)$ locally bounded.

(**Renewal lemma**)

- $M = F + M * \lambda_F$. For all $t > 0$, we have:
  $$
  \begin{aligned}
  M(t) &= E[N(t)] = E[E[N(t)\mid X_1]] = \int_0^\infty E[N(t) \mid X_1 = s] \dd F(s)\\
  & = \int_0^t E[N(t) \mid X_1 = s] \dd F(s) + \int_t^\infty E[N(t) \mid X_1 = s]\dd F(s)\\
  & = \int_0^t (1 + M(t - s)) \dd F(s) + E[N(t) 1(X_1 > t)]\\
  & = F(t) + M * \lambda_F + 0
  \end{aligned}
  $$

- $M(0) = F(0) + M(0)F(0)$. Since for $t = 0$, we have:
  $$
  M(0) = E[N(0)] = \sum_{k = 1}^\infty F(0)^k = \frac{F(0)}{1 - F(0)}
  $$

- $F = M - F * \lambda_M$. Since $F * \lambda_M = M * \lambda_F$.

- Therefore the Laplace transform of $F$ and $M$ are related as following:
  $$
  \l[F] = \l[M] - \l[F]\l[\lambda_M] \implies \l[\lambda_F](s) = \frac{\l[\lambda_M](s)}{1 + \l[\lambda_M](s)}, \quad \l[\lambda_M] = \frac{\l[\lambda_F](s)}{1 - \l[\lambda_F](s)}
  $$

- Since $\lambda_F$ is probabilisitic, $\l[\lambda_F]$ exists, and so $\l[\lambda_F]$ also exists in some ROC containing $y$-axis.
- Distributional function $M$ and $F$ contains the same information!

(**Solving a renewal equation**)

Consider a renewal process with interval distribution function $F$.

For $a \in \L([0, \infty) \to \R)$ locally bounded. Consider renewal equation for $u$.
$$
u(t) = a(t) + (u * \lambda_F) (t)
$$
The unique locally bounded solution is $u = a + a * \lambda_M$.

- First find the Laplace transform of $\l[u]$.
  $$
  \l[u] = \l[a] + \l[u] \l[\lambda_F] \implies \l[u] = \frac{\l[a]}{1 - \l[\lambda_F]}
  $$

- Notice that
  $$
  \l[u] = \l[a](1 + \l[\lambda_M]) = \l[a]\p{1 + \frac{\l[\lambda_F]}{1 - \l[\lambda_F]}} = \frac{\l[a]}{1 - \l[\lambda_F]}
  $$

(**Poisson process: uniqueness**)

The Poisson process with rate $\lambda$ is the unique renewal process with $M(t) = \lambda t$.

- A computation shows that $\l[\lambda_F] = \lambda / (\lambda + s)$. So $f(t) = \lambda e^{-\lambda t}$.

(**Bernoulli process: uniqueness**)

When $\lambda_F$ is discrete, $\lambda_M$ will also be discrete. So we can replace $\l$ with $z$-transforms.

The Bernoulli process with rate $p$ is the unique discrete renewal process with $M(n) = u[n]np$.

- $\lambda_M(n) = M(n) - M(n - 1) = u[n - 1] p$. So $M(z) = pz / (1 - z)$.
- Now solve for $F(z) = pz / (1 - qz)$. So $P(X = n) = p q^{n - 1}$.
- This is the Geometric distribution (starting from $1$).

