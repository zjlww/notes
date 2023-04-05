#### Rate-Distortion-Perception Tradeoff

> Blau, Y., & Michaeli, T. (2019). Rethinking Lossy Compression: The Rate-Distortion-Perception Tradeoff. *ArXiv, abs/1901.07821*.

##### Perceptual quality of lossy compression

Perceptual quality is commonly evaluate empirically by the mean opinion score of human subjects. Formally we define **perception quality measure** through a loss function between marginal distributions, including $f$-divergences, and integral probability metrics. This is motivated as following:

Let's consider a simpler case where we conduct AB test on original sample $X_*$ and reconstructed sample $X$. Human evaluators must choose one sample of better perceptual quality from each pair $(x_*, x)$. In this case, the preference rate of the reconstructed sample is given by
$$
p_{\mathrm{B}} = \frac{1}{2} - \frac{1}{2} d_{\mathrm{TV}}\p{P_{X_*} \Vert P_{X}}
$$
where $d_{\mathrm {TV}}$ is the total-variation distance between the two distribution. For lossless compression, $p_{\mathrm A} = p_{\mathrm B} = 1 / 2$.

##### Rate-distortion-perception (RDP) tradeoff

When considering the perception, we must have $\X = \Y$ since the perceptual qual

Given **distortion measure** $\Delta: \L(\X \times \Y \to \R^+)$ and a **perception measure** $d(P_X, P_Y)$ which maps a pair of marginal distribution $(P_X, P_Y)$ to $\R^+$.

Given a fixed random variable $X \sim P_X$ on $\X$. The rate-distortion-perception function is defined as
$$
R(D, Q) := \inf_{Y \in \M(X, \Y)} I(X; Y), \quad \operatorname{s.t.} E[\Delta(X, Y)] \le D,\quad  d(P_X, P_Y) \le Q
$$

The rate-distortion-perception function $R(D, Q)$ is non-increasing in $D$ and $Q$ separately.

Suppose the perception quality measure $d$ is convex in the second argument. Then $R(D, Q)$ is also convex.

- Suppose for $Y_0, Y_1$ we have $R_k := I(X; Y_k)$, $D_k := E[\Delta(X, Y_k)]$, and $Q_k := d(P_X, P_{Y_k})$.

- Suppose $Y_\lambda = \lambda Y_0 + (1 - \lambda Y_1)$ for some $\lambda \in (0, 1)$.

- Define $R_\lambda := I(X; Y_\lambda)$, $D_\lambda := E[\Delta(X; Y_\lambda)]$, and $Q_\lambda := d(P_X, P_{Y_\lambda})$.

- The points $\symbf A_k :=(D_k, Q_k, R_k)$ are above the surface $R(D, Q)$.

- We now can show that the surface $R(D, Q)$ is below the line between $\symbf A_0$ and $\symbf A_1$.

  - By definition $D_\lambda = \lambda D_0 + (1 - \lambda) D_1$.

  - Since $d$ is convex in the second argument, we have $Q_\lambda \le \lambda Q_1 + (1 - \lambda) Q_2$.

  - Since $I(X; Y)$ is convex in the second argument, we have $R_\lambda \le \lambda R_1 + (1 - \lambda) R_2$.


##### Data processing inequality ==TODO==

Random variables $X, Y, Z$ on some probability space forms a Markov chain if we have the joint distribution $P_{XYZ}$ can be decomposed as $P_{Z  | Y} \times P_{Y|X} \times P_X$ where $P_{Z | Y}$ and $P_{Y | X}$ are Markov kernels. We write $X \to Y \to Z$ in this case.

Suppose $X \to Y \to Z$, then we have data processing inequality
$$
I(X; Y) \ge I(X; Z)
$$

##### VAE-GAN traverses the RDP tradeoff

> Larsen, A.B., Sønderby, S.K., Larochelle, H., & Winther, O. (2015). Autoencoding beyond pixels using a learned similarity metric. *ArXiv, abs/1512.09300*.

Consider a VAE model trained with an extra adversarial loss, also referred to as a VAE-GAN model.

- Let $p_*(x)$ be the density of the data. Where $X_* \sim p_*(x)$ be a random variable representing the data.
- Let $q_\phi(z | x)$ be the approximate posterior density. Where $\what Z = E_\phi(X_*) \sim q_\phi(z | X_*)$ is a random variable representing the latent code.
- Let $p_\theta(z)$ be the prior density. Where $Z \sim p_\theta(z)$ is a random variable representing the prior latent code.
- Let $p_\theta(x | z)$ be the decoder density. Where $\what X = F_\theta(\what Z) \sim p_\theta(x | \what Z)$ is a random variable representing the reconstruction.
- Let $p_\theta(x)$ be the marginal model density. Where $X = F_\theta(Z) \sim p_\theta(x)$ is a random variable representing the generated samples.

Suppose the adversarial loss is approximately minimizing divergence $D(p_*(x) \Vert p_\theta(x))$. 

Our training objective can be written as minimizing the following function:
$$
\L_{\theta, \phi} := -E\s{\log p_\theta(X_* | \what Z)} + \beta E\s{\d{q_\phi(z | X_*)}{p_\theta(z)}} + \gamma D(p_*(x) \Vert p_\theta(x))
$$

- The first term $-E\s{\log p_\theta(X_* | \what Z)}$ can be viewed as the distortion measure.

  - For example, when $p_\theta(x | z)$ is fixed variance isotropic Gaussian, can also be written as $\alpha E\s{\n{X_*- \what X}_2^2}$.

- The second term $E\s{\d{q_\phi(z | X_*)}{p_\theta(z)}}$ is an upper bound of $I(X_*; \what X)$.

  - First apply the data processing inequality, $I(X_*; \what X) \le I(X_*; \what Z)$.

  - Now apply the variational upper bound mentioned before to get:
    $$
    I(X_*; \what Z) \le E\s{\d{q_\phi(z | X_*)}{p_\theta(z)}}
    $$


So approximately, the VAE-GAN training process is approaching the $R(D, Q)$ surface of the encoder-decoder system.

