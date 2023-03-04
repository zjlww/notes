#### SDE Reversal ==TODO==

##### Reverse diffusion (David A. Castanon) ==TODO==

Suppose $\sigma(t, x) \in \L([0, T] \times \R^n \to \R^{n \times n})$ and $\mu(t, x) \in \L([0, T] \times \R^n \to \R^n)$.

- Denote the **matrix function** $A(t, x) = \sigma(t, x) \sigma^T(t, x) = 2a(t, x)$.

Consider SDE: $dX_t = \sigma(t, X_t) dB_t + \mu(t, X_t)dt, (*)$ on $t \in [0, T]$.

- Given $(\Omega, \F, P)$ and $(B_t)$ a $\R^m$ valued standard BM.
- Define $\F_\infty^B = \sigma(B_t^{(j)}, 1 \le j \le m, t \in [0, T])$.
- Given $Z \in \L^2(\Omega \to \R^n, P)$ where $Z \perp \F_\infty^B$. Define $\F_t = \sigma(Z, B_{\le t}) \le \F_t$.
- Suppose $\mu$ and $\sigma$ also satisfies (**Strong condition**).

In the filtered space $(\Omega, \F, (\F_t), [0, T], P)$, we have the following:

- There exists $(X_t) \in \V_c(T)$ that is a **strong solution** to the SDE.
- $(X_t)$ is **pathwise unique** in $\V_c(T)$. All weak solutions of the SDE are **weakly unique**.
- And $(X_t)$ is Markov with respect to $(\F_t)$.
- Define the **backward filtration** $\G_t := \sigma(X_s, t \le s \le T)$.

Further assume the (**partial**) following properties (A. Castanon):

- $\mu_i$ and $\sigma_{ij}$ are bounded and Lipschitz continuous in $(x, t)$.
- $A_{ij}$ are Holder continuous in $x$.
- $\exists b >0,\forall \xi \in \R^n,\forall (x, t) \in \R^n \times [0, T]: \sum_{i, j = 1}^n A_{ij}(t, x)\xi_i \xi_j \ge b\|\xi\|^2$.
- $\part \mu_l /\part x_i$, $\part \sigma_{lk} / \part x_i$, and $\part^2 \sigma_{lk} / \part x_i \part x_j$ are locally bounded and locally Lipschitz continuous in $(x, t)$.
- Define the backward filtration $\G_t := \sigma(x_t, x_s, t \le s \le T)$.

These guarantees the forward equation is well-defined, and has a unique solution described by $p(t, x)$ continuously differentiable in $x$.

- There exists $(\overline B_t)_{t \in [0, T]}$ that is a standard Brownian motion independent of $X_T$.

- $\G_t = \sigma(B_s, X_T, t \le s \le T)$.

- The following is true with probability one.
  $$
  \forall t \in [0, T]: X_t - X_T = \int_T^t \bar \mu(s, X_s) ds + \int_T^t \sigma(s, X_s) d\overline B_s
  $$

- The function $\bar \mu(t, x)$ is given by:
  $$
  \begin{aligned}
  \bar \mu(t, x) & = \mu(t, x) - \frac{1}{p(t, x)} \sum_{j = 1}^n \frac{\part}{\part x_j} \left (A_{\cdot j}(t, x) p(t, x) \right)\\
  & = \mu(t, x) - \frac{1}{p(t, x)} \sum_{j = 1}^n \part_j A_{\cdot j}(t, x) p(t, x) - \frac{1}{p(t, x)} \sum_{j = 1}^n A_{\cdot j}(t, x) \part_j p(t, x)\\
  & = \mu(t, x) - \sum_{j = 1}^n \part_j A_{\cdot j}(t, x) - \sum_{j = 1}^n A_{\cdot j}(t, x) \part_j \log p(t, x)\\
  & = \mu(t, x) - A(t, x)\nabla_x - A(t, x) \nabla_x \log p(t, x)
  \end{aligned}
  $$
  where $A(t, x) \nabla_x = A(t, x) (\part_1, \ldots, \part_n)^T = \sum_{j = 1}^n \part_j A_{\cdot j}(t, x)$.

