#### Möbius Inversion Formula

> This note is based on Field Theory by Steven Roman. See the Appendix.

##### Locally finite posets

Suppose $P$ is a poset (partially ordered sets) with partial order $\le$.

For $a, b \in P$, define $[a, b] := \c{x \in P \mid a \le x \le b}$.

$P$ is **locally finite** if for all $a, b \in P$, $[a, b]$ is finite.

##### Incidence algebra of a poset

Suppose $P$ is a locally finite poset, and $F$ is a field. Define
$$
\A(P) := \c{f: P \times P \to F\mid  \forall x, y \in P: f(x, y) \neq 0 \implies [x, y] \neq \varnothing}
$$

- $\a{\A(P), +, \cdot}$ is a linear subspace of $P \times P \to F$ over $F$.
  - $(f + g) (x, y) := f(x, y) + g(x, y)$.
  - $(c\cdot f)(x, y) = c f(x, y)$ for $c \in F$.


Define multiplication on $\A(P)$ as
$$
(f * g)(x, y) := \sum_{x \le z \le y} f(x, z) g(z, y)
$$

- $\a{\A(P), +, *}$ is a ring with **unity** $\delta(x, y) := 1(x = y)$.
- $\a{\A(P), +, \cdot, *}$ is an commutative algebra over $F$.

Commutative algebra $\a{\A(P), +, \cdot, *}$ is called the **incidence algebra** of poset $P$ over $F$.

##### Units of the incidence algebra

Suppose $\A(P)$ is the incidence algebra of locally finite poset $P$ over field $F$.

$f \in \A(P)$ is a unit (invertible) iff $\forall x \in P: f(x, x) \neq 0$.

- $\to$ Suppose there exists $g \in \A(P)$ where $f * g = \delta$.

  - $1 = \delta(x, x) = f(x, x) g(x, x)$. So $f(x, x) \neq 0$.

- $\from$ Suppose $f(x, x) \neq 0$, we can construct a inverse $g(x, y)$.

  - Define $g_R(x, x) := f(x, x)^{-1}$ for all $x \in P$.

  - Define $g_R(x, y) := 0$ for all $x, y \in P$ where $[x, y] = \varnothing$.

  - Suppose $g_R(x, y)$ is defined on all pair $x, y$ where $|[x, y]| \le n$. We can extend its definition to all pairs for $|[x, y]| = n + 1$ in the following manner:

    - In order to satisfy $\delta(x, y) = 0$,
      $$
      f(x, x)g_R(x, y) + \sum_{x < z \le y} f(x, z) g_R(z, y) = 0
      $$

    - So $g_R(x, y)$ is uniquely determined by
      $$
      g_R(x, y) = - f(x, x)^{-1}\sum_{x < z \le y} f(x, z) g_R(z, y)
      $$

  - So there exists $g_R$ that is a right-inverse. Similarly we can construct a left-inverse $g_L$.

  - Note that $g_L = g_L *(f * g_R) = (g_L * f) * g_R = g_R$.

  - So $g = g_L = g_R$ is an inverse of $f$.

##### The zeta function and the Möbius function

Suppose $\A(P)$ is the incidence algebra of locally finite poset $P$ over field $F$.

The zeta function $\zeta \in \A(P)$ is defined by $\zeta(x, y) = 1([x, y] \neq \varnothing) = 1(x \le y)$.

- $1(\cdot)$ is the indicator function.
- $\zeta$ is invertible since $\forall x \in P: \zeta(x, x) = 1$.

The **Möbius function** $\mu \in \A(P)$ is the inverse of $\zeta$.

- Note that $\forall x \in P: \mu(x, x) = 1$.

- Since $\mu * \zeta = \delta$ and $\zeta * \mu = \delta$, we have
  $$
  \sum_{x \le z \le y} \zeta(x, z) \mu(z, y) = \delta(x, y), \quad \sum_{x \le z \le y} \mu(x, z) \zeta(z, y) = \delta(x, y)
  $$

- Therefore when $x < y$ we have
  $$
  \mu(x, y) = -\sum_{x < z \le y} \mu(z, y),\quad \mu(x, y) = -\sum_{x \le z < y} \mu(z, y)
  $$

- Therefore $\mu(x, y)$ where $|[x, y]| = n + 1$ can be derived from values of $\mu(x, y)$ where $|[z, y]| \le n$. This uniquely determines the function $\mu$.

##### Möbius inversion

Suppose $\A(P)$ is the incidence algebra of locally finite poset $P$ over field $F$. Suppose $f, g: P \to F$.

Suppose $P$ has a least element denoted by $0$ where $\forall x \in P: 0 \le x$.

We have
$$
g(x) = \sum_{0 \le y \le x} f(y) \implies f(x) = \sum_{0\le y \le x} g(y) \mu(y, x)
$$
Since
$$
\begin{aligned}
\sum_{0 \le y \le x} g(y) \mu(y, x) & = \sum_{0\le y \le x}\s{\sum_{0 \le z \le y} f(z)} \mu(y, x) = \sum_{0 \le y \le x} \s{\sum_{0 \le z \le y} \zeta(z, y) f(z)}\mu(y, x)\\
& = \sum_{0 \le z \le x} \sum_{z \le y \le x}\zeta(z, y) \mu(y, x) f(z) = \sum_{0 \le z \le x} f(z) \delta(z, x) = f(x)
\end{aligned}
$$
We have a multiplicative variant of the above formula,
$$
g(x) = \prod_{0 \le y \le x} f(y) \implies f(x) = \prod_{0 \le y \le x} \s{g(y)}^{\mu(y, x)}
$$
The proof is similar, 
$$
\begin{aligned}
\prod_{0 \le y \le x} g(y)^{\mu(y, x)} & = \prod_{0 \le y \le x} \s{\prod_{0 \le z \le y} \zeta(z, y) f(z)}^{\mu(y, x)} = \prod_{0 \le z \le x} \prod_{z \le y \le x} \zeta(z, y) f(z)^{\mu(y, x)}\\
& = \prod_{0 \le z \le x} f(z)^{\sum_{z \le y \le x} \zeta(z, y)\mu(y, x)} = f(x)
\end{aligned}
$$
Suppose $P$ has a greatest element denoted by $1$ where $\forall x \in P: x \le 1$. Then we have
$$
g(x) = \sum_{x \le y \le 1} f(y) \implies  f(x) = \sum_{x \le y \le 1} \mu(x, y)g(y)
$$

##### Classical Möbius inversion

Consider locally finite poset $\N^+$ with partial order $x \le y \iff x \mid y$.

- $1$ is the least element in $\N^+$ since $\forall n \in \N^+: 1 \mid n$.

Then $\mu(x, y)$ is given by:
$$
\mu(y / x) := \mu(x, y) =\left\{\begin{array}{cl}
1 & \text { if } y / x = 1 \\
(-1)^k & \text { if } y/x=p_1 \cdots p_k \text { (distinct primes) } \\
0 & \text { otherwise }
\end{array}\right.
$$
Then $(\mu * \zeta)(x, y) = \delta(x, y)$. Suppose $y / x = p_1^{e_1} \cdots p_n^{e_n}$ where $p_1, \ldots, p_n$ are distinct primes.
$$
(\mu * \zeta)(x, y) = \sum_{x \mid z \mid y} \mu\p{z, x} = 1 + \sum_{1 \le j \le n} C_{n}^j (-1)^j = (1 - 1)^{n} = 0^n
$$
Suppose $F$ is a field, and $f, g: \N^+ \to F$, we have:
$$
f(n) = \sum_{k \mid n} g(k) \implies g(n) = \sum_{k \mid n} f(k) \mu\p{\frac{n}{k}}
$$
We also have the multiplicative version of the inversion formula:
$$
f(n) = \prod_{k \mid n} g(k) \implies g(n) = \prod_{k \mid n} f(k)^{\mu\p{{n}/{k}}}
$$
