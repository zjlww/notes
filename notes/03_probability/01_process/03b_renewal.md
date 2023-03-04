#### Renewal Limit Theorems

> Consider renewal process:
>
> - Let $X, \p{X_k}$ be the i.i.d.arrival intervals with distribution function $F(t)$.
> - Let $\p{S_k}$ be the arrival times.
> - Let $N(t)$ be the counting process of a renewal process with renewal function $M(t)$.
> - Let $\mu = E[X] \in (0, \infty]$.
> - Let $\sigma^2 = \var(X)$ when it exists.

##### Renewal SLLN

$N_t / t \to 1 / \mu$ as $t \to \infty$ essentially pointwise.

- For $t$ large enough, $N_t > 0$ and 
  $$
  \frac{S_{N_t}}{N_t} \le \frac{t}{N_t} \le \frac{S_{N_{t} + 1}}{N_t}
  $$
- ${S_{N_t}}/{N_t} \to \mu$ essentially pointwise following standard **SLLN**.
- $S_{N_{t} + 1} / (N_{t} + 1) \to \mu$ essentially pointwise as well.
- $(N_t + 1) / N_t \to 1$ essentially pointwise.
- Now by squeezing, $N_t / t \to 1 / \mu$.

##### Elementary renewal theorem

$M_t / t \to 1 / \mu$ as $t \to \infty$.

- $\liminf_{t \to \infty} M(t) / t \ge 1 / \mu$.
  - When $\mu = \infty$, this is trivial. Now suppose $\mu < \infty$.
  - $S_{N_t + 1} > t$. So $E[S_{N_t + 1}] = E[N_t + 1] \mu = \s{M(t) + 1} \mu > t$.
    - $N_t + 1$ is a stopping time of $\p{X_k}$. Now apply Wald's equation.
  - Therefore $M(t)/t > 1 / \mu - \mu/t$.
- $\limsup_{t \to \infty} M(t) / t \le 1 / \mu$.
  - Truncate $X_{a, i}:= \min(X_i, a)$, where $a > 0$.
  - $S_{a, N_t + 1} \le t + a$ for $t > 0$.
  - So $[M_a(t) + 1] \mu \le t + a$ from Wald's equation.
  - Therefore
    $$
    \frac{M(t)}{t} \le \frac{M_a(t)}{t} \le \p{\frac{1}{\mu} + \frac{a}{t \mu}} - \frac{1}{t}
    $$

##### Renewal Theorem / Blackwell's Theorem ==TODO==

For $h > 0$, $M(t, t + h] \to h / \mu$ as $t\to \infty$. Or equivalently $N(t, t + h] \to h / \mu$ in $\L^1$-norm.

- For **arithmetic** renewal processes $h$ should be multiples of span $d$.

##### Delayed renewal process

Suppose $X_1$ is allowed to have a different distribution with $P(X_1 > 0) > 0$. Such a renewal progress is called a **delayed renewal process**.

- We still use $F$ and $M$ as the old distribution function, and the old renewal function.
- Let $G$ denotes the distribution function of $X_1$.
- Let $G_n = G * F_{n - 1}$ for $n \ge 2$, and $G_1 = G$ be the distribution functions of $S_n$.
- Let $U(t) := E[N_t]$ be the delayed renewal function.
  $$
  U(t) = E[N_t] =  \sum_{n = 1}^\infty G_n(t) = E\s{\sum_{n = 1}^\infty 1(S_n \le t)} = \sum_{n = 1}^\infty P(S_n \le t)
  $$
