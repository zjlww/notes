#### Limiting Distributions of DTMC

##### Bounded counting variable

Suppose $j \in S$ and $n \in \N^+$. Define
$$
N_{j}(n) := \sum_{k = 1}^n 1(X_k = j), \quad \tau_{j}(n) := \min\c{k \in \N^+:N_{j}(k) = n}
$$

- Clearly $N_{j}(n) \to N_j$ pointwise as $n \to \infty$.
- $\tau_j(n)$ is the time of $n$-th hit to state $j$.
  - $\tau_j(n)$ is a stopping time.
  - $\tau_j = \tau_j(1)$. Define $\tau_j(0) := 0$.

Define pre-$n$ counting matrix $G_n(i, j)$ as
$$
G_n(i, j) := E[N_j(n) \mid X_0 = i] = \sum_{k = 1}^n p_{ij}^{(k)}
$$

- Recall that $G(i, j) = E[N_j \mid X_0 = i]$. $G_n(i, j) \uparrow G(i, j)$ as $n \to \infty$.

##### Embedding renewal process in DTMC

Given $\c{X_0 = i}$, $i \to j$ where $j$ is recurrent.

It is easy to show $\p{\tau_j(n + 1) - \tau_j(n)}_{n = 0}^\infty$ are independent.

- For $n \ge 1$, they are i.i.d. random variables.
- For $n = 0$, $\tau_j$ has different distribution than the other variables.
- When $i \neq j$, note that $P\c{\tau_j = \infty} = 1 - f_{ij}$.

$\tau_j(n)$ are the arrival times of a **(delayed) renewal process**.

- $N_j(n)$ is the counting process of the renewal process.
- And $G_n(i, j) = E[N_j(n) \mid X_0 = i]$ happens to be the renewal function.

##### Limit of counts

Given $j \in S$, consider the limit of $N_j (n) / n$ given $\c{X_0 = i}$.

- Suppose $i \to j$ and $j \in S$ is **recurrent**.
  - On $\c{X_0 = i, \tau_j = \infty}$, $N_j(n) / n = 0$ pointwise for all $n$.
  - On $\c{X_0 = i, \tau_j < \infty}$, $N_j(n) / n \to 1 / \mu_{jj}$ essentially pointwise.
  - $E[N_j(n) / n \mid X_0 = i, \tau_j < \infty] \to 1 / \mu_{jj}$.
    - Following from elementary renewal theorem.
  - $E[N_j(n) / n \mid X_0 = i] \to f_{ij} / \mu_{jj}$.
- Suppose $i \to j$ and $j \in S$ is **transient**.
  - On $\c{X_0 = i, \tau_j = \infty}$, $N_j(n) / n = 0$ pointwise for all $n$.
  - On $\c{X_0 = i, \tau_j < \infty}$, $N_j(n) / n \to 0$ essentially pointwise.
    - Since $N_j(n) \le N_j$ and $P(N_j < \infty \mid X_0 = i) = 1$.
  - $E[N_j(n) / n\mid X_0 = i] \to 0$.
    - Since $\sum_{k = 1}^\infty p_{ij}^{(k)} < \infty$.
    - Notice that $\mu_{jj} = \infty$, so this agrees with the recurrent result.

##### Limit of transition probabilities

Given **recurrent** state $j \in S$, consider the limit of $p_{ij}^{(n)}$.

- When $j$ is **aperiodic**, $p_{ij}^{(n)} \to f_{ij} / \mu_{jj}$.

  - Notice the following:
    $$
    P(X_{n + 1} = j \mid X_0 = i, \tau_j < \infty) = E[N_j(n + 1) - N_j(n)\mid X_0 = i, \tau_j < \infty] \to \frac{1}{\mu_{jj}}
    $$

  - Therefore
    $$
    P(X_{n + 1} = j \mid X_0 = i) \to \frac{1}{\mu_{jj}} P(\tau_j < \infty \mid X_0 = i) = \frac{f_{ij}}{\mu_{jj}}
    $$

- When $j$ is **periodic** with period $d$, and $[i] = [j]$, where $i \to_k j$, then $p_{ij}^{(nd + k)} \to d / \mu_{jj}$.

  - Notice the following:
    $$
    E[N_j(n + d) - N_j(n)\mid X_0 = i] \to \frac{d}{\mu_{jj}}
    $$

For transient state $j \in S$, $p_{ij}^{(n)} \to 0$.

- Since $\sum_{k=1}^\infty p_{ij}^{(k)} = f_{ij} / (1 - f_{jj}) < \infty$.
- Notice that $\mu_{jj} = \infty$, so this agrees with the recurrent result.

##### Positive recurrent / null recurrent

Suppose $i \in S$ is recurrent.

- $i$ is positive recurrent if $\mu_{ii} < \infty$.
- $i$ is null recurrent if $\mu_{ii} = \infty$.

Suppose $i$ is positive recurrent and $i \to j$, then $j$ is positive recurrent.

- We have shown that $j$ is recurrent, and $i \lr j$.
- So for some $n, m$ we have $p_{ij}^{(n)}, p_{ji}^{(m)} > 0$.
- So $p^{(n + k + m)}_{jj} \ge p_{ji}^{(m)} p_{ii}^{(k)} p_{ij}^{(n)}$.
- w.l.o.g. suppose $i$ is aperiodic. Now take $k \to \infty$.
- So $\lim_{k \to \infty}p_{jj}^{(k)} > 0$. And $j$ is positive recurrent.

So a recurrent class is either positive recurrent or null recurrent.

A **closed and finite** class $T$ is positive recurrent.

- Consider any $i \in T$ with period $d$.
- The limiting theorem says that $\sum_{k = n + 1}^{n + d} p_{ij}^{(k)} \to d / \mu_{jj}$.
- Now sum over $j \in T$. Some $\mu_{jj} < \infty$ must be true.
- So $j$ is positive recurrent.

A closed and finite set $T$ does not contain null recurrent states.

- Suppose $x \in T$ is null recurrent. $[x]$ is a closed finite class.
- So $x$ must be positive recurrent. Contradiction.

##### Ergodic chain

A state that is positive recurrent and aperiodic is called **ergodic**.

A chain that is irreducible with ergodic states is called an **ergodic chain**.

#### Invariant Distributions of DTMC

##### Invariant function

A function $\pi: S \to [0, \infty)$ is **invariant** for $P$ if
$$
\forall j \in S: \pi_j = \sum_{i \in S} \pi_i P(i, j)
$$
$\pi$ that is invariant for $P$ must also be invariant for $P_n$ and $G_n / n$.

Now by dominated convergence, when $\sum_{i \in S} \pi_i < \infty$ we have
$$
\forall j \in S: \pi_j = \lim_{n \to \infty} \sum_{i \in S} \pi_i \frac{G_n(i, j)}{n} = \frac{1}{\mu_{jj}} \sum_{i \in S} \pi_i f_{ij}
$$
When $\sum_{i \in S} \pi_i = 1$, $\pi$ is called an invariant distribution for $P$.

When an invariant distribution does exist, it **concentrates on positive recurrent** states.

- When $\mu_{jj} = \infty$, that is when $j$ is transient or null recurrent. $\pi_j = 0$.

When the Markov chain is irreducible positive recurrent. $\pi_i = 1 / \mu_{ii}$ is the unique **invariant function**, and it happens to be a distribution.

- Let $C = \sum_{i \in S} \pi_i$, we can show that $C \le 1$.

  - $\sum_{j \in A} G_n(i, j) / n \le 1$ for finite $A \subseteq S$.
  - Now take limit $n \to \infty$ on both sides. $\sum_{j \in A} \pi_j \le 1$.
  - Since this is true for all finite $A$, $C \le 1$.

- Now we can show that $\pi_i$ is an invariant function for $P$.

  - For any finite $A \subseteq S$,
    $$
    \sum_{k \in A} \frac{G_{n}(i, k)}{n} p_{kj} \le \frac{G_{n + 1}(i, j)}{n}
    $$

  - Now take limits $n \to \infty$ on both sides:
    $$
    \sum_{k \in A} \pi_k p_{kj} \le \pi_j
    $$

  - Therefore
    $$
    \sum_{k \in S} \pi_k p_{kj} \le \pi_j
    $$

  - The equality is obtained. Otherwise, sum over $j$ gives, contradiction.
    $$
    \sum_{k \in S} \pi_k < \sum_{j \in S} \pi_j
    $$

- $\pi / C = \pi$ due to the limit result above. So $C = 1$.

If the Markov chain is irreducible recurrent (but may be null recurrent). There exists a unique positive invariant function up to multiplication.

- For $x \in S$ define
  $$
  \gamma_x(y) := E\s{\sum_{n = 0}^{\tau_x - 1} 1(X_n = y) \mid X_0 = x} = E\s{\sum_{n = 1}^{\tau_x} 1(X_n = y) \mid X_0 = x}
  $$

- Clearly $\gamma_x(x) = 1$.

- $\gamma_x (y)$ is invariant for $P$.
  $$
  \begin{aligned}
  \gamma_x(y)
  &= \sum_{n= 1}^\infty P\p{X_n = y, \tau_x \ge n \mid X_0 = x} \\
  &= \sum_{n = 1}^\infty \sum_{z \in S} P\p{X_n = y, X_{n - 1} = z, \tau_x \ge n \mid X_0 = x}\\
  &= \sum_{n = 1}^\infty \sum_{z \in S} P\p{X_n = y \mid X_{n - 1} = z, \tau_x \ge n, X_0 = x} P\p{X_{n - 1} = z, \tau_x \ge n \mid X_0 = x}\\
  &= \sum_{n = 1}^\infty \sum_{z \in S} P(z, y) P\p{X_{n - 1} = z, \tau_x \ge n \mid X_0 = x}\\
  &= \sum_{z \in S} P(z, y) E\s{\sum_{n = 1}^{\tau_x} 1(X_{n - 1} = z) \mid X_0 = x} = \sum_{z \in S} P(z, y)\gamma_x(z)
  \end{aligned}
  $$

- $\gamma_x(y) \in (0, \infty)$.

  - Suppose $P_k(x, y) > 0$ and $P_j(y, x) > 0$.
  - $\gamma_x(y) = (\gamma_x P_k)(y) \ge \gamma_x(x) P_k(x, y) > 0$.
  - $\gamma_x(x) = (\gamma_x P_j)(x) \ge \gamma_x(y) P_j(y, x) > 0$.

- Uniqueness ==TODO==

