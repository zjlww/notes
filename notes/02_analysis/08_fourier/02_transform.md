##### The upper plane

Denote $\bH$ as the open upper half-plane in $\C \simeq \R^2$. $\dH$ denotes $\R$ in $\C$.

$L^2(\dH \to \C, \lambda)$ is a Hilbert space.


##### Fourier transform

For $f \in L^1(\R \to \C)$, the Fourier transform is $\what f: \R \to \C$.
$$
\what f(\omega) = \F[f](\omega) := \int_{\R} f(x) \exp(-i \omega x)\dd x = \pd{f(x)}{e^{i\omega x}}
$$

- We have $\what f(\omega) \to 0$ as $\omega \to \pm \infty$ for $f \in \L^1(\R \to \C)$.
  - The proof is similar to the proof for Fourier series, using a density argument.
- And $\what f$ is bounded. $\n{\what f}_\infty \le \n{f}_1$.
  $$
  |f(\omega)| \le \int_{\R} |f(x)| \dd x = \n{f}_1
  $$

The Fourier transform $\f: L^1 \to L^\infty$ is a continuous linear map.

##### $\what f$ is uniformly continuous for $f \in L^1$

For $f \in L^1(\R \to \C)$, $\what f(\omega)$ is **uniformly continuous** on $\R$.

- Consider indicator $f(x) = 1_{[b, c]}(x)$. $\what f$ is uniformly continuous.
  $$
  \what f(\omega) = \int_{b}^c e^{-i\omega x} = \begin{cases}i(e^{-2\pi c \omega} - e^{-2 \pi b \omega})/\omega & \text { if } \omega \neq 0 \\ c-b & \text { if } \omega=0\end{cases}
  $$
- Therefore $\what f$ is uniformly continuous for $f \in \square^1(\R \to \C, \lambda)$.
- There exists a sequence of $\p{f_n} \subseteq {\square}^1(\R \to \C, \lambda)$. Where $f_n \rightrightarrows_{\R}f$.
- Since $\n{\what f_n - \what f}_{\infty} \le \n{f_n - f}_1$, $\what f_n \rightrightarrows_{\R} \what f$.
- Since uniform limit of uniformly continuous functions is uniformly continuous. $\what f(\omega)$ is uniformly continuous.

##### Derivative of Fourier transform

Suppose $f \in L^1(\R \to \C)$. If $g(x) = (-ix) f(x) \in L^1$.

Then $\what f(\omega) \in C^1$ and $(\what f)'(\omega)=\what g(\omega)$.

- The exchange of integral and differentiation is justified by dominated convergence.

##### Fourier transform of derivative

Suppose $f \in L^1(\R \to \C)$ and $f \in C^1$, $f' \in L^1$. Then $(f')\phat (\omega) =  i\omega \what f(\omega)$.

- The given conditions guarantees $f(x) \to 0$ as $x \to \pm \infty$.
  - Since $f, f' \in L^1$, For $\epsilon > 0$ there exists $a \in \R$ where
    $$
    \int_{a}^\infty \abs{f'(x)} \dd x < \epsilon \land  \abs{f(a)} < \epsilon
    $$
  - Now for $b > a$, and $f' \in C$, we have
    $$
    \abs{f(b)} = \abs {\int_{a}^b f'(x) \dd x + f(a)} \le \int_{a}^\infty \abs{f'(x)} \dd x + \abs{f(a)} < 2 \epsilon
    $$
- Now since $f' \in C$, we can apply integration by parts:
  $$
  \what{(f')}(\omega) = \int_\R f'(x) \exp(-i \omega x) \dd x = i\omega \int_\R f(x) \exp (-i\omega x) \dd x = i \omega \what f(\omega)
  $$

##### Fourier transform: linear transforms

Suppose $f \in L^1(\R \to \C)$.

- $\f[f(x - b)] = \int f(x - b) e^{-i\omega x} \dd x = e^{-ib \omega} \what f(\omega)$.
- $\f[e^{ibx} f(x)] = \what f(\omega - b)$.
- $\f[f(bx)] = \frac{1}{\abs{b}}\what f(\frac{t}{b})$.
- $\f[\overline{f(-x)}] = \overline {\what f(\omega)}$.
  $$
  \F [\overline{f(-x)}] (\omega) = \int_\R \overline{f(-x)} e^{-i \omega x} \dd x = \overline{\int_\R f(x) e^{-i \omega x}\dd x} = \overline{\what f(\omega)}
  $$

##### Integral of a function times a Fourier transform

Suppose $f, g \in L^1(\R)$, then
$$
\begin{aligned}
\int_\R \what f(x) g(x) \dd x & = \int_\R g(x) \int_{\R} f(y) e^{-iyx} \dd y \dd x = \iint f(y) g(x) e^{ixy} \dd x \times \dd y = \int_{\R} f(x) \what g(x) \dd x
\end{aligned}
$$
The change of order follows from Fubini's theorem.

##### Convolution

Suppose $f, g \in \L(\R \to \C)$. The convolution of $f$ and $g$ is denoted as $f * g$, and is the function defined by
$$
(f * g)(x) = \int_\R f(y) g(x - y) \dd y
$$

- If $f, g \in L^1(\R)$, $f * g$ is defined almost everywhere, and
  $$
  \n{f * g}_1 \le \int_{\R} \int_{\R} |f(y)||g(x - y)| \dd x \dd y \le \n{f}_1 \n{g}_1
  $$
  following Tonelli's Theorem.
- $(f * g)(x) = (g * f)(x)$ when $(f*g)$ is defined at $x$.
  - This follows from a linear change of variable.


##### $\L^p$-norm of convolution

Suppose $f \in L^1(\R \to \C, \sigma)$ and $g \in L^p(\R \to \C, \sigma)$. For $p \in [1, \infty]$ and $q = p'$.
$$
\n{f*g}_p = \sup_{h \in \L^{q}, \n{h}_q = 1} \abs{\pd{f * g}{h}} = \sup_{h \in \L^q, \n{h}_q = 1} \abs{\int_{\R} (f*g)(x)h(x) \dd x}
$$

- $f * g$ is finite almost surely.
  - Apply the procedure used in proving the $\L^p$-norm of cyclic convolution to $|f| * |g|$.
- $\n{f * g}_p = \n{f}_1 \n{g}_p$.
  - Apply the procedure again on $f * g$.

##### Fourier transform on $L^1$: convolution

Suppose $f, g \in L^1(\R \to \C, \sigma)$. Then $\f[f * g] (\omega) = \what f(\omega) \what g(\omega)$.
$$
\begin{aligned}
\int_{\R} (f* g)(x) e^{-ix\omega} \dd x &= \int_\R \p{\int_{\R} f(y) g(x - y) \dd y} e^{-ix \omega} \dd x\\
&= \int_\R\p{\int_\R g(x - y) e^{-ix\omega} \dd x}f(y) \dd y \\
& = \int_\R \what g(\omega) e^{-iy\omega} f(y) \dd y = \what g(\omega) \what f(\omega)
\end{aligned}
$$

##### Poisson kernel on $\R$

For $y > 0$, define Poisson kernel $P_y: \R \to (0, \infty)$ as
$$
P_y(x) = \frac{1}{\pi} \frac{y}{x^2 + y^2}
$$

- The kernel integrates to one:
  $$
  \begin{aligned}
  \int_\R P_y(x) \dd x & = \int_\R \frac{1}{\pi} \frac{y}{x^2 + y^2} \dd x = \left .\frac{1}{\pi} \arctan\p{\frac{x}{y}} \right |_{-\infty}^\infty = 1
  \end{aligned}
  $$
- The kernel concentrates to zero as $y \downarrow 0$. That is
  $$
  \lim_{y \downarrow 0} \int_{\R - B(0, \delta)} P_y(x) \dd x = 0
  $$
  - Notice the monotonicity, and the fact that $f(y) = {1}/\p{2\pi y}$.

Similarly, for $f \in L^p(\R \to \C)$ where $p \in [1, \infty]$. Define $\P_yf := f * P_y$.

- This is well defined, since $P_y \in L^q$.

##### Poisson convergence theorems on $\R$

Suppose $f \in UC,B(\R \to \C)$. Then $\P_y f\rightrightarrows_{\R} f$ as $y \downarrow 0$.

- A modification of the proof on $\dD$ gives the result.

Suppose $f \in L^p(\R \to \C)$, $p \in [1, \infty)$. Then $\P_y f \to f$ in $L^p$ as $y \downarrow 0$.

##### Fourier inversion formula

Suppose $f, \what f \in L^1(\R \to \C)$ then
$$
f(x) = \F^{-1}[\what f(\omega)] := \frac{1}{2\pi}\int_\R \what f(\omega) e^{ix \omega} \dd \omega
$$

- Therefore $\f$ and $\f^{-1}$ are related by a scaling and time reversal.
- Observe:
  $$
  \begin{aligned}
  \F^{-1} [e^{-y |\omega|}] (x) & = \frac{1}{2\pi}\int_\R e^{-y|\omega|} e^{i \omega x} \dd \omega\\
  &= \frac{1}{\pi} \re \int_{0}^\infty e^{-y \omega} e^{i \omega x} \dd \omega = \frac{1}{\pi}\re \frac{1}{ix - y} = \frac{1}{\pi} \frac{y}{x^2 + y^2} = P_y(x)
  \end{aligned}
  $$
- Further observe:
  $$
  \begin{aligned}
  \frac{1}{2\pi}\int_\R \what f(\omega) e^{-y|\omega|} e^{i x \omega} \dd \omega & = \frac{1}{2\pi} \int_\R \p{\int_\R f(z) e^{-i z \omega}\dd z} e^{-y |\omega|} e^{ix \omega} \dd \omega\\
  &= \int_\R f(z)\F^{-1}[e^{-y|\omega|}](x - z) \dd z\\
  & = f(x) * \F^{-1}[e^{-y |\omega|}] (x) = f(x) * P_y(x) = \P_yf(x)
  \end{aligned}
  $$
- As $y \downarrow 0$, $\text{LHS}\to \f^{-1}[\what f(\omega)]$ pointwise.
  - By dominated convergence, which requires $\what f(\omega) \in L^1$.
- As $y \downarrow 0$, $\text{RHS} \to f(x)$ in $\L^p$ norm.
- Therefore $\f^{-1}[\what f(\omega)] = f(x)$ due to uniqueness of convergence. And we are done.
- At last, we can verify that $\f[P_y(x)] (\omega) = e^{-y|\omega|}$.
  - This is interesting, as directly computing the result is difficult.
  - $\f[e^{-y|\omega|}] = P_y(x)$. Therefore $e^{-y|\omega|} = \f[P_y(x)]$. By applying $\f$ on both sides.

Since $f(x) = \f[\what f] (-x)$, and that $\what f \in L^1$, $f$ must be essentially **uniformly continuous** and **bounded**.

The inversion $\f^{-1}: L^1 \to L^\infty$ is also a continuous linear map.

##### Fourier transform on $L^1$: injective map

Suppose $f(x) \in L^1$ and $\what f(\omega) = 0$, then $f = 0$.

- Since $f, \what f \in L^1$, $f = \f^{-1}[\what f] = 0$.

Therefore $\f, \f^{-1}$ are injective linear map on $L^1$.

##### Fourier transform on $L^2$: Plancherel's Theorem

Suppose $f \in L^1, L^2(\R \to \C)$, and $\what f \in L^1$, then
$$
\begin{aligned}
\n{f}_2^2 &= \int_{\R} f(x) \overline{f(x)} \dd x = \int_{\R} f(-x) \overline{f(-x)} \dd x \\
&= \int_\R 2\pi\what{\what f}(x) \overline {f(-x)} \dd x = 2\pi\int_\R \what f(x) \overline{\what f(x)} \dd x = 2 \pi \norm{\what f(x)}_{2}^2
\end{aligned}
$$
Suppose $f \in L^1, L^2(\R \to \C)$, then $\n{f}_2^2 = 2\pi \n{\what f}_2^2$ is also true.

- Consider $f * P_y$, $(f * P_y) \phat \in L^1$. Thus $\n{f * P_y}_2 = \sqrt{2\pi} \n{(f * P_y)\phat}_2$.
- As $y \downarrow 1$, both LHS and RHS converges to $\n{f}_2$. ==TODO==

Since $L^1$ is dense in $L^2$, this allows us to extend continuous maps $\f$ and $\f^{-1}$ to $L^2$.

- Notice that $\what f$ notation denotes the integral, and $\f$ notation is the transform.

##### Schwartz functions

The Schwartz functions $\S(\R^n \to \C)$ is a subset of $\E(\R^n\to \C)$.
$$
\S(\R^n):= \left \{
\phi \in C^\infty(\R^n): \forall k \in \N^n,\forall m \in \N, \exists C_{m, k} \ge 0, \forall t: |t|^{m}\left|D^{k} \phi(t)\right| \leq C_{m,k}
\right \}
$$
Or equivalently, all partial derivatives of $\phi$ decrease to zero faster than any power of $1/|t|$.

- $\S$ is a vector space over $\C$.
- All functions in $\S$ are bounded and uniformly continuous.
- $\S$ is a subspace of $L^p(\R^n )$, for all $p \in [1, \infty]$.
- $\phi \in \S$ then $D^k \phi \in \S$ for any index $k \in \N^n$.
- $\D$ is a **proper subspace** of $\S$.
- $\D$ is dense in $\S$. for any $\phi \in \S$ there exists a sequence $\phi_\nu(t) \in \D$ that converge in $\S$ to $\phi(t)$.

##### Fourier transform on $\S(\R)$

Suppose $\phi \in \S(\R \to \C)$, then $\f[\phi] \in \S(\R)$ as well.

- By repeated differentiation of $\f[\phi]$ for all $k \in \N$:
  $$
  D^{k} \f[\phi] (\omega)=\f [(-ix)^{k} \phi(x)] (\omega)
  $$
  - $\f[\phi] \in C^\infty(\R)$, and all derivatives are bounded.
- By repeated differentiation of $\phi$ and compute the Fourier transform, for all $k \in \N$:
  $$
  \f [D^{k} \phi] (\xi)=(i\xi)^{k} \f[\phi] (\xi)
  $$
  - $\f[\phi] \in \S(\R)$ since the RHS must be bounded.

Therefore $\f: \S \to \S$ is a **linear isomorphism**.

