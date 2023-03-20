#### Score-based Generative Modeling Through SDEs

##### Simple diffusion

Consider probability space $(\Omega, \F, P)$ and time interval $[0, T]$.

- Suppose $X_0 \sim p_0(x)$ and is **independent** of the Brownian motion $(B_t)$.
- The revertible **forward SDE** model proposed by Song.
  - Suppose $\mu(t, x) \in \L([0, T] \times \R^n \to \R^n)$ and $g(t) \in \L(\R \to (0, \infty))$.
  - Define $\sigma(t, x) = g(t) I$ where $I \in \R^n$.
  - The **forward SDE**: $dX_t = g(t) dB_t + \mu(t, X_t) dt$ where $t \in [0, T]$.
- Suppose the forward SDE is revertible, then by (**Reverse diffusion**). We have the **backward SDE**:
  - $dX_t = (\mu(t, X_t) - g^2(t) \nabla \log p_t(X_t)) dt + g(t) d\bar B_t$.
  - Where $t \in [T, 0]$, the ordering on time is inverted.
- $\nabla \log p_t(x_t)$ is estimated by time dependent score network $s_\theta(x_t, t)$ by **score matching**.
  - By (**Denoising score matching**), $s_\theta(x_t, t)$ is trained with following objective: $$
    \L_\theta = E_{t \sim U[0, T]} \left \{
    \lambda(t) E_{p_{\data}} E_{p_{0t}(x_t|x_0)} \norm{s_\theta(x_t, t) - \nabla_{x_t}\log p_{0t}(x_t | x_0)}^2_2
    \right\}$$
  - As in DDPM and SMLD, Song propose to use $\lambda(t) \propto 1/E\norm{\nabla_{x_t} \log p_{0t}(x_t|x_0)}_2^2$.

##### General diffusion

Consider probability space $(\Omega, \F, P)$ and time interval $[0, T]$.

- Suppose $X_0 \sim p_0(x)$ and is **independent** of the Brownian motion $(B_t)$.
- The revertible **forward SDE** model proposed by Song.
  - Suppose $\mu(t, x) \in \L([0, T] \times \R^n \to \R^n)$ and $\sigma(t, x) \in \L([0, T] \times \R^n \to \R^{n \times n})$.
  - The **forward SDE**: $dX_t = \sigma(t, X_t) dB_t + \mu(t, X_t) dt$ where $t \in [0, T]$.
- Suppose the forward SDE is revertible, then by (**Reverse diffusion**). We have the **backward SDE**:
  - $dX_t = (\mu(t, X_t) - A(t, X_t)\nabla_x - A(t, X_t) \nabla_x \log p(t, x))dt + \sigma(t, X_t) d\bar B_t$.
  - Where $t \in [T, 0]$, the ordering on time is inverted.

##### Conditional generation

Continue from (**Simple diffusion**) or (**General diffusion**).

- Suppose $Y$ is a **discrete** random variable, $Y = c(X_0)$ is the **class label** of $X_0$.
- Suppose $s_\theta(x_t, t)$ is matching $\nabla \log p_t(x_t)$. And we want to sample from $p_0(x_0|y)$ now.
- Notice that the **conditional score** $\nabla_{x_t} \log p_t(x_t | y) = \nabla_{x_t} \log p_t(x_t) + \nabla_{x_t} \log p_t(y | x_t)$.
- With access to $\nabla_x \log p_t(y | x)$, and start from $p_T(x_T | y)$, conditional generation is solved.

##### Imputation

Continue from (**Simple diffusion**). Consider $X_t$ as an image.

- Consider SDE $dX_t = \mu(t, X_t) dt + g(t) dB_t$ for $t \in [0, T]$.

- Suppose $\mu(t, x)$ is component wise, that is $\mu(t, x_1, \ldots, x_n) = (\mu_1(t, x_1),\ldots \mu(t, x_n))$.

- Suppose $X_t = [Y_t, Z_t]$, where $Y_t$ are known pixels, and $Z_t$ are unknown pixels.

  - Suppose $\{k_1, \ldots, k_m\}$ are the indexes of the unknown pixels. And $Z_t^{(s)} = X_t^{(k_s)}$.
  - Therefore $X_t$ is in $\R^n$, $Z_t$ is in $\R^m$ and $Y_t$ is in $\R^{n - m}$.
  - Define $\tilde \mu(t, z)$ as $\tilde \mu(t, z_1, \ldots, z_n) = (\mu_{k_1}(t, z_1), \ldots, \mu_{k_m}(t, z_m))$.
  - Define $\widetilde B_t = (B_t^{(k_1)}, \cdots, B_t^{(k_m)})$ it is a standard BM.

- Recall $p_0(x)$ is the data density.

- Our goal is to sample from conditional density $p_0(z_0 | y_0)$.

- Consider a new SDE $dZ_t = \tilde \mu(t, Z_t) dt + g(t) d \widetilde B_t$.

  - Let $\tilde p_t(z_t)$ be the density of $Z_t$ with initial density $p_0(z_0 | y_0)$.

- Since forward SDE is component wise, $\tilde p_t(z_t) = p_t(z_t | y_0)$. ==TODO==.

  - So $\nabla \log \tilde p_t(z_t) = \nabla_{z_t}\log p_t(z_t | y_0)$.

  - Song et al. propose to approximate this term with following formula:

  $$
    \begin{aligned}
    \nabla \log p_t (z_t | y_0) & = \nabla \log \int_{\R^{n - m}} p_t(z_t | y_t, y_0) p_t(y_t | y_0) dy_t = \nabla \log E_{p_t(y_t | y_0)} p_t(z_t | y_t, y_0)\\
    & \approx \nabla \log E_{p_t(y_t | y_0)} p_t(z_t | y_t) \approx \nabla \log p_t(z_t | \hat y_t)
    \end{aligned}
  $$

  - Where $\hat y_t$ is a random sample from $p_t(y_t | y_0)$.

- See GuidedTTS for a conditional sampling algorithm.

##### Probability flow ODE

Consider from (**General diffusion**).

Recall the **forward SDE**: $dX_t = \sigma(t, X_t) dB_t + \mu(t, X_t) dt$ where $t \in [0, T]$.

> Suppose $p(t, x): [0, T] \times \R^d \to (0, \infty)$ is the twice differentiable density.
>
> $p(t, x)$ satisfies the following **FPK** PDE:
> $$
> \part_t p(t, x) = \L^* p(t, x) = - \nabla \cdot (p(t, x)\mu(t, x)) + \nabla^2 :(p(t, x)a(t, x))
> , \quad t \in [0, T], \quad p(0, x) = p_0(x)
> $$
> where $a(t, x) = \sigma(t, x) \sigma^T(t, x)/2$ is symmetric.

Now proceed with Einstein summation notation. Define the following ODE on $t \in [0, T]$.
$$
f_i(t, x) := \mu_i(t, x) - \part_j a_{ij}(t, x) - a_{ij}(t, x) \part_j\log p(t, x), \quad x'(t) = f(t, x), \quad t \in [0, T]
$$
We claim that this ODE shares the same **FPK equation** as the SDE.
$$
\begin{aligned}
-\part_i (pf_i) & = - \part_i (p\mu_i) + \part_i(p\part_j a_{ij}) + \part_i p a_{ij} \part_j \log p\\ & = -\part_i (p\mu_i) +\part_i (p \part_j a_{ij}) + \part_i a_{ij} \part_j p = -\part_i (p \mu_i) + \part_i \part_j (pa_{ij})
\end{aligned}
$$
Suppose the volatility is linear:
$$
dX_t = \mu(t, X_t) dt + g(t) dB_t , \quad t \in [0, T]
$$

- Denote $f(t, x) = \mu(t, x(t)) - \frac{1}{2}g^2(t) \nabla \log p_t(x)$.
- The **flow ODE** is $x'(t) = f(t, x(t))$.

##### Exact likelihood ==TODO==

Continue from (**Flow ODE**).

- If we want to simultaneously obtain the log-likelihood, we can solve in reverse-time:
  $$
  \frac{d}{d t}\left[\begin{array}{c} 
  x (t) \\
  \log p(t, x (t))
  \end{array}\right]=\left[\begin{array}{c}
  f(t, x (t)) \\
  - \nabla \cdot f(t, x(t))
  \end{array}\right];
  $$

- The term $\nabla \cdot f(t, x)$ can be estimated efficiently (**TODO**).

##### Reference: score of gaussian

Using linear SDE has the following benefit:

The score of Gaussian has closed forms. Consider density $p(x) = \mathcal N(x \mid \mu, \Sigma)$ in $\R^m$.
$$
p(x)=\frac{1}{(2 \pi)^{m / 2}(\operatorname{det} \Sigma)^{1 / 2}} \exp\left[{-\frac{1}{2}{(x-\mu)}^T{\Sigma^{-1}(x-\mu)}}\right]
$$
Therefore
$$
\begin{aligned}
\nabla \log p(x) & = \nabla \left ( -\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu)\right) = -\Sigma^{-1}(x - \mu)\\
\end{aligned}
$$
