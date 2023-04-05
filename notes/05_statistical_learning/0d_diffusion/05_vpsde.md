#### Continuous-Time Diffusion Models: VPSDE

>  Song, Y., Sohl-Dickstein, J.N., Kingma, D.P., Kumar, A., Ermon, S., & Poole, B. (2020). Score-Based Generative Modeling through Stochastic Differential Equations. *ArXiv, abs/2011.13456*.

#### SDE Diffusion: VPSDE

##### Continuous-time limit of DDPM

Let's try to take $N \to \infty$ in the discrete forward diffusion in DDPM.

Suppose $(\symbf X_{i/N})_{i = 1}^N$ and $(\symbf Z_{i/N})_{n = 1}^N$ are defined as in DDPM. Suppose $(\symbf B_t)$ is a standard $\R^d$ BM.

Take a continuous function $\beta(t): [0, 1] \to \R^+$ where $\beta(i / N) = \beta_i$ in DDPM.

- In DDPM the choice of $(\beta_i)_{i = 1}^T$ is $\bar \beta_{\min} = 0.1$, $\bar\beta_{\max} = 20.0$.
  $$
  \beta_{i}=\frac{\bar{\beta}_{\min }}{N}+\frac{i-1}{N(N-1)}\left(\bar{\beta}_{\max }-\bar \beta_{\min}\right)
  $$

- Now take $N \to \infty$ gives
  $$
  \beta(t)=\bar{\beta}_{\min }+t\left(\bar{\beta}_{\max }-\bar{\beta}_{\min }\right), \quad t\in [0, 1]
  $$

- For convenience, define

$$
\bar \alpha(t) := \exp\p{- \int_0^t\beta (\tau) \dd \tau} = \exp\p{-\frac{1}{2}t^2\p{\bar \beta_\max - \bar \beta_\min} - t \bar \beta_\min}
$$


Let $\Delta t := 1 / N$ and $t = i / N$. Then notice
$$
\begin{aligned}
\symbf X_{t + \Delta t} & = \sqrt{1 - \beta\p{t + \Delta t} \Delta t} \symbf X_{t} + \sqrt{\beta(t)\Delta t} \symbf Z_{t} \approx \symbf X_t - \frac{1}{2} \beta(t) \Delta t \symbf X_t + \sqrt{\beta (t)} \symbf Z_t \sqrt{\Delta t}\\
& \approx \symbf X_t - \frac{1}{2} \beta(t) \Delta t \symbf X_t + \sqrt{\beta(t)} \p{\symbf B_{t + \Delta t} - \symbf B_{t}}\\
\end{aligned}
$$
Now, formally take the limit $N \to \infty$ hints as the following diffusion
$$
\dd \symbf X_t = - \frac{1}{2} \beta(t) \dd \symbf X_t + \sqrt{\beta(t)}\dd \symbf B_t, \quad t \in [0, 1]
$$
It is called the Variance Preserving SDE (VPSDE) in Song's paper.

This is a linear SDE with density
$$
p_{t|0}(\symbf x_t | \symbf x_0) = \mathcal N(\symbf x_t \mid \symbf x_0 \sqrt{\bar \alpha(t)}, \p{1 - \bar \alpha(t)} \bI)
$$
For $\lambda \ge 0$ it has a family of reverse diffusion given by:
$$
d\symbf X_t = \p{-\frac{1}{2} \beta(t) \symbf X_t - (1 + \lambda)\beta(t) \nabla \log p(\symbf X_t, t)} \dd t + \sqrt{\lambda\beta(t)} \dd \bar {\symbf B}_t, \quad t \in [1, 0]
$$

##### VPSDE in EDM framework

Recall that a scaled driftless diffusion has differential
$$
\dd \symbf {\what X}_t =\frac{\dot s(t)}{s(t)} \symbf {\what X}_t \dd t + s(t) \sqrt{2 \dot \sigma(t) \sigma(t)} \dd \symbf B_t, \quad \symbf {\what X}_0 =  \symbf {X}_0, \quad t \in [0, 1]
$$
Now compare the unknowns and try to solve for $s(t)$ and $\sigma(t)$.

- $s(t)$ satisfies the IVP $\dot s(t) = -\frac{1}{2}\beta(t) s(t)$, where $s(0) = 1$. Therefore
  $$
  s(t) = \exp\p{-\frac{1}{2}\int_0^t \beta(s) \dd s} = \sqrt{\bar \alpha(t)}
  $$

- $\sigma(t)$ satisfies the IVP $(\sigma^2)'(t) = \beta(t) / \bar \alpha(t)$, where $\sigma^2(0) = 0$. Therefore
  $$
  \sigma^2(t) = \int_0^t \frac{\beta(\tau)}{\bar \alpha(\tau)} \dd \tau = \int_0^t \beta(\tau) \exp\p{\int_0^\tau \beta(\xi) \dd \xi} = \frac{1}{\bar \alpha(t)} - 1
  $$

