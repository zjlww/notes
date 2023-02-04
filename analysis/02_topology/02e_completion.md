#### Completion of Metric Spaces

(**Completion of metric spaces**)

A **completion** of $(E, d)$ is a complete metric space $(\widetilde E, \widetilde d)$ together with an isometry $\varphi: E \to \widetilde E$, such that $\varphi[E]$ is dense in $\widetilde E$.

(**Completeness Lemma**)

Let $(X, d)$ be a metric space and $A$ a dense subset such that every Cauchy sequence in A converges in $X$. Then $X$ is complete.

- Suppose $\p{x_n}$ is Cauchy in $X$.
- Define $C_n :=B(x_n, 1/n) \cap A$. $C_n \neq \varnothing$ since $A$ is dense.
- Pick sequence $\p{y_n}$ from $C_n$.
- Now $\p{y_n}$ is Cauchy. Suppose $y_n \to y \in X$.
- It is easy to show that $x_n \to y$ as well.

(**Existence of completion**)

Suppose $(E, d)$ is a metric space. It has a **completion**.

Consider the following construction of $\widetilde E, \widetilde d$ and $\varphi$.

- Define $\overline E$ as the set of all Cauchy sequences in $E$.
  $$
  \overline E:= \{(a_n)_{n = 1}^\infty \in E: \lim_{n, m\to\infty}d(a_n, a_m) =  0\}
  $$
  
- Define $\bar d[(a_n), (b_n)]:= \lim_{n \to \infty} d(a_n, b_n)$.
  - The limit does exist. So $\overline d$ is well defined.
    - $|d(a_n, b_n) - d(a_m, b_m)| \le d(a_n, a_m) + d(b_n, b_m)$.
    - So $d(a_n, b_n)$ is Cauchy.
  - $\bar d$ is a **pseudometric** on $\overline E$.
  
- $(a_n), (b_n) \in \overline E$ are **equivalent** or $(a) \sim (b)$ if $\lim_{n \to \infty} d(a_n, b_n) = 0$.
  - $\sim$ is indeed an equivalent relationship on $\overline E$.
  - Define $\widetilde E = \{[a_n]: (a_n) \in \overline E\}$ to be the set of all equivalent classes.
  
- Define $\widetilde d([a_n], [b_n]) = \overline d[(a_n), (b_n)]$.
  - Suppose $(a'_n)\sim (a_n)$, then
    $$
    \lim_n d(a'_n, b_n) \le \lim_n d(a_n, a'_n) + \lim_nd(a_n, b_n)
    $$
  
  - So $\widetilde d$ is well defined. And $\widetilde d$ is a **metric** on $\widetilde E$.
  
- Denote $\hat x := (x, x, \ldots)$. $\varphi(x) := [\widehat x]$ is clearly an **isometry**.

- And $\varphi[E]$ is dense in $\widetilde E$.

The constructed metric space $(\widetilde E, \widetilde d)$ is complete. We proceed with the Completeness Lemma.

- Suppose $([\widehat x_n]) = \p{[\widehat x_1], [\widehat x_2],\ldots}$ is Cauchy in $\varphi[E]$.
- Clearly $(x_n) = (x_1, x_2, \ldots)$ is Cauchy in $E$.
- $[\widehat x_n] \to [(x_m)]$.
  - $\widetilde d\p{[\widehat x_n], [(x_m)]} = \overline d( \widehat x_n, (x_m)) = \lim_{m\to\infty}d(x_n, x_m)$.
  - Clearly $\widetilde d\p{[\widehat x_n], [(x_m)]} \downarrow 0$.

#### The Real Space

(**Construction of $\R$**)

$\p{\Q, d}$ is a metric space. Let $\p{\R, d}, \varphi$ be a completion.

- Define $+, \times$ operations on $\R$ as element-wise addition and multiplication.
  - The operations are well defined.
- It is easy to verify that $\R$ is a field under these operations.

For $\R^n$, we construct the product metric space with the product metric.

- All product metrics generates the same topology on $\R^n$.
- $\R^n$ is clearly complete.

(**The Dyadic mesh of $\R^d$**)

Consider the space $\R^d$. For some $n, i_k \in \Z$,
$$
C = \left[\frac{i_{1}}{2^{n}}, \frac{i_{1}+1}{2^{n}}\right) \times \ldots \times\left[\frac{i_{d}}{2^{n}}, \frac{i_{d}+1}{2^{n}}\right)
$$
is a **dyadic cube**. Similarly we have **open dyadic cube** $C^\circ$ and **closed cube** $\overline C$.

- The set of all dyadic cube is the dyadic mesh denoted $\mathcal Q(\R^d)$.
- The set of all dyadic cube with side-length $2^{-n}$ is $\mathcal Q_n(\R^d)$.
- $\mathcal Q(\R^d)$ is countable.

Suppose $E \in \R^d$ is an open set. Then $E$ can be expressed as the countable union of dyadic cubes in $\mathcal Q(\R^d)$.

(**Set of all rational open balls in $\R^n$**)

$\Q^n \times \Q^+$ is countable, interpret the first two as coordinates and the last as radii. Construct countable set $G$ with elements being balls having **rational radii** and centers at points with **rational coordinates**.

Similarly, we can construct the set of all rational open boxes.

- Open sets in $\R^n$ are countable unions of rational open balls, and rational open boxes.

(**Linear ordering of $\R$**)

Suppose $S \subseteq \R$.

- $b \in \R$ where $\forall x \in S: x \le b$ is an **upper bound** of $S$.
- $b \in S$ where $\forall x \in S: x \le b$ is the **maximum element** of $S$.
  - The maximum is **unique** if exists, denoted by $b=\max S$.
- $b \in \R$ where $b$ is an upper bound of $S$ and no other upper bound is lower than $b$, $b$ is called a **least upper bound** of $S$, or **supremum** of $S$.
  - The supremum is **unique** if exists ,denoted by $b = \sup S$.
- Similarly defines the **greatest lower bound**, or **infimum** $\inf S$.
- Similarly there is greatest lower bound $\inf S$, and minimum $\min S$.

(**Completeness Axiom of $\R$**)

Suppose $S \subseteq \R$ and $S$ is bounded above, then $S$ has the supremum in $\R$.

- Define $a_n := \max \c{m 2^{-n} \in S: m \in \Z}$.
- Since $S$ is bounded above, clearly $a_n \in \Q$ is well defined.
- Then $[(a_n)]$ is clearly the supremum of $S$ in $\R$.

(**Open set representation theorem of $\R$**)

Suppose $S$ is open in $\R$.

- For $x \in \R$, define the interval as $I_{x}=(a(x), b(x))$ where
  $$
  a(x)=\inf \{a \in \R\mid(a, x) \subseteq S\}, b(x)=\sup \{b\in \R\mid(x, b) \subseteq S\}
  $$

- $I_x$ is called a component interval of $S$.

- Denote the equivalence relationship $x \sim y \iff I_x = I_y$ for $x, y \in S$.

- The partition $S / \sim$ is the interval partition of $S$.

  - $S / \sim$ is countable. Since $\Q$ is dense and countable.

(**Lindelöf Covering Theorem**)

Assume $A \subseteq \R^{n}$ and let $F$ be an **open covering** of $A$. Then there is a **countable** subset of $F$ which also covers $A$.

- There exists a countable open cover of $\cup F$ consists of open balls.

(**Heine-Borel Theorem**)

$S \subseteq \R^n$ is compact iff $S$ is closed and bounded.

- This immediately follows from the general theorem in metric spaces.
  - Bounded sets in $\R^n$ are totally bounded.
  - Closed sets in $\R^n$ are complete.

(**$\R\backslash \Q$ is not a countable union of closed sets**)

Otherwise, $\R$ is the countable union of closed, empty interior sets, which contradicts Baire's Theorem.

(**Bijection from $[0, 1)$ to $\{0, 1\}^\infty$**)

Define $b_k: [0, 1) \to \{0, 1\}$ and $b: [0, 1) \to \{0, 1\}^\infty$as  following:
$$
b_k(x) = 1\p{ 
\{2^{k-1} x\} \ge 1/2
};\quad b(x) = (b_1(x), b_2(x), \ldots)
$$

- $\c{x }$ is the decimal part of $x$.
- $b(x)$ is clearly injective, but not surjective.

