Discussion is restricted to 1D here.

(**Characterization of dirac delta, TODO**) Suppose $f \in \D'$. $m \in \N^+$. Then

$$
t^m f(t) = 0 \iff \exists c_\nu \in \C: f= \sum_{\nu=0}^{m-1} c_{\nu} \delta^{[\nu]}
$$

###  Local Boundedness of Distributions

Consider the **closed interval** $I = [a, b] \subseteq \R$.

(**Bounded support testing functions**) $\phi \in \D_I(\R )$ means that $\phi \in \D(\R )$ and $\su \phi \subseteq I$.

- $\D_I$ is a subspace of $\D$.
- $\D_I$ is closed under convergence. Suppose $\phi_\nu \in \D_I$ and $\phi_\nu \to \phi \in \D$. Then $\phi \in \D_I$.

(**Seminorms for space $\D_I$**) Define $\gamma_k: \D_I \to [0, \infty)$ as
$$
\gamma_k (\phi) : = (b - a)^k \sup_{t \in [a, b]} \left|\phi^{(k)}(t)\right|
$$

- For any $\gamma_k(\phi) = 0$ if and only if $\phi$ is identically zero.

Notice that $\gamma_k(\phi)$ is an **increasing** sequence:
$$
\phi^{(k)}(t) = \int_a^t \phi^{(k+1)}(t) dt \implies \left|\phi^{(k)}(t)\right| \leq(b-a) \sup _{t}\left|\phi^{(k+1)}(t)\right| \implies \gamma_k(\phi) \le \gamma_{k+1}(\phi)
$$
(**Convergence in seminorm**) For any sequence $(\phi_\nu)_{\nu=1}^\infty \subseteq \D_I$.
$$
\phi_\nu \to \phi \text{ in } \D\iff \forall k \in \N :\phi_\nu^{(k)}\rightrightarrows \phi^{(k)} \iff \forall k \in \N: \gamma_k(\phi_\nu - \phi) \to 0
$$
(**Local boundedness of distributions, TODO**)

For any $f \in \D'(\Omega)$, where $I \subset \Omega \subseteq \R^n$, and $\Omega$ is open. There exists $r \ge 0$ and $C > 0$ such that
$$
\forall \phi \in \D_I: |\langle f, \phi\rangle| \leq C \sup _{t}\left|\phi^{(r)}(t)\right|
$$

 ### Local Behavior of Distributions

Consider the **closed interval** $I = [a, b] \subseteq \R$.

(**Distributions are derivatives, TODO**) Suppose $f \in \D'(\Omega)$, where $I \subset \Omega \subseteq \R^n$, and $\Omega$ is open. 

Assume that for some $C > 0$ and $r \ge 0$.
$$
\forall \phi \in \D_I: |\langle f, \phi\rangle| \leq C \sup _{t}\left|\phi^{(r)}(t)\right|
$$
For some $h: \R \to \R$ with support in $I$. We have
$$
\forall \phi \in \D_I: \pd{f}{\phi} = \pd{\bD^{r + 2} h}{\phi}
$$
(**Distribution with bounded supports, TODO**) Suppose $f \in \D(\R )'$, with bounded support. There exists a $r\in \N^+$ and $h(t): \R  \in C[\R]$ such that
$$
f(t) = \bD^{r+2} h(t)
$$
