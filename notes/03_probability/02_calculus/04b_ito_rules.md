#### Multi-dimensional Itô Processes

##### Einstein summation notation

Einstein summation notation is a concise mathematical notation used to simplify the expression of sums involving indexed variables.

In Einstein summation notation, the summation symbol $\sum$ is omitted, and repeated indices in a product term are implicitly assumed to be summed over their entire range. For example, given two vectors $x_i$ and $y_i$, their dot product can be represented in Einstein summation notation as:

$x_i y_i = \sum_{i=1}^{n} x_i y_i$

Here, the repeated index $i$ indicates that the sum is taken over all values of $i$ from $1$ to $n$, where $n$ is the dimension of the vectors.

##### Multi-dimensional stochastic integrals

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\mathbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Suppose $(\mathbf G_t) \in \bA_{2, (n \times m)}(0, T)$. Then we define
$$
\p{\int_0^T \mathbf G_t \dd \mathbf B_t}_{i = 1}^n := \p{\int_0^T G_t^{(i, j)} \dd B^{(j)}_t}_{i = 1}^n
$$

Suppose $(\mathbf G_t) \in \bA^2_{(n \times m)}(0, T)$ we have the expectation is zero:

$$
E\s{\int_0^T \mathbf G_t \dd \mathbf B_t}_{i = 1}^n = E\s{\sum_{j = 1}^m \int_0^T G_t^{(i, j)} \dd B^{(j)}_t}_{i = 1}^n = \mathbf 0
$$
Suppose each process $(G_{t}^{(i, j)})$ are independent, with $\n{\cdot}_F$ being the Frobenius norm, we have
$$
E\s{\norm{\int_0^T \textbf G_t \dd \mathbf B_t}_F^2} = E \s{\int_0^T \norm{\mathbf G_t}_F^2 \dd t}
$$

##### Multi-dimensional Itô processes

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\mathbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Suppose for **non-anticipating** $(\mathbf F_t) \in \bA_{1, (n)}(0, T)$ and $(\mathbf G_t) \in \bA_{2, (n \times m)}(0, T)$, $(\mathbf X_t)$ is a $n$-dimensional stochastic process satisfying
$$
\forall 0 \le s \le r \le T: P\p{\mathbf X_r = \mathbf X_s + \int_s^r \mathbf F_t \dd t + \int_s^r \mathbf G_t \dd \mathbf B_t} = 1,
$$
we say that $(\mathbf X_t)$ is an $n$-dimensional Itô process and write
$$
\dd \mathbf X_t = \mathbf F_t \dd t + \mathbf G_t \dd \mathbf B_t, \quad t \in [0, T]
$$
Which means that for $0 \le i \le n$,
$$
\dd X^{(i)}_t = F_t^{(i)} \dd t + \sum_{j = 1}^m G^{(i, j)}_t \dd B_t^{(j)}, \quad t \in [0, T]
$$

- Notice that $(\mathbf X_t)$ has continuous paths almost surely.

##### Multi-dimensional Itô's chain rule I ==TODO==

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\mathbf B_t)$ be a **$m$-dimensional standard Brownian motion**.


$$
\forall 0 \le i \le n:\dd X^{(i)}_t = F^{(i)}_t \dd t + G^{(i, j)}_t \dd B^{(j)}_t, \quad t \in [0, T]
$$
Suppose $u(x, t) \in C^{2, 1}(\R^n \times [0, T] \to \R)$, that is $D_{t} u, D_{x_ix_j} u, D_{x_j} u$ all exist and are continuous.

- For convenience, we denote $u:= u(\mathbf X_t, t)$, $u_i := D_{x_i}u(\mathbf X_t, t)$, $u_t := D_t u(\mathbf X_t, t)$, $u_{ij} := D_{x_i,x_j}u(\mathbf X_t, t)$ in the following discussion.

Then $u(\mathbf X_t, t)$ has stochastic differential:
$$
\dd u(\mathbf X_t, t) = u_t \dd t + u_i \dd X^{(i)}_t + \frac{1}{2} u_{ij} G_t^{(i, l)}G_t^{(j, l)} \dd t \quad t \in [0, T]
$$

Suppose $u(x, t) \in C^{2, 1}(\R^n \times [0, T] \to \R^d)$, all we can apply Itô's formula to each output dimension:
$$
\dd u^{(k)}(\mathbf X_t, t) = u_t^{(k)} \dd t + u_i^{(k)} \dd X_t^{(i)} + \frac{1}{2} u_{ij}^{(k)} G_t^{(i, l)}G_t^{(j, l)} \dd t \quad t \in [0, T]
$$

##### Differential of the product of independent Brownian motions

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t, \wbar B_t)$ be a two independent **standard Brownian motion**.

Then $\dd (B_t \wbar B_t) = B_t \dd \wbar B_t + \wbar B_t \dd B_t$ for $t \in [0, T]$.

- Let $X_t := (B_t + \wbar B_t) / \sqrt{2}$. Then $(X_t)$ is a standard Brownian motion, as verified by the definition.
- Following from one-dimensional Itô formula: $\dd X_t^2 = 2 X_t \dd X_t + \dd t$, $\dd X_t = (\dd B_t + \dd \wbar B_t) / \sqrt{2}$
- Then
  $$
  \begin{aligned}
  \dd (B_t \wbar B_t) & = \dd \p{X_t^2 - \frac{1}{2}B_t^2 + \frac{1}{2} \wbar B_t^2} = 2X_t \dd X_t + \dd t - \frac{1}{2}(2 B_t \dd B_t + \dd t) - \frac{1}{2}(2\wbar B_t \dd \wbar B_t + \dd t)\\
  & = (B_t + \wbar B_t)(\dd B_t + \dd \wbar B_t) - B_t \dd B_t - \wbar B_t \dd \wbar B_t = B_t \dd \wbar B_t + \wbar B_t \dd B_t
  \end{aligned}
  $$

##### Multi-dimensional Itô product rule

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\mathbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Suppose $(G_t), (H_t) \in \bA_1(0, T)$ and $(\mathbf U_t), (\mathbf V_t) \in \bA_{2, (m)}(0, T)$. And
$$
\dd X_t = G_t \dd t + U^{(k)}_t \dd B^{(k)}_t, \quad \dd Y_t = H_t \dd t + V^{(k)}_t \dd B^{(k)}_t, \quad t \in [0, T]
$$
Now apply Itô chain rule with $u((x, y), t) = xy$ gives
$$
\dd (X_t Y_t) = Y_t \dd X_t + X_t \dd Y_t + U_t^{(k)} V_t^{(k)} \dd t
$$
