#### Stochastic Differential Equations

##### Stochastic differential equations

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\mathbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Suppose

- Random variable $\mathbf Z \in \L(\Omega \to \R^n)$ is independent of $(\mathbf B_t)$.
- $\mathbf b \in \L(\R^n \times [0, T] \to \R^n)$ and $\mathbf A \in \L(\R^n \times [0, T] \to \R^{n \times m})$ are deterministic functions.

An Itô stochastic differential equation (SDE) is of the form
$$
\dd \mathbf X_t = \mathbf b(\mathbf X_t, t) \dd t + \mathbf A(\mathbf X_t, t) \dd \mathbf B_t,\quad \mathbf X_0 = \mathbf Z, \quad t \in [0, T]
$$
A non-anticipating $\R^n$-valued stochastic process $(\mathbf X_t) \in \bL_{c}(0, T)$ is a **(strong) solution** of the Itô SDE if

- $(\mathbf X_t)$ satisfies $P(\mathbf X_0 = \mathbf Z) = 1$, and
  $$
  \forall t \in [0, T]: P\p{\mathbf X_t = \mathbf X_0 + \int_0^t \mathbf b(\mathbf X_s, s) \dd s + \int_0^t \mathbf A(\mathbf X_s, s) \dd \mathbf B_s} = 1
  $$
- $\mathbf b(\mathbf X_t, t) \in \bA_{1, (n)}(0, T)$ and $\mathbf A(\mathbf X_t, t) \in \bA_{2, (n \times m)}(0, T)$ such that the integrals are well defined.
- A strong solution exists on the filtered space where the given Brownian motion exists.

We can relax the requirements in the following way:

- $(\mathbf X_t)$ can exists on a **different** filtered space with a **different** standard Brownian motion $(\mathbf B_t)$.
- Only $\mathbf X_0 \sim \mathbf Z$ in distribution is required for the initial condition.

Such a solution, including the space, $(\mathbf X_t)$ and $(\mathbf B_t)$ is called a **weak solution** of the Itô SDE.

- A strong solution is also a weak solution.
- A **strong solution** is called **pathwise unique** if for any strong solution $(\mathbf Y_t)$, $P(\forall t \in [0, T]: \mathbf X_t = \mathbf Y_t) = 1$.
- A **weak solution** is called **weakly unique** if in any weak solution $(\mathbf Y_t)$ has the same joint distributions.

##### An existence and uniqueness condition ==TODO==

Continue above discussion of the Itô SDE
$$
\dd \mathbf X_t = \mathbf b(\mathbf X_t, t) \dd t + \mathbf A(\mathbf X_t, t) \dd \mathbf B_t,\quad \mathbf X_0 = \mathbf Z, \quad t \in [0, T]
$$
There exists a pathwise unique strong solution $(\mathbf X_t)$ if

- $\mathbf b \in C(\R^n \times [0, T] \to \R^n)$ and $\mathbf A \in C(\R^n \times [0, T] \to \R^{n \times m})$.
- $\mathbf b, \mathbf A$ are Lipschitz continuous in $x$ uniformly in $t$, that is
  $$
  \exists L > 0, \forall t \in [0, T], \forall x, y \in \R^n:\left \{
  \begin{aligned}
  &\n{\mathbf b (x, t)- \mathbf b (y, t)} \leq L\n{x-y} \\
  &\n{\mathbf A (x, t)- \mathbf A (y, t)} \leq L\n{x-y}
  \end{aligned}
  \right.
  $$
- $\mathbf b, \mathbf A$ has linear growth in $x$ uniformly in $t$, that is
  $$
  \exists L > 0, \forall t \in [0, T], \forall x \in \R^n: \left \{ 
  \begin{aligned}
  &\n{\mathbf b (x, t)} \leq L\p{1 + \n{x}} \\
  &\n{\mathbf A (x, t)} \leq L\p{1 + \n{x}}
  \end{aligned}
  \right.
  $$
- $E[\n{\mathbf Z}^2] < \infty$.

The solution has the following properties:

- $(\mathbf X_t)$ is adapted to completion of $(\G_t) :=\sigma(\mathbf Z, \mathbf B_{\le t})$.
- $(\mathbf X_t)$ has continuous path almost surely.
- $E\s{\int_0^T \n{\mathbf X_t}_2^2 \dd t} < \infty$.

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

