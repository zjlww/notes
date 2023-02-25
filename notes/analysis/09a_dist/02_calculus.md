##### DCT for locally integrable functions

Suppose $(f_k)_{k = 1}^\infty \in L_\loc(\R^n )$, and $f_k \to f$ a.e. Suppose for some $g \in \L_\loc(\R^n \to [0, \infty])$, $|f_k| \le g$.

- Then clearly $f \in L_{\loc}(\R^n )$.
- For all $\phi \in \D$, by DCT we have:

$$
\lim _{\nu \rightarrow \infty}\left\langle f_{\nu}(t), \phi(t)\right\rangle=\lim _{\nu \rightarrow \infty} \int_{ \R ^{n}} f_{\nu}(t) \phi(t) d t = \int_{\R^{n}} f(t) \phi(t) d t=\langle f(t), \phi(t)\rangle
$$

- So $f_k \to f$ a.e. in $\L_\loc$ implies $f_k \to f$ in $\D'$.

##### Convergent to delta functional

Suppose $(f_k)_{k =1}^\infty \in L_\loc(\R^n)$, and the following are met. Then $f_k \to \delta$ in $\D'$.

1. $(f_k)$ are uniformly bounded in absolute integral.

$$
\exists K > 0, \forall T > 0: \int_{|t|<T}\left|f_{k}(t)\right| d t \le K
$$

2. $f_k \rightrightarrows_U 0$ for all $U = \{t \in \R^n: 0<\tau \leq|t| \leq 1 / \tau<\infty\}$, for all $\tau \in (0, 1)$.
3. The functions concentrate to around zero.

$$
\forall T > 0: \lim_{k \to \infty} \int_{|t| < T} f_k(t) dt = 1
$$

Proof:

- Let $\epsilon > 0$. $\tau > 0$.

$$
\left\langle f_{\nu}, \phi\right\rangle=
\int_{|t| \leq \tau} \phi(0) f_{\nu}(t) d t
+\int_{|t| \leq \tau}[\phi(t)-\phi(0)] f_{\nu}(t) d t
+\int_{|t|>\tau} \phi(t) f_{\nu}(t) d t
$$

- Consider the second term. There exists an $M > 0$ such that $|\phi(t)-\phi(0)| \leq|t| M$.

$$
\int_{|t| \leq \tau}[\phi(t)-\phi(0)] f_{\nu}(t) d t \le \tau M \int_{|t| \leq \tau}\left|f_{\nu}(t)\right| d t \le \tau M K
$$

- The second term is less than $\epsilon / 3$ for small enough $\tau$. Now fix $\tau$.
- Consider the third term. This term converge to $0$ for large enough $\nu$.
- Consider the first term. This term converge to $\phi(0)$ for large enough $\nu$.
- So $\left|\left\langle f_{\nu}, \phi\right\rangle-\langle\delta, \phi\rangle\right| \leq \epsilon$.

##### Convergent to delta functional II

Suppose $f(t) \in L^1(\R^n )$. Suppose $\int_{\R^n} f = 1$. Suppose $|f(t)|= o(1/|t|^n)$ for some $n \ge 0$. Then $\nu^n f(\nu t) \to \delta(t)$ in $\D'$ as $\nu \to \infty$.

### Distributional Differentiation

##### Distributional derivative

Suppose $f \in \D' (\R )$, then $\bD f \in \D'$ in distribution sense is defined as:
$$
\left\langle \bD f(t), \phi(t)\right\rangle=\left\langle f(t),-D\phi(t)\right\rangle
$$

- $\bD f(t)$ is still a distribution (linear and continuous).
- $\bD$ considered as an operator on $\D'$ is clearly not injective.
  - Any functional differs by constant are mapped to the same functional.
- With a non-standard notation, we denote $\bD^k f$ as $f^{[k]}$ sometimes.

##### The Dirac family

Dirac is the derivative of heaviside functional in $\D'$.

- Recall that the Heaviside function $u(t) = 1(t\ge 0) \in \L_\loc(\R)$.
- Therefore $\forall \phi \in \D(\R): \pd u \phi = \int_0^\infty \phi(t) dt$.
- $\pd {\bD u} {\phi} = \pd {u}{-D\phi} = \int_0^\infty -\phi' = \phi(0) = \pd \delta \phi$.

Higher order deriavatives of Dirac functional are commonly used:

- $\pd{\bD^k\delta}{\phi}=\pd{\delta}{(-1)^k\phi^{(k)}}=(-1)^k\phi^{(k)}(0)$.

##### Distributional partial derivative

For $f \in \D'(\R^n)$, define the partial derivatives in distribution sense $\pd {\bD_i f}{\phi} = \pd f{- D_i \phi}$.

- Clearly $\bD_i f \in \D' (\R^n )$ is a continuous linear functional.
- The space $\D'$ is closed under distributional differentiation.

Order of partial differentiation does not matter for distributional partial differentiation.

- For multi-index $k \in \N^n$. $\left\langle \bD^{k} f, \phi\right\rangle=\left\langle f,(-1)^{|{k}|} D^{k} \phi\right\rangle$.

##### Product rule for distributional derivative

Suppose $f \in \D'(\R^n )$, $\psi \in C^\infty(\R^n )$. Then $f \psi \in \D'$.
$$
\begin{aligned}
\left\langle \bD_i(\psi f), \phi\right\rangle &=\left\langle\psi f,-\frac{\partial \phi}{\partial t_{i}}\right\rangle=\left\langle f,-\psi \frac{\partial \phi}{\partial t_{i}}\right\rangle \\
&=\left\langle f,-\frac{\partial}{\partial t_{i}}(\psi \phi)\right\rangle+\left\langle f, \phi \frac{\partial \psi}{\partial t_{i}}\right\rangle \\
&=\left\langle\bD_i f, \psi \phi\right\rangle+\left\langle f, \phi \frac{\partial \psi}{\partial t_{i}}\right\rangle \\
&=\left\langle\psi \bD_i f, \phi\right\rangle+\left\langle f D_i \psi, \phi\right\rangle
\end{aligned}
$$

##### Linearity of distributional derivative

Suppose $f, g \in \D'(\R^n )$. $\alpha \in \C$. Then the following are true:
$$
\bD^{k}(f+g)=\bD^{k} f+\bD^{k} g; \quad \bD^{k}(\alpha f)=\alpha \bD^{k} f
$$

##### Continuity of distributional derivative

Consider the space $\D'(\R^n)$ and operator $\bD^k$ for multi-index $k \in \N^n$.

- $\bD^k$ is a continuous linear operator.
- We only need to show continuity.
  - Suppose $(f_n)_{n=1}^\infty, f \in \D'(\R^n)$. Where $f_n \to f$ in $\D'$.
  - $\forall \phi \in \D: \pd {\bD^k f_n}{\phi} = \pd {f_n}{(-1)^{|k|}D^k \phi} \to \pd {f}{(-1)^{|k|}D^k \phi} = \pd {\bD^k f}{\phi}$.
  - Therefore $\bD^k f_n \to \bD^k f$.
- (**Corollary**) Suppose $\sum_{n=1}^\infty f_n \to f$ in $\D'$. Then $\sum_{n=1}^\infty \bD^k f_n \to \bD^k f$ in $\D'$.

### Classical Differentiation and Distributional Differentiation

##### Limit of quotient for distributions

 ^quotient

Suppose $f \in \D(\R)'$,

- $[f(t + \Delta t) - f(t)]/\Delta t \in \D'$ since $\D'$ is a vector space.
- For $\phi \in \D(\R)$, $lim _{\Delta t \rightarrow 0}\left\langle\frac{f(t+\Delta t)-f(t)}{\Delta t}, \phi(t)\right\rangle=\lim _{\Delta t \rightarrow 0}\left\langle f(t), \frac{\phi(t-\Delta t)-\phi(t)}{\Delta t}\right\rangle$.
- For $\phi \in \D(\R)$, define $\phi_{\Delta t}:= [\phi(t - \Delta t) - \phi(t)]/\Delta t$. $\phi_{\Delta t} \to -\phi^{(1)}(t)$ in $\D$ as $\Delta t \to 0$.
  - Define $\psi_{\Delta t}(t) := [\phi(t-\Delta t)-\phi(t)]/\Delta t+\phi^{(1)}(t)$.
  - Since the following:
$$
    \begin{aligned}
    \psi_{\Delta t}^{(k)}(t) &= \frac{1}{\Delta t}\left[\phi^{(k)}(t-\Delta t)-\phi^{(k)}(t)\right]+\phi^{(k+1)}(t) \\
    &=\frac{1}{\Delta t} \int_{t-\Delta t}^{t}\left[\phi^{(k+1)}(t)-\phi^{(k+1)}(x)\right] d x \\
    &=\frac{1}{\Delta t} \int_{t-\Delta t}^{t} \int_{x}^{t} \phi^{(k+2)}(y) d y d x\\
    {|\psi_{\Delta t}^{(k)}}(t)| & \leq \frac{M}{|\Delta t|}\left|\int_{t-\Delta t}^{t} \int_{x}^{t} d y d x\right| \\
    &=\frac{M |\Delta t|}{2} \rightarrow 0
    \end{aligned}
$$
- By continuity of functional $f$, we have:
$$
  \lim _{\Delta t \rightarrow 0}\left\langle\frac{f(t+\Delta t)-f(t)}{\Delta t}, \phi(t)\right\rangle = 
  \left\langle f(t),-\phi^{(1)}(t)\right\rangle= 
  \left\langle f^{[1]}(t), \phi(t)\right\rangle
$$
- Therefore $[f(t+\Delta t)-f(t)]/{\Delta t} \to f^{[1]}$ in $\D'$ as $\Delta t \to 0$.

This result can be generalized to $f \in \D(\Omega )'$ where $\Omega$ is an open set in $\R^n$, and $\phi(t) \in \D(\Omega )$.

The result can be generalized to partial derivatives. 
$$
\lim_{\Delta t_k \to 0}\pd{\frac{f(\ldots, t_k + \Delta t_k, \ldots) - f(t)}{\Delta t_k}}{\phi} = 
\left\langle f(t),-D_k \phi(t)\right\rangle= 
\left\langle \bD_k f(t), \phi(t)\right\rangle
$$
##### Distributional derivative on $C^1(\Omega )$

Suppose $f \in C^1(\Omega)$ where $\Omega$ is an open set in $\R^n$. Then $\pd{\bD_k f}{\phi} = \pd {D_k f}{\phi}$.
- First notice that: $$
\pd {D_k f}{\phi} = \pd{\lim_{\Delta t_k \to 0}\frac{f(\ldots, t_k + \Delta t_k, \ldots) - f(t)}{\Delta t_k}}{\phi}$$
- $({f(\ldots, t_k + \Delta t_k, \ldots) - f(t)})/{\Delta t_k}$ is bounded by the max value of $D_k f(t)$ on the **compact support** of $\phi$ due to mean value theorem. [[05_abstract_integral#^dct|DCT]] gives
$$
\pd{\lim_{\Delta t_k \to 0}\frac{f(\ldots, t_k + \Delta t_k, \ldots) - f(t)}{\Delta t_k}}{\phi} = \lim_{\Delta t_k \to 0}\pd{\frac{f(\ldots, t_k + \Delta t_k, \ldots) - f(t)}{\Delta t_k}}{\phi}
$$
- Further, [[#^quotient|Limit of quotient for distributions]] gives:
$$
\lim_{\Delta t_k \to 0}\pd{\frac{f(\ldots, t_k + \Delta t_k, \ldots) - f(t)}{\Delta t_k}}{\phi} = \pd{\bD_k f}{\phi}
$$

##### Sparsely piecewise continuous

 ^sparse-piecewise

Suppose $f: \R \to \C$. We say that $f$ is **sparsely piecewise continuous** if:
- Let $T$ contains all the points where $f(t)$ is discontinuous.
- All discontinuities are jump discontinuities.
- $T$ has no accumulation point in $\R$.
- $T \cap I$ is **finite** for any **compact interval** $I$ in $\R$.

##### Differentiate sparsely piecewise continuous functions

Suppose $f \in L_\loc(\R )$. And $f$ is [[#^sparse-piecewise|sparsely piecewise continuous]].
- Suppose the discontinuities are $T = (t_{\nu})_{\nu \in \Z}$.
- Define jump $\Delta_\nu = f(t_\nu +) - f(t_\nu-)$ for all $\nu \in \Z$.
- Such an $f$ is locally bounded. Define the continuous component $f_c$ as
$$
f_c(t) = f(t)-\sum_{\nu=-1}^{-\infty} \Delta _{\nu} u\left(t_{\nu}-t\right)+\sum_{\nu=0}^{\infty} \Delta_{\nu} u\left(t-t_{\nu}\right)
$$
- It can be shown that $f_c$ is continuous a.e.
- Define series $(f_k)_{k=0}^\infty \in L_{\loc}(\R)$ as following. $f_k \to f$ in $L_\loc$.
$$
f_k(t) := f_{c}(t) + \Delta_0 u(t)-\sum_{\nu=-1}^{-k} \Delta _{\nu} u\left(t_{\nu}-t\right)+\sum_{\nu=1}^{k} \Delta_{\nu} u\left(t-t_{\nu}\right)
$$
- Now differentiate in distribution sense, we have:
$$
\bD f(t) = \bD f_c(t) + \sum_{\nu=-\infty}^{\infty} \Delta_{\nu} \delta\left(t-t_{\nu}\right)
$$
### Distribution and Trignometric Series

##### Diverging trigonometric series

Polynomial bounded diverging trigonometric series can be interpreted as distributions.

Suppose $|b_n|<M|n|^k$ for some $M, k > 0$. Consider following series
$$
f(t) = \sum_{\nu=-\infty}^\infty b_{\nu} e^{i \nu t}
$$
Suppose $p \ge k + 2$, define
$$
g(t) = \sum_{\nu=-\infty; \nu \neq 0}^{\infty} \frac{b_{\nu}}{(i \nu)^{p}} e^{i \nu t}
$$
Since $b_\nu / (i\nu)^p = o(1/\nu^2)$ it must be absolutely convergent. So $g(t)$ converge uniformly on $t\in \R$, and $g(t)$ is continuous everywhere, with period $2\pi$.

Each term of $g(t)$ is in $L_\loc$, and clearly uniformly bounded. So $g \in L_\loc$.

Differentiate $g(t)$ in distribution sense term-by-term for $p$ times. This might generate singular distributions.
$$
g^{[p]}(t) =\sum_{\nu=-\infty; \nu \neq 0}^{\infty} b_{\nu} e^{i \nu t}; \quad f(t) = b_0 + g^{[p]}(t)
$$
##### Impulse train trigonometric series

Consider series
$$
f(t)=\sum_{\nu=-\infty}^{\infty} e^{i \nu t}; \quad g(t)=-\sum_{\nu=-\infty \atop \nu \neq 0}^{\infty} \frac{1}{\nu^{2}} e^{i \nu t} = \frac{\pi^{2}}{6}-\frac{1}{2}(t-\pi)^{2}, t\in (0, 2\pi)
$$

$$
g'(t) = -(t - \pi), t \in (0, 2\pi);\quad g^{[2]}(t) = -1 + 2\pi \sum_{n=-\infty}^\infty \delta(t - 2\pi n)
$$
So
$$
f(t)=\sum_{\nu=-\infty}^{\infty} 2 \pi \delta(t-2 \pi \nu)
$$
### Primitive of Distributions

We only deal with 1D space in this section.

##### Subspace $\H(\R)$ of $\D(\R)$

Define the space $\H \subseteq \D(\R )$ as $\H= \{\phi': \phi \in \D(\R )\}$.
- Suppose $\phi \in \D$. $\phi \in \H$ if and only if $\int_{-\infty}^\infty \phi(t) dt = 0$.
    - Suppose $\phi \in \D \cap \H$ and $\int_{-\infty}^\infty \phi(t) dt \neq 0$. Then $\su (\phi)$ is not bounded!
    - For the other direction, $\psi = \int_{-\infty}^t \phi(\tau) d \tau$ gives a testing primitive.

##### Projection from $\D(\R)$ into $\H(\R)$

Suppose $\phi \in \D(\R)$. Suppose $\phi_0 \in \D \backslash \H$ and $\int_{-\infty}^\infty \phi_0 = 1$.
- Let $k = \int_{-\infty}^\infty \phi$. Define $\chi = \phi - k \phi_0$ and $\psi = \int_{-\infty}^t \chi$.
- Clearly $\psi(t), \chi(t) \in \D$, and $\psi'(t) = \chi(t)$. Therefore $\chi(t) \in \H(\R)$.
- We call $\chi$ the projection of $\phi$ into $\H$. We call $\phi_0$ the **anchor of projection**.

##### Primitive of distributions

For any $\chi \in \H$ and $\psi = \int_{-\infty}^t \chi$. Define functional $f^{[-1]} = \bI f$ as
$$
\pd {\bI f}{\chi} = \pd {f}{-\psi}
$$
For any $\phi \in \D$. The definition requires an anchor $\phi_0 \in \D - \H$ where $\int \phi_0 = 1$.
- We define that $\pd {\bI f}{\phi_0} = 0$.
- Suppose $\phi = \chi +k \phi_0$ for some $\chi \in \H$, and $\psi = \int_{-\infty}^t \chi$.
- 
$$
\left\langle \bI f, \phi\right\rangle = k\left\langle \bI f, \phi_{0}\right\rangle+\left\langle \bI f, \chi\right\rangle = \langle f, -\psi\rangle
$$
- $\bI f$ defined this way is a **distribution**, that is, it is a **continuous linear functional**.
- The map $\bI : \D' \to \D'$ is a linear and continuous map.
- The map $\bI: \D' \to \D'$ is injective.

The distributions with a constant offset are also called primitives of $f$.
$$
\pd {\bI f + c}{\phi} = kc + \pd{\bI f}{\phi}
$$
##### Primitive of classic functions

 Continue with discussion above:

Suppose $f \in L_\loc(\R )$ has **classical primitive** $F: \R $ on $\R$.
$$
\pd {\bI f}{\phi} = \int F \chi = \int F(\phi - \phi_0\int \phi) = \int\left [(F - \int F\phi_0) \phi\right] = \pd {F - \int F \phi_0}{ \phi}
$$
It is guaranteed that $F - \int F \phi_0 \in L_\loc(\R )$. So $If = F - \int F \phi_0$.

So the primitive in classical and distributional sense are the same.

##### Derivative and Primitive in distribution

Suppose $f\in \D'$ and $\phi \in \D$. We have:
$$
\pd {\bD \bI f}{\phi} = \pd {\bI f}{-\phi'} = \pd {f}{\phi}
$$
So $\bD \bI f = f$.

On the other hand,
$$
\pd {\bI \bD f}{ \phi} = \pd {\bD f}{ - \psi} = \pd {f}{\chi} = \pd{f - \pd{f} {\phi_0}}{\phi}
$$
So $\bI \bD f = f - \pd{f} {\phi_0}$. The result is off by a constant similar to the classical case.

##### Integration by part in distribution

 Suppose $\lambda \in C^\infty$ and $f \in \D'$. Then
$$
\bI (\lambda\bD f) +  \bI(D\lambda f) = \bI \bD (\lambda f) = \lambda f + c
$$
##### Primitive of delta function

 
$$
\pd {\bI \delta}{\phi} = \pd{\delta}{-\psi} = - \psi(0) = \pd{u - \pd{u}{\phi_0}}{\phi}
$$
When restricting $\pd{\bI \delta}{\phi} = 0$ when $\phi$ is even, the primitive is $u(t) - 1/2 = \operatorname{sgn}(t) / 2$.

### Parameterized Testing Functions

Suppose $\phi(t, \tau): \R^n \times \R $, $[\phi]^\tau \in \D(\R^n )$ for all $\tau$.

Suppose $f \in \D(\R^n )'$. Define $g(\tau) = \pd{f}{[\phi]^\tau}$.

##### Limit under integral

 Suppose $\tau_0 \in (a, b) = I$.

- $\bigcup_{\tau \in I} \su [\phi]^\tau$ is bounded.
- For any multi-index $k \in \N^n$, $D_t^k\phi(t, \tau) \in C(\R^n \times [a, b])$.

Then the following limit exists at $\tau_0$.
$$
\lim_{\tau \to \tau_0} \pd{f}{[\phi]^\tau} = \pd{f}{[\phi]^{\tau_0}}
$$
##### Derivative under integral

 Suppose $\tau_0 \in (a, b)$.

- $\bigcup_{\tau \in I} \su [\phi]^\tau$ is bounded.
- For any multi-index $k \in \N^n$,
  - $D_t^k \phi(t, \tau) \in C(\R^n \times [a, b])$.
  - $D_\tau D_t^k[\phi]^\tau(t) \in C(\R^n \times [a, b])$.

Then the following derivative exist at $\tau_0$:
$$
D_\tau g(\tau_0) = \pd{f(t)}{D_\tau \phi(t, \tau_0)}
$$
##### Partial distribution

 Suppose $\phi(x, y): \R^n \times \R^m $, and $\phi(x, y) \in \D(\R^{n + m} )$.

Suppose $f \in \D(\R^n\to \C)'$ then define $\theta(y):= \pd{f(x)}{\phi^y(x)}$.

From above theorem, we immediately knows that for any multi-index $k \in \R^m$.
$$
D_y^k \theta(y) = D_{y}^{k}\langle f(x), \phi^y(x)\rangle=\left\langle f(x), D_{y}^{k} \phi^y(x)\right\rangle
$$
So $\theta(y)$ has compact support, and it is infinitely differentiable. So $\theta(y)\in \D(\R^m)$. 

