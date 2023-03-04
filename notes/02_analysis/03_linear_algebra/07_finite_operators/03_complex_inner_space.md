##### A non-diagonalizable operator

As an motivating example, consider $T(w, z) = (z, 0)$ operator on $\L(C^2)$.

- $\det(T - \lambda I) = \lambda^2$ so the only eigenvalue is $\lambda = 0$.
- The only eigenspace $E(0,T) = \{(w, z): z = 0\}$ is one dimensional.
- So the operator is not diagonalizable!

##### Chain of null space

Suppose $V$ is a vector space over $\bF$ with $\dim V = n$. And $T \in \L(V)$.

- $\forall k \ge 1:\null T^k \le \null T^{k + 1}$. Apparently true.
- Suppose $m \ge 1$ and $\null T^m = \null T^{m + 1}$ then $\forall k \ge m: \null T^k = \null T^m$.
  - Just notice that $T^{m + p + 1} v = 0 \leftrightarrow T^{m + 1} (T^p v) =0 \leftrightarrow T^m(T^p v) = 0$.
  - So for all $p \ge 0$, $\null T^{m + p + 1} = \null T^{m + p}$.
- $\null T^n = \null T^{n + 1}$.
  - Otherwise $\dim \null T^{n + 1} = n + 1 > n$.
- $V = \null T^n \oplus \range T^n$.
  - Otherwise, suppose $v \in \null T^n \cap \range T^n$ and $v \neq 0$.
  - $T^n v = 0\land T^n u = v \implies T^{2n} u = 0 \implies T^n u = 0 \neq v$. Contradiction!

Suppose $V$ is an inner product space and $T$ is normal. Then $\null T = \null T^2$.

- Suppose $v \in \null T^2$, then $\pd{T^2 v}{T^2 v} = \pd{T^*Tv}{T^*Tv} = 0$.
- Since $T$ is normal, $\range T = (\null T^*)^\perp$.
- But $T v \in \null T^* \cap \range T$, so $Tv = 0$.
- So $v \in \null T$.

##### Generalized eigenvectors

Suppose $V$ is a vector space over $\bF$ with $\dim V = n$. And $T \in \L(V)$.

Suppose $\lambda$ is an **eigenvalue** of $T$.

Define the **generalized eigenspace** of $T$ corresponding to $\lambda$ as $G(\lambda, T) : = \null (T - \lambda I)^n$.

- $v \in G(\lambda, T)$ and $v \neq 0$ is called a **generalized eigenvector** of $T$ corresponding to $\lambda$.
  - $E(\lambda, T) \subseteq G(\lambda, T)$.
- Generalized eigenvectors corresponding to distinct eigenvalues are linearly independent.
  - Suppose $\lambda_{1}, \ldots, \lambda_{m}$ are distinct eigenvalues of $T$.
  - And $v_{1}, \ldots, v_{m}$ are corresponding generalized eigenvectors.
  - Let $k$ be the largest nonnegative integer such that $\left(T-\lambda_{1} I\right)^{k} v_{1} \neq 0$.
  - Define $w=\left(T-\lambda_1 I\right)^{k} v_{1}$. So $Tw=\lambda_1 w$.
  - Suppose $a_1 v_1 + \cdots + a_m v_m = 0$ with $a_1 \neq 0$.
    - Apply $\left(T-\lambda_{1} I\right)^{k}\left(T-\lambda_{2} I\right)^{n} \cdots\left(T-\lambda_{m} I\right)^{n}$ to the equation.
    - For all $\lambda \in \bF$, $(T - \lambda I )^n w = (\lambda_1 - \lambda)^n w$.
    - Therefore $a_{1}\left(\lambda_{1}-\lambda_{2}\right)^{n} \cdots\left(\lambda_{1}-\lambda_{m}\right)^{n} w = 0$. Contradiction!
- Suppose $T$ is invertible then $G(\lambda_j, T) = G(\lambda_j^{-1}, T^{-1})$.
  - $(T - \lambda_j I)^nv = 0$ implies $(I - \lambda_jT^{-1})v = 0$.

##### Nilpotent

Suppose $V$ is a vector space over $\bF$ with $\dim V = n$.

An operator $N \in \L(V)$ is called **nilpotent** if some power of it equals 0.

- $N^n = 0$.
- There exists a basis $E$ of $V$ where $\M(N, E)$ is **strictly upper-triangular** (with zeros on the diagonal).
  - Begin with an empty list of vectors $E$.
  - For each $i = 1, \ldots, n$. Append $E$ to make it a basis of $\null N^i$.
- $0$ is the only eigenvalue of $N$.

##### Structure of complex operators

Suppose $V$ is a vector space over $\C$ with $\dim V = n$ and $T \in \L(V)$.

Suppose $\lambda_1, \ldots, \lambda_m$ are **distinct eigenvalues** of $T$. Then

1. $G(\lambda_j, T)$ is invariant under $T$.
   - $G(\lambda_j, T) = \null p(T)$ where $p(z) = (z - \lambda_j)^n$.
   - The null space of $p(T)$ is invariant under $T$.
2. $\left.\left(T-\lambda_{j} I\right)\right|_{G\left(\lambda_{j}, T\right)}$ is nilpotent on $G(\lambda_j, T)$.
   - Clearly since $\forall v \in G(\lambda_j, T): (T - \lambda_jI)^n v = 0$.
3. $V = G(\lambda_1, T) \oplus \cdots\oplus G(\lambda_m, T)$.
   - Since $V$ is a **complex** vector space, we are guaranteed to have a eigenvalue $\lambda_1$.
   - Now suppose $U = \operatorname{null} (T - \lambda_1 I)^n$ and $W = \range(T - \lambda_1I)^n$.
   - We have $V = U \oplus W$.
   - According to induction hypothesis, $W = G(\lambda_2, T|_W) \oplus G(\lambda_3, T|_W) \oplus \dots \oplus G(\lambda_m, T|_W)$.
   - This indicates that $V = G(\lambda_1, T) + G(\lambda_2, T) + \dots + G(\lambda_m, T)$. 
   - Since the vectors in generalized eigenspace corresponding to distinct eigenvalues are linearly independent. The sum is a direct sum.

##### Multiplicity of eigenvalues

Suppose $V$ is a vector space over $\bF$ with $\dim V = n$. And $T \in \L(V)$.

Suppose $\lambda$ is an eigenvalue of $T$.

- The **algebraic multiplicity** of $\lambda$ is $\dim G(\lambda, T)$.
- The **geometric multiplicity** of $\lambda$ is $\dim E (\lambda, T)$.

##### Block diagonal matrices

A block diagonal matrix in $\bF^{n \times n}$ is of the form $\left(\begin{array}{ccc}
A_{1} & & 0 \\
& \ddots & \\
0 & & A_{m}
\end{array}\right)$.

- $A_{1}, \ldots, A_{m}$ are square matrices lying along the diagonal.
- All the other entries of the matrix equal 0.
- The block diagonal matrix is also denoted as $A_1 \oplus \cdots \oplus A_m$.

##### Block diagonalization of complex operators

Suppose $V$ is a vector space over $\C$ with $\dim V = n$ and $T \in \L(V)$.

Let $\lambda_{1}, \ldots, \lambda_{m}$ be the distinct eigenvalues of $T,$ with multiplicities $d_{1}, \ldots, d_{m}$.

Then there is a basis of $V$ with respect to which $T$ has a block diagonal matrix with diagonal blocks $A_j \in \C^{d_j \times d_j}$. Further more, each $A_j$ is upper-triangular with $\lambda_j$ on the diagonal.

- Recall that $N_j = \left.\left(T-\lambda_{j} I\right)\right|_{G\left(\lambda_{j}, T\right)}$ is nilpotent.
  - There exist strictly upper triangular matrices for some basis for $N_j$.
  - Let $E_j$ be a list of such base vectors for $N_j$.
- Now define $E$ as the concatenation of all $E_j$.
- $\M(T, E)$ has the desired form.

##### Square root of $I + N$

Suppose $V$ is a vector space over $\bF$ with $\dim V = n$.

Suppose $N \in \mathcal{L}(V)$ is nilpotent. Then $I+N$ has a square root.

- We guess that the square root is of form $p(N)$.
  $$
  \begin{array}{l}
  \left(I+a_{1} N+a_{2} N^{2}+a_{3} N^{3}+\cdots+a_{m-1} N^{m-1}\right)^{2} \\
  \quad=I+2 a_{1} N+\left(2 a_{2}+a_{1}^{2}\right) N^{2}+\left(2 a_{3}+2 a_{1} a_{2}\right) N^{3}+\cdots\\
  \quad = I + N
  \end{array}
  $$

- Clearly we can solve for $a_1$, then $a_2$ and all are uniquely determined.

##### Square roots of complex invertible operators

Suppose $V$ is a vector space over $\C$ with $\dim V = n$.

Suppose $T \in \mathcal{L}(V)$ is invertible. Then $T$ has a square root.

- Recall that for complex vector space, $V = G(\lambda_1, T) \oplus \cdots\oplus G(\lambda_m, T)$.
- Recall that $N_j = (T - \lambda_j I)|_{G(\lambda_j, T)}$ is nilpotent.
- $T_j = T|_{G(\lambda_j, T)}$ and $T_j = N_j + \lambda_j I_j = \lambda_j(I_j + N_j/\lambda_j)$.
- Therefore $T_j$ has a square root $R_j$ restricted to $G(\lambda_j, T)$.
- Now define $R$ as following:
  - For all $v \in V$, there exists unique $g_j \in G(\lambda_j, T)$ where $v = g_1 + \ldots + g_m$.
  - Define $R(v) = \sum_j R_j(g_j)$.
  - So $R^2(v) = \sum_j R_j^2(g_j) = \sum_j T(g_j) = T(v)$.

##### Characteristic polynomial of complex operator

Suppose $V$ is a vector space over $\C$ with $\dim V = n$. And $T \in \L(V)$.

Let $\lambda_{1}, \ldots, \lambda_{m}$ denote the distinct eigenvalues of $T,$ with multiplicities $d_{1}, \ldots, d_{m}$.

The **characteristic polynomial** $p(z) \in \C[z]$ of $T$ is $p(z) = \prod_{i=1}^m (z - \lambda_i)^{d_i}$.

- (**Cayley-Hamilton Theorem**) $p(T) = 0$.
- Suppose $T$ is invertible, $q(z)=z^n p(z^{-1})/p(0)$ is the characteristic polynomial of $T^{-1}$.
  - Since $G(\lambda_j, T) = G(\lambda_j^{-1}, T^{-1})$.

##### Minimal polynomial of operators

Suppose $V$ is a vector space over $\bF$ with $\dim V = n$. And $T \in \L(V)$.

There is a unique monic polynomial $p$ of some minimal degree such that $p(T) = 0$.

> A monic polynomial is a polynomial whose highest-degree coefficient equals 1.

- Consider $I, T, T^{2}, \ldots, T^{n^{2}}$, the list is linearly dependent.
- Find the first $m \in \N$ such that $T^m$ is a linear combination of $T^i, i < m$.
- Suppose $T^m + \sum_{i = 0}^{m - 1} a_i T^i = 0$, define $p(z) = z^m + \sum_{i = 0}^{m - 1} a_i z^i$.
- Clearly $p(T) = 0$.
- There is clearly no other polynomial $q(z)$ with lower degree and $q(T) = 0$.
- Suppose there is another $q(z) \neq p(z) \in \bF[z]$ and $\deg q = \deg p$. Notice that $p - q \neq 0$ and $\deg (p - q) \lt m$. This is not possible.

Such a polynomial $p(z)$  of degree $m$ is called the **minimal polynomial** of $T$.

- When $\bF = \C$, $\deg p \le n$ as the characteristic polynomial has degree $n$.

- To find the minimal polynomial, try to solve the system for different $m$:
  $$
  a_{0} \mathcal{M}(I)+a_{1} \mathcal{M}(T)+\cdots+a_{m-1} \mathcal{M}(T)^{m-1}=-\mathcal{M}(T)^{m}
  $$
  The first successful solution is guaranteed to give the minimal polynomial.

- For $q \in \bF[z]$, $q(T) = 0$ implies $p(z) \mid q(z)$.

  - Clearly $\deg q > \deg p$, division gives $q(T) = p(T) s(T) + r(T)$.
  - $r(T)$ must be zero, otherwise $r(T) = 0$, and $\deg r < \deg p$ which is not possible.

- Zeros of the minimal polynomial is exactly the eigenvalues of $T$. The multiplicity is denoted as the index of the eigenvalue $\lambda$.

  - Suppose $\lambda$ is one of the zeros of $p$.

    - $p(T) = (T - \lambda I)r(T)$. The operator $(T - \lambda I)$ must not be invertible. Otherwise $p(T)$ is not minimal.

  - Suppose $\lambda$ is a eigenvalue of $T$, then
    $$
    \begin{aligned}
    0=p(T) v &=\left(a_{0} I+a_{1} T+a_{2} T^{2}+\cdots+a_{m-1} T^{m-1}+T^{m}\right) v \\
    &=\left(a_{0}+a_{1} \lambda+a_{2} \lambda^{2}+\cdots+a_{m-1} \lambda^{m-1}+\lambda^{m}\right) v \\
    &=p(\lambda) v
    \end{aligned}
    $$

- $T$ is invertible iff the constant term in $p(z)$ is non-zero.

  - $T$ is invertible iff zero is not an eigenvalue.

- If $T$ is invertible the minimal polynomial of its inverse is $q(z) = z^m p(z^{-1})/p(0)$.

  - Since $T^{-m}p(T) = 0$. $q(T^{-1}) = 0$.
  - By symmetry, $p, q$ must be of the same degree.

- When $\bF = \C$, $T$ is diagonalizable if and only if $p(z)$ has no repeated zeros.

- (**Change of coordinate**) Suppose $P \in \L(V)$ is invertible, $S = P^{-1}T P$. Then $p$ is also the minimal polynomial of $S$.

##### Cyclic basis of nilpotent operators

Suppose $V$ is a vector space over $\bF$ and $N \in \L(V)$ is nilpotent.

The **cyclic expansion** of $(v_k)_{k = 1}^n \in V$ by $N$ is defined as following:

- For each $v_k$, define list $E_k = [N^jv_k: 0 \le j \le n, N^{j + 1} v_k \neq 0]$.
- And the expansion is just the concatenation of $E_k$.
- $\newcommand{\expand}[1]{\langle {#1}\rangle}$The expansion is denoted as $N \expand{v_k}$.

$V$ has a basis that is a cyclic expansion by $N$. Called a $N$-**cyclic basis**.

Prove by induction on the dimension $n$:

- The result clearly holds for $\dim V = 1$. Now suppose it holds for $n \le k$.
- Suppose $\dim V = k + 1$.
- Consider $U = \range N$.
  - $U$ is invariant under $N$, and $\dim U \le k$.
  - Suppose $N\expand{v_i}$ is a basis of $U$.
  - Since $v_i \in \range N$, there exists $(u_i)$ where $v_i = Nu_i$.
- $N\expand{u_i}$ is linearly independent.
  - Split $N\expand{u_i} = [N\expand{v_i}, u_1, \ldots, u_n]$.
  - Then $u_j$ is the linear combination of previous vectors.
  - Apply $N$ on the linear combination will show $N\expand{v_i}$ is linearly dependent. Contradiction!
- Extend $N\expand{u_i}$ to a basis of $V$ by appending $(w_1, \ldots, w_p)$.
- If we can ensure $Nw_j = 0$, $(u_i) \cup (w_j) = (r_k)$, then $N\expand{r_k}$ is a basis of $V$. This is indeed possible.
  - There exists $x_j \in \span N\expand{u_i}$ such that $Nx_j = N w_j$.
  - Redefine $w_j := w_j - x_j$. This does not change the span and linear independence. But now $N w_j = 0$.

##### Jordan basis

Suppose $V$ is a vector space over $\bF$. $\dim V = n$ and $T \in \L(V)$.

A basis of $V$ is called a **Jordan basis** for $T$ if $\M(T)$ has following form:
$$
\M(T) = \left(\begin{array}{ccc}
A_{1} & & 0 \\
& \ddots & \\
0 & & A_{p}
\end{array}\right); \quad A_{j}=\left(\begin{array}{cccc}
\lambda_{j} & 1 & & 0 \\
& \ddots & \ddots & \\
& & \ddots & 1 \\
0 & & & \lambda_{j}
\end{array}\right)
$$

- Define $J_n = (J_{ij}) = 1({j- i = 1})$ where $J_n \in \bF^{n \times n}$.
- Then $A_j = \lambda_j I_{n_j} + J_{n_j - 1}$.

##### Jordan form of complex operators

Suppose $V$ is a vector space over $\C$. $\dim V = n$ and $T \in \L(V)$.

Then there exists a Jordan basis for $T$.

- Suppose $T$ is nilpotent, its $T$-cyclic basis is a Jordan basis.
- Suppose $T$ is not nilpotent, and $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$.
  - $(T - \lambda_j I) |_{G(\lambda_j, T)}$ is nilpotent and has a Jordan basis as list $E_j$.
  - Define $E$ as the concatenation of $(E_j)$.
  - It is easy to see that $E$ is a Jordan basis.

A Jordan form of $T$ is convenient as it completely determines the following:

- The sum of sizes of Jordan blocks corresponding to $\lambda$ gives its **algebraic multiplicity** or its power in the **characteristic polynomial**.
- Maximum of sizes of Jordan blocks corresponding to $\lambda$ gives its **index**, or its power in the **minimal polynomial**.
- Number of Jordan blocks corresponding to $\lambda$ gives its **geometric multiplicity**.
  - Notice that $E(\lambda, T) \subseteq G(\lambda, T)$.
  - Now split $G(\lambda, T) = U \oplus E(\lambda, T)$.
  - The dimension of $U$ is given by algebraic multiplicity minus the number of Jordan blocks.

The Jordan form of $T$ is **unique up to permutations** of Jordan blocks:

- Suppose $\lambda$ is an eigenvalue of $T$. Consider only the Jordan blocks corresponding to $\lambda$.
- The minimum integer $k$ where $T^k = 0$ gives the index of $\lambda$.
- Notice the following:
  - $\rank T^{k - 1} = n_k$ is the number of Jordan blocks corresponding to $\lambda$ with size $k$.
  - $\rank T^{k - 2} = 2 \rank T^{k - 1} + n_{k-1}$.
  - $\rank T^{k - 3} = 3\rank T^{k - 1} + 2 \rank T^{k - 2} + n_{k - 2}$.
- Notice that the Jordan form is not uniquely determined by indexes and multiplicities.

