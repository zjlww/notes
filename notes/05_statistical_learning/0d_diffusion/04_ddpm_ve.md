#### Denoising Diffusion Probabilistic Models: Variance Explosion

The scaling of $\symbf X_{n - 1}$ slightly complicates the mathematical form of the equations. In this note we derive DDPM without the scaling factor. This simplifies the expressions.

> Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. *ArXiv, abs/2006.11239*.

##### Markov forward diffusion

Suppose $\symbf X_0 \sim p_0(\symbf x)$ is a random variable in $\R^d$ with data distribution.

Consider a sequence of strictly increasing square root of variance $(\sigma_0, \sigma_1, \ldots, \sigma_T)$ where $\sigma_0 = 0$ and $\sigma_T$ is sufficiently large.

Let $(\symbf Z_n)_{n = 1}^{T} \sim_{\iid} \mathcal N(\symbf 0, \bI_d)$ be $T$ independent gaussian random variables.

For $n \in \c{1, \ldots, T}$ define $\beta_n > 0$ as $\beta_n = \sigma_n^2 - \sigma_{n - 1}^2$. Define $(\symbf X_{n})_{n = 1}^T$ recursively as:
$$
\symbf X_n = \sqrt{\beta_n} \symbf Z_n + \symbf X_{n - 1}, \quad n \in \c{1, \ldots, T}
$$
The Markov process $(\symbf X_n)_{n = 0}^T$ is called the **forward diffusion**, which gradually adds noise into $\symbf X_0$.

Suppose $q(\symbf x_0, \ldots, \symbf x_T)$ is the joint density function of $(\symbf X_0, \ldots, \symbf X_T)$. The forward diffusion process has conditional density given by:
$$
q(\symbf x_{1..T}|\symbf  x_0) = \prod_{n=1}^T q(\symbf x_{n} | \symbf x_{n-1}); \quad q(\symbf x_n | \symbf x_{n-1}) = \mathcal N\p{\symbf x_n; \symbf x_{n-1}, \beta_n \bI_d}
$$
The marginal conditional density is given by:
$$
q(\symbf x_n | \symbf x_0) = \mathcal N(\symbf x_n ; \symbf x_0, \sigma_n^2\bI_d)
$$
Therefore for some $\symbf E_n \sim \mathcal N(\symbf 0, \bI_d)$ depending on $(\symbf Z_1, \ldots, \symbf Z_n)$, we have:
$$
\symbf X_n = \sigma_n \symbf E_n + \symbf X_0
$$

##### A posterior of forward diffusion

The posterior density can be derived by Bayes' theorem

$$
q(\symbf{x}_{n-1}|\symbf{x}_{n}, \symbf{x}_0) = \frac{q(\symbf{x}_{n}|\symbf{x}_{n-1}, \symbf{x}_0)q(\symbf{x}_{n-1}|\symbf{x}_0)}{q(\symbf{x}_n|\symbf{x}_0)}
$$

Where we already know:

- $q(\symbf{x}_n | \symbf{x}_{n - 1}, \symbf{x}_0) = q(\symbf{x}_n | \symbf{x}_{n-1}) = \mathcal N(\symbf{x}_n; \symbf{x}_{n-1}, \beta_n \symbf{I})$.
- $q(\symbf{x}_n | \symbf{x}_0) = \mathcal N(\symbf{x}_n ; \symbf{x}_0, \sigma_n^2 \bI)$ and $q(\symbf{x}_{n-1} | \symbf{x}_0) = \mathcal N(\symbf{x}_{n - 1}; \symbf{x}_0, \sigma_{n - 1}^2 \symbf{I})$.

Let $\gamma_n = \sigma_{n - 1}^2 / \sigma_n^2$. The conditional density $q(\symbf x_{n - 1} | \symbf x_n, \symbf x_0), n \in \c{2, \ldots, T}$ has the closed form solution:
$$
\begin{aligned}
q(\symbf{x}_{n - 1} | \symbf{x}_n, \symbf{x}_0) &= \mathcal N\p{\symbf{x}_{n - 1}; \tilde \mu_n(\symbf{x}_n, \symbf{x}_0), \tilde \beta_n I}\\
\tilde \mu_n(\symbf x_n, \symbf x_0) & = \gamma_n \symbf x_n + (1 - \gamma_n) \symbf x_0; \quad \tilde \beta_n = \sigma_{n - 1}^2 (1 - \gamma_n)
\end{aligned}
$$

##### Discretized reverse diffusion

Consider a reverse time Markov process with states in $\R^d$ decomposed as:
$$
p_\theta(\symbf x_0, \ldots, \symbf x_T) = p_\theta(\symbf x_T) \prod_{n = 1}^T p_\theta(\symbf x_{n - 1} | \symbf x_{n}),\quad p_\theta(\symbf x_T) := \mathcal N(\symbf x_T;\symbf 0, \sigma_T^2\bI_d)
$$
this process is also called the **denoising process**.

##### ELBO of DDPM(VE)

Similar to DDPM, the form of the ELBO is the same:
$$
\begin{align}
\mathcal L_\theta = E\s{
\log p_\theta (\symbf{X}_0 | \symbf{X}_1) - \sum_{n=2}^T\d{q(\symbf{x}_{n-1}|\symbf{X}_n, \symbf{X}_0)}{p_\theta(\symbf{x}_{n-1}|\symbf{X}_n)} - \d{q(\symbf x_T | \symbf X_0)}{p_\theta(\symbf x_T)}
} + \const
\end{align}
$$

Consider the following restricted sampler formulation for $p_\theta(\symbf x_{n - 1} | \symbf x_n)$, $n \ge 2$ consider:
$$
p_\theta(\symbf x_{n - 1} |\symbf x_n) = \mathcal N(\symbf x_{n - 1}; \mu_\theta(\symbf x_n, n), \Sigma_\theta(\symbf x_n, n)), \quad \Sigma_\theta(\symbf x_n, n) = \omega^2_n \bI_d
$$

Further define that:
$$
\mu_\theta(\symbf x_n, n) := \tilde \mu_n(\symbf x_n, D_\theta(\symbf x_n, \sigma_n))
$$

Take the KL term at $D_n(\symbf x_n, \symbf x_0) := \d{q(\symbf x_{n - 1} | \symbf x_n, \symbf x_0)}{p_\theta(\symbf x_{n - 1} | \symbf x_n)}$ as an example. According to the analytic KL divergence of diagonal Gaussians:
$$
D_n(\symbf x_n, \symbf x_0) = \frac{1}{2 \omega_n^2} \norm{\tilde \mu_n(\symbf x_n, \symbf x_0) - \tilde \mu_n (\symbf x_n, D_\theta(\symbf x_n, \sigma_n))}_2^2 = \frac{(1 - \gamma_n)^2}{2 \omega_n^2} \norm{\symbf x_0 - D_\theta(\symbf x_n, \sigma_n)}_2^2
\label{equ:ddpmveloss}
$$
##### Optimal Variance ==TODO==

Consider the following decomposition of the ELBO:
$$
\begin{aligned}
\L_\theta(\symbf{X}_0) & = 
E\s{
\log p_\theta(\symbf{X}_T) + \sum_{n=1}^T\log \frac{p_\theta(\symbf{X}_{n-1}|\symbf{X}_{n})}{q(\symbf{X}_n|\symbf{X}_{n-1})}
}
\\
& = E\s{
\log p_\theta(\symbf{X}_T) + \sum_{n=1}^T\log \p{\frac{p_\theta(\symbf{X}_{n-1}|\symbf{X}_{n})}{q(\symbf{X}_{n-1}|\symbf{X}_{n})} \cdot \frac{q(\symbf{X}_{n-1})}{q(\symbf{X}_n)}}
}\\
& = E\s{
\log \frac{p_\theta(\symbf{X}_T)}{q(\symbf{X}_T)} + \sum_{n=1}^T\log \frac{p_\theta(\symbf{X}_{n-1}|\symbf{X}_{n})}{q(\symbf{X}_{n-1}|\symbf{X}_{n})} + \log q(\symbf{X}_0)
}
\\
& = -\d{q(\symbf{X}_T)}{p_\theta(\symbf{X}_T)} - E\s{\d{q(\symbf{x}_{n-1}|\symbf{X}_n)}{p_\theta(\symbf{x}_{n-1}|\symbf{X}_n)} + \log q(\symbf{X}_0)}
\end{aligned}
$$
Notice that we haven't discussed the choice of variance $\omega_n^2$ here. It is left for further discussion. It is straight forward to derive the optimal variance for some special cases:

When $\symbf X_0$ is deterministic or $q_0(\symbf x_0) = \delta(\symbf x_0 - \symbf c_0)$, then:
$$
q(\symbf x_{n - 1} | \symbf x_{n}) = q(\symbf x_{n - 1} | \symbf x_n, \symbf x_0) = \mathcal N\p{\symbf{x}_{n - 1}; \tilde \mu_n(\symbf{x}_n, \symbf{x}_0), \tilde \beta_n I}
$$
So $\omega_n = \tilde \beta_n$ is the optimal solution.

When $\symbf X_0$ has density $q_0(\symbf{x}_0) = \mathcal N(\symbf{x}_0; \symbf{0}, \sigma_{\mathrm{data}}^2\symbf{I})$, then

- $q(\symbf{x}_{n-1} | \symbf{x}_n) = {q(\symbf{x}_{n-1}) q(\symbf{x}_n | \symbf{x}_{n - 1})} /{q(\symbf{x}_n)}$.
- $q(\symbf{x}_n) = \mathcal N(\symbf{x}_n; \symbf{0}, (\sigma_{\mathrm{data}}^2 + \sigma_{n}^2)\symbf{I})$, $q(\symbf{x}_{n-1}) = \mathcal N(\symbf{x}_{n-1}; \symbf{0}, (\sigma_{\mathrm{data}}^2 + \sigma_{n - 1}^2)\symbf{I})$.
- $q(\symbf{x}_n | \symbf{x}_{n - 1}) = \mathcal N(\symbf{x}_n; \symbf{x}_{n-1}, \beta_n \symbf{I})$.

Therefore:
$$
q(\symbf x_{n - 1} | \symbf x_{n}) = \mathcal N\p{\symbf x_{n - 1}; \frac{\sigma_{\mathrm{data}}^2 + \sigma_{n - 1}^2}{\sigma_{\mathrm{data}}^2 + \sigma_n^2}\cdot \symbf x_n, \frac{\sigma_{\mathrm{data}}^2 + \sigma_{n - 1}^2}{\sigma_{\mathrm{data}}^2 + \sigma_n^2} \cdot \beta_n}
$$

##### Continuous Time Likelihood Weighting of DDPM(VE)

> [1] Kingma, Diederik, et al. "Variational diffusion models." *Advances in neural information processing systems* 34 (2021): 21696-21707.
>
> [2] Song, Yang, et al. "Maximum likelihood training of score-based diffusion models." *Advances in Neural Information Processing Systems* 34 (2021): 1415-1428.

Inspired by [1], in the following derivation, we demonstrates what happens when we take $T \to \infty$.

We fix the minimal and the maximal variance $\sigma_1$ and $\sigma_T$, from now on we will denote them as $\sigma_{\min}$ and $\sigma_{\max}$ instead.

Suppose there is a function $\sigma(t): [0, 1] \to [\sigma_{\min}, \sigma_{\max}]$ such that:

- $\sigma(t)$ is strictly increasing and continuously differentiable.
- $\sigma(0) = 0$ and $\sigma(n / T) = \sigma_n$ for $n \in \c{1,\ldots, T}$.

Consider equation $\ref{equ:ddpmveloss}$, notice that equivalently, for $2 \le n \le T$:
$$
\begin{align}
D_n(\symbf x_n, \symbf x_0) & = \frac{\sigma_n^2 - \sigma_{n - 1}^2}{2 \sigma_n^2 \sigma_{n - 1}^2} \norm{\symbf x_0 - D_\theta(\symbf x_n, \sigma_n)}_2^2 \\
& \gtrapprox \frac{\sigma^2(n/T) - \sigma^2((n - 1) / T)}{2 \sigma^4(n/T)} \norm{\symbf x_0 -  D_\theta(\symbf x_{n}, \sigma(n/T))}_2^2
\end{align}
$$

Now notice that as the partition becomes finer and $T \to \infty$:
$$
\begin{align}
\lim_{T \to \infty}\sum_{n = 2}^T D_n(\symbf x_n, \symbf x_0) &\to \int_{\sigma_{\min}}^{\sigma_{\max}} \frac{D[\sigma^2](t)}{2 \sigma^4(t)} \norm{\symbf x_{0} - D_\theta(\symbf x_t, \sigma(t))}_2^2 \dd t \\
&= \int_{\sigma_{\min}}^{\sigma_{\max}} D[\sigma^2](t) \norm{S_\theta(\symbf x_t, \sigma(t)) - \nabla \log p(\symbf x_t | \symbf x_0)}_2^2 \dd t
\end{align}
$$
This is consistent with the result given in reference [1] and [2]. The verification is left to the readers.

