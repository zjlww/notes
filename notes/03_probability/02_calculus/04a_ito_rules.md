#### Itô Rules in 1D

##### Itô processes

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

Suppose for **non-anticipating** $(F_t) \in \bA_1(0, T)$ and $(G_t) \in \bA_2(0, T)$, $(X_t)$ is a real-valued stochastic process satisfying
$$
\forall 0 \le s \le r \le T: P\p{X_r = X_s + \int_s^r F_t \dd t + \int_s^r G_t \dd B_t} = 1,
$$
we say that $(X_t)$ is an 1-dimensional Itô process and write
$$
\dd X_t = F_t \dd t + G_t \dd B_t, \quad t \in [0, T]
$$
- Notice that $(X_t)$ has continuous paths almost surely.
- $(G_t) \in \bA^2(0, T)$ guarantees that $\p{\int_0^t G_s \dd B_s} \in \bL_{c, [2], m}^2(0, T)$.
- $(F_t) \in \bA^1(0, T)$ guarantees that $\p{\int_0^t F_s \dd s} \in \bL_{c, [1]}^1(0, T)$.
- When $X_0 = 0$ is deterministic, the process is said to have a **zero start**.
- $(G_t)$ is called the **local volatility**, $(F_t)$ is called the **local drift**.

##### Basic transforms of the Brownian motion

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

We can demonstrate that
$$
\dd B_T^2 = \dd t + 2B_t \dd B_t, \quad t \in [0, T]
$$

- Given partition $(t_{k})_{k = 0}^{m_n} \in P[s, t]$ we have
  $$
  \sum_{k = 0}^{m_n - 1} B_{t_k}(B_{t_{k + 1}} - B_{t_k}) = \frac{B_t^2 - B_s^2}{2} - \frac{1}{2} \sum_{k = 0}^{m_n - 1} (B_{t_{k + 1}} - B_{t_k})^2
  $$
- Now take any sequence of shrinking partition $\p{(t_{n, k})_{k = 0}^{m_n}}_{n = 1}^\infty \subseteq P[s, t]$. We have that with probability one:
  $$
  \int_s^t B_\tau \dd B_\tau = \frac{B_t^2 - B_s^2}{2} + \frac{t - s}{2}
  $$

Also we have
$$
\dd (t B_t) = B_t \dd t + t \dd B_t,\quad t \in [0, T]
$$

- Given partition $(t_{k})_{k = 0}^{m_n} \in P[s, t]$ we have
  $$
  \sum_{k = 0}^{m_n - 1} t_{k} (B_{t_{k + 1}} - B_{t_k}) + \sum_{k = 0}^{m_n - 1} B_{t_{k + 1}}(t_{k + 1} - t_k) = t B_t - sB_s
  $$
- Now take any sequence of shrinking partition $\p{(t_{n, k})_{k = 0}^{m_n}}_{n = 1}^\infty \subseteq P[s, t]$. We have that with probability one:
  $$
  t B_t - sB_s = \int_s^t B_\tau \dd \tau + \int_s^t \tau \dd B_\tau
  $$

##### Itô chain rule ==TODO==

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**. Suppose
$$
\dd X_t = F_t \dd t + G_t \dd B_t,\quad t \in [0, T]
$$
Suppose $u(x, t) \in C^{2, 1}(\R \times [0, T] \to \R)$, that is $D_1 u, D_{11} u, D_2 u$ all exist and are continuous.

- For convenience, we denote $u:= u(X_t, t)$, $u_x := D_1 u(X_t, t)$, $u_t := D_2 u(X_t, t)$, $u_{xx} := D_{11}u(X_t, t)$ in the following discussion.

Then $Y_t = u(X_t, t)$ has stochastic differential
$$
\dd Y_t = \dd u(X_t, t) = u_t \dd t + u_x \dd X_t + \frac{1}{2} u_{xx} G_t^2 \dd t = \p{u_t + u_x F_t + \frac{1}{2} u_{xx} G_t^2} \dd t + u_x G_t \dd B_t, \quad t \in [0, T]
$$

- We always have $\p{u_t + u_x F_t + \frac{1}{2} u_{xx} G_t^2}  \in \bA_{1}(0, T)$ and $(u_x G_t) \in \bA_{2}(0, T)$, they are both non-anticipating.

##### Generalized Itô chain rule ==TODO==

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**. Suppose
$$
\forall i \in \c{1, \ldots, n}:\dd X_t^{(i)} = F_t^{(i)} \dd t + G_t^{(i)} \dd B_t, \quad t \in [0, T]
$$
Suppose $u \in C^{1, 2}(\R^n \times [0, T] \to \R)$. Then let $u_t := D_t u(\mathbf X_t, t)$, $u_i:= D_{x_i} u(\mathbf X_t, t)$ and so on.
$$
\dd u(\mathbf X_t, t) = u_t \dd t + \sum_{i = 1}^{n} u_{i} \dd X^{(i)}_t + \frac{1}{2} \sum_{i, j = 1}^n u_{ij} G_t^{(i)} G_t^{(j)} \dd t,\quad t \in [0, T]
$$

##### Itô's product rule

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

And suppose
$$
\dd X_t = G_t \dd t + U_t \dd B_t, \quad \dd Y_t = H_t \dd t + V_t \dd B_t, \quad t \in [0, T]
$$
Then immediately
$$
\begin{aligned}
\dd (X_t + Y_t) & = (G_t + H_t) \dd t + (V_t + U_t) \dd B_t,& t \in [0, T]\\
\dd (X_t Y_t) & = \frac{1}{2} \p{\dd (X_t + Y_t)^2 - \dd X_t^2 - \dd Y_t^2}, & t \in [0, T]
\end{aligned}
$$
Consider $u(x, t) = x^2$, we have
$$
\begin{aligned}
&\dd X_t^2 = 2X_t \dd X_t + U_t^2\dd t = 2X_t (G_t \dd t + U_t \dd B_t) + U_t^2\dd t = (2X_t G_t + U_t^2) \dd t + 2X_t U_t \dd B_t\\
&\dd Y_t^2 = 2Y_t \dd Y_t + V_t^2 \dd t = 2Y_t (H_t \dd t + V_t \dd B_t) + V_t^2\dd t = (2Y_t H_t + V_t^2) \dd t + 2Y_t V_t \dd B_t\\
&\dd(X_t + Y_t)^2  = 2(X_t+ Y_t) \dd (X_t + Y_t) + (U_t + V_t)^2 \dd t\\
&\dd (X_t + Y_t)^2 = \p{2(X_t + Y_t)(H_t + G_t) + (U_t + V_t)^2} \dd t + 2(X_t + Y_t)(U_t+ V_t) \dd B_t
\end{aligned}
$$
Therefore by subtraction,
$$
\begin{aligned}
\dd (X_t Y_t) &= X_t \dd Y_t + Y_t \dd X_t + U_t V_t \dd t\\
&= X_t(H_t \dd t + V_t \dd B_t) + Y_t (G_t \dd t + U_t \dd B_t) + U_t V_t \dd t\\
& = (X_t H_t + Y_t G_t + U_t V_t) \dd t + (X_t V_t + Y_t U_t) \dd B_t
\end{aligned}
$$

Notice that the same result also follows from the generalized Itô's chain rule.

