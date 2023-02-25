#### Connected Topological Spaces

> See this [wiki article on connected space](https://en.wikipedia.org/wiki/Connected_space).
>

##### Connected spaces

Consider topological space $X$.

**The following are equivalent definitions of $X$ being connected:**

1. $X$ is not the union of two disjoint nonempty open sets.
2. Only $\c{\varnothing, X}$ are both open and closed in $\P\p{X}$.
3. All continuous functions in $X \to \c{0, 1}$ are constant.
   - The space $\c{0, 1}$ has the discrete topology.
   - The open sets are $\c{\c{0}, \c{1}, \c{0, 1}, \varnothing}$.
   - We call such functions binary functions in these notes.

A subset $S \subseteq X$ is called connected if it is a connected subspace.

##### Closures of connected sets

Suppose $X$ is a topological space. Suppose $E$ is connected. Then $\overline E$ is also connected.

- Suppose $\overline E$ is not connected. Let $\overline E = A \cup B$ where $A, B$ are nonempty disjoint open sets in subspace $\overline E$.
- $E = \p{A \cap E} \cup \p{B \cap E}$. Notice that $\p{A \cap E}, \p{B \cap E}$ are disjoint and open in subspace $E$.
- So w.l.o.g. assume $E = A \cap E$. Therefore $A \supseteq E$.
- So $B = \overline E - A \subseteq \overline E - E$.
- Suppose $e \in B$. Take $N$ as a neighborhood of $e$ inside $B$. $N$ must contain points of $E$. Therefore $B$ contains points of $E$.
- This is a contradiction.

##### Connected components

Suppose $X$ is a topological space.

The union of overlapping connected sets is connected.

- Suppose $x \in X$ and $\p{U_\alpha}_{\alpha \in I}$ are connected. Suppose $x \in \cap_\alpha U_\alpha$.
- Consider the set $U = \cup_\alpha U_\alpha$.
- Clearly all functions in $C\p{U \to \c{0, 1}}$ are constants.

$x, y \in X$ are **connected**, if there is a connected $T \subseteq X$ where $x, y \in T$.

Denoted by $x \leftrightarrow y$ if $x, y$ are connected.

- $\leftrightarrow$ is an equivalence relationship.
- The equivalence classes of $\leftrightarrow$ are called **connected components** of $X$.
- Connected components are closed in $X$.
  - Suppose $E$ is a connected component.
  - $\overline E$ is also connected. Therefore $E \supseteq \overline E$. So $E$ is closed.
- Suppose there are only finitely many connected components. They are all open in $X$.
  - Each connected component is the complement of the union of other components.
- $X$ is **connected** if there is only one connected component.

##### Connectedness under continuous maps

Suppose $X, Y$ are topological spaces. Suppose $f: X \to Y$ is a function continuous on $X$.

If $X$ is connected, $f[X]$ is connected.

- Suppose $f[X]$ is not connected. There exists a continuous binary function $g: f[X] \to \c{0, 1}$ that is not constant.
- $g \circ f: X \to \c{0, 1}$ is a non-constant continuous binary function.
- So $X$ is not connected.

##### Path-connected spaces

Suppose $X$ is a topological space.

A **continuous** function $\gamma: [a, b] \to X$ with $f(a) = x$ and $f(b) = y$ is called a **path from $x$ to $y$**. $f[a, b]$ is the graph of the path.

- When $\gamma$ is made of **countably** many line segments, it is called a **polygonal path**.

Denote $x \leftrightarrow_p y$ if there is a path between them.

- $\leftrightarrow_p$ is an equivalence relationship.
- The equivalence classes of $\leftrightarrow_p$ are called **path-components**.
- $X$ is **path-connected** if there is one and only one path-component.
- $x \leftrightarrow_p y \implies x \leftrightarrow y$.
- The path $\gamma$ is called **rectifiable** (see variations) if it has finite arc length by inscribing polygon.
  - $\gamma$ is rectifiable if, and only if, $\gamma$ is of bounded variation on $[a, b]$.
- The path $\gamma$ is called **smooth** $\gamma \in C^1[a, b]$, and $\gamma' \neq 0$.
- The path $\gamma$ is called **piecewise smooth**, if it is continuous on $[a, a_1], [a_1, a_2], \ldots, [a_n, b]$.
  - Every **piecewise smooth path is rectifiable** and its arc length is given by the integral $\int_{a}^{b}\left|\gamma^{\prime}(t)\right| d t$.
- The path $\gamma$ is called a **circuit** if it is piecewise smooth and closed.
- The path $\gamma$ is called **simple** if $\gamma$ is injective.
- The path $\gamma$ is called **closed** if $\gamma(a) = \gamma(b)$.

The image of a path is called a **curve**.

Path $\alpha: [a, b] \to \C$ and $\beta: [c, d] \to \C$ are **equivalent** if there exists a $u: [a, b] \to [c, d]$ continuous and strictly monotonic, and $\beta \circ u = \alpha$.

##### Connectedness in $\R^n$

Open connected sets in $\R^n$ are path-connected.

There exists a polygonal path with **finite segments** between any two points.

- Consider $x \in S$.
- Let $A \subseteq S$ contain all finitely polygonal connected points with $x \in S$.
  - $A$ is clearly nonempty.
  - $A$ is open. Suppose $y \in A$, then $B_S(y; r) \subseteq A$.
- Suppose $B = S - A$ is not empty.
- $B$ is also open. Suppose $y \in B$, then $B_S(y; r) \in B$ is a must.
- Therefore $S = A \cup B$, contradiction!
- Suppose $S \subseteq \R^n$ is open.
  - Connected components of $S$ are open.
  - The connected partition of $S$ is a open covering of $S$. Therefore countable.

$S \subseteq \R^n$ (also $\C^n$) is a region, if $S$ contains an open connected set $A$ in $\R^n$ with some of $\part A$ in $\R^n$.

- If $S$ is open, $S$ does not contain any of $\part A$. $S$ is called an open region or a domain.
- If $S$ is closed, $S$ contains all of $\part A$. $S$ is called a closed region.
