#### Kolmogorov's Equations and Fokker-Planck Equation of SDEs

##### Strong assumptions

Consider the SDE $dX_t = b(t, X_t) dt + \sigma(t, X_t)d B_t$. $(B_t)$ and $(X_t)$ are $\R^d$ valued.

Further given initial value $X_0 = Z$. And assume (**Strong condition**) is satisfied.

- A unique strong solution $(X_t)$ exists adapted to $(\F_t)$. Where $\F_t = \sigma(Z, B_{\le t})$.
- $(X_t) \in \V_c(T)$.
- $(X_t)$ is Markov with respect to $(\F_t)$.
- All weakly solutions are weakly unique.

We make the following definitions:

- Define the **matrix** $a(t, x) = \sigma(t, x) \sigma^T(t, x)/2$.
- Define the tensor product $a:b = \sum_{ij} a_{ij}b_{ij}$, for matrix function $a, b$.
- Define the **generator** $\L$ of the diffusion process $(X_t)$.
  - For $f(t, x): I \times \R^d \to \R$, $\L f(t, x) := \nabla f(t, x) \cdot b(t, x) + \nabla^2 f(t, x) : a(t, x)$.
  - For $f(x): \R^d \to \R$, $\L f(x) := \nabla f(x) \cdot b(x) + \nabla^2 f(x): a(x)$ for autonomous SDE.
- Define $\L^* g(t, x) := - \nabla \cdot (g(t, x)b(t, x)) + \nabla^2 :(g(t, x)a(t, x))$.

Suppose $f \in C^{2}([0, T] \times \R^d)$ then by Ito formula:
$$
\begin{aligned}
df(t, X_t)  = & \part_0 f(t, X_t) dt + \nabla f(t, X_t) dX_t + \frac{1}{2} dX_t^T \nabla ^2 f(t, X_t) dX_t = \cdots \\
= & (\part_0 f+ \L f)(t, X_t) dt + \nabla ^T f(t, X_t) \sigma(t, X_t) dB_t
\end{aligned}
$$
Suppose $f \in C^2(\R^d)$ then by Ito formula, as expected:
$$
\begin{aligned}
df(X_t) & = \nabla f(X_t)^T dX_t + \frac{1}{2} dX_t^T \nabla^2 f(X_t) dX_t = \cdots\\
& = \L f(t, X_t) dt + \nabla^T f(t, X_t) \sigma(t, X_t dB_t)
\end{aligned}
$$
##### Fokker-Planck-Kolmogorov equation

Suppose the strong assumptions are true. Consider SDE in $\R^d$ on $I = [0, T]$.
$$
dX_t = b(t, X_t) dt + \sigma(t, X_t)d B_t, \quad b(t, x) \in C(I \times \R^d \to \R^d), \quad \sigma(t, x) \in C(I \times \R^d \to \R^{d \times m})
$$
Suppose $X_t$ has density $p(t, x) \in C^2(I \times \R^d \to [0, \infty))$. And $p_0(x)$ is the density of $X_0$.

- For any $f \in C_c^2(\R^d \to \R)$, we have $d f(X_t) = \L f(X_t) dt + \nabla^T f(X_t) \sigma(t, X_t) dB_t$. Or
  $$
  f(X_{t + s}) - f(X_{t}) = \int_{t}^{t + s} \L f(X_\tau)d\tau + \int_{t}^{t + s}\nabla^T f(X_\tau) \sigma(\tau, X_\tau) dB_\tau
  $$
- Take expectation on both sides, and assume the last part is Martingale and swapping integral is fine.
  $$
  E[f(X_{t + s}) - f(X_{t})] = E \left [\int_{t}^{t + s} \L f(X_\tau)d\tau\right ] = \int_t^{t + s} E[\L f(X_\tau)] d\tau
  $$
- Take limit $s \downarrow 0$ on both sides, and assuming swapping limit and integral is fine.
  $$
  \begin{aligned}
  \frac{\part E[f(X_t)]}{\part t} & = E[\L f(X_t)] = E[\nabla f(X_t) \cdot b(t, X_t) + \nabla^2 f(X_t) : a(t, X_t)]
  \end{aligned}
  $$
  - Consider $E[\nabla f(X_t) \cdot b(t, X_t)]$.
    $$
    E[\nabla f(X_t) \cdot b(t, X_t)] = \int_{\R^d} \nabla f(x) \cdot b(t, x) p(t, x) dx = - \int_{\R^d} f(x) \cdot \nabla (b(t, x)p(t, x)) dx
    $$
  - Consider $E[\nabla^2 f(X_t):a(t, X_t)]$.
    $$
    E[\nabla^2 f(X_t):a(t, X_t)] = \int_{\R^d} \nabla^2 f(x):(a(t, x)p(t, x)) dx = \int_{\R^d} f(x) : \nabla^2(a(t, x)p(t, x))dx
    $$
- Since $E[f(X_t)] = \int_{\R^d} f(x) p(t, x) dx$, assuming swapping differential and integral is fine:
  $$
  \frac{\part E[f(X_t)]}{\part t} = \int_{\R^d} f(x) \frac{\part p(t, x)}{ \part t} dx
  $$
- Now combine what we have for any testing function $f(x) \in C^2_c(\R^d \to \R)$.
  $$
  \int_{\R^d} f(x) \frac{\part p(t, x)}{\part t} dx = \int_{\R^d} f(x) \L^* p(t, x) dx
  $$
- Therefore $p(t, x)$ satisfies the following **FPK** PDE:
  $$
  \part_t p(t, x) = \L^* p(t, x) = - \nabla \cdot (p(t, x)b(t, x)) + \nabla^2 :(p(t, x)a(t, x))
   , \quad t \in [0, T], \quad p(0, x) = p_0(x)
  $$
  where $a(t, x) = \sigma(t, x) \sigma^T(t, x)/2$.

##### Kolmogorov backward equation

Suppose the strong assumptions are true. Consider SDE in $\R^d$ on $[0, T]$.

Let $(X_t)$ be the unique strong solution of the SDE. And $s < t$.

- **Assume** $f \in C_c^2(\R^d)$. The expectation $E[f(X_t) | X_s = y]$ is given by **backward PDE**.
  - Define $u(s, y) = E^{s, y}f(X_t) = E[f(X_t) | X_s = y]$. Ito formula gives:
  $$
  du(t, X_t) = (\part_0 u+ \L u)(t, X_t) dt + \nabla ^T u(t, X_t) \sigma(t, X_t) dB_t
  $$
  - Integrate from $s$ to $t$ gives:
  $$
  u(t, X_t) - u(s, X_s) = \int_s^t (\part_0 u + \L u)(r, X_r) dr + \int_s^t \nabla ^T u(r, X_r) \sigma(r, X_r) dB_r
  $$
  As $u(s, y) = E^{s, y} f(X_t)$, $u(t, X_t) = f(X_t)$. Then $E^{s, y} u(t, X_t) = E^{s, y}f(X_t) = u(s, y)$.
  - Take expectation on $X_s = y$. **Assume** the ito integral part has zero mean.
  $$
  E^{s, y} u(t, X_t) - u(s, y) = 0 = E^{s, y}\int_s^t (\part_0 u + \L u)(r, X_r) dr
  $$
  - **Assume** swapping integral is legal. Divide by $(t - s)$ and take limit $t \downarrow s$ gives:
  $$
  0 = \lim_{t \to s} \frac{1}{t - s}\int_s^t E^{s, y}(\part_0 u + \L u)(r, X_r) dr =^* (\part_0 u + \L u)(s, y)
  $$
  - where $*$ follows from integral MVT. Therefore $u$ is the solution of following **backward PDE**.
  $$
  (\part_0 u + \L u)(s, y) = 0, \quad s < t, \quad u(t, y) = f(y)
  $$
- **Assume** $f \in C_c^2(\R^d)$. The solution of **backward PDE** is $u(s, y) = E[f(X_t) | X_s = y]$.
  - Suppose $u(s, y)$ is the solution of the following differential equation:
  $$
  (\part_0 u + \L u)(s, y) = 0, \quad s < t, \quad u(t, y) = f(y)
  $$
  - **Assume** $u \in C^{1, 2}([0, T] \times \R^d)$, now apply (**Ito formula**):
  $$
  d u(t, X_t) = (\part_0 u + \L u)(t, X_t) dt + \nabla^T u(t, X_t) \sigma(t, X_t) dB_t
  $$
  - Integrate from $0$ to $t$ gives:
  $$
  \Delta u(t, X_t) = u(t, X_t) - u(0, X_0) = \int_0^t \nabla ^T u(r, X_r) \sigma(r, X_r) dB_r
  $$
  - **Assume** the ito integral part is $(\F_t)$-martingale.
  - $\Delta u(s, X_s) = E[u(t, X_t) | X_s] - u(0, X_0) = E[f(X_t) | X_s] - u(0, X_0)$
  - $u(s, X_s) = E[f(X_t) | X_s]$. So $u(s, y) = E[f(X_t) | X_s = y]$ a.s.

Suppose $(X_t)$ has transition density $p(t, x | s, y)$ for $0 \le s \le t \le T$.

- Suppose for some test function $f(x) \in C^2(\R^d)$.
- Define $u(s, y) = E[f(X_t) | X_s = y] = \int f(x) p(t, x | s, y) dx$.
- From above, with some assumptions, $u(s, y)$ satisfies the **backward PDE**:
  $$
  (\part_0 u + \L u)(s, y) = 0, \quad s < t, \quad u(t, y) = f(y)
  $$
- **Assume** the following operation makes sense at all:
  $$
  \part_0 u(s, y) = \int f(x) \part_s p(t, x | s, y) dx; \quad \L u(s, y) = \int f(x) \L_y p(t, x | s, y) dx\\
  (\part_0 u + \L u)(s, y) = \int f(x) (\part_s p + \L_y p)(t, x | s, y) dx = 0, \quad s < t, \quad p(x, t | y, t) = \delta(x - y)
  $$
- Then the transition density $p(t, x | s, y)$ satisfies the following **backward PDE** in the **weak sense**.
  $$
  \part_s p(t, x | s, y) + \L_y p(t, x | s, y) = 0, \quad s < t, \quad p(t, x|t, y) = \delta(x - y)
  $$

Suppose the SDE is of the form $dX_t = b(X_t) dt + \sigma(X_t) dB_t$, i.e. it is autonomous.

- Assume $f \in C_c^2(\R^d)$. The expectation $E[f(X_t) | X_0 = x]$ is a solution of **backward PDE**.
  - Define $u(t, y) = E^{t, y}f(X_T) = E[f(X_T) | X_t = y]$.
  - From above discussion, $u$ is the solution to the backward PDE:
    $$
    (\part_0 u + \L u)(t, y) = 0, \quad t < T, \quad u(T, y) = f(y)
    $$
  - Define $v(t, x) = u(T - t, x) = E^{T - t, x} f(X_T) = E^{0, x} f(X_{t})$.
  - Then $v$ is the solution to the backward PDE:
  $$
  (\part_0 v - \L v)(t, x) = 0, \quad s \in (0, T), \quad v(0, x) = f(x)
  $$
- Assume $f \in C_c^2(\R^d)$. A solution of **backward PDE** $v(t, x) = E[f(X_t) |X_0 = x]$. (**TODO**)

##### Heat equation

Suppose $b(t, x) = 0$ and $\sigma(t, x) = 1$, that is $(X_t)$ is a $\R^d$ standard BM.

- The generator of $(X_t)$ is $\L f(t, x) = \Delta f(t, x)/2$.
- The initial-value backward equation is $\part_0 u(t, x) = \Delta u(t, x) / 2$. Which is the **heat equation**.
- For $f \in C_c^2(\R^d)$, $u(t, x) = E[f(X_t) | X_0 = x]$ solves the heat equation with $u(0, x) = f(x)$.

##### Kolmogorov forward equation

Suppose the strong assumptions are true. Consider SDE in $\R^d$ on $[0, T]$.

Let $(X_t)$ be a **weak solution**.

- Let $p(t, x | s, y)$ be the transition density of $(X_t)$. **Assume** $\part_t p(t, x | s, y)$ is continuous in $t$.
  - Consider some test function $f(x) \in C_c^2(\R^d)$. Ito formula gives:
  $$
  df(X_t)  = \nabla f(X_t) dX_t + \frac{1}{2} dX_t^T \nabla ^2 f(X_t) dX_t =  \L f(t, X_t) dt + \nabla ^T f(X_t) \sigma(t, X_t) dB_t
  $$
  - Integrate from $s$ to $t$ gives:
  $$
  f(X_t) - f(X_s) = \int_s^t \L f(r, X_r) dr + \int_s^t \nabla^T f(X_r) \sigma(r, X_r) dB_r
  $$
  - Take expectation on $X_s = y$. **Assume** the Ito integral part has zero mean.
  $$
  E^{s, y} f(X_t) - f(y) = E^{s, y} \int_s^t \L f(r, X_r) dr
  $$
  - **Assume** swapping expectation and integral is legal. Then
  $$
  \int_{\R^d} f(x) p(t, x | s, y) dx - f(y) = \int_s^t \int_{\R^d} \L f(r, x) p(r, x | s, y) dx dr
  $$
  - **Assume** swapping derivative and integral is legal. Then
  $$
  \int_{\R^d} f(x) \part_t p(t, x | s, y) dx = \int_{\R^d} \L f(t, x) p(t, x | s, y)dx = \int_{\R^d} f(x) \L^*_x p(t, x | s, y) dx
  $$
  - Then the transition probability is a **weak solution** to the **forward PDE**:
  $$
  \part_t p(t, x | s, y) - \L_x^* p(t, x | s, y) = 0, \quad t > s, \quad p(s, x | s, y) = \delta(x - y)
  $$
