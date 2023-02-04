#### Cyclotomic Polynomials

##### n-th roots of unity

Suppose $F$ is a field. And polynomial $f(x) = x^n - 1 \in F[x]$.

Note that $f(x)$ is **separable** except when $\char F = p$ and $\gcd(n, p) > 1$.

- When $\char F = 0$, $\gcd(f, f') = 0$.
- When $\char F = p$ and $\gcd(n, p) = 1$, $\gcd(f, f') = 0$.
- When $\char F = p$ and $\gcd(n, p) > 1$, that is $n = k p$ for $k > 1$, $f(x)$ is not separable.
  - $f(x) = x^n - 1 = x^{kp} - 1^p = (x^k  - 1)^p$.

In the following discussion, we will always assume $f(x)$ is **separable**.

Let $U_n$ be all the roots of $f(x)$ in $\overline F$. $u \in U_n$ is called a **n-th root of unity** on $F$.

- $U_n$ is a **cyclic subgroup** of $F^*$, and $|U_n| = n$.
  - $U_n$ is a finite subgroup of $F^*$. Since for all $\alpha, \beta \in U_n$, $\alpha \beta^{-1} \in U_n$.
  - Recall that all finite subgroups of $F^*$ are cyclic.

Let $\Omega_n$ be the set of generators of $U_n$. $\omega \in \Omega_n$ is called a **n-th primitive root of unity** on $F$.

- $U_n = \a{\omega} = \c{\omega^0, \ldots, \omega^{n - 1}}$.
- Recall that $U_n = \a{\omega^k}$ iff $\gcd\p{k, n} = 1$.

Let $S_n = F[U_n]$ be the splitting field of $f(x)$. $S_n / F$ is called the **n-th cyclotomic extension** over $F$.

- $S_n / F$ is a Galois extension.
  - $S_n / F$ is a simple extension. Since $S_n = F[U_n] = F[\omega]$.
  - $S_n / F$ is a normal extension. Since $S_n$ is the splitting field of $f(x)$ over $F$.
  - $S_n / F$ is a separable extension. Since $x^n - 1$ is separable.

##### Cyclotomic polynomials

Suppose $F$ is a field, where $x^n - 1 \in F[x]$ is separable. Let $\omega$ be a $n$-th primitive root of unity.

The **$d$-th cyclotomic polynomial** over $F$ is defined as
$$
Q_d(x) := \prod_{z \in \Omega_d} (x - z) = \prod_{o(\omega^k) = d, 0 \le k < n} (x - \omega^k)
$$
$(x^n - 1)$ can be factored into products of cyclotomic polynomials.
$$
U_n = \bigcup_{d \mid n, 1 \le d \le n} \Omega_d \implies x^n - 1 = \prod_{d \mid n, 1 \le d \le n} Q_d(x)
$$
##### Cyclotomic polynomials have coefficients in the primitive field

Suppose $F$ is a field. Let $F_p$ be the primitive subfield of $F$.

Then all defined cyclotomic polynomials $Q_n(x)$ are in $F_p[x]$.

- $Q_1(x) = x - 1 \in F_p[x]$.

- For prime $p$. Note that $x^p - 1 = Q_1(x) Q_p(x)$. So
  $$
  Q_p(x) = \frac{x^p - 1}{x - 1} = x^{p - 1} + \cdots + 1 \in F_p[x]
  $$

- For all other $n \in \N^+$ where $x^n - 1$ is separable.

  - Proceed with induction, suppose for $m < n$ we have $Q_m \in F_p[x]$.

  - Factorize $x^n - 1 = Q_n(x) R(x)$, where $R(x) \in F_p[x]$ by the induction hypothesis.
    $$
    x^n - 1 = Q_n(x) \s{\prod_{d \mid n, 1 \le d < n} Q_d(x)} = Q_n (x) R_n(x)
    $$

  - Since $x^n - 1 \in F_p[x]$ and $R_n(x) \in F_p[x]$, we have $Q_n(x) \in F_p[x]$.

For example, cyclotomic polynomials over $\Q$ are all in $\Z[x]$.

##### Calculating $Q_n(x)$

Suppose $F$ is a field, where $x^n - 1 \in F[x]$ is separable. Recall that:
$$
x^n - 1 = \prod_{d \mid n, 1 \le d \le n} Q_d(x) = Q_n(x) \s{\prod_{d \mid n, 1 \le d < n} Q_d(x)} = Q_n(x) R_n(x)
$$

Therefore $Q_n(x) = (x^n - 1) / R_n(x)$. And by Möbius inversion:
$$
Q_n(x) = \prod_{d \mid n} (x^d - 1)^{\mu(n / d)} = \prod_{d \mid n} (x^{n / d} - 1) ^{\mu(d)}
$$
##### Irreducibility of p-th Cyclotomic polynomials over $\Q$

Over field $\Q$, $Q_p(x) \in \Z[x]$ is irreducible for prime $p$.
$$
Q_{p}(x)=\frac{x^{p}-1}{x-1}=x^{p-1}+x^{p-2}+\cdots+x+1
$$

- $Q_p(x)$ is irreducible iff $Q_p(x + 1)$ is irreducible. Observe:
  $$
  Q_{p}(x+1)=\frac{(x+1)^{p}-1}{(x+1)-1}=\frac{x^{p}+\left(\begin{array}{c}
  p \\
  1
  \end{array}\right) x^{p-1}+\cdots+p x}{x}\\
  = x^{p-1}+\left(\begin{array}{c}
  p \\
  1
  \end{array}\right) x^{p-2}+\cdots+p
  $$

- $Q_p(x + 1)$ is irreducible in $\Z[x]$ and $\Q[x]$ by Eisenstein's Criterion and Gauss's Lemma.

##### Primitive polynomials and cyclotomic polynomials

Let $p(x) \in \bF_q[x]$ be a primitive polynomials of extension $\bF_{q^n} / \bF_q$. Then
$$
p(x) \mid Q_{q^n - 1}(x) \mid x^{q^n - 1} - 1
$$
Therefore $Q_{q^n - 1}(x)$ is the product of all primitive polynomials of $\bF_{q^n} / \bF_q$.

A prime factorization of $Q_{q^n - 1}(x)$ in $\bF_q[x]$ gives all primitive polynomials.
