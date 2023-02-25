##### Matrix

Let $m$ and $n$ denote positive integers. An $m \times n$ matrix $A$ is a rectangular array of elements of $\mathbf{F}$ with $m$ rows and $n$ columns:
$$
A=\left(\begin{array}{ccc}
A_{1,1} & \ldots & A_{1, n} \\
\vdots & & \vdots \\
A_{m, 1} & \ldots & A_{m, n}
\end{array}\right)
$$
- The notation $A_{jk}$ denotes the entry in row $j,$ column $k$ of $A$.

- For $m$ and $n$ positive integers, the set of all $m$-by-$n$ matrices with entries in $\mathbf{F}$ is denoted by $\mathbf{F}^{m \times n}$.

- For $A \in \bF^{m \times n}$:

  - If $1 \leq j \leq m,$ then $A_{j,\cdot}$ denotes the $1$-by-$n$ matrix of row $j$ of $A$

  - If $1 \leq k \leq n,$ then $A_{\cdot, k}$ denotes the $m$-by-$1$ matrix of column $k$ of $A$.


##### Matrix of a linear map

Suppose $T \in \mathcal{L}(V, W)$ and $v_{1}, \ldots, v_{n}$ is a basis of $V$ and $w_{1}, \ldots, w_{m}$ is a basis of $W .$ The matrix of $T$ with respect to these bases is the $m$-by-n matrix $\mathcal{M}(T)$ whose entries $A_{j, k}$ are defined by
$$
T v_{k}=A_{1, k} w_{1}+\cdots+A_{m, k} w_{m}
$$
If the bases are not clear from the context, then the notation $\mathcal{M}\left(T,\left(v_{1}, \ldots, v_{n}\right),\left(w_{1}, \ldots, w_{m}\right)\right)$ is used.

##### Matrix addition

The sum of two matrices of the same size is the matrix obtained by adding corresponding entries in the matrices:
$$
\left(\begin{array}{ccc}
A_{1,1} & \ldots & A_{1, n} \\
\vdots & & \vdots \\
A_{m, 1} & \ldots & A_{m, n}
\end{array}\right)+\left(\begin{array}{ccc}
C_{1,1} & \ldots & C_{1, n} \\
\vdots & & \vdots \\
C_{m, 1} & \ldots & C_{m, n}
\end{array}\right)
$$
In other words, $(A+C)_{j, k}=A_{j, k}+C_{j, k}$

- Suppose $S, T \in \mathcal{L}(V, W) .$ Then $\mathcal{M}(S+T)=\mathcal{M}(S)+\mathcal{M}(T)$.

##### Scalar product of matrix

The product of a scalar and a matrix is the matrix obtained by multiplying
each entry in the matrix by the scalar:
$$
\lambda\left(\begin{array}{ccc}
A_{1,1} & \ldots & A_{1, n} \\
\vdots & & \vdots \\
A_{m, 1} & \ldots & A_{m, n}
\end{array}\right)=\left(\begin{array}{ccc}
\lambda A_{1,1} & \ldots & \lambda A_{1, n} \\
\vdots & & \vdots \\
\lambda A_{m, 1} & \ldots & \lambda A_{m, n}
\end{array}\right)
$$
In other words, $(\lambda A)_{j, k}=\lambda A_{j, k}$.

- Suppose $\lambda \in \mathbf{F}$ and $T \in \mathcal{L}(V, W) .$ Then $\mathcal{M}(\lambda T)=\lambda \mathcal{M}(T)$.

Suppose $m$ and $n$ are positive integers. With addition and scalar multiplication defined as above, $\bF^{m \times n}$ is a vector space with dimension $m n$.

##### Matrix multiplication

Suppose $A$ is an $m$-by-$n$ matrix and $C$ is an $n$-by-$p$ matrix. Then $A C$ is defined to be the $m$-by-$p$ matrix whose entry in row $j$, column $k$, is given by the following equation:
$$
(A C)_{j, k}=\sum_{r=1}^{n} A_{j, r} C_{r, k}
$$

- If $T \in \mathcal{L}(U, V)$ and $S \in \mathcal{L}(V, W),$ then $\mathcal{M}(S T)=\mathcal{M}(S) \mathcal{M}(T)$.
- $(A C)_{j, k}=A_{j, \cdot} C_{\cdot, k}$ for $1 \leq j \leq m$ and $1 \leq k \leq p$.
- $(A C)_{\cdot, k}=A C_{\cdot, k}$ for $1 \leq k \leq p$.
- Matrix multiplication distributes over addition. $A(B + C) = AB + AC$.
- Matrix multiplication is associative $ABC = (AB)C = A(BC)$.

##### Nonsingular matrix

$A \in \bF^{n \times n}$ is **nonsingular** if there exists $B \in \bF^{n \times n}$ and $AB = I$.

- We do not distinguish left / right inverse since:

  $AB = I \implies BAB = B \implies (BA - I)B = 0 \implies BA = I$.

- $B$ is called an inverse of $A$.

- If the inverse of $A$ exists, it is unique. Denoted by $A^{-1}$.
  - Suppose $B'$ is another inverse, $B'AB = B' = B$.

##### Column space and row space

For $A \in \bF^{m \times n}$, we can define following spaces:

- the column space $\col(A) \subset \bF^m$ or $\range A$ is the span of all column vectors
- the row space $\row(A) = \col(A^T) \subset \bF^n$.
- the solution space $\sol(A) \subset \bF^n$ or $\null A$ is $\{x \in \bF^n: Ax = 0\}$.

##### Elementary operations

There are three row (resp. column) elementary operations. 

1. (**Add**) Add a row to another row.
2. (**Interchange**) Interchange two rows.
3. (**Scale**) Multiply all entries in a row by a nonzero constant in $\mathbf F$.

Two matrices are called **row (resp. column) equivalent** if there is a finite sequence of elementary row operations that transforms one matrix into the other.

- All elementary operations are invertible.

##### Linear system

A linear system over $\bF$ of $m$ **equations** in $n$ **unknowns** is a set of equations:
$$
\begin{array}{cc}
a_{11} x_{1}+\cdots+a_{1 n} x_{n} & =b_{1} \\
a_{21} x_{1}+\cdots+a_{2 n} x_{n} & =b_{2} \\
\vdots & \vdots \\
a_{m 1} x_{1}+\cdots+a_{m n} x_{n} & =b_{m}
\end{array}
$$
where $a_{ij}, b_i \in \bF$.

The linear system can be represented with matrices:
$$
A \mathbf x = \mathbf b; \quad (a_{ij}) = A; \quad \mathbf b = (b_1, \cdots, b_m)^T
$$

- A **solution** is a vector $\mathbf s \in \bF^n$ such that $A\mathbf{s} = \mathbf b$.
  - A solution $\mathbf s \in \bF^n$ is **nontrivial** if $\mathbf s \neq \mathbf 0$.
  - A **solution set** is the set of all solutions of the system.
  - The set of all solutions to the homogeneous system is the **null space** of the system.
- The matrix $[A|b]$ is the **augment matrix**.
  - If the augmented matrices of two linear systems are row equivalent, then the two systems have the same solution set.
- The system is called **homogeneous** if $\mathbf{b} = \mathbf{0}$.
- The system of linear equations has either
  1. no solution (**inconsistent**).
  1. exactly one solution (**consistent and fully determined**).
  1. infinitely many solutions (**consistent and under-determined**).

##### Elementary matrices

Applying elementary row (resp. column) operations on identity matrix gives the **elementary matrices**.

- Left multiplication of row elementary matrix applies the same row operation.
- Right multiplication of column elementary matrix applies the same column operation.
- Elementary matrices are **invertible**.

##### Row echelon form

The first non-zero element of a non-zero row is called a **pivot**.

A column containing a pivot is called a **pivot column**.

A rectangular matrix is in **row echelon form** if it has the following three properties:

1. All zero rows are at the bottom of the matrix.
2. Each pivot is in a column to the right of the pivot in rows above it.
3. All entries below a pivot are zeros.

If a matrix in echelon form satisfies the following additional conditions, then it is in reduced echelon form (or **reduced row echelon form**):

4. The pivot in each non-zero row is $1$.
5. All entries above a pivot are zeros.

##### Existence of RREF

The existence of the reduced row Echelon form for any matrix $A \in \bF^{m \times n}$ is guaranteed by the reduction algorithm (omitted here).

RREF of $A \in \bF^{m \times n}$ might look like this:
$$
\operatorname{RREF}(A) = \left[\begin{array}{lllllllll}
1 & 2 & 0 & 4 & 2 & 4 & 0 & 2 & 3 \\
0 & 0 & 1 & 5 & 2 & 5 & 0 & 5 & 5 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 5 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{array}\right]
$$

- The number of pivot columns is the **row rank** of the matrix
  - Denoted by $\rank A$ or $r(A)$.

- Suppose $A$ is the coefficient matrix of linear system $Ax = b$, then
  - Pivot columns corresponds to **fixed variables** / **lead variables**.
  - Other variables are called **free variables**.
  - $\null A$ is given by the non-zero rows.
    - Each non-zero row gives a linear constraint to the space $\null A$.
    - $\dim \null A = n - \rank A$. 

##### Uniqueness of RREF

The row Echelon form of a matrix may not be unique. But the reduced row Echelon form exists and is unique for any matrix.

See [this web site](https://www.cs.uleth.ca/~holzmann/notes/reduceduniq.pdf) for a slick proof.

##### Standard form

A matrix in $\bF^{m \times n}$ is in **standard form** $\left(\begin{array}{cc}
I_{r} & O \\
O & O
\end{array}\right)_{m \times n}$ when $I_r \in \bF^{r \times r}$ is the identity:

For any matrix $A \in \bF^{m \times n}$ we can reduce it into SF:

- Apply row operations to reduce $A$ it to RREF $A_R$. Suppose $R_1, \ldots, R_s$ are row elementary matrix in $\mathbb F^{m \times m}$.
  $$
  R_{s} \cdots R_{2} R_{1} A= A_R
  $$

- Apply column operations to reduce $A_R$ to **standard matrix** $E$. Suppose $C_1, \ldots, C_t$ are column elementary matrices in $\bF^{n \times n}$.

$$
R_{s} \cdots R_{2} R_{1} A C_{1} C_{2} \cdots C_{t} = E
$$

The SF of a matrix must be unique, where $r = \rank A$.

An invertible matrix's RREF and SF must be the same.

##### Blocked matrices

A **blocked matrix** is the tuple $(A \in \bF^{n, m}, (n_1, \ldots, n_s), (m_1,\ldots, m_t))$, where $\sum_{i = 1}^s n_s = n$ and $\sum_{i = 1}^t m_t = m$.

- Then $\mathbf A = (A_{ij})_{i \le s, j \le t}$ where $A_{ij} \in \bF^{n_i \times m_j}$ is the blocking of $A$ under partition $(n_i), (m_j)$.
- $(A \in \bF^{n \times m}, (n_i), (m_j))$ and $(B \in \bF^{m\times p}, (m_j), (p_k))$ can be **multiplied**. The product under shared partition is $(AB, (n_i), (p_k))$ where $\mathbf {AB} = (\sum_{j \le t}A_{ij} B_{jk})_{i \le s, k \le u}$.
- Transpose, addition, ... also works.

##### Matrix inverse algorithm

Suppose we need to inverse matrix $A \in \mathbf F^{n \times n}$.

- Construct $[A | I]$ and row reduce the left half to $I \in \mathbf F^{n \times n}$.
- The result is guaranteed to be $(I | A^{-1})$.


