#### Linear Maps

##### Linear map

Suppose $V$ and $W$ are vector spaces over $\bF$. $T: V \to W$ is called a **linear map** if $\forall v \in V, \forall \alpha \in \bF: T(\alpha v) = \alpha Tv$ and $\forall u, v \in V: T(u + v) = Tu + Tv$.

- The set of all linear maps from $V$ to $W$ is denoted $\mathcal{L}(V, W)$.
- $\L(V, W)$ is a vector space over $\mathbf F$.
    - with addition $(S+T)(v)=S v+T v$.
    - with scalar multiplication $(\lambda T)(v)=\lambda(T v)$.
- Linear maps are also called **vector space homomorphisms**. Denoted by $\hom_{\bF}(V, W)$.
    - Linear maps are group homomorphisms.

- Linear maps are determined by values on the bases of $V$.
    - Suppose $E$ is a basis of $V$. Suppose for all $e \in E$, $w_e \in W$.
    - There exists a unique linear map $T \in \L(V, W)$ where $T(e) = w_e$.
- Suppose $S \in \L(V, W)$ and $T \in \L(W, U)$. Then $T\circ S = TS \in \L(V, U)$.
- Suppose $T \in \L(V, W)$ is a bijection, it is called **invertible**.
    - $T^{-1} \in \L(W, V)$. $TT^{-1} = I_V$ and $T^{-1}T = I_W$.
    - Invertible linear maps are also called **vector space isomorphisms**.
    - In this case $V \simeq W$ are called **isomorphic**.

- Two finite-dimensional vector spaces over the same field $\mathbf{F}$ are isomorphic if and only if they have the same dimension.
- $\dim \L(V, W) = \dim V \times \dim W$.
- $T \in \L(V, V) = \L(V)$ is called a **linear opertor**.

##### Push-back basis

Suppose $V$ and $W$ are vector spaces over $\bF$. Suppose $T \in \mathcal{L}(V, W)$.

Suppose $v_{1}, \ldots, v_{m}$ is a list of vectors in $V$ such that $T v_{1}, \ldots, T v_{m}$ is a linearly independent list in $W$. Then $v_{1}, \ldots, v_{m}$ is linearly independent list in $V$.

##### Range and null space

Suppose $V$ and $W$ are vector spaces over $\bF$. Suppose $T \in \L(V, W)$.

- Define $\null T=\{v \in V: T v=0\}$.
  - $\null T$ is a subspace of $V$.
  - $T$ is injective if and only if $\null T=\{0\}$.
- Define $\range T=\{T v: v \in V\} = T[V]$.
  - $\range T$ is a subspace of $W$.

##### Fundamental theorem of Linear maps

Suppose $V$ and $W$ are **finite-dimensional** vector spaces over $\bF$. Suppose $T \in \L(V, W)$. Then $\dim V = \dim \null T + \dim \range T$.

##### Sylvester’s rank inequality

Suppose $U, V$ and $W$ are **finite-dimensional** vector spaces over $\bF$. 

Suppose $S \in \L(V, W)$ and $T \in \L(U, V)$.

- Clearly $\dim \null ST = \dim \null T + \dim [\null S \cap \range T]$.
- Which leads to $\dim \null T \le \dim \null ST \le\dim \null S + \dim \null T$.
- Which leads to the **Sylvester’s rank inequality**: 
  - $\dim U - r(T) \le \dim U - r(ST) \le \dim V - r(S) + \dim U - r(T)$.
  - $r(T) \ge r(ST) \ge r(S) + r(T) - \dim V$.
- Which further shows $r(ST) \le \min( r(T), r(S))$.

##### Product vector space

Suppose $(V_\alpha)_{\alpha \in A}$ are vector spaces over $\bF$.

- $\times_\alpha V_\alpha$ with addition and scalar multiplication by coordinate is a vector space.
- Suppose $A$ and $\dim V_\alpha$ are **finite**. $\dim \times_\alpha V_\alpha = +_\alpha \dim V_\alpha$.

##### Direct sum and product space

Suppose $U_1, \ldots, U_m$ are subspaces of vector space $V$.

- Define $\Gamma: U_{1} \times \cdots \times U_{m} \to U_{1}+\cdots+U_{m}$ by $\Gamma\left(u_{1}, \ldots, u_{m}\right)=u_{1}+\cdots+u_{m}$.
- $U_{1}+\cdots+U_{m}$ is a direct sum iff $\Gamma$ is injective.
- $U_{1}+\cdots+U_{m}$ is a direct sum iff $\dim\left(U_{1}+\cdots+U_{m}\right)=\dim U_{1}+\cdots+\dim U_{m}$.

##### Quotient vector space

Suppose $V$ is a vector space over $\bF$. Let $v \in V$ and $U$ a subspace of $V$.

- Define $v+U=\{v+u: u \in U\}$.
- Since $U$ is a normal subgroup, define quotient space $V / U$ with addition.
- Additionally define scalar multiplication $\lambda(v + U) = \lambda v + U$.
  - Scalar multiplication is well defined.
- $(V / U, +, \cdot)$ is a vector space over $\mathbf F$.
- $v + U \in V/  U$ are called **affine subsets**. $v + U$ is said to be **parallel** to $U$.

We could construct a special basis of $V$ as following:

- Suppose $E \subset V$ and $\{e + U: e \in E\}$ is a basis of $V / U$.
- Suppose $F \subset U$ is a basis of $U$.
- Then $E \cup F$ is a basis of $V$.

So if $V$ is a finite-dimensional vector space. Then $\dim V / U = \dim V - \dim U$.

We usually denote the **canonical projection** $v \mapsto v + U$ as $Q_U: V \to V/U$.

- $Q_U \in \L(V, V/U)$ and $\null Q_U = U$, $\range Q_U = V/U$.

##### Quotient linear maps

Suppose $V, W$ are vector spaces over $\bF$. And $T \in \L(V, W)$.

- Suppose $U$ is a subspace of $V$ where $\null T \supseteq U$.
- Let $Q_U(v) = v + U$, then $Q_U\in \L(V, V / U)$.
- Define $T_U: V / U \to W$ by $v + U \mapsto Tv$.
  - $T_U$ is well defined. And $T_U \in \L(V / U, W)$.
  - $\range T/U = \range T$.
  - $T_U$ is the unique map from $V / U$ to $W$ such that $T = T_U \circ Q_U$.
- (**Fundamental theorem of linear homomorphisms**) When taking $U = \null T$, $T_U = \widetilde T$ is an **isomorphism**. So $V / \null T \simeq W$.

##### Double quotient linear maps

Suppose $X, Y$ are vector spaces over $\bF$. Suppose $X_0, Y_0$ are subspaces of $X, Y$.

Suppose $T \in \L(X, Y)$ where $T[X_0] \subseteq Y_0$. Then there exists a unique $_{Y_0}T_{X_0} \in \mathcal L(X/X_0, Y/Y_0)$ such that $_{Y_0}T_{X_0}\circ Q_{X_0} = Q_{Y_0} \circ T$.

- Apply (**Quotient linear maps**) to $Q_{Y_0}\circ T$, demonstrates the existence and uniqueness of $_{Y_0}T_{X_0}$.

Suppose $V = X = Y$. $U$ is a subspace of $V$. And $T \in \L(V)$ where $T[U] \subseteq U$.

- $U$ is called an **invariant subspace** under operator $T$.
- In this case, restricting $T|_U \in \L(U)$.
- In this case, denote $_{U}T_{U} = T/U$. $T / U \in \L(V / U)$.
