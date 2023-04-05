#### Linear Stochastic Differential Equations

##### Linear SDE I

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

Consider the following Itô SDE:
$$
\dd Y_t = \lambda Y_t \dd B_t, \quad Y_0 = 1,\quad t \in [0, T]
$$

Consider the function $u(x, t) = \exp(\lambda x - \lambda^2 t / 2)$. It satisfies the following partial differential equations:
$$
u_t(x, t) + \frac{1}{2}u_{xx}(x,t) = 0,\quad u_x(x, t) = \lambda u(x, t)
$$
Now notice that
$$
\dd u(B_t, t) = u_t \dd t + u_x \dd B_t + \frac{1}{2} u_{xx} \dd t = \lambda u(B_t, t) \dd B_t, \quad u(0, 0) = 1
$$

##### Linear SDE II

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

Suppose $\beta, \sigma \in C([0, T] \to \R)$. And consider linear SDE
$$
\dd X_t = \beta(t) X_t \dd t + \sigma(t)X_t \dd B_t, \quad X_0 = Z, \quad t \in [0, T]
$$
- Define $(Y_t)$ as the following
  $$
  Y_t := \int_0^t \p{\beta(s) - \frac{1}{2} \sigma^2(s)} \dd s + \int_0^t \sigma(s) \dd B_s
  $$
- Then
  $$
  \dd Y_t = \p{\beta(t) - \frac{1}{2} \sigma^2(t)} \dd t + \sigma(t) \dd B_t
  $$
- Now apply Itô chain rule on $\dd \exp(Y_t)$ gives
  $$
  \dd \exp(Y_t) = \exp(Y_t) \dd Y_t + \frac{1}{2} \exp(Y_t) \sigma^2(t) \dd t = \beta(t) \exp(Y_t) \dd t + \sigma(t) \exp(Y_t) \dd B_t
  $$
- Now consider $X_t = Z \exp(Y_t)$,
  $$
  \dd X_t = Z \dd \exp(Y_t) = \beta(t) Z \exp(Y_t) \dd t + \sigma(t) Z \exp(Y_t) \dd B_t = \beta(t) X_t \dd t + \sigma(t) X_t \dd B_t
  $$

##### Narrow-sense linear SDE: 1-dimensional equation

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

Suppose $\alpha, \beta, \sigma \in C([0, T] \to \R)$. And consider linear SDE
$$
\dd X_t = \p{\alpha(t) + \beta(t) X_t} \dd t + \sigma(t) \dd B_t, \quad X_0 = Z, \quad t \in [0, T]
$$

- Consider the linear ODE $x'(t) = \beta(t) x(t)$ where $x(t) \in C^1([0, T] \to \R)$.
  - The principal matrix solution is
    $$
    \Pi(t, s) = \I\exp\p{\int_{s}^t \beta(\tau) \dd \tau}, \quad \Pi(t_0, t_0) = \I
    $$
  - $\Pi(t_0, t)$ is an integrating factor in the sense that $D_2 \Pi(t_0, t) = -\Pi(t_0, t) \beta(t)$.
  - Therefore multiply on both sides gives:
    $$
    \Pi(t_0, t) x'(t) - \Pi(t_0, t) \beta(t) x(t) = \p{\Pi(t_0, t) x(t)}' = \Pi(t_0, t)\alpha(t)
    $$
  - Now integration on both sides from $t_0 \to t$ gives
    $$
    \Pi(t_0, t) x(t) - x(t_0) = \int_{t_0}^t \Pi(t_0, \tau) \alpha(\tau) \dd \tau
    $$
  - Therefore we have the solution:
    $$
    x(t) = \Pi(t, t_0) x_0 + \int_{t_0}^t \Pi(t, \tau) \alpha(\tau) \dd \tau
    $$
  
- Now we can solve the linear SDE with integrating factor method.
  - According to Itô's chain rule, we have
    $$
    \dd (\Pi(0, t) X_t) = \Pi(0, t) \dd X_t - \Pi(0, t) \beta(t) X_t \dd t = \Pi(0, t)\alpha(t) \dd t + \Pi(0, t)\sigma(t) \dd B_t
    $$
  - Now integration on both sides from $0 \to t$ gives almost surely
    $$
    \Pi(0, t) X_t - Z = \int_0^t \alpha(\tau)\Pi(0, \tau) \dd \tau + \int_0^t \sigma(\tau)\Pi(0, \tau) \dd B_\tau
    $$
  - Now multiply $\Pi(t, 0)$ on both sides gives the final solution.

##### Narrow-sense linear SDE: n-dimensional equation

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\symbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Suppose $\Alpha \in C([0, T] \to \R^{n})$, $\Beta \in C([0, T] \to \R^{n \times n})$, and $\Sigma \in C([0, T] \to \R^{n \times m})$. And consider linear SDE:

$$
\dd \symbf X_t = \p{\Alpha(t) + \Beta(t) \symbf X_t} \dd t + \Sigma(t) \dd B_t, \quad \symbf X_0 = \symbf Z, \quad t \in [0, T]
$$

- Consider the linear ODE $x'(t) = \Beta(t) x(t)$ where $x(t) \in C^1([0, T] \to \R^n)$.
  - Suppose the principal matrix solution is $\Pi(t, s)$. It satisfies the ODE
    $$
    D_1 \Pi(t, t_0) = \Beta(t) \Pi(t, t_0), \quad \Pi(t_0, t_0) = \I
    $$
  - $\Pi(t_0, t)$ is an integrating factor in the sense that $D_2 \Pi(t_0, t) = -\Pi(t_0, t) \beta(t)$.
- Now we can solve the linear SDE with integrating factor method.
  - According to Itô's chain rule, we have
    $$
    \dd \p{\Pi^{(i, j)}(0, t) X^{(j)}_t} = D_t\Pi^{(i, j)}(0, t) X_t^{(j)} \dd t + \Pi^{(i, k)}(0, t) \dd X_t^{(k)}
    $$
  - Or in vector notation
    $$
    \dd (\Pi(0, t) \symbf X_t) = D_2\Pi(0, t)\symbf X_t \dd t + \Pi(0, t) \dd \symbf X_t = \Pi(0, t) \Alpha(t) \dd t + \Pi(0, t) \Sigma(t) \dd \symbf B_t
    $$
  - Now integration on both sides from $0 \to t$ gives almost surely
    $$
    \Pi(0, t) \symbf X_t - \symbf Z = \int_0^t \Pi(0, \tau) \Alpha(\tau) \dd \tau + \int_0^t \Pi(0, \tau) \Sigma(\tau) \dd \symbf B_\tau
    $$
  - Now rearrange the terms gives the final solution.

##### Langevin dynamics

> The convergence of Langevin SDE and Langevin MCMC are widely studied.
>
> Cheng, X., & Bartlett, P.L. (2017). Convergence of Langevin MCMC in KL-divergence. *International Conference on Algorithmic Learning Theory*.

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\symbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Suppose $U(\symbf x) \in C^1(\R^n \to \R)$ is an energy function of a Gibbs distribution $p(\symbf x)$. Consider the following **Langevin SDE**
$$
\dd \symbf X_t = -\frac{1}{2} \nabla U(\symbf X_t) \dd t + \dd \symbf B_t,\quad \symbf X_0 \sim p_0(\symbf x), \quad t \in [0, \infty)
$$

- Suppose $\nabla U(x)$ is good enough, and the SDE satisfies strong assumptions. The FPK equation is
  $$
  D_t p_t(\symbf x) = -\frac{1}{2} D_i \p{D_i U(\symbf x) p_t(\symbf x)} + \frac{1}{2}D_{ii} p_t(\symbf x),\quad t \in [0, \infty)
  $$

- Let $p(\symbf x) = \exp(-U(x))/Z$ where $\int_{\R^n} p(\symbf x) \dd \symbf x = 1$. Then $p(\symbf x)$ is a stable density since
  $$
  \begin{aligned}
  - \frac{1}{2} D_{ii} U(\symbf x) p(\symbf x) - \frac{1}{2} (D_i U(\symbf x))^2 D_i p(\symbf x) + \frac{1}{2} D_{ii} p(\symbf x) = 0
  \end{aligned}
  $$

Typically in the literature, the Langevin SDE is **discretized** into the Langevin MCMC algorithm with **step size** $\epsilon > 0$.
$$
\symbf x_{n + 1} = \symbf x_n - \frac{\epsilon}{2} \nabla U(\symbf x_n) + \sqrt{\epsilon} \symbf {Z}_{n}; \quad (\symbf Z_n) \sim_{\iid} \mathcal N(\symbf 0, \I)
$$

- It can be used to sample from energy-based models and score-based models.

