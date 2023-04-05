#### Rate-Distortion Theory

##### Rate-distortion function

Suppose $(\Omega, \F, P)$ is a probability space. Consider the following set up.

Let measurable space $(\X, \F_X)$ be the **source space**. Let measurable space $(\Y, \F_Y)$ be the **reproduction space**.

Consider a fixed random variable $X \in \L(\Omega \to \X)$ with distribution $P_X$.

Let $\M(X, \Y) \subseteq \L(\Omega \to Y)$ be the set of all random variables such that for $Y \in \M(X, \Y)$ the joint distribution $P_{XY} = P_{Y | X} \times P_X$ where $P_{Y|X}(x, F)$ is a probability kernel (also Markov kernel, or stochastic kernel).

Given distortion measure $\Delta: \L(\X \times \Y \to \R^+)$. We define the rate-distortion function as
$$
\begin{split}
R(D) := \inf_{Y \in \M(X, \Y)} I(X;Y) = \inf_{Y \in \M(X, \Y)} E\s{\d{P_{Y|X}(X, \cdot)}{P_Y}}\\
\operatorname{s.t.} \quad E\s{\Delta(X, Y)} \le D
\end{split}
$$

- $R(D)$ is interpreted as the minimum amount of information required to reproduce the source with average distortion less or equal to $D$.

- The discrete case of this statement is well studied. In the general case resources are scarce.

- When $\X, \Y$ are both finite, $I(P_X; P_Y)$ is a continuous functional of matrix $P_{XY}$, and the minimum is obtained.

Following above discussion $R(D)$ has the following properties:

- $R(D)$ is non-increasing, since $Q(D)$ is non-decreasing.
- $R(D)$ is convex, since KL divergence is a convex functional in its input pairs.
- Suppose $D_{\max} := \inf_{y \in \Y} E_{X \sim P_X}[\rho(X, y)] < \infty$, then $R(D_{\max}) = 0$.
  - Since by taking $P_{Y|X}(x, F) = 1_{\c{y}}(F)$, where $y$ is optimal, gives the result.
- Suppose $P_X$ is discrete, then $R(0) \le H(P_X)$.
  - Since by taking $P_{Y|X}(x, F) = 1_{\c{x}}(F)$ gives the result.

> The latter equality follows from the following.
>
> - Expand the definition of the KL divergence
>   $$
>   \d{P_{XY}}{P_{X} \times P_Y} = \int_{\X \times \Y} \log \p{\frac{P_{XY}(\dd x, \dd y)}{P_X(\dd x) P_Y(\dd y)}(x, y)}P_{XY}(\dd x, \dd y)
>   $$
>
> - It is easy to verify that the Radon-Nikodym derivative satisfies
>   $$
>   \frac{P_{XY}(\dd x, \dd y)}{P_X(\dd x) P_Y(\dd y)}(x, y) = \frac{P_{Y|X}(x, \dd y)}{P_Y(\dd y)}
>   $$
>
> - Therefore $\d{P_{XY}}{P_X \times P_Y} = E_{X \sim P_X}\s{\d{P_{Y|X}(X, \cdot)}{P_Y}}$.
>
>
> We could further generalize the distortion measure to taking values in $\R$, under the constraint that for the $X$ of concern,
>
> - Define $c(x) \in \L(\X \to \eR)$ as $x \mapsto \inf_{y \in \Y} \Delta(x, y)$.
> - $\Delta$ is called **normal** if $\forall x \in \X: c(x) = 0$.
> - If $E_{X \sim P_X}\s{c(X)} \in \R$, $\Delta$ can be normalized by defining $\wtilde \Delta(x, y) := \Delta(x, y) - c(x)$.
>
> Normalization add a constant bias to any $E[\Delta(X, Y)]$ since
> $$
> \iint \wtilde \Delta(x, y) P_{XY}(\dd x, \dd y) = \iint \Delta(x, y) P_{XY}(\dd x, \dd y) + \underbrace{\int c(x) P_X(\dd x)}_{\text{only depends on } P_X}
> $$

##### A variational upper bound of mutual information

> Huang, S., Makhzani, A., Cao, Y., & Grosse, R.B. (2020). Evaluating Lossy Compression Rates of Deep Generative Models. *International Conference on Machine Learning*.

Continue above discussion. The mutual information $I(X; Y)$ can be difficult to evaluate due to the requirement of marginal distribution $P_Y$. The following upper bound is found useful in practice.

Take another distribution $P_{\wtilde Y}$ on $(\Y, \F_Y)$. We have an upper bound
$$
\d{P_{Y|X}(X,\cdot)}{P_Y} + \d{P_Y}{P_{\wtilde{Y}}} = \d{P_{Y|X}(X, \cdot)}{P_{\wtilde Y}}
$$
Given $P_X$ and $P_{\wtilde Y}$, define the variational rate-distortion function as
$$
\begin{split}
\wtilde R(D) := \inf_{Y \in \M(X, \Y)} \d{P_{XY}}{P_X \times P_{\wtilde Y}}=\inf_{Y \in \M(X, \Y)} E\s{\d{P_{Y|X}(X, \cdot)}{P_{\wtilde Y}}}\\
\operatorname{s.t.} \quad E\s{\Delta(X, Y)} \le D
\end{split}
$$

- Notice that when $P_{XY} \not \ll P_X \times P_{\wtilde Y}$, the KL divergence is defined as $\infty$.
- $\wtilde R(D)$ is non-increasing and convex.
- $\wtilde R(D) \ge R(D)$ by definition, and the equality is obtained when $P_{\wtilde Y}$ is appropriate.

##### Latent variable models are lossy compressors

Let $(\X, \F_X)$ and be the observed space and $(\mathcal Z, \F_Z)$ be the latent space of the latent variable model.

- Suppose $Z \sim P_{Z}$ on $\mathcal Z$ has the prior latent distribution
- Suppose $F \in \L(\mathcal Z \times \Omega \to \X)$ is a stochastic decoding function.
- Suppose $X = F(Z)$. Then $X \sim P_{X | Z}\times P_Z$ on $\X$, where $P_{X|Z}$ is a Markov kernel defined by $F$.

Suppose we are concerned with distortion measure $\Delta(x, \what x) \in \L(\X^2 \to \R^+)$.

Suppose $\wtilde X \sim \wtilde P_X$ on $\X$ is the data distribution. Then
$$
\begin{split}
R(D) = \inf_{\wtilde Z \in \M(\wtilde X, \mathcal Z)} I(\wtilde X, \wtilde Z)= \inf_{\wtilde Z \in \M(\wtilde X, \mathcal Z)} E\s{\d{P_{\wtilde Z | \wtilde X}(\wtilde X)}{P_{\wtilde Z}}}
\\
\operatorname{s.t.} \quad E[\Delta(\wtilde X, F(\wtilde Z))] \le D
\end{split}
$$
