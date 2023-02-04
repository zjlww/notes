#### Chinese Remainder Theorem

> Check TODO: Can the assumptions on rings be weakened in this section?

##### Congruence modulo an ideal

Suppose $R$ is a **nonzero ring**. And $a, b \in R$, $N \sqsubseteq R$.

- $a, b$ are **congruent** modulo $N$ if $a - b \in N$.
- Denoted as $a \equiv_N b$ or $a\equiv b \quad(\bmod N)$.
- $\equiv_N$ is clearly an equivalence relation on $R$.
- Suppose $R$ is a PID, and $N = (p)$. We can just write $a \equiv_{p} b$ or $a \equiv b \quad (\bmod p)$.

##### Coprime ideals

Suppose $R$ is a **nonzero ring**. And $I, J \sqsubseteq R$. $I, J$ are **coprime** if $I + J = R$.

Suppose $R$ is a **NCU ring**. And $I, J \sqsubseteq R$ are coprime. $IJ = I \cap J$.

- Clearly $IJ \subseteq I \cap J$.
- There exists $a \in I$ and $b \in J$ where $a + b = 1$.
- We only need to show $IJ \supseteq I \cap J$. Suppose $c \in I \cap J$.
  - Then $c = 1 \cdot c = (a + b) \cdot c = ca + cb$.
  - Since $c \in J$ and $a \in I$, $ca \in IJ$.
  - Since $c \in I$ and $b \in J$, $cb \in IJ$.
  - Therefore $c \in IJ$.

##### Chinese remainder theorem

Suppose $R$ is a **NCU ring**. And $\mathcal I = \c{I_k}_{k = 1}^n$ contains $n\ge 2$ ideals.

- Define $I =: \cap_{k = 1}^n I_k = (I_1I_2 \cdots I_n)$.
- Define $e_k \in R/I_1 \times \cdots \times R / I_n$ as $(0, \ldots, 1 + I_k, \ldots, 0)$.
- Define $\phi_k: R \to R / I_k$ as $x\mapsto x + I_k$.
- Define $\phi: R \to R/I_1 \times \cdots \times R / I_n$ as $x\mapsto (\phi_1(x), \ldots, \phi_n(x))$.

$\phi$ is a ring homomorphism where $\ker \phi = I$.

$\phi$ is surjective if and only if $\mathcal I$ is **pairwise coprime**.

- $\to$ Suppose $\phi$ is surjective.
  - For $1 \le k \le n$, let $a_k \in \phi^{-1}[\c{e_k}]$.
  - For all $1 \le i \neq j\le n$, $1 \in I_i + I_j = R$.
    - $a_i \in I_j$ since $\phi_j(a_i) = 0$.
    - $(1 - a_i) \in I_i$ since $\phi_i(1 - a_i) = \phi_i(1) - \phi_i(a_i) = 1 - 1 = 0$.

- $\from$ Suppose $\mathcal I$ is pairwise coprime.
  - Consider a fixed $1 \le k \le n$.
  - For each $i \neq k$, there exists $u_i \in I_k$ and $v_i \in I_i$, such that $u_i + v_i = 1$.
  - Define $\alpha = \prod_{i \neq k} v_{i}$. Then $\phi(\alpha) = e_k$.
    - $\phi_k(\alpha) = \phi_k\p{\prod_{i \neq k} (1 - u_{i})} = 1$.
    - For $j \neq k$, $\phi_j(1 - \alpha) = \phi_j(v_j \prod_{i \neq k, i \neq j} v_i) = 0$.
  - Therefore $\phi^{-1}[\c{x_1e_1 + \cdots + x_n e_n}]$ is not empty.
  - So $\phi$ is surjective.


When $\mathcal I$ is pairwise coprime, the **Chinese remainder theorem (CRT)** is just: $R / I \simeq R/I_1 \times \cdots \times R / I_n$.

- This immediately follows from the fundamental theorem of ring homomorphisms.

Equivalently, the **CRT** can be stated as: There exists a solution to equations $x \equiv_{I_k} a_k$ where $1 \le k \le n$ and $a_k \in R$. Any two solution are congruent modulo $I = I_1 \cdots I_n$.

#### Rings of Integers

##### The ring of integers

Consider **NCU ring** $\a{\Z, +, \cdot}$.

- $\Z$ is an integral domain. $\Z^* = \c{-1, 1}$.
- $\a{\Z, +}$ is cyclic, since $\Z = (1)$.
- $\Z$ is an Euclidean domain, with norm $v(x) := \abs{x}$ except for $v(0) = -\infty$.
- All subrings of $\Z$ are **principal ideals** of the form $n\mathbb Z = (n)$ for $n \in \Z$.
- The maximal ideals of $\mathbb{Z}$ are precisely the ideals $p \mathbb{Z}$ for prime number $p$.
- GCDs on $\Z$ are unique up to minus signs.
  - We use $\gcd: \P(\Z) \to \N$ to denote the positive GCD.


##### The ring of integers modulo n

Consider **NCU ring** $\a{\Z_n, +_n, \cdot_n}$ for $n > 1$.

- Consider the map $\phi(x) = x \bmod n$, this is a ring homomorphism from $\Z \to \Z_n$.
  - $\phi(x + y) = \phi(x) +_n \phi(y)$ and $\phi(xy) = \phi(x) \cdot_n \phi(y)$.
- $n \mathbb Z = \ker \phi$ is an ideal in $\mathbb Z$.
- $\Z/n\Z \simeq \Z_n$ by fundamental theorem of ring homomorphism.

##### Units of $\Z_n$

Consider nonzero element $[x] \in \Z_n$. Let $\Z_n^*$ be the set of units in $\Z_n$.

- $[x] \in \Z_n^* \iff \exists [y] \in \Z_n: [x][y] = [1] \iff \exists y \in \Z: xy \equiv_n  1 \iff \gcd(x, n) = 1$.
- $[x] \notin \Z_n^* \iff \gcd(x, n) = d > 1 \iff [x][n / d] = [kn] = [0]$.

$\Z_n$ is a field if and only if $n$ is a prime.



##### Euler's phi function

$\phi(n): \N^+ \to \N$ defined as
$$
\phi(n):= \abs{\Z_n^*} = \c{k \in \c{0, \ldots, n - 1}:\gcd(k, n) = 1}
$$

We have following comments:

- Suppose $m, n \in \N^+$ are coprime, then $\phi(mn) = \phi(m)\phi(n)$.
  - By CRT on ring $\Z$, we have $Z_{nm} \simeq \Z_m \times \Z_n$.
  - Therefore $(\Z_m \times \Z_n)^* \simeq \Z_{mn}^*$ and $\Z_m^* \times \Z_n^* \simeq \Z_{mn}^*$.

- For prime $p$, and positive integer $n$. $\phi(p^n)  = p^{n - 1} (p - 1)$.
  - Hint: just count $\phi(p^n)$ from the definition.

Consider cyclic group $G = \a{a}$ where $o(a) = n$.

- $\a{a^d}$ has $\phi(n/d)$ generators of order $n / d$. And they are all the elements of order $n / d$ in $G$.
- By Möbius inversion, we have


$$
n = \sum_{1 \le d \le n, d \mid n} \phi (n / d) = \sum_{1 \le d\le n, d \mid n} \phi(d) \implies \phi(n) = \sum_{d \mid n} d \mu\p{\frac{n}{d}}
$$

##### Euler's theorem

For $a, n \in \Z$ and $\gcd (a, n) = 1$, $a^{\phi(n)}\equiv_n 1$.

- Consider ring $\Z_n$ and multiplicative group $\Z_n^*$.
- $\Z_n^*$ is cyclic since it is a subgroup of a cyclic group.
- Since $\gcd(a, n) = 1$, $[a] \in \Z_{n}^*$.
- Therefore $[a]^{\phi(n)} = [1]$ in $\Z_N^*$.

##### Fermat's little theorem

For prime $p$ and any $a \in \Z$, we have $a^{p} \equiv_p a$.

- Consider field $\Z_p$.
- $[a]^{p - 1} = [1]$ is true in $\Z_p^*$ since $|\Z_p^*| = p - 1$.

Take power of $p$ on both side for $k - 1$ times gives $a^{p^k}\equiv_p a$.
