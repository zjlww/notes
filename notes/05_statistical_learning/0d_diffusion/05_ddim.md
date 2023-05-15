#### Denoising Diffusion Implicit Models

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

The DDPM forward diffusion is a special case of the DDIM forward diffusion.

When viewing $(\rho_n)$ as fixed, solve for parameters $a_n, b_n$ such that the marginals matches with DDPM:
$$
\forall 1 \le n \le T: \symbf X_n \sim \mathcal N\p{\sqrt{\bar \alpha_n} \symbf x_0, (1 - \bar \alpha_n) \bI_d}
$$
And it turns out that:
$$
\forall n \ge 2: a_n = \frac{\sqrt{1 - \bar \alpha_{n - 1} - \rho_n^2}}{\sqrt{1 - \bar \alpha_n}};\quad b_n = \sqrt{\bar \alpha_{n - 1}} - a_n \sqrt{\bar \alpha_n};\quad \rho_n^2 \in [0, 1 - \bar \alpha_{n - 1}]
$$
Therefore, define:
$$
\mu_n(\symbf x_n, \symbf x_0) := b_n \symbf x_0 + a_n \symbf x_n = \sqrt{\bar{\alpha}_{n-1}}\symbf  x_0+\sqrt{1-\bar{\alpha}_{n-1}-\rho_n^2} \cdot \frac{\symbf x_n-\sqrt{\bar{\alpha}_n} \symbf x_0}{\sqrt{1-\bar{\alpha}_n}}
$$
Then we have:
$$
q_\rho\p {\symbf x_{n-1} | \symbf  x_n, \symbf x_0}= \mathcal N \p{\symbf x_{n-1} ; \mu_n\p{\symbf x_n, \symbf x_0}, \rho_n^2 \bI_d}
$$

When taking $\rho_n^2 = \tilde \beta_n$, $q_\rho\p {\symbf x_{n-1} | \symbf  x_n, \symbf x_0}$ is equivalent to the DDPM case. Thus DDIM is a generalization of DDPM.

- In the DDIM paper, the author tried the definition $(\rho_n^2)_{n = 1}^T = (\eta^2 \tilde \beta_n)$. And the deterministic sampler $\eta = 0$ worked the best.

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

Similar to DDPM, there is the problem of picking the variance here. Taking $\rho_\theta(\symbf x_n, n) = \rho_n^2 \bI$ is the optimal choice for $p_0(\symbf x_0) = \delta(\symbf x_0 - \symbf c_0)$.

Now suppose $D_\theta(\symbf x_n, n)$ is a neural network, and define:
$$
\mu_\theta(\symbf x_n, n) := \mu_n(\symbf x_n, D_\theta(\symbf x_n, n))
$$

According to the analytical KL-divergence of isotropic Gaussians:
$$
\d{q(\symbf x_{n - 1} | \symbf x_n, \symbf x_0)}{p_\theta(\symbf x_{n - 1} | \symbf x_n)} = \frac{b_n^2}{2 \rho_n^2} \norm{D_\theta(\symbf x_n, n) - \symbf x_0}_2^2 + \const
$$
So the ELBO is still denoising score matching over multiple scales.

##### Deterministic DDIM

Consider the limiting case where $\rho_n \downarrow 0$ for all $n \in \c{1, \ldots, T}$, in this case, the DDIM sampler becomes deterministic given $\symbf x_T$.
$$
a_n = \frac{\sqrt{1 - \bar \alpha_{n - 1}}}{\sqrt{1 - \bar \alpha_n}}; \quad b_n = \sqrt{\bar \alpha_{n - 1}} - a_n \sqrt{\bar \alpha_n}
$$
For convenience, define $E_\theta(\symbf x_n, n)$ for $n \ge 1$ as following:
$$
\symbf x_n := \sqrt{1-\bar \alpha_n} E_\theta(\symbf x_n, n) + \sqrt{\bar \alpha_n} D_\theta(\symbf x_n, n)
$$
Therefore:
$$
E_\theta(\symbf x_n, n) := \frac{\symbf x_n - \sqrt{\bar \alpha_n} D_\theta(\symbf x_n, n)}{\sqrt{1 - \bar \alpha_n}},\quad D_\theta(\symbf x_n, n) = \frac{\symbf x_n - \sqrt{1 -\bar \alpha_n} E_\theta(\symbf x_n, n)}{\sqrt{\bar \alpha_n}}
$$
The iteration rule is:
$$
\begin{aligned}
\symbf x_{n - 1} & = a_n \symbf x_n + b_n D_\theta(\symbf x_n, n) = \frac{\sqrt{1 - \bar \alpha_{n - 1}}}{\sqrt{1 - \bar \alpha_n}} \symbf x_n + \c{\sqrt{\bar \alpha_{n - 1}} - \frac{\sqrt{1 - \bar \alpha_{n - 1}}}{\sqrt{1 - \bar \alpha_n}} \sqrt{\bar \alpha_n}} D_\theta(\symbf x_n, n)\\
& = \sqrt{\bar \alpha_{n - 1}} D_\theta(\symbf x_n, n) + \sqrt{1 - \bar \alpha_{n - 1}} E_\theta(\symbf x_n, n)
\end{aligned}
$$

Define $t_n = \sqrt{1 - \bar \alpha_n } / \sqrt{\bar \alpha_n}$. Notice that:
$$
\begin{aligned}
\frac{\symbf x_{n - 1}}{\sqrt{\bar \alpha_{n - 1}}} & = D_\theta(\symbf x_n, n) + \frac{\sqrt{1 - \bar \alpha_{n - 1}}}{\sqrt{\bar \alpha_{n - 1}}} E_\theta(\symbf x_n, n)\\
& = \frac{\symbf x_n}{\sqrt{\bar \alpha_n}} +\c{\frac{\sqrt{1 - \alpha_{n - 1}}}{\sqrt{\bar \alpha_{n - 1}}} - \frac{\sqrt{1 - \bar \alpha_n}}{\sqrt{\bar \alpha_n}}} E_\theta(\symbf x_n, n)\\
& = \frac{\symbf x_n}{\sqrt{\bar \alpha_n}} + \c{t_{n - 1} - t_n} \frac{\symbf x_n / \sqrt{\bar \alpha_n} - D_\theta(\symbf x_n, n)}{t_n}
\end{aligned}
$$

This is the discretization of the following ODE, which is the probability flow ODE of the driftless diffusion with $\sigma(t) = t$ and $s(t) = 1$ in EDM:
$$
\dot {\symbf x}(t) =  \frac{\symbf x(t) - D(\symbf x(t), t)}{t}
$$
