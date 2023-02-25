#### Special Point-sets

##### Special points and sets

Suppose $(X, G)$ is a topological space. And $S \subseteq X$.

- $x \in S$ is an **interior point** of $S$ in $X$,
  - iff $x \in O$ for some $O \in G$ and $O \subseteq S$;
  - iff $S \in N_G(x)$;
- $S^\circ$ is the **interior** of $S$ in $X$,
  - iff $S^\circ$ is the set of all interior points of $S$,
  - iff $S^\circ$ is the union of all open sets of $X$ that is a subset of $S$;
  - iff $S^\circ$ is the largest open subset of $X$ that is a subset of $S$;
- $x \in X$ is an **adherent point** of $S$ in $X$,
  - iff every neighborhood of $x$ contains a point of $S$.
- $\overline S$ is the **closure** $S$ in $X$,
  - iff $\overline S$ is the set of all adherent points of $S$ in $X$;
  - iff $\overline S$ is the intersection of all closed set $F \supseteq S$;
  - iff $\overline S$ is the smallest closed subset of $X$ that contains $S$.
  - $\overline S$ is closed in $X$.
- $x \in X$ is an **accumulation** point of $S$ in $X$,
  - iff every neighborhood of $x$ contains a point of $S- \c x$.
  - If $x$ is an accumulation point of $S$, it is an adherent point of $S$.
- $S'$ is the **derived set** of $S$ in $X$,
  - iff $S'$ is the set of all accumulation points of $S$ in $X$.
- $S$ is **closed** in $X$,
  - iff $S$ contains all its adherent points in $X$;
  - iff $S$ contains all its accumulation points in $X$;
  - iff $S$ equals to its closure in $X$;
- $x \in X$ is an **isolated point** of $S$ in $X$ iff $x \in S - S'$.
- $x\in X$ is an **boundary point** of $S$ in $X$ iff $x \in \overline S \cap \overline{S^c}$.
- $\part S = \overline S - S^\circ$ is the **boundary** of $S$ in $X$.
  - $\part S$ is closed in $X$.


##### Disjoint sets

Suppose $(X, G)$ is a topological space. And $A, A_k, B$ are subsets of $X$.

- If $A^\circ \cap B^\circ = \varnothing$, $A$ and $B$ are almost disjoint.
- If $A \cap B = \varnothing$, $A$ and $B$ are disjoint sets.

##### Topological subspace

Suppose $(X, G)$ is a topological space. And $Y \subseteq X$.

The following are **equivalent** and gives a **topological subspace** $Y$.

- Modify the **neighborhood topology** $N'(y) = \{B \cap Y \mid B \in N(y)\}$.
- Modify the **set of open sets** $G'= \{U \cap Y \mid U \in G\}$.

Consider the topological subspace $(Y, G')$. Suppose $S \subseteq Y$.

- $S$ is open in $Y$ iff $S = A \cap Y$ for some open set $A$ in $X$.
- $S$ is closed in $Y$ iff $S = A \cap Y$ for some closed set $A$ in $X$.

##### Dense sets

Suppose $X$ is a topological space. And $E \subseteq X$.

- When $\overline E = X$, $E$ is called **dense** in $X$.
  - $E$ is dense if and only if every nonempty open subset of $X$ contains a element of $E$.
  - $E$ is dense if and only if $X \backslash E$ has no interior points.
- When $(\overline E)^\circ = \varnothing$ in $E$, $E$ is called **nowhere dense** in $X$.
- When $\overline E$ has no interior points, $E$ is called **nowhere dense**.

#### Topological Properties

##### Separable

Topological space $X$ is **separable** if it has a countable dense subset.

##### First-countable

A topological space $X$ is **first-countable** if for any $x \in X$ there exists a sequence $N_1, N_2, \ldots \in N(x)$ such that for any $O \in N(x)$ there is an $N_k$ contained in $O$.

Without loss of generality, we can require the sequence to contain only open neighbors.

##### Second-countable

A topological space $X$ is **second-countable** if there exists some countable collection $U =\left\{U_{i}\right\}_{i=1}^{\infty}$ of open subsets of $X$ such that any open subset of $X$ can be written as a union of elements of some subfamily of $U$.

- Suppose $X$ has a metric, then separable is equivalent to second-countable.
- The Euclidean spaces are second-countable. 

##### Hausdorff space

Suppose $X$ is a topological space.

If for all $x, y \in X$ where $x \neq y$, there exists $U \in N(x)$ and $V \in N(y)$, where $U \cap V = \varnothing$. $X$ is called **Hausdorff**.

##### Compactness of topological spaces

Suppose $X$ is a topological space with open sets topology $G$.

The space $X$ is called **compact** if all of its open covers have a finite subcover.

Consider subset $K \subseteq X$. $K$ is called **compact**, if the subspace $(K, G|_K)$ is compact.

##### Compact subspaces

Suppose $X$ is a compact topological space.

**Suppose $F$ is closed in $X$, then $F$ is a compact subspace.**

- Suppose $\p{G_\alpha}_{\alpha \in I}$ is an open cover of $F$ in $F$.
- Consider $\p{G_\alpha \cup \p{X - F}}$, which is an open cover of $X$.
- Therefore there is a finite open subcover.

Suppose $X$ is **Hausdorff**. **Suppose $F$ is a compact subspace of $X$. Then $F$ is closed in $X$.**

- Suppose $F$ is not closed in $X$, and $p \in \overline F - F$.
- Since $X$ is Hausdorff, there exists open neighborhoods $O_x \in N(x)$ and $P_x \in N(p)$. Such that $O_x \cap P_x = \varnothing$.
- Consider the open covering $O:=\c{O_x: x \in F}$.
- Now there exists some open subcover $O'$ of $F$.
- Therefore $p \notin \overline F$. Contradiction!
