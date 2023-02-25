#### Cosets

##### Cosets

Suppose $\a{G, \cdot}$ is a group, and $H \le G$.

- The subgroup $aH$ is the **left coset** of $H$ with representative $a$.
- The subgroup $Ha$ is the **right coset** of $H$ with representative $a$.
- $|H| = |aH| = |Ha|$.
  - $|H| = |aH|$, since $x \mapsto ax$ is a bijection on $H$.

The relations $\sim_{L}$ and $\sim_R$ are defined on $G$ by
$$
a \sim_{L} b \iff a^{-1} b \in H, \quad a \sim_{R} b \iff a b^{-1} \in H
$$

- Then $\sim_{L}, \sim_R$ are equivalence relations on $G$.
- The equivalent classes happens to be the left / right cosets.

$$
a\sim_L b \iff a^{-1}b \in H \iff \exists h\in H,b = ah \iff b \in aH \newline
a\sim_R b \iff b a^{-1} \in H \iff \exists h\in H,b = ha \iff b \in Ha
$$

##### Lagrange's theorem

Suppose $\a{G,\cdot}$ is a finite group and $H \le G$. Then $o(H) \mid o(G)$.

- Since $\abs{\c{aH\mid a \in G}} \cdot |H| = |G|$.

##### Prime order groups are cyclic

Suppose $G$ is a group of prime order. Consider $\langle a \rangle$, $a\neq e \in G$. It must be true that $\langle a \rangle = G$.

##### Set of all cosets

Suppose $\a{G, \cdot}$ is a group, and $H \le G$.

- Define the set of left cosets $G / H = \{a H \mid a \in G\}$.
- Similarly the set of right cosets $G \backslash H = \{Ha \mid a \in G\}$.
- Clearly $|G| = |G/H|\cdot |H|$ when $G$ is finite.
- $|G/H| = (G:H)$ is the **index** of $H$ in $G$.
- $|G/H| = |G\backslash H|$.
  - Consider $f: aH \mapsto Ha^{-1}$. Notice $a_1 \sim_L a_2 \iff a_2^{-1}a_1 \in H \iff$ $ a_2^{-1} \sim_R a_1^{-1}$. So the mapping is a function.
  - $f$ is also a bijection.

##### Group index is multiplicative

Suppose $\a{G, \cdot}$ is a group, and $K \le H \le G$. Then
$$
(G: K) = (G: H) (H : K)
$$
We prove the case where $(G:H)$ and $(H:K)$ are both **finite**.

- Suppose $G/H = \{a_1 H, a_2H, \cdots, a_nH\}$ and $H/K = \{b_1K , \cdots, b_mK\}$.
- Define $A = \{a_i b_j K \mid 1 \le i \le n \land 1 \le j \le m\}$.
- $A$ is a partition of $G$.

  - Let $x \in G$ be any element.
  - There exists unique $1 \le i \le n$ where $x \in a_iH$, so $a_i^{-1}x \in H$.
  - There exists unique $1 \le j \le m$ where $a_i^{-1} x \in b_j K$, so $b_j^{-1} a_j^{-1} x \in K$.
  - Therefore $x \in a_i b_j K$.
  - Suppose $x \in a_s b_t K$ as well. Then
    - $x \in a_i H$ and $x \in a_s H$ implies $i = s$.
    - $a_i^{-1} x \in b_j K$ and $a_i^{-1} x \in b_t K$ implies $j = t$.
- Therefore $A = G / K$.

#### Normal Subgroups

##### Normal subgroups

Suppose $\a{G, \cdot}$ is a group, and $H \le G$.

$H$ is a **normal** subgroup of $G$ if $\forall g \in G :gH = Hg$.

- This relationship is denoted by $H \ltrieq G$.
- When $G$ is abelian, all subgroups are normal.
- The relationship $\ltrieq$ is **not transitive**.

##### Normal subgroup test

Suppose $\a{G, \cdot}$ is a group, and $H \le G$.
$$
\forall g \in G: g H g^{-1} \subseteq H \iff \forall g \in G: gH \subseteq Hg \land Hg \subseteq gH \iff  H \ltrieq G
$$
##### Factor group / Quotient group

Suppose $\a{G, \cdot}$ is a group, and $H \le G$. Then
$$
\forall a, b \in G: (aH)(bH) = (ab)H \iff H \ltrieq G
$$

- ($\from$) Suppose $H \ltrieq G$, then $(aH)(bH) = a(Hb)(H) = a(bH)(H) = ab H$.
- ($\to$) Suppose $(aH)(bH) = (ab)H$, then $\forall a \in G:aH a^{-1}H = H$, therefore $aH a^{-1} \subseteq H$.

Suppose $H \ltrieq G$. $\a{G / H, \cdot}$ is a **group** with operation $\cdot$ defined as
$$
(aH) \cdot (bH) \mapsto (ab)H
$$

- Associative: $(a H)[(b H)(c H)]=(a H)[(b c) H]=[a(b c)] H = [(ab)c]H$.
- Identity: $(a H)(e H)=(a e) H=a H=(e a) H=(e H)(a H)$.
- Inverse: $\left(a^{-1} H\right)(a H)=\left(a^{-1} a\right) H= H =\left(a a^{-1}\right) H=(a H)\left(a^{-1} H\right)$.

$\a{G / H, \cdot}$ is called a factor group or a quotient group.

Suppose $G = \a{g}$ then $G/H = \a{gH}$. Factor groups of cyclic groups are cyclic.

##### Kernels are normal subgroups

Suppose $\a{G, \cdot}, \a{H, \cdot}$ are groups.

Let $\phi: G \to H$ be a group homomorphism. Then $\ker \phi \ltrieq G$.

- For any $g \in G$, and $h \in \ker \phi$. $\phi(g h g^{-1}) = \phi(g) 1_H \phi(g^{-1}) = 1_H$.
- Therefore $\forall g \in G: g \ker(\phi) g^{-1} \subseteq \ker (\phi)$.

##### Normal subgroups are kernels

Suppose $\a{G, \cdot}$ is a group, and $H \ltrieq G$.

Consider $\phi: x \mapsto xH$.

- $\phi$ is a group homomorphism from $G$ to $G / H$.
  - $\forall a, b \in G: \phi(ab) = abH = aH bH = \phi(a)\phi(b)$.

- $\ker \phi = \{x \in G: \phi(x) = H\} = H$.

##### The fundamental theorem of group homomorphisms

Suppose $\a{G, \cdot}, \a{H, \cdot}$ are groups.

Let $\phi: G \to H$ be a group homomorphism.

- Define $\mu: G / \ker \phi \rightarrow \phi[G]$ by $g \ker\phi \mapsto \phi(g)$.
  - $\mu$ is clearly well-defined.

  - $\mu$ is group **isomorphism**.
    - It is an homomorphism as $\mu(ab \ker \phi) = \phi(a) \phi(b)$.
    
    - It is an injection as
      $$
      \mu(a\ker\phi) = \mu(b \ker \phi) \iff a^{-1}b \in \ker\phi \iff a\ker \phi = b \ker \phi
      $$
    
    - it is an surjection by definition.

- Define $\gamma: G \rightarrow G / \ker\phi$ by $g \mapsto g(\ker\phi)$.
  - $\gamma$ is a group homomorphism, see (Normal subgroups are kernels).

The map $\phi$ is factored as $\phi=\mu \circ \gamma$.

##### Fibers of group homomorphism

For $b \in\phi[G]$, $\phi^{-1}\c{b} \in G / \ker \phi$.

- There exists $a \in G$ where $\phi(a) = b$.

- $\mu^{-1}\c{b} = \c{a\ker \phi}$.
- $\phi^{-1} \c{b} = \gamma^{-1} \circ \mu^{-1}\c{b} = a \ker \phi$.

##### Group homomorphisms preserves normal subgroups

Suppose $\phi: A \to B$ is a group homomorphism. $H \ltrieq A$ and $G \ltrieq B$.

- $H \ltrieq A \implies \phi[H] \ltrieq \phi[A]$.
  - $H \ltrieq A \iff \forall a \in A:aHa^{-1} \subseteq H \implies \forall \phi(a) \in \phi[A]:\phi(a) \phi[H] \phi(a)^{-1} \subseteq \phi[H]$.
- $G \ltrieq B \implies \phi^{-1}[G] \ltrieq \phi^{-1}[B]$.
  - $g\in \phi^{-1}[B], x \in \phi^{-1}[G] \implies \phi(g)\phi(x)\phi(g^{-1}) = \phi(gxg^{-1}) \in G \implies gxg^{-1} \in \phi^{-1}[G]$.


##### Subgroup of index 2

Suppose $G$ is a group, and $H < G$ with $(G : H) = 2$, then $H \ltri G$.

- Clearly $G = H + aH = H + Ha$, so $aH = Ha$.
- Consider cyclic subgroup $\a{a}$. Clearly $a^2 = e$, so $a = a^{-1}$.
- Therefore $H \ltri G$. Since
  - For $x \in H$, $xHx^{-1} = H$.
  - For $x \in aH$, WLOG $x = ah$, $ahHh^{-1}a^{-1} = aHa = a^2H = H$.

##### Center subgroup

For group $G$, the center $Z(G)$ of $G$ is defined as 
$$
Z(G): \c{z \in G\mid \forall g \in G: zg = gz}
$$

- $Z(G)$ is an abelian normal subgroup of $G$.
- When $G$ is abelian, $Z(G) = G$.

##### Commutators

For group $G$, the commutator subgroup of $G$ is defined as $C(G) := \c{aba^{-1}b^{-1}\mid a, b \in G}$.

- $C(G)$ is a normal subgroup of $G$.

  - For any $x = aba^{-1} b^{-1} \in C(G)$ and $g \in G$, note the following
    $$
    g^{-1} x g = g^{-1} aba^{-1}b^{-1} g = (g^{-1} aba^{-1})(g b^{-1}b g^{-1})(b^{-1}g)
    $$

  - Therefore $g^{-1} x g \in C(G)$.

- Suppose $N \ltrieq G$ then $G/N$ is abelian if and only if $C(G) \le N$.

  - ($\from$) If $C(G) \le N$ then for any $a, b \in G$,
    $$
    \begin{aligned}
    (a N)(b N) & =a b N=a b\left(b^{-1} a^{-1} b a\right) N \\
    & =\left(a b b^{-1} a^{-1}\right) b a N=b a N=(b N)(a N)
    \end{aligned}
    $$

  - ($\to$) Suppose $G/N$ is abelian.

    - For any $a, b \in G$, $(a^{-1}N)(b^{-1}N) = (b^{-1}N)(a^{-1}N)$. So $(aba^{-1}b^{-1})N = N$.

