#### Sets

##### Subset

A set $B$ is a subset of a set $A,$ denoted by $B \subseteq A$ or $A \supseteq B,$ if every element of $B$ is in $A$. The notations $B \subset A$ or $A \supset B$ will be used for $B \subseteq A$ but $B \neq A$.

If $A$ is any set, then $A$ is the improper subset of $A .$ Any other subset of $A$ is a proper subset of $A$.

##### Cartesian product

Let $A$ and $B$ be sets. The set $A \times B=\{(a, b) \mid a \in A$ and $b \in B\}$ is the Cartesian product of $A$ and $B$.

- Let $(B_i)_{i = 1}^n$ be sets, finite length cartesian product $\prod_{i=1}^n B_i$ exists.
- Let $H$ be a function with domain $I$, $H(i)  = H_i$.
  - Such a function is also viewed as an indexed family of sets.
- Let $H:= \cup H_i$. Set theory guarantees the existence of
  $$
  X = \prod_{i \in I} H_i = \{f \mid f:I \to H \land \forall i\in I: f(i) \in H_i\}
  $$
  - If some $H(i)$ is empty, the product $\prod H_i$ is $\varnothing$.
  - The **axiom of choice** guarantees that the product is non-empty when all $H_i$ is non-empty.
  - For $x \in X$, $x_\alpha = x(\alpha)$ is the $\alpha$-th **coordinate** of $x$.
  - Define the $\alpha$-th **projection** or **coordinate map** $\pi_{\alpha}: X \rightarrow X_{\alpha}$ by $\pi_{\alpha}(x)=x(\alpha)$.
  - In the particular case where $\forall i \in I: H_i = Y$ we write $\prod_{i \in I} H_i = Y^A$.

##### Number systems

- $\mathbb{Z}$ is the set of all integers (that is, whole numbers: positive, negative, and zero).
- $\mathbb{Q}$ is the set of all rational numbers (that is, numbers that can be expressed as quotients $m / n$ of integers, where $n \neq 0$ ).
- $\mathbb{R}$ is the set of all real numbers. $\overline \R$ is the extended real, $\overline \R  = \R \cup \{\infty, -\infty\}$.
- $\mathbb{Z}^{+}, \mathbb{Q}^{+},$ and $\mathbb{R}^{+}$ are the sets of positive members.
- $\mathbb C$ is the set of all complex numbers.
- $\mathbb{Z}^{*}, \mathbb{Q}^{*}, \mathbb{R}^{*},$ and $\mathbb{C}^{*}$ are the sets of nonzero members.

##### Set algebra

- Power set: $\mathcal P(X)$ is the set of all subsets of $X$.
- Symmetric difference: $A \Delta  B  = (A \backslash B) \cup (B \backslash A)$.
  - $A\Delta C \subseteq A \Delta B \cup B \Delta C$.
- Disjointization identity: $(P \times Q) \backslash (E \times F) = [P\times (Q \backslash F)] \cup [(P\backslash E) \times F]$.
- DeMorgan's laws:
  $$
  \left(\bigcup_{\alpha \in A} E_{\alpha}\right)^{c}=\bigcap_{\alpha \in A} E_{\alpha}^{c}, \quad\left(\bigcap_{\alpha \in A} E_{\alpha}\right)^{c}=\bigcup_{\alpha \in A} E_{\alpha}^{c}
  $$

#### Relations

##### Relation

$R \subseteq A \times B$ is a relation from $A$ to $B$. $\forall a \in A ,\forall b \in B:a R b \iff (a, b )\in R$.

##### Function

A **function** $\phi$ mapping $X$ into $Y$ is a **relation** between $X$ and $Y$ with the property that each $x \in X$ appears as the first member of exactly one ordered pair $(x, y)$ in $\phi$. 

- Such a function is also called a map or mapping of $X$ into $Y$.
- We write $\phi: X \rightarrow Y$ and express $(x, y) \in \phi$ by $\phi(x)=y$.
- The **domain** of $\phi$ is the set $X$ and the set $Y$ is the **codomain** of $\phi$.
- The **range** of $\phi$ is $\phi[X]=\{\phi(x) \mid x \in X\}$.

For a function $f: X \to Y$:

- $f$ is injective if $\forall a,b \in X:f(a) = f(b) \to a = b$.
- $f$ is surjective if $Y = f[X]$.
- $f$ is bijective if $f$ is both injective and surjective.
- If and only if $\phi$ is both injective and surjective, $\phi$ is said to be bijective.

##### Binary operation

$*: S\times S \to S$ is called a binary operation on $S$. 

- For each $(a, b) \in$ $S \times S$, we will denote the element $*(a, b)$ of $S$ by $a * b$.
- $*$ is called **commutative** if $a * b=b * a$ for all $a, b \in S$.
- $*$ is called **associative** if $(a * b) * c=a *(b * c)$ for all $a, b, c \in S$.

##### Image

For function $f: A \to B$, $C \subseteq B$, $D \subseteq A$.

- $f^{-1}[C] = \{a \in A \mid f(a) \in C\}$ is the inverse image of $C$.
- $f[D] = \{b \in B \mid \exists a \in A :f(a) = b\}$ is the image of $D$.
- $f^{-1}[\{b\}]$ is called the fiber of $f$ over $b \in B$.

##### Inverse function

Suppose $f: A \to B$. Then:
- $f$ has a **left inverse** if there is a function $g: B \rightarrow A$ such that $g \circ f: A \rightarrow A$ is the identity map.
- $f$ has a **right inverse** if there is a function $h: B \rightarrow A$ such that $f \circ h: B \rightarrow B$ is the identity map.
- The map $f$ is **injective** if and only if $f$ has a left inverse.
- The map $f$ is **surjective** if and only if $f$ has a right inverse.
- The map $f$ is a **bijection** if and only if $f$ is injective and surjective.

Define the inverse map $f^{-1}: \P(B) \to \P(A)$ as $f^{-1}[D]=\{a \in A: f(a) \in D\}$.

- When $f$ is a bijection, $f^{-1}$ can also denote $f^{-1}(y) = \operatorname{elem}{f^{-1}\{y\}}$. And it is called the inverse function.

##### Restriction / extension of function

- If $A \subseteq B$ and $f: B \rightarrow C$, we denote the **restriction** of $f$ to $A$ by $\left.f\right|_{A}$. If the context is clear, we can denote $f|_A$ as $f$.
- If $A \subseteq B$ and $g: A \rightarrow C$ and there is a function $f: B \rightarrow C$ such that $\left.f\right|_{A}=g$, we shall say $f$ is an **extension** of $g$ to $B$.

##### Equivalence and partition

Suppose $S$ is a nonempty set.

$P \subset \mathcal P(S)$ is a **partition** of $S$ if $P$ is disjoint and $\cup P = S$.

- Elements of $P$ are called blocks / cells.
- Denote $\bar{x}$, $[x]$ as the block containing the element $x$ of $S$.

$R \subseteq S \times S$ is an **equivalence relation** on $S$ if it is

- (**reflexive**) $\forall a \in S: (a, a) \in R$.
- (**symmetric**) $\forall a, b \in S: (a, b) \in R \to (b, a) \in R$.
- (**transitive**) $\forall a, b, c \in S: (a, b) \in R \land (b, c) \in R \to (a, c) \in R$.

There is a bijection from all partitions to all equivalence relations on $S$.

- Define $f: P \mapsto \{(a, b) \in S \times S \mid \exists B \in P, a \in B \land b \in B\}$.
- Define $u: a \mapsto \{x \in S\mid a R x \}$, and $g: R \mapsto \{u(a) \mid a \in R\}$.
- We can show that $g \circ f$ is the identity, and $f \circ g$ is the identity.

##### Inverse images of sets

Consider mapping $f: X \to Y$. $f^{-1}: \mathcal{P}(Y) \rightarrow \mathcal{P}(X)$ has following properties:

- $f^{-1}\left(\bigcup_{\alpha \in A} E_{\alpha}\right)=\bigcup_{\alpha \in A} f^{-1}\left(E_{\alpha}\right)$.
- $f^{-1}\left(\bigcap_{\alpha \in A} E_{\alpha}\right)=\bigcap_{\alpha \in A} f^{-1}\left(E_{\alpha}\right)$
- $f^{-1}\left(E^{c}\right)=\left(f^{-1}(E)\right)^{c}$.
- $f^{-1}(A - B) = f^{-1}(A \cap B^c) = f^{-1}(A) - f^{-1}(B)$.
