#### Energy-Based Models

##### Energy-based models

Measurable space $(X, \F)$ is called the **state space** of the model. $X$ can be $\R^d$ or $\{1, \ldots, k\}$, and so on.

$f_\theta(x): X \to \R$ with parameter $\theta \in \Theta$ is called a **energy function**.

- As a non-standard notation, we define energy and potentials:
  - $U_\theta(x): X \to \R$ is the potential function. Higher potential states are more stable and has higher density.
  - $E_\theta(x): X \to \R$ is the energy function. Lower energy states are more stable states.
  - And we use the convention that $p_\theta(x) \propto \exp(-U_\theta(x)) \propto \exp(E_\theta(x))$.

The normalizing constant $Z_\theta = \int_{X} e^{- U_\theta(x)} \dd x$ is called the **partition function**. Which is usually **intractable**.

EBMs are **unnormalized probability density models**. The probability measure of the energy-based model is $\dd P_\theta(A) := f_\theta(x) / Z_\theta\dd x$.

- A distribution of the form $P_\theta$ is called a **Gibbs distribution**.

##### Score-based models

Suppose $p(x): \R^d \to [0, \infty)$ is a differentiable density function.

A model $s_\theta(x): \R^d \to \R^d$ matching the score $s_\theta(x) \approx \nabla_x \log p(x)$ is called a **score-estimator**.

- Energy-based models on $\R^d$ can be transformed into score-based models.
  - The score is just $-\nabla_x U_\theta(x)$ or $\nabla_x E_\theta(x)$.
- Score-based models on $\R^d$ could be transformed into energy-based models.
  - Suppose $s_\theta(x)$ describes a conservative vector field. Path integrals recover the energy function.

> See this [wikipedia page](https://en.wikipedia.org/wiki/Conservative_vector_field) on conservative vector fields.

##### Contrastive divergence algorithm

Continue from (**EBMs**). Let $p(x): \R^d \to (0, \infty)$ be the target density.

- We want to optimize the forward $\d{p}{p _ \theta}$ where $p _ \theta(x) = \exp(-U _ \theta(x)) / Z _ \theta$.
- $\nabla_\theta \log p_\theta(x) = -\nabla_\theta U_\theta(x) - \nabla_\theta \log Z_\theta$. Consider the following:
  $$
  \begin{aligned}
  \nabla_\theta \log Z_\theta & = \frac{1}{Z_\theta} \nabla_\theta Z_\theta = \frac{1}{Z_\theta} \nabla_\theta \int \exp (-U_\theta(x)) dx  = \frac{-1}{Z_\theta} \int \exp (-U_\theta(x)) \nabla U_\theta(x) dx\\
  & = - \int p_\theta(x) \nabla U_\theta(x) dx = - E_{p_\theta(x)} [\nabla_\theta U_\theta(x)]
  \end{aligned}
  $$
- The EBM training algorithm based on the following called the **Contrastive divergence algorithm**.
  $$
  \nabla_\theta E_{X \sim p(x)} \s{\log p_\theta(X)} = E_{X \sim p(x)} \s{\nabla_\theta E_\theta(X)} - E_{X \sim p_\theta(x)} \s{\nabla_\theta E_\theta(X)}, \quad (*)
  $$

##### Langevin dynamics

Continue from (**SBMs**). This method is for sampling from a SBM.

- The SDE $dX_t = - \nabla U(X_t) dt + \sigma dB_t$ for $t \in [0, \infty)$.
  - Also consider the following **discretization** for step $\Delta t$.
    $$
    X_{t + \Delta t} - X_t = -\nabla U(X_t) \Delta t + \sigma \sqrt{\Delta t} Z, \quad Z \sim N(0, I)
    $$
  - The forward PDE for density on $t \in (0, \infty)$ is given by:
    $$
    \begin{aligned}
    \part_t p(t, x) & = \L^* p(t, x) = - \nabla \cdot (\nabla U(x) p(t, x)) + \nabla^2 :(\sigma^2 p(t, x))\\
    & = \nabla_x p(t, x)^T \nabla U(x) + \operatorname{div} \nabla U(x) p(t, x) + \frac{1}{2} \sigma^2 \Delta p(t, x)
    \end{aligned}
    $$
- (**TODO**) For $T = \sigma^2 / 2$ and $p_G(x) = \exp(-U(x) / T) / Z$ is a stable distribution.
  - Let $p(0, x) = p_G(x)$, then $p(t, x) = p_G(x)$ is a solution to the forward SDE.
- Given **energy-based** model $U(x): \R^d \to \R$ leading to density $p(x) = \exp(-U(x)) / Z$.
  - To sample from $p(x)$, set $T = 1$ and $\sigma = \sqrt{2}$ and run the Langevin SDE.
- Given **score-based** model $s(x) \approx \nabla \log p(x)$.
  - Define $U(x) = -\log p(x)$. This is the corresponding energy function.
  - Notice that $-\nabla U(x) = \nabla \log p(x) \approx s(x)$.
  - To sample from $p(x)$, we can run Langevin SDE $dX_t = s(x) dt + \sqrt 2 dB_t$.
- Typically in the literature, the Langevin SDE is **discretized** into  
  $$
  x_{n + 1} = x_n - \frac{\epsilon}{2} \nabla U(x_t) + \sqrt{\epsilon} Z; \quad Z \sim N(0, I)
  $$
  The discretization is not necessarily reasonable, there are some theoretical analyses of it.

##### Metropolis-Hastings Markov chain Monte Carlo ==TODO==

Continue from (**EBMs**).

- $x_0 \sim \pi(x)$ be some initial sampling method.
- Continue the following iteration for $n = 0, 1, 2, \ldots, N - 1$.
  - $x' = x_n + Z_n$ where $Z_n$ is some random noise.
  - If $E_\theta(x') \ge E_\theta(x_n)$, set $x_{n + 1} = x'$.
  - Else $E_\theta(x') < E_\theta(x_n)$,
    - Set $x_{n + 1} = x'$ with probability $\alpha = \exp(E_\theta(x') - E_\theta(x_n))$.
    - Set $x_{n + 1} = x_n$ with probability $1 - \alpha$.
- In theory, $x_n$ converges to $p_\theta(x)$ when $n \to \infty$.
- Convergence slows down exponentially in dimensionality.
