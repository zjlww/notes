#### Distributions and Stochastic Differential Equations

> Särkkä, S., & Solin, A. (2019). Applied Stochastic Differential Equations.
>
> "The solutions of SDEs are stochastic processes, and therefore their solutions have certain probability distributions and statistics."

##### Strong assumptions

We will be working under following assumptions in this section.

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\mathbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Consider an Itô stochastic differential equation (SDE) is of the form

$$
\dd \mathbf X_t = \mathbf b(\mathbf X_t, t) \dd t + \mathbf A(\mathbf X_t, t) \dd \mathbf B_t,\quad \mathbf X_0 = \mathbf Z, \quad t \in [0, T]
\label{equ:forward_sde}
$$

- For $R=(r_{ij}), S = (s_{ij}) \in \R^{n \times n}$, define $R:S := \sum_{ij} r_{ij} s_{ij}$.
- Define $\mathbf C(\mathbf x, t): \R^n \times [0, T] \to \R^{n \times n}$ as
  $$
  \mathbf C(\mathbf x, t) := \frac{1}{2}\mathbf A(\mathbf x, t) \mathbf A^T(\mathbf x, t)
  $$

We will make the following **strong assumptions** in the following derivations.

- $\mathbf b \in C(\R^n \times [0, T] \to \R^n)$ and $\mathbf A \in C(\R^n \times [0, T] \to \R^{n \times m})$ satisfies the strong conditions.
- Existence and uniqueness of the strong solution. Weak uniqueness of weak solutions.
- The strong solution $(\mathbf X_t)$ is **Markov** with respect to $(\F_t)$.
- Existence of $C^2$ Markov transition densities.
  - For $t > s$, we have $C^2(\R^n \times [0, T] \to [0, \infty))$ conditional density $p_{t, s}(\mathbf x_t|\mathbf x_s)$.
  - Denote $E^{\mathbf x, s}$ for $E[\cdot | \mathbf X_{s} = \mathbf x]$ and $P^{\mathbf x, s}$ for $P(\cdot | \mathbf X_s = \mathbf x)$.
- Consistent of the transition density with an local SDE IVP for all constant $(\mathbf x, s) \in \R^n \times [0, T]$.
  $$
  \dd \mathbf X_{t + s} = \mathbf b(\mathbf X_{t + s}, t + s) \dd s + \mathbf A(\mathbf X_{t + s}, t + s) \dd \mathbf B_s,\quad \mathbf X_s = \mathbf x, \quad t \in [s, T]
  $$

##### Generalized generators of Itô SDEs

The **generalized generator** $\A$ of the Itô SDE is an operator on $\D :=C_c^\infty(\R^n \times [0, T] \to \R)$.

Consider $f(\mathbf x, t) \in \D$.

- Define $\nabla f(\mathbf x, t) := (D_{x_i} f(\mathbf x, t))_{i = 1}^n$, and $\nabla^2 f(\mathbf x, t) := (D_{x_i, x_j} f (\mathbf x, t))_{1 \le i, j \le n}$.
- Define $f'(\mathbf x, t) := D_t f(\mathbf x, t)$. We will keep using prime for time derivatives in the following.
- For convenient, we abbreviate the arguments $(\mathbf X_t, t)$ in most functions.

$$
\begin{aligned}
\dd f(\mathbf X_t, t) & = f' \dd t + \nabla f \cdot\dd \mathbf X_t + \nabla^2 f : \mathbf C\, \dd t\\
& = f' \dd t + \nabla f \cdot \p{\mathbf b \, \dd t + \mathbf A \, \dd \mathbf B_t} + \nabla^2 f: \mathbf C \dd t\\
& = \p{f' + \nabla f \cdot \mathbf b + \nabla^2 f : \mathbf C} \dd t + \nabla f \cdot \mathbf A \dd \mathbf B_t
\end{aligned}
$$

Therefore we have:

$$
\begin{aligned}
\A f(\mathbf x, t) & := \lim_{\tau \downarrow 0}\frac{E^{\mathbf x, t}[f(\mathbf X_{t + \tau}, t + \tau)] - f(\mathbf x, t)}{\tau}\\
& = \lim_{\tau \downarrow 0} \int_{\Omega} \frac{f(\mathbf X_{t + \tau},t + \tau) - f(\mathbf X_{t}, t)}{\tau} \dd P^{\mathbf x, t}(\omega)\\
& = \lim_{\tau \downarrow 0} \int_{\Omega}\frac{1}{\tau}\s{\int_t^{t + \tau} \p{f'(\mathbf X_{t + \tau}, t + \tau) + \nabla^T f(\cdot) \, \mathbf b(\cdot) + \nabla^2 f(\cdot) : \mathbf C(\cdot)} \dd \tau} \dd P^{\mathbf x, t}(\omega)\\
& = {f'(\mathbf x, t) + \nabla^T f(\mathbf x, t) \, \mathbf b(\mathbf x, t) + \nabla^2 f(\mathbf x, t) : \mathbf C(\mathbf x, t)}
\end{aligned}
$$

##### Generators of Itô SDEs

The generator also dented by $\A_t$ of the Itô SDE is an operator on $\mathcal D := C_c^\infty(\R^n \to \R)$.

Consider $f(\mathbf x) \in \D$. And we adopt previous conventions.
$$
\dd f(\mathbf X_t)  = \p{\nabla^T f \, \mathbf b + \nabla^2 f : \mathbf C} \dd t + \nabla^T f \mathbf A \,\dd \mathbf B_t
\label{generator}
$$
Therefore we have,
$$
\A_t f(\mathbf x) := \lim_{\tau \downarrow 0}\frac{E^{\mathbf x, t}[f(\mathbf X_{t + \tau})] - f(\mathbf x)}{\tau} = \nabla^T f(\mathbf x) \, \mathbf b(\mathbf x, t) + \nabla^2 f(\mathbf x) : \mathbf C(\mathbf x, t)
$$

Define the dual operator of $\mathcal A_t$ as $\mathcal A_t^*$ on $\mathcal D'$.
$$
\mathcal A^*_t p(\mathbf x) := \mathbf \nabla \cdot \p{\mathbf b(\mathbf x, t) p(\mathbf x)} + \nabla^2 : \p{\mathbf C(\mathbf x, t) p(\mathbf x)}
$$

##### Fokker-Planck Kolmogorov equation of Itô SDEs

Suppose that for $t \in [0, T]$, we have $C^2(\R^n \times [0, T] \to [0, \infty))$ density $p_{t}(\mathbf x_t)$.

For any $f \in \D = C_c^\infty(\R^n \to \R)$ we have equation $\ref{generator}$ therefore
$$
f(\mathbf X_{t + \tau}) - f(\mathbf X_{t}) = \int_t^{t + \tau} \p{\nabla f(\mathbf X_{u}, u) \cdot \mathbf b(\cdot) + \nabla^2 f(\cdot): \mathbf C(\cdot)} \dd t +\nabla f(\cdot) \cdot \mathbf A(\cdot) \dd \mathbf B_u
$$
Following assumptions $\nabla^T f(\mathbf X_t, t) \mathbf A(\mathbf X_t, t) \dd \mathbf B_t$ is a martingale with zero expectation. So

$$
\begin{aligned}
E\s{f(\mathbf X_{t + \tau}) - f(\mathbf X_{t})} & = E\s{\int_t^{t + \tau} \p{\nabla f(\mathbf X_{u}) \cdot \mathbf b(\mathbf X_u, u) + \nabla^2 f(\mathbf X_u): \mathbf C(\mathbf X_u, u)} \dd u}\\
& = \int_t^{t + \tau} E\s{\nabla f(\mathbf X_{u})\cdot \mathbf b(\mathbf X_u, u)} + E\s{\nabla^2 f(\mathbf X_u): \mathbf C(\mathbf X_u, u)} \dd u
\end{aligned}
\label{equ:expectation_difference}
$$
Consider the first term, apply Fubini's theorem + integral by parts.
$$
\begin{aligned}
E\s{\nabla^T f(\mathbf X_{u}) \mathbf b(\mathbf X_u, u)} & = \int_{\R^n} \nabla f(\mathbf x)\cdot \mathbf b(\mathbf x, u) p_u(\mathbf x) \dd \mathbf x\\
& = \int_{\R^n} f(\mathbf x) \nabla\cdot(\mathbf b(\mathbf x, u) p_u(\mathbf x)) \dd \mathbf x
\end{aligned}
$$
Similarly for the second term, apply Fubini's theorem + integral by part twice.
$$
\begin{aligned}
E\s{\nabla^2 f(\mathbf X_u): \mathbf C(\mathbf X_u, u)} & = \int_{\R^n} \nabla^2 f(\mathbf x):(\mathbf C(\mathbf x, u)p_u(\mathbf x)) d\mathbf x\\
& = \int_{\R^n} f(\mathbf x) \nabla^2:(\mathbf C(\mathbf x, u)p_u(\mathbf x))\dd \mathbf x
\end{aligned}
$$
Now consider equation $\ref{equ:expectation_difference}$, the expectations are continuous in $u$, therefore
$$
\begin{aligned}
\lim_{\tau \downarrow 0} E\s{\frac{f(\mathbf X_{t + \tau}) - f(\mathbf X_{t})}{\tau}} & = E\s{\nabla f(\mathbf X_{t})\cdot \mathbf b(\mathbf X_t, t)} + E\s{\nabla^2 f(\mathbf X_t): \mathbf C(\mathbf X_t, t)}\\
& = \int_{\R^n} f(\mathbf x) \c{ \nabla\cdot(\mathbf b(\mathbf x, t) p_t(\mathbf x)) + \nabla^2:(\mathbf C(\mathbf x, t)p_t(\mathbf x))} \dd \mathbf x
\end{aligned}
$$
By assumptions, it is legal to swap the differential and integral here:
$$
D_t E[f(\mathbf X_t)] = E[D_t f(\mathbf X_t)] = D_t\int_{\R^n} f(\mathbf x) p_t(\mathbf x) \dd \mathbf x = \int_{\R^n} f(\mathbf x) p'_t(\mathbf x) \dd \mathbf x
$$
Therefore we have
$$
\forall f(\mathbf x) \in \D: \int_{\R^n} f(\mathbf x) p'_t(\mathbf x) \dd \mathbf x = \int_{\R^n} f(\mathbf x) \A^* p(\mathbf x) \dd \mathbf x
$$
Therefore $p_t(\mathbf x)$ satisfies the following **FPK PDE**:
$$
p'_t(\mathbf x) = \A^* p(\mathbf x),\quad  t \in [0, T]
$$

##### Weak-sense time reversal of SDEs

> I do not have enough weapons to prove the more general result proved in the following paper.
>
> Castañón, D.A. (1982). Reverse-time diffusion processes. *IEEE Trans. Inf. Theory, 28*, 953-956.
>
> For now, I can demonstrate a weaker result with restricted generality.

Suppose $(\wbar\Omega, \wbar\F, (\wbar\F_t), T = [T, 0], P)$ is a complete filtered probability space. Let $(\mathbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Consider the following class of reverse-time SDE. We would like to find $\mathbf {\wbar b}(\mathbf x, t)$ that gives an appropriate time reversal SDE.
$$
\dd \mathbf {\wbar X}_t = \mathbf {\wbar b}(\mathbf {\wbar X}_t, t) \dd t + \lambda \mathbf {{A}}(\mathbf {\wbar X}_t, t) \dd \mathbf {\wbar {B}}_t,\quad \mathbf{\wbar X}_T = \mathbf X_T, \quad t \in [T, 0]
$$
Recall that the forward SDE has FPK equation.
$$
p'_t(\mathbf x) = D_i \p{\mathbf b^{(i)}(\mathbf x, t) p_t(\mathbf x)} + D_{ij} \p{\mathbf C^{(i,j)}(\mathbf x, t) p_t(\mathbf x)}, \quad t \in [0, T]
$$
Notice that the backward SDE has FPK equation, the sign is **flipped** due to time reversal.
$$
p_t'(\mathbf x) = -D_i \p{{\mathbf {\wbar b}}^{(i)}(\mathbf x, t) p_t(\mathbf x)} - \lambda^2 D_{ij} \p{\mathbf C^{(i, j)}(\mathbf x, t) p_t(\mathbf x)}, \quad t \in [0, T]
$$
To achieve weak-sense time reversal, we need the two FPK equations to be equal. Assuming that $p_t(\mathbf x) > 0$ on $\R^n$,
$$
\begin{aligned}
{{\mathbf {\wbar b}}^{(i)}(\mathbf x, t)} & = -{\mathbf b^{(i)}(\mathbf x, t)} - \frac{(1 + \lambda^2)}{p_t(\mathbf x)} D_{j}\p{\mathbf C^{(i,j)}(\mathbf x, t) p_t(\mathbf x)}\\
& = -{\mathbf b^{(i)}(\mathbf x, t)} - (1 + \lambda^2) \p{D_j \mathbf C^{(i, j)}(\mathbf x, t) + \mathbf C^{(i, j)}(\mathbf x, t)D_j \log p_t(\mathbf x)}
\end{aligned}
$$
Notice that for $\lambda = 0$, this gives the reverse **probability flow ODE**.

