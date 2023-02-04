

#### Projection to Convex Sets

(**Convex set**)

Suppose $V$ is a vector space. And $U \subset V$.

- For $a, b \in V$ define line segment $\overline{ab} = \{\alpha a + (1 - \alpha) b: \alpha \in [0, 1]\}$.
- $U$ is **convex** if $\forall a, b \in U: \overline{ab} \subseteq U$.
- Suppose $U$ is a **subspace** of $V$, $U$ is convex.

Suppose $V$ is a normed vector space.

- All open balls in $V$ are convex. Due to triangle inequality of the norm.

(**Projections**)

Suppose $V$ is a **normed space** over $\bF$. Suppose $U$ is a **nonempty subset** of $V$.

- We say $u \in U$ is an **projection** of $v \in V$ onto $U$ if $\n{v - u} = \dist(v, U)$.
- Let $\mathcal P_U(v)$ be the **set of all projections** of $v$ onto $U$.

Suppose $V$ is an **inner product space** over $\bF$.

- We say $u \in U$ is **an orthogonal projection** of $v \in V$ onto $U$ if $v - u \perp U$.
- Let $\mathcal O_U(v)$ be the set of all orthogonal projections of $v$ onto $U$.
- $\mathcal O_U(v) \subseteq \mathcal P_U(v)$.
  - Suppose $u \in \mathcal O_U (v)$ then $v - u \perp U$.
  - For $w \in U$, $\n{v - w}^2 = \n{v - u}^2 + \n{u - w}^2$. So $u \in \mathcal P_U(v)$.

(**Projection to closed convex sets in Banach spaces**)

Suppose $V$ is a **Banach space** over $\bF$ and $U$ is a **closed convex subset** of $V$.

Then $\mathcal P_U(v)$ is always a **singleton**. Denoted by $\P_U(v) = \c{P_U(v)}$.

- Construct $u_n \in U$ where $\|v - u_n\| \downarrow \dist(v, U) := A$.

- Such $u_n$ is **Cauchy** since:
  $$
  \begin{aligned}
  \n {u_j - u_k}^2 &= \n{(v - u_j) - (v - u_k)}^2\\ &= 2\n{v - u_j}^2 + 2\n{v - u_k}^2 - 4\n{v - (u_j + u_k)/2}^2\\
  & \le 2 \n{v - u_j}^2 + 2\n{v - u_k}^2 - 4A^2 \to 0
  \end{aligned}
  $$

- $u_n \to u$ for some $u \in V$, since $V$ is complete.

- $u \in U$ since $U$ is a closed subset.

- $\|v - u\| = A$.

- The vector $u$ is unique.

  - Suppose $w \in U$ is another vector where $\n{v - w} = A$.
  - $\n{u - w}^2 \le 2\n{v - u}^2 + 2\n{v - w}^2 - 4A^2 = 0$. So $u = w$.

- Following **existence and uniqueness**, define the **projection func** $P_U: V \to U$ as $P_U(v) = u$.

- $P_U(v) = v$ iff $\dist(v, U) = 0$ iff $v \in U$. So $P_U^2 = P_U$. (Idiompotent.)

(**Projection from closure**)

Suppose $V$ is a **normed space** over $\bF$ and $U$ is a nonempty subset of $V$.

Then $\mathcal P_U(v)$ is never empty implies $U$ is closed.

- For $v \in \overline U \backslash U$, suppose $u \in \mathcal P_U(v)$, then $\n{v - u} = 0$ so $v \in U$. Therefore $U$ is closed.

(**Projection to subspace**)

Suppose $V$ is an **inner product space**. And $v \in V$.

Suppose $U$ is a **subspace** of $V$. $\O_U(v) = \P_U(v)$ is **at most a singleton**.

- $\mathcal O_U(v) \neq \varnothing$ then $\mathcal O_U(v)$ is a **singleton**.
  - Let $u, u' \in \mathcal O_U(v)$, then $v - u \perp U$ and $v - u' \perp U$, so $u - u' \perp U$. So $u - u' = 0$.
- $\mathcal P_U(v) \subseteq \mathcal O_U(v)$. Therefore $\mathcal P_U(v) = \mathcal O_U(v)$.
  - Suppose $u \in U$ and $u \notin\mathcal O_U(v)$. Suppose $w \in U$ and $v - u \not\perp w$.
  - Without loss of generality, suppose $\pd{v - u}{w} > 0$.
  - $\n{v - u + t w}^2 = \n{v - u}^2 + 2t \re\pd{v - u}{w} + t^2\n{w}^2$.
  - So for some $t < 0$, $\n{v - u + tw} < \n{v - u}$. Contradiction.

But in the general case, $\P_U(v)$ can be empty.

(**Projection to finite dimensional subspace**)

Suppose $V$ is an **inner product space**. And $v \in V$.

Suppose $U$ is a **finite dimensional subspace** of $V$. $P_U(v)$ is well defined.

- For every orthonormal basis $e_{1}, \ldots, e_{m}$ of $U$. $P_{U} v=\left\langle v, e_{1}\right\rangle e_{1}+\cdots+\left\langle v, e_{m}\right\rangle e_{m}$.

#### Projection in Hilbert Spaces

(**Hilbert projection to closed subspace**)

Suppose $V$ is a **Hilbert space** over $\bF$. And $U$ is a **closed subspace** of $V$.

- $P_U: V \to U$ is well defined since $V$ is Banach and $U$ is closed and convex.
- In this case $\mathcal O_U(v) = \mathcal P_U(v) = \{P_U(v)\}$.
- $P_U \in \mathcal B(V, U)$.
  - $P_U(x + y) = P_U x + P_U y$. Since $\forall w \in U:(x + y) - (P_U x + P_U y) \perp w$.
  - $P_U(c x) = c P_U x$. Since $\forall w \in U: cx - cP_U x \perp w$.
  - $\n{P_U v} \le \n{v}$ with equality iff $v \in U$.
    - $(v - P_U v) \perp P_U v$, so $\n{v - P_U v}^2 + \n{P_U v}^2 = \n v^2$.
- $V = U \oplus U^\perp$.
  - We already know $U \oplus U^\perp \subseteq V$.
  - For any $v \in V$, $v = P_U(v) + \p{v - P_U\p{v}}$.
- $U = (U^\perp)^\perp$.
  - We already know $U \subseteq \p{U^\perp}^\perp$.
  - $U \supseteq \p{U^\perp}^\perp$.
    - Suppose $v \in (U^\perp)^\perp$. $P_U v \in U \subseteq (U^\perp)^\perp$.
    - So $v - P_{U}v \in (U^\perp)^\perp$. Also $v - P_{U} v \in U^\perp$.
    - So $v = P_{U}v$ and $v \in U$.
- $\range P_{U} = U$ and $\null P_{U} = U^\perp$.

#### Fourier Series

(**Fourier coefficients**)

Suppose $H$ is an **inner product space**.

Given $E = (e_i)_{i \in I}$ is an **orthonormal basis**. Denote $G := \span E$.

- Proof assuming $E$ being countable is much simpler. But we proceed with the general case using **unordered series**.
- In general $G \neq \overline G$. $G = \overline G$ when $E$ is finite.

Given $x \in H$. The $i$-th **Fourier coefficient** of $x$ is defined as $c_i = \pd x {e_i}$. Denoted as
$$
x \sim \sum_{i \in I} c_i e_i
$$
Note that the series on the RHS may not even converge.

When the Fourier series **converges** to $y \in \overline G$. We have following nice properties:

- $y = P_G(x)$. $(x - y) \perp G$.

  - $x - y = x - \sum_i \pd{x}{e_i} e_i$. Therefore $\pd{x - y}{e_j} = 0$.

  - Therefore $y \in \O_G(x) \subseteq \P_G(x)$.

- $\n{y}^2 = \sum_{i\in I} |c_i|^2$. Only countably many coefficients are nonzero!
  $$
  \n{y}^2 = \pd{\sum_{i \in I} c_i e_i}{\sum_{j\in I} c_j e_j} = \sum_{i=0}^\infty |c_i|^2
  $$

- $y = P_{\overline G}(x)$. That is $(x - y) \perp y$.
  $$
  \pd{x}{y} - \n{y}^2 = \pd{x}{\sum_{i \in I} c_i e_i} - \sum_{i \in I} |c_i|^2 = \sum_{i \in I} \pd{x}{c_i e_i} - \sum_{i \in I} |c_i|^2 = 0
  $$

- (Bessel) we always have $\n{x} \ge \n y$, since $y = P_{\overline G}(x)$.

- A very special case is $y \in G$.

  - Only finitely many coefficients are nonzero! Due to definition of span.
  - Clearly $y = P_G(x)$.


Suppose $x = \sum_{i \in I} a_i e_i$ and $y = \sum_{i \in I} b_i e_i$ both converges.

- $\pd{x}{x} = \n{x}^2 = \sum_{i}|a_i|^2 < \infty$, so $\p{a_i}, \p{b_i} \in \ell^2(I)$.
- (Parseval) $\pd{x}{y} = \sum_{i \in I} a_i \overline{b_i}$ happens to be $\pd{(c_i)}{(d_i)}$ in $\ell^2(I)$.
- The map $T: x \mapsto (a_i)$ is an **unitary isomorphism** from $\overline G\to \ell^2(I)$.

(**Orthonormal basis**)

Suppose $H$ is an **inner product space**.

Suppose $E = (e_i)_{i \in I} \in H$ is **orthonormal sequence**.

1. $E$ is an **orthonormal basis** of $H$ if $\forall x \in H, \exists (c_i)_{i \in I} \in \bF: x = \sum_{i \in I} c_i e_i$.
   - An orthonormal basis is in general **NOT** a Hamel basis.
   - By Parseval, $(c_i) \in \ell^2(I)$.
   - So there are at most **countable nonzero Fourier coefficients**.
2. $E$ is **total** if $\overline{\span E} = H$.
3. $E$ is **maximal** if $E$ is not properly contained in larger orthonormal families.
   - $E$ is maximal iff $E^\perp = \{0\}$.

When $H$ is an **inner product space**:

- $(1 \to 2)$ **An orthonormal basis is total.**
  - Suppose $\p{e_i}$ is an orthonormal basis. Suppose $x \in H$.
  - Therefore $x = \sum_{k=1}^\infty a_k f_k$. Where $\p{f_k} \subseteq \p{e_i}$ is countable.
  - Let $x_n = \sum_{k=1}^n a_k f_k$. Clearly $x_n \to x$.
  - So $\span E$ is dense in $H$.
- $(2 \to 1)$ **A total orthonormal set is an orthonormal basis.**
  - Suppose $x \in H$.
  - For $n \ge 1$, there exists a finite $E_n \subseteq E$ and $x_n \in \span E_n$.
  - We can construct a sequence $\p{f_i}_{i=1}^\infty$ where $x_n \in \span (f_i)_{i = 1}^{N(n)}$.
  - Define $c_i = \pd {x}{f_i}$, then $\n{x - \sum_{i = 1}^{N(n)} c_i f_i} < 1/n$.
  - So $\lim_{n\to\infty} \n{x -\sum_{i=1}^n c_i f_i} = \n{x - \sum_{i = 1}^\infty c_i f_i} = 0$. So $x = \sum_i c_i f_i$.
- $(2 \to 3)$ **A total orthonormal set is maximal.**
  - $E^\perp = (\overline{\span E})^\perp  = H^\perp= \{0\}$.


When $H$ is an **Hilbert space**:

- $(3 \to 2)$ **A maximal orthonormal set is total.**
  - Suppose $E$ is maximal. Then $(\overline {\span{E}})^\perp = E^\perp = \c{0}$.
  - Since $H$ is a Hilbert space, $H = E^\perp \oplus \overline {\span E}$.
  - Therefore $\overline{\span E} = H$.


(**Separable inner product space**)

Suppose $H$ is a separable inner product space.

Suppose $E = (e_i)_{i \in I}$ is an orthogonal family in $H$. Then $E$ must be countable.

- Without loss of generality, assume $E$ is an orthonormal.
- Let $X = (x_n)_{n = 1}^\infty \in H$ be a countable dense subset of $H$.
- $\forall i\neq j \in I: B(e_i,\sqrt2 / 2) \cap B(e_j, \sqrt2 / 2) = \varnothing$.
- The open balls $B(e_n, \sqrt{2} / 2)$ are clearly countable.

(**Existence of orthonormal basis**)

Suppose $H$ is an **separable inner product space**.

Then $H$ has an at most countable orthonormal basis.

- Suppose $F = (f_i)_{i = 1}^\infty$ is **at most countable and dense** in $H$.
- Apply (**Gram-Schmidt**) to $F$, obtaining $G = (g_i)_{i = 1}^\infty$.
- Then $G$ is an at most countable orthonormal basis.
