#### Polynomial Rings over NCU Rings

> Consider a polynomial ring over a NCU ring.
>
> - **Division with remainder** exists and is unique when the divisor has a unit leading coefficient.
> - **Factor theorem**, $f(a) = 0 \iff (x - a) \mid f(x)$.

##### Long division of polynomials

Suppose $R$ is a **NCU ring**. Suppose $f, g \in R[x]$, and $g \neq 0$.

Suppose $g(x) = g_nx^n + \cdots$ where the leading coefficient $g_n \in R^*$.

There exists $q, r \in R[x]$ such that $f(x) = q(x) g(x) + r(x)$, where $\deg r(x) < \deg g(x)$.

- The quotient $q$ and remainder $r$ can be found by **long division of polynomials**.
- Starting with $q^{(0)}(x) = 0$, and $r^{(0)}(x) = f(x) - q^{(0)}(x) g(x) = f(x)$.
- While $\deg r^{(n)}(x) \ge \deg g$, carry out the following steps:
  - Suppose $r_m x^m$ is the leading term of $r^{(n)}(x)$.
  - Define $c(x) = r_m g_n^{-1} x^{m - n}$.
  - Define $q^{(n+1)}(x) := q^{(n)}(x) + c(x)$.
  - Define $r^{(n + 1)}(x) := f(x) - q^{(n + 1)}(x) g(x)$.
  - Clearly $\deg r_{n + 1}(x) < \deg r_n(x)$.
- Suppose for the first time, $\deg r^{(N)}(x) < \deg g$.
- Let $q(x):= q^{(N)}(x)$ and $r(x) = r^{(N)}(x)$.

There exists no other $q', r' \in R[x]$ such that $f(x) = g(x) q'(x) + r'(x)$, where $\deg r' < \deg g$.

- $g(x)(q'(x) - q(x)) = r(x) - r'(x)$.
- Since $\deg (r - r') < \deg g$, we have $q' = q$. Therefore $r' = r$.

##### Factor theorem

Suppose $R$ is a **NCU ring**.

An element $a \in R$ is a **zero / root** of $f(x) \in R[x]$ iff $(x - a)$ is a factor of $f(x)$ in $F[x]$.

- Divide $f(x)$ by $(x - a)$. $f(x) = q(x) (x - a) + c$. So $f(a) = c$.

#### Polynomial Rings over Integral Domains

##### Degrees of products of polynomials: over ID

Suppose $D$ is an **ID**. $f, g\in D[x]$. $\operatorname{deg}(f g)=\operatorname{deg}(f)+\operatorname{deg}(g)$.

- Since in an integral domain, multiplication of two nonzero leading coefficients is not zero.

##### Number of roots of polynomials over integral domains

Suppose $D$ is an **ID**. $f \in D[x]$. The number of roots of $f(x)$ is less or equal to $\deg f(x)$.
- Suppose the roots are $(z_i)_{i = 1}^k \in D$.
- $f(x) = (x - z_1) r_1(x)$ by application of the factor theorem.
- $f(z_2) = (z_2 - z_1)r_1(z_2)$, since $D$ is integral domain, $r_1(z_2) = 0$.
- Repeat the above procedure for $k$ times.
  $$
  f(x) = (x - z_1)(x - z_2) \cdots (x - z_k)r_k(x)
  $$

Suppose $F$ is a field. And $G$ is a finite subgroup of $F^*$. Then $G$ is cyclic.

##### Finite multiplicative subgroups of IDs are cyclic

Suppose $D$ is an **ID**. Then $\a{D^*, \cdot}$ is a group. All finite subgroups of $D^*$ are cyclic.

- Suppose $G \le D^*$ is a finite subgroup.
- Since $G$ is a finite abelian group, $G \simeq \times_{k=1}^n \Z_{p_k^{n_k}}$. Where $p_k$ are primes (may be not distinct).
- All primes are distinct.
  - Let $m = \lcm(p_k^{n_k})_{k = 1}^n$. Let $R = \c{\alpha \in G: \alpha^m = 1}$.
  - For $\alpha \in G$, clearly $\alpha^m = 1$, so $G \subseteq R$.
  - Therefore $|R| \le m \le \prod_k p_k^{n_k} = |G| \le |R|$.
  - So $m = \prod_{k} p_k^{n_k}$, and the primes are distinct.
- So $G$ is a cyclic group.

