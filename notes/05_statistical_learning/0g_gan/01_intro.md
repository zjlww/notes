#### Generative Adversarial Networks

> GAN is about minimizing divergence while only sampling is efficient and differentiable.
>
> Nowozin, S., Cseke, B., & Tomioka, R. (2016). f-GAN: Training Generative Neural Samplers using Variational Divergence Minimization. *NIPS*.

##### Fenchel conjugate function ==TODO==

Suppose $f: (0, \infty) \to \R$ is a convex function.

Then there exists an a Fenchel conjugate $f^*: \T \subseteq \R \to \R$ such that
$$
\forall u \in (0, \infty): \sup_{t \in \T} \p{t u - f^*(t)}
$$

##### Variational lower bound of $f$-divergence

Suppose on measurable space $(\Omega, \F)$ there are two probability measures $P, Q$. And that $P \ll Q$.

Suppose $P$ and $Q$ have density $p$ and $q$ with respect to the Lebesgue measure.

Suppose $f$ defines an $f$-divergence, and its has Fenchel conjugate $f^*: \T\subseteq \R \to \R$.
$$
\begin{aligned}
D_f(p \| q) & =\int_{\R^d} p(x) f\left(\frac{q(x)}{p(x)}\right) \dd x \\
& = \int_{\R^d} p(x) \sup_{t \in \T}\c{t \frac{q(x)}{p(x)} - f^*(t)} \dd x\\
& \ge \sup_{T \in \F} \p{\int_{\R^d} q(x) T(x) \dd x-\int_{\R^d} p(x) f^*(T(x)) \dd x}
\end{aligned}
$$

Where $\F \subseteq \L(\R^d \to \T)$ is a family of bounded measurable functions. When $\F$ is very broad, we are guaranteed equality.

The optimal $T(x)$ is given by
$$
T^*(x) := \sup_{t \in \T} \c{t \frac{q(x)}{p(x)} - f^*(t)}
$$

##### Generator functions

Suppose $Z \in \L(\Omega \to \R^h)$ is a random variable.

Then $f_\theta \in \L(\R^h \to \R^d)$ with parameter $\theta \in \Theta \subseteq \R^m$ is called a **generator function**.

- Let $X = f_\theta(Z)$, then the distribution $P_X = Q_\theta$ is the **generated distribution**, it is a parametric probabilistic model. Let $\mathcal Q = \c{Q_\theta: \theta \in \Theta}$.
- Let $X_* \in \L(\Omega_* \to \R^d)$ be the random variable with the **data distribution**.

We make the following assumptions in the following derivation:

- $f_\theta(x)$ is differentiable in $\theta$.
- $P_X$ has density $p_\theta(x)$, $P_{X_*}$ has density $p_*(x)$, and $P_Z$ has density $p(z)$ with respect to the Lebesgue measure.

Due to the very few constraints we impose on $f_\theta(x)$, $\log q_\theta(x)$ becomes intractable. Therefore the model is also called **likelihood-free model**.

It turns out that we optimize for $D_f(p_* \Vert q_\theta)$ with only sampling, at the cost of adding an "discriminator" network.

##### Variational optimization of the generator function

Suppose $f$ with Fenchel conjugate $f^*: \T \to \R$ defines an $f$-divergence.

Let $p_*$ be the data density, and $q_\theta$ be our generated density.

Now consider the variational lower bound of $D_f(p_*\Vert q_\theta)$. While the family $\F$ is parameterized by $\phi \in \Phi$.
$$
D_f(P_*\Vert Q_\theta) \ge \sup_{\phi \in \Phi} \c{E_{P_*}\s{T_\phi(X_*)} - E_{Q_\theta}\s{f^*(T_\phi(X))}}
$$
Now we could rewrite the objective of $\min_\theta D_f(p_* \Vert q_\theta)$ when the maximum is obtainable.
$$
\min_{\theta \in \Theta} \max_{\phi \in \Phi} \c{E_{P_*}\s{T_\phi(X_*)} - E_{Q_\theta}\s{f^*(T_\phi(X))}}
$$
In practice we cannot work directly with this objective since:

- $\F$ may be restricted and global maximum in $\phi$ is not achievable.
- It is too slow to solve the inner maximum when $T_\phi$ is a neural network.

So we have to work with some approximation of the objective...

