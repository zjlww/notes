#### Discrete Time Normalizing Flows

> Papamakarios, G., Nalisnick, E.T., Jimenez Rezende, D., Mohamed, S., & Lakshminarayanan, B. (2019). Normalizing Flows for Probabilistic Modeling and Inference. *J. Mach. Learn. Res., 22*, 57:1-57:64.

##### Review: Change of variable ==TODO==

Suppose $f: \R^d \to \R^d$ is a non-degenerate $C^1$-diffeomorphism (or just **smooth** in this section).

- $f$ is a bijection with inverse $\phi^{-1}$.
- $f \in C^1(\R^d \to \R^d)$ and $f^{-1} \in C^1(\R^d \to \R^d)$.
- $\forall x \in \R^d: \abs{\det f'(x)} > 0$.

Suppose $p_X(x) \in \L^1(\R^d \to [0, \infty])$ is a **probability density**. Suppose on some probability space $X \sim p_X(x)$.

Let $Y = f(X) \sim p_Y(y)$. Suppose $y = f(x)$, then
$$
p_Y(y) = \frac{p_X(f^{-1}(y))}{\abs{\det f'(f^{-1}(y))}}, \quad p_X(x) = p_Y(f(x)) \abs{\det f'(x)}
$$
Take logarithm on both sides gives:
$$
\begin{aligned}
\log p_Y(y) &= \log p_X(f^{-1}(y)) - \log \abs{\det f'(f^{-1}(y))}\\
\log p_X(x) &= \log p_Y(f(x)) + \log \abs{\det f'(x)}
\end{aligned}
$$

##### Flows for generative modeling

Suppose $Z \sim p_{\psi}(z)$ where $p_{\psi}(z) \in \L^1(\R^d \to [0, \infty])$ is a density function parameterized by $\psi \in \Psi$.

Suppose $f_\theta: \R^d \to \R^d$ is a parameterized non-degenerate $C^1$-diffeomorphism. Let $X = f_\theta(Z) \sim p_{\theta, \psi}(x)$.

To sample from $p_X(x)$:

- First sample $z$ from $p_Z(z)$.
- Then apply transform $x = f(z) \sim p_X(x)$.

To evaluate $\log p_X(x)$:

- First compute $z = f^{-1}(x)$.
- Then compute $\log\abs{\det f'(z)}$ and $\log p_Z(z)$. Since $\log p_X(x) = \log p_Z(z) - \log \abs{\det f'(z)}$.

Notice that **efficient** sampling, and log probability evaluation have different requirements.

- Efficient sampling requires fast sampling from $p_Z$ and fast transform $f_\theta$.
- Efficient evaluation requires fast inverse $f^{-1}$ , fast evaluation of $\log p_Z(z)$, and fast evaluation of $\log \abs{\det f'(z)}$.

Suppose $X_* \sim p_*(x)$ is a **data density** on $\R^d$. Training with the forward KL is
$$
\d{p_*}{p_X} = \int_{\R^d} p_*(x) \log \frac{p_*(x)}{p_X(x)} \dd x = - \int_{\R^d} p_*(x) \log p_X(x) \dd x + \const
$$

##### Flows for generative modeling: a normalizing transformation

Continue the discussion above. Let $Z_* = \phi^{-1}(X_*) \sim p_{Z_*}(f(z)) \abs{\det f'(z)}$. Note that $Z \sim p_Z(z) = p_X(f(z)) \abs{\det f'(z)}$.
$$
\begin{aligned}
\d{p_*}{p_X} & = \int_{\R^d} p_*(x) \log \frac{p_*(x)}{p_X(x)} \dd x\\
&= \int_{\R^d} p_*(f(z)) \log \frac{p_*(f(z))}{p_X(f(z))} \abs{\det f'(z)} \dd z = \d{p_{Z_*}}{p_Z}
\end{aligned}
$$
In the context of generative models, a flow model can be interpreted as normalizing the data distribution, and transform it into the tractable prior distribution $p_Z$.

##### Flows for variational inference

Suppose $p(z, x)$ is a latent variable model, where $z \in \R^d$. Let the family of approximate posteriors $\mathcal Q$ in **variational inference** be a flow model.

Suppose $U \sim q_\phi(u)$ is the prior distribution, and $\what Z = f_\phi(U) \sim q_{\what Z}(z)$ has a density parameterized by a flow model.

$$
\newcommand{\elbo}{\operatorname{ELBO}}
\begin{aligned}
\elbo(p, q_\phi, x) & = E \s{\log \frac{p(\what Z, x)}{q_\phi(\what Z)}} = - \d{q_\phi(z)}{p(z|x)} + \log p(x)\\
& = \int_{\R^d} \log \frac{p(z, x)}{q_\phi(z)} q_\phi(z) \dd z = \int_{\R^d} \log \frac{p(f_\phi(u), x)}{q_\phi(f_\phi(u))} q_{\phi}(f_\phi(u)) \abs{\det f_\phi'(u)}\dd u\\
& = \int_{\R^d} \log \frac{p(f_\phi(u), x)}{q_\phi(u)/\abs{\det f_{\phi}'(u)}} q_\phi(u) \dd u\\
& = E[\log p(f_\phi(U), x)] + H(U) + E\s{\log \abs{\det f'_\phi(U)}}
\end{aligned}
$$
Flow models in the context of variational inference can be thought of implementing a generalized reparameterization trick.

For efficient optimization of the ELBO, we need fast sampling of $U$ and fast evaluation of $\log \abs{\det f_\phi'(u)}$.

##### Flows for enhancing approximate posteriors in VAEs

> Jimenez Rezende, D., & Mohamed, S. (2015). Variational Inference with Normalizing Flows. *International Conference on Machine Learning*.
>
> Kingma, D.P., Salimans, T., Józefowicz, R., Chen, X., Sutskever, I., & Welling, M. (2016). Improving Variational Autoencoders with Inverse Autoregressive Flow. *NIPS*.

Similar to the case of variational inference, amortized variational inference in VAEs also benefits from flow transforms.

Suppose the approximate posterior is a density function $q_{\phi}(z | x)$ on $\R^d$, and $\wtilde Z \sim q_\phi(z | x)$.

Suppose $f_\eta: \R^d \to \R^d$ is smooth. And $\what Z = f_\eta(\wtilde Z) \sim q_{\phi, \eta}(z|x)$.

$$
\begin{aligned}
\elbo(p_\theta, q_{\phi, \eta}, x) & := E\s{\log \frac{p_\theta(x | \what Z) p_\theta(\what Z)}{q_{\phi, \eta}(\what Z | x)}} = \int \log \frac{p_\theta(x, \what z)}{q_{\phi, \eta}(\what z | x)} q_{\phi, \eta} (\what z | x) \dd \what z\\
& = \int \log \frac{p_\theta(x, f_\eta(\wtilde z))}{q_{\phi}(\wtilde z | x) \abs{\det f_\eta'(\wtilde z)}} q_\phi(\wtilde z | x) \dd \wtilde z\\
& = \log p_\theta(x) - \boxed{\d{q_\phi(\wtilde z | x)}{\frac{p_\theta(f_\eta(\wtilde z) | x))}{\abs{\det f'_\eta(\wtilde z)}}}}\\
& = E\s{\log p_\theta(x, f_\eta(\wtilde Z))} + H(\wtilde Z) - E\s{\log \abs{\det f'_\eta(\wtilde Z)}}
\end{aligned}
$$

For efficiently doing stochastic gradient variational Bayes (SGVB) with the flow enhanced posterior, we need

- efficient evaluation of $f_\eta(\wtilde z)$ and
- efficient evaluation of $\log \abs{\det f_\eta'(\wtilde z)}$.

The $\boxed{\text{boxed}}$ KL-divergence in the above equation gives another view of the ELBO.

- Suppose $\wbar Z \sim p_\theta(z | x)$ is the true posterior given $x$. Let $Z' = f_{\eta}^{-1}(\wbar Z)$.
- Then $Z' \sim p_\theta(f_\eta(z) | x) / \abs{\det f_\eta '(z)}$.
- Therefore the KL-divergence can be interpreted as normalizing the true posterior to make it simpler.
