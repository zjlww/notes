#### Normed Spaces

Assume $\bF = \R, \C$ in this chapter.

##### Norm

A **norm on a vector space** $U$ over $\mathbf F$ is a function $\|\cdot\| \in U \rightarrow[0, \infty)$ such that 

1. $\|u\|=0$ if and only if $u=0$.
2. $\|\alpha u\|=|\alpha|\|u\|$ for all $\alpha \in \mathbf{F}$ and all $u \in U$.
3. $\|u+v\| \leq\|u\|+\|v\|$ for all $u, v \in U$.
    - This implies $\abs{\n u - \n v}\le \n{u - v}$.

##### Seminorm

Remove condition $(1)$ in Norm then $\|\cdot\|$  is called a **seminorm**. Suppose $\|\cdot\|$ is a seminorm on $U$, then:

- Let $N = \{\|x\| = 0: x \in U\}$ then $N$ is a subspace.
- Define $\|[x]\|$ as $\|x\|$ for $[x] \in U / N$.
- Then $U / N$ is a quotient vector space with norm $\|x + N\|:= \|x\|$.

##### Norm and metric

Suppose $U$ is a normed vector space. Its norm induces metric by $d(x, y) = \|x - y\|$ on $U$.
- The norm $\|\cdot\|: U \to [0, \infty)$ is continuous under the metric.

Suppose $U$ is a metric space. The metric induces norm by $\|x\| = d(x, 0)$ on $U$.

##### Infinite Triangle Inequality

Suppose $V$ is a normed space. Suppose $(a_n) \subseteq V$, and $\sum a_n$ is absolutely convergent.

Then $\n{\sum_{n=1}^\infty a_n} \le \sum_{n=1}^\infty \n{a_n}$.

- $\n{\sum_{n=1}^m a_n} \le \sum_{n=1}^m \n{a_n} \le \sum_{n=1}^\infty \n{a_n}$ following from the triangle inequality.
- Now take $n \to \infty$ on both sides. Notice that the norm function is continuous.

#### Banach Spaces

Assume $\bF = \R, \C$ in this chapter.

##### Banach Space

Normed vector space $U$ is a **Banach space** if $U$ is complete.

##### Absolute convergence test

Normed vector space $U$ is a Banach space iff all **absolutely convergent** series in $U$ **converge**.

- Suppose $(g_k)_{k = 1}^\infty \in U$ is absolutely convergent, that is $\sum_{k=1}^\infty \|g_k\| < \infty$.
- $\to$ direction: Let $f_k = \sum_{n = 1}^k g_k$. $\sum_{k = 1}^\infty \|g_k\| < \infty$ implies $f_k$ is Cauchy. So $f_k$ converges if $U$ is Banach.
- $\leftarrow$ direction:
    - Suppose $(f_n)_{n =1}^\infty \in U$ is Cauchy. To show it converges, we only need to show a subsequence converges.
    - It is clearly possible to construct $(f_{n_k})$ where $\sum_{k = 1}^\infty \|f_{n_k} - f_{n_{k - 1}}\| < \infty$.
    - Then $\sum_{k=1}^m (f_{n_k} - f_{n_{k-1}}) = f_{n_m} \to v \in U$, by assumptions.
    - So $f_n \to v$ in $U$. And $U$ is complete.

##### All finite dimensional spaces are Banach

**Finite dimensional** normed vector spaces over $\bF$ are **Banach** spaces.

- Use the **absolute convergence test** to prove this. Suppose $(f_n) \in U$ is absolutely converging.
- Consider each dimension separately. Since $\bF$ is complete, each coordinate component converges.
- Therefore $\sum f_n$ converges in $U$. And $U$ is Banach.

##### Closure of subspaces

Suppose $V$ is a normed vector space over $\bF$.

The closure of subspace $U$ of $V$ denoted by $\overline U$ is a subspace of $V$.
- Consider $x, y \in \overline U$ and $x_n \to x$, $y_n \to y$ for $(x_n), (y_n) \in U$.
    - $(x_n + y_n) \to x + y$. So $x + y \in \overline U$.
    - $cx_n \to cx$ for $c \in \bF$. So $cx \in \overline U$.

#### Continuous Linear Maps

Assume $\bF = \R, \C$ in this chapter.

##### Norm of linear maps

Suppose $V$ and $W$ are **seminormed vector spaces** over $\bF$.

The norm of $T \in \L(V, W)$ is defined as
$$
\begin{aligned}
\norm{T} :=& \inf \c{k \in [0, \infty): \forall v \in V: \norm{Tv} \le k \n{v}} = \inf \c{k \in [0, \infty): \forall v \in V \backslash N: \frac{\n{Tv}}{\n{v}} \le k}\\
=& \sup_{\n{v} \neq 0} \frac{\n{Tv}}{\n{v}} = \sup_{\n{v} \neq 0} \norm{T\p{\frac{v}{\n{v}}}} = \sup_{\n{v} = 0} \norm{Tv} = \sup_{\n{v} \le 1} \norm{Tv}
\end{aligned}
$$

- $\forall v \in V: \|Tv\| \le \|T\|\|v\|$.
- $T$ is called **bounded** if $\|T\| < \infty$.

##### Bounded linear maps

Suppose $V$ and $W$ are **semi-normed spaces** over $\bF$.

The set of **bounded linear maps** from $V$ to $W$ is denoted by $\mathcal B(V, W)$.

- $\mathcal B(V, W)$ is a vector space over $\bF$.
- $\|\cdot\|: \mathcal B(V, W) \to [0, \infty)$ is a **seminorm**.
    - For $T \in \mathcal B(V, W)$ and $\alpha \in F$, $\|\alpha T\| = |\alpha|\|T\|$.
    - For $S, T \in \mathcal B(V, W)$, $\|S + T\| \le \|S \| + \|T\|$.
- $T \in \mathcal B(V, W)$ and $S \in \mathcal B(W, X)$. Then $ST \in \mathcal B(V, X)$.
- $\forall v \in V: \|ST v\| \le \|S\|\|Tv\| \le \|S\|\|T\| \|v\|$.

Suppose $V$ and $W$ are **normed vector spaces** now. Now $\mathcal B(V, W)$ is a **normed space**.

- $\|\cdot\|: \mathcal B(V, W) \to [0, \infty)$ is a **norm**.
    - $\|T\| = 0$ if and only if $T = 0$.

##### $\mathcal B(V, W)$ is Banach if $W$ is Banach

Suppose $V$ and $W$ are **normed vector spaces**.

Normed space $\mathcal B(V, W)$ is Banach if $W$ is Banach.
- Suppose $(T_k)_{k = 1}^\infty \in \mathcal B(V, W)$ and $\sum_{k = 1}^\infty \|T_k\| = M < \infty$.
- Consider any $v \in V$.
- Let $T(v) := \sum_{k = 1}^\infty T_kv$. Since $\sum_{k = 1}^\infty \norm{T_k v} \le M\|v\| < \infty$.
- So $T$ is well defined on $V$ and clearly $T \in \L(V, W)$.
- $T \in \mathcal B(V, W)$ as well, since $\norm{Tv} = \norm{\sum_{k = 1}^\infty T_k v} \le \sum_{k = 1}^\infty \norm{T_k v} \le M \|v\|$.

##### Continuous linear maps

Suppose $V$ and $W$ are **normed vector spaces**.

- $T \in \L(V, W)$ is continuous iff $T$ is continuous at $0 \in V$.
- $T \in \L(V, W)$ is continuous iff $T \in \mathcal B(V, W)$.

$T \in \mathcal B(V, W)$ then $\null T$ is closed.

#### Ordering of Norms

Assume $\bF = \R, \C$ in this chapter.

##### Ordering of norms

Suppose $V$ is a **vector space** over $\bF$.

Suppose  $\|\cdot\|'$  and $\|\cdot\|''$ are norms on $V$. And the generated open sets are $\tau', \tau''$.

- $\|\cdot\|'$  is **dominated** by $\|\cdot\|''$ if $\tau' \subseteq \tau''$. Denoted by $\|\cdot\|' \preceq \|\cdot\|''$. (resp. strictly.)
  - Equivalently if the closed sets under $\tau'$ are closed under $\tau''$.
- $\|\cdot\|'$ and $\|\cdot\|''$ are **equivalent** if $\tau' = \tau''$. Denoted by $\|\cdot\|' \approx \|\cdot\|''$.
  - $\|\cdot\|' \approx \|\cdot\|''$ if and only if $\|\cdot\|' \preceq \|\cdot\|''$  and $\|\cdot\|'' \preceq \|\cdot\|'$.

Consider identity map $I: (V, \|\cdot\|'') \to  (V, \|\cdot\|')$. The following are equivalent:	

- $I$ is continuous.
- $I$ is bounded.
- $\exists C > 0, \forall v \in V:\|v\|'\le C\|v\|''$.
- $I^{-1}$ maps open sets to open sets.
- $\tau' \subseteq \tau''$.

A Cauchy sequence remains Cauchy under equivalent norms.

##### All norms on finite dimensional spaces are equivalent

Suppose $V$ is finite dimensional vector space over $\bF$. All norms on $V$ are equivalent. ==TODO==

Therefore $V$ is complete under any norms.

##### Finite dimensional subspace are closed

Suppose $V$ is a normed space over $\bF$ and $U$ is a finite dimensional subspace. Then $U$ is closed.
- Suppose sequence $(f_n)_{n=1}^\infty \in U$ and $f_n \to g$ in $V$. We only need to show $g \in U$.
- $U$ is a complete metric space according to.
- $(f_n)$ is Cauchy in $U$. So $g \in U$. And $U$ is closed.

#### Linear Homeomorphisms

> When is a linear map a homeomorphism? Being continuous alone is not enough.

Assume $\bF = \R, \C$ in this chapter.

##### Linear Homeomorphisms

Suppose $X, Y$ are normed vector spaces.

$T \in \mathcal \L(X, Y)$ is a homeomorphism iff $T$ is bijective and is **bounded above and below**.

Suppose $T \in \mathcal B(X, Y)$ is bijective. Then the following are equivalent:
1. $T$ is a homeomorphism.
1. $T^{-1}$ is continuous.
1. $\exists c > 0, \forall y \in Y: \|T^{-1} y\| \le c\|y\|$, or $T^{-1}$ is **bounded above**.
1. $\exists c > 0, \forall x \in X: \norm{T x} \ge c\| x\|$, or $T$ is **bounded below**.


Suppose $T$ is a linear homeomorphism.

- If $X$ is Banach, $Y$ is also Banach.
- $T^{-1}$ is also a linear homeomorphism.

##### Topological embedding

Suppose $T \in \L(X, T[X])$ is an linear homeomorphism, $T$ is a **(topological) embedding**.

##### Identity norms keeps the space Banach

Suppose $\|\cdot\|' \approx \|\cdot\|''$ are norms on $X$, and $(X, \|\cdot\|')$ is Banach, then $(X, \|\cdot\|'')$ is Banach.

- Since $\|\cdot\|'' \approx \|\cdot\|'$, identity map $I: (X, \|\cdot\|') \to  (X, \|\cdot\|'')$ is a homeomorphism.

##### Coisometry and isometry

Suppose $X, Y$ are nonzero normed vector spaces over $\bF$.

Now suppose $T \in \L(X, Y)$.

$T \in \L(X, Y)$ is called a **coisometry** if $TB_X(0; 1) = B_Y(0; 1)$.

- Equivalently we could define $T\overline{B_X(0; 1)} = \overline{B_Y(0; 1)}$.
- $T$ is **continuous** with $\n{T} = 1$, and $T$ is **surjective**.

$T$ is called an **isometry** if $\forall x \in T: \n{x} = \n{Tx}$.

- A surjective isometry is a coisometry.

$T$ is called an **isometric homeomorphism** iff $T$ is an injective coisometry.

- $T$ is an isometric homeomorphism iff $T$ is a **bijection between unit balls**.
- $T$ is also called an **isometric isomorphism**.

#### Linear Open Mappings

Assume $\bF = \R, \C$ in this chapter.

##### Open mappings

Suppose $X, Y$ are topological spaces. And $f: X \to Y$.

$f$ is an **open mapping**, or just $f$ is open, if $f$ maps open maps to open maps. (c.f. closed).

##### Linear open mappings

Suppose $X, Y$ are normed vector spaces over $\bF$. And $T \in \L(X, Y)$.

$T$ is open iff there exists $r > 0$ where $T[B_X(0; 1)] \supseteq B_Y(0; r)$.

- $\to$ Since $T B_X(0; 1)$ is open, some open neighbor of $0$ is in $TB_X(0; 1)$.
- $\from$
  - Suppose $U \subseteq X$ is open, and $x \in U$.
  - So $x + B_X(0; \epsilon) \subseteq U$.
  - Then $Tx + B_Y(0; r\epsilon) \subseteq T[U]$.
  - So $T[U]$ is open in $Y$.

We have following properties:

- Open linear maps are surjective.
- Coisometries are open maps.
