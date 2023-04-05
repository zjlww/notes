#### Bernoulli Family

> Many distributions are functions of i.i.d. Bernoulli trials...

##### Bernoulli distribution

$X: \Omega \to \c{0, 1}$ has **Bernoulli** distribution.

- Denoted as $X \sim \operatorname{Bernoulli}(p)$ when $P(X = 0) = q$ and $P(X = 1) = p = 1-q$.
- $E[z^X] = q + pz$.
- $E[X] = p$, $E[X^2] = p$. $\var(X) = pq$.

##### Binomial distribution

Suppose independent $X_1, \ldots, X_n \sim \operatorname{Bernoulli}(p)$. Let $X = X_1 + \cdots + X_n$.

Then $X$ has **Binomial** distribution.

- $X \sim \operatorname{Binomial}(n, p)$.
- For $0 \le x \le n$ we have
  $$
  P(X = x) = \p{\begin{array}{c}n \\ x \end{array}} p^x q^{n -x}
  $$
- $E[z^X] = (q +pz)^n$.
- $E[X] = np$, $E[X^2] = n(n-1) p^2 + np$, $\var(X) = npq$.
- Binomial distribution is a special case of Multinomial distribution.

##### Categorical distribution

$X: \Omega \to \c{1, \dots, k}$ has **Categorical** distribution.

- Denoted as $X \sim \operatorname{Categorical}(k, \symbf p)$ when $P(X = i) = p_i$. Where $\sum p_i = 1$.

##### Multinomial distribution

Suppose independent $C_1, \ldots, C_n \sim \operatorname{Categorical}(k, \symbf p)$. $\symbf p = (p_1, \ldots, p_k)$.

For $1 \le i \le k$. Define $X_i = \sum_{m=1}^{n} 1(C_m = i)$.

Then $\symbf X = (X_1, \ldots, X_k)$ has **Multinomial** distribution with parameter $n$ and $\symbf p = (p_1, \ldots p_k)$.

- Denoted as $\symbf X \sim \operatorname{Multinomial}(n, \symbf p)$.
- When $x \in \N^k$ and $|\symbf x| = n$, by **multinomial theorem**:
  $$
  P(\symbf X = \symbf x) = \p{\begin{array}{c} n \\x_1, \ldots, x_k\end{array}} \prod_{i = 1}^k p_i ^{x_i} = \frac{n !}{\prod_{i=1}^k x_k!} \prod_{i=1}^{k} p_i^{x_i}
  $$
- For $1 \le i \le k$, we have $X_i \sim \operatorname{Binomial}(n, p_i)$.

##### Conditioned Multinomial distribution

Denoted as $\symbf X \sim \operatorname{Multinomial}(n, \symbf p)$. Where $\symbf p = (p_1, \ldots, p_k)$.

Given subspace $\c{X_j = m}$, $\bY :=\bX_{-j} \sim \operatorname{Multinomial}(n - m, \symbf p / (1 - p_j))$.

- When $|\symbf x| = n$ and $\symbf x_j = m$. By definition:
  $$
  P(\bX = \symbf x | X_j = m) = \frac{P(\bX = \symbf x)}{P(X_j = m)} = \frac{\frac{n !}{\prod_{i=1}^k x_k!} \prod_{i=1}^{k} p_i^{x_i}}{\frac{n!}{(n-m)!m!}p_j^m (1 - p_j)^{n - m}}
  $$
- Observe that some terms cancel and leads to:
  $$
  P(\symbf X = \symbf x |X_j = m) =  \frac{(n - m) !}{\prod_{i\neq j} x_k!} \prod_{i \neq j} \left({\frac{p_i}{1-p_j}}\right)^{x_i}
  $$

#### Bernoulli Process

##### Bernoulli process

$\p{X_k}_{k=1}^\infty \sim_{\operatorname{i.i.d.}} \operatorname{Bernoulli(p)}$, where $p \in (0, 1]$ is called a **Bernoulli process**.

##### Geometric Distribution

Consider $X:= \inf \c{k \ge 1: X_k = 1} - 1$. $X$ has **Geometric distribution**.

- Denoted as $X \sim \operatorname{Geometric}(p)$.
- $X$ is the number of failures before first success.
- $P(X = k) = q^k p$ for $k \in \N$.
- $E[z^X] = p / (1 - qz)$.
- $E[X] = q/p$, $E[X^2] = q(1 + q) / p^2$, and $\var(X) = q / p^2$.
- Recursive solution for $E[X]$ and $E[X^2]$ exists.
  - $E[X] = E[X | X_1 = 0] q + E[X | X_1 = 1] p = (1 + E[X])q$.
  - $E[X^2] = E[X^2 | X_1 = 0] q = q E[(X + 1)^2]$.

##### Expectation of Geometric distribution

Suppose $P(X = n) = p q^{n}$ for $n \ge 0$.

Computing the mean is actually simple, and does not require z-transform...

$$
E[X] = \sum_{n = 0}^\infty n p q^{n} = (1 - q) \sum_{n = 0}^\infty n q^{n} = \sum_{n = 1}^\infty n q^{n} - \sum_{n = 1}^\infty (n - 1) q^n = \frac{q}{1 - q} = \frac{q}{p}
$$

##### Negative binomial distribution: failures before success

Suppose $\p{X_k}_{k=1}^\infty \sim_{\operatorname{i.i.d.}} \operatorname{Bernoulli(p)}$, where $p \in (0, 1]$.

Define $X: \Omega \to \N \cup \c{\infty}$ as the number of failures before $r \in \N^+$ successes.

Then $X$ has the Negative Binomial distribution.

- Denoted as $X \sim \operatorname{NegBinomial}(p, r)$.
- $P(X = \infty) = 0$ and for $k \in \N$:
  $$
  P(X = k) = \p{\begin{array}{c} r + k - 1 \\ k\end{array}} p^{r}q^{k}
  $$
  - where $C_{r + k - 1}^{r - 1}$ is the number of ways to insert $r - 1$ successes into $k$ failures.

##### Negative binomial distribution: sum of geometric variables

Suppose $\p{X_k}_{k=1}^\infty \sim_{\operatorname{i.i.d.}} \operatorname{Geometric(p)}$, where $p \in (0, 1]$.

Given $r \in \N^+$, define $X := X_1 + \cdots + X_r$. Then $X \sim \operatorname{NegBinomial}(p, r)$.
$$
E[z^X] = p^r/(1-qz)^r = \left(\sum_{k=0}^\infty q^k p z^k\right)^r = p^r\left(\sum_{k=0}^\infty (qz)^k\right)^r = \sum_{k=0}^\infty C_{k+r-1}^{r-1} q^k p^r z^k
$$
