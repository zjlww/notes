>  For a very good instruction on functional analysis see [this video](https://www.bilibili.com/video/BV11v4y1f7pC).

##### Vector space

A vector space over field $\bF$ is a set $V$ along with an addition $+$ on $V$ and a scalar multiplication ${\cdot: \bF \times V \to V}$ such that:
- $(V, +)$ is an abelian group.
- For $a, b \in \bF$ and $u, v \in V$:
    - Distribution over addition:
        - $a(u+v)=a u+a v$.
        - $(a+b) v=a v+b v$.
    - Associativity:
        - $(ab) v = a(bv)$.
    - Multiplicative identity: $1 v=v$ for $1 \in \bF$.

Elements of $V$ are called vectors, and elements of $\bF$ are scalars.

Examples of vector spaces:

- For any field $F$, $F[x]$ is a $F$-vector space.
- For any fields $F < E$, $E$ is a $F$-vector space.

##### Functional vector space

If $S$ is a set, then $\mathbf{F}^{S}$ denotes the set of functions from $S$ to $\mathbf{F}$.

- For $f, g \in \mathbf{F}^{S},$ the sum $f+g \in \mathbf{F}^{S}$ is the function defined by $(f+g)(x)=f(x)+g(x)$ for all $x \in S$.
- For $\lambda \in \mathbf{F}$ and $f \in \mathbf{F}^{S},$ the product $\lambda f \in \mathbf{F}^{S}$ is the function defined by $(\lambda f)(x)=\lambda f(x)$ for all $x \in S$.
- $\mathbf F^S$ is a vector space.
    - Take $S = N = \{1, \cdots, N\}$, $\bF^N$ is a vector space over $\bF$.
    - Take $S = \{1, \cdots, m\} \times \{1, \cdots, n\}$, $\bF^{m \times n}$ is a vector space over $\bF$.

##### Commutative ring over field

Suppose $R$ is a NCU ring and $\bF < R$ is a field.

Then $R$ is a vector space over $\bF$, with the addition and scalar multiplication defined naturally.

##### Properties of vector spaces

- All properties of an abelian group.
- $0\cdot v=\vec 0$ for every $v \in V$: Just notice that $0 v=(0+0) v=0 v+0 v$.
- A number times the vector $0$ is $0$: Just notice that $a 0=a(0+0)=a 0+a 0$.
- The number $-1$ times a vector is the additive inverse: Just notice that $v+(-1) v=1 v+(-1) v=(1+(-1)) v=0 v=0$.
- $-(-v) = v$: Just notice that $(-v) + v = 0$.
- $av = 0 \implies$ $a = 0$ or $v=0$
  - Suppose $a$ is not zero, times $\frac{1}{a}$ on both side.
  - Suppose $v$ is not zero. If $a$ is not zero, we have $v = 0$. Which is contradictory.

##### Subspace

A subset $U$ of $V$ is called a subspace of $V$ if $U$ is also a vector space over $\mathbf F$.

##### Subspace test

A subset $U$ of $V$ is a subspace of $V$ if and only if $U$ satisfies the following three conditions:

 - additive identity $0 \in U$.
 - closed under addition $u, w \in U \text { implies } u+w \in U$.
 - closed under scalar multiplication $a \in \mathbf{F}$ and $u \in U$ implies $a u \in U$.

Intersection of subspaces is a subspace. But unions of subspaces may not be a subspace.

##### Spaning subspaces

Suppose $U_{1}, \ldots, U_{m}$ are subspaces of $V .$ Then $U_{1}+\cdots+U_{m}$ is the smallest subspace of $V$ containing $U_{1}, \ldots, U_{m}$.

The sum $U_{1}+\cdots+U_{m}$ is called a **direct sum** if each element of $U_{1}+\cdots+U_{m}$ can be written in only one way as a sum $u_{1}+\cdots+u_{m},$ where each $u_{j}$ is in $U_{j}$. Denoted by $U_{1} \oplus \cdots \oplus U_{m}$.

##### Direct sum test I

$U_{1}+\cdots+U_{m}$ is a direct sum if and only if the only way to write $0$ as a sum $u_{1}+\cdots+u_{m},$ where each $u_{j}$ is in $U_{j},$ is by taking each $u_{j}$ equal to $0$.

##### Direct sum test II

Suppose $U$ and $W$ are subspaces of $V .$ Then $U+W$ is a direct sum if and only if $U \cap W=\{0\}$.
