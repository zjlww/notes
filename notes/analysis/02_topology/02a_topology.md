#### Topological Spaces

##### Open set axioms

A **topological space** is an ordered pair $(X, G)$, where $X$ is a set and $G$ is the collection of **open sets** of $X$, satisfying the **open set axioms**:

1. The empty set and $X$ itself are open.
2. Unions of open sets (even uncountable) are open.
3. Finite intersections of open sets are open.

##### Intersection of topological spaces

Suppose $(X, G_\alpha)_{\alpha \in A}$ are topological spaces then $(X, \cap_\alpha G_\alpha)$ is a topological space. This immediately follows from the open set axioms.

##### Neighborhood axioms

Suppose $(X, G)$ is a topological space with open set axioms.

Define $N_G: X \to \mathcal \P\P(X)$ as $N_G(x) := \{B \in \P(X): \exists U \in G: x \in U \subseteq B\}$.

- $N_G(x)$ contains all subsets of $X$ that are super-sets of some open set containing $x$.
- Sets in $N_G(x)$ are called **neighborhoods** of $x \in X$.

$N_G$ is called a **neighborhood topology** on $X$. It satisfies the **neighborhood axioms**:

1. $\forall x \in X: N(x) \neq \varnothing$.
2. $\forall x \in X, \forall B \in N(x): x \in B$.
3. Suppose $B_0 \in N(x)$ and $x \in B_0 \subseteq B \subseteq X$, then $B \in N(x)$.
4. Suppose $B_0, B_1 \in N(x)$ then $B_0 \cap B_1 \in N(x)$.
5. Suppose $B \in N(x)$, then there is $B_0 \in N(x)$ such that $B_0 \subseteq B$ and $\forall x_0 \in B_0: B \in N(x_0)$.

##### Closed set axioms

Suppose $(X, G)$ is a topological space with open set axioms.

Define a set $S$ to be **closed** if $X \backslash S \in G$. The closed sets in $\P(X)$ satisfies the following **closed set axioms**:

1. The empty set and $X$ itself are closed.
2. Intersections of closed sets (even uncountable) are closed.
3. Finite union of closed sets is closed.

Here is a very useful result: If $A$ is open and $B$ is closed, then $A-B$ is open and $B-A$ is closed.

##### Neighborhood axioms $\iff$ open set axioms

Suppose $X$ is a set, and $N: X \to \P\P(X)$ satisfies the **neighborhood axioms**.

Define $G_N := \{U \subseteq X: \forall x \in U: U \in N(x)\}$.

- $G_N$ satisfies the open set axioms. So $(X, G_N)$ is a topology space.
- $N_{G_N} = N$ and $G_{N_G} = G$.
	- ==TODO==, $N_{G_N} = N$ is not verified yet, but highly desirable.

##### Covering

$\F$ is a **covering** of $X$ if $X \subseteq \cup \F$.

- If all sets in $\F$ are open, then $F$ is an **open covering**.
- A subset of $\F$ that also covers $X$ is called a **sub-cover** of $\F$.

#### Generated Topology

##### Basis of topology

Suppose $X$ is a set. $\mathcal B \subseteq \P(X)$ is a **basis of a topology** if

1. $\mathcal B$ covers $X$.
2. Any finite intersections of sets in $\mathcal B$ is the union of elements in $\mathcal B$.
   - Equivalently: For all $B_1, B_2 \in \mathcal B$ and $x \in B_1 \cap B_2$, there exists $B_3 \in \mathcal B$ where $x \in B_3 \subseteq B_1 \cap B_2$.

##### Generated topology

Suppose $\mathcal B$ is a basis of a topology on $X$. Define the topology **generated** by $\mathcal B$, as $G_{\mathcal B} := \c{
\cup \F:\F \subseteq \mathcal B}$.

- Then collection $G_\mathcal B$ obeys the open set axioms.
- Therefore $(X, G_\mathcal B)$ is a topological space.
- $G_\mathcal B$ is the **minimum topology** containing $\mathcal B$.

##### Product topological space

Suppose $(X_\alpha, G_\alpha)_{\alpha \in A}$ are topological spaces. Let $X = \times_\alpha X_\alpha$.

Define $\mathcal B$ that contains all sets of the form $\times_{\alpha} U_\alpha$ where $U_\alpha \in G_\alpha$ and for only finitely many $\alpha\in A$,  $U_\alpha \neq X_\alpha$.
- Then $\mathcal B$ is a basis of topology on $X$.
- $(X, G_{\mathcal B})$ is called the **product space**. And $G_\mathcal B$ is the **product topology**.

##### Box topological space

Suppose $(X_\alpha, G_\alpha)_{\alpha \in A}$ are topological spaces. Let $X = \times_\alpha X_\alpha$.

Define $\mathcal E = \{\times_\alpha U_\alpha: U_\alpha \in G_\alpha\}$.
- Then $\E$ is a basis of topology on $X$.
  - $\E$ is closed under finite intersection, and $\E$ covers $X$.
- Let $G_\E$ be the generated topology on $X$.
- $(X, G_\E)$ is called the **box topological space**.

Notice that in general $G_\E \supseteq G_{\mathcal B}$. And when $A$ is finite, $G_{\E} = G_{\mathcal B}$.

