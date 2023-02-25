#### Metric Spaces

##### Metric space

A **metric space** is a nonempty set $M$ together with a metric function $d:M \times M \to [0, \infty)$.

The **metric** $d$ satisfying the following four properties for all points $x, y, z$ in $M$:

1. $d(x, x)=0$.
2. $d(x, y)>0$ if $x \neq y$.
   - $d(x, y) \ge 0$ gives **pseudo-metrics**.
   - Pseudo-metrics can be converted into metrics by processing equivalence classes.
3. $d(x, y)=d(y, x)$.
4. $d(x, y) \leq d(x, z)+d(z, y)$.

When $d$ is allowed to obtain $+\infty$, we call $d$ an **extended metric**.

##### Distances in metric spaces

Suppose $(M, d)$ is a metric space. And $E, F \subseteq M$.

- Distance between set $E$ and $F$: $\operatorname{dist}(E, F):=\inf \{d(x-y): x \in E, y \in F\}$.
- Distance between $x \in M$ and set $E$: $\operatorname{dist}(x, E) = \operatorname{dist}(\{x\}, E)$
  - $\operatorname{dist}(x, E) = 0$ iff $x \in \overline E$.
- Diameter of a set: $\operatorname{diam}(E):=\sup \{d(x, y): x, y \in E\}$.

##### Metric subspace

$S \subseteq M$ with the same metric $d$ is called a **metric subspace** of $M$.

##### Open balls in metric spaces

Suppose $(M, d)$ is a metric space. For $r \in (0, \infty)$.
- $B_M(a; r) := \c{x \in M: d(x, a) < r}$ is an **open ball** with radius $r$ at $a$.
- $U_M(a; r):= \c{x \in M: d(x, a) \in (0, r)}$ is a **centerless open ball** with radius $r$ at $a$.

Let $\mathcal B$ be the set of all open balls in $M$.

- $\mathcal B$ is a basis of topology.
  - $\mathcal B$ covers $M$.
  - Finite intersections of open balls are unions of open balls.

Consider the generated topology $G_{\mathcal B}$.

- $G_{\mathcal B}$ is the set of all **open sets** in metric space $M$.
- $G_\mathcal B$ is the **Euclidean topology**, the **usual / ordinary topology** on $M$.

$M$ with the Euclidean topology has following properties:

- $M$ is Hausdorff.
- $M$ is first-countable.

##### Point classification in metric spaces

Suppose $(M, d)$ is a **metric space**. And $S \subseteq M$.

With the **Euclidean topology**, we have following equivalent definitions:

- $x$ is an **interior point** of $S$ in $M$ if $B_M(x, r) \subseteq S$ for some $r \in (0, \infty)$.
- $x$ is an **adherent point** of $S$ in $M$ if $\forall r > 0: B_M(x, r) \cap S \neq \varnothing$.
- $x$ is an **accumulation point** of $S$ in $M$ if $\forall r > 0: U_M(x, r) \cap S \neq \varnothing$.
- $x$ is an **boundary point** of $S$ in $M$ if $x$ adheres to $S$ and $S^c$ in $M$.

We also define the derived sets:

- **Interior** of $S$ in $M$ denoted by $S^\circ$ is the set of all interior points of $S$ in $M$.
  - $S^\circ$ is open in $M$. Since it is the union of open balls.
- **Closure** of $S$ in $M$ denoted by $\overline S$ is the set of all adherent points of $S$ in $M$.
  - $\overline S$ is closed in $M$. Since $M - \overline S$ is open.
- **Derived set** of $S$ in $M$ denoted by $S'$ is the set of all accumulation points of $S$ in $M$.
- **Boundary set** of $S$ in $M$ denoted by $\part S$ is $\part S = \overline S \cap \overline {S^c} = \overline S - S^\circ$.
  - $\part S$ is closed in $M$. Since intersection of two closed sets are closed.

##### Metric subspace

Suppose $\p{M, d}$ is a **metric space**. And nonempty $S \subseteq M$.

Then $(S, d|_{S \times S})$ is called a **metric subspace** of $(M, d)$.

- $S$ is the topological subspace of $M$ under the Euclidean topology.

#### Boundedness of Metric Spaces

##### Boundedness in metric spaces

Suppose $(M, d)$ is a metric space. $M$ is bounded if for some $r > 0$, $\forall s, t \in M: d(s, t) < r$.

- A subset $S \subseteq M$ is bounded if $(S, d|_S)$ is bounded.
- A function $f: A \to M$ is bounded if $f[A]$ is bounded.

##### Totally bounded and $\epsilon$-nets

Suppose $(M, d)$ is a metric space.

Let $\epsilon > 0$, a set $\c{x_\alpha}_{\alpha \in I}$ is an $\epsilon$-net for metric space $M$ if $M$ is covered by $\epsilon$-balls centered at $\c{x_\alpha}$.

$M$ is totally bounded if it has a **finite $\epsilon$-net** for all $\epsilon > 0$.

- Totally bounded metric spaces are clearly bounded.
- A subset $S \subseteq M$ is totally bounded if $(S, d|_S)$ is totally bounded.

#### Completeness of Metric Spaces

##### Sequence limit

Suppose $S$ is a topological space. Where $N$ is the Neighborhood topology.

Consider the sequence $(x_n)_{n=1}^\infty \subseteq S$, and $p \in S$.

$(x_n)$ converge to $p$, denoted by $x_n \to p$, if
$$
\forall B \in N(p), \exists N \in \Z, \forall n \ge N: x_n \in B
$$
We have following statements:

- $x_n \to p$ then $p \in \overline{\p{x_n}_{n=1}^\infty}$ in $S$.
  - This follows immediately from the definition of adherent points.
- For $A \subseteq S$, and $p \in \overline A$, there exists $\p{x_n}_{n=1}^\infty \subseteq A$ and $x_n \to p$.
  - Apply the definition of adherent points, and the axiom of choice.
- $x_n \to p$ iff all subsequence $x_{k(n)} \to p$.

Suppose $S$ is Hausdorff, a sequence can only converge to a single point.

- Suppose $\p{x_n}_{n=1}^\infty \subseteq S$ converges to both $p, q \in S$ where $p \neq q$.
- Take $B_p$ where $\forall n \ge N_p: x_n \in B_p$. Similarly $B_q$ where $\forall n \ge N_q: x_n \in B_q$.
- However $S$ is Hausdorff, we can take $B_p$ disjoint from $B_q$.

Suppose $S$ is a metric space. We have an alternative definition of convergence:
$$
x_n \to p \iff \forall \epsilon > 0,\exists N \in \Z,\forall n \ge N: x_n \in B_S(p, \epsilon)
$$

- $x_n \to p$ iff $d(x_n,p) \to 0$ in $\R$.
- $x_n \to p$ then $\p{x_n}_{n \ge 1}$ is bounded in $S$.

##### Complete metric spaces

Suppose $(M, d)$ is a metric space.

- Sequence $(x_n)_{n = 1}^\infty$ is **Cauchy** if $\forall \epsilon > 0, \exists N \in \Z, \forall n, m \ge N: d(x_n, x_m) \lt \epsilon$.
  - Converging sequences are Cauchy.
  - Suppose $\p{x_n}$ is Cauchy, and $p \in \p{x_n}'$, then $x_n \to p$.

$M$ is complete if all Cauchy sequences in $M$ converges in $M$.

A subset $S\subseteq M$ is complete if subspace $(S, d|_S)$ is complete.

##### Complete metric subspaces

Suppose $(M, d)$ is a metric space.

$S \subseteq M$ is a complete metric subspace iff $S$ is closed in $M$.

- $\to$ Suppose $S$ is a complete metric subspace.
  - We only need to show $S = \overline S$. Clearly $S \subseteq \overline S$ is true.
  - Suppose $p \in \overline S$. Then $p \in S$. So $S \supseteq \overline S$.
    - Consider the sequence of neighborhood $\p{B_S\p{p, 1/n}}_{n=1}^\infty$.
    - By axiom of choice, construct sequence $\p{x_n}_{n=1}^\infty$ where $x_n \in B_S(p, 1/n)$.
    - By completeness, $p \in S$.
- $\from$ Suppose $S$ is closed in $M$.
  - Suppose $\p{x_n}_{n=1}^\infty \subseteq S$ is Cauchy. Then $x_n \to p \in M$.
  - We only need to show that $p\in S$.
  - Clearly $p \in \overline S$. Since $S$ is closed, $S = \overline S$, so $p \in S$.

#### Sequentially Compact

##### Sequentially compact

Suppose $(M, d)$ is a metric space.

$M$ is called **sequentially compact** if every sequence $\p{p_n} \subseteq M$ has a convergent subsequence.

**$M$ is sequentially compact if and only if $M$ is totally bounded and complete.**

- If $M$ is sequentially compact, then $M$ is complete.
  - Suppose $\p{x_n}$ is Cauchy in $M$.
  - Suppose $\p{y_n}$ is a subsequence and $y_n \to p$.
  - Then $p$ is an adherent point of $\p{x_n}$. Therefore $x_n \to p$.
- $M$ is sequentially compact then $M$ is totally bounded.
  - Suppose $M$ is empty, the result is trivially true.
  - Suppose $M$ is not totally bounded. There exists some $\p{a_n} \subseteq M$ and $\epsilon > 0$ such that
    $$
    \forall k \in \N: \cup_{n =1}^k B(a_n, \epsilon) \subset M
    $$
  - Define set sequence $A_k := M - \cup_{n=1}^k B(a_n, \epsilon) \neq \varnothing$.
  - By the axiom of choice, there exists a sequence $(b_n) \subseteq M$ such that $b_n \in A_n$.
  - The sequence $\p{b_n}$ cannot converge, but it does. Contradiction!
- If $M$ is complete and totally bounded, then $M$ is sequentially compact.
  - Consider sequence $\p{x_n} \subseteq M$. We now construct a subsequence that converges.
  - Consider the sequence of $1/n$-nets, $\p{M_n} = \p{\c{x_\alpha}_{\alpha \in I_n}}_{n=1}^\infty$.
  - For all $n$, there exists at least one $c_n \in M_n$ such that $B(c_n, 1/n)$ contains infinitely many terms in $\p{x_n}$.
  - By axiom of choice, there exists a subsequence of $\p{x_n}$, denoted by $\p{y_n}$ such that $B(c_n, 1/n)$ contains all $y_{\ge n}$. Therefore $\p{y_n}$ is Cauchy! And it converges!

##### Sequentially compact subspaces

Suppose $(M, d)$ is a sequentially compact metric space.

$S \subseteq M$ is a sequentially compact metric subspace iff $S$ is closed in $M$.

- $\to$ Suppose $S$ is sequentially compact.
  - $S$ is complete, therefore closed in $M$.
- $\from$ Suppose $S$ is closed in $M$.
  - $S$ is clearly totally bounded since $M$ is totally bounded.
  - $S$ is complete since it is closed in complete metric space $M$.

##### Intersection of decreasing closed sets

Suppose $(M, d)$ is a metric space.

**$M$ is sequentially compact iff every decreasing sequence of closed nonempty sets in $M$ has nonempty intersection.**

- $\to$ Suppose $M$ is sequentially compact.
  - Suppose $\p{F_n}_{n=1}^\infty$ is a sequence of closed nonempty sets in $M$.
  - With axiom of choice, construct sequence $\p{f_n}$ where $f_n \in F_n$.
  - Suppose some subsequence $\p{f_{n_k}}_{k=1}^\infty$ converges to $p \in M$.
  - $\forall n \ge 1: p \in F_n$, so $p \in \cap_n F_n$.
    - Since each $F_n$ is closed, and $p$ is an adherent point for each $F_n$.
- $\from$ Suppose $\p{x_n} \subseteq M$ is any sequence.
  - Define $T_n = \c{x_k: k \ge n}$. And $F_n = \overline{T_n}$.
  - Then $\p{F_n}$ is a decreasing sequence of non-empty, closed sets.
  - So there exists $x \in \cap_n F_n$. Notice that $x \in \cap_n \overline T_n$.
  - It is possible to pick a subsequence $\p{x_{k_n}}$ s.t. $x_{k_n} \in B_M\p{x, 1/n}$.

##### Lebesgue Covering Lemma

Suppose $(M, d)$ is a **sequentially compact metric space**.

Suppose $\p{G_\alpha}_{\alpha \in I}$ is an open cover of $M$. Then
$$
\exists \delta > 0, \forall x \in M, \exists \alpha \in I: B\p{x, \delta} \subseteq G_\alpha
$$

- Suppose such $\delta$ does not exist.
- For $\delta = 1/n$, there exists $x_n \in M$ where $B(x_n, 1/n) \not\subseteq G_\alpha$.
- The sequence $\p{x_n}$ has subsequence $\p{x_{n_k}}$ where $x_{n_k} \to_k x$.
- Since $x \in M$, $x \in G_\alpha$ for some $\alpha \in I$.
- Suppose $x \in B(x, \epsilon) \subset G_\alpha$ for $\epsilon > 0$.
- But for $n$ large enough, clearly $x_n \in B(x, \epsilon/2)$. Contradiction!

##### Bolzano-Weierstrass Theorem

Suppose $(M, d)$ is a sequentially compact metric space.

If $S \subseteq M$ is infinite and bounded, then $S'$ is not empty.

- There exists a closed bounded ball $B \subseteq M$, where $S \subseteq B$.
- $B$ is sequentially compact, since $B$ is complete, and totally bounded.
- It is possible to construct sequence $\p{x_n} \subseteq S$ with distinct elements.
- $\p{x_n}$ has a converging subsequence, therefore $S'$ is not empty.

#### Compactness of Metric Spaces

##### Compact metric spaces

**A metric space is compact iff it is sequentially compact.**

Consider metric space $(M, d)$.

- $\from$ Suppose metric space $M$ is sequentially compact with open cover $\p{G_\alpha}_{\alpha \in I}$.
  - With Lebesgue covering lemma, there exists $\delta > 0$ where all $\delta$-balls are covered by $G_\alpha$.
  - $M$ is totally bounded. So there exists a finite $\delta$-net of $M$.
  - Clearly only a finite subset of $\p{G_\alpha}$ is required to cover finite number of $\delta$-balls.
- $\to$ Suppose metric space $M$ is compact. Consider any decreasing nonempty closed sets $\p{F_n}_{n=1}^\infty$.
  - Define $G_n := M - F_n$.
  - $\cup_n G_n \neq X$.
    - Otherwise, $\p{G_n}$ is an open cover. So there is a finite subcover.
    - For some $M \in \N^+$, $\cup_{n=1}^M G_n = X$.
    - Therefore $\cap_{n=1}^M F_n = F_M = \varnothing$. Contradiction!
  - Therefore $\cap_{n=1}^\infty F_n \neq X$.

##### Compact metric subspaces

Suppose $(M, d)$ is a compact metric space.

**$S \subseteq M$ is a compact metric subspace iff $S$ is closed in $M$.**

- $\to$ Suppose $S$ is compact.
  - This is a special case of the general result for Hausdorff spaces.
  - An alternative proof:
    - Suppose $p \in \overline S - S$.
    - Consider the open cover of $S$ defined as $O := \c{B_S\p{x, d\p{x,p}}: x \in S}$.
    - Now there exists some open subcover $O'$ of $S$.
    - Therefore $p \notin \overline S$. Contradiction!
- $\from$ Suppose $S$ is closed in $M$.
  - This is a special case of the general result for Topological spaces.
  - Alternative proof:
    - $S$ is complete, since $S$ is closed in complete metric space $M$.
    - $S$ is totally bounded, since $S$ is a subset of totally bounded $M$.

##### Product metric space

Suppose $(X_\alpha, d_\alpha)_{\alpha = 1}^n$ are metric spaces. Let $X = \times_\alpha X_\alpha$.

- For $\rho = \infty$, define $d_\infty: X \to [0, \infty)$ as $d_\infty(x, y):=\max_\alpha d_\alpha(x_{\alpha}, y_\alpha)$.
- For $\rho \in [1, \infty)$, define $d_{\rho}: X \to [0, \infty)$ as $d_\rho(x, y) := \|(d_\alpha(x_\alpha, y_\alpha))_{\alpha = 1}^n\|_\rho$.

All the product metrics generates the same topology.

- Notice that $d_\infty(x, y) \le d_\rho(x, y) \le n d_\infty(x, y)$.
  - An open ball in $d_\infty$ with radius $r$ contains an open ball in $d_\rho$ with radius $r / n$.
  - An open ball in $d_\rho$ with radius $r$ contains an open ball in $d_\infty$ with radius $r$.

##### Baire's Theorem

Suppose $(S, d)$ is a complete metric space.

Suppose $\p{U_n}_{n=1}^\infty$ are open and dense sets, $\cap_n U_n$ is dense.

- Consider any $x_0 \in S$ and $r_0 > 0$. We now show that the ball $B(x_0, r_0) \cap \cup_{n} U_n \neq \varnothing$.
- Since $U_1$ is dense, $B(x_0, r_0) \cap U_1$ is open and nonempty.
- So there exists $x_1 \in S$ and $r_1 < 1$, $\overline{B(x_1, r_1)} \subseteq B(x_0, r_0) \cap U_1$.
- Continue the iteration, we have $\overline{B(x_n, r_n)} \subseteq B(x_{n-1}, r_{n-1}) \cap U_n$. Where $r_n < 1/n$.
- The sequence $\p{x_n}$ is clearly Cauchy, therefore $x_n \to x$. $x \in \cap_n U_n$.

