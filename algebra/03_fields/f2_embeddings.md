#### Field Embeddings

##### F-embeddings

Consider field extensions $E/F$, $L/F$.

- Suppose $\iota: F \to F$ is the identity map.
- $\hom_F(E, L):=\hom_\iota(E, L)$.
  - They are called $F$-embeddings from $E$ to $L$.
  - $\sigma \in \hom_F(E, L)$ is also written as $\sigma: E \hookrightarrow L$ **over** $F$.

##### F-automorphisms

Consider field extension $E/F$.

- Suppose $\iota: F \to F$ is the identity map.
- $\aut_F(E) := \aut_{\iota}(E)$.
  - They are called $F$-automorphisms on $E$.

When $E/F$ is **algebraic**, $\hom_{F}(E, E) = \aut_{F}(E)$.

- Suppose $\sigma \in \hom_{F}(E, E)$. And $\alpha \in E$. Suppose $p = \irr (\alpha, F)$.
- Roots of $p$ inside $E$ are permuted to roots of $p$ by $\sigma$.
- All $\alpha \in E$ is in some set of zeros. So $\sigma$ is onto $E$.

##### Frobenius map

Suppose $F$ is a **NCU ring**, $\char F = p$ is **finite** and $p \ge 2$.

The Frobenius map $\sigma: F \to F$ is $x \mapsto x^p$. $\sigma \in \hom(F, F)$.

- $\sigma(a \pm b) = (a \pm b)^p = a^p \pm b^p = \sigma(a) \pm \sigma(b)$.
  - When $p = 2$, $(a - b)^p = a^p + b^p = a^p - b^p$.
- Also $\sigma(ab) = \sigma(a) \sigma(b)$.

 $\sigma_n(x) = x^{p^n}$ is the composition of $n$ Frobenius homomorphism. $\sigma_n \in \hom(F, F)$.

- $\sigma_n(a \pm b) = (a \pm b)^{p^n} = a^{p^n}\pm b^{p^n} = \sigma_n(a) \pm \sigma_n(b)$.
- $\sigma_n(ab) = \sigma_n(a)\sigma_n(b)$.

$\sigma[F]$ is usually denoted as $F^p$.

This can be further generalized to multiple terms $(a + b + c)^{q} = a^q + b^q + c^q$. For $q = p^n$.

- Just notice that $a + b + c = a + (b + c)$.

##### Properties of field embeddings

Suppose $E, K$ are fields. Suppose $\sigma \in \hom(E, K)$.

- The inverse $\sigma^{-1}: \sigma[E] \to E$ is also an embedding.
- Preserves subfield:
  - Suppose $E/F$, then $\sigma[E]/\sigma [F]$.
- Preserves adjunction:
  - Suppose $E/F$, and $S \subseteq E$.
  - Then $\sigma[F(S)] = \sigma[F](\sigma [S])$.
  - Then $\sigma[F[S]] = \sigma[F][\sigma [S]]$.

Suppose $\sigma$ also denotes the polynomial extension of $\sigma \in \hom(E, K)$.

- Preserves polynomial factorization:
  - $f(x) = p(x) q(x) \iff f^\sigma(x) = p^\sigma(x) q^\sigma(x)$.
- Preserves roots:
  - Suppose $\alpha \in E$, $f(x) \in E[x]$.
  - $f(\alpha) = 0 \iff \sigma(f)(\sigma(\alpha)) = 0$.
- Preserves irreducible polynomials.
  - Suppose $p(x) \in E[x]$ is irreducible. $\sigma(p) \in \sigma[E][x]$ is also irreducible.

Consider field extension $E/F$ and $K/L$. Let $\sigma \in \hom (F, L)$ and $\varsigma \in \hom_\sigma(E, K)$.

- Suppose $\alpha \in E$​​ is algebraic over $F$​​. Then $\varsigma (\alpha)$​​ is algebraic over $\varsigma[F]$​​.
  - Suppose $p = \irr (\alpha, F)$, $p(\alpha) = 0$, so $p^\sigma(\varsigma(\alpha)) = 0$.
- Suppose $E/F$ is algebraic, then $\varsigma E/\varsigma F$ is also algebraic.
  - This directly follows from the result above.
- $\varsigma$ can be viewed as a **linear map**:
  - $E$ is a $F$-linear space, and $\varsigma E$ is a $\sigma[F]$-linear space.
  - By identifying $F$ and $\sigma F$, we can view $\varsigma$ as an **injective linear map** between **vector spaces** $E$ and $\varsigma E$ over $F$.
    - For $a, b \in F, x, y \in E$, $\varsigma(a x + b y) = \sigma(a) \varsigma(x) + \sigma(b)\varsigma(y)$.

#### Algebraic Extension of Embeddings


##### Simple algebraic extension of embeddings

Suppose $\sigma \in \hom(F, L)$. Suppose $L$ is algebraically closed. Consider field extension $E / F$.

Suppose $\alpha \in E-F$ is **algebraic** over $F$. Suppose $\irr(\alpha, F) = p(x) \in F[x]$.

Then $p^\sigma \in F^\sigma[x]$ is also **irreducible**. Suppose $R$ is the set of roots of $p^\sigma(x)$ in $L$.

Any element $\varsigma \in \hom_\sigma(F[\alpha],L)$ is completely determined by $\varsigma(\alpha)$.

- Since embeddings preserves roots, $\beta = \varsigma(\alpha) \in R$.
- $\varsigma(\alpha)$ **completely determines** $\varsigma$.
  - Suppose $\deg (\alpha, F) = \deg p = \deg p^\sigma= n$.
  - $1, \alpha, \cdots, \alpha^{n-1}$ is a basis of $F[\alpha]$. Then $1, \beta, \cdots, \beta^{n-1}$ is a basis of $F^\sigma[\beta]$.
  - Since $\varsigma$ is a ring homomorphism, $\varsigma(\alpha^k) = \varsigma(\alpha)^k = \beta^k$.

There exists a $\varsigma \in \hom_{\sigma}(F[\alpha], L)$ where $\varsigma(\alpha) = \beta$.

- Define $\varsigma(\alpha) := \beta$. $\varsigma$ is a well defined function according to previous discussion.
- $\varsigma$ is a ring homomorphism. For any $f, g \in F[x]$, therefore any $f(\alpha), g(\alpha) \in F[\alpha]$, we have:
  - $\varsigma(f(\alpha) + g(\alpha)) = \varsigma(f(\alpha)) + \varsigma(g(\alpha))$.
  - $\varsigma(f(\alpha) g(\alpha)) = \varsigma((fg)(\alpha)) = \varsigma(f(\alpha))\varsigma(g(\alpha))$.

Clearly $\abs{\hom_{\sigma}(F[\alpha], L)} = \abs{R}$.

##### Infinite algebraic extension of embeddings

> **Zorn's lemma** — Suppose a non-empty partially ordered set $P$ has the property that every chain in $P$ has an upper bound in $P$. Then the set $P$ contains at least one maximal element.
>
> An element $m \in P$ is **maximal** if there is no other greater element in $P$.

Suppose $\sigma\in \hom(F,L)$. Suppose $E/F$ is algebraic and $L$ is algebraically closed.

**$\hom_\sigma(E,L)$ is not empty**.

- Consider the set $\mathcal E = \cup_{F \le X \le E}\hom_\sigma(X, L)$.
- The set $\E$ is not empty as a simple algebraic extension of $\sigma$ is possible.
- Define **partial ordering** $\tau_0 \le \tau_1$ on $\mathcal E$ if $\tau_0 \subseteq \tau_1$.
- Suppose $\mathcal C = \{\tau_i: X_i \to L: i \in \mathcal I\}$ is a chain, define $\Tau = \cup_i \tau_i$. Then $\Tau$ is an **upper bound** of $\mathcal C$.
  - Define $K = \cup_i X_i$, can verify $K$ is a field, and for all $i\in \mathcal I$, $X_i \le K \le E$.
  - Similarly we can verify that $\Tau$ is an embedding, so $\Tau \in \mathcal E$.
  - Clearly $\forall i\in \mathcal I: \tau_i \le \Tau$ so $\Tau$ is an upper bound of the chain $\mathcal C$.
- By Zorn's Lemma, there is a maximal extension $\tau:Y \to L$.
  - $Y = E$, otherwise we can further extend $\tau$ with $r \in E - Y$. Then $\tau$ is not maximal!

