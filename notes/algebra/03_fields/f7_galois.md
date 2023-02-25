#### Galois Theory

##### Lemma

Suppose $M / K$ is finite. And $M = K[\alpha_1, \ldots, \alpha_n]$.

Suppose $\overline K$ is an algebraic closure of $K$. Let $G := \hom_K(M, \overline K)$.

We have $|G| \le [M : K]$ for general extension $M / K$.

- Define $K_m = K[\alpha_1, \ldots, \alpha_m]$ for $1 \le m \le n$.
- Consider extension chain $K = K_0 \le K_1 \le \cdots \le K_n = M$.
- We can extend $\iota$ to $\hom_{K}(K_1, \overline K)$, $\hom_K(K_2, \overline K)$, and so on...
  $$
  \iota \in \hom_{K}(K_0, \overline K) \to \hom_{K}(K_1, \overline K) \to \cdots \to \hom_{K}(K_n, \overline K) \ni \sigma
  $$
  - Each step is a **simple extension** of embedding!
- Suppose $\irr(\alpha_m, K_{m - 1})$ has roots $R_m$ in $\overline K$. Define $R := R_1 \times R_2 \times \cdots \times R_n$. Then $|R| = |G|$.
  - For any $\beta = (\beta_1, \ldots, \beta_n) \in R$.
  - Define $\lambda(\beta)$ as the **unique** $\sigma \in \hom_K(M, \overline K)$ with $\sigma(\alpha_m) = \beta_m$ for all $1 \le m \le n$.
  - The function $\lambda: R \to G$ is **bijective**. It has inverse
    $$
    \lambda^{-1}(\sigma) := (\sigma(\alpha_1), \sigma(\alpha_2), \ldots, \sigma(\alpha_n))
    $$
- Since $|R_m| \le [K_m : K_{m - 1}]$, we finally have $|G| \le [M:K] = \prod_{m = 1}^n [K_{m} : K_{m - 1}]$.

$|G| = [M:K]$ if and only if $\alpha_1, \ldots, \alpha_n$ are **separable** over $K$.

- ($\to$) Prove the contrapositive. Suppose $\alpha_k$ is not separable.
  - Swap $\alpha_1, \alpha_k$ in the list, $K[\alpha_k, \alpha_2, \ldots, \alpha_1, \ldots, \alpha_n] = M$.
  - Then $|R_1| < [K_1:K]$ so $|G| < [M:K]$.
- $(\from)$ Supose $\alpha_1, \ldots, \alpha_n$ are separable over $K$.
  - Since $\irr(\alpha_m, K_{m - 1}) \mid \irr(\alpha_m, K)$, $\irr(\alpha_m, K_{m - 1})$ is separable.
  - Therefore $|R_m| = [K_{m }: K_{m - 1}]$ for all $m$.

##### Splitting field of a separable polynomial is separable

Suppose $M$ is the splitting field of $p(x) \in K[x]$ over $K$. And $p(x)$ is separable. Then $M / K$ is separable.

- Let $G = \aut_{K}(M)$. And $R = [\alpha_1, \ldots, \alpha_n]$ be the list of roots of $p(x)$ in $M$. So $M = K[R]$.
- Since roots in $R$ are separable over $K$, by (Lemma), $|G| = [M:K]$.
- For any $\alpha \in M - K$, it must be separable over $K$.
  - $M = K[\alpha, R]$. And $|G| = [M : K]$. So by (Lemma), $\alpha$ must be separable over $K$.

##### Galois extensions and Galois groups

Consider field extension tower $\overline K / M / K$, where $M / K$ is **finite** and **normal**. Let $G = \aut_K(M)$.

$M / K$ is an **Galois extension** if any of the following equivalent conditions are true:

1. $M / K$ is separable.
2. $[M:K] = |G|$.
3. $M^G = K$.
   - Define $M^G := \c{\alpha \in M\mid \forall \sigma \in G: \sigma(\alpha) = \alpha}$.
   - That is $M^G$ is the set of elements of $M$ fixed by all embeddings in $G$.
   - $M^G$ is a field between $K$ and $M$.
     - Suppose $a, b \in M^G$, then $ab^{-1} \in M^G$.

Proof:

- ($1 \to 2$) Suppose $M / K$ is separable. $|G| = [M : K]$.
  - Recall the process of extending $\iota: K \to K$ to $\hom_K(M, \overline K)$ in (Lemma).
  - When extending $\sigma_{m - 1} \in \hom_{K}(K_{m - 1}, \overline K)$ to $\hom_K(K_{m}, \overline K)$, there is exactly $[K_m : K_{m - 1}]$ distinct extensions for each $\sigma_{m - 1}$.
- ($2 \to 3$) Suppose $[M: K] = |G|$, $M^G = K$.
  - Note that
    $$
    [M:K] = |G| \le [M : M^G] \le [M:K]
    $$
  - Therefore $M^G = K$.
- ($3 \to 1$) Suppose $M^G = K$, $M/K$ is separable.
  - Consider any $\alpha \in M - K$.
  - Let $R := \c{\sigma(\alpha): \sigma \in G}$. Let $p(x) = \prod_{\beta \in R} (x - \beta)$.
  - $\sigma \in G$ permutes elements in $R$, so $p(x)$ is invariant under all $\sigma \in G$.
  - So $p(x) \in M^G[x] = K[x]$. $p(\alpha) = 0$. Therefore $p(x) = \irr(\alpha, K)$.
  - Clearly $p(x)$ is separable by definition.

For Galois extension $M / K$, the group $G = \aut_{K}(M)$ is called the **Galois group** of $M / K$.

- The same group is also denoted as $\operatorname{Gal}(M/K)$.
- Functional composition is the group operation group $\aut_F(E)$.

##### Intermediate fields of Galois extensions

Consider extension tower $M/L/K$ where $K / M$ is a Galois extension.

Then $K/L$ is also a Galois extension.

- Since $K / M$ is separable, $K/L$ is separable.
- Since $K/F$ is normal, $K/E$ is normal.

##### Galois correspondence

Consider Galois extension $M / K$.

- Let $\mathcal F$ be the set of intermediate fields between $M$ and $K$.
- Let $\G$ be the set of subgroups of $\Gal(M / K)$.
- For $L \in \F$, consider map $\mathrm{fg}:L \mapsto \Gal(M / L)$ (fields to groups).
- For $H \in \G$, consider map $\mathrm{gf}: H \mapsto M^H$ (groups to fields).

Notice that:

- $\fg \circ \gf (H) = \fg(M^H) = \Gal(M / M^H) \supseteq H$.
- $\gf \circ \fg (L) = \gf(\Gal(M / L)) = M^{\Gal(M / L)} \supseteq L$.

The **Galois correspondence** states that $\fg$ and $\gf$ are **inverse of each other**.

- Define function $\nu: \F \cup \G \mapsto \N^+$ as following:
  - For $L \in \F$, $\nu(L) := [M : L]$.
  - For $H \in \G$, $\nu(H):= |H|$.
- $\nu$ is **invariant** under transform $\fg$ and $\gf$.
  - For $L \in \F$, $\nu(L) = \nu(\fg(L)) = \nu(\Gal(M / L))$. That is $|\Gal(M / L)| = [M : L]$.
    - This immediately follows from that $M / L$ is a Galois extension.
  - For $H \in \G$, $\nu(H) = \nu(\gf(H)) = \nu(M^H)$. That is $|H| = [M : M^H]$.
    - Suppose $K[\alpha] = M$ for $\alpha \in M - K$ by primitive element theorem.
      - Then $\sigma \in \Gal(M / K)$ is uniquely determined by $\sigma(\alpha)$.
    - Define $R := \c{\sigma(\alpha) \mid \sigma \in H}$. Define $f(x) = \prod_{z \in R}(x - z) \in M[x]$.
    - Then $f(x) \in M^H[x]$.
      - For any $\sigma \in H$, $\sigma$ permutes roots $R$.
      - So coefficients of $f(x)$ are invariant under $\sigma \in H$.
    - Define $p(x) = \irr(\alpha, M^H)$. Then $p(x) \mid f(x)$. And
      $$
      \deg p(x) = [M : M^H] \le \deg f(x) \le |H|
      $$
    - Since $M / M^H$ is Galois. And $\Gal(M / M^H) \supseteq H$.
      $$
      [M : M^H] = \abs{\Gal(M / M^H)} \ge |H|
      $$
    - Therefore $|H| = [M : M^H]$.
- Therefore we have $\fg \circ \gf (H) = H$ and $\gf \circ \fg (L) =L$.
