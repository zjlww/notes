#### Continuous-Time Diffusion Models: EDM Formulation

> We give an introduction following the mathematical framework proposed in this paper (EDM). It managed to decouple the score estimator and the sampling process.
>
> Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the Design Space of Diffusion-Based Generative Models. *ArXiv, abs/2206.00364*.

Let $(\mathbf B_t)$ be a $n$-dimensional standard Brownian motion, and $(\mathbf {\wbar B})_t$ be an $n$-dimensional reverse Brownian motion.

##### Driftless diffusion

Suppose $(\mathbf X_t)$ is the following diffusion process, it is called a **driftless diffusion**. For strictly increasing $\sigma(t) \in C^1([0, T] \to \R^+)$.
$$
\dd \mathbf X_t = \sqrt{2\dot \sigma(t)\sigma(t)} \dd \mathbf B_t, \quad \mathbf X_0 \sim p(\mathbf x; 0), \quad t \in [0, T]
$$
Where $p(\mathbf x; 0)$ is the data density on $\R^n$. Equivalently $\mathbf X_t$ can be viewed as adding noise to $\mathbf X_0$ in the following way,
$$
\mathbf X_t = \mathbf X_0 + \int_0^t \sqrt{2\dot \sigma(\tau)\sigma(\tau)} \dd \mathbf B_\tau, \quad \int_0^t \sqrt{2\dot \sigma(\tau)\sigma(\tau)} \dd \mathbf B_\tau \sim \mathcal N\p{\mathbf 0, \sigma^2(t)\bI_n}, \quad t \in [0, T]
$$

Denote the density of $\mathbf X_t$ as $p(\mathbf x; \sigma(t))$.

Then according to weak-sense time reversal, we have the reverse diffusion for $\lambda(t)\in C([0, T] \to \R^+)$:
$$
\dd \mathbf X_t = -(1 + \lambda(t)) \dot \sigma(t) \sigma(t) \nabla_{\mathbf x} \log p(\mathbf X_t; \sigma(t)) \dd t + \sqrt{2 \lambda (t)\dot \sigma(t)\sigma(t)}\dd \mathbf {\wbar B}_t,\quad t \in [T, 0]
$$
The $\beta(t)$ in EDM is defined as $\beta(t) = \lambda(t) \dot \sigma(t) / \sigma(t)$. By taking $\beta(t) = \lambda(t) = 0$, we will obtain the probability flow ODE.

##### Scaled driftless diffusion

Suppose $(\mathbf {X}_t)$ is a driftless diffusion, and $\mathbf {\what X}_t = s(t) \mathbf {X}_t$ for some scaling function $s(t) \in C^1([0, T]\to \R^+)$ where $s(0) = 1$.

Now by Itô's formula, it has stochastic differential
$$
\dd \mathbf {\what X}_t = \dot s(t) \mathbf {X}_t \dd t + s(t) \dd \mathbf {X}_t = \frac{\dot s(t)}{s(t)} \mathbf {\what X}_t \dd t + s(t) \sqrt{2 \dot \sigma(t) \sigma(t)} \dd \mathbf B_t, \quad \mathbf {\what X}_0 =  \mathbf {X}_0, \quad t \in [0, T]
$$
By definition we have
$$
\mathbf {\what X}_t = s(t) \mathbf {X}_0 + s(t)\int_0^t \sqrt{2\dot \sigma(\tau)\sigma(\tau)} \dd \mathbf B_\tau, \quad t \in [0, T]
$$
Denote the density of $\mathbf {\what X}_t$ as $\what p(\mathbf { x}; \sigma(t))$. Then
$$
\log \what p(\mathbf x; \sigma(t)) = -n \log s(t) + \log  p\p{\frac{\mathbf x}{s(t)}; \sigma(t)}
$$
Actually we could compute $\nabla \log \what p(\mathbf x; \sigma)$ from $\nabla \log p(\mathbf x; \sigma)$.
$$
\nabla_{\mathbf x} \log \what p(\mathbf x; \sigma(t)) = \frac{1}{s(t)}\nabla_{\mathbf x} \log p\p{\frac{\mathbf x}{s(t)}; \sigma(t)}
$$
Similar to driftless diffusion, we have reverse diffusion:
$$
\dd \mathbf {\what X}_t = \p{\frac{\dot s(t)}{s(t)} \mathbf {\what X}_t - (1 + \lambda(t))s(t)\dot \sigma(t) \sigma(t) \nabla_{\mathbf x} \log p\p{\frac{\mathbf {\what X}_t}{s(t)}; \sigma(t)}} \dd t + s(t) \sqrt{2 \lambda(t)\dot \sigma(t) \sigma(t)} \dd \mathbf B_t,\quad t \in [T, 0]
$$

##### The denoising function and the score function

Define the score function $S(\mathbf x, \sigma): \R^n \times \R^+ \to \R^n$ as
$$
S(\mathbf x, \sigma) = \argmin{S} E {\norm{S(\mathbf X_0 + \sigma \mathbf N, \sigma) - \frac{\mathbf N}{\sigma}}^2_2} = \nabla \log p(\mathbf x; \sigma)
$$
Define the denoising function $D(\mathbf x, \sigma): \R^n \times \R^+ \to \R^n$ as $D(\mathbf x, \sigma) := E[\mathbf X_0 | \mathbf Y_{\sigma} = x]$.

According to tweedie's formula, we have the following relationship:
$$
D(\mathbf x, \sigma) = \mathbf x - S(\mathbf x, \sigma) \sigma^2  = \mathbf x - \sigma^2\nabla \log p(\mathbf x; \sigma)
$$
Let $\mathbf N \sim \mathcal N(\mathbf 0, \bI_n)$ be independent to all other variables. Then $D(\mathbf x, \sigma)$ is the function such that
$$
D(\mathbf x, \sigma) = \argmin{D}  E\n{D(\mathbf X_0 + \sigma \mathbf N, \sigma) - \mathbf X_0}_2^2
$$

##### Hyperparameters in diffusion

The choice of $\lambda(t)$, $s(t)$, and $\sigma(t)$ changes the reverse diffusion process, therefore the truncation error when applying numerical solvers to them.

In EDM, the authors proposed $\lambda(t) = 0$, $\sigma(t) = t$ and $s(t) = 1$ for the probability flow ODE.

- Suppose $\mathbf x(t)$ is a solution of the probability flow ODE, then
  $$
  \dot {\mathbf x}(t) = -t\nabla_{\mathbf x} \log p(\mathbf x(t), t) = \frac{D(\mathbf x(t), t) - \mathbf x(t)}{t}
  $$

- The tangent vector at $\mathbf x(t)$ is pointing towards the denoised data $D(\mathbf x(t), t)$, which is largely stable. So the solution trajectory is mostly linear.

##### Denoising models and score estimators

We may use a neural network to approximate either $D(\mathbf x, \sigma)$ or $S(\mathbf x, \sigma)$.

- A model $D_\theta(\mathbf x, \sigma) \approx D(\mathbf x, \sigma)$ is called a **denoiser**.
- A model $S_\theta(\mathbf x, \sigma)\approx S(\mathbf x, \sigma)$ is called a **score estimator**.

Directly output $D(\mathbf x, \sigma)$ may be a bad idea as its norm varies greatly with $\sigma$.

Let $c_{\text{loss}}, c_{\text{skip}}, c_{\text{out}}, c_{\text{in}} \in C(\R^+ \to \R^+)$ be scaling factors. EDM propose to parameterizes $D_\theta(\mathbf x, \sigma)$ as
$$
D_\theta(\mathbf x ; \sigma) = c_{\text {skip }}(\sigma) \mathbf x +c_{\text {out }}(\sigma) F_\theta\p{c_{\text {in }}(\sigma) \mathbf x ; \sigma}
$$
where $F_\theta(\mathbf x, \sigma)$ is our neural network. The denoiser may be trained by score matching loss. For convenience, define $\mathbf Y_{\sigma} := \mathbf X_{\sigma^{-1}(\sigma)}$.

Suppose $\Sigma \sim p_{\text{train}}(\sigma)$ is an independent random variable representing the noise scale. And $\mathbf N \sim \mathcal N(\mathbf 0, \bI_n)$ is an independent noise.
$$
\begin{aligned}
\L_\theta &= E \s{c_{\text{loss}}(\Sigma) \norm{D_\theta(\mathbf Y_{\Sigma};\Sigma) - \mathbf X_0}_2^2} \\
& = E \s{c_{\text{loss}}(\Sigma) \norm{c_{\text {skip}}(\Sigma) \p{\mathbf X_0 + \Sigma \mathbf N} +c_{\text {out}}(\Sigma) F_\theta\p{c_{\text{in}}(\Sigma) \p{\mathbf X_0 + \Sigma \mathbf N} ; \Sigma} - \mathbf X_0}_2^2}\\
& = E \s{\underbrace{c_{\text{loss}}(\Sigma) c_{\text{out}}^2(\Sigma)}_{\text{effective weight}} \norm{\underbrace{F_\theta\p{c_{\text{in}}(\Sigma) \p{\mathbf X_0 + \Sigma \mathbf N} ; \Sigma}}_{\text{neural network output}} -\underbrace{\p{\mathbf X_0-c_{\text {skip}}(\Sigma) \p{\mathbf X_0 + \Sigma \mathbf N}}/{c_{\text{out}}(\Sigma)}}_{\text{effective training target}}}_2^2}\\
\end{aligned}
$$
Now following EDM, we derive appropriate choices of scaling factors.

- Suppose we have $\mathbf X_0$ such that $\var(\mathbf X_0) = \operatorname{diag}(\sigma^2_{\text{data}})$.

- Consider the input to the network $\mathbf Y_\sigma$, it has variance
  $$
  \var(\mathbf Y_{\sigma}) = \var(\mathbf X_0 + \sigma \mathbf N) = \var(\mathbf X_0) + \sigma^2 \bI_n
  $$

  - For the input to have unit variance, take $c_{\text{in}}(\sigma) := 1 / \sqrt{\sigma^2 + \sigma^2_{\text{data}}}$.

- The variance of the effective training target is
  $$
  \begin{aligned}
  \var\p{\frac{1}{c_{\text{out}}(\sigma)}\p{\mathbf X_0-c_{\text {skip}}(\sigma) \p{\mathbf X_0 + \sigma \mathbf N}}} = \frac{(1 - c_{\text{skip}}(\sigma))^2\sigma_{\text{data}}^2 + c_{\text{skip}}^2(\sigma)\sigma^2}{c_{\text{out}}^2(\sigma)}
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

- Empirically, we require the effective weight $c_{\text{loss}}(\sigma) c_{\text{out}}^2(\sigma)$ to be uniform so $c_{\text{loss}}(\sigma) = (\sigma^2 + \sigma_{\text{data}}^2) / (\sigma \cdot \sigma_{\text{data}})$.
