### Parameterized Testing Functions

----

Suppose $\phi(t, \tau): \R^n \times \R \to F$, and $[\phi]^\tau(t) \in \D(\R^n)$. Suppose $f \in \D'(\R^n)$.
$$
g(\tau) := \pd{f(t)}{\phi(t, \tau)}
$$

----

Suppose $I = [a, b]$, $\tau_0 \in I$.

Suppose $\Omega = \bigcup_{\tau \in I} \su [\phi]^\tau$ is bounded by compact $K \subset \R^n$.

Suppose $D^k_t \phi(t,\tau) \in C[\R^n \times I]$. 

Then $D_t^k \phi(t, \tau) \in C[K, I]$.

So $D_t^k \phi(t, \tau) \rightrightarrows_{\R^n}^\tau D_t^k \phi(t, \tau_0)$. So $\phi(t, \tau) \to \phi(t, \tau_0)$ in $\D_t$ when $\tau \to \tau_0$.

So $g(\tau)$ is continuous on $[a, b]$.

----

Suppose $I = [a, b]$, $\tau_0 \in I$.

Suppose $\Omega = \bigcup_{\tau \in I} \su [\phi]^\tau$ is bounded by compact $K \subset \R^n$.

Suppose $D^k_t \phi(t,\tau) \in C[\R^n \times I]$. Suppose $[D_\tau D_t^k\phi](t, \tau) \in C[\R^n \times I]$.

Then
$$
\left.\frac{d g}{d \tau}\right|_{\tau=r_{0}}=\left\langle f(t),\left.\frac{\partial}{\partial \tau} \phi(t, \tau)\right|_{\tau=\tau_{0}}\right\rangle
$$
(**Partial evaluation of testing function**)

> This theorem also works when $g \in \S'$ and $\phi \in \S$.

Suppose $g \in \D'(\R ^{m})$ and $\varphi \in \D(\R^{n}\times \R^{m})$, the function
$$
\psi(x)=\langle g(y), \varphi(x, y)\rangle \in \D(\R^n)
$$
Moreover for every multi-index $\alpha$:
$$
D^{\alpha} \psi(x)=\left\langle g(y), D_{x}^{\alpha} \varphi(x, y)\right\rangle
$$
Also, if $\varphi_{n} \rightarrow \varphi$ in $\D(\R ^{n+m})$, then
$$
\psi_{n}=\left\langle g(y), \varphi_{n}(x, y)\right\rangle \rightarrow \psi \text{ in } \D(\R^n)
$$
