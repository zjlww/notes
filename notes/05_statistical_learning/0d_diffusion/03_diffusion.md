#### Continuous-Time Diffusion Models: EDM Formulation

> We give an introduction following the mathematical framework proposed in this paper (EDM). It managed to decouple the score estimator and the sampling process.
>
> Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the Design Space of Diffusion-Based Generative Models. *ArXiv, abs/2206.00364*.

Let $(\symbf B_t)$ be a $n$-dimensional standard Brownian motion, and $(\symbf {\wbar B})_t$ be an $n$-dimensional reverse Brownian motion.

##### Driftless diffusion

Suppose $(\symbf X_t)$ is the following diffusion process, it is called a **driftless diffusion**. For strictly increasing $\sigma(t) \in C^1([0, T] \to \R^+)$.
$$
\dd \symbf X_t = \sqrt{2\dot \sigma(t)\sigma(t)} \dd \symbf B_t, \quad \symbf X_0 \sim p(\symbf x; 0), \quad t \in [0, T]
$$
Where $p(\symbf x; 0)$ is the data density on $\R^n$. Equivalently $\symbf X_t$ can be viewed as adding noise to $\symbf X_0$ in the following way,
$$
\symbf X_t = \symbf X_0 + \int_0^t \sqrt{2\dot \sigma(\tau)\sigma(\tau)} \dd \symbf B_\tau, \quad \int_0^t \sqrt{2\dot \sigma(\tau)\sigma(\tau)} \dd \symbf B_\tau \sim \mathcal N\p{\symbf 0, \sigma^2(t)\bI_n}, \quad t \in [0, T]
$$

Denote the density of $\symbf X_t$ as $p(\symbf x; \sigma(t))$ or just $p(\symbf x_t)$ by omitting $\sigma(t)$.

Then according to weak-sense time reversal, we have the reverse diffusion for $\lambda(t)\in C([0, T] \to \R^+)$:
$$
\dd \symbf X_t = -(1 + \lambda(t)) \dot \sigma(t) \sigma(t) \nabla_{\symbf x} \log p(\symbf X_t; \sigma(t)) \dd t + \sqrt{2 \lambda (t)\dot \sigma(t)\sigma(t)}\dd \symbf {\wbar B}_t,\quad t \in [T, 0]
$$
The $\beta(t)$ in EDM is defined as $\beta(t) = \lambda(t) \dot \sigma(t) / \sigma(t)$. By taking $\beta(t) = \lambda(t) = 0$, we will obtain the probability flow ODE.

##### Scaled driftless diffusion

Suppose $(\symbf {X}_t)$ is a driftless diffusion, and $\what {\symbf X}_t = s(t) \symbf {X}_t$ for some scaling function $s(t) \in C^1([0, T]\to \R^+)$ where $s(0) = 1$.

Now by Itô's formula, it has stochastic differential
$$
\dd \what {\symbf X}_t = \dot s(t) \symbf {X}_t \dd t + s(t) \dd \symbf {X}_t = \frac{\dot s(t)}{s(t)} \what {\symbf X}_t \dd t + s(t) \sqrt{2 \dot \sigma(t) \sigma(t)} \dd \symbf B_t, \quad \what {\symbf X}_0 =  \symbf {X}_0, \quad t \in [0, T]
$$
By definition we have
$$
\what {\symbf X}_t = s(t) \symbf {X}_0 + s(t)\int_0^t \sqrt{2\dot \sigma(\tau)\sigma(\tau)} \dd \symbf B_\tau, \quad t \in [0, T]
$$
Denote the density of $\what {\symbf X}_t$ as $\what p(\symbf { x}; \sigma(t))$. Then
$$
\log \what p(\symbf x; \sigma(t)) = -n \log s(t) + \log  p\p{\frac{\symbf x}{s(t)}; \sigma(t)}
$$
Actually we could compute $\nabla \log \what p(\symbf x; \sigma)$ from $\nabla \log p(\symbf x; \sigma)$.
$$
\nabla_{\symbf x} \log \what p(\symbf x; \sigma(t)) = \frac{1}{s(t)}\nabla_{\symbf x} \log p\p{\frac{\symbf x}{s(t)}; \sigma(t)}
$$
Similar to driftless diffusion, we have reverse diffusion:
$$
\dd \what {\symbf X}_t = \p{\frac{\dot s(t)}{s(t)} \what {\symbf X}_t - (1 + \lambda(t))s(t)\dot \sigma(t) \sigma(t) \nabla_{\symbf x} \log p\p{\frac{\what {\symbf X}_t}{s(t)}; \sigma(t)}} \dd t + s(t) \sqrt{2 \lambda(t)\dot \sigma(t) \sigma(t)} \dd \symbf B_t,\quad t \in [T, 0]
$$

##### The denoising function and the score function

Define the score function $S(\symbf x, \sigma): \R^n \times \R^+ \to \R^n$ as
$$
S(\symbf x, \sigma) = \argmin{S} E {\norm{S(\symbf X_0 + \sigma \symbf N, \sigma) - \frac{\symbf N}{\sigma}}^2_2} = \nabla \log p(\symbf x; \sigma)
$$
Define the denoising function $D(\symbf x, \sigma): \R^n \times \R^+ \to \R^n$ as $D(\symbf x, \sigma) := E[\symbf X_0 | \symbf Y_{\sigma} = x]$.

According to tweedie's formula, we have the following relationship:
$$
D(\symbf x, \sigma) = \symbf x + S(\symbf x, \sigma) \sigma^2  = \symbf x + \sigma^2\nabla \log p(\symbf x; \sigma)
$$
Let $\symbf N \sim \mathcal N(\symbf 0, \bI_n)$ be independent to all other variables. Then $D(\symbf x, \sigma)$ is the function such that
$$
D(\symbf x, \sigma) = \argmin{D}  E\n{D(\symbf X_0 + \sigma \symbf N, \sigma) - \symbf X_0}_2^2
$$

##### Hyperparameters of diffusion in EDM

The choice of $\lambda(t)$, $s(t)$, and $\sigma(t)$ changes the reverse diffusion process, therefore the truncation error when applying numerical solvers to them.

In EDM, the authors proposed $\lambda(t) = 0$, $\sigma(t) = t$ and $s(t) = 1$ for the probability flow ODE.

- Suppose $\symbf x(t)$ is a solution of the probability flow ODE, then
  $$
  \dot {\symbf x}(t) = -t\nabla_{\symbf x} \log p(\symbf x(t), t) = \frac{\symbf x(t) - D(\symbf x(t), t)}{t}
  $$

- The tangent vector at $\symbf x(t)$ is pointing towards the denoised data $D(\symbf x(t), t)$, which is largely stable. So the solution trajectory is mostly linear.

##### Denoising models and score estimators

We may use a neural network to approximate either $D(\symbf x, \sigma)$ or $S(\symbf x, \sigma)$.

- A model $D_\theta(\symbf x, \sigma) \approx D(\symbf x, \sigma)$ is called a **denoiser**.
- A model $S_\theta(\symbf x, \sigma)\approx S(\symbf x, \sigma)$ is called a **score estimator**.

Directly output $D(\symbf x, \sigma)$ may be a bad idea as its norm varies greatly with $\sigma$.

Let $c_{\text{loss}}, c_{\text{skip}}, c_{\text{out}}, c_{\text{in}} \in C(\R^+ \to \R^+)$ be scaling factors. EDM propose to parameterizes $D_\theta(\symbf x, \sigma)$ as
$$
D_\theta(\symbf x ; \sigma) = c_{\text {skip }}(\sigma) \symbf x +c_{\text {out }}(\sigma) F_\theta\p{c_{\text {in }}(\sigma) \symbf x ; \sigma}
$$
where $F_\theta(\symbf x, \sigma)$ is our neural network. The denoiser may be trained by score matching loss. For convenience, define $\symbf Y_{\sigma} := \symbf X_{\sigma^{-1}(\sigma)}$.

Suppose $\Sigma \sim p_{\text{train}}(\sigma)$ is an independent random variable representing the noise scale. And $\symbf N \sim \mathcal N(\symbf 0, \bI_n)$ is an independent noise.
$$
\begin{aligned}
\L_\theta &= E \s{c_{\text{loss}}(\Sigma) \norm{D_\theta(\symbf Y_{\Sigma};\Sigma) - \symbf X_0}_2^2} \\
& = E \s{c_{\text{loss}}(\Sigma) \norm{c_{\text {skip}}(\Sigma) \p{\symbf X_0 + \Sigma \symbf N} +c_{\text {out}}(\Sigma) F_\theta\p{c_{\text{in}}(\Sigma) \p{\symbf X_0 + \Sigma \symbf N} ; \Sigma} - \symbf X_0}_2^2}\\
& = E \s{\underbrace{c_{\text{loss}}(\Sigma) c_{\text{out}}^2(\Sigma)}_{\text{effective weight}} \norm{\underbrace{F_\theta\p{c_{\text{in}}(\Sigma) \p{\symbf X_0 + \Sigma \symbf N} ; \Sigma}}_{\text{neural network output}} -\underbrace{\p{\symbf X_0-c_{\text {skip}}(\Sigma) \p{\symbf X_0 + \Sigma \symbf N}}/{c_{\text{out}}(\Sigma)}}_{\text{effective training target}}}_2^2}\\
\end{aligned}
$$
Now following EDM, we derive appropriate choices of scaling factors.

- Suppose we have $\symbf X_0$ such that $\cov(\symbf X_0) = \sigma^2_{\text{data}}\bI_d$.

- Consider the input to the network $\symbf Y_\sigma$, it has variance
  $$
  \var(\symbf Y_{\sigma}) = \var(\symbf X_0 + \sigma \symbf N) = \var(\symbf X_0) + \sigma^2 \bI_n
  $$

  - For the input to have unit variance, take $c_{\text{in}}(\sigma) := 1 / \sqrt{\sigma^2 + \sigma^2_{\text{data}}}$.

- The variance of the effective training target is
  $$
  \begin{aligned}
  \var\p{\frac{1}{c_{\text{out}}(\sigma)}\p{\symbf X_0-c_{\text {skip}}(\sigma) \p{\symbf X_0 + \sigma \symbf N}}} = \frac{(1 - c_{\text{skip}}(\sigma))^2\sigma_{\text{data}}^2 + c_{\text{skip}}^2(\sigma)\sigma^2}{c_{\text{out}}^2(\sigma)}
  \end{aligned}
  $$

  - We want to make $c_{\text{out}}^2(\sigma)$ to be as low as possible, while the training target has unit variance.
    $$
    c_{\text{skip}}(\sigma) = \argmin{c_{\text{skip}}(\sigma)} c^2_{\text{out}}(\sigma), \quad \operatorname{s.t.}\quad  c_{\text{out}}^2(\sigma) = (1 - c_{\text{skip}}(\sigma))^2\sigma_{\text{data}}^2 + c_{\text{skip}}^2(\sigma)\sigma^2
    $$

  - There is a unique solution
    $$
    c_{\text{skip}}(\sigma) := \frac{\sigma_{\text{data}}^2}{\sigma^2 + \sigma_{\text{data}}^2},\quad c_{\text{out}}(\sigma) := \sqrt{(1 - c_{\text{skip}}(\sigma))^2\sigma_{\text{data}}^2 + c_{\text{skip}}^2(\sigma)\sigma^2} = \sigma \cdot \sigma_{\text{data}} / \sqrt{\sigma^2+\sigma_{\text{data}}^2}
    $$

- Empirically, we require the effective weight $c_{\text{loss}}(\sigma) c_{\text{out}}^2(\sigma)$ to be uniform so $c_{\text{loss}}(\sigma) = (\sigma^2 + \sigma_{\text{data}}^2) / (\sigma \cdot \sigma_{\text{data}})^2$.

##### Loss weighting

The loss of **multi-scale denoising score matching** can be written as:
$$
\L_\theta = \int_0^\infty w(\sigma) p(\sigma) \n{D_\theta(\symbf Y_\sigma; \sigma) - \symbf X_0}_2^2 \dd \sigma
$$
Where $w(\sigma)$ is the weighting function, and $p(\sigma)$ is the sample density function.

In different works with multi-scale denoising score-matching training, we have different choice of $w, p$.

In the EDM paper, $w(\sigma) = c_{\mathrm{loss}}(\sigma)$ defined above. And $\ln (\Sigma) \sim \mathcal N(-1.2, 1.2)$ where values of $\Sigma$ are clipped to $[0.002, 80]$. Notice that $\sigma_{\mathrm{data}} = 1 / 2$ in the paper.

