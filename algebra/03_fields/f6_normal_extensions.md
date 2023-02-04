#### Normal Extension


##### Normal extensions

Consider algebraic field extensions $\overline F / K / F$.

Algebraic field extension $K/F$ is **normal**, if any of the following equivalent statement is true:

1. $\hom_F(K, \overline F) = \aut_F(K)$.
2. Any irreducible polynomial $p(x)$ in $F[x]$ with one root in $K$ splits in $K$.
3. $K$ is a splitting field of some $P \subseteq F[x]$ over $F$.

Proof:

- ($1\to 2$)
  - Suppose $p(x) \in F[x]$ is irreducible.
  - Suppose $\alpha \in K$ and $p(\alpha) = 0$.
  - Suppose $\beta \in \overline F$ and $p(\beta) = 0$.
  - There exists $\sigma \in \hom_{F}(K, \overline F)$ where $\sigma(\alpha) = \beta$.
  - Then $\sigma \in \aut_F(K)$, so $\beta \in K$.
- ($2 \to 1$)
  - Consider any $\sigma \in \hom_F(K, \overline F)$.
  - Suppose $\alpha \in K$. Suppose $p(x) = \irr(\alpha, F)$.
  - Then $p(x)$ splits in $K$.
  - $p(\sigma(\alpha)) = 0$, so $\sigma(\alpha) \in K$.
  - Therefore $\sigma \in \hom_F(K, K) = \aut_F(K)$.
- ($2 \to 3$)
  - Define $P= \c{\irr (\alpha, F) \mid \alpha \in K}$.
  - Define $R$ as the set of zeros of $P$ in $\overline F$.
  - Then $R \subseteq K$. So $F(R) = R = K$.
- ($3 \to 1$)
  - Define $R$ as the set of zeros of $P$ in $\overline F$.
  - Then $K = F(R)$.
  - Suppose $\sigma \in \hom_F(K, \overline F)$.
  - Since $\sigma$ permutes zeros, $\sigma \in \hom_F(K, K) = \aut_F(K)$.

##### Finite normal extensions

Suppose field extension $E/F$ is finite and normal. Then $E$ is the splitting field of some $f(x) \in F[x]$.

- Since $E/F$ is finite, suppose $E = F[\alpha_1, \ldots, \alpha_n]$.
- Just define $f(x) = \prod_{i=1}^n\irr(\alpha_i, F) \in F[x]$.

> Not all finite extensions are normal.
>
> - Consider $\Q(\sqrt 2, \sqrt 3)/\Q$, this is normal, since it is the splitting field of $(x^2 - 2)(x^2 - 3)$.
> - Consider $\Q(2^{1/4})/\Q$, this is not normal. $\irr(2^{1/4}, \Q) = x^4 - 2$, it has root $2^{1/4}i \notin \Q(2^{1/4})$.
>   - Violating condition 2 of normal extensions.

##### Any extension of degree 2 is normal

Consider field extension $E/F$ and $[E:F] = 2$. Then $E/F$ is normal.

- Suppose $\alpha \in E - F$, so $E = F[\alpha]$. Suppose $p(x) = \irr(\alpha, F)$, and $\deg p(x) = 2$.
- Since $p(x)$ has one root in $E$, by the factor theorem, it splits in $E$.
- So $E$ is the splitting field of $\c{p(x)}$ over $F$. $E/F$ is normal.

##### Intermediate fields of normal extensions

Suppose $K/F$ is normal. Consider extension tower $K / E / F$.

Then $K/E$ is normal.

- $K$ is the splitting field of $\F := \c{\irr(\alpha, F) \mid \alpha \in K}$ over $F$.
- $K$ is the splitting field of $\mathcal F$ over $E$ as well.

Notice that $E/F$ is **not** necessarily normal. e.g. consider $\C_{\Q}/\Q(\sqrt[3]{2})/\Q$.