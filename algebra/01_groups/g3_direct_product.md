#### Direct Product of Groups

##### External direct product

Let $\a{G_1,\cdot}, \a{G_2,\cdot}, \ldots, \a{G_k, \cdot}$ be groups. We can define group structure on $G = G_1 \times \cdots \times G_k$.

- Define $(a_1, \ldots, a_k) \times (b_1, \ldots b_k) := (a_1 b_1, \ldots, a_k b_k)$.
- Clearly $(e_1, \ldots, e_k)$ is the identity element. And $(a_1, \ldots, a_k)^{-1} = (a_1^{-1},\ldots, a_k^{-1})$.

We will now identify the element $a \in G_j$ with $\what a :=(e_1, \ldots, a, \ldots, e_k) \in G$.

- Denote $\what G_{j}$ as $\c{\what a: a \in G_j}$.
- $\what G_j$ is a normal subgroup of $G$. Since $\forall a \in \what G_i, \forall b \in \what G_j: (i \neq j \implies ab = ba)$.

##### Internal direct product

Let $\a{G, \cdot}$ be a group with subgroups $H_1, \ldots, H_k$.

$G$ decomposes into direct product $H_1 \times \cdots \times H_k$ if the following are true:

1. (Factorization) $\forall g \in G, \exists h_1 \in H_1, \ldots, \exists h_k \in H_k:  g = h_1 h_2 \cdots h_k$.
2. (Uniqueness) Suppose $h_1 h_2 \cdots h_k = h_1' h_2' \cdots h_k'$. Where for all $i$, $h_i, h_i' \in H_i$. Then $h_i = h_i'$.
   - For $k = 2$, this is equivalent to $H_1 \cap H_2 = \c{e}$.
3. (Commutativity) For all $i \neq j$, if $h_i \in H_i$ and $h_j \in H_j$, then $h_i h_j = h_j h_i$.
   - For $k = 2$, given Unique Factorization is true, the following Normality property is stronger than the Commutativity property.
   - (Normality) Both $H_1$ and $H_2$ are normal subgroups of $G$.
   - Consider any $a \in H_1$ and $b \in H_2$. We only need to show that $ab = ba$.
   - Note that $aba^{-1}b^{-1} = (aba^{-1})b^{-1} = a(ba^{-1}b^{-1}) \in H_1 \cap H_2$.

When $G$ decompose into $H_1 \times \cdots \times H)_k$, $H_j$ are normal subgroups of $G$.

$G \simeq G_1 \times \cdots \times G_k$ by group isomorphism $h_1h_2 \cdots h_k \mapsto (h_1, h_2, \ldots, h_k)$.

If $G$ is finite, and for subgroups $H_1, \ldots, H_k$, the uniqueness property holds. Then the factorization property is equivalent to $|G| = |H_1|\times \cdots \times |H_k|$.

- Define $S := \c{h_1h_2\cdots h_k: h_j \in H_j}$. By uniqueness, $|S| = |H_1| \times \cdots \times |H_k|$.
- Since $S \subseteq G$, $|S| \le |G|$.
- Factorization property iff $S = G$ iff $|S| = |G|$ iff $|G| = |H_1| \times \cdots \times |H_k|$.

##### Orders in direct product of groups

Suppose $(G_i)_{i = 1}^n$ are groups, and $a_i \in G_i$ with $o(a_i) = r_i$.

Then $o(a_1, \ldots, a_n) = \lcm(r_1, \ldots, r_n)$.

##### Example: $\C^*$ decompose into $\R_+ \times \bS$

The complex unit circle $\bS = \c{|z| = 1: z \in \C}$, and $\R_+ = (0, \infty)$ are subgroups of $(\C^*, \times)$.

It is straight forward to verify Factorization, Uniqueness, and Commutativity properties.

- Since all complex numbers $z \in \C^*$ are uniquely expressed as $z = |z| \exp(i \arg(z))$.

##### Fundamental theorem of finitely generated abelian groups ==TODO==

Every finitely generated abelian group $G$ is isomorphic to a direct product of cyclic groups in the form
$$
\mathbb{Z}_{\left(p_{1}\right)^{r_{1}}} \times \mathbb{Z}_{\left(p_{2}\right)^{r_{2}}} \times \cdots \times \mathbb{Z}_{\left(p_{n}\right)^{r_{n}}} \times \mathbb{Z} \times \mathbb{Z} \times \cdots \times \mathbb{Z}
$$

- $p_{i}$ are primes, not necessarily distinct.
- $r_{i}$ are positive integers. 
- The direct product is unique except for possible rearrangement of the factors.
  - The number (Betti number of $G$) of factors $\mathbb{Z}$ is unique.
  - The prime powers $\left(p_{i}\right)^{r_{i}}$ are unique.

