(**Moments of SDE**)

Consider the SDE $dX_t = b(t, X_t) dt + \sigma(t, X_t)d B_t$ in $\R^d$ satisfying the strong conditions.
$$
\begin{aligned}
\frac{\part E[f(X_t)]}{\part t} & = E[\L f(X_t)] = E[\nabla f(X_t) \cdot b(t, X_t) + \nabla^2 f(X_t) : a(t, X_t)]
\end{aligned}
$$

- As we are most interested in mean and covariance, let $m(t) = E[X_t]$ and $P(t) = \cov(X_t)$.
- $m(t)$ satisfies IVP $m'(t) = E[b(t, X_t)]$ with $m(0) = E[X_0]$.
  - Take $f(x) = x_k$.
  - Then $\part_t E[X_t]_k= E[b_k(t, X_t)]$.
  - Therefore $\part_t E[X_t] = E[b(t, X_t)]$.
- $P(t)$ satisfies IVP $P'(t) = E[b(t, X_t)(X_t - m(t))^T] + E[(X_t - m(t))b^T(t, X_t)] + 2E[a(t, X_t)]$.
  - Hint: take $f(x) = x_u x_v - m_u(t)m_v(t)$.

(**Linear SDE**)

Suppose $F(t): C(I \to \R^{d \times d})$, $u(t): C(I\to \R^d)$ and $L(t): C(I \to \R^{d \times m})$. Consider the following SDE satisfying strong assumptions.
$$
dX_t = F(t)X_t dt + u(t) dt + L(t) dB_t
$$

- For the linear ODE $x'(t) = F(t)x(t) + u(t)$, suppose $\Pi(s, t): I \times I \to \R^{d \times d}$ is the **principal matrix**.

  - Let $\Psi(t) = \Pi(0, t)$, $\Psi'(t) = -\Psi(t)F(t)$, and $\Psi(0) = \I$.
  - Apply Ito formula $d(\Psi(t)X_t) = -\Psi(t)F(t) X_t dt + \Psi(t) dX_t = \Psi(t)u(t) dt + \Psi(t)L(t) dB_t$.

- That is equivalent to say:
  $$
  \Psi(t)X_t = X_0 + \int_{0}^t \Psi(s) u(s) ds + \int_0^t \Psi(s) L(s) dB_s
  $$

- And further equivalent to:
  $$
  X_t = \Pi(t, 0)X_0 + \int_0^t \Pi(t, s) u(s) ds + \int_0^t \Pi(t, s) L(s) dB_s \quad (*)
  $$

(**Moments of Linear SDE**)

Continue above discussion. Equation for mean and variance are simplified to:

- $m'(t) = E[F(t) X_t + u(t)] = F(t) m(t) + u(t)$ with $m(0) = E[X_0]$.
- $P'(t) = F(t)P(t) + P(t) F(t)^T + L(t)L(t)^T$ with $P(0) = \cov(X_0)$.

The solutions can be read off the explicit solution $(*)$.

- $m(t) = \Pi(t, 0) m(0) + \int_0^t \Pi(t, s)u(s) ds$.
- $P(t) = \int_0^t \Pi(t, s)L(s) L(s)^T \Pi(t, s)^T ds$.