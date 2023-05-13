#### Denoising Diffusion Probabilistic Models

This is the original formulation of the DDPM, this derivation is very influential and is referenced in many works.

> Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. *ArXiv, abs/2006.11239*.

##### Discrete forward diffusion

Suppose $\symbf X_0 \sim p_0(\symbf x)$ is a random variable in $\R^d$ with data distribution.

Let $(\symbf Z_n)_{n = 1}^{T} \sim_{\iid} \mathcal N(\symbf 0, \bI_d)$ be $T$ independent gaussian random variables. Define $(\symbf X_{n})_{n = 1}^T$ recursively as
$$
\symbf X_n = \sqrt{\beta_n} \symbf Z_n + \sqrt{1 - \beta_n} \symbf X_{n - 1}, \quad n \in \c{1, \ldots, T}
$$
for some sequence of predefined $(\beta_n)_{n = 1}^T \in (0, 1)$. The Markov process $(\symbf X_n)_{n = 0}^T$ is called the **forward diffusion**, which gradually adds noise into $\symbf X_0$.

- The forward diffusion process has conditional density given by
  $$
  q(\symbf x_{1..T}|\symbf  x_0) = \prod_{n=1}^T q(\symbf x_{n} | \symbf x_{n-1}) \quad q(\symbf x_n | \symbf x_{n-1}) = \mathcal N(\symbf x_n; \sqrt {1-\beta_n} \symbf x_{n-1}, \beta_n \bI_d)
  $$

- For $n \in 1.. T$ define $\alpha_n = 1 - \beta_n \in (0, 1)$ and $\bar \alpha_n = \prod_{k = 1}^n \alpha_k$. $\alpha_n$ and $\bar \alpha_n$ strictly decreases from $1$ to a value close to $0$.

- Then the marginal conditional density is given by
  $$
  q(\symbf x_n | \symbf x_0) = \mathcal N(\symbf x_n ; \symbf x_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n )\bI_d)
  $$

- For some $\symbf E_n \sim \mathcal N(\symbf 0, \bI_d)$ depending on $(\symbf Z_1, \ldots, \symbf Z_n)$, we have
  $$
  \symbf X_n = \sqrt{1-\bar \alpha_n} \symbf E_n + \sqrt{\bar \alpha_n} \symbf X_0
  $$

##### A posterior of forward diffusion

The posterior density can be derived by Bayes' theorem

$$
q(\symbf{x}_{n-1}|\symbf{x}_{n}, \symbf{x}_0) = \frac{q(\symbf{x}_{n}|\symbf{x}_{n-1}, \symbf{x}_0)q(\symbf{x}_{n-1}|\symbf{x}_0)}{q(\symbf{x}_n|\symbf{x}_0)}
$$

Where we already know:

- $q(\symbf{x}_n | \symbf{x}_{n - 1}, \symbf{x}_0) = q(\symbf{x}_n | \symbf{x}_{n-1}) = \mathcal N(\symbf{x}_n; \sqrt {1-\beta_n} \symbf{x}_{n-1}, \beta_n \symbf{I})$.
- $q(\symbf{x}_n | \symbf{x}_0) = \mathcal N(\symbf{x}_n ; \symbf{x}_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n) \symbf{I})$.
- $q(\symbf{x}_{n-1} | \symbf{x}_0) = \mathcal N(\symbf{x}_{n - 1}; \symbf{x}_0 \sqrt{\bar \alpha_{n - 1}}, (1 - \bar \alpha_{n - 1}) \symbf{I})$.


We can simplify with following knowledge:

- The result must be a gaussian density function.

- Each dimension is independent, so we can assume 1D case WLOG.
  $$
  \mathcal N(x; \mu, \sigma^2) = \frac{\exp \p{-(x-\mu)^2 / 2 \sigma^2)}}{\sigma \sqrt{2\pi}}; \quad \log \mathcal N(x; \mu, \sigma^2) = - \frac{1}{2\sigma^2} x^2 + \frac{\mu}{\sigma^2} x - \frac{1}{2 \sigma^2} \mu^2 + \text{const.}
  $$

- Take logarithm, and ignore the constants, the result must be a quadratic in $x_{n-1}$.

We now only need the quadratic and linear coefficient of $x_{n-1}$ to find the mean and variance.
$$
-\frac{1 - \bar \alpha_n}{2\p{1 - \bar \alpha_{n - 1}} \beta_n} x_{n - 1}^2 + \frac{\sqrt{\alpha_n} \p{1 - \bar \alpha_{n - 1}} x_n + \beta_n \sqrt{\bar \alpha_{n - 1}} x_0}{\beta_n (1 - \bar \alpha_{n - 1})} x_{n - 1} + \text{const.}
$$
Now compare with Gaussian density function gives:
$$
\sigma^2 = \frac{\p{1 - \bar \alpha_{n - 1}}\beta_n}{(1 - \bar \alpha_n)}; \quad \mu = \frac{\sqrt{\alpha_n} \p{1 - \bar \alpha_{n - 1}} x_n + \beta_n \sqrt{\bar \alpha_{n - 1}} x_0}{\p{1 - \bar \alpha_n}}
$$

So the conditional density $q(\symbf x_{n - 1} | \symbf x_n, \symbf x_0), n \in 2..T$ has the closed form solution:

$$
\begin{aligned}
q(\symbf{x}_{n - 1} | \symbf{x}_n, \symbf{x}_0) &= \mathcal N\p{\symbf{x}_{n - 1}; \tilde \mu_n(\symbf{x}_n, \symbf{x}_0), \tilde \beta_n \bI}\\
\quad \tilde\mu_{n}\left(\symbf{x}_n, \symbf{x}_0\right) &= \frac{\sqrt{\bar{\alpha}_{n-1}} \beta_{n}}{1-\bar{\alpha}_{n}} \symbf{x}_{0}+\frac{\sqrt{\alpha_{n}}\left(1-\bar{\alpha}_{n-1}\right)}{1-\bar{\alpha}_{n}} \symbf{x}_{n}; \quad \tilde{\beta}_{n}=\frac{1-\bar{\alpha}_{n-1}}{1-\bar{\alpha}_{n}} \beta_{n}
\end{aligned}
$$

##### Discrete reverse diffusion model

The idea is to train an autoregressive model on $\R^d$ to sample paths from the forward diffusion without $\symbf X_0$.

Consider a reverse time Markov process with states in $\R^d$ decomposed as
$$
p_\theta(\symbf x_0, \ldots, \symbf x_T) = p_\theta(\symbf x_T) \prod_{n = 1}^T p_\theta(\symbf x_{n - 1} | \symbf x_{n}),\quad p_\theta(\symbf x_T) := \mathcal N(\symbf x_T;\symbf 0, \bI_d)
$$
this process is also called the **denoising process**.

##### ELBO of DDPM

But there is indeed an ELBO we could use for training. This is equivalent to an VAE with approximate posterior $q$ and prior $p_\theta$.

$$
\begin{aligned}
\mathcal L_\theta
&= E\s{\log p_\theta(\symbf{X}_0|\symbf{Z}) - \log q(\symbf{Z}|\symbf{X}_0) + \log p_\theta(\symbf{Z})}\\
&= E\s{\log p_\theta(\symbf{X}_0, \symbf{X}_{1..T}) - \log q(\symbf{X}_{1..T}|\symbf{X}_0)}\\
&= E\s{
\log p_\theta(\symbf{X}_T) + \sum_{n=2}^T\log \frac{p_\theta(\symbf{X}_{n-1}|\symbf{X}_{n})}{q(\symbf{X}_{n-1}|\symbf{X}_n, \symbf{X}_0)} + \log \frac{p_\theta (\symbf{X}_0 | \symbf{X}_1)}{q(\symbf{X}_1 | \symbf{X}_0)}
}\\
&= E\s{
\log \frac{p_\theta(\symbf{X}_T)}{q(\symbf{X}_T|\symbf{X}_0)} + \sum_{n=2}^T\log \frac{p_\theta(\symbf{X}_{n-1}|\symbf{X}_{n})}{q(\symbf{X}_{n-1}|\symbf{X}_{n}, \symbf{X}_0)} + \log p_\theta (\symbf{X}_0 | \symbf{X}_1)
} + \const\\
&= E\s{
\log p_\theta (\symbf{X}_0 | \symbf{X}_1) - \sum_{n=2}^T\d{q(\symbf{x}_{n-1}|\symbf{X}_n, \symbf{X}_0)}{p_\theta(\symbf{x}_{n-1}|\symbf{X}_n)} - \d{q(\symbf{x}_T|\symbf{X}_0)}{p_\theta(\symbf{x}_T)}
} + \const
\end{aligned}
$$

Consider the following restricted sampler formulation for $p_\theta(\symbf x_{n - 1} | \symbf x_n)$, $n \ge 2$ consider:
$$
p_\theta(\symbf x_{n - 1} |\symbf x_n) = \mathcal N(\symbf x_{n - 1}; \mu_\theta(\symbf x_n, n), \Sigma_\theta(\symbf x_n, n)),\quad \Sigma_\theta(\symbf x_n, n) = \sigma_n^2 \bI
$$

- Note that $\sigma_n^2 = \beta_n$ is optimal for $X_0 \sim \mathcal N(0, I)$. And we will be **assuming** $\sigma_n^2 = \beta_n$ from now on.

- Then by the analytic KL-divergence of isotropic Gaussians:
  $$
  \d{q(\symbf{x}_{n - 1} | \symbf{X}_n, \symbf{X}_0)}{p_\theta(\symbf{x}_{n - 1} | \symbf{X}_n)} = \frac{E\norm{\tilde \mu_n(\symbf{X}_n, \symbf{X}_0) - \mu_\theta(\symbf{X}_n, n)}^2_2}{2\sigma_n^2} + \const
  $$

- Define $J_\theta^{(n)} := E\norm{\tilde \mu_n(\symbf{X}_n, \symbf{X}_0) - \mu_\theta(\symbf{X}_n, n)}^2_2$. Define $L_\theta^{(n)} := J_\theta^{(n)} / 2\sigma_n^2$.

Predicting $\symbf{E}_n$ given $\symbf X_0$ seems to be a good choice. Let $E_\theta(\symbf{x}_n, n)$ be the neural predictor of $\symbf{E}_n$.

- Recall that $\symbf X_n = \sqrt{1-\bar \alpha_n} \symbf E_n + \sqrt{\bar \alpha_n} \symbf X_0$. Then
  $$
  \symbf X_0 =  \frac{1}{\sqrt{\bar \alpha_n}}\p{\symbf X_n - \sqrt{1-\bar \alpha_n} \symbf E_n}
  $$

- Then we have
  $$
  \mu_\theta\p{\symbf X_n, \frac{1}{\sqrt{\bar \alpha_n}}\p{\symbf X_n - \sqrt{1-\bar \alpha_n} \symbf E_n}} = \frac{1}{\sqrt{\alpha_n}}\p{\symbf X_n - \frac{\beta_n}{\sqrt{1 - \bar \alpha_t}}\symbf E_n}
  $$

- This inspires us to define
  $$
  \mu_\theta(\symbf X_n, n) := \frac{1}{\sqrt{\alpha_n}}\p{\symbf X_n - \frac{\beta_n}{\sqrt{1 - \bar \alpha_t}}E_\theta(\symbf X_n, n)}
  $$

- Then $J_\theta^{(n)}$ simplifies to
  $$
  J_\theta^{(n)} = E\s{\norm{\frac{1}{\sqrt{\alpha_n}}\left(\symbf{X}_n - \frac{\beta_n}{\sqrt{1 - \bar \alpha_n}} \symbf E_n\right) - \frac{1}{\sqrt{\alpha_n}}\p{\symbf X_n - \frac{\beta_n}{\sqrt{1 - \bar \alpha_t}}E_\theta(\symbf X_n, n)}}^2_2}
  $$

- And $L_\theta^{(n)}$ becomes
  $$
  L_\theta^{(n)} = \frac{\beta_n^2}{2\sigma_n^2 \alpha_n (1 - \bar \alpha_n)} E\s{\norm{\symbf E_n - E_\theta(\symbf{X}_n, n)}^2_2}
  $$

- Ho et al. propose to **ignore the weighting term** and optimize for
  $$
  \widetilde L_\theta^{(n)}:= E\s{\norm{\symbf E_n - E_\theta(\symbf{X}_n, n)}^2_2}
  $$

- Notice that the parameterization of $p_\theta(\symbf{x}_0 | \symbf{x}_1)$ may depend on the problem in the DDPM framework.

As we have shown before, such a loss is equivalent to denoising score matching. Define $S_\theta(\symbf{x}_n, n) = -E_\theta(\symbf{x}_n, n) / \sqrt{1 - \bar\alpha_n}$.
$$
\widetilde L_\theta^{(n)} = (1 - \bar \alpha_n) E\s{\norm{S_\theta(\symbf{X}_n, n) - \nabla\log q(\symbf{X}_n | \symbf{X}_0)}_2^2}
$$
The sampling process resembles sampling the reverse SDE, and the update rule is:
$$
\symbf x_{n - 1} = \frac{1}{\sqrt{\alpha_n}}(\symbf x_n + \beta_n S_\theta(\symbf x_n, n)) + \sqrt{\beta_n} \symbf z_n
$$

##### Optimal variance ==TODO==

Consider the following alternative derivation of $\L_\theta$:
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
The optimal variance for $p_\theta(\symbf{x}_{n - 1} | \symbf{x}_n)$ can be derived from $q(\symbf{x}_{n - 1} | \symbf{x}_n)$ if it is also diagonal Normal.

When $q_0(\symbf{x}_0) = \delta(\symbf{x}_0 - \symbf{c}_0)$, then

- $q(\symbf{x}_{n-1} | \symbf{x}_n) = q(\symbf{x}_{n-1} | \symbf{x}_n, \symbf{x}_0)$.
- Clearly $\sigma_n := \tilde{\beta}_{n}=\frac{1-\bar{\alpha}_{n-1}}{1-\bar{\alpha}_{n}} \beta_{n}$ minimizes the KL divergence.

When $q_0(\symbf{x}_0) = \mathcal N(\symbf{x}_0; \symbf{0}, \symbf{I})$, then

- $q(\symbf{x}_{n-1} | \symbf{x}_n) = {q(\symbf{x}_{n-1}) q(\symbf{x}_n | \symbf{x}_{n - 1})} /{q(\symbf{x}_n)}$.
  - $q(\symbf{x}_n) = \mathcal N(\symbf{x}_n; \symbf{0}, \symbf{I})$, $q(\symbf{x}_{n-1}) = \mathcal N(\symbf{x}_{n-1}; \symbf{0}, \symbf{I})$.
  - $q(\symbf{x}_n | \symbf{x}_{n - 1}) = \mathcal N(\symbf{x}_n; \sqrt {1-\beta_n} \symbf{x}_{n-1}, \beta_n \symbf{I})$.
- Therefore $q(\symbf{x}_{n - 1} | \symbf{x}_n) = \mathcal N(\symbf{x}_{n-1}; \sqrt{1 - \beta_n} \symbf{x}_n, \beta_n \symbf{I})$.
- Clearly $\sigma_n := \beta_n$ is the optimal choice here.

