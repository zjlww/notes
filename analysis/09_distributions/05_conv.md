### Direct Product

----

Suppose $f \in \D'(\R^n)$ and $g \in \D'(\R^m)$. Define

> This theorem also works when $f \in \S'(\R^n)$ and $g \in \S'(\R^m)$. Then $f \cdot g \in \S'(\R^{n + m})$.

$$
\langle f(x) \cdot g(y), \varphi(x, y)\rangle=\langle f(x),\langle g(y), \varphi(x, y)\rangle\rangle, \quad \forall \varphi \in \D (\R ^{n+m})
$$
$f \cdot g \in \D'(\R^{n + m})$ is **well defined, linear and continuous**.

- $f(x) \cdot g(y) = g(y) \cdot f(x)$.
- Direct product of distributions is **associative**.

----

(**Direct product of delta function**) Suppose $\delta(x) \in \D'(\R^n)$ and $\delta(y) \in \D'(\R^m)$, then for all $\phi \in \D(\R^{n} \times \R^m)$.

> Replace $\D$ with $\S$ still works.

$$
\pd{\delta(x) \cdot \delta(y)}{\phi(x, y)} = \pd{\delta(x)}{\pd{\delta(y)}{\phi(x, y)}} = \phi(0, 0) = \pd{\delta(x, y)}{\phi(x, y)}
$$

---

(**Direct product of regular distributions**)

> Replace $L_\loc$ with $L_s$ and $\D$ with $\S$.

Suppose $f \in L_\loc(\R^n)$ and $g \in L_\loc(\R^m)$, then $f(x) g(y) \in L_\loc(\R^{n + m})$.

For all $\phi \in \D(\R^n \times \R^m)$, clearly $\phi(x, y) f(x) g(y) \in L^1(\R^n \times \R^m)$ in Lebesgue measure.
$$
\pd{f(x)\cdot g(y)}{\phi(x, y)} = \pd{f(x)}{\pd{g(y)}{\phi(x, y)}} = \int_{\R^n} \left (\int_{\R^m} \phi(x, y) g(y) f(x) dy\right) dx
$$
So the classical and distributional direct product agrees.

----

(**Support of direct product**) Suppose $f \in \D'(\R^n)$ and $g \in \D'(\R^m)$.

It is apparent that $\su f \cdot g \subseteq \su f \times \su g$.

Suppose $\phi \in \D(\R^n)$ and $\psi \in \D(\R^m)$, then $\phi \cdot \psi \in \D(\R^n \times \R^m)$.
$$
\pd{f(x) \cdot g(y)}{\phi(x) \psi(y)} = \pd{f}{\phi} \cdot \pd{g}{\psi}
$$
So we know that $\su f \cdot g \supseteq \su f \times \su g$.

----

(**Integration and partial evaluation**)

> Still works when replacing $\D$ with $\S$.
>
> Notice that the indicator $1_E \in L^1_s \subset L^1_\loc$.

Suppose $\phi(x, y) \in \D(\R^n \times \R^m)$. And $g \in \D(\R^m)$. Then for $E \in \L(\R^m)$.
$$
\int_{E} \pd{g(y)}{\phi(x, y)} dx = \pd{1_E(x) \cdot g(y)}{\phi(x, y)} = \pd{g(y)}{\int_E \phi(x, y) dx}
$$

### Distributional Convolutions

(**Derivative and Integral**) Suppose $g(t, x) : \R^n \times \R^n \to \C$.
$$
f(t) = \int_{\R^n} g(t,x ) dx
$$

- Suppose $g, D_k g$ are continuous everywhere.
- Suppose $D_k g(x, t)$ is bounded by unsigned integrable function $b(x)$ for all $t$.

$$
\frac{\partial f}{\partial t_{k}}(t)=\int_{\R ^{n}} \frac{\partial g}{\partial t_{k}}(t, x) d x
$$

-----

(**Classical convolution**) For $f, g: \R^n \to \C$ define convolution as:
$$
(f*g)(x) =  \int_{\R^n} f(y) g(x - y) dy
$$

- When all exist, $(f*g) = (g*f)$.
- When all exist, $f*g + f*h = f*(g + h)$.
- When exists, $f *( c g) = c(f*g)$.
- $f * (g * h)\neq (f*g)*h$ in general.

----

**Distributional convolution**.

> The following also works for $f, g \in \S'$, and $\phi \in \S(\R^n)$. Replace all $\D$ with $\S$.

Suppose $f, g \in \D'(\R^n)$.

Suppose $\phi \in \D(\R^{n})$. Define $\phi(x + y) \in C^\infty(\R^{n} \times \R^n)$.

Suppose $\Omega_f$ and $\Omega_g$ are the supports of $f, g$. Then $\Omega = \Omega_f \times \Omega_g$ is the support of $f \cdot g$.

Suppose $\lambda(x, y) \in C^\infty(\R^n)$ is a soft indicator on $\Omega$.

And $\lambda(x, y) \phi(x + y) \in \D(\R^n \times \R^n)$ for any $\phi \in \D$.

This is clearly guaranteed when one of the following is true.

- $\su f$ or $\su g$ is bounded.
- $\su f$ and $\su g$ are both causal / anti-causal.

Then the distributional convolution $f \star g$ **exists**.
$$
\pd{f \star g}{\phi} := \pd{f(x) \cdot g(y)}{\phi(x + y)\lambda (x, y)}
$$

- $f \star g \in \D'(\R^n)$.
- $f \star g = g \star f$.
- $f \star(\alpha g+\beta h)=\alpha f \star g+\beta f \star h$. When both sides exists.
- The support of $f \star g$ is contained in $\Omega_f + \Omega_g$.
- $f \star (g \star h)\neq (f \star g) \star h$ in general.

Notice that the partial $h(x) = \pd{g(y)}{\phi(x + y)\lambda(x, y)} \in \D(\R^n)$.

----

**Classical convolution agree with distributional ones.**

> The following works by replacing $L_\loc$ with $L_s$ and $\D$ with $\S$.
>
> I am not so sure about this the immediately following:

Suppose $f, g \in L_\loc(\R^n)$, then $f(x)g(y) \in L_\loc(\R^n \times \R^n)$.

Suppose $\phi \in \D(\R^n)$.

Suppose $f \star g$ exists. $\lambda \in C^\infty(\R^n \times \R^n)$ is soft indicator of $\Omega_f \times \Omega_g$. $\lambda(x, y) \phi(x + y) \in \D(\R^n \times \R^n)$.
$$
\pd{f \star g}{\phi} = \int f(x)\left (\int g(y) \lambda(x, y)\phi(x + y)dy\right)dx
$$

Fubini's theorem allows to exchange the integral and gives:
$$
\pd{f \star g}{ \phi} = \int_{-\infty}^{\infty} \phi(t)\left[\int_{-\infty}^{\infty} f(\tau) g(t-\tau) d \tau\right] d t
$$
So the interior $(f*g)(t)=\int_{-\infty}^{\infty} f(\tau) g(t-\tau) d \tau$ is defined almost everywhere.

In this case $f*g = f \star g$ in $\D'(\R^n)$.


-----

**Associativity of distributional convolution.**

Suppose $f, g, h \in \D'(\R^n)$.

Suppose one of the following conditions is true:

- The support of all distributions, except for one, are bounded.
- All supports are causal / anti-causal.

Then the following is well defined and true:
$$
(f \star g) \star h = f \star ( g\star h)
$$

> I am assuming that this theorem is also true for the discrete case ...... No idea how to prove it.

### Modifying Distributional Convolutions

(**Convolution with Delta functional**) Consider $f \in \D'(\R^n)$. For any $\phi \in \D(\R^n)$.

> Also $f \in \S'(\R^n)$, for all $\phi \in \S(\R^n)$. The following are still true.

- $\pd{(\bD^m \delta) \star f}{\phi} = \pd{f(x)}{\pd{\bD^m \delta(y)}{\phi(x + y)}} = \pd{f(x)}{(-1)^m D^m\phi(x)} = \pd{\bD^m f}{\phi}$.
- $\delta(t) * u(t) = 1$.

----

(**Time shift**) Suppose $f, g \in \D'(\R^n)$ and $h = f \star g$ exists. Then
$$
h(t-a)=f(t-a) \star g(t)=f(t) \star g(t-a)
$$

----

(**Differentiation**) Suppose $f, g \in \D'(\R^n)$ and $h = f \star g$ exists. Then for all $\phi \in \D(\R^n)$:

> Also works for $f ,g \in \S'(\R^n)$ and $\phi \in \S(\R^n)$.  

$$
\pd{\bD (f \star g)}{\phi} =  \pd{f(x)}{\pd{g(y)}{-D_y\phi(x +y)}} = \pd{f(x)}{\pd{\bD {g(y)}}{\phi(x + y)}} = \pd{f \star (\bD g)}{\phi}
$$

----

(**Continuity of distributional convolution**) Suppose $f_k \to f$ in $\D'(\R^n)$. Suppose $g \in \D'(\R^n)$. For any $\phi \in \D(\R^n)$.

> This theorem also works when replacing $\D$ with $\S$.

Suppose $\Omega_f = \bigcup_k \su f_k$, and $\Omega_g = \su g$. Clearly $\su f \subseteq \Omega_f$.

Suppose $\Omega = \Omega_f \times \Omega_g$. Suppose there **exists** a $\lambda(x, y) \in C^\infty(\R^n \times \R^n)$ that is $1$ on some neighbor of $\Omega$, and zero otherwise.

The above is clearly true if any of the following is true:

- $\su g$ is bounded.
- $\bigcup_k \su f_k$ is bounded.
- $\su g$ and $\bigcup_k \su f_k$ are both causal / anti-causal.

And $\psi(x, y) = \lambda(x, y) \phi(x + y) \in \D(\R^n \times \R^n)$ for any $\phi \in \D$.
$$
\lim_{k\to \infty}\pd{f_k \star g}{\phi} = \pd{f(x)}{\pd{g(y)}{\psi(x, y)}} = \pd{f \star g}{\phi} \implies f_k \star g \to f \star g \text{ in }\D'(\R^n)
$$
### Convolution in $\S$ and $\S'$

----

Suppose $f \in \S(\R^n)$ and $g \in C^\infty(\R^n)$ and $g \in L^1(\R^n)$.

The convolution $f * g$ is well defined since $f(x - y) g(y) \in L^1(\R^n)$ for all $x$.
$$
\begin{aligned} \frac{\partial}{\partial x_{k}} \int_{\R ^{n}} f(x-y) g(y) d y &=\int_{ \R ^{n}} \frac{\partial}{\partial x_{k}}(f(x-y) g(y)) d y \\ &=\int_{ \R ^{n}} \frac{\partial f}{\partial x_{k}}(x-y) g(y) d y=\left(\frac{\partial f}{\partial x_{k}} * g\right)(x) \end{aligned}
$$
Clearly then $f * g \in C^\infty(\R^n)$.

----

Suppose $f, g \in \S(\R^n)$. Then $f * g \in \C^\infty(\R^n)$, also for $k \in \{1, \cdots, n\}$:
$$
\left(\frac{\partial f}{\partial x_{k}} * g\right)(x)=\frac{\partial}{\partial x_{k}}(f * g)(x)=\left(f * \frac{\partial g}{\partial x_{k}}\right)(x)
$$

----

Suppose $f, g \in \S(\R^n)$. Then $f * g \in \S(\R^n)$, since:
$$
\begin{aligned}
 &|x|^{m}\left|D^{k}(f * g)(x)\right| \leq \int_{\R ^{n}}|x|^{m}|g(x-y)|\left|D^{k} f(y)\right| d y\\
&\leq 2^{m}\left(\int_{\R ^{n}}|x-y|^{m}|g(x-y)|\left|D^{k} f(y)\right| d y +\int_{\R ^{n}}|y|^{m}|g(x-y)|\left|D^{k} f(y)\right| d y\right)
\end{aligned}
$$

-----

Suppose $\phi, \psi, \varphi \in \S(\R^n)$ then
$$
\begin{aligned}
\langle\phi * \varphi, \psi\rangle &=\int_{ R ^{n}}(\phi * \varphi)(x) \psi(x) d x=\int_{ R ^{n}} \int_{ R ^{n}} \phi(y) \varphi(x-y) d y \psi(x) d x\\
& = \int_{ R ^{n}} \phi(y)\left(\int_{ R ^{n}} \varphi(x-y) \psi(x) d x\right) d y\\
& = \int_{ R ^{n}} \phi(y)\left(\int_{ R ^{n}} \tilde{\varphi}(y-x) \psi(x) d x\right) d y
\end{aligned}
$$
So it says that $\langle\phi * \varphi, \psi\rangle=\langle\phi, \tilde{\varphi} * \psi\rangle$. Where $\tilde \varphi$ is the transposition of $\varphi$.

-----

Suppose $\phi, \psi, \varphi \in \S(\R^n)$ then the following is true:
$$
(\phi * \psi) * \varphi = \phi * (\psi * \varphi)
$$

----

Suppose $f \in \S'(\R^n)$ and $\psi \in \S(\R^n)$, define functional $f \star \psi = \psi \star f$.

> This extends the definition of convolution in $\S'$ where the support is special.
>
> This definition is compatible with previous definition.

$$
\forall \phi \in \S(\R^n): \pd{f \star \psi}{ \phi} = \pd{f}{\tilde \psi * \phi}
$$
Then $f \star \psi \in \S'(\R^n)$.

-----

Suppose $f_k, f \in \S'(\R^n)$ and $\psi_k, \psi, \varphi \in \S(\R^n)$, then

- (**Derivative**) $\frac{\partial}{\partial x_{k}}(f \star \psi)=\frac{\partial f}{\partial x_{k}} \star \psi=f \star \frac{\partial \psi}{\partial x_{k}}$.
- (**Associative**) $(f \star \psi) \star \varphi = f \star (\psi * \varphi)$.
- (**Linearity in second**) $f_{1} \star\left(\alpha g_{1}+\beta g_{2}\right)=\alpha f_{1} \star g_{1}+\beta f_{1} \star g_{2}$.
- (**Linearity in first**) $\left(\alpha f_{1}+\beta f_{2}\right) * g_{1}=\alpha f_{1} * g_{1}+\beta f_{2} * g_{1}$.

-----

Suppose $f_k \to f$ in $\S'(\R^n)$ and $\psi \in \S(\R^n)$, then $f_k \star \psi \to f \star \psi$ in $\S'$.

Suppose $f \in \S'(\R^n)$ and $\psi \in \S(\R^n)$, then $f \star \psi_k \to f \star \psi$ in $\S'$.

