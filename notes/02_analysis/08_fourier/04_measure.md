#### Convergence in Distribution

##### Testing equivalence of measures

Denote the space of finite positive measures on $\R^d$ by $M_+(\R^d)$.

Suppose $\mu_1, \mu_2 \in M_+(\R^d)$, $\mu_1 = \mu_2$ iff
$$
\forall \varphi \in \D: \int_{\R^d} \varphi \dd \mu_1 = \int_{\R^d} \varphi \dd \mu_2
$$

- $\D$ can be replaced with box indicators, $\S$, and more.
- Notice that box indicators are pointwise decreasing limit of function sequences in $\D$.

##### Weak convergence of measure

Suppose $\p{\mu_n}, \mu \in M_+(\R^d)$. We say $\mu_j \to \mu$ **weakly** if

$$
\forall \varphi \in C_c(\R^d): \lim_{j \to \infty} \int_{\R^d} \varphi \dd\mu_j = \int_{\R^d} \varphi \dd \mu
$$
Since $\S$ and $\D$ are both dense in $C_c$, using testing functions in $\S$ or $\D$ also works.

- They are dense in all $L^p$ spaces where $p \in [1, \infty]$.

##### Converge in distribution

Suppose $X, \p{X_n}$ are real random variables with distributions $P, \p{P_n}$ on $\R$.

Then $X_n \to X$ **in distribution** if $P_n \to P$ weakly.

Suppose $X_n \to X$ in probability, $X_n \to X$ in distribution.

#### Fourier Transform of Measures

##### Fourier transform of finite measures

For $\mu \in M_+(\R)$ define the Fourier transform by
$$
\what \mu(\omega) = \f[\mu] (\omega) := \int_\R e^{-ix\omega} d\mu (x)
$$

- $\abs{\what \mu (\omega)} \le \mu(\R) < \infty$, so $\what \mu$ is well defined on $\R$.
- $\what \mu(\omega)$ is **continuous** due to DCT.

##### Fourier transform of measure: injective map

The map $\f: M_+(\R) \to C(\R)$ is injective.

- For $\varphi \in \S(\R)$ according to Fubini's theorem.
  $$
  \int_\R \what \varphi(y) \dd \mu(y) = \int_\R \int_\R e^{-ixy} \varphi(x) \dd x \dd \mu(y) = \int_\R \what \mu(x) \varphi(x) \dd x
  $$
- Now suppose $\mu_1$ and $\mu_2$ in $M_+(\R)$ have the same Fourier transform $\what \mu(x)$.
- Therefore for all testing function $\what \varphi \in \S(\R)$, we have
  $$
  \int_\R \what \varphi(x) \dd \mu_1(x) = \int_\R \what \varphi(x) \dd \mu_2(x)
  $$
- Now take $\varphi_n(x) \in \S(\R)$ decreasing to $1_{[a, b]}(x)$.
- By dominated convergence $\mu_1[a, b] = \mu_2[a, b]$. So $\mu_1 = \mu_2$.

##### Fourier transform and weak convergence

Suppose $\p{\mu_n}, \mu \in M_+(\R)$. $\mu_n \to \mu$ weakly if
$$
\forall \omega \in \R: \lim_{n \to \infty} \what \mu_n(\omega) = \what \mu(\omega)
$$

- $\mu_j(\R) = \what \mu_j(0) \to \what \mu(0)$, so the sequence $\mu_j(\R)$ is bounded.
- By dominated convergence, we have
  $$
  \forall \varphi \in \S: \lim_{j \to \infty} \int_\R \varphi(\omega) \what \mu_j(\omega) \dd \omega = \int_\R \varphi(\omega) \what \mu(\omega) \dd \omega
  $$
- Therefore
  $$
  \forall \varphi \in \S: \lim_{j \to \infty}\int_\R \what \varphi(\omega) \mu_j (\omega)\dd \omega = \int_\R \what \varphi(\omega) \mu(\omega) \dd \omega
  $$
- Terefore $\mu_j \to \mu$ weakly.

#### Laplace Transform of Measures

##### Convolution of causal LS measures

Suppose $G$ is a causal distributional function, i.e. $\su G \subseteq [0, \infty)$.

We adopt the following **notational conventions**:

- Denote $G[0, t] = G(-\infty, t] = G(t)$. And $\int_0^t f(s) \dd G(s) := \int_{[0, t]} f \dd G$.
- Denote $G(s, t] = G(t) - G(s)$ for $0 < s < t$. And $\int_s^t f(s) \dd G(s) = \int_{(s, t]} f \dd G$.
- Denote $G(A)$ as the measure of $A \in \B[0, \infty)$.

Suppose $F, G, H$ are a **causal distributional function**.

Suppose $f, g, h: \L([0, \infty) \to \R)$ are **locally bounded**.

- The convolution of $f$ with LS measure $\lambda_G$ is defined as:
  $$
  (f * \lambda_G)(t) := \int_0^t f(t - s) \dd G(s), \quad t \in [0, \infty)
  $$
  - Clearly convolution is **linear** in both operands.
- The convolution of $F$ with $\lambda_G$ is a **causal distributional function**.
  $$
  (F * \lambda_G) (t) := \int_0^t F(t - s) \dd G(s), \quad t \in [0, \infty)
  $$
  - Let $\triangle_t := \c{x + y \le t: x, y \in [0, \infty)^2}$. Then
    $$
    F * \lambda_G(t) = \int_0^t \int_0^{t - s} \dd F(r) \dd G(s) = (F \otimes G)(\triangle_t)
    $$
  - Therefore $F * \lambda_G = G*\lambda_F$ and it is distributional.
  - Define $\lambda_F * \lambda_G :=\lambda_{F * \lambda_G} = \lambda_{G * \lambda_F}$.
- Suppose $X, Y$ have causal distribution functions $F, G$. Then $X + Y$ has causal distribution $\lambda_F * \lambda_G$.
- $(f * \lambda_G) * \lambda_H = f* (\lambda_{G} * \lambda_H)$.
  $$
  \begin{aligned}
  \s{(f * G) * H}(t) &= \int_0^t (f*G)(t - s) \dd H(s) = \int_0^t \int_{0}^{t - s} f(t - s - r) \dd G(r) \dd H(s)
  \end{aligned}
  $$
  - Suppose $f$ is a indicator function, the result is clearly true.
  - Suppose $f$ is a simple function, the result is true by linearity.
  - Suppose $f$ is locally bounded, the result follows from dominated convergence.

##### Laplace transform of distribution

Given causal distributional function $F$. And the LS measure $\lambda_F$ induced by $F$.

- $\lambda_F$ is of exponential type if for some $c \in \R$, $e^{-cx} \dd F(x)$ is **finite**.
  - Let $\sigma_F$ be the infimum of all such $c$.
  - $\c{z \in \C: \re z > \sigma_f}$ is the region of convergence (**ROC**).

For $s = a + i\omega \in \C$ where $\re s > \sigma_F$, define the Laplace transform of $F$ as:
$$
\l[\lambda_F] (s) := \int_0^\infty e^{-st} \dd F(t) = \int_0^\infty e^{-a t} e^{-i\omega t}\dd F(t) = \f[e^{-at} \dd F(t)] (s)
$$

- Similar to traditional Laplace transforms, $\l[\lambda_F] (s)$ is **analytic** on the ROC.
- The distributional Laplace transform is an injective map from the space of all distributional functions to analytic functions. The reasoning is the same as traditional Laplace transform.

Observe the following, the result resembles integration.
$$
\begin{aligned}
\l[F] (s) & = \int_\R e^{-st} 1_{[0, \infty)} (t) F(t) \dd t = \int_\R e^{-st} 1_{[0, \infty)}(t) \p{\int_\R 1_{[0, t]}(u) \dd F(u)} \dd t\\
& = \iint_{\R^2} 1(t \ge 0, 0 \le u \le t) e^{-st} \dd t \dd F(u) = \int_0^\infty \int_u^\infty e^{-st} \dd t \dd F(u)\\
& = \int_0^\infty \frac{1}{s} e^{-su} \dd F(u) = \frac{1}{s} \l[\lambda_F] (s)
\end{aligned}
$$
- So $\lambda_F$ may have larger ROC than $F$.

Suppose $\lambda_F$ is finite (e.g. probabilistic), then $\sigma_F \le 0$.

##### Laplace transform of distributions: convolution

Suppose $f \in \L([0, \infty) \to \R)$ is locally bounded. And $F, G$ are a causal distributional function.

Suppose $\re s > \min(\sigma_f, \sigma_G)$. Then the following is justified by Fubini's theorem.
$$
\begin{aligned}
\l\s{f * \lambda_G} (s) & = \int_\R 1(t \ge 0) e^{-st} \p{f * \lambda_G}(t) \dd t\\
& = \int_\R 1(t \ge 0) e^{-st} \p{\int_\R 1(0 \le x \le t) f(t - x) \dd G(x)} \dd t\\
& = \int_{\R^2} 1(t \ge 0, 0 \le x \le t) e^{-st} f(t - x) \dd t \dd G(x)\\
& = \int_0^\infty e^{-sx} \int_x^\infty e^{-s(t - x)}  f(t - x) \dd t \dd G(x)\\
& = \int_0^\infty e^{-sx} \l[f] (s) \dd G(x) = \l[\lambda_G] (s) \cdot \l[f] (s)
\end{aligned}
$$
And as a result, we have the following:
$$
\l[\lambda_{F} * \lambda_G] (s) = \frac{1}{s} \l\s{F * \lambda_G}(s) = \frac{1}{s}\l[F] (s) \cdot \l[\lambda_G] (s) = \l[\lambda_F] (s) \cdot \l[\lambda_G] (s)
$$
