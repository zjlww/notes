Assuming all vector spaces are **finite-dimensional** inner product spaces over $\bF = \R, \C$.

##### Traversal lemma

Suppose $V$ is a **inner product space** over $\bF$. And $s, t \in V$, $T\in \L(V)$.

- $\forall v \in V: \pd v s = \pd v t \iff s = t$.
- $\forall v, w \in V: \pd {Tv} w = \pd{Sv} w \iff T = S$.

##### Operator adjoint

Suppose $V, W, U$ are **inner product spaces** over $\bF$. Let $T \in \L(V, W)$ and $S \in \L(W, U)$.

- The **adjoint** of $T$ is the map $T^{*}: W \rightarrow V$ such that $\forall v \in V, \forall w \in W: \pd{T v} w=\pd v {T^{*} w}$.
  - By **Riesz representation theorem in finite case**, $T^*: W \to V$ is well defined.
  - The adjoint remains linear $T^{*} \in \mathcal{L}(W, V)$.
  - The map $\L(V, W) \to \L(W, V)$ defined by $T \mapsto T^*$ is conjugate linear.
    - $(S+T)^{*}=S^{*}+T^{*}$.
    - $(\lambda T)^{*}=\bar{\lambda} T^{*}$ for all $\lambda \in \symbf{F}$.
  - $(T^{*})^{*}=T$ by definition.
  - $I^{*}=I$, where $I$ is the identity operator on $V$.
  - $(S T)^{*}=T^{*} S^{*}$.
- The range and null spaces of $T$ and $T^*$ are of special interest.
  - $\null T^* = (\range T)^\perp$.
    - $w\in \null T^* \iff \forall v:\pd v{T^*w} = 0 \iff \forall v:\pd {Tv} w = 0 \iff w \in (\range T)^\perp$
  - $\range T^* = (\null T)^\perp$.
  - $\null T = (\range T^*)^\perp$.
  - $\range T = (\null T^*)^\perp$.
- $T$ is injective if and only if $T^{*}$ is surjective.
- $T$ is surjective if and only if $T^{*}$ is injective.
- $\dim \null T^* = \dim \null T + \dim W - \dim V$.
- And $\dim \range T^* = \dim \range T$.

##### Matrix adjoint

Suppose $A \in \bF^{m \times n}$, the conjugate transpose of $A$ is denoted by $A^* \in \bF^{n \times m}$. $A_{ij} = \overline{A_{ji}^*}$.

Suppose $(e_i)$ and $(f_j)$ are **orthonormal basis** of $V$ and $W$. Suppose $T \in \L(V, W)$.

- $\M(T)_{ij} = \pd {Te_j}{f_i} = \pd{e_j}{T^* f_i} = \overline{\pd{T^* f_i}{e_j}} = \overline{\M(T^*)_{ji}}$.
- So $\M(T)^* = \M(T^*)$.

##### Self-adjoint

Suppose $V$ is an **inner product space** over $\bF$. Let $S, T \in \L(V)$.

- Suppose $T = T^*$, $T$ is called **self-adjoint**.
  - $\forall v, w \in V: \pd {Tv}{w} = \pd{v}{Tw}$.
  - $\M(T) = \M(T)^*$.
- Suppose $T = -T^*$, $T$ is called **anti-self-adjoint**.
- All operators are the sum of self-adjoint and anti-self-adjoint operators.
  - Let $P = (T + T^*) / 2$ and $Q = (T - T^*) / 2$. Then $T = P + Q$.
- Suppose $S, T$ are self-adjoint, then $S + T$ is self-adjoint, $\alpha S$ for $\alpha \in \R$ is self-adjoint.

Now suppose $T$ is a **self-adjoint** operator.

- Eigenvalues of $T$ are real.
  - Suppose $Tv = \lambda v$. $\langle Tv, v \rangle = \lambda \|v\|^2 = \bar \lambda \|v\|^2$.
- Suppose $U$ is an invariant subspace under $T$.
  - $U^{\perp}$ is invariant under $T$.
    - Suppose $u \in U^\perp$, $\forall w \in U: \pd {Tu} w = \pd{u}{Tw} = 0$. So $Tu \in U^\perp$.
  - $T|_U \in \L(U)$ is self-adjoint.
- $\range T = (\null T)^\perp$. Since $\range T = (\null T^*)^\perp$.
  - $\null T$ and $\range T$ are invariant under $T$.
  - $T|_{\null T}$ and $T|_{\range T}$ are self-adjoint.


##### Complex traversal lemma

Suppose $V$ is an **inner product space** over $\C$, and $T \in \L(V)$.

- $\forall v \in V: \pd {Tv}{v} = 0 \iff T = 0$.
  - Just notice that in a complex inner product space:
    $$
    \begin{aligned}
    \langle T u, w\rangle&=\frac{1}{4}\left(\langle T(u+w), u+w\rangle-\langle T(u-w), u-w\rangle\right) \\
    &+\frac{i}{4}\left({\langle T(u+i w), u+i w\rangle-\langle T(u-i w), u-i w\rangle}\right)
    \end{aligned}
    $$
  - This is clearly not true when $\bF = \R$. Consider the $90^\circ$ rotation.
- $\forall v \in V:\pd {Tv} v \in \R \iff T = T^*$.
  - $\forall v \in V: \pd{Tv} v - \overline{\pd {Tv} v} = \pd{Tv} v - \pd v{Tv} = \pd{Tv} v - \pd {T^* v} v = \pd{(T - T^*) v} {v} = 0$.

##### Real traversal lemma

Suppose $V$ is an **inner product space** over $\R$, and $T \in \L(V)$.

- $\forall v \in V: \pd {Tv}{v} = 0 \iff T = -T^*$.
  - Just notice that in a real inner product space:
    $$
    \pd {(T + T^*)u}{w} = \left(\pd{T(u + w)}{u + w} - \pd {T(u - w)}{u - w}\right) / 2
    $$
  - Therefore $T^* = -T$.
  - The converse is apparent.
- Suppose $T$ is self-adjoint and $\forall v \in V: \pd {Tv} v = 0$ then $T = 0$.

##### Normal operators

Suppose $V$ is an **inner product space** over $\bF$, and $T \in \L(V)$.

- Suppose $TT^* = T^*T$ , then $T$ is called **normal**.
- If $T$ is self-adjoint / anti-self-adjoint, then $T$ is normal.
- $T$ is normal if and only if $\forall v\in V: \n{Tv} = \n{T^*v}$.
  - $\n{Tv}^2  = \n{T^* v}^2 \iff \pd{T^* T v}{v} = \pd {TT^* v}{v} \iff \pd{(T^* T - TT^*)v}{v} = 0$.
  - Notice that $(T^*T - TT^*)$ is self-adjoint.
- If $T$ is normal, for all $\lambda \in \bF$, $T - \lambda I$ is also normal.
  - $(T - \lambda I)(T^* - \bar \lambda I) = TT^* - \lambda T^* - \bar \lambda T + |\lambda|^2 I = (T^* -\bar \lambda I)(T - \lambda I)$.
- If $T$ is normal, then $v \in E(\lambda , T) \iff v \in E(\bar \lambda , T^*)$.
  - Suppose $v \in E(\lambda, T)$. That is $v \in \null (T - \lambda I)$.
  - $0 = \n{(T - \lambda I) v} = \n{(T - \lambda I)^* v} = \n{(T^* - \bar \lambda I)v}$.
  - So $v \in \null (T^* - \bar \lambda I)$. That is $v \in E(\bar \lambda, T^*)$.
- If $T$ is normal, eigenvectors of $T$ corresponding to distinct eigenvalues are **orthogonal**.
  - Suppose $v \in E(\alpha, T)$ and $u \in E(\beta, T)$. Then $u \in E(\bar \beta, T^*)$.
  - $(\alpha - \beta)\pd u v = \pd{\alpha u} v - \pd u {\bar \beta v} = \pd{Tu}{v} - \pd{u}{T^*v} = 0$.
- The set of all normal operators in $\L(V)$ is not a subspace of $\L(V)$.
  - Self-adjoint and anti-self-adjoint operators are normal.
  - If this is true, all operators are normal.
  - However it is easy to construct non-normal operators when $\dim V \ge 2$.
- If $T$ is normal, then $\null T = \null T^*$ and $\range T = \range T^*$.
  - Clearly $\null T = \null T^*$.
  - Also $\range T = (\null T^*)^\perp$ and $\range T^* = (\null T)^\perp$.
- $T$ is normal if and only if for some orthonormal basis $e_1, \ldots, e_n$ of $V$, $\forall j:\n{Te_j} = \n{T^* e_j}$.
  - $\to$ direction is apparent.
  - $\leftarrow$ direction: $\forall v\in V: \n{T v} = \n{T^* v}$.

##### Unitary matrix

Consider a matrix $U \in \bF^{n \times n}$. $U$ is **unitary** if $UU^* = U^* U  = I$.

- $U$ is invertible. And $U^{-1} = U^*$.
- Columns and rows of $U$ are orthonormal basis of $\bF^n$.
- Suppose $(\alpha_i)$ is an orthonormal basis of $\C^n$, then $U = [\alpha_1, \ldots, \alpha_n]$ is unitary.

##### Schur theorem

Suppose $V$ is a inner product space over $\C$. Suppose $\dim V = n$. Let $T \in \L(V)$.

Then $T$ has upper triangular matrix with respect to some orthonormal basis of $V$.

Equivalently, for any matrix $A \in \C^{n \times n}$ there exists unitary $U \in \C^{n \times n}$ and $U^*AU = B$ where $B$ is upper-triangular. We proceed with induction:

- Since $A \in \C^{n \times n}$ there must exists an eigenvalue $\lambda_1$ and unit eigenvector $\alpha_1$.
- Extend $\alpha_1$ to an orthonormal basis of $\C^n$. Define matrix $U_1 = [\alpha_1, \ldots, \alpha_n]$.
- Then $U_1^* A U_1$​ must be of the form $U_1^*AU_1 = \left(\begin{array}{cc}
  \lambda_{1} & \symbf c_{2*}\\ \symbf 0 & C_1\end{array}\right)$.
- Some unitary $U_2 \in \bF^{n - 1 \times n - 1}$ and $U_2^* C_1 U_2 = B_1$ is upper-triangular.
- Now define $U=U_1\left(\begin{array}{ll}
  1 & \symbf 0\\
  \symbf 0& U_{2}
  \end{array}\right)$. Then $U^*AU$ is upper-triangular.
- $$
  U^*AU = \left(\begin{array}{ll}
  1 & \symbf 0\\
  \symbf 0& U_{2}^*
  \end{array}\right)\left(\begin{array}{cc}\lambda_{1} & \symbf c_{2*}\\ \symbf 0 & C_1\end{array}\right) \left(\begin{array}{ll}
  1 & \symbf 0\\
  \symbf 0& U_{2}
  \end{array}\right) = \left(\begin{array}{ll}
  1 & \symbf c_{2*}\\
  \symbf 0& U_{2}^* C_1 U_2
  \end{array}\right)
  $$

##### Complex diagonalization

Suppose $V$ is a inner product space over $\C$. And $T \in \L(V)$.

Then $T$ is normal if and only if $\M(T)$ is **diagonal** under some **orthonormal basis** of $V$.

- $\leftarrow$ direction. Suppose $\M(T)$ is diagonal matrix under orthonormal basis $(e_i)$.
  - $\M(T) \M(T)^* = \M(TT^*) = \M(T)^* \M(T) = \M(T^*T)$. So $T$ is normal.
- $\to$ direciton.
  - There is an orthonormal basis $(e_i)$ where $\M(T)$ is upper triangular by (**Schur**).
  - Then $\M(T, (e_i))$ must be diagonal.
    - Since $\n{T e_1}  = \n{T^* e_1}$, the first row has only one non-zero element.
    - Proceed with $\n{Te_k} = \n{T^* e_k}$, all rows contains only one non-zero element.

##### Positive operators

Suppose $V$ is an inner product space over $\bF$. And $T \in \L(V)$.

Suppose $T$ is **self-adjoint**, then $\forall v \in V: \pd{Tv}{v} \in \R$.

Consider the lower-bound $A = \inf\{\pd {Tv}{v}: v\in V\}$.

- Suppose $A \ge 0$, $T$ is called **positive semi-definite**, or just **positive**.
- Suppose $\forall v \in V\backslash\{0\}: \pd{Tv}v > 0$. Then $T$ is called **positive definite**.
- $T$ is positive and invertible iff $T$ is positive definite.

When we say $T$ is positive, we automatically assume $T$ is self-adjoint.

##### Irreducible quadratic of self-adjoint operators

Suppose $V$ is a **inner product space** over $\bF$. And $T \in \L(V)$.

Suppose $T$ is **self-adjoint** and $b, c \in \R$ obeys $b^2 < 4c$. Then $(T^2 + bT + c I)$ is **positive definite**.
$$
\begin{aligned}
\left\langle\left(T^{2}+b T+c I\right) v, v\right\rangle &=\left\langle T^{2} v, v\right\rangle+b\langle T v, v\rangle+c\langle v, v\rangle \\
&=\langle T v, T v\rangle+b\langle T v, v\rangle+c\|v\|^{2} \\
& \geq\|T v\|^{2}-|b|\|T v\|\|v\|+c\|v\|^{2} \\
&=\left(\|T v\|-\frac{|b|\|v\|}{2}\right)^{2}+\left(c-\frac{b^{2}}{4}\right)\|v\|^{2} \\
&>0
\end{aligned}
$$

So $(T^2 + bT + c I)$ injective, therefore invertible.

##### Existence of eigenvalue in Real vector space

Suppose $V$ is a **inner product space** over $\R$. And $T \in \L(V)$.

Suppose $V \neq \{0\}$ and $T$ is self-adjoint, then $T$ has at least one eigenvalue.

- For any $v \in V\backslash \{0\}$ the list $v, Tv, \ldots ,T^n v$ is linearly dependent.
- Suppose for nonconstant $p(z) \in \R[z]$, and $\deg p \le n$, $p(T)(v)= 0$.
- Factor $p(T)$ in $\R[T]$. Irreducible quadratic terms are invertible.
- So it must be some term $(T - \lambda I)$ that is not injective.

##### Real diagonalization

Suppose $V$ is a inner product space over $\R$. And $T \in \L(V)$.

$T$ is self-adjoint if and only if $\M(T)$ is diagonal under some orthonormal basis of $V$.

- $\leftarrow$ direction is apparent.
- $\to$ direction: Since $T$ is self-adjoint, there exists an eigenvalue $\lambda$, and unit vector $u \in E(\lambda, T)$. 
  - Let $U = \R u$. Then $U, U^\perp$ are invariant under $T$.
  - Construct an orthonormal basis $E$ for $T|_{U^\perp}$. Clearly $u \perp E$.
  - Now add $u$ to $E$ gives a orthonormal basis of $V$.
  - $\M(T, E)$ is diagonal.

##### Character of positive operators

Suppose $V$ is an inner product space over $\bF$.

- $R \in \L(V)$ is called a **square root** of $T \in \L(V)$ if $R^{2}=T$.
- For $T \in \L(V)$ the following are equivalent, prove in loop $1 \to 5$.
  1. $T$ is positive.
     - $(5 \to 1)$ $\pd {Tv}v = \pd{R^* R v}v = \n{Rv} \ge 0$.
  2. $T$ is self-adjoint and all eigenvalues of $T$ are nonnegative.
  3. $T$ has a positive square root.
     - $(2 \to 3)$ Diagonalize under orthonormal basis $(e_i)$.
     - Then $\M(R) = \M(R)^{1/2}$ pointwise gives the matrix of a positive square root.
  4. $T$ has a self-adjoint square root.
  5. $\exists R \in \L(V): T = R^* R$.
- For **positive** $T \in \L(V)$, it has a **unique** positive square root.
  - Since $T$ is positive, there exists an orthonormal basis $(u_i)$ of $V$ that are eigenvectors with eigenvalue $\mu_i \ge 0$.
  - Define $R$ as the linear map where $Ru_i = \sqrt{\mu_i} u_i$.
  - Suppose $S$ is another positive square root of $T$.
  - Since $S$ is positive, there exists an orthonormal basis $(v_i)$ of $V$ that are eigenvectors with eigenvalue $\lambda_i \ge 0$.
  - $Tv_i = S^2 v_i = \lambda_i^2v_i$, so $(v_i)$ are also eigenvectors of $R$.
  - $R^2 v_i = Tv_i = \lambda_i^2 v_i$.
  - Therefore $R$ and $S$ have exactly the same eigenspaces.
- For positive $T \in \L(V)$, denote its unique positive square root as $\sqrt T$.

##### Isometry

Let $V$ be an inner product space over $\bF$. And $S \in \L(V)$.

The following are equivalent for $S \in \L(V)$. Proceed in loop $1 \to 7$.

1. $S$ is an isometry. That is $\forall v \in V: \n {Sv} = \n v$.
   - $(6 \leftrightarrow 5)$
2. $\forall u, v \in V: \pd{Su}{Sv} = \pd uv$.
   - $(1 \to 2)$ By (**Polarization**), the inner product is completely determined by norms.
3. $S(e_i)_{i = 1}^n$ is orthonormal if list $(e_i)$ is orthonormal.
   - $(2 \to 3)$ is apparent.
4. There exists an orthonormal basis $(e_i)$ of $V$, where $S(e_i)_{i = 1}^n$ is orthonormal.
   - $(3 \to 4)$ is apparent.
5. $S^* S = I$.
   - $(4 \to 5)$ just consider the matrix of $S$ under $(e_i)$.
6. $SS^* = I$.
   - $(5 \leftrightarrow 6)$ the left inverse is an right inverse.
7. $S^*$ is an isometry.
   - $(6 \leftrightarrow 7)$, $\forall v \in V: \n{S^* v} = \pd {S^* v} {S^* v} = \pd {SS^* v}{v} = \n v$.

If $S$ is an isometry, it is also normal.

- Since $S$ is an isometry then $S^*S = SS^* = I$.

##### Special matrices and operators

 Consider inner product space $\bF^n$.

| Matrix definition $U \in \bF^{n \times n}$ | Operator definition $T \in \L(\bF^n)$                        |
| ------------------------------------------ | ------------------------------------------------------------ |
| $U$ is **normal** if $UU^* = U^*U$.        | $T$ is **normal** if $TT^* = T^* T$.                         |
| $U$ is **unitary** if $UU^* = U^* U =I$.   | $T$ is an **isometry** if $\forall v \in V: \n{Tv} = \n{v}$. |
| $U$ is **symmetric** if $U^t = U$.         | N/A                                                          |
| $U$ is **Hermitian** if $U^* = U$.         | $T$ is **self-adjoint** if $T^* = T$.                        |
| $U$ is **anti-Hermitian** if $U^* = -U$.   | $T$ is **anti-self-adjoint** if $T^* = - T$.                 |
| $U$ is **idempotent** if $U^2 = U$.        | $T$ is **idempotent** if $T^2 = T$.                          |

##### Polar decomposition

Suppose $V$ is an inner product space over $\bF$. And $T \in \L(V)$.

There exists an **isometry** $S \in \L(V)$ such that $T = S D$ where $D = \sqrt{T^* T}$.

- $T^* T$ and $TT^*$ are **positive** operators, since $\n{Tv} = \pd{Tv}{Tv} = \pd{T^*Tv}{v}$.
- Define $D = \sqrt{T^*T}$. $D$ is positive and $D^2 = T^* T$.
- Then $\n{Tv} = \pd {Tv}{Tv} = \pd {D^2 v}v = \n{D v}$.
- There exists orthonormal basis $(e_i)_{i = 1}^n$ diagonalizing $D$. Suppose $De_i = \sigma_i e_i$, $\sigma_i \in [0, \infty)$.
  - Since $D$ is positive. $V = \range D \oplus \null D$, and $\range D = (\null D)^\perp$.
  - $e_i$ is either in $\range D$ or $\null D$. Split $(e_i, \sigma_i)_{i=1}^n$ into $(r_i, \lambda_i)_{i=1}^m$ and $(n_i, 0)_{i=1}^k$.
  - Such that $\range D = \span(r_i)$ and $\null D = \span(n_i)$.
- Let's further analysis the effect of $T$ on the basis $(e_i)$.
  - Let $U = T[\range D]$.
  - $T[(r_i)] = (Tr_i)$ is an orthogonal basis of $U$.
    - $\pd{Tr_i}{Tr_j} = \pd{Dr_i}{Dr_j} = \lambda_i \lambda_j \delta_{ij}$.
  - Since $\null T = \null D$, $T[(n_i)] = \{0\}$.
- Now we can determine $S$ by defining $S e_i$, while guaranteeing $SD = T$.
  - For $(r_i)_{i=1}^m$, define $S r_i = Tr_i / \lambda_i$. Then $SDr_i = T r_i$.
  - Suppose $(p_i)_{i=1}^k$ is an orthonormal basis of $U^\perp$.
  - For $(n_i)_{i=1}^k$, define $S n_i = p_i$. Then $S D n_i = 0 = T n_i$.
- $S$ is an **isometry**, since $\forall i, j: \pd {S e_i}{S e_j} = \delta_{ij}$.
  - For $r_i$ and $r_j$, $\pd{Sr_i}{Sr_j} = \pd{Tr_i}{Tr_j}/\lambda_i\lambda_j = \delta_{ij}$.
  - For $r_i$ and $n_j$, $\pd{Sr_i}{Sn_j} = \pd{Tr_i/\lambda_i}{p_j} = 0$.
  - For $n_i$ and $n_j$, $\pd{S n_i}{S n_j} = \pd{p_i}{p_j} = \delta_{ij}$.
- $S$ and $D$ are unique in the following sense.
  - Suppose $S$ is an isometry and $R$ is positive and $T = SR$, then $R = D$.
    - $T^* = R^* S^*, T = SR \implies T^* T = R^* R = R^2$.
  - When $T$ is invertible, $S = TD^{-1}$ is uniquely determined.
- The **nonnegative** eigenvalues $\sigma_i$ of **positive** operator $D$ are called **singular values** of $T$.
  - $T$ and $T^*$ have same singular values.
    - $T T^{*}=S \sqrt{T^{*} T}(S \sqrt{T^{*} T})^{*}=S \sqrt{T^{*} T} \sqrt{T^{*} T} S^{*}=S(T^{*} T) S^{-1}$.
    - Now apply result on eigenvalues of similar operators.
  - Suppose $T$ is self-adjoint, the singular values are **absolute** eigenvalues.
  - $\n v\min_i \sigma_i \le \n {Tv} \le \n v\max_i \sigma_i$.


There exists **isometry** $S \in \L(V)$ such that $T = G S$ where $G = \sqrt{TT^*}$.

- Replace $T$ with $T^*$ shows there exists an isometry $S \in \L(V)$ such that $T^* = H\sqrt{TT^*}$.
- Then $T = \sqrt{TT^*} H^*$ where $H^*$ is an isometry.

##### Idiompotent operator

Suppose $V$ is a inner product space over $\bF$ and $P\in \L(V)$.

Suppose $P$ is idempotent, $P^2 = P$.

- $V=\operatorname{null}P\oplus \operatorname{range}P$.
  - Suppose $v \in \range P \cap \null P$. Then $v = Pw$ for some $w \in V$ and $w \neq 0$.
  - But $Pv = P^2 w = Pw \neq 0$. Contradiction.
- $P = P_U$ for some $U \le V$ if and only if $P$ is self-adjoint and $P$ is idempotent.
  - $\to$ direction: $P$ is clearly idempotent.
    - Now suppose $x = u + w$ and $y = s + t$ are orthogonal decompositions.
    - $\pd {P_U (u + w)}{s + t} = \pd{u}{s + t} = \pd u s = \pd {u + w}{P_U(s + t)}$.
    - So $P$ is self-adjoint.
  - $\leftarrow$ direction: TODO.

