#### Deep Generative Models are Lossy Compressors

Denote $\M(\Omega, \F)$ as the set of all probability measures on measurable space $(\Omega, \F)$.

##### Rate-distortion function on abstract spaces

> Rezaei, F., Ahmed, N.U., & Charalambous, C.D. (2006). Rate Distortion Theory for General Sources With Potential Application to Image Compression.
>
> Cover, T.M., & Thomas, J.A. (1991). Elements of Information Theory.

Suppose $(\Omega, \F, P)$ is a probability space.

Suppose measurable space $(\X, \F_X)$ is the **source space**. Given a fixed $P_X \in \M(\X, \F_X)$.

Suppose measurable space $(\Y, \F_Y)$ is the **reproduction space**.

Let $Q$ be the set of all stochastic kernels from $\X$ to $\Y$. A kernel $P_{Y|X} \in Q$ is a function $P_{Y|X} :\X \times \Y \to [0, 1]$ such that

- For all $x \in \X$, $P_{Y|X}(x, \cdot) \in \M(\Y, \F_Y)$.
- For all $F \in \F_Y$, $P_{Y|X}(\cdot, F) \in \L(\X \to [0, 1], \F_X)$.

For each kernel $P_{Y|X} \in Q$, we define the following probability measures:

- Define $P_{XY} :=P_X \times P_{Y|X} \in \M(\X \times \Y, \F_X \otimes \F_Y)$ as the product probability measure
  $$
  P_{XY}(G) = \int_A P_{Y|X}(x, [G]_x) P_X(\dd x)
  $$

- Define the marginal distribution on $\Y$ as $P_Y(F) := P_{XY}(\X \times F)$.

Consider **distortion measure** $\rho: \L(\X \times \Y \to \R, \F_X \otimes \F_Y)$.

- Define $c(x) \in \L(\X \to \eR)$ as $x \mapsto \inf_{y \in \Y} \rho(x, y)$.
- $\rho$ is called **normal** if $\forall x \in \X: c(x) = 0$.
- If $E_{X \sim P_X}\s{c(X)} \in \R$, $\rho$ can be normalized by defining $\wtilde \rho(x, y) := \rho(x, y) - c(x)$.

For each $D \in \R$, define $Q(D) \subseteq Q$ as
$$
Q(D)  := \c{P_{Y|X}\in Q: \iint_{\X \times \Y} \rho(x, y) P_{XY}(\dd x, \dd y) \le D}
$$
Then the rate **distortion function** $R(D): \R \to [0, \infty]$ is defined as
$$
R(D) := \inf_{P_{Y|X} \in Q(D)} \d{P_{XY}}{P_X \times P_Y} = \inf_{P_{Y|X} \in Q(D)} E_{X \sim P_X}\s{\d{P_{Y|X}(X, \cdot)}{P_Y}}
$$
- The latter equality follows from the following.

  - Expand the definition of the KL divergence
    $$
    \d{P_{XY}}{P_{X} \times P_Y} = \int_{\X \times \Y} \log \p{\frac{P_{XY}(\dd x, \dd y)}{P_X(\dd x) P_Y(\dd y)}(x, y)}P_{XY}(\dd x, \dd y)
    $$

  - It is easy to verify that the Radon-Nikodym derivative satisfies
    $$
    \frac{P_{XY}(\dd x, \dd y)}{P_X(\dd x) P_Y(\dd y)}(x, y) = \frac{P_{Y|X}(x, \dd y)}{P_Y(\dd y)}
    $$

  - Therefore $\d{P_{XY}}{P_X \times P_Y} = E_{X \sim P_X}\s{\d{P_{Y|X}(X, \cdot)}{P_Y}}$.

- $R(D)$ is interpreted as the minimum amount of information required to reproduce the source with average distortion less or equal to $D$.

- The discrete case of this statement is well studied. In the general case resources are scarce.

- When $\X, \Y$ are both finite, $I(P_X; P_Y)$ is a continuous functional of matrix $P_{XY}$, and the minimum is obtained.

- The normalization of $\rho$ shifts the $R(D)$ curve in $D$.
  $$
  \iint \wtilde \rho(x, y) P_{XY}(\dd x, \dd y) = \iint \rho(x, y) P_{XY}(\dd x, \dd y) + \underbrace{\int c(x) P_X(\dd x)}_{\text{only depends on } P_X}
  $$


Following above discussion. $R(D)$ has following properties:

- $R(D)$ is non-increasing, since $Q(D)$ is non-decreasing.
- $R(D)$ is convex, since KL divergence is a convex functional in its input pairs.
- Suppose $D_{\max} := \inf_{y \in \Y} E_{X \sim P_X}[\rho(X, y)] < \infty$, then $R(D_{\max}) = 0$.
  - Since by taking $P_{Y|X}(x, F) = 1_{\c{y}}(F)$, where $y$ is optimal, gives the result.
- Suppose $P_X$ is discrete, then $R(0) \le H(P_X)$.
  - Since by taking $P_{Y|X}(x, F) = 1_{\c{x}}(F)$ gives the result.

##### Variational rate-distortion function

> Huang, S., Makhzani, A., Cao, Y., & Grosse, R.B. (2020). Evaluating Lossy Compression Rates of Deep Generative Models. *International Conference on Machine Learning*.

Following above discussion. The variational rate-distortion function is an upper bound of the rate-distortion function.

Take another distribution $P_{\wtilde Y}$ on $(\Y, \F_Y)$. We have an upper bound
$$
\d{P_{Y|X}(X,\cdot)}{P_Y} + \d{P_Y}{P_{\wtilde{Y}}} = \d{P_{Y|X}(X, \cdot)}{P_{\wtilde Y}}
$$
Given $P_X$ and $P_{\wtilde Y}$, define the variational rate-distortion function as
$$
\wtilde R(D):= \inf_{P_{Y|X} \in Q(D)} \d{P_{XY}}{P_X \times P_{\wtilde Y}} = \inf_{P_{Y|X} \in Q(D)} E_{X \sim P_X} \s{\d{P_{Y|X}(X, \cdot)}{P_{\wtilde Y}}}
$$

- Notice that when $P_{XY} \not \ll P_X \times P_{\wtilde Y}$, the KL divergence is defined as $\infty$.
- $\wtilde R(D)$ is non-increasing and convex.
- $\wtilde R(D) \ge R(D)$ by definition.
- We have $R(D) = \min_{P_{\wtilde Y}} \wtilde R(D)$.

##### Deep generative models are lossy compressors

A generative model can be viewed as a lossy compressor.

- Suppose $(\X, \F_X)$ is the source space, also the data space of the model.
- Suppose $(\mathcal Z, \F_Z)$ is the reproduction space, also the latent space of the model.
- Suppose $\wtilde Z \sim P_{\wtilde Z}$ on $\mathcal Z$ is the prior latent distribution.
- Suppose the generator is a stochastic function $f_\theta(z, N)$ where $N$ is some independent stochastic source.
- Let $\rho(x, z) = E[d(x, f_\theta(z, N))] \in \L(\X \times \mathcal Z \to \R)$ be the distortion function. Where $d(x, \what x)$ is some distortion function on $\X^2$.
- Suppose $X \sim P_X$ on $\X$ is the true data distribution.

Define $Q(D)$ similarly from above discussion. Then $R(D)$ becomes
$$
R(D) = \inf_{P_{Z|X} \in Q(D)} E\s{\d{P_{Z|X}(X, \cdot)}{P_{Z}}}
$$
$R(D)$ can be hard to evaluate in practice, so we can use the following variational rate-distortion function
$$
\wtilde R(D) = \inf_{P_{Z|X} \in Q(D)} E\s{\d{P_{Z|X}(X, \cdot)}{P_{\wtilde Z}}}
$$
