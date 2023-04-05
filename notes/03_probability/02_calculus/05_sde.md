#### Stochastic Differential Equations

##### Stochastic differential equations

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\symbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Suppose

- Random variable $\symbf Z \in \L(\Omega \to \R^n)$ is independent of $(\symbf B_t)$.
- $\symbf b \in \L(\R^n \times [0, T] \to \R^n)$ and $\symbf A \in \L(\R^n \times [0, T] \to \R^{n \times m})$ are deterministic functions.

An Itô stochastic differential equation (SDE) is of the form
$$
\dd \symbf X_t = \symbf b(\symbf X_t, t) \dd t + \symbf A(\symbf X_t, t) \dd \symbf B_t,\quad \symbf X_0 = \symbf Z, \quad t \in [0, T]
$$
A non-anticipating $\R^n$-valued stochastic process $(\symbf X_t) \in \bL_{c}(0, T)$ is a **(strong) solution** of the Itô SDE if

- $(\symbf X_t)$ satisfies $P(\symbf X_0 = \symbf Z) = 1$, and
  $$
  \forall t \in [0, T]: P\p{\symbf X_t = \symbf X_0 + \int_0^t \symbf b(\symbf X_s, s) \dd s + \int_0^t \symbf A(\symbf X_s, s) \dd \symbf B_s} = 1
  $$
- $\symbf b(\symbf X_t, t) \in \bA_{1, (n)}(0, T)$ and $\symbf A(\symbf X_t, t) \in \bA_{2, (n \times m)}(0, T)$ such that the integrals are well defined.
- A strong solution exists on the filtered space where the given Brownian motion exists.

We can relax the requirements in the following way:

- $(\symbf X_t)$ can exists on a **different** filtered space with a **different** standard Brownian motion $(\symbf B_t)$.
- Only $\symbf X_0 \sim \symbf Z$ in distribution is required for the initial condition.

Such a solution, including the space, $(\symbf X_t)$ and $(\symbf B_t)$ is called a **weak solution** of the Itô SDE.

- A strong solution is also a weak solution.
- A **strong solution** is called **pathwise unique** if for any strong solution $(\symbf Y_t)$, $P(\forall t \in [0, T]: \symbf X_t = \symbf Y_t) = 1$.
- A **weak solution** is called **weakly unique** if in any weak solution $(\symbf Y_t)$ has the same joint distributions.

##### An existence and uniqueness condition ==TODO==

Continue above discussion of the Itô SDE
$$
\dd \symbf X_t = \symbf b(\symbf X_t, t) \dd t + \symbf A(\symbf X_t, t) \dd \symbf B_t,\quad \symbf X_0 = \symbf Z, \quad t \in [0, T]
$$
There exists a pathwise unique strong solution $(\symbf X_t)$ if

- $\symbf b \in C(\R^n \times [0, T] \to \R^n)$ and $\symbf A \in C(\R^n \times [0, T] \to \R^{n \times m})$.
- $\symbf b, \symbf A$ are Lipschitz continuous in $x$ uniformly in $t$, that is
  $$
  \exists L > 0, \forall t \in [0, T], \forall \symbf x, \symbf y \in \R^n:\left \{
  \begin{aligned}
  &\n{\symbf b (\symbf x, t)- \symbf b (\symbf y, t)} \leq L\n{\symbf x-\symbf y} \\
  &\n{\symbf A (\symbf x, t)- \symbf A (\symbf y, t)} \leq L\n{\symbf x-\symbf y}
  \end{aligned}
  \right.
  $$
- $\symbf b, \symbf A$ has linear growth in $x$ uniformly in $t$, that is
  $$
  \exists L > 0, \forall t \in [0, T], \forall \symbf x \in \R^n: \left \{ 
  \begin{aligned}
  &\n{\symbf b (\symbf x, t)} \leq L\p{1 + \n{\symbf x}} \\
  &\n{\symbf A (\symbf x, t)} \leq L\p{1 + \n{\symbf x}}
  \end{aligned}
  \right.
  $$
- $E[\n{\symbf Z}^2] < \infty$.

The solution has the following properties:

- $(\symbf X_t)$ is adapted to completion of $(\G_t) :=\sigma(\symbf Z, \symbf B_{\le t})$.
- $(\symbf X_t)$ has continuous path almost surely.
- $E\s{\int_0^T \n{\symbf X_t}_2^2 \dd t} < \infty$.

#### Brownian Bridge

##### Brownian bridge

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

Then $(X_t) = (B_t - t B_1)$ for $t \in [0, 1]$ is a standard Brownian bridge.

- $X_0 = X_1 = 0$. And $(X_t) \perp (B_t)_{t \ge 1}$.
- Note that $B_t = X_t + tB_1$ construct a BM from the bridge.
- $(X_t)$ is a Gaussian process on $[0, 1]$.
  - $E[X_t] = E[B_t - t B_1] = 0$.
  - $E[X_s X_t] = E[(B_s - sB_1)(B_t - t B_1)] = E[B_s B_t - B_s t B_1 - B_t s B_1 + st B_1^2] = s \wedge t - st$.
  - $\var(X_t) = t(1 - t)$.

