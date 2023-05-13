#### Maximal and Prime Ideals

> In NCU ring $R$ where $M \sqsubseteq R$.
>
> - $R / M$ is a field iff $M$ is maximal.
> - $R / M$ is an ID iff $M$ is prime.

##### Ideals of a field

Suppose $R$ is a **NCU ring**. For $N \sqsubseteq R$, if $N$ contains a unit of $R$, $N = R$.

- Unit $u \in N$ implies $1 \in N$. Therefore $N \supseteq 1R = R$.

Suppose $R$ is a **field**. It has only two trivial ideals $\{0\}$ and $R$.

##### Field embeddings

Suppose $E$ and $F$ are **fields**. Suppose $\phi: F \to E$ is a ring homomorphism.

Then $\phi$ is either injective or the zero map.

- Consider $\ker\phi = \phi^{-1}(\{0\})$. $\ker \phi \sqsubseteq F$.
- Since $F$ is a field, all ideals are trivial.

An **injective ring homomorphism between fields** is called an **embedding**. Denoted as $\phi: F \inj E$.

- $\hom(F, L)$ is the set of embeddings from $F$ to $L$.
- $\hom_\sigma(E, L)$ is the set of embeddings from $E$ to $L$, that are supersets ##### extension of $\sigma$.
- $\aut(F)$ is the set of **automorphisms** on $F$.

##### Maximal ideal

Suppose $R$ is a **NC ring**. $M \sqsubset R$ is a **maximal ideal** if
$$
\forall N \subseteq R: (M \subseteq N \sqsubset R \implies M = N)
$$
##### Prime ideal

Suppose $R$ is a **NC ring**. $N \sqsubset R$ is a **prime ideal** if
$$
\forall a, b \in R: (ab \in N \implies a \in N \lor b\in N)
$$
The zero ideal is prime iff $R$ has no zero-divisors.

##### Prime elements

Suppose $R$ is a **NC ring**. A **nonzero nonunit** element $p$ of $R$ is **prime** if:
$$
\forall a, b \in R : (p \mid ab \implies p \mid a \lor p \mid b)
$$

- $p \in R$ is prime, iff $(p)$ is a nonzero prime ideal.
  - Hint: $p \mid a \iff a \in (p)$.


##### Field and maximal ideal

Suppose $R$ is a **NCU ring**. $R$ is a field if and only if $(0)$ is a maximal ideal.

- $\to$ Suppose $R$ is a field, clearly $\{0\}$ is the maximal ideal.
- $\from$ Suppose $R$ is not a field.
  - There is a nonzero nonunit element $a \in R$.
  - Then $(0)\subset (a) \sqsubset R$, since $1 \notin (a)$.
  - So $(0)$ is not the maximal ideal.

Suppose $R$ is a **NCU ring**. Given $M \sqsubseteq R$. $M$ is a maximal ideal if and only if $R / M$ is a field.

- Define ring homomorphism $\phi: R \to R/M$, $x \mapsto x + M$.
- $\to$ consider the contrapositive. Suppose $R/M$ is not a field.
  - Then there exists $\c{0} \subset N \sqsubset R/M$.
  - Then $M \subset \phi^{-1}[N] \sqsubset R$.
  - So $M$ is not maximal.
- $\from$ consider the contrapositive. Suppose $M$ is not maximal.
  - Then there exists $M \subset S \sqsubset R$.
  - Then $\c{0 + M} \subset \phi[S] \sqsubset R/M$.
  - So $R/M$ is not a field.

##### Integral domain and prime ideal

Suppose $R$ is a **NCU ring**. Given $N \sqsubseteq R$, the following are equivalent.

1. $N$ is a prime ideal.
2. $N \neq R$ and $\forall a, b \in R: (ab \in N \implies a \in N \lor b \in N)$.
3. $N \neq R$ and $\forall a, b \in R: \s{(a + N) \times (b + N) = N \implies (a + N) = N \lor (b + N) = N}$.
4. $R/N$ is an integral domain.

##### Maximal ideals are prime ideals

Suppose $R$ is a **NCU ring**. Then maximal ideals are prime ideals.

- $M \sqsubset R$ is a maximal ideal, so $R / M$ is a field.
- So $R/M$ is an integral domain.
- So $M \sqsubset R$ is a prime ideal.
