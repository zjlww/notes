Assuming all vector spaces are **finite-dimensional** spaces over $\bF = \R, \C$.

##### Eigenvalues and eigenvectors

Suppose $V$ is a vector space, and $S, T \in \L(V)$.

- $\lambda \in \bF$ is an **eivenvalue** of $T$ if exists $v \in V \backslash \{0\}$ such that $(T - \lambda I)v = 0$.
- $v \in V \backslash \{0\}$ is called **an eigenvector** of $T$ corresponding to $\lambda$.

We have following properties for eigenvalues / vectors:

- Eigenvector corresponding to **distinct** eigenvalues are linearly independent.
  - Suppose $\lambda_{1}, \ldots, \lambda_{m}$ are distinct eigenvalues of $T$.
  - And $v_{1}, \ldots, v_{m}$ are corresponding eigenvectors.
  - Suppose $k$ is the minimum integer where $v_1, \ldots, v_k$ are linearly independent.
  - Then $v_k = \sum_{i = 1}^{k - 1}a_i v_i$. So $\lambda_k v_k = \sum_{i = 1}^{k - 1}\lambda_i a_i v_i$.
  - Suppose $\lambda_k = 0$, contradiction.
  - Suppose $\lambda_k \neq 0$, $v_k = \sum_{i = 1}^{k - 1}\lambda_i / \lambda_k a_i v_i$. Contradiction.
  - So $T$ has at most $\dim V$ distinct eigenvalues.
- The **eigenspace** of $T$ corresponding to $\lambda$ denoted $E(\lambda, T) = \null (T - \lambda I)$.
  - Let $\lambda_{1}, \ldots, \lambda_{m}$ be distinct eigenvalues of $T$, then $E\left(\lambda_{1}, T\right)\oplus \cdots \oplus E\left(\lambda_{m}, T\right)$.
    - Clearly $\dim E\left(\lambda_{1}, T\right)+\cdots+\dim E\left(\lambda_{m}, T\right) \leq \dim V$.
- Suppose $\M(T) \in \R^{n \times n}$, and $\bF = \C$. If $\lambda$ is an eigenvalue, so is $\bar \lambda$.
  - Suppose $Tv = \lambda v$.
  - Now we proceed in the matrix space.
  - $\M(T) \M(v) = \lambda \M(v)$.
  - Now take complex conjugate on both sides. $\bar \lambda$ is also an eigenvalue.
- $ST$ and $TS$ have the same eigenvalues.
  - Consider eigenvector $v$ and eigenvalue $\lambda$ for $ST$:
  - $ST v = \lambda v \implies TS(Tv) = T\lambda v = \lambda (Tv)$.
  - $Tv \neq 0$ for sure, so $Tv$ is the eigenvector corresponding to $\lambda$ for $TS$.
- Suppose $u, v, (u + v)$ are eigenvectors of $T$. They have the same eigenvalue.
  - $T(u + v) = \lambda(u + v) = \mu u + \nu v \implies (\lambda - \mu) u = (\nu - \lambda) v$.
- Suppose $T$ is invertible.
  - $T v  = \lambda v \implies \lambda^{-1}v = T^{-1} v$.
- Suppose $S$ and $T$ are similar, $S = P^{-1} T P \in \L(V)$ for some $P \in \L(V)$.
  - Since $(P^{-1} T P - \lambda I) = P^{-1} (T - \lambda I) P$, $S$ and $T$ have same eigenvalues.
  - $Tv = \lambda v \iff P^{-1}TP(P^{-1}v) = \lambda P^{-1}v$. So $P^{-1}v \in E(\lambda , S)$.
  - Equivalently $E(\lambda, S) = P^{-1}[E(\lambda, T)]$.

##### Polynomial of operators

Suppose $V$ is a vector space over $\bF$. Suppose $T \in \mathcal{L}(V)$.

- Let $p \in \mathbf F[z]$ and $p(z)=a_{0}+a_{1} z+a_{2} z^{2}+\cdots+a_{m} z^{m}$.

- Define $Q: \bF[z] \to \L(V)$ as $p \mapsto p(T)$. $p(T)=a_{0} I+a_{1} T+a_{2} T^{2}+\cdots+a_{m} T^{m} \in \L(V)$.
  - $Q(p + q) = Q(p) + Q(q)$.
  - $Q(pq) = Q(p)Q(q) = Q(q) Q(p)$.
  
- If $\lambda$ is an eigenvalue of $T$. $p(\lambda)$ is an eigenvalue of $p(T)$.
  
  - $Tv = \lambda v \implies p(T)v = p(\lambda)v$.

- Suppose $\bF = \C$. If $\alpha$ is an eigenvalue of $p(T)$, it must be of the form $p(\lambda)$ where $\lambda$ is an eigenvalue of $T$.
  
  - $p(T)-\alpha I=c\prod_{i = 1}^d(T-\lambda_{1} I)$ is not invertible.
  - So one of $(T - \lambda_k I)$ is not invertible.
  - Therefore $p(\lambda_k) - \alpha = 0$.
  
  - Notice that this does **not** work when $\bF = \R$.
  
- $\null p(T)$ and $\range p(T)$ are invariant under $T$.
  
  - $p(T) v = 0 \implies T \circ p(T) (v) = 0 \implies p(T) (Tv) = 0$.
  - $v = p(T) u \implies Tv = p(T) (Tu)$.
  

##### Existence of eigenvalue of Complex operators

Suppose $V$ is a vector space over $\C$ and $\dim V = n$. Suppose $T \in \L(V)$.

- For any $v \neq 0$, consider $v, T v, T^{2} v, \ldots, T^{n} v$. The list must be linearly dependent.
- Therefore $\sum_i a_i T^i v = 0$ with not all zero $a_i \in \C$.
- Define $p(z) = a_i z^i = c\prod_{i = 1}^m(z - \lambda_i)$. Then $p(T)$ is not invertible.
- So for some $k$, $(T - \lambda_k I)$ is not invertible.
- So $\lambda_k \in \C$ is an eigenvalue of $T$.

##### Upper triangular matrix

A **square** matrix is called **upper triangular** if all the entries below the diagonal equal $0$. For example $\left(\begin{array}{ccc}
\lambda_{1} & & * \\
& \ddots & \\
0 & & \lambda_{n}
\end{array}\right) \in \bF^{n \times n}$ is an upper triangular matrix.

Suppose $T \in \mathcal{L}(V)$ and $v_{1}, \ldots, v_{n}$ is a basis of $V$. Then the following are equivalent:

- $\M(T,(v_1, \ldots, v_m))$ is upper triangular.
- $T v_{j} \in \operatorname{span}\left(v_{1}, \ldots, v_{j}\right)$ for each $j=1, \ldots, n$.
- $\operatorname{span}\left(v_{1}, \ldots, v_{j}\right)$ is invariant under $T$ for each $j=1, \ldots, n$.

Suppose $T \in \L(V)$ has upper-triangular matrix $U$ under some basis.

- $T$ is invertible iff all diagonal entries in $U$ are nonzero.
- The eigenvalues of $T$ are precisely the entries on the diagonal of $U$.

##### Complex operators have upper-triangular matrices

Suppose $V$ is a vector space over $\C$ and $\dim V = n$.

Suppose $T \in \L(V)$. Then $T$ has an upper-triangular matrix with respect to some basis of $V$.

- First find one eigenvalue and eigenvector $v_1$. $U = \operatorname{span}(v_1)$.
- Consider a upper triangular basis of $V/U$ as $(v_i + U)_{i=2,3,\dots,n}$.
- $(T / U)\left(v_{j}+U\right) \in \operatorname{span}\left(v_{2}+U, \ldots, v_{j}+U\right)$.
- Since $T/U \circ Q_U(v_j) = Q_U \circ T(v_j)$. $T(v_j) \in \span(v_1, \ldots, v_j)$.

##### Diagonal matrix

A **diagonal matrix** is a square matrix that is $0$ everywhere except possibly along the diagonal.

- The short-hand for diagonal matrices is $\operatorname{diag}\left(a_{11}, a_{22}, \cdots, a_{nn}\right)$.

Suppose $T \in \L(V)$ has a diagonal matrix under some basis. Then $T$ is called **diagonalizable**.

Let $\lambda_{1}, \ldots, \lambda_{m}$ denote the distinct eigenvalues of $T$. Then the following are equivalent:

- $T$ is diagonalizable.
- $V$ has a basis consisting of eigenvectors of $T$.
- There exist 1-dimensional subspaces $U_{1}, \ldots, U_{n}$ of $V$, each invariant under $T,$ such that $V=U_{1} \oplus \cdots \oplus U_{n}$.
- $V=E\left(\lambda_{1}, T\right) \oplus \cdots \oplus E\left(\lambda_{m}, T\right)$.
- $\operatorname{dim} V=\operatorname{dim} E\left(\lambda_{1}, T\right)+\cdots+\operatorname{dim} E\left(\lambda_{m}, T\right)$.

