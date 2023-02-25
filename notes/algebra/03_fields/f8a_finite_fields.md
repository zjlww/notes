#### Finite Fields

##### Finite extension of finite fields

Suppose $F$ is a **finite field**. And extension $E/F$ is finite. $[E:F] = n$. Then $\abs{E} = \abs{F}^n$.

- Since $E$ is a $n$-dimensional vector space over $F$.
- Enumerate the coordinates on any finite basis gives the total count of $\abs{F}^n$.

##### Size of a Finite Field

Suppose $F$ is a **finite field**. $\abs{F}$ is some power of a prime.

- Suppose $\Z_p$ is the prime subfield of $F$.
- Then field extension $F/\Z_p$ is finite. And $|F| = |N|^n = p^n$.

##### Group primitives

Suppose $F$ is a **finite field**. Then $\a{F^*, \cdot}$ is a cyclic group.

A **generator** of $F^*$ is a (group) **primitive** of finite field $F$.

##### Defining polynomial of finite fields

Suppose $F$ is a **finite field**. And $|F| = q = p^n$.

- Since $F^*$ is cyclic, $\forall x \in F^*: x^{q - 1} = 1$.
- Therefore $\forall x \in F: x(x^{q - 1} - 1) = x^q - x = 0$.
- Consider $f(x) = x^q - x \in F[x]$.
- $F$ is **exactly the set of all roots** of $f(x)$ in $F$.
  - $f(x)$ is clearly separable.
  - $F$ is the splitting field of $x^q - x$ (over the prime subfield $\Z_p$).


The polynomial $f(x)$ is called the **defining polynomial** of $F$.

##### Power of polynomials

Suppose $F$ is a **finite field**. And $|F| = p^n = q$. For any polynomial $f(x) \in F[x]$:
$$
f^q(x) = \p{\sum_{i = 0}^m a_i x^i}^q= a_0^{q} + \p{\sum_{i=1}^m a_i x^i}^{q} =\cdots =\sum_{i=0}^m a_i x^{iq} = f(x^q)
$$
- Note that we are using the rule $(a + b)^{p^n} = a^{p^n} + b^{p^n}$ repeatedly.

##### Finite fields of the same size are isomorphic

Suppose $F$ and $F'$ are **finite fields** of order $p^n$. Where $p$ is prime and $n \in \N^+$.

- Both $F$ and $F'$ has prime subfield $\Z_p$ up to field isomorphism.
- They are both splitting fields of $f(x) = x^{p^n} - x$.
- Therefore $F \simeq F'$.

Therefore we can write $\bF_{p^n}$ as a generic finite field of order $p^n$. And we can treat all finite fields of the same order as the same entity (up to isomorphism).

##### Existence of a finite field of order $p^n$

Suppose $q = p^n$, $n \in \N^+$, and $p$ is a prime. There exists a finite field $F$ of size $p^n$.

- Consider $f(x) = x^q - x = x(x^{q-1} - 1) \in \Z_p[x]$.
- $f(x)$ is separable.
  - $f'(x) = qx^{q - 1} - 1 = -1$.
  - So $\gcd(f, f') = 1$.
- $f(x)$ splits in $\overline \Z_p$. Suppose the **set of roots** is $F \subseteq \overline \Z_p$.
- $F$ is a **finite field** of order $p^n$, since
  - $\forall \alpha, \beta \in F: (\alpha - \beta)^q = \alpha^q - \beta^q = \alpha - \beta$ so $(\alpha - \beta) \in F$.
  - $\forall \alpha \in F, \beta \in F^*:(\alpha \beta^{-1})^q = (\alpha \beta^{-1})$ so $\alpha/\beta \in F$.
- Since $1 \in F$, $\Z_p \subseteq F$.

#### Towers of Finite Fields

##### Factorization Lemma

Suppose $0 < k < n$. $k \mid n \iff (x^k - 1) \mid (x^n - 1)$ in $F[x]$ for any field $F$.

- Suppose $n = mk + r$ where $0 \le r < k$.
- When $m \ge 1$ we have $x^{mk + r} - 1 = x^k\p{x^{(m-1)k + r} - 1} + (x^k - 1)$.
- Therefore
  $$
  (x^k - 1) | (x^{mk + r} - 1) \iff (x^k - 1) | (x^{(m-1)k + r} - 1) \iff (x^k - 1) | (x^r - 1)
  $$
- since $r < k$, this is true iff $r = 0$.

For $m \ge 1$, we have the following expansion:
$$
x^{mk + r} - 1 = \p{x^k - 1}\p{1 + x^k + \cdots + x^{(m-1)k}} + x^k\p{x^r - 1}
$$
##### Towers of finite fields

Suppose $p$ is a prime, now we work inside algebraic closure $\overline \Z_p$.

Now suppose $q = p^N$ for some $N \ge 1$. Now for $0 < d < n$, the following are equivalent:

1. $d \mid n$.
2. $q^d - 1 \mid q^n - 1$.
3. $x^{q^d - 1} - 1 \mid x^{q^n - 1} - 1$ in $\overline \Z_{p}[x]$.
4. $x^{q^d} - x \mid x ^{q^n} - x$ in $\overline \Z_p[x]$.
5. $\bF_{q^d} \le \bF_{q^n}$.

Proof:

- $1 \to 2$ immediately follows from factorization lemma.
- $2 \leftrightarrow 3 \leftrightarrow 4 \leftrightarrow 5$ is apparent.
- $5 \to 1$, suppose $\bF_{q^d} \le \bF_{q^n}$ then $(q^d)^k = q^n$ has a solution. So $d \mid n$.

##### Number of irreducible polynomials in polynomial rings over finite fields

Suppose there are $N_q(n)$ irreducible polynomials in $\bF_q[x]$ of degree $n \ge 1$.

The product of all irreducible polynomials of degree $1 \le d \le n$ where $d \mid n$ is $x^{q^n} - x$.

Thus by Möbius inversion:
$$
q^n = \sum_{d \mid n} d N_q(d) \implies N_q(n) = \frac{1}{n}\sum_{d \mid n} q^d \mu\p{\frac{n}{d}}
$$

#### Galois Groups of Finite Fields

##### The Galois groups of finite fields

Suppose $F$ is a finite field, and $|F| = q$. Suppose $E/F$ is a finite field extension.

Consider $\sigma_q: E \to E$ where $\sigma_q: \alpha \mapsto \alpha^q$.

$\sigma_q \in \aut_F(E)$ since

- $\sigma_q$ is the **Frobenius map** repeated $r$ times. So $\sigma_q \in \aut(E)$.
- Suppose $\alpha \in F^*$, then $\sigma_q(\alpha) = \alpha^{q - 1} \alpha = \alpha$. So $\sigma_q \in \aut_F(E)$.

Actually $\aut_F(E) = \a{\sigma_q}$.

- Notice that $\sigma_q^k = \sigma_{q^k}$. And $\sigma_q^d = \sigma_{q^d} = \iota_E$ is the identity map.
- For $1 < k < d$, $\sigma_q^k$ cannot be identity.
  - Otherwise $\alpha^{q^k} = \alpha$ for all $\alpha \in E$. Contradiction!


##### Irreducible polynomials in finite fields

Suppose $f(x) \in \bF_{q}[x]$ is **irreducible**, and $\deg f(x) = d$.

Suppose $\alpha$ is a root of $f(x)$ in $\overline{\bF_q}$.

Then $f(x) \mid (x^{q^d} - x)$. And $f(x)$ splits in $\bF_{q^d}$.

- $\bF_q[\alpha] = \bF_{q^d}$ in $\overline {\bF_q}$.
- $f(x)$ splits in $\bF_q[\alpha]$, since $\bF_q[\alpha] / \bF_q$ is Galois.
- So $f(x) \mid (x^{q^d} - x)$.

For $n \ge 1$, $f(x) \mid (x^{q^n} - x)$ if and only if $d \mid n$.

- $\from$ apparently, since $\bF_{q^{d}} \le \bF_{q^n}$.
- $\to$ $\alpha \in F_{q^n}$. So $\bF_{q^d} \le \bF_{q^n}$.

Consider the Galois group $G = \aut_{\bF_q}(\bF_{q^d}) = \a{\sigma_q}$. $|G| = o(\sigma_q) = d$.

- Each automorphism $\varphi \in G$ is completely determined by $\varphi(\alpha)$.

So all the roots of $f(x)$ are given by: $R = (\alpha, \alpha^q, \ldots, \alpha^{q^{d - 1}})$, and $\alpha^{q^d} = \alpha$.

- Non of the roots of $f(x)$ is zero. $R \subseteq \bF_{q^d}^*$.

All roots of $f(x)$ have the same **multiplicative order**.

- Suppose $\alpha, \beta \in \bF_{q^d}$ are two different roots of $f(x)$. Suppose $\beta = \alpha^{q^k} = \sigma_q^k(\alpha)$.
- Notice that $\alpha^n = 1 \iff \sigma_q^k(\alpha^n) = 1 \iff \beta^n = 1$.

Denote $o(f) := o(\alpha)$ (multiplicative order) as the **order of the irreducible polynomial** $f(x)$.

Suppose $o(f) = \abs{\bF_{q^d}} = q^d - 1$. $f(x)$ is called a **primitive polynomial of extension** $\bF_{q^d}/\bF_q$.

- All roots of $f(x)$ are a group primitive of $\bF_{q^d}$.

##### Irreducibility, degree, and order

Suppose $f(x) \in \bF_{q}[x]$ and $\deg f(x) = d$.

Suppose $\alpha$ is a root of $f(x) \in \bF_q[x]$ in $\overline{\bF_q}$. And $\alpha$ has multiplicative order $\nu$.

$q$ has multiplicative order $d$ in $\Z_\nu$ if and only if $f(x)$ is irreducible.

- Lemma: For any $n \ge 1$, the following is true:
  $$
  \alpha^{q^n} = \alpha \iff \alpha^{q^n - 1} = 1 \iff \nu \mid q^{n} - 1 \iff q^n \equiv_\nu 1
  $$
- $\from$ Suppose $f(x)$ is irreducible. $q$ has multiplicative order $d$ in $\Z_\nu$ since:
  $$
  \alpha^{q^n} = \alpha \iff \bF_{q^d} \le \bF_{q^n} \iff d \mid n
  $$
  - So the minimum positive $n$ for $q^n \equiv_\nu 1$ is $d$.
- $\to$ Suppose $f(x)$ is reducible.
  - Then $\alpha$ must be a root for some irreducible $g(x) \in \bF_q[x]$.
  - Now apply $\from$ direction result. $q$ has multiplicative order less than $d$ in $\Z_\nu$.

