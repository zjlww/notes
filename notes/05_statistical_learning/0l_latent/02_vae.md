#### Variational Autoencoders

> Doersch, C. (2016). Tutorial on Variational Autoencoders. *ArXiv, abs/1606.05908*.

##### Amortized variational inference

In traditional variational inference, we optimize the variational parameters for each data point independently, which can be computationally expensive for large datasets.

Amortized variational inference, on the other hand, aims to share the computational cost across data points by learning a function that maps the observed data to the variational parameters. This function, often parameterized by a neural network, effectively "amortizes" the cost of inference over the dataset, making it more scalable and efficient.

##### Variational autoencoders

VAEs are a class of deep generative models that use amortized variational inference to learn the parameters of the generative model.

Suppose $p_\theta(z, x)$ is a parameterized latent variable model. And $p_*(x)$ is the data density.

However, we wish to use a model $p_\theta(x, z) = p_\theta(x|z)p_\theta(z)$ that is made of neural networks.

This leads to the following properties:

- Sampling and evaluating $p_\theta(z)$ and $p_\theta(x | z)$ are easy.
- Integration of $p_\theta(x) = \int p_\theta(z, x) \dd z$ is intractable.
- Computing $p_\theta(z|x)$ is intractable, so we cannot directly apply EM algorithm here.

Introduce a **estimated posterior** $q_\phi(z|x)$ to estimate $p_\theta(z | x)$.
$$
\newcommand{\elbo}{\operatorname{ELBO}}
\begin{aligned}
\elbo(p_\theta, q_\phi, x) & := E_{\what Z \sim q_\phi(z|x)}\s{\log \frac{p_\theta(x | \what Z) p_\theta(\what Z)}{q_\phi(\what Z | x)}}\\
& = \log p_\theta(x) - \d{q_\phi(z|x)}{p_\theta(z | x)}\\
& = E_{\what Z \sim q_\phi(z|x)}\s{\log p_\theta(x | \what Z)}-\d{q_\phi(z|x)}{p_\theta(z)}
\end{aligned}
$$
The training loss of the Variational autoencoder is:
$$
\begin{aligned}
\L_{\theta, \phi} & := E\s{\elbo({p_\theta, q_\phi, X_*})} = E_{\what Z \sim q_{\phi}(z | X_*)}\s{\log \frac{p_\theta(\what Z, X_*)}{q_\phi(\what Z | X_*)}} \\
& = -\d{p_*(x) q_{\phi}(z|x)}{p_{\theta}(z, x)}
\end{aligned}
$$
We have some special names for the densities here:

- $p_\theta(z)$ is called the **prior**.
- $p_\theta(z | x)$ is called the **posterior**.
- $q_\phi(z | x)$ is called the **approximate posterior**.

The objective $\L_{\theta, \phi}$ can be optimized by gradient. Most commonly, we use a mean-field approximate posterior, and a pathwise gradient estimator.

##### VAE with an autoregressive prior

> Child, R. (2020). Very Deep VAEs Generalize Autoregressive Models and Can Outperform Them on Images. *ArXiv, abs/2011.10650*.

Suppose $Z = (Z_0, \ldots, Z_N)$. Here is one possible formulation of an VAE with autoregressive prior.

- Decompose $p_\theta(z) = p_\theta(z_0) \prod_{t = 1}^N p_\theta(z_t | z_{<t})$.
- Decompose $q_\phi(z_{0..N}|x) = q_\phi(z_0|x) \prod_{t=1}^N q(z_t|z_{<t},x)$.

Then
$$
\begin{aligned}
\L_{\theta, \phi} &= E\s{\log \frac{p_\theta(\what Z, X_*)}{q_\phi(\what Z | X_*)}} = E\s{\log \frac{p_\theta(X_* | \what Z)p_\theta(Z_0) \prod_{t = 1}^N p_\theta(\what Z_t | \what Z_{ <t })}{q_\phi(\what Z_0|X_*) \prod_{t=1}^N q(\what Z_t|\what Z_{<t}, X_*)}}\\
& = E\s{\log p_\theta(X_*, \what Z)} - \d{q_\phi(z_0 | x)}{p_\theta(z_0)} - \sum_{t = 1}^N\d{q_\phi(z_t | z_{< t }, x)}{p_\theta(z_t | z_{<t})}
\end{aligned}
$$
