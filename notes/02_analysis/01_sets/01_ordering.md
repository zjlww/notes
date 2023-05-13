#### Ordering

##### Partial ordering

A **partial ordering** on a nonempty set $X$ is a relation $\le$ on $X$ with the following properties:
- (**transitivity**) if $x \le y$ and $y \le z$, then $x \le z$.
- (**antisymmetry**) if $x \le y$ and $y \le x$, then $x=y$.
- (**reflectivity**) $x \le x$ for all $x$.

A partially ordered set is also called a **poset**.

##### Strict partial ordering

A strict partial ordering on $X$ is a relation $<$ on $X$ with the following properties:

- (**transitivity**) if $x<y$ and $y<z$ then $x<z$.
- (**asymmetry**) $x<y$ then never $y<x$.
- (**irreflecivity**) $x < x$ is false.

For example, $\P(X)$ is partially ordered by $\subset$.

##### Linear ordering

A partial ordering $\le$ on $X$ is a **linear / total ordering** if $\forall x, y \in X: x \le y \lor y \le x$.

$X$ is called a linearly / totally ordered set, or a **chain**.

##### Maximal / minimal elements

If $X$ is partially ordered by $\leq$, then:

- $x \in X$ is **maximal** if $\forall y \in X: x \le y \implies x = y$.
- $x \in X$ is **minimal** if $\forall y \in X: y \le x \to y = x$.
- Maximal and minimal elements may not exist.
    - There is no maximal element in $\N$.
- Maximal and minimal elements may not be **unique** in general.
    - Linear ordering guarantees uniqueness.

##### Upper and lower bound

If $X$ is partially ordered by $\leq$. And $E \subseteq X$. Then:
- $x \in X$ is an **upper bound** of $E$ if $\forall y \in E: y \le x$.
- $x \in X$ is a **lower bound** of $E$ if $\forall y \in E: x \le y$.

We have following comments for the upper bound:

- Notice that an upper bound for $E$ need not be an element of $E$.
- And a maximal element of $E$ need not be an upper bound for $E$.

##### Least upper bound and greatest lower bound

If $X$ is partially ordered by $\leq$. And $E \subseteq X$.

$x \in X$ is an least upper bound of $E$ if

- $x$ is an upper bound of $E$.
- Suppose $y$ is another upper bound of $E$, $y \le x$.
- Greatest lower bounds are similarly defined.

The LUB and GLB are unique if they exist, denoted as $\lub E$ and $\glb E$.

- $\lub E$ is also denoted as $\vee E$, or the **join** of $E$.
  - $\vee\c{a, b}$ is usually denoted as $a \lor b$, and called a join operation.
- $\glb E$ is also denoted as $\wedge E$ or the **meet** of $E$.
  - $\land \c{a, b}$ is usually denoted as $a \land b$ and called a meet operation.

##### Least and greatest elements

If $X$ is partially ordered by $\leq$.

- $a \in X$ where $\forall x \in X: x \le a$ is a greatest element of $X$.
- $a \in X$ where $\forall x \in X: x \ge a$ is a least element of $X$.

##### Lattice

Suppose $X$ is a poset.

- $X$ is a **lattice** if for every pair, there is a join and meet.
  - $S$ is called a sub-lattice if $S \subseteq X$, and it is closed under binary join and meet in $X$.
- $X$ is a **complete lattice** if every subset, there is a LUB and GLB.

##### Well ordering

If $X$ is linearly ordered by $\leq$ and every **nonempty** subset of $X$ has a (unique) minimal element, $X$ is said to be **well ordered** by $\leq$.

- The ordering $\leq$ is called a **well ordering** on $X$.
- $\mathbb{N}$ is well ordered by its natural ordering.

#### Axiom of Choice

##### Hausdorff maximal principle ==TODO==

Every partially ordered set by $\le$ has a maximal linearly ordered subset (under $\subseteq$).
- There is a set $E \subseteq X$ that is linearly ordered by $\leq$.
- No subset of $X$ that properly includes $E$ is linearly ordered by $\leq$.

##### Well ordering principle ==TODO==

Every nonempty set $X$ can be well ordered.

##### Zorn's Lemma ==TODO==

If $X$ is a partially ordered set and every chain in $X$ has an upper bound in $X$, then $X$ has a maximal element.

##### The Axiom of Choice

If $\left\{X_{\alpha}\right\}_{\alpha \in A}$ is a nonempty collection of nonempty sets, then $\prod_{\alpha \in A} X_{\alpha}$ is nonempty.

##### The Axiom of Choice II

If $\left\{X_{\alpha}\right\}_{\alpha \in A}$ is a **disjoint** collection of nonempty sets, there is a set $Y \subset \bigcup_{\alpha \in A} X_{\alpha}$ such that $Y \cap X_{\alpha}$ contains precisely one element for each $X_\alpha$.

#### Counting Sets

##### Cardinality

If $X$ and $Y$ are nonempty sets, we define the expressions

- $|X| \le |Y|$ if some $f: X \to Y$ is injective.
- $|X| = |Y|$ if some $f: X \to Y$ is bijective.
- $|X| \ge |Y|$ if some $f: X \to Y$ is surjective.
- $|X| < |Y|$ if $|X| \le |Y|$ but $|X| \neq |Y|$.
- $|X| \le |Y| \iff |Y| \ge |X|$.
- $|X| \le |Y| \lor |Y| \le |X|$.
- (**The Schröder-Bernstein Theorem**)
    - ==TODO== $|X| \le |Y|$ and $|Y| \le |X|$ then $|X| = |Y|$.
- (**Cantor**)
    - ==TODO== $|X|< |\mathcal P (X)|$.
    - This allows us to construct larger and larger sets.

##### Countability

A set $X$ is called **countable** (or **denumerable**) if $|X| \le |\N|$.

- If $X$ and $Y$ are countable, so is $X \times Y$.
- If $A$ is countable and $X_{\alpha}$ is countable for every $\alpha \in A$, then $\cup_{\alpha \in A} X_{\alpha}$ is countable.
- If $X$ is countably infinite, then $\operatorname{card}(X)=\operatorname{card}(\mathbb{N})$.
- $\Z$ and $\Q$ are countable.
- ==TODO== $|\mathcal P(\N)| = |\R|$. 
