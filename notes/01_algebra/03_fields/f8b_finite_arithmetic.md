#### Finite Field Arithmetic

##### Computing order of polynomials

Suppose $\bF_q$ is a **finite field**. Suppose $f(x) \in \bF_{q}[x]$ is irreducible and $\deg f(x) = d$.

Suppose $\alpha \in \overline {\bF_{q}}$ is a root of $f(x)$. We intend to compute the order $\nu:= o(f)$. Note the following facts:

- Clearly $\nu \mid q^d - 1$.
- $p(x) \mid (x^n - 1) \iff \alpha^n = 1 \iff \nu \mid n$.
  - Just notice that $p(x) \mid Q_{\nu}(x)$.
  - $p(x) \mid (x^n - 1)$ iff $\alpha^n = 1$ since all roots have the same order.
  - If $p(x) \mid (x^n - 1)$ is true in $\overline {\bF_q}[x]$, it is true in $\bF_q[x]$.

Now we describe the algorithm to determine $\nu$.

- Suppose $q^d - 1 = p_1^{e_1} \cdots p_{m}^{e_m}$, where $e_i \ge 1$, $m \ge 1$, and $p_i$ are primes.
- Similarly suppose $\nu = p_1^{f_1}\cdots p_m^{f_m}$, where $0 \le f_i \le e_i$.
- Now we can determine $f_1, \ldots, f_m$ with at most $\times e_i$ trials.

##### Finite field table

Suppose $f(x) \in \bF_q[x]$ is **primitive** with degree $n$ and a root $\alpha$. Consider field $\bF_{q^n}$.

- **Polynomial representation**: $\bF_{q^n} \simeq \bF_q[x] / (f)$.
  - $\bF_{q^n} = \c{g(\alpha): g \in \bF_q[x], \deg g < n}$.
  - Then $\c{1, \alpha^1, \ldots, \alpha^{n-1}}$ is a basis of vector space $\bF_{q^n}$ over $\bF_q$.
- **Power representation**: $\bF_{q^n} = \bF_q[\alpha]$.
  - $\bF_{q^n} = \c{0} + \c{1, \alpha^1, \ldots, \alpha^{q^n-2}}$.

For $0 \le k < q^n - 1$, we can solve for $\alpha^k = a_{n - 1}\alpha^{n - 1} + \cdots + a_0$ by computing $x^k \bmod f(x)$.

The table formed by putting all solutions together is called a **field table** of $\bF_{q^n}$ over $\bF_q$ with primitive polynomial $f(x) \in \bF_q[x]$.

##### Finding minimal polynomial

Suppose $\bF_{q^n} = \bF_{q}[\alpha]$. Now we need to find the minimal polynomial of $\alpha$.

- Recall that $\aut_{\bF_q}(\bF_{q^n}) = \a{\sigma_{q}}$.
- All conjugates of $\alpha$ is given by $\c{\alpha, \alpha^q, \ldots, \alpha^{q^{n-1}}}$.
- So $\irr (\alpha, \bF_q)$ must be
  $$
  p(x) = (x - \alpha^{q^0})(x - \alpha^{q^1})\cdots(x - \alpha^{q^{n-1}}) \in \bF_{q}[x]
  $$

##### Separable factorization of polynomials

Suppose $F$ is a field. Given $f(x) \in F[x]$ where $\deg f(x) = d > 1$.

The following procedure breaks down $f(x)$ into **separable factors**.

- Take $u(x) \in \GCD_{F[x]} (f(x), f'(x))$.
- Suppose $u(x) \in F^*$, $f$ is already separable.
- Suppose $\deg u(x) > 0$, $f$ is inseparable.
  - Suppose $f(x) = u(x) g(x)$. $g(x)$ is separable.
  - Apply the algorithm recursively to $u(x)$.
- Suppose $u(x) = f(x)$, then $f'(x) = 0$.
  - $f(x) = g(x^p) = (g(x))^p$ for some $g(x) \in F[x]$.
  - Apply the algorithm recursively to $g(x)$.
- This algorithm always stops in finitely many steps.

##### Prime factorization of polynomials (Berlekamp's algorithm)

Suppose $F$ is a field with $\char F = p$. Denote $\Z_p$ as the prime subfield of $F$.

Observe that $x^p - x = x(x-1)\cdots (x-p+1)$ in $\Z_p[x]$.

- $x^p - x$ is the defining polynomial of $\Z_p$.
- For any $g(x) \in F[x]$, we have $g(x)^p - g(x) = \prod_{i=0}^{p-1} (g(x) - i)$.
- Notice that $\c{\p{g(x) - i}}_{i = 0}^{p - 1}$ are **pairwise coprime**.

Given **separable monic** $f(x) \in F[x]$ where $\deg f(x) = d > 1$.

Also given $g(x) \in F[x]$ where $f(x) \mid g(x)^p - g(x)$ and $\deg g < d$. We have the Berlekamp's algorithm for prime factorization:

- Let $\F$ be the set of all $g(x)$ where $f(x) \mid g(x)^p - g(x)$ and $\deg g < d$.
- It turns out $\F$ can be found by solving a linear system.
  - Suppose $g(x) = g_0 + \cdots + g_{d - 1} x^{d - 1}$.
  - Then $g(x)^p - g(x) = g(x^p) - g(x) = \sum_{i=0}^{d-1} g_i (x^{ip} - x^i)$.
  - By division with remainders, $x^{ip} = f(x) h_i(x) + r_i(x)$, where $\deg r_i < d$.
  - Suppose $r_i(x) = r_{i,0} + r_{i, 1} x + \cdots + r_{i, d-1}x^{d-1}$ for all $i$.
  - Then $g(x)^p - g(x) \equiv_{f(x)} \sum_{i=0}^{d-1} g_i(r_i(x) - x^i)$.
  - So $f(x) \mid g(x)^p - g(x) \iff \sum_{i=0}^{d-1}g_i(r_i(x) - x^i) = 0$.
  - It is fairly obvious that this is a linear equation over $F$. The equation can be transformed into matrix form
    $$
    R^T G - G = 0 \iff (R^T - I)G = 0
    $$
    - Define matrix $R \in F^{d \times d}$ as $R := (r_{ij})$ for $0 \le i, j < d$.
    - Define vector $G \in F^{d}$ as $G := (g_i)$ for $0 \le i < d$.
  - The **null space** $N \subseteq F^d$ of $(R^T - I)$ can be solved with row reductions.
    -  $N$ is isomorphic to $\F$.
- $\dim \null(R^T - I)$ equals to the number of prime factors of $f(x)$ in $F[x]$.
  - Suppose $f(x)$ has $k$ (necessarily distinct) prime factors $p_0, \ldots, p_{k - 1}$. Then
    $$
    f(x) = p_0(x) \cdots p_{k-1}(x) \mid \prod_{i=0}^{d-1} (g(x) - i)
    $$
  - Since $(g(x) - i)$ are co-primes. Each $p_j$ must divides some $g(x) - u_j$, where $u_j \in \Z_p$.
  - So $g(x)$ must satisfy following congruence equations:
    $$
    0 \le i < k \quad g(x) \equiv u_i \mod p_i(x)
    $$
  - CRT guarantees a unique solution $g(x)$ modulo $f(x)$ for each choice of $u_0, \ldots, u_{k - 1} \in \Z_p^k$.
  - Therefore $\F$ is isomorphic to $\Z_p^k$. And
    $$
    p^k = |\Z_p^k| = \abs{\F} = \abs{\null(R^T - I)},\quad k = \dim\null(R^T - I) \ge 1
    $$
- Since $f(x) \mid g(x)^p - g(x)$, $f(x) = \prod_i \gcd(g(x) - i, f(x))$.
