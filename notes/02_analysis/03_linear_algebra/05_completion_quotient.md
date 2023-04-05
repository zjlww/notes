#### Completion of Normed Spaces

Suppose $\bF = \R$ or $\C$.

##### Extending codomain to closure

Suppose $X$ is a normed space over $\bF$. And $Y$ is a Banach space.

Suppose $X_0 \subset X$ is a dense subspace. And $T_0 \in \mathcal B(X_0, Y)$.

There exists a **unique** $T \in \mathcal B(X, Y)$ that extends $T_0 \in \mathcal B(X_0, Y)$ where $\n T = \n{T_0}$.

- Suppose $x \in X$, $T(x)$ is defined as following:
  - There exists $(x_n)_{n = 1}^\infty \in X_0$ where $x_n \to x$.
  - $(x_n)$ is Cauchy, so $(T_0 x_n) \in Y$ is Cauchy.
  - Since $Y$ is a **Banach** space, $T_0x_n$ converges to some $y \in Y$.
  - Now define $T(x):= y$
- Above $T: X \to Y$ is well defined.
  - For any other seqeuence $(x'_n) \in X_0$ such that $x'_n \to x$.
  - $\norm{x_n - x'_n} \to 0$ implies $\norm{T_0x_n - T_0x'_n} \to 0$.
- The defined $T$ extends $T_0$.
  - Since for $x_0 \in X_0$, we can take $x_n = x_0$.
- The defined $T$ is a linear map.
  - Suppose $a, b \in X$. There exists $(a_n), (b_n) \in X_0$ such that $a_n \to a$, $b_n \to b$.
  - $\norm{(a + b) - (a_n + b_n)} \le \norm{a - a_n} + \norm{b - b_n} \to 0$. So $(a_n + b_n) \to a + b$.
  - $T(a + b) = \lim_n T_0(a_n + b_n) = T(a) + T(b)$.
  - Similarly $T(c x) = cT(x)$.
- $T \in \mathcal B(X, Y)$. And $\norm{T} = \norm{T_0}$.
  - $\norm{T} \ge \norm{T_0}$ since $T|_{X_0} = T_0$.
  - $\norm{T} \le \norm{T_0}$.
    - Suppose $x \in X$ and $x_n \to x$ with $\p{x_n} \subseteq X_0$.
      $$
      \n{Tx} = \n{T(x_n + x - x_n)} = \n{T_0x_n} + \n{T_0 x_n - Tx} \le \n{T_0} \n{x_n} + \epsilon
      $$
    - Now take limits on both sides.

If $T_0$ is an embedding then $T$ is an embedding.

- $\exists c > 0, \forall x \in X_0: \norm{T_0 x} \ge c \|x\|$.
- Suppose $x \in X$ and $x_n \to x$. $\norm{Tx} + \norm{T_0 x_n - Tx} \ge \norm{T_0 x_n} \ge c\norm{x_n}$.
- Take limit $n \to \infty$. $\norm{Tx} \ge c\|x\|$.

If $T_0$ is an isometry, then $T$ is an isometry.

- Take $c = 1$ in above proof. Then $\norm{Tx} \ge \|x\|$.
- Also $\norm{Tx} \le \norm{T_0}\|x\| = \|x\|$. So $\norm{Tx} = \|x\|$.

##### Completion of normed spaces

Suppose $X$ is a normed space. A **completion** of $X$ is a pair $(\widetilde X, J)$:

- $\widetilde X$ is a Banach space.
- $J \in \L(X, \widetilde X)$ is an **isometric embedding**. Where $J[X]$ is dense in $\widetilde X$.
- Wit the embedding $J$, we can identify $X$ with $J[X]$.

##### Existence of Norm space completion

Suppose $X$ is a **normed space** over $\bF$. $X$ has a completion $(\widetilde X, J)$.

- Let $(\widetilde X, \widetilde d, J)$ be a **completion of the metric space** $(X, d)$.
  - $(\widetilde X, \widetilde d)$ is a complete metric space.
  - We identify elements in $X$ with those in $\widetilde X$.
- Define addition and scalar multiplication on $\widetilde X$ as following:
  - Let $x, y \in \widetilde X$, suppose $x = [(x_n)_{n = 1}^\infty], y = [(y_n)_{n = 1}^\infty]$, for $\p{x_n}, \p{y_n} \subseteq X$.
    - $(x_n)$ and $(y_n)$ are Cauchy, both in $(X, d)$ and $(\widetilde X, \widetilde d)$.
  - Define $x + y := [(x_n + y_n)_{n=1}^\infty]$.
    - $(x_n + y_n)$ is Cauchy, so $(x + y) \in \widetilde X$.
    - Clearly the addition is well defined.
  - For $\alpha \in \symbf F$, define $\alpha x := [(\alpha x_n)]$.
    - Clearly the scalar-multiplication is well defined.
- Define the norm on $\widetilde X$ as $x \mapsto \widetilde d(x, 0)$.
- The operations and norm **extends** original operations on $X$.
- The defined $(\widetilde X, + ,\cdot)$ is a normed vector space over $\bF$.
  - Just verify the axioms of vector spaces.
- $J$ is an isometric homeomorphism.

##### Completion of bounded linear maps

Suppose $X$ is a normed space, and $Y$ is a Banach space over $\bF$.

- There exists a completion $(\widetilde X, J)$ of the normed space $X$.

Suppose $T \in \mathcal B(X, Y)$.

- There exists a **unique** $\widetilde T \in \mathcal B(\widetilde X, Y)$ extending $T$, and further $\|{\widetilde T}\| = \norm{T}$.
- $T$ is an embedding / isometry iff $\widetilde T$ is an embedding / isometry.

The map $\varphi: \mathcal B(\widetilde X, Y) \to \mathcal B(X, Y)$ defined by $\widetilde T \mapsto \widetilde T \circ J = T$.

- $\varphi$ is bijective. Since completion of $T$ is unique.
- $\varphi$ is an isometric homeomorphism.

##### Uniqueness of norm space completion

All completions of a norm space are the same up to **isometric homeomorphisms**.

Suppose $X$ is a normed space with completion $(X_1, J_1)$ and $(X_2, J_2)$.

- There is a unique isometry $I_{12} \in \mathcal B(X_1, X_2)$ extending $J_2 \in \mathcal B(X, X_2)$.
- There is a unique isometry $I_{21} \in \mathcal B(X_2, X_1)$ extending $J_1 \in \mathcal B(X, X_1)$.
- There is a unique isometry $I_{11} \in \mathcal B(X_1, X_1)$ extending $J_1 \in \mathcal B(X, X_1)$.
- There is a unique isometry $I_{22} \in \mathcal B(X_2, X_2)$ extending $J_2 \in \mathcal B(X, X_2)$.
- $I_{11}$ and $I_{22}$ are identities on $X_1$ and $X_2$.

Consider the map $I_{21}\circ I_{12} \in \mathcal B(X_1, X_1)$ 

- It extends $J_1 \in \mathcal B(X, X_1)$.
  - For any $x \in X$, $I_{21}\circ I_{12}(x) = I_{21}(J_2(x)) = J_1(x)$.
- By uniqueness of extension $I_{21}\circ I_{12} = I_{11}$. Similarly $I_{12}\circ I_{21} = I_{22}$.

$I_{12}$ and $I_{21}$ are **isometric homeomorphisms**!

#### Quotient Normed Spaces

> We have already seen quotient vector spaces, these are the new results for normed spaces:
>
> - Consider $X / X_0$. The quotient norm is generally a semi-norm. And only when $X_0$ is closed, it is a true norm.
> - The map $Q: x \mapsto x + X_0$ is a coisometry when $X_0$ is closed.
>
> We have already seen quotient linear maps, these are the new results:
>
> - Suppose $T \in \mathcal B(X, Y)$ and $X_0 \subseteq \null T$ is closed.
> - $T_{X_0} \in \mathcal B(X/X_0, Y)$ and $\norm{T_{X_0}} = \norm{T}$.

##### Quotient normed space

Suppose $X$ is a normed space and $X_0$ is a subspace.

Then $X / X_0$ is a vector space. Consider $Q \in \L(X, X / X_0)$ where $Q: x \mapsto x + X_0$.

Define the **quotient norm** as
$$
\norm{x + X_0} := \inf\{\norm{x - y}: y \in X_0\} = \operatorname{dist}(x, X_0)
$$

- $\n{\cdot}$ is a **seminorm** on $X / X_0$.
  - Clearly $\norm{x + X_0} \ge 0$ and $\norm{0 + X_0} = 0$.
  - $\norm{\alpha x + X_0} = \alpha\norm{x + X_0}$.
  - Triangle inequality is true.
    - Hint: let $(x_n)_{n = 1}^\infty \in X_0$ such that $\norm{x - x_n} \to \norm{x + X_0}$.
- The following are equivalent:
  1. $X_0$ is a **closed** subspace of $X$.
  2. $\forall x\notin X_0: \operatorname{dist}(x, X_0) > 0$.
  3. $\forall x \notin X_0: \norm{x + X_0} > 0$.
  4. $\n{\cdot}$ is a norm on $X / X_0$.

Suppose $X_0$ is a **closed** subspace. Then $Q$ is a **coisometry**.

- $\norm{Q} \le 1$ since $\|x\| = \inf\{\norm{x + y}: y \in \{0\}\} \ge \norm{x + X_0}$.
- So $QB_X(0; 1) \subseteq B_{X/X_0}(0; 1)$.
- Suppose $x + X_0 \in B_{X / X_0}(0; 1)$, for some $y \in X_0$, $\norm{x + y} < 1$.
- So $QB_X(0; 1) \supseteq B_{X/X_0}(0; 1)$.

##### Quotient bounded linear maps

Suppose $X, Y$ are nonzero normed space over $\bF$. And $T \in \mathcal B(X, Y)$.

- Suppose $X_0 \subseteq \null T$ is a **closed subspace** of $X$. ($\null T$ is also closed.)
- Define $Q_{X_0}(x) = x + X_0$. $Q_{X_0}$ is a **coisometry** by (**Quotient normed space**).
- By (**Quotient linear maps**), $T_{X_0} \in \L(X/X_0, Y)$ **uniquely exists** such that  $T_{X_0} \circ Q_{X_0} = T$.

In this case, we have the following properties:

- Since $T_{X_0}[B_{X/X_0}(0; 1)] = T[B_X(0; 1)]$, $(*)$.
  - $T_{X_0} \in \mathcal B(X/X_0, Y)$ and $\norm{T_{X_0}} = \norm{T}$.
    - Suppose $Y \neq \{0\}$, then $\norm{T / X_0} = \norm{T}$.
  - $T_{X_0}$ is open iff $T$ is open.
  - $T_{X_0}$ is coisometry iff $T$ is coisometry.

Consider space $V = \c{T \in \mathcal B(X, Y): X_0 \subseteq \null T}$. $V$ is a vector space over $\bF$.

- Consider the map $T \mapsto T_{X_0}$, this is an isometric homeomorphism from $V$ to $\mathcal B(X / X_0, Y)$.

##### Corollary: double quotient of bounded linear maps

Suppose $X, Y$ are normed spaces with $X_0, Y_0$ being subspaces.

Suppose $T \in \mathcal B(X, Y)$ where $T[X_0] \subseteq Y_0$. Then there **exists a unique** $\widehat T\in \mathcal B(X / X_0, Y / Y_0)$  such that $\widehat T \circ Q_{X_0} = Q_{Y_0} \circ T$. Further $\n{\widehat T} = \n{Q_{Y_0}\circ T} \le \n{T}$.

- Apply (**Quotient bounded linear maps**) to $Q_{Y_0}\circ T$, demonstrates the existence and uniqueness.
- $\n{Q_{Y_0}\circ T} \le \n{T}$ by definition.

##### Corollary: fundamental theorem of bounded linear homomorphisms

Suppose $X, Y$ are normed spaces over $\bF$. And $T \in \mathcal B(X, Y)$.

- By (**Fundamental theorem of linear homomorphisms**) $\widetilde T = T_{\null T}$ is the unique **isomorphism** such that $\widetilde T \circ Q_{\null T} = T$.

We extend above theorem in following ways:

- $\widetilde T$ is a topological isomorphism if and only if $T$ is open.
  - Since $\widetilde T$ is open **iff** $T$ is open. So $\widetilde T^{-1}$ is continuous **iff** $\widetilde T$ is top. iso. **iff** $T$ is open.
- $\widetilde T$ is an isometric isomorphism if and only if $T$ is an coisometry.
  - $T$ is a coisometry iff $\widetilde T$ is a coisometry iff $\widetilde T$ is an isometry by (**Coisometry**).

##### Completeness of quotient normed spaces

Suppose $X$ is a Banach space. $X_0 \subseteq X$ is a closed subspace. Then $X / X_0$ is a Banach space.

- Suppose $(u_n)_{n = 1}^\infty \in X / X_0$ and $\sum_n \norm{u_n} < \infty$.
- Pick $(x_n)_{n = 1}^\infty \in X$ such that $\norm{x_n} \le \norm{u_n} + 1/2^n$. So $(x_n)$ is absolutely convergent.
- Suppose $\sum_n x_n = x \in X$. Then $Q(x) = Q(\sum_n x_n) = \sum_n u_n$ as $Q$ is continuous.
- So absolutely convergent series in $X / X_0$ are convergent.
