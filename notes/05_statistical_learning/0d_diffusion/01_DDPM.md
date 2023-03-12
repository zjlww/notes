#### Denoising Diffusion Probabilistic Models

##### Derivation of DDPM

A diffusion model can be formulated as a variational Auto-encoder.

- Suppose $(X_n)_{n = 0}^T$ are random variables on the same space with values in $\R^d$.

- $X_0$ is the observed variable and $Z = (X_1, \ldots, X_T)$ are latent variables.

- The trainable **prior** is **factorized** as $p_\theta(x_0, \ldots, x_T) = p_\theta(x_T) \prod_{n = 1}^T p_\theta(x_{n - 1} | x_{n})$.

  - Where $p_\theta(x_T)$ is fixed as $\mathcal N(x_T; 0, I)$.

- Thus a diffusion model can be sampled with backward ancestral sampling. The process is also called the reverse (**denoising**) process.

- The **estimated posterior** $q(x_{1..T} | x_0)$ is fixed as a Markov chain.

  - Given a sequence of predefined $(\beta_n)_{n = 1}^T \in (0, 1)$.
    $$
    q(x_{1..T}|x_0) = \prod_{n=1}^T q(x_{n} | x_{n-1}) \quad q(x_n | x_{n-1}) = \mathcal N(x_n; \sqrt {1-\beta_n} x_{n-1}, \beta_n I)
    $$

- The conditional density $q(x_n | x_0)$ has closed form. Consider a fixed $x_0 \in \R^d$.

  - For $n \in 1.. T$ define $\alpha_n = 1 - \beta_n \in (0, 1)$ and $\bar \alpha_n = \prod_{k = 1}^n \alpha_k$.
    - $\alpha_n$ and $\bar \alpha_n$ strictly decreases from $1$ to a value close to $0$.
  - Just notice that $X_{n} = \sqrt{\beta_n}Z_n + \sqrt{1-\beta_n}X_{n-1}$ where $(Z_n)_{n=1}^T$ are standard Gaussians, and iterate on this formula.
  - The result is $X_n = \sqrt{1-\bar \alpha_n} E_n + \sqrt{\bar \alpha_n} x_0$.
    - $E_n$ is a standard gaussian and a function of $Z_1, \ldots, Z_n$.
  - And the density is given by $q(x_n | x_0) = \mathcal N(x_n ; x_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n )I)$.

- The ELBO is simplified through (by Jonathan Ho et al.)
  $$
  \begin{aligned}
  \mathcal L_\theta(x_0) &= E_{q(z|x_0)} \log p_\theta(x_0|z) - \d{q(z|x_0)}{p_\theta(z)}\\
  &= E_{q(z|x_0)} \left [
  \log p_\theta(x_0|z) - \log q(z|x_0) + \log p_\theta(z)
  \right]\\
  &= E_{q(x_{1..T}|x_0)} \left [
  \log p_\theta(x_0, x_{1..T}) - \log q(x_{1..T}|x_0)
  \right]\\
  &= E_{q(x_{1..T}|x_0)} \left [
  \log p_\theta(x_T) + \sum_{n=1}^T\log \frac{p_\theta(x_{n-1}|x_{n})}{q(x_n|x_{n-1})}\right ]\\
  &= E_{q(x_{1..T}|x_0)}
  \left [
  \log p_\theta(x_T) + \sum_{n=2}^T\log \frac{p_\theta(x_{n-1}|x_{n})}{q(x_n|x_{n-1})}
   + \log \frac{p_\theta (x_0 | x_1)}{q(x_1 | x_0)}
  \right ]\\
  &= E_{q(x_{1..T}|x_0)}
  \left [
  \log p_\theta(x_T) + \sum_{n=2}^T\log \frac{p_\theta(x_{n-1}|x_{n})}{q(x_{n-1}|x_{n}, x_0)}  + \sum_{n=2}^T\log  \frac{q(x_{n-1}|x_0)}{q(x_n|x_0)}
   + \log \frac{p_\theta (x_0 | x_1)}{q(x_1 | x_0)}
  \right ]\\
  &= E_{q(x_{1..T}|x_0)}
  \left [
  \log \frac{p_\theta(x_T)}{q(x_T|x_0)} + \sum_{n=2}^T\log \frac{p_\theta(x_{n-1}|x_{n})}{q(x_{n-1}|x_{n}, x_0)} 
   + \log p_\theta (x_0 | x_1)
  \right ]\\
  &= E_{q(x_{1..T}|x_0)}
  \left [
  \log p_\theta (x_0 | x_1)
   - \sum_{n=2}^T\d{q(x_{n-1}|x_n, x_0)}{p_\theta(x_{n-1}|x_n)} - \d{q(x_T|x_0)}{p_\theta(x_T)}
   \right ]\\
   &= E_{q(x_{1..T}|x_0)}
   \left [
   \log p_\theta (x_0 | x_1)
   - \sum_{n=2}^T\d{q(x_{n-1}|x_n, x_0)}{p_\theta(x_{n-1}|x_n)}
   \right ] + C
   \end{aligned}
  $$

- The conditional density $q(x_{n - 1} | x_n, x_0), n \in 2..T$ also has a closed form solution.

  - Just compute $q(x_{n-1}|x_{n}, x_0) = q(x_{n}|x_{n-1}, x_0)q(x_{n-1}|x_0)/q(x_n|x_0)$.

  - The simplification is horrible... **See below**.
    $$
    \begin{aligned}
    q(x_{n - 1} | x_n, x_0) &= \mathcal N\p{x_{n - 1}; \tilde \mu_n(x_n, x_0), \tilde \beta_n I}\\
    \quad \tilde\mu_{n}\left(x_n, x_0\right)& =\frac{\sqrt{\bar{\alpha}_{n-1}} \beta_{n}}{1-\bar{\alpha}_{n}} x_{0}+\frac{\sqrt{\alpha_{n}}\left(1-\bar{\alpha}_{n-1}\right)}{1-\bar{\alpha}_{n}} x_{n}; \quad \tilde{\beta}_{n}=\frac{1-\bar{\alpha}_{n-1}}{1-\bar{\alpha}_{n}} \beta_{n}
    \end{aligned}
    $$

- Parameterization of $p_\theta(x_{n - 1} |x_n)$, for $n \ge 2$, by (Ho et al.)

  - **Parameterize** $p_\theta(x_{n - 1} | x_n) = \mathcal N(x_{n - 1}; \mu_\theta(x_n, n), \Sigma_\theta(x_n, n))$.

  - Set $\Sigma_\theta(x_n, n) = \sigma_n^2 I$.

    - $\sigma_n^2 = \beta_n$ is optimal for $X_0 \sim \mathcal N(0, I)$. **See below.**
    - We will be **assuming** $\sigma_n^2 = \beta_n$ from now on.

  - Then by the analytic KL-divergence of isotropic Gaussians:
    $$
    D_\theta^{(n)}:= \d{q(x_{n - 1} | x_n, x_0)}{p_\theta(x_{n - 1} | x_n)} = C + \frac{\norm{\tilde \mu_n(x_n, x_0) - \mu_\theta(x_n, n)}^2_2}{2\sigma_n^2}
    $$

  - Denote the term of interest $J_\theta^{(n)} = \norm{\tilde \mu_n(x_n, x_0) - \mu_\theta(x_n, n)}^2_2$.

  - Denote the KL loss term $L_\theta^{(n)} = J_\theta^{(n)} / 2\sigma_n^2$.

  - Recall the prior is $q(x_n | x_0) = \mathcal N(x_n ; x_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n )I)$.

  - Recall that $X_n = \sqrt{1-\bar \alpha_n} E_n + \sqrt{\bar \alpha_n} x_0$.

  - Predicting $E_n$ which is a standard Normal variable seems to be a good choice.

  - Let $e_\theta(x_n, n)$ be the neural predictor of $E_n$.

    - Then $\mu_\theta(x_n, n) = \frac{1}{\sqrt{\alpha_n}}\left(x_n - \frac{\beta_n}{\sqrt{1 - \bar \alpha_n}} e_\theta(x_n, n)\right)$.
    - Denote $e_n = (x_n - x_0\sqrt{\bar \alpha_n}) / \sqrt{1 - \bar \alpha_n}$.
    - Then $J_\theta^{(n)} = \norm{\frac{1}{\sqrt{\alpha_n}}\left(x_n - \frac{\beta_n}{\sqrt{1 - \bar \alpha_n}} e_n\right) - \mu_\theta(x_n, n)}^2_2$.
    - And $L_\theta^{(n)} = \frac{\beta_n^2}{2\sigma_n^2 \alpha_n (1 - \bar \alpha_n)} \norm{e_n - e_\theta(x_n, n)}^2_2$.

  - Ho et al. propose to **ignore the weighting term** and optimize: $$
    \widetilde L_\theta^{(n)}:= \norm{e_n - e_\theta(x_n, n)}^2_2$$

- Notice that the parameterization of $p_\theta(x_0 | x_1)$ may depend on the problem in the DDPM framework.

- Song and Ho claim that $\widetilde L_\theta^{(n)}$ is implicit **denoising score matching**.

  - Define $s_\theta(x_n, n) = -e_\theta(x_n, n) / \sqrt{1 - \bar\alpha_n}$ following Song. Then immediately:
    $$
    \widetilde L_\theta^{(n)} = (1 - \bar \alpha_n) \norm{s_\theta(x_n, n) - \nabla_{x_n}\log q(x_n | x_0)}_2^2
    $$

- Song and Ho claim that the sampling process resembles **Langevin dynamics**:

  - Sample from $p(x_T)$ and for $n = T \to 1$: sample $z_n \sim N(0, I)$ and
    $$
    x_{n - 1} = \frac{1}{\sqrt{\alpha_n}}(x_n + \beta_n s_\theta(x_n, n)) + \sqrt{\beta_n} z_n
    $$

##### Derivation of the posterior

In the derivation above, we are required to simplify the following expression:
$$
q(x_{n-1}|x_{n}, x_0) = \frac{q(x_{n}|x_{n-1}, x_0)q(x_{n-1}|x_0)}{q(x_n|x_0)}
$$
Where we already know:

- $q(x_n | x_{n - 1}, x_0) = q(x_n | x_{n-1}) = \mathcal N(x_n; \sqrt {1-\beta_n} x_{n-1}, \beta_n I)$.
- $q(x_n | x_0) = \mathcal N(x_n ; x_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n )I)$.
- $q(x_{n-1} | x_0) = \mathcal N(x_{n - 1}; x_0 \sqrt{\bar \alpha_{n - 1}}, (1 - \bar \alpha_{n - 1}) I)$.

We can simplify with following knowledge:

- The result must be a density function.

- Each dimension is independent, so we can assume 1D case WLOG.
  $$
  \mathcal N(x; \mu, \sigma^2) = \frac{\exp \p{-(x-\mu)^2 / 2 \sigma^2)}}{\sigma \sqrt{2\pi}}; \quad \log \mathcal N(x; \mu, \sigma^2) = - \frac{1}{2\sigma^2} x^2 + \frac{\mu}{\sigma^2} x - \frac{1}{2 \sigma^2} \mu^2 + \text{const.}
  $$

- Take logarithm, and ignore the constants, the result must be a quadratic in $x_{n-1}$.

We now only need the quadratic and linear coefficient of $x_{n-1}$ to find the mean and variance!
$$
-\frac{1 - \bar \alpha_n}{2\p{1 - \bar \alpha_{n - 1}} \beta_n} x_{n - 1}^2 + \frac{\sqrt{\alpha_n} \p{1 - \bar \alpha_{n - 1}} x_n + \beta_n \sqrt{\bar \alpha_{n - 1}} x_0}{\beta_n (1 - \bar \alpha_{n - 1})} x_{n - 1} + \text{const.}
$$
Now compare gives:
$$
\sigma^2 = \frac{\p{1 - \bar \alpha_{n - 1}}\beta_n}{(1 - \bar \alpha_n)}; \quad \mu = \frac{\sqrt{\alpha_n} \p{1 - \bar \alpha_{n - 1}} x_n + \beta_n \sqrt{\bar \alpha_{n - 1}} x_0}{\p{1 - \bar \alpha_n}}
$$
##### Choice of variance

Consider the following alternative derivation of $\L_\theta(x_0)$:
$$
\begin{aligned}
\L_\theta(x_0) & = E_{q(x_{1..T}|x_0)} \left [
\log p_\theta(x_T) + \sum_{n=1}^T\log \frac{p_\theta(x_{n-1}|x_{n})}{q(x_n|x_{n-1})}\right ]\\
& = E_{q(x_{1..T}|x_0)} \left [
\log p_\theta(x_T) + \sum_{n=1}^T\log \left (\frac{p_\theta(x_{n-1}|x_{n})}{q(x_{n-1}|x_{n})} \cdot \frac{q(x_{n-1})}{q(x_n)}\right)\right ]\\
& = E_{q(x_{1..T}|x_0)} \left [
\log \frac{p_\theta(x_T)}{q(x_T)} + \sum_{n=1}^T\log \frac{p_\theta(x_{n-1}|x_{n})}{q(x_{n-1}|x_{n})} + \log q(x_0)\right]\\
& = -\d{q(x_T)}{p_\theta(x_T)} - E_{q(x_{1..T}|x_0)}\d{q(x_{n - 1} | x_n)}{p_\theta(x_{n-1}|x_n)} + \log q(x_0)
\end{aligned}
$$
The optimal variance for $p_\theta(x_{n - 1} | x_n)$ can be derived from $q(x_{n - 1} | x_n)$ if it is also diagonal Normal.

When $q_0(x_0) = \delta(x_0 - c_0)$, then

- $q(x_{n-1} | x_n) = q(x_{n-1} | x_n, x_0)$.
- Clearly $\sigma_n := \tilde{\beta}_{n}=\frac{1-\bar{\alpha}_{n-1}}{1-\bar{\alpha}_{n}} \beta_{n}$ minimizes the KL divergence.

When $q_0(x_0) = \mathcal N(x_0; 0, I)$, then 

- $q(x_{n-1} | x_n) = {q(x_{n-1}) q(x_n | x_{n - 1})} /{q(x_n)}$.
  - $q(x_n) = \mathcal N(x_n; 0, I)$, $q(x_{n-1}) = \mathcal N(x_{n-1}; 0, I)$.
  - $q(x_n | x_{n - 1}) = \mathcal N(x_n; \sqrt {1-\beta_n} x_{n-1}, \beta_n I)$.
- Therefore $q(x_{n - 1} | x_n) = \mathcal N(x_{n-1}; \sqrt{1 - \beta_n} x_n, \beta_n I)$, which is **quite symmetric**.
- Clearly $\sigma_n := \beta_n$ is the optimal choice here.

(**A discretized continuous distribution for image synthesis**)

The range [0, 255] is scaled linearly to [-1, 1] as input to the neural network. In order to obtain a discrete log likelihood the decoder $p_\theta(x_0 | z)$ is defined to be following
$$
p_\theta(x_0 | z) = p_\theta(x_0 | x_1) = \prod_{i=1}^D \int_{\delta_-(x_0^i)}^{\delta_+(x_0^i)} \mathcal N(x; \mu_\theta^i (x_1, 1), \sigma_1^2) dx
$$

$$
\delta_{+}(x)=\left\{\begin{array}{ll}
\infty & \text { if } x=1 \\
x+\frac{1}{255} & \text { if } x<1
\end{array}\right. \quad \delta_{-}(x)=\left\{\begin{array}{ll}
-\infty & \text { if } x=-1 \\
x-\frac{1}{255} & \text { if } x>-1
\end{array}\right.
$$

where $D$ is the data dimensionality, and $i$ is the superscript indicating extraction of one coordinate.

In training, we just assume that the data is a continuous distribution on $\R^D$.
$$
L'(\theta, n) = E_{x_0 \sim p^*(x), e\sim \mathcal N(0, I)}\left [
\|e - e_\theta(x_t(x_0, e), t)\|^2
\right ]
$$
For $t > 1$, this is approximating $L_{t-1}$ by ignoring all constants, which makes the training a weighted variant of the ELBO. For $t = 0$, this is
$$
L'(\theta, 1) = \frac{1}{2\sigma_1^2}\left \|x_0 - \mu_\theta(x_t, t) 
\right \|^2
$$
Which is exactly $\log p_\theta(x_0 | x_1)$.