##### Laplace transform

Suppose $f(x) \in L_{\loc}^1([0, \infty) \to \C)$ with following constraints:

- And that $f$ is of **exponential type**: $\exist c > 0: f(x) e^{-c x} \in L^1([0, \infty) \to \C)$.
  - Define $\sigma_f := \inf\{c \in \R: f(x) e^{-cx} \in L^1(\R)\}$.
  - $\c{z \in \C: \re z > \sigma_f}$ is the region of convergence (**ROC**) for Laplace transform.

For $s = \sigma + i \omega \in \C$, and $\re s > \sigma_f$. Define the **right-sided Laplace transform** of $f(x)$ as
$$
F(s) = \l[f] (s) := \f[f(x)e^{-\sigma x}] = \int_{0}^{\infty} f(x) e^{-s x} \dd x = \int_0 ^\infty f(x) e^{-\sigma x} e^{-i\omega x} \dd x
$$

- $F(s)$ is **holomorphic** on the ROC.
  - This follows from Fubini's theorem and Morera's theorem.
- The **derivative** of $F(s)$ on the ROC is given by:
  $$
  F^{(k)}(s)=\int_{0}^{\infty}(-t)^{k} f(t) e^{-s t} d t = \l[(-t)^k f]
  $$
  - The swapping is justified by dominated convergence.
  - Notice that $t^k f(t)$ has the same ROC as $f(t)$.

##### Laplace transform: injective map

Suppose $f, g \in L^1_\loc([0, \infty) \to \C)$ are of exponential type.

If $F(s) = G(s)$ on mutual ROC, then

- $\sigma_f = \sigma_g$ by analytic extension.
- And $f(x) = g(x)$ a.e. on $[0, \infty)$.
  - Since Fourier transform is injective.

##### Laplace inverse of meromorphic functions

From complex analysis, we know that $\C[z]$ is the set of all meromorphic functions on $\eC$.

> We further assume that $\infty$ is a removable singularity.
> The inverse of meromorphic functions with poles at $\infty$ requires distribution theory.

Suppose $f: \C \to \eC$ is meromorphic. And $\infty$ is a removable singularity of $f$. Review the following analysis:

- $f$ has only finitely many poles.
- Suppose $p_1, \ldots, p_n$ are the poles in $\C$, with order $d_1, \ldots, d_n$.
- Near pole $p_k$, for some $g_k \in \C[z]$, where $\deg g_k = d_k$, and holomorphic $h_k(z)$.
  $$
  f(z) = g_k\p{\frac{1}{z - p_k}} + h_k(z)
  $$
- Then we can represent $f(z)$ as
  $$
  f(z) = c + \sum_{k = 1}^n g_k \p{\frac{1}{z - p_k}}
  $$

Given $F(s) \in \C[s]$ of the form
$$
F(s)=\frac{\alpha_{n} s^{n}+\alpha_{n-1} s^{n-1}+\cdots+\alpha_{0}}{\beta_{m} s^{m}+\beta_{m-1} s^{m-1}+\cdots+\beta_{0}}, \quad n \le m
$$
First **decompose** $F(s)$ into standard form:
$$
F(s) = c + \sum_{k = 1}^n G_k \p{\frac{1}{s - p_k}}
$$
Now just note that for $p \in \C$ and $m \ge 0$, we have:
$$
\f[t^k e^{pt}] (s) = \frac{(d - 1)!}{(s - p)^d}; \quad \re s > p
$$
Therefore we can obtain $f(t)$ by inverting each fractional term.

##### Laplace transform: time derivative

Suppose $f \in D([0, \infty) \to \C)$ and $f' \in L_\loc^1([0, \infty) \to \C)$ are of exponential type.

In the **shared ROC**, $\re s > \min(\sigma_f, \sigma_{f'})$, we have
$$
\l[f'(t)] (s) = \int_{0}^\infty f'(t) e^{-st} \dd t = \left. f(t) e^{-st}\right|^{\infty}_{0} + s \int_{0}^\infty f(t) e^{-st} \dd t = sF(s) - f(0)
$$
according to integral by part.

##### Laplace transform: time integral

Suppose $f \in C([0, \infty) \to \C)$ is of exponential type. Let $g(t) = \int_0^t f(\tau) \dd \tau$.

Then $g \in C^1$ and has at least the same ROC with $f$.

Following differentiation theorem, we have:
$$
\l\s{\int_0^t f(\tau) \dd \tau}(s) = \frac{1}{s} F(s)
$$
##### Laplace transform: initial / terminal value theorem

Suppose $f \in L_{\loc}^1$ is **bounded**. And $\lim_{t \downarrow 0} f(t) = \alpha$.
$$
\lim_{s \to \infty} sF(s) = \lim_{s \to \infty} \int_0^\infty f(t) se^{-st} \dd t = \lim_{s \to \infty} \int_0^\infty f\p{\frac{t}{s}} e^{-t} \dd t = \alpha
$$
by dominated convergence.

Suppose $f \in L^1_\loc$ is not bounded. The theorem remains true.

- Define $g(t) = e^{-\alpha t}f(t)$ where $\alpha > \sigma_{f}$.
- $g(t)$ is bounded, and $\l[g(t)] (s) = F(s + \alpha)$.
- $\lim_{t\downarrow 0} g(t) = f(0^+)$.

Suppose $f \in L_\loc^1$ and $\lim_{t\to \infty}f(t) = \alpha$. Then with a similar proof:
$$
\lim_{s \downarrow 0} sF(s) = \lim_{t \to \infty} f(t)
$$
##### Laplace transform: shifting and scaling

Suppose $f \in L_{\loc}^1([0, \infty) \to \C)$ is of exponential type, and $\l[f] (s) = F(s)$.

- (Time shift) $f(t - a) \in L_{\loc}^1([a, \infty) \to \C)$. And for $\re s > \sigma_f + a$.
  $$
  \l[f(t - a)] (s) = \int_{a}^\infty f(t - a) e^{-st} \dd t = e^{-sa} F(s)
  $$
- (Frequency shift) For $\alpha \in \C$ we have:
  $$
  \l[f(t)e^{\alpha t}] (s) = \int_0^\infty f(t) e^{\alpha t} e^{-s t} \dd t =  F(s - \alpha)
  $$
- (Time scaling) For $\alpha \in (0, \infty)$, we have
  $$
  \l[f(\alpha t)] (s) = \int_0^\infty f(\alpha t) e^{-s t} \dd t = \frac{1}{\alpha}\int_0^\infty f(t) e^{-st/\alpha} \dd t = \frac{F(s / \alpha)}{\alpha}
  $$
