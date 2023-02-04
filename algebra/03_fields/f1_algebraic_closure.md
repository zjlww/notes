#### Algebraic Closures

##### Subrings of algebraic field extensions are fields

Consider **algebraic** field extension $E/F$.

For any subring $R$ where $F \le R  \le E$, $R$ is a field.

- For any $\alpha \in R$, $F[\alpha] \subseteq R$, so $\alpha^{-1} \in F[\alpha] \subseteq R$.

##### Transitivity of Algebraic Extension

Suppose $E/F$ is algebraic, $L/E$ is algebraic, then $L/F$ is algebraic.

- We only need to show that any $\alpha \in L$ is algebraic over $F$.

- Let $p(x) = \operatorname{irr}(\alpha, E)$, suppose $p(x) = a_ix^i$, $a_i \in E$.

- Consider the extension chain
  $$
  F < F[a_0] < F[a_0, a_1] < \cdots < F[a_i, \alpha]
  $$

- Each extension is finite, so $F < F[\alpha, a_i]$ is finite. So $\alpha$ must be algebraic over $F$​.

Algebraic extensions are **transitive**, so we can also say $L/E/F$ is algebraic.

##### Algebraic closure subfield

Consider field extension $E/F$. Collect elements in $E$ that are algebraic over $F$ as $F_E$.

$F_E$ is a field, called the **algebraic closure** of $F$ in $E$.

- Suppose $\alpha, \beta \in F_E$, then $F< F[\alpha, \beta]$ is finite field extension.
- Then $\alpha - \beta$, and $\alpha / \beta$ are all inside $F_E$.


##### The field of algebraic numbers

The set of all algebraic numbers is the algebraic closure of $\mathbb Q$ in $\mathbb C$, that is $\mathbb Q_{\mathbb C}$.

- Recall that $x^{n} - p$ is a monic irreducible in $\Q[x]$ for prime $p$.
- Therefore $[\Q_\C:\Q]$ can not be finite. This is an **infinite algebraic extension**.

##### Algebraically closed field

A **field** $F$ is **algebraically closed** if any of the following is true:

1. Every non-constant polynomial in $F[x]$ factors into **linear** factors in $F[x]$.
2. $F$ has no proper algebraic extension.

##### Algebraic closure

Suppose $E/F$ is **algebraic** and $E$ is **algebraically closed**, $E$ is called an **algebraic closure** of $F$.

- We often write $\overline F$ to denote an algebraic closure of $F$.

##### A splitting algebraic extension is an algebraic closure

Suppose $K/F$ is algebraic and every $f \in F[x]$ has all roots in $K$, $K$ is an algebraic closure of $F$.

- Suppose $G / K$ is a **proper** algebraic extension. Then $G/F$ is algebraic.
- For $\alpha \in G$, $\irr(\alpha, F)$ has all roots in $K$. So $\alpha \in K$.
- Therefore $G = K$. There are no proper algebraic extensions to $K$.

##### Uniqueness of algebraic closure

Consider field extension $K / F$ where $K$ is algebraically closed.

The embedded algebraic closure $F_K$ is algebraically closed.

- Suppose non-constant $p \in F_K[x]$, $p$ splits in $K$.
- Suppose $\alpha \in K$ is a root of $p$.
- $F_K[\alpha] / F_K$ is algebraic, $F_K / F$ is algebraic. So $F_K[\alpha] / F$ is algebraic.
- Therefore $F_K[\alpha] = F_K$.

All algebraic closures of $F$ inside $K$ are the same.

- Consider field extensions $K / A / F$ and $K / B / F$.
- Suppose $A, B$ are algebraic closures of $F$ inside $K$. Then $A = B$.
  - Suppose $\alpha \in A$. Let $p(x) = \irr (\alpha, F) \in F[x]$.
  - $p(x)$ splits in $A, B, K$.
  - Therefore the set of zeros of $p(x)$ in $A, B, K$ are the same.
  - Therefore $\alpha \in B$. $A \subseteq B$.
  - By symmetry, $B \subseteq A$. So $A = B$.

Therefore the embedded algebraic closure $F_K$ is the only algebraic closure of $F$ in $K$.

##### Existence of algebraic closure: countable case

Suppose $F$ is a countable field, then there exists an **algebraic closure** of $F$.

- Since $F$ is countable, $F[x]$ is countable. Let $\p{p_i(x)}_{i = 1}^\infty = F[x]$.
- Now construct the splitting field of $p_1, (p_1, p_2), \ldots$ and so on.
- The splitting fields form an ascending chain $F \le F_1 \le F_2 \le \ldots$
- Define $G := \cup_i F_i$. Then $G$ is an algebraic closure of $F$.
  - $G$ is a field. $G / F$ is clearly an algebraic extension.
  - $G$ is algebraically closed.
    - Suppose irreducible $p(x) \in G[x]$ and $p(x) = \sum_{i = 0}^d a_i x^i$.
    - Consider $F \le F[a_0, \ldots, a_d] \le F[a_0, \ldots, a_d][\alpha]$.
      - Where $\alpha$ is a root of $p(x)$ in some extension field of $F[a_0, \ldots, a_d]$.
    - Clearly $F[a_0, \ldots, a_d, \alpha] / F$ is algebraic. So $\alpha \in G$.
