#### SDE Diffusion: VPSDE

(**DDPM in SDE framework**)

Continue (**Simple Diffusion**).

Recall the formulation of DDPM:

- We choose a sequence $(\beta_n)_{n = 1}^N \in (0, 1)$.
- For $n \in 1.. N$ define $\alpha_n = 1 - \beta_n \in (0, 1)$ and $\bar \alpha_n = \prod_{k = 1}^n \alpha_k$.
- $q(x_n | x_{n-1}) = \mathcal N(x_n; \sqrt {1-\beta_n} x_{n-1}, \beta_n I)$.
- It can be shown that $q(x_n | x_0) = \mathcal N(x_n ; x_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n )I)$.

Now we can try to derive the continuous time limit of the DDPM noising process:

- Let $\beta(t):[0, 1] \to [0, \infty)$ and $\beta(i / N) = N \beta_i$ for $i \in 1..N$.
- Since $X_i = \sqrt{1 - \beta_i} X_{i - 1} + \sqrt{\beta_i}Z_i$ as defined in DDPM.
- Let $Y_{i/N} = X_i$ and $B_{i/N} = Z_i/\sqrt{N}$.
  - $Y_{i/N} = \sqrt{1 - \beta(i/N)/N}Y_{(i-1)/N} + \sqrt{\beta(i/N)} B_{i/N}$.
- Let $t = (i - 1) / N$ and $\Delta t = 1/N$.
  - $Y_{t + \Delta t} = \sqrt{1 - \beta(t + \Delta t) \Delta t} Y_t + \sqrt{\beta(t + \Delta t)} B_{t}$.
- Notice that $\sqrt{1 + x} = 1 + x / 2 + o(x^2)$ at $0$.
  - $Y_{t + \Delta t}  = \sqrt{1 - \beta(t + \Delta t)\Delta t} Y_t + \sqrt{\beta(t + \Delta t)} Z_t\approx Y_t - \frac{1}{2} \beta(t) \Delta t Y_t + \sqrt{\beta(t) \Delta t} Z_t$ 

This begs us to consider $dX_t = -\frac{1}{2} \beta(t)X_t dt + \sqrt{\beta(t)} dB_t$ on $t \in [0, 1]$.

- This is a linear SDE and it solves to the following:
  $$
  \bar \alpha(t) := \exp({- \int_0^t \beta(s) \dd s})\\
  p_{0t}(x_t | x_0) = \mathcal N(x_t \mid x_0 \sqrt{\bar \alpha(t)}, \p{1 - \bar \alpha(t)} I) = \mathcal N(x_t \mid \mu_t, \Sigma_t)
  $$

(**Probability flow ODE**)

The probability flow ODE is given by:
$$
x'(t) = -\frac{1}{2} \beta(t) x(t) - \frac{1}{2} \beta(t) \nabla \log p_t(x), \quad t \in [0, 1]
$$
Start sampling from $t = 1$ gives the data distribution.

(**Reverse SDE**)

The reverse-time SDE is given by:
$$
dX_t = \p{-\frac{1}{2} \beta(t) X_t - \beta(t) \nabla \log p_t(X_t)} dt + \sqrt{\beta(t)} d\bar B_t, \quad t: 1 \to 0
$$
(**Choice of hyper-parameters**)

In DDPM the choice of $(\beta_i)_{i = 1}^T$ is
$$
\beta_{i}=\frac{\bar{\beta}_{\min }}{N}+\frac{i-1}{N(N-1)}\left(\bar{\beta}_{\max }-\bar \beta_{\min}\right)
$$
Now take $N \to \infty$ gives 
$$
\beta(t)=\bar{\beta}_{\min }+t\left(\bar{\beta}_{\max }-\bar{\beta}_{\min }\right), \quad t\in [0, 1]
$$
And
$$
\bar \alpha(t) = \exp\p{- \int_0^t\beta (s) \dd s} = \exp\p{-\frac{1}{2}t^2\p{\bar \beta_\max - \bar \beta_\min} - t \bar \beta_\min}
$$
To avoid numerical issues during training, $t \in [\epsilon, 1]$ where $\epsilon = 10^{-5}$.

(**Variation with drifted mean**)

Consider forward SDE:
$$
dX_t = -\frac{1}{2} \beta(t) X_t dt + \frac{1}{2}\mu \beta(t) dt + \sqrt{\beta(t)} dB_t
$$
This is a linear SDE and it solves to the following:
$$
p_{0t}(x_t | x_0) = \mathcal N(x_t \mid (1-e^{-\frac{1}{2} \int_{0}^{t} \beta(s) d s}) \mu +  x_0 e^{-\frac{1}{2} \int_0^t \beta(s) ds}, [1 - e^{-\int_0^t \beta(s) ds}] I) = \mathcal N(x_t \mid \mu_t, \Sigma_t)
$$
The probability flow ODE is given by:
$$
x'(t) = -\frac{1}{2} \beta(t) x(t) - \frac{1}{2} \beta(t) \p{\nabla \log p_t(x) - \mu}, \quad t \in [0, 1]
$$
Notice that $\nabla \log p_t(x) - \mu$ should be the target of the neural network in this case.

