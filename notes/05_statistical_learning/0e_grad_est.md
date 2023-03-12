#### Gradient Estimation

> STA 4273 Winter 2021: [Minimizing Expectations](https://www.cs.toronto.edu/~cmaddis/courses/sta4273_w21/), [Chris Maddison](https://www.cs.toronto.edu/~cmaddis/), University of Toronto

##### Expectation minimization

Suppose $(O, \O, \mu)$ is a measure space. And $\mathcal Q$ is a set of density functions on $O$ with respect to $\mu$.

Suppose $f: O \times \mathcal Q \to \R$ is a function.

Let $X \sim q \in \mathcal Q$. We are interested in optimization problems of the form $\inf_{q \in \mathcal Q} E\s{f(X, q)}$.

This type of optimization is a recurring pattern in machine learning.

##### Gradient estimation

Continue above discussion. Suppose $f: O \times \R^D \to \R$ is a function.

Suppose $\mathcal Q = \c{q_\theta\mid \theta \in \R^D}$. And consider $J(\theta) := E\s{f(X, \theta)}$, where $X \sim q_\theta(x)$.

A gradient estimator is a random variable $G(\theta) \in \L(\Omega\to \R^D, \F)$.

- If $E[G(\theta)] = \nabla_\theta J(\theta)$, the estimator is called **unbiased**.
- $E\norm{G(\theta) - \nabla_\theta J(\theta)}^2_2$ is called the **variance** of the estimator.

##### Pathwise gradient estimator

Consider $J(\theta) = E\s{f(X, \theta)}$ following previous assumptions.

- Suppose there exists some random variable $R \in \L(\Omega \to E, \F/\E)$.
- Suppose for function $g: \E \times \R^D \to O$ such that $g(R, \theta) \sim q_\theta$.

Now suppose the exchange of integral and derivative is allowed, then
$$
\nabla_\theta E\s{f(X, \theta)} = \nabla_\theta E\s{f(g(R, \theta), \theta)} = E\s{\nabla_\theta f(g(R, \theta), \theta)}
$$
Now take $G(\theta) = \nabla_\theta f(g(R, \theta))$, the Monte Carlo estimator.

##### Gaussian reparameterization

For $X \sim q_\theta = \mathcal N(\mu_\theta, A_\theta A^*_\theta)$. Take a $R \sim \mathcal N(0, I)$, and notice $A_\theta R + \mu_\theta \sim X$.

##### Score function gradient estimator

Consider $J(\theta) = E\s{f(X, \theta)}$ following previous assumptions.
$$
\begin{aligned}
\nabla_\theta J(\theta) & = \nabla_\theta E \s{f(X, \theta)} = \nabla_\theta \int f(x, \theta) q_\theta(x) \dd x\\
& = \int \nabla_\theta f(x, \theta) q_\theta(x) \dd x + \int f(x, \theta) \nabla_\theta \log q_\theta(x) q_\theta(x) \dd x\\
& = E\s{\nabla_\theta f(X, \theta)} + E\s{f(X, \theta) \nabla_\theta \log q_\theta(X)}
\end{aligned}
$$
- $\nabla_\theta \log q_\theta(x)$ is also called the **score function**.
- Notice how the second term computes gradient before the sampling.

