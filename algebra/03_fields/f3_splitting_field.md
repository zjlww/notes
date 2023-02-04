#### Splitting Fields

##### Splitting fields

Suppose $F$ is a **field**. And $f(x) \in F[x]$.

$f(x) \in F[x]$ splits in $F$, or $F$ splits $f(x)$, if:

- $f(x)$ factors into linear factors in $F[x]$.
- or $F$ contains all zeros of $f(x)$.

Suppose $P \subseteq F[x]$. A splitting field of $P$ **over $F$** is an extension field $K / F$ where:

1. Every polynomial $f(x) \in P$ splits in $K$.
2. For any intermediate field $E$, where $F \lt E<K$, at least one polynomial $g(x) \in P$ does not split in $E$.

Suppose $R \subseteq \overline F$ is the set of all zeros of polynomials in $P$ in $\overline F$.

- $K = F(R)$ is the unique **splitting field** of $P$ over $F$, in $\overline F$.

Algebraic closures are splitting fields as well. Take $P = F[x]$.

- $\overline F$ is the splitting field of $F[x]$.

##### Splitting fields are isomorphic

Suppose $F$​ is a **field**, $P \subseteq F[x]$​.

Suppose $K, K'$ are two splitting fields of $P$ over $F$. Then $K \simeq K'$.

- Suppose $R$ and $R'$ are the zeros of $P$ in $K$ and $K'$.
- Then $K = F(R)$ and $K' = F(R')$.
- There exists a $F$-embedding $\sigma \in \hom_F(K, K')$.
  - The existence of $\sigma$ is guaranteed by *algebraic extension of embeddings*.
- $\sigma[R] = R'$.
  - For any $f(x) \in P$, $\sigma$ maps its zeros in $K$ to its zeros in $K'$.

- $\sigma[K] = K'$.
  - So $\sigma[K] = \sigma[F(R)] = F(\sigma[R]) = F(R') = K'$. And $\sigma$ is an isomorphism.


##### All algebraic closures are isomorphic

Suppose $F$ is a field, then all algebraic closures of $F$ are isomorphic.

- Since $\overline F$ is the splitting field of $F[x]$ over $F$.

##### Irreducible polynomials in algebraic extensions

Consider algebraic field extension $E / K / F$.

Suppose $\alpha \in E$. $p(x) = \irr (\alpha, F)$ and $q(x) = \irr (\alpha, K)$.

- $\gcd(p, q)$ is non-constant in $E[x]$. So it is non-constant in $K[x]$.
- Since $q$ is irreducible in $K[x]$, $q \in \gcd_K(p, q)$.
- That is, all zeros of $q(x)$ are also zeros of $p(x)$.

