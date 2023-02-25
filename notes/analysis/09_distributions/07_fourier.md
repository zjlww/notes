$$
\newcommand{D}{{\mathcal D}}
\newcommand{H}{{\mathcal H}}
\newcommand{G}{{\mathcal G}}
\newcommand{loc}{{\operatorname{loc}}}
\newcommand{M}{\mathcal M}
\newcommand{P}{\mathcal P}
\newcommand{B}{\mathbb B}
\newcommand{E}{\mathcal E}
\newcommand{F}{\mathcal F}
\newcommand{J}{\mathcal J}
\newcommand{A}{\mathcal A}
\newcommand{L}{\mathcal L}
\newcommand{S}{\mathcal S}
\newcommand{su}{\operatorname{supp}}
\newcommand{re}{\operatorname{Re}}
\newcommand{im}{\operatorname{Im}}

\newcommand{pf}{\operatorname{Pf}}
\newcommand{pv}{\operatorname{Pv}}
\newcommand{pd}[2]{\left \langle #1, #2 \right\rangle}
\newcommand{dp}{\mathbf{D}}
\newcommand{ip}{\mathbf{I}}
\newcommand{cas}{\D'_+}
\newcommand{f}{\mathfrak F}
\newcommand{fi}{\mathfrak F^{-1}}
\newcommand{Fi}{\mathcal F^{-1}}
$$

(Fourier Transform on $L^1(\R^n)$)

Suppose $f \in L^1(\R^n \to \C)$ define
$$
\f f(\xi) = \hat{f}(\xi)=\int_{\R ^{n}} f(x) \exp({-ix \cdot \xi}) d x
$$

- $\f f(\xi)$ is **bounded** and **uniformly continuous**.
- Suppose $f, g \in L^1(\R^n)$ and $\alpha, \beta \in \C$, then $\alpha f + \beta g \in L^1(\R^n)$ and $\f (\alpha f+\beta g)=\alpha \f f+\beta\f g$.
- Due to Fubini's Theorem, this integral can be done **coordinate by coordinate**.

Define the inverse Fourier transform of $f$ as following if it exists in Lebesgue integral.
$$
\fi f(\xi) = \check{f}(\xi)=\frac{1}{(2 \pi)^{n}} \int_{\R ^{n}} f(x) \exp({i \xi \cdot x}) d x
$$

------

Suppose $f \in L^1(\R)$ and $f \in D(a, b)$. Then
$$
\forall t \in (a, b): f(t)=\lim _{y \rightarrow \infty} \frac{1}{2 \pi} \int_{-y}^{y} \hat{f}(\omega) e^{i \omega t} d \omega
$$

---

Suppose $f \in L^1(\R)$, define
$$
g_y(t) = \frac{1}{2 \pi} \int_{-y}^{y} \hat{f}(\omega) e^{i \omega t} d \omega
$$
$g_y(t) \to f(t)$ in $\D'(\R)$ sense as $y \to \infty$.

----

Suppose $f, g \in L^1(\R)$. And $\hat f = \hat g$ almost everywhere. Then $f = g$ almost everywhere.

### Fourier Transform on $\S$ and $\S'$

---

Suppose $\phi \in \S(\R^n)$. For all $k \in \N^n$:
$$
D^{k} \f[\phi](\xi)=\f [(-ix)^{k} \phi(x)](\xi)
$$

Clearly $\f[\phi] \in C^\infty(\R^n)$.

-----

Suppose $\phi \in \S(\R^n)$.
$$
\f \left[\frac{\partial \phi}{\partial x_{i}}\right](\xi)=\int_{\R ^{n}} \frac{\partial \phi}{\partial x_{i}}(x) e^{-i(\xi \cdot x)} d x = \int_{ \R ^{n-1}} \int_{ \R } \frac{\partial \phi}{\partial x_{i}}(x) e^{-i(\xi \cdot x)} d x_id x_{\neq i}
$$

By integration by parts:
$$
\f \left[\frac{\partial \phi}{\partial x_{i}}\right](\xi) = i \xi_{k} \int_{\R ^{n}} \phi(x) e^{-i(\xi \cdot x)} d x
$$
Repeat the above procedure, we have for all $k \in \N^n$:
$$
\f [D^{k} \phi](\xi)=(i\xi)^{k} \f[\phi](\xi)
$$

----

Suppose $\phi \in \S(\R^n)$ then $\f[\phi] \in \S(\R^n)$.

---

$\f: \S \to \S$ is a continuous linear map on $\S$.

---

Suppose $\phi \in \S(\R^n)$. For $\tau \in \R^n$, $\lambda \in \R$ and $\varphi \in S$.

- (Shifting) $\f [\phi(x - \tau)](\xi) = \exp(-i \xi\cdot \tau) \f[\phi](\xi)$.

- (Scaling) $\f[\phi(\lambda x)](\xi) ={1} / {|\lambda|^n} \f \phi \left( {\xi}/{\lambda} \right)$.

- (Parseval) This can be proved by Fubini's theorem:
  $$
  \int_{ R ^{n}} \f [\phi](x) \varphi(x) d x=\int_{ R ^{n}} \phi(x) \f [\varphi](x) d x
  $$

---

Suppose $\phi \in \S(\R^n)$, 
$$
\fi[\phi](\xi) = \frac{1}{(2\pi)^n} \int_{\R^n} \phi(x) \exp{(ix \cdot \xi)} dx
$$
Clearly $\fi: \S \to \S$ is also a continuous linear map on $\S$. And
$$
\f \circ \fi[\phi] = \phi = \fi\circ \f[\phi]
$$

---

Suppose $\phi, \varphi \in \S(\R^n)$.
$$
\fi[\phi] = \f[\tilde \phi]/(2\pi)^n; \quad
\f[\widetilde \phi](\xi) = {\f[\phi]}(-\xi)
$$

----

Suppose $\phi, \varphi \in \S(\R^n)$. Then
$$
\f[\phi * \varphi] = \f[\phi] \cdot \f[\varphi];\quad
\f[\phi \cdot \varphi] = \frac{\f[\phi] * \f[\varphi]}{(2\pi)^n}
$$

---

Suppose $\phi, \varphi \in \S(\R^n)$. Then
$$
\int_{\R^n}\phi(t) \overline{\varphi(t)} dt = \frac{1}{(2 \pi)^{n}} \int_{\R ^{n}} \f [\phi](t) \overline{\f[\varphi](t)} d t
$$
In particular:
$$
\int_{\R^n}|\phi(t)|^2 dt = \frac{1}{(2 \pi)^{n}} \int_{\R ^{n}} |\f [\phi](t)|^2 d t
$$

----

Suppose $f \in \S'(\R^n)$. Define $\F[f]$ as a functional over $\S$:
$$
\forall \phi \in \S(\R^n) :\pd{\F[f]}{\phi} = \pd{f}{\F[\phi]}
$$
$\F[f] \in \S'(\R^n)$.

This definition is **compatible** for the case $f \in \S(\R^n)$.

----

Suppose $f \in \S'(\R^n)$. Define $\Fi[f]$ as a functional over $\S$:
$$
\forall \phi \in \S(\R^n) :\pd{\Fi[f]}{\phi} = \pd{f}{\Fi[\phi]}
$$
$\Fi[f] \in \S'(\R^n)$.

This definition is **compatible** for the case $f \in \S(\R^n)$.

----

Suppose $f \in \S'(\R^n)$.
$$
\F\circ \Fi [f] = f = \Fi \circ \F[f]
$$

----

Suppose $f \in \S'(\R^n)$. For any $k \in \N^n$,
$$
D^{k} \F[f](\xi)= \F [(-ix)^{k} f(x)](\xi)
$$
and
$$
\F [D^{k} f](\xi)=(i\xi)^{k} \F[f](\xi)
$$
and
$$
\Fi[f] = \F[\tilde f]/(2\pi)^n; \quad
\F[\widetilde f](\xi) = {\F[f]}(-\xi)
$$

----

$\Fi,\F: \S' \to \S'$ are **continuous linear** maps on $\S'$.

----

Suppose $f \in \S'(\R^n)$ and $\psi \in \S(\R^n)$. For any $\phi \in \S(\R^n)$, we have
$$
\pd{\F[f\star \psi]}{\phi} = \pd{f}{\widetilde \psi * \F[\phi]} = \pd{\F[f]}{\Fi[\widetilde \psi * \F [\phi]]} = \pd{\F[f]}{\F[\psi]\cdot \phi} = \pd{\F f \cdot \F \psi}{\phi}
$$
So $\F[f \star \psi] = \F[f] \cdot \F[\psi]$.

----

For $\phi \in \S(\R^{n}\times \R^{m})$. Notice that Fourier transform can be done **partially** on some variables:

$$
\F[\phi(\xi, \eta)](x, y) = \F_\eta[\F_\xi[\phi(\xi, \eta)](x, \eta)](x, y)
$$
Where
$$
\F_\xi[\phi(\xi, \eta)](x, \eta) = \int_{\R^n} \phi(\xi, \eta) \exp(-ix \cdot \xi) d\xi
$$

Suppose $f \in \S'(\R^n)$ and $g \in \S'(\R^m)$. 
$$
\pd{\F [f(x) \cdot g(y)](\xi, \eta)}{\phi(\xi, \eta)} = \pd{f(x)}{\pd{g(y)}{\F[\phi(\xi, \eta)](x, y)}} = \cdots = \pd{\F f(\xi) \cdot \F g(\eta)}{\phi(\xi, \eta)}
$$

So $\F [f(x) \cdot g(y)](\xi, \eta) = \F f(\xi) \cdot \F g(\eta)$.

### Fourier Transform on $\E'$

##### The space $\E'(\R^n)$

 Suppose $f \in \E'(\R^n)$, that is $f \in \D'(\R^n)$ and has compact support. 

Suppose $\lambda(x) \in \D(\R^n)$ is a **soft indicator** of $\su f$.

For $\phi \in C^\infty(\R^n)$. $\lambda(x) \phi(x) \in \D(\R^n)$. The evaluation can be projected into $\D$:
$$
\pd{f(x)}{\phi(x)} = \pd{f(x)}{\lambda(x)\phi(x)}
$$

---

Suppose $f(t) \in \E'(\R^n) \subset \S'(\R^n)$ with soft indicator $\lambda(t) \in \D(\R^n)$. For $\phi(\omega) \in \S(\R^n)$:

Consider Fourier transform $\pd{\F[f](\omega)}{\phi(\omega)} = \pd{f(t)}{\F [\phi](t)}$.
$$
\pd{\F[f]}{\phi} = \pd{f(t)}{\int_{\R^n} \phi(\omega)\lambda(t)\exp(-i\omega \cdot t) d\omega} = \int_{\R^n}\pd{f(t)}{\lambda(t) \exp(-i\omega\cdot t)} \phi(\omega) d\omega
$$
As a fact: $\pd{f(t)}{\lambda(t) \exp(-i \omega\cdot t)} \in C^\infty(\R^n) \subset L_\loc$.

So $\F[f] \in \D'$ and we can alternatively define:
$$
\F[f](\omega) = \pd{f(t)}{\exp(-i \omega\cdot t)}
$$

----

Suppose $f, g \in \E'(\R^n)$. Then $h = f \star g \in \E'(\R^n)$ (**Prove it!**)
$$
\F[h](\omega) = \pd{h(t)}{\exp(-i \omega \cdot t)} = \pd{f(t)}{\pd{g(\tau)}{\exp(-i\omega\cdot(t + \tau))}} = (\F[f]\F[g])(\omega)
$$
Also we have
$$
\Fi[f \star g] = (2\pi)^n \Fi [f] \Fi[g]
$$
