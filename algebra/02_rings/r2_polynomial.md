#### Polynomial Rings

##### Polynomial rings

Suppose $R$ be a **ring**. $R[x]$ is defined as the following set:
$$
R[x] := \{r \in R^{\N} \mid \exists N \in \N, \forall n > N:r(n) = 0\}
$$
- With an **indeterminate symbol** $x$, we may write elements in $R[x]$ **pretending** they are polynomials in the following way:
  $$
  f(x) = (a_0, \cdots, a_n, 0, \cdots) = a_0 + a_1 x + \cdots + a_n x^n \in R[x]
  $$

  - $f(x) \in R[x]$ is **not** a polynomial function. It is only a sequence $(a_0, a_1, \ldots)$. The resemblance is merely **notational** here.
  - The $a_{i}$ are called **coefficients** of $f(x)$.
  - We often omit terms with zero coefficients.
  - If $R$ has **unity** $1 \neq 0$, we will write a term $1 x^{k}$ in such a sum as $x^{k}$.
  - Suppose $f(x) \neq 0$. The highest index nonzero coefficient is called the **leading coefficient**.

- If $R$ has **unity** $1 \neq 0$, polynomials with **leading coefficient** $1$ are called **monic**.

- The **degree** of $f(x) \in R[x]$ is a function $\deg: R[x] \mapsto \c{-\infty} \cup \N$.

  - Suppose $f(x) = 0$, $\deg f(x) := -\infty$.
  - Suppose $f(x) \neq 0$. $\deg f(x): =\max\c{k \mid a_k \neq 0} \in \N$.


$R[x]$ is a ring when the binary operations on $R[x]$ are defined as if its elements are polynomials.

- **Addition** is defined as $\sum_{i}a_i x^i + \sum_ib_i x^i := \sum_i (a_i + b_i)x^i$.

- **Multiplication** is defined as $\p{\sum_i a_i x^i}\p{\sum_j b_jx^j} := \sum_i\sum_ka_{i - k}b_kx^i$.

  - Also called the **convolution** of sequences $(a_i)$ and $(b_j)$.

- $\a{R[x], +}$ is clearly an additive group.

- Convolution of finite length sequences is associative, and distributes over addition.

  - Let's give a prove using the Einstein Summation notation.

  - Multiplication is associative:
    $$
    (a_i x^i)((b_j x^j)(c_k x^k)) = (a_ix^i)(b_{m - k}c_k x^m) = (a_{l - j}(b_{j - k}c_k))x^l = a_{l - j}b_{j - k} c_k x^l
    $$

  - Multiplication distributes over addition:
    $$
    c(x) (a(x) + b(x)) = 
    c_{i - j} (a_j + b_j) x^i = 
    c_{i - j} a_j x^i + c_{i - j} b_j x^i = c(x) a(x) + c(x) b(x)
    $$


We have the following comments:

- Suppose ring $F \le E$ then ring $F[x] \le E[x]$.
- Suppose $R$ is commutative, then $R[x]$ is commutative.
- We often identify $R$ with constant polynomials in $R[x]$.

Polynomial ring of $k$ variables is a subset of $R^{\N^k}$ with **finitely many** nonzero terms.

- Under this definition $R[x_1, \cdots, x_n], R[x_1, \cdots, x_{n-1}][x_n]$ and so on are clearly isomorphic.

##### Extending homomorphisms to polynomials

Suppose $R$ and $S$ are **rings**.

Suppose $\sigma: R \to S$ is a homomorphism. We can extend the definition to $\sigma: R[x] \to S[x]$.

- Let's identify $a \in R$ with $(a, 0, 0, \ldots) \in R[x]$. Similarly for $S$ and $S[x]$.
- Extending $\sigma$ by applying $\sigma$ to each coordinate of $(a_0, a_1, \ldots) \in R[x]$.
- The extended $\sigma$ is a ring homomorphism. (Einsum notation)
  - $\sigma((a_ix^i)(b_jx^j)) = \sigma(a_{k-i}b_ix^k) = \sigma(a_{k-i}) \sigma(b_i)x^k = \sigma(a_ix^i) \sigma(b_jx^j)$.
  - $\sigma((a_i + b_i)x^i) = (\sigma(a_i) + \sigma(b_i))x^i = \sigma(a_i x^i) + \sigma(b_i x^i)$.
- The extended $\sigma$ is injective if and only if $\sigma$ is injective.

##### Evaluation homomorphism of polynomial rings

Suppose $R$ is a **NC ring**. And $s \in R$.

For $f(x) \in R[x]$, and $f(x) = \sum_i a_i x^i$. The **evaluation** of $f(x)$ at $s \in R$ is denoted as $f(s):= \sum_i a_i s^i$.

Define the **evaluation homomorphism** $\theta_s: R[x] \to S$ as $f(x) \mapsto f(s)$.

- $\theta_s$ is a ring homomorphism.
  - $\theta_s((a_ix^i)(b_j x^j)) = \theta_s(a_{k - i}b_i x^k) = a_{k-i}b_is^k = \theta_s(a_i x^i) \theta_s(b_j x^j)$.
  - $\theta_s(a_i x^i + b_i x^i) = \theta_s((a_i + b_i)x^i) = \theta_s(a_ix^i) + \theta_s(b_i x^i)$.
- $\theta_s$ is surjective.
- Suppose $f(s) = 0$ for some $s \in S$, $s$ is called a zero of $f(x)$.

##### Polynomial ring of integral domains

$R$ is an **ID** if and only if $R[x]$ is an **ID**.

- $\to$ Suppose $R$ is an integral domain.

  - $R[x]$ is clearly commutative, since $R$ is commutative.

  - The element $1 \neq 0$ is the unity in $R[x]$.

  - Suppose $a(x), b(x) \neq 0$ but $a(x) b(x) = 0$. Two nonzero leading coefficient in $R$ must product to zero. Which is not possible.
  - So $R[x]$ is an integral domain.

- $\from$ Suppose $R[x]$ is an ID, $R < R[x]$ so $R$ is an ID.

Immediately, when $F$ is a subdomain of $E$, $F[x]$ is a subdomain of $E[x]$.
