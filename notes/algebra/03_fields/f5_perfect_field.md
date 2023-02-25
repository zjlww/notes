#### Perfect Fields

##### Perfect fields

Suppose $F$ is a **field**. $F$ is perfect if all irreducible polynomials in $F[x]$ are separable.

Every **algebraically closed** field $F$ is perfect. Since irreducible polynomials are linear terms.

##### Frobenius test for perfect field

Suppose $F$ is a field.

Suppose $\char F = 0$. Then $F$ is perfect.

Suppose $\char F = p \neq 0$. $F$ is perfect if and only if $F^p = F$.

- Suppose $F \neq F^p$. $F$ is not perfect.
  - Take $\alpha \in F - F^p$.
  - Consider $p(x) = x^p - \alpha \in F[x]$. Suppose $E$ splits $p(x)$.
  - Suppose $p(\beta) = 0$ for some $\beta \in E$.
  - Then $\beta^p = \alpha$. And $p(x) = x^p - \beta^p = (x - \beta)^p$.
  - Clearly $p(x)$ has multiple roots.
  - $p(x)$ is irreducible in $F[x]$.
    - Suppose $p(x)$ is reducible in $F[x]$. With one monic factor $g(x)$.
    - $g(x)$ must be of the form $g(x) = (x - \alpha)^m$ for some $m = 1, \ldots, p - 1$.
    - $g(x) = x^m + (-m \alpha)x^{m -1} + \cdots$.
    - Suppose $(-m \alpha) \in F$, then $\alpha \in F$. Contradiction!
  
- Suppose $F^p = F$. $F$ is perfect.

  - Suppose $F$ is not perfect.

  - There exists a $f(x) \in F[x]$ is irreducible and inseparable.

  - Then $f'(x) = 0$ and for some $g(x) \in F[x]$.
    $$
    f(x) = g(x^p) = a_i (x^p)^{i} = b_i^p (x^p)^{i} = (b_i x^i)^p
    $$

  - But this shows $f(x)$ is reducible. Contradiction!


All finite fields are perfect.

- Since $F^p = F$ is clearly true for character $p$.

If every finite extension of a **field** $F$ is **separable**, then $F$ is **perfect**.

- The proof follows from definitions.

##### Algebraic extensions of perfect fields are perfect

Suppose $F$ is perfect. $E/F$ is algebraic. Then $E$ is perfect.

- Consider $F < E \le \overline E$.
- For all irreducible $p(x) \in E[x]$, there exists some $\alpha \in \overline E$, $p(\alpha) =0$. 
- Suppose $p(x) = \operatorname{irr}(\alpha, E)$, $q(x) = \operatorname{irr}(\alpha, F) \in F[x]$, $q(x)$ is separable.
- Also $p(x) \mid q(x)$ in $E[x]$, so $p(x)$ is also separable.

##### Purely inseparable extension

Suppose $E / F$ is **algebraic**. Suppose $\char F = p$.

$E/F$ is **purely inseparable** if for all $\alpha \in E - F$, $\irr(\alpha, F)$ is not separable.

- $F / F$ is called a trivial purely inseparable extension.
- $F$ must be **imperfect** when $E/F$ is non-trivial.
- $F$ must has $\char F = p\neq 0$. And $F$ must be infinite.

$E/F$ is purely inseparable iff for all $\alpha \in E - F$, $\irr(\alpha, F)$ if of the form $(x - \beta)^{p^k}$ where $\beta \in F$, and $\alpha = \beta^{p^k}$ for $k \ge 1$.

- Note that an irreducible polynomial is separable iff it is of the form $(f(x))^p$.

If $E/F$ is purely inseparable, and $E/K/F$, then $E/K$ and $K/F$ are also purely inseparable.

- Just recall this fact: $\irr(\alpha, K) \mid \irr(\alpha, F)$.

If $E/K$ and $K/F$ are purely inseparable, then $E/F$ is purely inseparable.

- This also follows from the fact that $\irr(\alpha, K) \mid \irr(\alpha, F)$ for $\alpha \in E - K$.
