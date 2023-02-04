#### Separable Extensions

##### Formal derivative in $F[x]$

Let $F$ be a **field**. We define the formal derivative $D: F[x] \to F[x]$:
$$
p(x)=\sum_{k=0}^{n} a_{k} x^{k} \in F[x], \quad D(p(x))=\sum_{k=1}^{n}\left(k \cdot\left(a_{k} x^{k-1}\right)\right)
$$
Let $p(x), q(x) \in F[x],$ and let $n$ and $m$ be nonnegative integers. The following is true:

- $D(p(x)+q(x))=D(p(x))+D(q(x))$.
- $D(a p(x))=a D(p(x))$ for any $a \in F$.
- $D\left(x^{n} x^{m}\right) = (n + m) x^{n + m - 1} = (n x^{n-1}) x^m + x^n (m x^{m-1}) =x^{n} D\left(x^{m}\right)+D\left(x^{n}\right) x^{m}$.
- $D\left(p(x) x^{m}\right)=p(x) D\left(x^{m}\right)+D(p(x)) x^{m}$.
- $D(p(x) q(x))=p(x) D(q(x))+D(p(x)) q(x)$.

##### Multiplicity of roots

Suppose $F$ is a field. $f(x) \in F[x]$. Suppose $E$ is a splitting field of $f(x)$ over $F$.

Suppose $\alpha \in E$ is a root of $f(x)$.

The **multiplicity** of $\alpha$ is defined as the largest $n \in \N$ such that $(x - \alpha)^n \mid f(x)$ in $E[x]$.

Suppose $n = 1$, $\alpha$ is a **single root**, otherwise $\alpha$ is a **multiple root**.

##### Separability

Suppose $F$ is a field. And $f(x)$ is non-constant.

- $f(x) \in F[x]$ is **separable** if it has no multiple root in any splitting field.
- Otherwise $f(x)$ is **inseparable**.

Consider field extension $E/F$.

- An **algebraic** element $\alpha \in E$ is **separable** **over** $F$, if $\operatorname{irr}(\alpha, F) \in F[x]$ is separable.

Consider algebraic extension $E/F$.

- $E/F$ is separable if every $\alpha \in E$ is separable **over** $F$.

##### Separable polynomials

Consider field extension $E/F$. Suppose $f(x) \in F[x]$ splits in $E$.

$f$ and $f'$ are co-prime if and only if $f$ is separable.

- Suppose $\alpha_k \in E$ are distinct roots of $f(x)$.

- Now split $f(x)$ in $E$.
  $$
  f(x)= c\p{x-\alpha_{1}}^{e_{1}} \cdots\p{x-\alpha_{n}}^{e_{n}} \implies f'(x) = c\sum_ie_i(x - \alpha_i)^{e_i - 1} \prod_{j \neq i} (x - \alpha_j)^{e_j}
  $$

- Suppose $f(x)$ is separable and all $e_i = 1$, clearly $1 \in \gcd(f, f')$.

- Suppose $1 \in \gcd(f, f')$. We must have $e_i = 1$ for all $i$.

When $f$ is irreducible, $f$ and $f'$ are co-prime iff $f' = 0$ iff $f$ is separable.

- Since $f$ is irreducible in $F[x]$, and $\deg f' < \deg f$.
- $1 \in \gcd (f, f')$ if and only if $f' \neq 0$.

Further suppose $\char F = 0$. All irreducibles in $F[x]$ are all separable.

- As $f(x)$ is non-constant, $f'(x)$ is never zero.

Further suppose $\char F = p$ is a prime.

- For nonzero $a \in F$, $k \in \Z$, $ka = 0$ if and only if $p \mid k$.
- Suppose $f(x) = \sum_{i=0}^n a_i x^i$ then $f'(x) = \sum_{i=1}^n i a_i x^{i -1}$.
- $f'(x) = 0$ iff $\forall i \notin \p p: a_i = 0$ iff $f(x)$ if of form $g_1(x^p)$.

Suppose $g'_0(x) = 0$, $g_0(x)$ is separable, otherwise, repeat above process:
$$
f(x) = g_0(x) =  g_1(x^p) = g_2(x^{p^2}) = \cdots g_k(x^{p^k})
$$
Until $g_k(x) \in F[x]$, $g_k'(x) = 0$. Then $g_k$ is separable.

- $k$ is called the **radical exponent** of $f(x)$.
- Since $g_0(x)$ is irreducible, $g_i(x)$ are also irreducible.

##### Primitive element theorem

Consider extension $\overline F/E/F$.

Suppose $E/F$ is a **finite separable** field extension. Then $E/F$ is **simple**.

Proof:

Suppose $F$ is finite, $E$ is also finite. Suppose $E^* = \a \alpha$, then $F(\alpha) = E$.

Suppose $F$ is infinite. And $E = F(\beta, \gamma)$. Where $\beta, \gamma \in E- F$. We claim that there exists $\alpha = \beta + a \gamma$ where $a \in F^*$, and $F(\alpha) = F(\beta, \gamma)$.

- Define $f(x) = \irr(\beta, F)$ and $g(x) = \irr(\gamma, F)$.

- Let $(\beta_i)_{i=1}^n$ be the distinct zeros of $f(x)$ and $(\gamma_i)_{i=1}^m$ be the distinct zeros of $g(x)$ in $\overline F$.

  - Since $\beta, \gamma \notin F$, and $E/F$ is **separable**, $m, n \ge 2$.
  - w.l.o.g. we assume $\beta = \beta_1$ and $\gamma = \gamma_1$.

- There exists $a \in F^*$ such that for all $1 \le i \le n, 1 \le j \le m$ except $i = j = 1$ we have
  $$
  a \gamma + \beta \neq a \gamma_j + \beta_i
  $$

  - Since we only eliminated finitely many elements from the infinite $F^*$:
    $$
    \forall 2 \le i \le n, \forall 2 \le j \le m: \frac{\beta_i - \beta_1}{\gamma_1 - \gamma_j} \neq a
    $$

- Now we claim that $F(\alpha) = F(\beta, \gamma)$.

  - Consider $h(x) = f(\alpha - ax) \in F(\alpha)[x]$.
    - $h(\gamma_1) = f(\beta) = 0$.
    - For all $2 \le j \le m$, $h(\gamma_j) = f(\alpha - a \gamma_j) \neq 0$ since $\forall 1 \le i \le n:\alpha - a \gamma_j \neq \beta_i$.
  - Therefore $(x - \beta) \in \gcd_{\overline F}(h, g)$.
  - Since GCD is invariant under PID extension, $(x - \beta) \in \gcd_{F(\alpha)}(h, g)$.
  - Therefore $\beta \in F(\alpha)$. And $\gamma \in F(\alpha)$. So $F(\alpha) = F(\beta, \gamma)$.

Suppose $F$ is infinite. And $E = F(\beta_1, \beta_2, \ldots, \beta_n)$. Where $\beta_1, \ldots, \beta_n \in E-F$. Proceed as
$$
F(\beta_1, \beta_2, \ldots, \beta_n) = F(\beta_1, \ldots, \beta_{n-2})(\beta_{n-1}, \beta_n) = F(\beta_1, \ldots, \beta_{n-2}, \alpha_{n-1})
$$
##### Intermediate fields of a separable extension

Consider extension tower $E/K/F$, where $E / F$ is separable.

Then $E/K$ and $K/F$ are both separable.

- $K/F$ is separable by definition.
- $E/K$ is separable. As for $\alpha \in E$, $\irr(\alpha, K) \mid \irr(\alpha, F)$.
