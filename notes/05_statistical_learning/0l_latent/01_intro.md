##### Probabilistic models

A family of distributions $\mathcal Q$ on some measurable space $(\Omega, \F)$ is a **probabilistic model**.

$\mathcal Q$ can be parameterized by parameter $\theta$ in some parameter space $\Theta$. In this case, we often denote the distribution as $Q_\theta$, and the density as $q_\theta$. And the model is called a parametric probability model.

We may have different ways of constructing $\mathcal Q$, leading to different properties of $q \in \mathcal Q$.

- Whether sampling from $q$ is tractable.
- Whether computing $\log q(x)$ is tractable.
- Whether computing the gradient $\part \log q_\theta(x) / \part \theta$ is tractable.

##### Latent variable models

Consider measurable space $(\Omega, \F)$ and following random variables.

- $Z \in \L(\Omega \to E, \F/\E)$ is the **latent** random variable with values in $(E, \E, \nu)$.
- $X \in \L(\Omega \to O, \F/\O)$ is **observed** random variable with values in $(O, \O, \mu)$.
- For the measures $\mu$ and $\nu$:
  - They are usually the counting measure for finite spaces.
  - They are usually the Lebesgue measure for Euclidean spaces.
  - In the following we will only write $\dd z$ and $\dd x$ in the integral. We actually mean $\dd \nu(z)$ and $\dd \mu(x)$.

A **latent variable model** is the joint distribution of $(Z, X)$ on measurable space $(E \times O, \E \otimes \O)$.

- Such a distribution may have parameter $\theta \in \Theta$.
- We often write $\mathcal Z = Z[\Omega]$, and similarly $\X = X[\Omega]$.

We sometimes consider the "observed data" as a random variable $X_* \in \L(\Omega_* \to O, \F_*/\O)$ as well.

==TODO== We assume all densities and conditional densities exists over $\nu \times \mu$.

- The density $p_\theta(z, x)$ fully describes a latent variable model.
- $p_*(x_*)$ is called the data density.

The **learning problem** is to minimize some divergence between the data distribution and the model marginal distribution. For example we could minimize the KL divergence:
$$
\hat \theta = \argmin{\theta \in \Theta}\d{X_*}{X} = \argmin{\theta \in \Theta} \int_{\O} p_* (x) \log \frac{p_*(x)}{p_\theta(x)} \dd x
$$

- Suppose $p_*(x) = \sum_{i=1}^N \delta(x_i) / N$. This becomes minimizing log likelihood.
  $$
  \what \theta = \argmin{\theta \in \Theta} \frac{1}{N}\sum_{i = 1}^N -\log p_\theta(x_i)
  $$

The **inference problem** is to find $p_\theta(z | x)$.
$$
\what z := \argmax{z \in \mathcal Z} \log p_\theta(z|x)
$$

##### Evidence Lower Bound (ELBO)

Suppose $p(z, x)$ is a latent variable model. Given density $\what Z \sim q(z)$, and $Z \sim p(z)$ observe:
$$
\begin{aligned}
\log p(x) & = \log \int p(z, x) \dd z = \log \int p(x | z) p(z) \dd z = \log \int \frac{p(x | z) p(z)}{q(z)} q(z) \dd z\\
& \ge \int \log \frac{p(x | z) p(z)}{q(z) } q(z) \dd z = E\s{\log \frac{p(\what Z, x)}{q(\what Z)}}
\end{aligned}
$$
Define the evidence lower bound (**ELBO**) given density $q(z)$, model $p(z, x)$ and a sample $x$. Let $\what Z \sim q(z)$.
$$
\newcommand{\elbo}{\operatorname{ELBO}}
\begin{aligned}
\elbo(p, q, x) &:= E\s{\log \frac{p(\what Z, x)}{q(\what Z)}} = E\s{\log \frac{p(\what Z | x)}{q(\what Z)}} + \log p(x)\\
&= \log p(x) -\d{q(z)}{p(z | x)} \le \log p(x)
\end{aligned}
$$

Also notice that
$$
\begin{aligned}
\elbo(p, q, x) &= E\s{\log \frac{p(x | \what Z)}{q(\what Z)} + \log q(\what Z)} + E\s{\log p(\what Z) - \log q(\what Z)}\\
& = E\s{\log p(x|\what Z)} - \d{q(z)}{p(z)}
\end{aligned}
$$

##### Variational inference

Suppose $p(z, x)$ is a latent variable model. Suppose $\mathcal Q$ is a family of densities on $\mathcal Z$.

**Variational inference** provides an approximate solution of the **inference problem**.

The following is the **variational objective**:
$$
q^* := \argmax{q \in \mathcal Q} \elbo(p, q, x)
$$

- Clearly $q^*(z) = p(z | x)$ when $\mathcal Q$ is general enough.

The main idea of variational inference is to **restrict** the family $\mathcal Q$ to make this optimization (more) tractable.

- The **mean-field assumption** is to assume coordinate independence in $\mathcal Q$, $q( z )=\prod_{j=1}^m q_j(z_j)$.
- Coordinate ascent mean-field variational inference (**CAVI**) is a general optimization routine for the variational problem under the mean-field assumption that performs coordinate descent by optimizing on $q_j$ at a time, holding the others fixed.


##### EM algorithm

Suppose $p_\theta(z, x)$ is a parameterized latent variable model. And $p_*(x)$ is the data density.

The **EM algorithm** provides a iterative solution to the **learning problem**, with the following coordinate ascent iteration:

- Define density $q[x_*, \theta](z)$ as $q(x_*) := \max_{q \in \mathcal Q} \elbo(p_\theta, q, x_*)$.
- Now update $\theta \to \theta'$ with $\theta' = \argmax{\theta' \in \Theta} E\s{\elbo(p_{\theta'}, q[X_*, \theta], X_*)}$.

When $\mathcal Q$ is appropriate, such that $q[x_*, \theta] =p_\theta(z|x_*)$ for all $x_*$. $E[\log p_\theta(X_*)]$ increases in each EM iteration.
$$
E\s{\log p_{\theta'}(X_*)} \ge E\s{\elbo(p_{\theta'}, q[X_*, \theta], X_*)} \ge E\s{\elbo(p_\theta, q[X_*, \theta], X_*)} = E\s{\log p_\theta(X_*)}
$$

