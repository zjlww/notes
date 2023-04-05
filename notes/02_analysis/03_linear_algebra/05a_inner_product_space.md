#### Inner Product Spaces

Suppose $\bF = \R$ or $\C$.

##### Inner product

Suppose $V$ is a vector space over $\bF$. An **inner product** on $V$ is $\pd{\cdot}{\cdot}: V \times V \to \symbf F$.

- (positivity) $\forall v \in V:\langle v, v\rangle \in [0, \infty)$.
- (definiteness) $\forall v \in V: v = 0 \iff \langle v, v\rangle=0$.
- (additivity in first slot) $\forall u, v, w \in V: \langle u+v, w\rangle=\langle u, w\rangle+\langle v, w\rangle$.
- (homogeneity in first slot) $\forall \lambda \in \bF, \forall u, v \in V: \langle\lambda u, v\rangle=\lambda\langle u, v\rangle$.
- (conjugate symmetry) $\forall u, v \in V: \langle u, v\rangle=\overline{\langle v, u\rangle}$.

An **inner product space**  is a vector space $V$ along with an **inner product** on $V$.

- The dot product $x \cdot y := \pd{x}{y} = x_i \overline {y_i}$ is the standard inner product on $\bF^n$.

The following properties follows from the axioms:

- $\forall u \in V: v \mapsto \pd v u \in \L(V, \bF)$.
- $\forall u \in V: \pd 0 u = \pd u 0 =0$.
- $\forall u, v, w \in V: \pd {u}{v+w}=\pd{u}{v}+\pd{u}{w}$.
- $\forall u, v \in V, \forall \lambda \in \bF: \pd{u}{\lambda v} = \bar {\lambda} \pd u v$.

The inner product induces a norm on $V$, define $\|v\|:= \pd vv^{1/2}$.

- $\|\cdot\|$ is a **norm** on $V$. See (**Triangle inequality**). So $V$ is a **normed space**.
- The inner product is continuous under the induced topology.
  - Suppose $d_n \to 0$ in $V$ and $u \in V$. $\pd {v + d_n} u - \pd v u = \pd {d_n}{u}$.
  - $|\pd {d_n} u| \le \|d_n\|\|u\| \to 0$ by (**Cauchy-Schwartz**).

Suppose $V$ with the norm defined by inner product is **Banach**. $V$ is a **Hilbert space**.

- **Closed subspace** of a Hilbert space is a Hilbert space.
- Finite dimensional inner product spaces are **Hilbert spaces**.

##### Orthogonality

Suppose $V$ is an inner product space over $\bF$. Two vectors $u, v \in V$ are called **orthogonal** if $\langle u, v\rangle=0$ denoted by $u \perp v$.

- $0$ is orthogonal to every vector in $V$.
- $0$ is the only vector in $V$ that is orthogonal to itself.

##### Pythagorean Theorem

Suppose $V$ is an inner product space over $\bF$.

Suppose $u, v \in V$ and $u \perp v$ then
$$
\|u+v\|^{2}= \pd{u + v}{u + v} = \pd u u + \pd uv + \pd vu + \pd vv = \|u\|^{2}+\|v\|^{2}
$$
##### Orthogonal decomposition

Suppose $V$ is an inner product space over $\bF$. 

Suppose $u, v \in V$ and $v \neq 0$. Let $c={\langle u, v\rangle}/{\|v\|^{2}}$ and $w=u-{\langle u, v\rangle}v/{\|v\|^{2}}$. Then $w \perp v$, and $u=c v+w$.

##### Cauchy-Schwarz Inequality

Suppose $V$ is an inner product space over $\bF$. Suppose $u, v \in V$ 

Then $|\langle u, v\rangle| \leq\|u\|\|v\|$ with equality iff $u = cv$ for some $c \in \bF$ or $v = 0$.

- If $v = 0$, the theorem is clearly true.
- If $v \neq 0$, consider orthogonal decomposition $u={\langle u, v\rangle}v/{\|v\|^{2}}+w$.
- By (**Pythagorean**), $\|u\|^{2} ={|\langle u, v\rangle|^{2}}/{\|v\|^{2}}+\|w\|^{2}
  \geq {|\langle u, v\rangle|^{2}}/{\|v\|^{2}}$.

##### Triangle Inequality

Suppose $V$ is an inner product space over $\bF$. Suppose $u, v \in V$. Then $\|u+v\| \leq\|u\|+\|v\|$.

This inequality is an equality if and only if one of $u, v$ is a nonnegative multiple of the other.

$$
\begin{aligned}
\|u+v\|^{2} &=\langle u+v, u+v\rangle =\langle u, u\rangle+\langle v, v\rangle+\langle u, v\rangle+\langle v, u\rangle \\
&=\langle u, u\rangle+\langle v, v\rangle+\langle u, v\rangle+\overline{\langle u, v\rangle} =\|u\|^{2}+\|v\|^{2}+2 \operatorname{Re}\langle u, v\rangle \\
& \leq\|u\|^{2}+\|v\|^{2}+2|\langle u, v\rangle|  \leq\|u\|^{2}+\|v\|^{2}+2\|u\|\|v\| \\
&=(\|u\|+\|v\|)^{2}
\end{aligned}
$$

With equality if and only if $u = cv$ for some $c \in \R$ or $v = 0$.

##### Parallelogram Equality

Suppose $V$ is an inner product space over $\bF$. Suppose $u, v \in V$. Then
$$
\|u+v\|^{2}+\|u-v\|^{2} = \pd {u + v} {u + v} + \pd {u - v} {u - v} =2(\|u\|^{2}+\|v\|^{2})
$$

##### Perpendicular test

Suppose $V$ is an inner product space over $\bF$. Suppose $u, v \in V$. Then
$$
\pd u v = 0 \iff \forall a \in \bF : \n{u} \le \n{u + av}
$$
##### Product of inner product spaces

Suppose $V_{1}, \ldots, V_{m}$ are inner product spaces over $\bF$.

Then $V = \times_{i = 1}^m V_i$ is a vector space over $\bF$.

- A possible **inner product** on $V$ as $\pd{u}{v} = +_i\pd{u_i}{v_i}$.

##### Orthonormal family / sequences

Suppose $V$ is a **inner product space** over $\bF$.

A set $E \subset V$ is an **orthonormal family** if $\forall a, b \in E: \langle a, b \rangle = 1(a = b)$.

- A orthonormal family is **linearly independent**.
- All elements of $E$ has norm $1$.
- For any finite subset $\{e_1, \ldots, e_m\} \subset E$. And $v = \sum_{i = 1}^ma_i e_i$ for $a_{1}, \ldots, a_{m} \in \symbf{F}$.
  - $\|v\|^{2}=\left|a_{1}\right|^{2}+\cdots+\left|a_{m}\right|^{2}$.
  - $v=\left\langle v, e_{1}\right\rangle e_{1}+\cdots+\left\langle v, e_{n}\right\rangle e_{n}$.
  - $\|v\|^{2}=\left|\left\langle v, e_{1}\right\rangle\right|^{2}+\cdots+\left|\left\langle v, e_{n}\right\rangle\right|^{2}$.
- When $E$ is countable, it is called an **orthonormal sequence**.

An **orthonormal basis** of $V$ is an orthonormal family in $V$ that is also a basis.

Suppose $V$ is **finite dimensional**, every orthonormal list of vectors in $V$ with length $\operatorname{dim} V$ is an orthonormal basis of $V$.

##### Gram-Schmidt procedure

Suppose $V$ is a **inner product space** over $\bF$.

Suppose $(v_i)_{i = 1}^\infty \in V$ is a linearly independent list.

Let $e_{1}=v_{1} /\left\|v_{1}\right\|$. For $j \ge 2$ define $e_{j}$ inductively by
$$
e_{j}=\frac{v_{j}-\left\langle v_{j}, e_{1}\right\rangle e_{1}-\cdots-\left\langle v_{j}, e_{j-1}\right\rangle e_{j-1}}{\left\|v_{j}-\left\langle v_{j}, e_{1}\right\rangle e_{1}-\cdots-\left\langle v_{j}, e_{j-1}\right\rangle e_{j-1}\right\|}
$$
- Then $(e_i)_{i = 1}^\infty$ is an **orthonormal** list of vectors in $V$.
- And $\forall m \in \N^+: \span(v_i)_{j \le m} = \span(e_i)_{j \le m}$.

We have following apparent results:

- Every finite-dimensional inner product space has an orthonormal basis.
- Every orthonormal list can be extended to an orthonormal basis.
- If $T$ has an upper-triangular matrix with respect to some basis of $V,$ then $T$ has an upper-triangular matrix with respect to some orthonormal basis of $V$.

##### Polarization: Expressing inner product with norm

Suppose $V$ is an **inner product space** over $\bF$. And $\n{x }:= \sqrt{\pd xx}$, we have:

1. $\n{x + y}^2 = \n x ^2 + \n y ^2 + 2 \re \pd x y$.
2. $2\n x^2 + 2\n y ^2 = \n {x + y}^2 + \n{x - y}^2$.

The **polarization identities** follows:

- When $\bF = \R$, $\pd xy = (\n{x + y}^2 - \n x^2 - \n y^2)/2$.
  - $\pd x y = -(\n{x - y}^2 - \n x^2 - \n y^2)/2$ by replacing $y$ with $-y$.
  - $\pd x y = (\n{x + y}^2 - \n{x - y}^2) / 4$ by the parallelogram law.
- When $\bF = \C$.
  - $\im \pd x y = - \re \pd {ix} y = \re \pd x{iy}$.
  - So $\pd x y = \re \pd x y +i \re\pd {x} {iy}$.
  - So $\pd x y = (\n{x + y}^2 - \n{x - y}^2 + i\n{x + iy}^2 - i\n{x - i y}^2) / 4$ is a possible solution.

##### Inner product from norm

 ==TODO==

Suppose $(V, \n\cdot)$ is a normed space over $\bF$. If $\n \cdot$ obeys the **parallelogram equality**, then the polarization identities gives an inner product inducing $\n \cdot$.

##### Orthogonal complement

Suppose $V$ is a **inner product space** over $\bF$. Suppose $U \subset V$.

Define the **orthogonal complement** of $U$ as $U^\perp = \{v \in V: \forall u \in U: \pd u v = 0\}$.

- $U^\perp$ is a **closed subspace** of $V$.
  - Suppose $(u_n)_{n = 1}^\infty \in U^\perp$ and $u_n \to u$. Consider $v \in V$.
  - $|\pd u v| = |\pd {u - u_n} v + \pd {u_n} v| = |\pd{u - u_n}{v}| \le \|u - u_n\|\|v\| \to 0$.
  - So $u \in U^\perp$ and $U^\perp$ is closed.
- $\{0\}^{\perp}=V$, $V^{\perp}=\{0\}$.
- $U \cap U^{\perp} \subset\{0\}$. Since $v \perp v \iff v = 0$.
- $U \oplus U^\perp$.
  - Suppose $v = u_1 + w_1 = u_2 + w_2$ where $u_1, u_2 \in U$ and $w_1, w_2 \in U^\perp$.
  - then $u_1 - u_2 = w_2 - w_1 \in U \cap U^\perp$.
  - So $u_1 = u_2$ and $w_1 = w_2$.
- If $U \subset W$, then $W^\perp \subset U^\perp$.
- $(\span U)^\perp = U^\perp$.
- $(\overline U)^\perp = U^\perp$.
  - Clearly $(\overline U)^\perp \subseteq  U^\perp$. We only need to show that $(\overline U)^\perp \supseteq U^\perp$.
  - Suppose $v \in U^\perp$, and $u_n \to u$ where $u_n\in U$ and $u \in \overline U$.
  - The inner product is continuous, so $\pd{v}{u_n} \to \pd v u$ so $\pd v u = 0$. So $v \in (\overline U)^\perp$.
- $U \subseteq (U^\perp)^\perp$.
  - Suppose $u \in U$ and $v \in U^\perp$. Then $\pd u v = 0$.
  - So $u \in (U^{\perp})^\perp$.
- $\overline{\span U} \subseteq (U^\perp)^\perp$.
  - Replace $U$ in $U \subseteq (U^\perp)^\perp$ as $\overline {\span U}$.

##### Unitary

Suppose $H_1, H_2$ are **inner product spaces**.

$U \in \L(H_1, H_2)$ is **unitary** if $\forall x, y \in H_1: \pd{Ux}{Uy} = \pd x y$.

- If $U$ is a unitary and bijective, then $U^{-1}$ is unitary and bijective.

$U$ is **unitary** iff $U$ is **isometric**.
- $\to$ direction: $\norm{Ux} = \pd {Ux}{Ux} = \pd xx = \n{x}$.
- $\leftarrow$ direction: Apply (**Inner product from induced norm**).
