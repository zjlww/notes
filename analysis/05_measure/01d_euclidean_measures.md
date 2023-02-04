#### Distributional Functions

(**Boxes in Euclidean spaces**)

A **(bounded) box** in $\R^d$ is the Cartesian product of $d$ real **bounded** intervals. $B = I_1 \times \cdots \times I_d$.

- The volume of $B$ is the product of lengths of $I_i$.

The following are common **semi-rings** of boxes.
- The set of all boxes in $\R^d$ is $\S_d$. Then $\S_d$ is a semi-ring.
- The open boxes $\S_d^\circ := \{S^\circ: S \in \S_d\}$.
- The compact boxes $\S_d^c := \{\overline S: S \in \S_d\}$.
- The left semi-open boxes $\S_d^+ := \{\varnothing\} \cup \{(a, b]: a, b \in \R^d\} \subseteq \P(\R^d)$.
- The right semi-open boxes $\S_d^-$ is similarly defined.

$\S_d^+, \S_d^-$ are sub-semi-rings of $\S_d$. But $\S_d^\circ$ and $\S_d^c$ are only sub-$\pi$-systems of $\S_d$.

**Ring** $\overline \S_d$ generated from semi-ring $\S_d$ is the set of all **elementary sets** in $\R^d$.

(**Box $(a, b]$**)

Consider box $(a, b] \in \S_d^+$.

- The **vertices** of the box are
  $$
  V(a, b]:= \left\{ x \in \mathbb{R}^{d}: \forall 1 \le k \le d: x_{k}=a_{k} \lor   x_{k}=b_{k}\right\}
  $$

- The sign of the vertices are
  $$
  \sgn_{(a, b]}(x) := \sgn(x - (a + b)/2);\quad \sgn(x) = \sgn(x_1, \ldots, x_k) := \prod_{k=1}^d x_k
  $$

We can define $F: \S_d^+ \to \R$ by $F: \R^d \to \R$.
$$
F(a, b] := \Delta^b_a F(x) := \sum_{x \in V(a, b]} \sgn_{(a, b]}(x) F(x)
$$
(**Distributional functions**)

Consider $F: \R^d \to \R$. We define the following properties:

- $F(x)$ is **increasing** if $\forall b \ge a:F(b) - F(a) \ge 0$.
- $F(x)$ is **locally increasing** if $F(a, b] \ge 0$ for all $(a, b] \in \S_d^+$.
  - But $F(x)$ is not necessarily increasing.
- $F(x)$ **has left-limit** at $x \in \R^d$ if $\forall \epsilon > 0, \exists \delta > 0, \forall y \in (x - \delta, x): |F(y) - A| < \epsilon$.
  - The left-limit at $x$ is denoted as $F(x-)$.
- $F(x)$ is **right-continuous** if $\forall x \in \R^d, \forall \epsilon > 0, \exists \delta > 0, \forall y \in [x, x + \delta): |F(y) - F(x)| < \epsilon$.
  - Then $F(x)$ has left-limit everywhere.
  - $F(x)$ is continuous at $x$ iff $F(x) = F(x-)$.
- $F(x)$ is **distributional** if $F$ is right-continuous and locally increasing.

Suppose $F, G: \R^d \to \R$ are distributional.

- $F, G$ are equivalent if $\forall (a, b] \in \S_d^+:F(a, b] = G(a, b]$.

#### Lebesgue-Stieltjes Measures

(**LS measures**)

A **Lebesgue-Stieltjes measure** $\mu$ on $\R^d$ is a measure on $\B(\R^d)$ such that $\mu(B) < \infty$ for all bounded box $B \in \S_d$.

(**Distribution function $\to$ LS measure**)

Suppose $F: \R^d \to \R$ is distributional.

Define $\mu: \S_d^+ \to [0, \infty]$ as $\mu(a, b] = F(a, b]$.

Then $\mu$ is a **$\sigma$-finite measure** on semi-ring $\S_d^+$.

- $\mu$ is a proto-measure: $\mu(\varnothing) = 0$.
- $\mu$ is $\sigma$-finite, just consider $A_j = (-j, j]^d$.
- $\mu$ is finitely additive:
  - Suppose $A, (B_i)_{i = 1}^n \in \S_d^+$. And $A =+_i B_i$.
  - Consider the greatest common grid on $A$. Split $B_i$ into grids. Then take sum.
- $\mu$ is countably subadditive:
  - Suppose $A, (B_i)_{i = 1}^\infty \in \S_d^+$. And $A = \cup_i B_i$.
  - Suppose $A = \times_i (a_i, b_i]$ and $B_i = \times_j (a_{ij}, b_{ij}]$.
  - For any $\epsilon > 0$.
    - Shrink the lower end of $A$ to get box $C = \times_i(a_i + \delta, b_i]$. Where $\mu(A) \le \mu(C) + \epsilon$.
    - Extend the upper end of $B_i$ by $\eta_i$ to get boxes $D_i = \times_j(a_{ij}, b_{ij} + \eta_i]$. Such that $\mu(D_i) \le \mu(B_i) + \epsilon / 2^i$.
    - So $\p{D_i^\circ}$ is an open cover of $\overline C$. There is a finite subcover $\p{D^\circ_{i_k}}$.
    - Then $\cup_k D_{i_k}$ must covers $C$.
    - So $\mu(C) \le \mu(\cup_k D_{i_k})\le \sum_k\mu(D_{i_k}) \le \sum_i \mu(D_i)$. And $\mu(A)\le \sum_i \mu(B_i) + 2\epsilon$.
  - So $\mu(A) \le \sum_{i} \mu(B_i)$.

The measure of other kinds of boxes can be directly given by:

- $\mu[a, b] = F(b) - F(a-)$.
- $\mu(a, b) = F(b-) - F(a)$.
- $\mu[a, b) = F(b-) - F(a-)$.
- $\mu\{x\} = F(x) - F(x-)$.

Now by extension theorems:

- $\overline \mu$ is the **unique** measure extending $\mu$ from $\S_d^+$ to $\overline \S_d^+$.
- $\widetilde \mu$ is the **unique** measure extending $\mu$ from $\S_d^+$ to $\widetilde \S_d^+$.
- $\mu^*$ is the **unique** measure extending $\mu$ to any $\sigma$-algebra $\M \le \M_{\mu^*}$.

For convenience, denote $\M_{\mu^*}$ as $\L_F^d$.

Therefore, we will say that $\mu^*$ is the **induced (LS) measure** by $F$ on $\L_F^d$.

- $\mu, \overline \mu, \widetilde \mu, \mu^*$ are all $\sigma$-finite.
- $\widetilde \S_d = (\S_d)_\sigma = \sigma(\S_d) = \B(\R^d) \subset \L_F^d$.

(**LS measure by outer open sets**)

Suppose $\mu^*$ is the LS measure induced by $F$ on $\L_F^d$.

$E \in \L_F^d$ iff for all $\epsilon > 0$, there exists open set $U$ containing $E$ and $\mu^*(U - E) \le \epsilon$.

- $\to$ Suppose $E \in \L_F^d$.
  - There exists $A \in \p{\S_d^+}_\sigma$ such that $A \supseteq E$ and $\mu^*(A - E) \le \epsilon$.
  - Suppose $A = \cup_{k=1}^\infty A_k$ where $A_k \in \S_d^+$.
  - It is easy to modify $A$ to generate open set $B \supseteq A$ where $\mu^*(B - A) \le \epsilon$.
- $\from$
  - Construct open set sequence $U_n$ by taking $\epsilon = 1/  n$.
  - Clearly $\cap_n U_n \supseteq E$. $\mu^*(\cap_n U_n - E) = 0$. And $\cap_n U_n \in \L_F^d$.

$E \in \L_F^d$ iff $E$ is a $G_\delta$ set subtract some $\mu^*$-null set.

- The proof immediately follows from the above results.

(**LS measure by inner closed sets**)

Suppose $\mu^*$ is the LS measure induced by $F$ on $\L_F^d$.

$E \in \L_F^d$ iff for all $\epsilon > 0$, there exists closed set $K$ inside $E$ and $\mu^*(E - K) \le \epsilon$.

$E \in \L_F^d$ iff $E$ is a $G_\delta$ set union some $\mu^*$-null set.

These results immediately follows the open set counterpart.

#### Jordan-Stieltjes Measures

(**Elementary measure**)

Suppose $F: \R^d \to \R$ is distributional.

And $\mu$ is the induced measure by $F$.

**The restriction of $\mu$ on ring $\overline \S_d$ is the elementary measure induced by $F$.**

(**Jordan contents**)

Suppose $\mu$ is the measure induced by distributional $F: \R^d \to \R$.

Define **Jordan outer content** $m^*: \P(\R^d) \to [0, \infty]$ induced by $F$ as
$$
m_* (E) := \sup_{A \in \overline \S_d, A \subseteq E} \mu(A)
$$
Similarly define **Jordan inner content** $m_*: \P(\R^d) \to [0, \infty]$ induced by $F$ as
$$
m^*(E): = \inf_{B \in \overline \S_d, E \subseteq B} \mu(B)
$$
(**Jordan measurable sets**)

Suppose $m^*, m_*$ are the Jordan contents induced by distributional $F: \R^d \to \R$.

$E \in \P(\R^d)$ is **Jordan measurable** if $m_*(E) = m^*(E) < \infty$.

The following are equivalent conditions of $m_*(E) = m^*(E)$, when $m^*(E) < \infty$.

- $\forall \epsilon > 0, \exists A, B \in \overline \S_d: A \subseteq E \subseteq B \land m^*(B - A) \le \epsilon$.
- $\forall \epsilon > 0, \exists A \in \overline \S_d: m^*(A \Delta E) \le \epsilon$.


Let $\J_F^d$ be the set of all Jordan measurable sets.

- $\J_F^d$ is a **ring**.
  - $\J_F^d$ is closed under union.
    - Consider $A, B \in \J_F^d$.
    - There exists $A', B' \in \overline S_d$ where $m^*(A \Delta A') \le \epsilon$ and similar for $B$.
    - Consider $C = A \cup B$ and $C' = A' \cup B'$.
      $$
      C \Delta C' = (A \cup B) \Delta (A'\cup B') \subseteq (A \Delta A') \cup (B \Delta B')
      $$
    - Therefore $m^*(C \Delta C') \le 2 \epsilon$.
    - $\J_F^d$ is closed under difference.
      - The proof is similar to the union case.
  - $\J_F^d$ is a proto-ring.

(**JS measure**)

Suppose $m^*, m_*$ are the Jordan contents induced by distributional $F: \R^d \to \R$.

Define **Jordan-Stieltjes measure** $m: \J_F^d \to [0, \infty)$ induced by $F$, as
$$
m(E) := m^*(E) = m_*(E)
$$
Then $m$ is a finite-additive measure on ring $\J_F^d$.

- As the $m_*$ is finitely additive.

The JS measure $m$ is "complete":
- Subsets of Jordan null sets remains Jordan null sets.
- Jordan measure zero iff Jordan outer measure zero.

(**Relationships between induced LS and JS measures**)

Consider distributional $F: \R^d\to \R$.

- Suppose $m$ is the JS measure induced by $F$ on $\J_F^d$.
- Suppose $\mu$ is the LS measure induced by $F$ on $\L_F^d$.

We have the following relationships:

- $\overline \S_d^+ \subseteq \J_F^d$. This immediately follows from the definition.
- $\J_F^d \subseteq \L_F^d$. And $m = \mu$ on $\J_F^d$.
  - Suppose $E \in \J_F^d$. Then $E \in \L_F^d$.
    - By definition of $m_*(E)$. Construct a increasing sequence $\p{D_n}$ where $D_n \subseteq E$, and $\mu(D_n) \to m(E)$.
    - $N = \cap_n (E - D_n) = E - \cup D_n$ is a $\mu$-null set. And $\cup D_n \in \L_F^d$.
  - $m(E) = \mu(E)$.
    - By definition of $m^*(E)$. Construct a decreasing sequence $\p{F_n}$ where $E \subseteq F_n$, and $\mu(F_n) \to m(E)$.
    - $\mu(D_n) \le m(E) \le \mu(F_n)$.
    - Take limits $n \to \infty$ gives $\mu(\cup D_n) = m(E) = \mu(\cap F_n) = \mu(E)$.
- $\J_F^d = \c{m^*(E) < \infty: E \in \L_F^d}$.
  - Suppose $E \in \L_F^d$ with $m^*(E) < \infty$.
  - $\mu$ is a finitely-additive measure on semi-ring $\S_d^+$.
  - Therefore there exists $A \in \overline \S_d^+$ where $\mu(A \Delta E) \le \epsilon$. (**See approximations.**)
  - Therefore $E \in \J_F^d$.
- For $E \in \P(\R^d)$, we have $m_*(E) \le \mu(E) \le m^*(E)$.

(**The Jordan and the Lebesgue measure on $\R^d$**)

Consider $I: \R^d \to \R$ as $(x_1,\ldots, x_d) \mapsto x_1 \cdots x_d$. Clearly $I$ is distributional.

- The JS measure $m$ induced by $I$ on $\J(\R^d) := \J_F^d$ is the **Jordan measure** on $\R^d$.
- The LS measure $\lambda$ induced by $I$ on $\L(\R^d):= \L_F^d$ is the **Lebesuge measure** on $\R^d$.

