#### Linear Inverse Problem Solvers Based On Gaussian Approximation of  $p(\symbf x_0 | \symbf x_t)$

> References:
>
> [1] Ho, Jonathan, et al. "Video diffusion models." *arXiv preprint arXiv:2204.03458* (2022).
>
> [2] Chung, Hyungjin, et al. "Improving diffusion models for inverse problems using manifold constraints." *arXiv preprint arXiv:2206.00941* (2022).
>
> [3] Chung, Hyungjin, et al. "Diffusion posterior sampling for general noisy inverse problems." *arXiv preprint arXiv:2209.14687* (2022).
>
> [4] Song, Jiaming, et al. "Pseudoinverse-guided diffusion models for inverse problems." *International Conference on Learning Representations*. 2023.
>
> Some unfriendly comments:
>
> As far as I know, [1] is the first publication of the idea. Little innovation in [2, 3, 4].
>
> [2, 3, 4] all relies on the same gaussian approximation of $p(\symbf x_0 | \symbf x_t)$ proposed in [1]. So far the theoretical underpinning is still lacking.
>
> [2, 3] are almost the same. Further more, the derivation in [3] is wrong. I would NOT recommend you studying the derivation in [2].
>
> The solution for handling quantization in [4]... It is only tested on JPEG restoration. It seems to be essentially the straight-through estimator for the quantization operation.

##### The general idea

Suppose $\symbf X_0$ is a random vector in $\R^d$. Suppose $p(\symbf y | \symbf x): \R^o \times \R^d \to \R^+$ is a differentiable conditional probability density. Suppose $\symbf Y$ is a random vector with conditional density $p(\symbf y | \symbf x)$.

Decompose the problem-specific score via Bayes' rule:
$$
\nabla_{\symbf x_t} \log p(\symbf x_t | \symbf y) = \nabla_{\symbf x_t} \log p(\symbf x_t) + \underbrace{\nabla_{\symbf x_t} \log p(\symbf y | \symbf x_t)}_{\text{gradient guidance}}
$$
$p(\symbf y | \symbf x_t)$ can be decomposed into:
$$
p(\symbf y | \symbf x_t) = \int_{\R^d} p(\symbf x_0 | \symbf x_t) p(\symbf y | \symbf x_0) \dd \symbf x_0
\label{equ:convp}
$$

Unfortunately $p(\symbf x_0 | \symbf x_t)$ is intractable. Define $\hat {\symbf x}_t:= D_\theta(\symbf x_t, \sigma_t) \approx E[\symbf x_0 | \symbf x_t]$. A crude approximation would be:
$$
p(\symbf x_0 | \symbf x_t) \approx q(\symbf x_0 | \symbf x_t) := \mathcal N(\symbf x_0; E[\symbf x_0 | \symbf x_t], r_t^2 \bI) \approx \mathcal N(\symbf x_0;D_\theta(\symbf x_t,\sigma(t)), r_t^2 \bI)
$$

[4] offered the following approximation for the choice of $r_t^2$.

- From Bayes' rule:
  $$
  p(\symbf x_0 | \symbf x_t) = p(\symbf x_t | \symbf x_0) p(\symbf x_0) / p(\symbf x_t)
  $$

- Suppose $\symbf X_0 \sim \mathcal N(\symbf 0, \sigma_{\mathrm{data}}^2\bI)$. We have:

  - $p(\symbf x_0) = \mathcal N(\symbf x_0; \symbf 0, 	\sigma_{\mathrm{data}}^2\bI)$. And $p(\symbf x_t | \symbf x_0) = \mathcal N(\symbf x_t; \symbf x_0, \sigma_t^2 \bI)$.

  - $p(\symbf x_t) = \mathcal N(\symbf x_t; \symbf 0, (\sigma_{\mathrm{data}}^2 + \sigma_t^2) \bI)$.

  $$
  p(\symbf x_0 | \symbf x_t) = \mathcal N\p{\symbf x_0; \frac{\sigma_{\mathrm{data}}^2}{\sigma_{\mathrm{data}}^2 + \sigma_t^2} \cdot \symbf x_t,\frac{\sigma_{\mathrm{data}}^2 \sigma_{t}^2}{\sigma_{\mathrm{data}}^2 + \sigma_{t}^2} \bI}
  $$

- Therefore we should take the following $r_t^2$ in $q(\symbf x_0 | \symbf x_t)$.

$$
r_t^2 = \frac{\sigma_{\mathrm{data}}^2 \sigma_{t}^2}{\sigma_{\mathrm{data}}^2 + \sigma_{t}^2}
$$

Notice that there are two source of noises here we need to manage:

- Noise introduced by the uncertainty in $q(\symbf x_0 | \symbf x_t) \approx p(\symbf x_0 | \symbf x_t)$.
- Noise in measurement $p(\symbf y | \symbf x_0)$.

For general non-linear kernel $p(\symbf y | \symbf x_0)$ the convolution in equation $\ref{equ:convp}$ is again intractable.

- In [4] the discussion is limited to linear problems.
- In [3] the noise in $q(\symbf x_0 | \symbf x_t)$ is completely ignored.
- [4] demonstrated that, in the case where $p(\symbf y | \symbf x)$ contains quantization, it can be made approximately differentiable by applying the straight-through gradient estimator.

##### Noisy linear inverse problem [4]

Suppose $\symbf Y = H\symbf X_0 + \symbf Z$ where $\symbf Z \sim \mathcal N(\mu, \Sigma)$ and $H \in \R^{o \times d}$.

$$
p(\symbf y | \symbf x_t) \approx \int_{\R
^d} q(\symbf x_0 | \symbf x_t) p(\symbf y | \symbf x_0) \dd \symbf x_0 = \mathcal N(H \hat {\symbf x}_t + \mu, r_t^2 HH^T + \Sigma)
$$
