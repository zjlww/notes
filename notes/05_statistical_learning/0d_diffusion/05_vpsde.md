#### Continuous-Time Diffusion Models: VPSDE

>  Song, Y., Sohl-Dickstein, J.N., Kingma, D.P., Kumar, A., Ermon, S., & Poole, B. (2020). Score-Based Generative Modeling through Stochastic Differential Equations. *ArXiv, abs/2011.13456*.

#### SDE Diffusion: VPSDE

##### Continuous-time limit of DDPM

Let's try to take $N \to \infty$ in the discrete forward diffusion in DDPM.

Suppose $(\mathbf X_{i/N})_{i = 1}^N$ and $(\mathbf Z_{i/N})_{n = 1}^N$ are defined as in DDPM. Suppose $(\mathbf B_t)$ is a standard $\R^d$ BM.

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
\mathbf X_{t + \Delta t} & = \sqrt{1 - \beta\p{t + \Delta t} \Delta t} \mathbf X_{t} + \sqrt{\beta(t)\Delta t} \mathbf Z_{t} \approx \mathbf X_t - \frac{1}{2} \beta(t) \Delta t \mathbf X_t + \sqrt{\beta (t)} \mathbf Z_t \sqrt{\Delta t}\\
& \approx \mathbf X_t - \frac{1}{2} \beta(t) \Delta t \mathbf X_t + \sqrt{\beta(t)} \p{\mathbf B_{t + \Delta t} - \mathbf B_{t}}\\
\end{aligned}
$$
Now, formally take the limit $N \to \infty$ hints as the following diffusion
$$
\dd \mathbf X_t = - \frac{1}{2} \beta(t) \dd \mathbf X_t + \sqrt{\beta(t)}\dd \mathbf B_t, \quad t \in [0, 1]
$$
It is called the Variance Preserving SDE (VPSDE) in Song's paper.

This is a linear SDE with density
$$
p_{t|0}(\mathbf x_t | \mathbf x_0) = \mathcal N(\mathbf x_t \mid \mathbf x_0 \sqrt{\bar \alpha(t)}, \p{1 - \bar \alpha(t)} \bI)
$$
For $\lambda \ge 0$ it has a family of reverse diffusion given by:
$$
d\mathbf X_t = \p{-\frac{1}{2} \beta(t) \mathbf X_t - (1 + \lambda)\beta(t) \nabla \log p(\mathbf X_t, t)} \dd t + \sqrt{\lambda\beta(t)} \dd \bar {\mathbf B}_t, \quad t \in [1, 0]
$$

##### VPSDE in EDM framework

Recall that a scaled driftless diffusion has differential
$$
\dd \mathbf {\what X}_t =\frac{\dot s(t)}{s(t)} \mathbf {\what X}_t \dd t + s(t) \sqrt{2 \dot \sigma(t) \sigma(t)} \dd \mathbf B_t, \quad \mathbf {\what X}_0 =  \mathbf {X}_0, \quad t \in [0, 1]
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

