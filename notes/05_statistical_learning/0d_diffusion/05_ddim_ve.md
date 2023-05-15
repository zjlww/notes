#### Denoising Diffusion Implicit Models: Variance Explosion

Similar to `DDPM: Variance Explosion` we now derive a version of DDIM without scaling $\symbf x_0$.

> Song, J., Meng, C., & Ermon, S. (2020). Denoising Diffusion Implicit Models. *ArXiv, abs/2010.02502*.

##### DDIM forward diffusion

Let $(\symbf Z_n)_{n = 1}^{T} \sim_{\iid} \mathcal N(\symbf 0, \bI_d)$ be $T$ independent gaussian random variables. Define $(\symbf X_{n})_{n = 1}^T$ recursively when given $\symbf x_0$.
$$
\symbf X_T \sim \mathcal N(\symbf 0, \symbf I_d), \quad \symbf X_{n - 1} = a_n \symbf X_{n} + b_n \symbf x_0 + \rho_n \symbf Z_n, \quad 1 \le n \le T
$$
$(a_n)_{n = 1}^T, (b_n)_{n = 1}^T$ and $(\rho_n)_{n = 1}^T$ are positive real parameters of the model. We require that $b_1 = 1$ and $a_1 = \rho_1 = 0$.

Suppose $q$ is the joint density function of $(\symbf X_1, \ldots, \symbf X_T)$, then for $n \ge 2$:
$$
q(\symbf x_{n - 1} | \symbf x_n, \symbf x_0) = \mathcal N(\symbf x_{n - 1};a_n \symbf x_n + b_n \symbf x_0, \rho_n^2 \bI_d)
$$

##### DDIM forward diffusion generalizes DDPM

The DDPM(VE) forward diffusion is a special case of the DDIM(VE) forward diffusion.

When viewing $(\rho_n)$ as fixed, solve for parameters $a_n, b_n$ such that the marginals matches with DDPM(VE):
$$
\forall 1 \le n \le T: \symbf X_n \sim \mathcal N\p{\symbf x_0, \sigma_n^2 \bI}
$$
And it turns out that for $n \in \c{2, \ldots, T}$:
$$
a_n = \sqrt{\frac{\sigma_{n - 1}^2 - \rho_n^2}{\sigma_n^2}}; \quad b_n = 1 - a_n;\quad \rho_n^2 \in [0, \sigma_{n - 1}^2]
$$
Therefore, define:
$$
\mu_n(\symbf x_n, \symbf x_0) := b_n \symbf x_0 + a_n \symbf x_n = (1 - a_n) \symbf x_0 + a_n \symbf x_n
$$
Then we have:
$$
q_\rho\p {\symbf x_{n-1} | \symbf  x_n, \symbf x_0}= \mathcal N \p{\symbf x_{n-1} ; \mu_n\p{\symbf x_n, \symbf x_0}, \rho_n^2 \bI_d}
$$

When taking $\rho_n^2 = \tilde \beta_n$, $q_\rho\p {\symbf x_{n-1} | \symbf  x_n, \symbf x_0}$ is equivalent to the DDPM(VE) case. Thus DDIM(VE) is a generalization of DDPM(VE).

##### ELBO of DDIM

Similar to DDPM, the ELBO of DDIM is the sum of denoising score matching terms. Thus DDIM is a discrete diffusion sampler.
$$
\begin{aligned}
\L_\theta(\symbf x_0) & = E \s{\log p_\theta(\symbf x_0 | \symbf X_{1..T})} - \d{q(\symbf x_{1..T} | \symbf x_0)}{p_\theta(\symbf x_{1..T})}\\
& = E\s{\log p_\theta(\symbf x_0| \symbf X_1) - \sum_{n = 2}^T \d{q(\symbf x_{n - 1} | \symbf X_n, \symbf x_0)}{p_\theta(\symbf x_{n - 1} | \symbf X_n)}} + \const
\end{aligned}
$$
Consider the following restricted sampler formulation. $p_\theta(\symbf x_T) = \mathcal N(\symbf x_T; \symbf 0, \bI_n)$. For $p_\theta(\symbf x_{n - 1} | \symbf x_n)$, $n \ge 2$ consider:
$$
p_\theta(\symbf x_{n - 1} |\symbf x_n) = \mathcal N(\symbf x_{n - 1}; \mu_\theta(\symbf x_n, n), \rho_\theta(\symbf x_n, n))
$$

Similar to DDPM, there is the problem of picking the variance here. Taking $\rho_\theta(\symbf x_n, n) = \rho_n^2 \bI$ is the optimal choice for $q_0(\symbf x_0) = \delta(\symbf x_0 - \symbf c_0)$.

Now suppose $D_\theta(\symbf x_n, n)$ is a neural network, and define:
$$
\mu_\theta(\symbf x_n, n) := \mu_n(\symbf x_n, D_\theta(\symbf x_n, \sigma_n))
$$

According to the analytical KL-divergence of isotropic Gaussians:
$$
\d{q(\symbf x_{n - 1} | \symbf x_n, \symbf x_0)}{p_\theta(\symbf x_{n - 1} | \symbf x_n)} = \frac{b_n^2}{2 \rho_n^2} \norm{D_\theta(\symbf x_n, \sigma_n) - \symbf x_0}_2^2 + \const
$$
So the ELBO is still denoising score matching over multiple scales.

##### Deterministic DDIM

Consider the limiting case where $\rho_n \downarrow 0$ for all $n \in \c{1, \ldots, T}$, in this case, the DDIM sampler becomes deterministic given $\symbf x_T$.
$$
a_n = \sqrt{\gamma_n} = \frac{\sigma_{n - 1}}{\sigma_n};\quad b_n = 1 - \sqrt{\gamma_n} = \frac{\sigma_{n} - \sigma_{n - 1}}{\sigma_n}
$$
The iteration rule is:
$$
\symbf x_{n - 1} = (1 - b_n) \symbf x_n + b_n D_\theta(\symbf x_n, \sigma_n) = \symbf x_n + \frac{\p{D_\theta(\symbf x_n, \sigma_n) - \symbf x_n}}{\sigma_n} \p{\sigma_n - \sigma_{n - 1}}
$$
This is the discretization of the following ODE, which is the probability flow ODE of the driftless diffusion with $\rho(t) = t$ and $s(t) = 1$ in EDM:
$$
\dot {\symbf x}(t) =  \frac{\symbf x(t) - D_\theta(\symbf x(t), t)}{t}
$$
