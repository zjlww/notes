#### Recurrence of States

##### Counting variable

For $x \in S$, $A \subseteq S$, define $N_A$ as the variable representing number of visits to $A$.
$$
N_A := \sum_{n = 1}^\infty 1(X_n \in A);\quad N_x := N_{\c x}
$$
##### Potential matrix $R$

Define the **potential matrix** $R: S^2 \to [0, \infty]$ as:
$$
R(x, A) := \sum_{n = 0}^\infty P_n(x, A), \quad R(x, y) := R(x, \c y)
$$

- $R(x, A)$ is a kernel.
- $R(x, A)$ is the expected number of visits to $A$ starting from $X_0 = x$.
  $$
  R(x, A) = \sum_{n = 0}^\infty P_n(x, A) = E_x\s{\sum_{n = 0}^\infty 1(X_n = A)} = E_x[N_A]
  $$

For $\alpha \in (0, 1]$, define $\alpha$-potential matrix $R_\alpha: S^2 \to [0, \infty]$ as:
$$
R_\alpha(x, A) := \sum_{n = 0}^\infty \alpha^n P_n(x, A), \quad R_\alpha(x, y) = R_\alpha(x, \c y)
$$

- $R_\alpha(x, A)$ is a kernel.
- $R_\alpha(x, A)$ is basically the $z$-transform of $P_n(x, A)$.
- $R_\alpha$ is bounded by $1/(1 - \alpha)$ when $\alpha \in (0, 1)$. Since
  $$
  R_\alpha(x, S) = \sum_{n = 0}^\infty \alpha^n = \frac{1}{1-\alpha}
  $$

##### Hitting time

Suppose $A \subseteq S$ is nonempty. The hitting time to $A$ is
$$
\tau_A := \inf \c{n \in \N^+: X_n \in A}
$$

- $\c{\tau_A = n} = \c{X_{1:n}\notin A, X_n \in A}$.
- $\tau_x: =\tau_{\c{x}}$ for $x \in S$.
- $\tau_A = \min \c{\tau_x: x \in A}$.
- Define $\inf \varnothing = + \infty$, so $\tau_A$ takes values in $\N^+ \cup \c{\infty}$.

##### Hitting matrix

Define following matrices, for $x \in S, A \subseteq S$,

- $H_n(x, A) := P(\tau_A = n \mid X_0 = x)$. And $H_n(x, y) := P(\tau_y = n \mid X_0 = x)$.
  - Notice that $H_1(x, A) = P(x, A)$.
- $H(x, A) := P(\tau_A < \infty \mid X_0 = x)$. And $H(x, y) := P(\tau_y <\infty\mid X_0 = x)$.
  - $H(x, A) = \sum_{n = 1}^\infty H_n (x, A)$.
  - $1 - H(x, A) = P(\tau_A = \infty \mid X_0 = x)$.

To be consistent with the book, define:
$$
f_{ij}^{(n)} := P(\tau_j = n \mid X_0 = i) = H_n(i, j);\\
f_{ij} := P(\tau_j < \infty \mid X_0 = i) = \sum_{n = 1}^\infty f_{ij}^{(n)} = H(i, j);
$$

Define the expected hitting time as
$$
\mu_{ij} := E[\tau_j \mid X_0 = i] = \sum_{n = 1}^\infty n f_{ij}^{(n)}
$$

##### Expected hit matrix

For $x \in S$ and $A \subseteq S$. Define the expected number of hits to $A$.
$$
G(x, A) := E(N_A \mid X_0 = x), \quad G(x, y):= G(x, \c y)
$$

- $G(x, A)$ is a kernel. Since $G(x, A) = \sum_{n = 1}^\infty P_n(x, A)$.
- $G(x, A) = R(x, A) - P_0(x, A)$.
  - Recall that $R(x, A) = \sum_{n = 0}^\infty P_n(x, A)$.
- $E[N_j\mid X_0 = i] = \sum_{n = 1}^\infty p_{ij}^{(n)}$.

##### Recurrent and transient

For state $i \in S$.

- State $i$ is transient if $f_{ii} < 1$.
- State $i$ is recurrent if $f_{ii} = 1$.

##### Hitting matrix and transition matrix

$f_{ij} > 0 \iff i \to j$.

- Notice that $f_{ij} \ge p^{(n)}_{ij} \ge f_{ij}^{(n)}$ is true.
- $\to$ since $p_{ij}^{(n)} \ge f_{ij}^{(n)} > 0$ for some $n \in \N^+$.
- $\from$ since $f_{ij} \ge p^{(n)}_{ij}$ for some $n\in \N^+$.

$p_{ij}^{(n)} = \sum_{k = 1}^n f_{ij}^{(n)} p_{jj}^{(n)}$ for $n \in \N^+$.

- Conditioning on $\tau_y = k$ gives the result:
  $$
  P(X_n = j \mid X_0 = i) = \sum_{k = 1}^n P(X_n = j, \tau_y = k \mid X_0 = i)
  $$

$f_{ij}^{(n + 1)} = \sum_{k \neq j} p_{ik} f_{kj}^{(n)}$ for $n \in \N^+$.

- Conditioning on $X_1 = k$ gives the result.
  $$
  P(X_{n} = j, X_{1:n} \neq j \mid X_0 = i) = \sum_{k \neq j} P(X_n = j, X_{2:n}\neq j, X_1 = k \mid X_0 = i)
  $$

##### Equivalent definition of recurrence

For $i, j \in S$, we have

- $P(N_j = 0 \mid X_0 = i) = 1 - f_{ij}$.
- $P(N_j = n \mid X_0 = i) = f_{ij} f_{jj}^{n - 1}(1 - f_{jj})$ for $n \ge 1$.

Suppose $j \in S$ is transient. Then $f_{jj} < 1$.

- $P(N_j < \infty \mid X_0 = i) = 1$.
- The expected hits to $j$ starting from $i$ is
  $$
  \sum_{n = 1}^\infty p_{ij}^{(n)} = E[N_j \mid X_0 = i] = \sum_{n = 1}^\infty n P(N_j = n \mid X_0 = i) = \frac{f_{ij}}{1 - f_{jj}} < \infty
  $$

Suppose $j \in S$ is recurrent. Then $f_{jj} = 1$.

- $P(N_j = 0 \mid X_0 = i) = 1 - f_{ij}$.
- $P(N_j = \infty \mid X_0 = i) = f_{ij}$.
- $\sum_{n = 1}^\infty p_{ij}^{(n)} = \infty \cdot f_{ij}$.

So we have the following relationship:

- $j \in S$ is transient iff $f_{jj} < 1$ iff $\sum_{n = 1}^\infty p_{jj}^{(n)} < \infty$.
- $j \in S$ is recurrent iff $f_{jj} = 1$ iff $\sum_{n = 1}^\infty p_{jj}^{(n)} = \infty$.

##### Recurrence is contagious

Suppose $i \in S$ is recurrent and $i \to j$, then $j$ is recurrent, and $f_{ij} = f_{ji} = 1$.

- When $i = j$ the result is trivial. Now assume $i \neq j$.
- There exists a minimum $n \in \N^+$ where $p_{ij}^{(n)} > 0$.
- $1 - f_{ii} \ge p_{ij}^{(n)} (1 - f_{ji})$. But $f_{ii} = 1$, which implies $f_{ji} = 1$.
- So $j \to i$. There exists $m \in \N^+$ where $p_{ji}^{(m)} > 0$.
- Notice the following:
  $$
  p_{jj}^{(m + k + n)} \ge p_{ji}^{(m)} p^{(k)}_{ii} p^{(n)}_{ij}
  $$
- Therefore $\sum_{n = 1}^\infty p_{jj}^{(n)} = \infty$. So $j$ must be recurrent.
- Now by symmetry, $f_{ij} = f_{ji} = f_{ii} = f_{jj} = 1$.

So recurrence is also a class property. A class $T$ is recurrent if all states are recurrent.

- A recurrent class is closed.
  - Suppose $T$ is not closed, and $x \in T$, $x \to y$, $y \notin T$.
  - Then $y \to x$ by above theorem. Contradiction.
- A closed finite class $T$ is recurrent.
  - $P(N_T = \infty \mid X_0 = i) = 1$. For any $i \in T$.
  - So $P(N_j = \infty \mid X_0 = i) > 0$ for some $j \in T$.
  - Therefore $\sum_{n = 1}^\infty p_{ij}^{(n)} = \infty$.
  - Now suppose $p_{ji}^{(k)} > 0$. Since $p_{jj}^{(n)} \ge p_{ji}^{(k)} p_{ij}^{(n - k)}$.
  - Clearly $\sum_{n = 1}^\infty p_{jj}^{(n)} = \infty$ as well. So $j$ is recurrent.
