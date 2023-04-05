#### Distributions and Stochastic Differential Equations

> Särkkä, S., & Solin, A. (2019). Applied Stochastic Differential Equations.
>
> "The solutions of SDEs are stochastic processes, and therefore their solutions have certain probability distributions and statistics."

##### Strong assumptions

We will be working under following assumptions in this section.

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(\symbf B_t)$ be a **$m$-dimensional standard Brownian motion**.

Consider an Itô stochastic differential equation (SDE) is of the form

$$
\dd \symbf X_t = \symbf b(\symbf X_t, t) \dd t + \symbf A(\symbf X_t, t) \dd \symbf B_t,\quad \symbf X_0 = \symbf Z, \quad t \in [0, T]
\label{equ:forward_sde}
$$

- For $R=(r_{ij}), S = (s_{ij}) \in \R^{n \times n}$, define $R:S := \sum_{ij} r_{ij} s_{ij}$.
- Define $\symbf C(\symbf x, t): \R^n \times [0, T] \to \R^{n \times n}$ as
  $$
  \symbf C(\symbf x, t) := \frac{1}{2}\symbf A(\symbf x, t) \symbf A^T(\symbf x, t)
  $$

We will make the following **strong assumptions** in the following derivations.

- $\symbf b \in C(\R^n \times [0, T] \to \R^n)$ and $\symbf A \in C(\R^n \times [0, T] \to \R^{n \times m})$ satisfies the strong conditions.
- Existence and uniqueness of the strong solution. Weak uniqueness of weak solutions.
- The strong solution $(\symbf X_t)$ is **Markov** with respect to $(\F_t)$.
- Existence of $C^2$ Markov transition densities.
  - For $t > s$, we have $C^2(\R^n \times [0, T] \to [0, \infty))$ conditional density $p_{t, s}(\symbf x_t|\symbf x_s)$.
  - Denote $E^{\symbf x, s}$ for $E[\cdot | \symbf X_{s} = \symbf x]$ and $P^{\symbf x, s}$ for $P(\cdot | \symbf X_s = \symbf x)$.

##### Generalized generators of Itô SDEs

The **generalized generator** $\A$ of the Itô SDE is an operator on $\D :=C_c^\infty(\R^n \times [0, T] \to \R)$.

Consider $f(\symbf x, t) \in \D$.

- Define $\nabla f(\symbf x, t) := (D_{x_i} f(\symbf x, t))_{i = 1}^n$, and $\nabla^2 f(\symbf x, t) := (D_{x_i, x_j} f (\symbf x, t))_{1 \le i, j \le n}$.
- Define $f'(\symbf x, t) := D_t f(\symbf x, t)$. We will keep using prime for time derivatives in the following.
- For convenient, we abbreviate the arguments $(\symbf X_t, t)$ in most functions.

$$
\begin{aligned}
\dd f(\symbf X_t, t) & = f' \dd t + \nabla f \cdot\dd \symbf X_t + \nabla^2 f : \symbf C\, \dd t\\
& = f' \dd t + \nabla f \cdot \p{\symbf b \, \dd t + \symbf A \, \dd \symbf B_t} + \nabla^2 f: \symbf C \dd t\\
& = \p{f' + \nabla f \cdot \symbf b + \nabla^2 f : \symbf C} \dd t + \nabla f \cdot \symbf A \dd \symbf B_t
\end{aligned}
$$

Therefore we have:

$$
\begin{aligned}
\A f(\symbf x, t) & := \lim_{\tau \downarrow 0}\frac{E^{\symbf x, t}[f(\symbf X_{t + \tau}, t + \tau)] - f(\symbf x, t)}{\tau}\\
& = \lim_{\tau \downarrow 0} \int_{\Omega} \frac{f(\symbf X_{t + \tau},t + \tau) - f(\symbf X_{t}, t)}{\tau} \dd P^{\symbf x, t}(\omega)\\
& = \lim_{\tau \downarrow 0} \int_{\Omega}\frac{1}{\tau}\s{\int_t^{t + \tau} \p{f'(\symbf X_{t + \tau}, t + \tau) + \nabla^T f(\cdot) \, \symbf b(\cdot) + \nabla^2 f(\cdot) : \symbf C(\cdot)} \dd \tau} \dd P^{\symbf x, t}(\omega)\\
& = {f'(\symbf x, t) + \nabla^T f(\symbf x, t) \, \symbf b(\symbf x, t) + \nabla^2 f(\symbf x, t) : \symbf C(\symbf x, t)}
\end{aligned}
$$

##### Generators of Itô SDEs

The generator also dented by $\A_t$ of the Itô SDE is an operator on $\mathcal D := C_c^\infty(\R^n \to \R)$.

Consider $f(\symbf x) \in \D$. And we adopt previous conventions.
$$
\dd f(\symbf X_t)  = \p{\nabla^T f \, \symbf b + \nabla^2 f : \symbf C} \dd t + \nabla^T f \symbf A \,\dd \symbf B_t
\label{generator}
$$
Therefore we have,
$$
\A_t f(\symbf x) := \lim_{\tau \downarrow 0}\frac{E^{\symbf x, t}[f(\symbf X_{t + \tau})] - f(\symbf x)}{\tau} = \nabla^T f(\symbf x) \, \symbf b(\symbf x, t) + \nabla^2 f(\symbf x) : \symbf C(\symbf x, t)
$$

Define the adjoint operator of $\mathcal A_t$ as $\mathcal A_t^*$ on $\mathcal D'$.
$$
\mathcal A^*_t p(\symbf x) := - \nabla \cdot \p{\symbf b(\symbf x, t) p(\symbf x)} + \nabla^2 : \p{\symbf C(\symbf x, t) p(\symbf x)}
$$

##### Fokker-Planck Kolmogorov equation of Itô SDEs

Suppose that for $t \in [0, T]$, we have $C^2(\R^n \times [0, T] \to [0, \infty))$ density $p_{t}(\symbf x_t)$.

For any $f \in \D = C_c^\infty(\R^n \to \R)$ we have equation $\ref{generator}$ therefore
$$
f(\symbf X_{t + \tau}) - f(\symbf X_{t}) = \int_t^{t + \tau} \p{\nabla f(\symbf X_{u}, u) \cdot \symbf b(\cdot) + \nabla^2 f(\cdot): \symbf C(\cdot)} \dd t +\nabla f(\cdot) \cdot \symbf A(\cdot) \dd \symbf B_u
$$
Following assumptions $\nabla^T f(\symbf X_t, t) \symbf A(\symbf X_t, t) \dd \symbf B_t$ is a martingale with zero expectation. So

$$
\begin{aligned}
E\s{f(\symbf X_{t + \tau}) - f(\symbf X_{t})} & = E\s{\int_t^{t + \tau} \p{\nabla f(\symbf X_{u}) \cdot \symbf b(\symbf X_u, u) + \nabla^2 f(\symbf X_u): \symbf C(\symbf X_u, u)} \dd u}\\
& = \int_t^{t + \tau} E\s{\nabla f(\symbf X_{u})\cdot \symbf b(\symbf X_u, u)} + E\s{\nabla^2 f(\symbf X_u): \symbf C(\symbf X_u, u)} \dd u
\end{aligned}
\label{equ:expectation_difference}
$$
Consider the first term, apply Fubini's theorem + integral by parts.
$$
\begin{aligned}
E\s{\nabla^T f(\symbf X_{u}) \symbf b(\symbf X_u, u)} & = \int_{\R^n} \nabla f(\symbf x)\cdot \symbf b(\symbf x, u) p_u(\symbf x) \dd \symbf x\\
& = -\int_{\R^n} f(\symbf x) \nabla\cdot(\symbf b(\symbf x, u) p_u(\symbf x)) \dd \symbf x
\end{aligned}
$$
Similarly for the second term, apply Fubini's theorem + integral by part twice.
$$
\begin{aligned}
E\s{\nabla^2 f(\symbf X_u): \symbf C(\symbf X_u, u)} & = \int_{\R^n} \nabla^2 f(\symbf x):(\symbf C(\symbf x, u)p_u(\symbf x)) d\symbf x\\
& = \int_{\R^n} f(\symbf x) \nabla^2:(\symbf C(\symbf x, u)p_u(\symbf x))\dd \symbf x
\end{aligned}
$$
Now consider equation $\ref{equ:expectation_difference}$, the expectations are continuous in $u$, therefore
$$
\begin{aligned}
\lim_{\tau \downarrow 0} E\s{\frac{f(\symbf X_{t + \tau}) - f(\symbf X_{t})}{\tau}} & = E\s{\nabla f(\symbf X_{t})\cdot \symbf b(\symbf X_t, t)} + E\s{\nabla^2 f(\symbf X_t): \symbf C(\symbf X_t, t)}\\
& = \int_{\R^n} f(\symbf x) \c{-\nabla\cdot(\symbf b(\symbf x, t) p_t(\symbf x)) + \nabla^2:(\symbf C(\symbf x, t)p_t(\symbf x))} \dd \symbf x
\end{aligned}
$$
By assumptions, it is legal to swap the differential and integral here:
$$
D_t E[f(\symbf X_t)] = E[D_t f(\symbf X_t)] = D_t\int_{\R^n} f(\symbf x) p_t(\symbf x) \dd \symbf x = \int_{\R^n} f(\symbf x) p'_t(\symbf x) \dd \symbf x
$$
Therefore we have
$$
\forall f(\symbf x) \in \D: \int_{\R^n} f(\symbf x) p'_t(\symbf x) \dd \symbf x = \int_{\R^n} f(\symbf x) \A^* p(\symbf x) \dd \symbf x
$$
Therefore $p_t(\symbf x)$ satisfies the following **Fokker-Planck Equation**:
$$
p'_t(\symbf x) = \A^* p(\symbf x),\quad  t \in [0, T]
$$

##### Weak-sense time reversal of SDEs

> I do not have enough weapons to prove the more general result proved in the following paper.
>
> Castañón, D.A. (1982). Reverse-time diffusion processes. *IEEE Trans. Inf. Theory, 28*, 953-956.
>
> For now, I can demonstrate a weaker result with restricted generality.

Suppose $(\wbar\Omega, \wbar\F, (\wbar\F_t), T = [T, 0], P)$ is a complete filtered probability space. Let $(\wbar {\symbf B}_t)$ be a reverse-time **$m$-dimensional standard Brownian motion** starting at $T$.

Consider the following class of reverse-time SDE. We would like to find $\symbf {\wbar b}(\symbf x, t)$ that gives an appropriate time reversal SDE.
$$
\dd \symbf {\wbar X}_t = \symbf {\wbar b}(\symbf {\wbar X}_t, t) (-\dd t) + \sqrt{\lambda(t)} \symbf {{A}}(\symbf {\wbar X}_t, t) \dd \symbf {\wbar {B}}_t,\quad \symbf{\wbar X}_T = \symbf X_T, \quad t \in [T, 0]
$$
Recall that the forward SDE has FPK equation.
$$
p'_t(\symbf x) = -D_i \p{\symbf b^{(i)}(\symbf x, t) p_t(\symbf x)} + D_{ij} \p{\symbf C^{(i,j)}(\symbf x, t) p_t(\symbf x)}, \quad t \in [0, T]
$$
Notice that the backward SDE has FPK equation, the sign is **flipped** due to time reversal.
$$
p_t'(\symbf x) = D_i \p{-{\symbf {\wbar b}}^{(i)}(\symbf x, t) p_t(\symbf x)} - \lambda(t) D_{ij} \p{\symbf C^{(i, j)}(\symbf x, t) p_t(\symbf x)}, \quad t \in [0, T]
$$
To achieve weak-sense time reversal, we need the two FPK equations to be equal. Assuming that $p_t(\symbf x) > 0$ on $\R^n$,
$$
\begin{aligned}
{{\symbf {\wbar b}}^{(i)}(\symbf x, t)} & = {\symbf b^{(i)}(\symbf x, t)} - \frac{(1 + \lambda(t))}{p_t(\symbf x)} D_{j}\p{\symbf C^{(i,j)}(\symbf x, t) p_t(\symbf x)}\\
& = {\symbf b^{(i)}(\symbf x, t)} - (1 + \lambda(t)) \p{D_j \symbf C^{(i, j)}(\symbf x, t) + \symbf C^{(i, j)}(\symbf x, t)D_j \log p_t(\symbf x)}
\end{aligned}
$$
Notice that for $\lambda(t) = 0$, this gives the reverse **probability flow ODE**.

