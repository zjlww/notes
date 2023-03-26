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
