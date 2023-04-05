#### Basis

Suppose $V$ is a vector space over $\bF$.

##### Lists

$(v_{i})_{i = 1}^n \subseteq V$ is a finite list. Similarly we can define infinite list.

- The set $\{v_i\}_{i = 1}^n$ is called the **range** of the list.

##### Linear combination

A linear combination of a list $(v_i)_{i = 1}^m \subseteq V$ is of the form $a_{1} v_{1}+\cdots+a_{m} v_{m}$ where $a_{1}, \ldots, a_{m} \in \symbf{F}$.
- Linear combinations of the empty list $()$ is $\c{0}$.
- When all $a_k = 0$, or the list is empty, the linear combination is **trivial**.

##### Spanned subspace

Suppose $E \subseteq V$. $\span E$ is the set of all linear combinations of finite lists in $E$.

- $E$ spans $V$ if $\span E = V$.
- $\span E$ is the smallest subspace of $V$ containing $E$.
- $V$ is finite-dimensional if $|E| < \infty$ and $\span E = V$.

##### Linearly independent

Suppose $E \subseteq V$. $E$ is **linearly independent** if $0$ is **not** a nontrivial linear combination of any finite subsets of $E$.

- The empty list $()$ is linearly independent.
- A list of vectors in $V$ is called **linearly dependent** if it is not linearly independent.

##### Linear dependence lemma

Suppose $S = (v_{1}, \ldots, v_{m})$ is a **linearly dependent** list in $V .$ Then there exists $j \in\{1,2, \ldots, m\}$ such that $v_{j} \in \span(v_1, \cdots, v_{j-1})$, and removing $v_j$ does not change the span of the list.

##### Linearly independent list & spanning set

In a finite-dimensional vector space, the length of every linearly independent list of vectors is less than or equal to the length of every spanning list of vectors.

##### Hamel basis

A **Hamel basis** of $V$ is a subset of $V$ that is linearly independent and spans $V$.

- Every countable spanning list in $V$ can be reduced to a basis.
- Decomposition of any $v \in V$ against a basis is **unique**.

##### Existence of Hamel basis

Every vector space has a Hamel basis. Every linearly independent set can be extended to a Hamel basis.

- Suppose $V$ is a vector space. Then $E \subseteq V$ is a basis of $V$ if and only if it is a **maximal element** in the following sense.
- Consider $P \subseteq \P(V)$, the set of all linearly independent subsets of $V$. Define partial order by subset relationship.
- $E \in P$ is maximal in $P$ if no other set in $P$ properly contains $E$.
- For any chain $C$ in $P$, $\bigcup C \in P$ and is an upper bound of $C$. So there must be an maximal element in $P$, this is a basis of $V$.
- Suppose $F \in P$ is not a basis but linearly independent. We can extend it to a basis of $V$.

##### Standard basis

For $V = \bF^n$ we have the standard basis $(e_1, \cdots, e_n)$. Where $e_j = (0, \cdots, 0, 1, 0, \cdots, 0)$.

##### Dimension

Suppose $V$ is a **finite-dimensional** vector space. Any two finite bases of $V$ have the same length. Defined as the dimension of $V$, $\dim V$.
- Every linearly independent list of vectors in $V$ with length $\operatorname{dim} V$ is a basis of $V$.
- If $U_{1}$ and $U_{2}$ are subspaces of a finite-dimensional vector space, then $$\operatorname{dim}\left(U_{1}+U_{2}\right)=\operatorname{dim} U_{1}+\operatorname{dim} U_{2}-\operatorname{dim}\left(U_{1} \cap U_{2}\right)$$
- If $V$ is finite-dimensional and $U$ is a subspace of $V,$ then $\operatorname{dim} U \leq \operatorname{dim} V$.

##### Subspace decomposition

Suppose $U$ is a subspace of $V$. Then there is a subspace $W$ of $V$ such that $V=U \oplus W$.
- First construct a basis of $U$, then extend the basis to $V$.
- Define $W$ as the spanned space from the extra base vectors.

##### Dimension bound of sum

Suppose $V$ is finite-dimensional. And $U_{1}, \ldots, U_{m}$ are subspaces.

- $U_{1}+\cdots+U_{m}$ is finite-dimensional, $\dim(U_{1}+\cdots+U_{m}) \le \dim U_{1}+\cdots +\dim U_{m}$.
- $U_{1} \oplus \cdots \oplus U_{m}$ is finite dimensional, $\dim (U_{1} \oplus \cdots \oplus U_{m})=\dim U_{1}+\cdots+\dim U_{m}$.
