

##### The unit circle

Define $\cD = \overline {B(0, 1)} \subseteq \C$. Define $\dD$ as the complex unit circle.

- $\dD$ is associated with $(-\pi, \pi]$ through homeomorphism $\theta: e^{it} \to t$.
- For $f: \dD \to \C$, it is associated with $\wtilde f(t) = f(e^{it}): \R \to \C$ with period $2\pi$.
- $f$ is $k$ times continuously differentiable if $\wtilde f$ is $k$ times continuously differentiable on $\R$.
  - Define $f^{[k]}(e^{it}):=\wtilde f^{(k)}(t)$.

  - The space of such functions is $C^k(\dD \to\C)$.
- We define the following measures on $\dD$.

  - Define measure $\sigma$ on $\dD$ as the push-forward of Lebesgue measure by $\varphi$ scaled by $1/2\pi$.


We now have the following for $f \in L^1(\dD \to \C, \sigma)$.
$$
\int_{\dD} f(z) \dd \sigma(z) = \frac{1}{2\pi}\int_{-\pi}^\pi f(e^{it})\dd t =^* \frac{1}{2\pi i}\oint_{\dD} \frac{f(z)}{z} \dd z
$$

$L^2(\dD \to \C, \sigma)$ is a Hilbert space with inner product:
$$
\pd fg = \int_{\dD} f(z) \overline{g(z)} \dd \sigma(z)
$$
##### Fourier basis

$\p{z^n}_{n=-\infty}^\infty$ is an **orthonormal sequence** on $L^2(\dD \to \C, \sigma)$.

- $\pd{z^n}{z^n} = \frac{1}{2\pi i} \oint_{\dD} z^{-1} \dd z = 1$.
- $\pd{z^n}{z^m}$ where $n \neq m$ is $0$.

##### Fourier coefficients on $L^1$: existence

For $f \in L^1(\dD \to \C, \sigma)$, the following is well defined.
$$
\widehat f(n) := \pd{f}{z^n} = \int_{\dD} f(z) \overline{z^n} \dd \sigma(z) = \frac{1}{2\pi} \int_{-\pi}^\pi f(e^{it}) e^{-int} \dd t
$$
Fourier transform is a linear map $\f$ from $L^1$ to $\ell$, which is not continuous ==TODO==.

##### Fourier coefficients of analytic functions

Suppose $f$ is **analytic** in some region containing $\cD$. And $f(z) = \sum_{n=0}^\infty a_n z^n$.

Then $\widehat f(n) = a_n$ for $n \ge 0$, and $\widehat f(n) = 0$ otherwise.

##### Riemann-Lebesgue Lemma

We have $\what f(n) \to 0$ as $n \to \pm \infty$ for the following function families.

- **Indicators** $f(z) = 1_E(z)$ where $E$ is an interval on $\dD$.
  - This is immediate, due to the periodicity of bases.
- $\square_c^1(\dD \to \C, \sigma)$.
  - Linearity of integral.
- $L^1(\dD \to \C, \sigma)$.
  - $\square_c^1(\dD \to \C, \sigma)$ is dense in this class. And inner products are continuous.

##### Cyclic convolution

Suppose $f, g \in L(\dD \to \C, \sigma)$. The **(cyclic) convolution** of $f$ and $g$ is $f * g$ defined by
$$
(f * g)(z): = \int_{\dD} f(s) g(z \bar s) \dd \sigma(s)
$$
- If $f * g \in L^1(\sigma)$ then $f * g$ is well-defined almost everywhere, and
  $$
  \n{f * g}_1 \le\int_{\dD} \int_{\dD} \abs{f(s) g(z \bar s)} \dd \sigma(s) \dd \sigma(z) = \n{f}_1\n{g}_1
  $$
  following Tonelli's Theorem.

- $f * g = g * f$. This follows from a linear change of variable.

##### $L^p$-norm of cyclic convolution

Suppose $f \in L^1(\dD \to \C, \sigma)$ and $g \in L^p(\dD \to \C, \sigma)$.

We can testing the norm in $L^p$ with functions in $L^q$.
$$
\n{f*g}_p = \sup_{h \in \L^{q}, \n{h}_q = 1} \abs{\pd{f * g}{h}} = \sup_{h \in \L^q, \n{h}_q = 1} \abs{\int_{\dD} (f*g)(z)h(z) \dd \sigma(z)}
$$
Now notice for any $h \in L^q$ we have:
$$
\begin{aligned}
\abs{\int_{\dD} (f * g)(z) h(z) \dd \sigma(z)} & \le \int_{\dD} \p{\int_{\dD} |f(s)| |g(z\bar s)| \dd \sigma(s)} |h(z)| \dd \sigma(z)\\
& \le \int_{\dD} \int_{\dD} |g(z \bar s)||h(z)| \dd \sigma(z) |f(s)| \dd \sigma(s) \le \n{f}_1 \n{g}_{p} \n{h}_q
\end{aligned}
$$
Therefore $\n{f * g}_p \le \n{f}_1 \n{g}_p$.

##### Poisson kernel

For $f \in L^1(\dD \to \C, \sigma)$ and $r \in [0, 1)$. Define $\P_r f: \dD \to \C$ as
$$
\P_r f(z) = \sum_{n=-\infty}^\infty r^{|n|} \widehat f(n) z^n
$$

- The unordered series on the RHS **absolutely converges**, so $\P_rf (z)$ is well defined on $\dD$.
  $$
  \sum_{n \in \Z} r^{|n|} \abs{\widehat f(n) z^n} < \infty
  $$

- This is actually a **convolution**, exchange integral with Fubini's theorem:
  $$
  \begin{aligned}
  \P_rf(z) = \sum_{n \in \Z} r^{|n|} \what f(n) z^n = \sum_{n \in \Z} r^{|n|}z^n \int_{\dD} f(w) \overline{w^{n}} \dd \sigma(w) = \int_{\dD} f(w) \p{\sum_{n \in \Z} r^{|n|}(z\overline w)^n} \dd \sigma(w)\\
  \end{aligned}
  $$


For $r \in [0, 1)$, define **Poisson kernel** $P_r(z): \dD \to (0, \infty)$ as following:
$$
\begin{aligned}
P_r(z) := \sum_{n \in \Z} r^{|n|}z^n = 1 + \sum_{n=1}^\infty r^n z^n + \sum_{n=1}^\infty r^n \overline z^n
= 1 + \frac{rz}{1-rz} + \frac{\overline{rz}}{1 - \overline {rz}} = \frac{1-r^2}{|1-rz|^2} \in (0, \infty)
\end{aligned}
$$

- Notice that $P_r(z)$ is holomorphic on $A(0; r, 1/r)$. And that
  $$
  \int_{\dD} P_r(z) \dd \sigma(z) = \frac{1}{2\pi i} \oint_{\dD} \frac{P_r(z)}{z} = 1
  $$

- The Poisson kernel **concentrates** to $1$ as $r \uparrow 1$, as described in:
  $$
  \forall \delta > 0:\lim_{r \uparrow 1} \int_{\dD - B(1, \delta)} P_r(z) \dd \sigma(z) = 0
  $$

  - $|1 - rz| = |1 - z + z - rz| \ge |1-z| - (1 - r)$.
  - Note that $|1-z| \ge \delta$. So when $r$ is big enough, where $(1 - r) < \delta / 2$.
  - We have $|1-rz| > \delta / 2$.
  
- The Poisson kernel is symmetrical, $P_r(z) = P_r(\bar z)$.

Therefore we can rewrite $\P_rf(z)$.
$$
\P_r f(z) = \int_{\dD} f(w) P_r(z\overline w) \dd \sigma(w) = (f * P_r)(z) = \int_{\dD} f(w) \frac{1-r^2}{|1-rz\overline w|} \dd w
$$
##### Poisson convergence theorems

Suppose $f \in C(\dD \to \C)$, then $\P_r f \rightrightarrows_{\dD} f$ as $r \uparrow 1$.

- $f$ is uniformly continuous on $\dD$, suppose $|f(z) - f(s)| < \epsilon$ as long as $\abs{z - s} < \delta$.

- Consider any $z \in \dD$. Then
  $$
  \begin{aligned}
  \abs{f(z) - \P_rf (z)} & = \abs{f(z) - \int_{\dD} f(s) P_r(z\bar s) \dd \sigma(s)}
  = \abs{\int_{\dD} \p{f(z) - f(s)} P_r(z \bar s) \dd \sigma(s)}\\
  & \le \epsilon \int_{\dD - B(z; \delta)} P_r(z\bar s)\dd \sigma(s) + 2 \n{f}_{\infty}\int_{\dD \cap B(z; \delta)} P_z(z \bar s)\dd \sigma(s)
  \end{aligned}
  $$

Suppose $f \in L^p(\dD \to \C, \sigma)$, $p \in [1, \infty)$. Then $\P_r f \to f$ in $L^p$ as $r \uparrow 1$.

- There exists $g \in C_c^\infty(\sigma)$ very close to $f$. $\P_r g \to g$ in $L^p$.

- Now notice the following:
  $$
  \begin{aligned}
  \n{f * P_r - f}_p &\le \n{f * P_r - g * P_r + g * P_r - g + g - f}_p\\
  & \le \n{P_r}_1 \n{f - g}_p + \n{g * P_r - g}_p + \n{g - f}_p
  \end{aligned}
  $$

##### Fourier coefficients on $C^k$

Suppose $f \in C^k(\dD \to \C)$. Then
$$
\p{f^{[k]}}\phat (n) = \frac{1}{2\pi}\int_{-\pi}^\pi \wtilde f^{(k)} (t) e^{-int} \dd t = \frac{in}{2\pi} \int_{-\pi}^\pi \wtilde f^{(k-1)} (t) e^{-int} \dd t = in\p{f^{[k-1]}}\phat (n)
$$
$C^2(\dD \to \C) \subseteq \overline {\span \p{e_n}} \subseteq L^2(\dD \to \C, \sigma)$.

- Consider $f \in C^2$, $\abs{\what f(n)} = \abs{ {\pd{f^{[2]}}{z^n}}/{n^2}} \le \n{f^{[2]}}_1/n^2$.

  - Therefore the Fourier series of $f$ **converges absolutely**.
  - And the truncated sum $\sum_{n=-N}^{N} \what f(n) z^{n}$ converges uniformly as $N \to \infty$.

- The Fourier series converges to $f$.
  $$
  f(z) = \lim_{r \uparrow 1} \P_rf(z) = \lim_{r \uparrow 1} \sum_{n \in \Z} r^{|n|} \what f(n) z^n = \sum_{n \in \Z} \what f(n) z^n
  $$

  - Swapping is legal due to dominated converge theorem.

##### Fourier basis is an orthonormal basis in $L^2$

The Fourier basis is an orthonormal basis of $L^2(\dD \to \C, \sigma)$.

- Since $L^2(\sigma)$ is a **Hilbert space**, we only need to show that $\c{z^n}$ is maximal.
  - Suppose $f \in \span \c{z^n}^\perp$ and $f \in L^2(\sigma)$.
  - There exists $\p {g_n} \in C_c^\infty(\sigma)$ where $g_n \to f$ in $L^2$ norm.
  - Therefore $\pd{g_n}{z^n} \to \pd{f}{z^n} = 0$.
  - But $g_n \in C^2(\dD \to \C) \subseteq \overline{\span \c{z^n}}$. Therefore $g_n = 0$. So $f = 0$.

##### Fourier coefficients on $L^1$: injective map

The Fourier transform $\f: L^1(\dD \to \C, \sigma) \to \ell(\Z)$ is injective.

- Suppose $f \in L^1(\sigma)$ and $\what f(n) = 0$ for all $n \in \Z$. Then $\P_r f = 0$.
- But $\P_r f \to f$ in $L^1$, so $\n{f}_1 = 0$.

##### Fourier coefficients on $L^1$: transform

Suppose $f, g \in L^1(\dD \to \C, \sigma)$.

- (Rotation) $\f[f(z \bar w)] = \bar w^n \what f(n)$ for $w \in \dD$.
  $$
  \F[f(z \bar w)] = \pd{f(z \bar w)}{z^n} = \int_{\dD} f(z\bar w) \bar z^n \dd \sigma(z) = \int_{\dD} f(s) \bar s^n \bar w^n \dd \sigma(s) = \bar w^n \what f(n)
  $$

- (Convolution) $\f[(f * g)(z)] = \what{f}(n) \what{g}(n)$. By swapping the following integral.
  $$
  \begin{aligned}
  \F[(f * g)(z)] & = \int_{\dD} \p{\int_\dD f(s) g(\bar s z) \dd \sigma(s)} \bar z^n \dd \sigma(z)
  \end{aligned}
  $$

##### Convolution in $L^1$ is associative

Suppose $f, g, h \in L^1(\dD \to \C, \sigma)$, then $(f * g) * h = f * (g * h)$.

- Since they have the same Fourier series. And the Fourier transform is injective.
