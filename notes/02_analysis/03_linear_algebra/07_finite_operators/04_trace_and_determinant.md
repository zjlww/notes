##### Trace of complex operator

Suppose $V$ is a vector space over $\C$ with $\dim V = n$ and $T \in \L(V)$.

Trace of $T\in \L(V)$ denoted by $\tr T$ is the sum of the eigenvalues repeated according to its multiplicity.

- $\tr T$ equals the negative of the coefficient of $z^{n - 1}$ in characteristic polynomial $p(z)$.
  - Recall that $p(z) = \prod_{i=1}^m (z - \lambda_i)^{d_i}$.

Trace of $A \in \C^{n \times n}$ denoted by $\tr A$ is the sum of the diagonal entries of $A$.

- Suppose $B \in \C^{n \times n}$, $\tr(AB) = \tr (BA)$.
  - $A_{ij}B_{ji} = B_{ji} A_{ij}$.
- Suppose $P \in \C^{n \times n}$ is invertible. Then $\tr(P^{-1}A P) = \tr(APP^{-1}) = \tr(A)$.
- $\tr(T) = \tr(\M(T), (e_i))$ where $(e_i)$ is any basis of $V$.
- $\tr(A + B) = \tr A + \tr B$.

##### Commutator

Define $[S, T] = ST - TS$ as the commutator of $S, T \in \C^{n \times n}$.

- $\tr[S, T] = 0$. And $[S, T] \neq I$.

##### Determinant of complex operators

Suppose $V$ is a vector space over $\C$ with $\dim V = n$ and $T \in \L(V)$.

The determinant of $T$ denoted by $\det(T)$ is the product of the eigenvalues of $T$ repeated according to their multiplicities.

- $\det(T)$ equals $(-1)^n$ times the constant term of the characteristic polynomial $p(z)$.
- $T$ is invertible if and only if $\det T \neq 0$.
- The characteristic polynomial of $T$ is $p(z) = \det(zI - T)$.
  - Suppose $\lambda$ is an eigenvalue with multiplicity $d$ for $T$.
  - $z - \lambda$ is an eigenvalue with multiplicity $d$ for $zI - T$.

##### Permutation

A permutation (on $I = \{1, \ldots, n\}$) is a bijection $\sigma: I \to I$.

- Let $S_n$ be the set of all such permutations. $\abs{S_n} = n!$

We define a sign function $\sgn: S_n \to \{-1, 1\}$.

- Let $\tau(\sigma)$ be the number of inversion pairs.
  - Consider all pairs of $\sigma(i), \sigma(j)$, when $i < j$ but $\sigma(i) > \sigma(j)$ the pair is an inversion. 
- Define $\sgn(\sigma):= (-1)^{\tau(\sigma)}$.
- $\sgn(\sigma^{-1}) = \sgn(\sigma)$.
- $\sgn(\sigma_1\circ \sigma_2) = \sgn(\sigma_1) \sgn(\sigma_2)$.

##### Determinant of complex matrices

Suppose $A = (A_{ij})\in \C^{n \times n}$. The determinant of $A$ denoted by $\det A$ is:
$$
\det A:= \sum_{\sigma\in S_n} \sgn(\sigma) \prod_{i=1}^n A_{\sigma(i),i} = \sum_{\sigma\in S_n} \sgn(\sigma) \prod_{i=1}^n A_{i,\sigma^{-1}(i)} = \sum_{\sigma\in S_n} \sgn(\sigma) \prod_{i=1}^n A_{i,\sigma(i)}
$$

- Suppose $A$ is upper-triangular, then $\det A = 0$.

  - $\sigma(1) \le 1$, $\sigma(2) \le 2$, and so on. The only $\sigma \in S_n$ that satisfies these conditions is the identity.
  - So $\det A = \prod A_{ii}$.

- Elementary operations have various effect on the determinant:

  - Suppose $B$ is the result of application of a single operation.
  - Interchange two rows, then $\det A = -\det B$.
    - Suppose two rows in $A$ are equal, then $\det A = 0$.
  - Add (multiples) a row to another row, then $\det B = \det A$.
    - This is equivalent to add the determinant of a new matrix $B$ with another row replaced with a row. But $\det B = 0$.
  - Multiply a row with $c \in \C$, then $\det B = c \det A$.
  - Permuting the rows with $\sigma$, then $\det B = \sgn(\sigma) \det A$.

- Suppose $A, B \in \C^{n \times n}$ then $\det(AB) = \det(BA) = \det A\cdot \det B$.

  - Construct the following matrix $C = \left(\begin{array}{cc}A & 0 \\
    -I & B\end{array}\right)$.​

  - Now reduce the first row in $C$ to $(0, AB)$ by repeatedly adding the bottom rows:
    $$
    \det C =\det \left(\begin{array}{cc}
    A & 0 \\
    -I & B
    \end{array}\right) = \det \left(\begin{array}{cc}
    0 &AB\\
    -I & B
    \end{array}\right) = (-1)^{n^2} (-1)^n \det AB
    $$

- Determinant of similar matrices are the same as $\det(P^{-1}AP) = \det(APP^{-1}) = \det A$.
- Suppose $V$ is vector space over $\C$ with $\dim V = n$. And $T \in \L(V)$. Then $\det T = \det \M(T, E)$.
  - Since determinant does not depend on the basis, we can take **Jordan form**.

##### Minor

Suppose $A = (A_{ij}) \in \bF^{n \times n}$.

- The $(i, j)$ **minor** $M_{ij}$ of $A$ is the determinant of $A$ removing row $i$ and column $j$.
  $$
  M_{i j}=\left|\begin{array}{cccccc}
  A_{11} & \cdots & A_{1, j-1} & A_{1, j+1} & \cdots & A_{1 n} \\
  \vdots & & \vdots & \vdots & & \vdots \\
  A_{i-1,1} & \cdots & A_{i-1, j-1} & A_{i-1, j+1} & \cdots & A_{i-1, n} \\
  A_{i+1,1} & \cdots & A_{i+1, j-1} & A_{i+1, j+1} & \cdots & A_{i+1, n} \\
  \vdots & & \vdots & \vdots & & \vdots \\
  A_{n 1} & \cdots & A_{n, j-1} & A_{n, j+1} & \cdots & A_{m i}
  \end{array}\right|
  $$

- The $(i, j)$ **cofactor** $C_{ij} = (-1)^{i + j}M_{ij}$.

- $(\newcommand{adj}{\operatorname{adj}}\adj A)_{ji} = (C_{ij})$ is called the **adjugate matrix** of $A$.

##### Laplace expansion

Suppose $A = (A_{ij}) \in \bF^{n \times n}$. Then $\det A = \sum_{k = 1}^{n} A_{ik} C_{ik}$.
$$
C_{nn} = M_{nn} = \left|\begin{array}{ccccc}
A_{11} & A_{12} & \cdots & A_{1, n-1} & A_{1 n} \\
A_{21} & A_{22} & \cdots & A_{2, n-1} & A_{2 n} \\
\vdots & \vdots & & \vdots & \vdots \\
A_{n-1,1} & A_{n-1,2} & \cdots & A_{n-1, n-1} & A_{n-1, n} \\
0 & 0 & \cdots & 0 & 1
\end{array}\right|=\left|\begin{array}{cccc}
A_{11} & A_{12} & \cdots & A_{1, n-1} \\
A_{21} & A_{22} & \cdots & A_{2, n-1} \\
\vdots & \vdots & & \vdots \\
A_{n-1,1} & A_{n-1,2} & \cdots & A_{n-1, n-1}
\end{array}\right|
$$
Now consider generic $C_{ij}$, we claim that
$$
C_{ij} = \left|\begin{array}{ccccccc}
A_{11} & \cdots & A_{1, j-1} & A_{1, j} & A_{1, j+1} & \cdots & A_{1 n} \\
\vdots & & \vdots & \vdots & \vdots & & \vdots \\
A_{i-1.1} & \cdots & A_{i-1, j-1} & A_{i-1, j} & A_{i, j+1} & \cdots & A_{i n} \\
0 & \cdots & 0 & 1 & 0 & \cdots & 0 \\
A_{i+1,1} & \cdots & A_{i+1, j-1} & A_{i+1, j} & A_{i+1, j+1} & \cdots & A_{i+1, n} \\
\vdots & & \vdots & \vdots & \vdots & & \vdots \\
A_{n 1} & \cdots & A_{n, j-1} & A_{n j} & A_{n, j+1} & \cdots & A_{m 1}
\end{array}\right|
$$
This is proved by swapping the row $i$ to the bottom, then swapping the row $j$ to the right.

Now just notice that
$$
|A| = \begin{array}{|cccc|}
A_{11} & A_{12} & \cdots & A_{1 n} \\
\vdots & \vdots & & \vdots \\
A_{i 1}+0+\cdots+0 & 0+A_{i 2}+\cdots+0 & \cdots & 0+\cdots 0+A_{i n} \\
\vdots & \vdots & & \vdots \\
A_{n 1} & A_{n 2} & \cdots & A_{n n}
\end{array}
$$
As a immediate corollary:

- $\sum_{k = 1}^{n} A_{jk} C_{ik} = (A \adj A)_{ij} = 0$ for $i \neq j$.
  - Since this is equivalent to finding the determinant of a matrix with two identical row.
- $A \adj A = (\adj A)A = |A|I$. Thus $A^{-1} = \adj A / |A|$.

##### Vandermonde determinant
$$
D_{n}=\left|x_{j}^{i-1}\right|_{n}=\left|\begin{array}{cccc}
1 & 1 & \cdots & 1 \\
x_{1} & x_{2} & \cdots & x_{n} \\
x_{1}^{2} & x_{2}^{2} & \cdots & x_{n}^{2} \\
\vdots & \vdots & & \vdots \\
x_{1}^{n-1} & x_{2}^{n-1} & \cdots & x_{n}^{n-1}
\end{array}\right|=\prod_{1 \leqslant i<j \leqslant n}\left(x_{j}-x_{i}\right)
$$
Proof: Use mathematical induction. Consider the transform
$$
D_n = \begin{array}{|cccc|}
1 & \cdots & 1 & 1 \\
x_{1}-x_{n} & \cdots & x_{n-1}-x_{n} & 0 \\
x_{1}^{2}-x_{1} x_{n} & \cdots & x_{n-1}^{2}-x_{n-1} x_{n} & 0 \\
\vdots & & \vdots & \vdots \\
x_{1}^{n-1}-x_{1}^{n-2} x_{n} & \cdots & x_{n-1}^{n-1}-x_{n-1}^{n-2} x_{n} & 0
\end{array}
$$
Vandermonde matrix have zero determinant if and only if two columns are the same.

##### Cramer's rule

Suppose $A \in \bF^{n \times n}$ is invertible and $b \in \bF^n$, then $Ax = b$ has unique solution.
$$
D_{j}:=\left|\begin{array}{ccccccc}
A_{11} & \cdots & A_{1, j-1} & b_{1} & A_{1, j+1} & \cdots & A_{1 n} \\
A_{21} & \cdots & A_{2, j-1} & b_{2} & A_{2, j+1} & \cdots & A_{2 n} \\
\vdots & & \vdots & \vdots & \vdots & & \vdots \\
A_{n 1} & \cdots & A_{n, j-1} & b_{n} & A_{n, j+1} & \cdots & A_{m n}
\end{array}\right|
$$
The unique solution is of the form $x_k = D_k/|A|$.
