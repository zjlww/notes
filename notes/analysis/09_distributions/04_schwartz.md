### The Schwartz Space

##### Convergence in $\S$

 $(\phi_k)_{k=1}^\infty \subset \S$ is said to converge to $\phi \in C^\infty$ if
$$
\forall k \in \N^n,\forall m \in \N: |t|^m D^k \phi_\nu(t) \rightrightarrows^\nu_{t \in \R^n} |t|^m D^k \phi(t)
$$

- $\phi \in \S$. $\S$ is closed under convergence.
- Convergence is linear.
- Convergence in $\D$ implies convergence in $\S$.

##### Function of slow growth

 $f \in L_\loc(\R^n )$ is a **function of slow growth** if there exists a number $N \in \N$ such that
$$
\lim _{|t| \rightarrow \infty}|t|^{-N}|f(t)|=\lim _{|t| \rightarrow \infty} \frac{|f(t)|}{|t|^{N}}=0 .
$$
So for any $\epsilon > 0$ there exists a $M > 0$ such that $\forall |t| > M: |f(t)|<\epsilon |t|^N$.

Denote this space as $L_s(\R^n)$.

- Every bounded function is of slow growth.
- Every function in $\S$ is of slow growth.

##### Multipliers

 Define $O_M(\R^n)$ as the subset of $C^\infty(\R^n)$, where all derivatives are in $L_s(\R^n)$.

Suppose $\psi \in O_M$, then $\phi \mapsto \psi \phi$ is a continuous map on $\S$.

##### Common operations

 Let $\phi \in \S \left(\R ^{n}\right), \tau \in \R ^{n}, a \in \R -\{0\}$ and $p(t)$ a polynomial in $\R [t_1 \ldots, t_n]$. Then,

1. $\phi(t+\tau), \phi(-t), \phi(a t) \in \S(\R ^{n})$.
1. Suppose $T \in GL(\R^n)$, $\phi(T(t)) \in \S(\R^n)$
2. $p(t) \phi(t) \in \S (\R ^{n})$.
2. Product of $\phi, \psi \in \S(\R^n)$ remains to be in $\S(\R^n)$.

### Tempered Distributions

##### Distributions of slow growth, tempered distributions

 **Continuous linear** functionals of $\S$ are tempered distributions.

Denote the space of all such functionals $\S(\R^n )'$.

- $\S'$ is a **proper subspace** of $\D'$. $\S'$ is dense in $\D'$.
- Suppose $f_1, f_2 \in \S'$ and $\forall \phi \in \D:\pd{f_1}{\phi} = \pd{f_2}{\phi}$, then since $\D$ is dense in $\S$, $\forall \phi \in \S:\pd{f_1}{\phi} = \pd{f_2}{\phi}$.

##### Convergence in $\S'$

 Suppose $f_k \in \S'$. $f_k$ converge in $\S'$ if for all $\phi \in \S$, $\langle f_k ,\phi\rangle$ converges in $\C$. Define $f: \S $ as
$$
\langle f, \phi \rangle = \lim_{k \to \infty} \langle f_k, \phi \rangle
$$
We say $f$ is the limit in $\S'$, $f_k \to f$ in $\S'$, and also write $\lim_{k \to \infty} f_k = f$.

**$\S'$ is closed under convergence (TODO)** , the above $f \in \S'$.

##### Delta functional

 Define $\delta$ functional as $\pd{\delta}{\phi} = \phi(0)$. $\delta \in \S'$.

##### $L^p(\R^n) \subseteq \S'(\R^n)$

### Regular Tempered Distributions

##### Regular distribution

 If $f \in \L_\loc(\R^n )$, and $\pd{f}{\phi} = \int_{\R ^{n}} f(t) \phi(t) d t$ happens to define a distribution in $\S'$ (or $\D$ before), such distribution is a regular distribution. Other distributions are singular distributions.

##### Any function in $\L_s$ is a tempered functional

 Suppose $f \in \L_s(\R^n )$, then it is a regular distribution in $\S'$.

For any $\phi \in \S$, $\phi f \in L^1(\R^n )$.

Suppose $\phi_k \to \phi$ in $\S$. Notice that
$$
\left|\langle f, \phi\rangle-\left\langle f, \phi_{\nu}\right\rangle\right| =\left|\int_{\R^n} f(t)\left[\phi(t)-\phi_{\nu}(t)\right] d t\right| \leq \int_{\R^n}|f(t)|\left|\phi(t)-\phi_{\nu}(t)\right| d t
$$
So $f$ acting as a functional is continuous. Clearly it is also linear.

- Suppose $f, g \in \L_s \subset \L_\loc$ and their corresponding regular tempered distribution agree, then $f, g$ agree almost everywhere.
  - So $L_s$ is identified with some subspace of $\S'$.
- Two continuous functions that induce the same tempered regular distribution are identical. So $C_s(\R^n )$ is identified with some subspace of $\S'$.
- Similarly $\S \subset C_s$ is identified with some subspace of $\S'$.

##### Chain of spaces

- $\D \subset \S \subset C_s \subset L_s \subset \S' \subset \D'$.
- $L_s \subset L_\loc \subset \D'$.
- $L^p(\R^n) \subset \S'(\R^n)$.
- Distributions in $\D'$ with bounded supports are tempered distributions.

### Convergence in $\S'$

##### Convergence in $\S'$

 Suppose $f_k \in \S'$. $f_k$ converge in $\S'$ if for all $\phi \in \S$, $\langle f_k ,\phi\rangle$ converges in $\C$. Define $f: \S $ as
$$
\langle f, \phi \rangle = \lim_{k \to \infty} \langle f_k, \phi \rangle
$$
We say $f$ is the limit in $\S'$, $f_k \to f$ in $\S'$, and also write $\lim_{k \to \infty} f_k = f$.

**$\S'$ is closed under convergence (TODO)** , the above $f \in \S'$.

(Convergence in $\S$ implies convergence in $\S'$) Suppose $\phi_k \to \phi$ in $\S$, then $\phi_k \to \phi$ in $\S'$.

##### Series of distributions

 Suppose $f_k \in \S'$, $h_m = \sum_{k=1}^n f_k$ are partial sums. If $h_m \to h$ in $\S'$, the series is said to converge in $\S'$.

##### Linearity of convergence in $\S'$

 Suppose $\alpha, \beta \in \C$ and if $\left\{f_{\nu}\right\}_{\nu=1}^{\infty}$ and $\left\{g_{\nu}\right\}_{\nu=1}^{\infty}$ both converge in $\S'$ to $f$ and $g$, respectively, then $\left\{\alpha f_{\nu}+\beta g_{v}\right\}_{\nu=1}^{\infty} \to \alpha f+\beta g$ in $\S'$.

### Operations on $\S'$

##### Closed under operations

 Since $\S'$ is a subspace of $\D'$, operations defined on $\D'$ are also operations on $\S' \to \D'$. Suppose the operations are $\S' \to \S'$, we say $\S'$ is closed under it.

##### Common operations

 Suppose $f, g \in \S(\R^n )'$. $\phi \in \S$. Then we have

- (**Addition**) $\langle f+g, \phi\rangle \triangleq\langle f, \phi\rangle+\langle g, \phi\rangle$.
- (**Multiplication**) $\langle\alpha f, \phi\rangle \triangleq\langle f, \alpha \phi\rangle$ for $\alpha \in \C$.
- (**Shifting**) Suppose $\tau \in \R^n$. $\langle f(t-\tau), \phi(t)\rangle \triangleq\langle f(t), \phi(t+\tau)\rangle$. And $f(t- \tau) \in \S(\Omega + \tau )'$.

##### Linear transform

 Suppose $T \in GL(\R^n)$. Suppose $f \in \S(\R^n )'$. $\phi \in \S$. Define
$$
\langle f(T(t)), \phi(t) \rangle  = \left \langle f(t), \frac{\phi(T^{-1}(t))}{|\det T|}\right\rangle
$$

- (**Transposition**) $\langle f(-t), \phi(t)\rangle \triangleq\langle f(t), \phi(-t)\rangle$.
  - A distribution is **even** if $f(t) = f(-t)$. Otherwise it is odd.
- (**Scaling**) for $a > 0$ $(\langle f(at), \phi(t)\rangle = \langle f(t), \phi(t/a)|a|^{-n}\rangle)$.

##### Infinite continuous product

 Suppose $f \in \S(\R^n )'$.

Suppose $\psi \in O_M(\R^n)$.

For any $\phi \in \S(\R^n )$, $\phi \psi \in \S$. Define $\langle\psi f, \phi\rangle \triangleq\langle f, \psi \phi\rangle$.

Such $\psi f$ is a linear functional, since
$$
\left\langle\psi f, \alpha \phi_{1}+\beta \phi_{2}\right\rangle=\left\langle f, \alpha \psi \phi_{1}+\beta \psi \phi_{2}\right\rangle=\left\langle f, \alpha \psi \phi_{1}\right\rangle +\left\langle f, \beta \psi \phi_{2}\right\rangle 
=\alpha\left\langle\psi f, \phi_{1}\right\rangle+\beta\left\langle\psi f, \phi_{2}\right\rangle
$$
Suppose $\phi_k \to 0$ on $\S$, then $\psi \phi_k \to 0$ on $\S$ as well, so $\psi f$ is continuous.

### Derivative in $\S'$

##### Derivative in $\S'$

 Since $\S' \subset \D'$, we only need to note that $\bD f \in \S'$ for $f \in \S'$.

For multi-index $k$, we have, $\bD^k f \in \S'$ and
$$
\left\langle \bD^{k} f, \phi\right\rangle=\left\langle f,(-1)^{|{k}|} D^{k} \phi\right\rangle
$$

- (**Product rule**) Suppose $f \in \S'(\R^n )$, $\psi \in C_s^\infty(\R^n )$. Then $f \psi \in \S'$.
  $$
  \pd{\bD_i (\psi f)}{ \phi} = \pd{\psi \bD_i f}{\phi} + \pd{f D_i \psi}{\phi}
  $$

- (**Linearity of differentiation**) Suppose $f, g \in \S'(\R^n )$. $\alpha \in \C$.
  $$
  \bD^{k}(f+g)=\bD^{k} f+\bD^{k} g; \quad \bD^{k}(\alpha f)=\alpha \bD^{k} f
  $$

- (**Continuity of differentiation**) Suppose $f_n, f \in \S'(\R^n \to\C)$.
  $$
  f_n \to f \text{ in }\S' \implies \forall k \in \N^n:\bD^k f_n \to \bD^k f \text{ in }\S'
  $$

- (**Differentiate by term**) Suppose $f_n, f \in \S'(\R^n \to\C)$.
  $$
  \sum_{n=1}^\infty f_n \to f \text{ in }\D' \implies \forall k \in \N^n: \sum_{n=1}^\infty \bD^k f_n \to \bD^k f \text{ in } \D'
  $$

### Primitive in $\S'$

##### Derivative of testing functions

 Define the space $\G \subseteq \S(\R )$ as
$$
\G= \{\bD f: f \in \S(\R )\}
$$

- For $f \in \S$, $f \in \G$ then $\int f(t) dt = 0$.
- For $f \in \S$, and $\int f = 0$, $\int^t_{-\infty} f \in \S$.

##### Projection into $\H$

 Suppose $\phi_0 \in \S - \G$. Suppose $\int\phi_0 = 1$.

For any $\phi \in \S(\R )$. Define $\int \phi = k$.

Define $\chi = \phi - k \phi_0 \in \G$. Define $\psi = \int_{-\infty}^t \chi \in \S$.

We say that $\chi$ is the projection of $\phi$ into $\G$ with anchor $\phi_0$.
$$
\phi = \chi + k \phi_0;\quad \psi = \int_{-\infty}^t \chi \in \D
$$
##### Primitive

 For any $\chi \in \G$ and $\psi = \int_{-\infty}^t \chi$. Define functional $f^{[-1]} = \bI f$ as
$$
\pd {\bI f}{\chi} = \pd {f}{-\psi}
$$
For any $\phi \in \S$. The definition requires an anchor $\phi_0 \in \D - \H$ where $\int \phi_0 = 1$.

Suppose $\phi = \chi +k \phi_0$ for some $\chi \in \H$, and $\psi = \int_{-\infty}^t \chi$.

We define that $\pd {\bI f}{\phi_0} = 0$.
$$
\left\langle \bI f, \phi\right\rangle = k\left\langle \bI f, \phi_{0}\right\rangle+\left\langle \bI f, \chi\right\rangle = \langle f, -\psi\rangle
$$

- $\bI f \in \S'$.
- The map $\bI : \S' \to \S'$ is a linear and continuous map.
- The map $\bI: \D' \to \D'$ is injective.

The distributions with a **constant offset** are also called **primitives** of $f$.
$$
\pd {\bI f + c}{\phi} = kc + \pd{\bI f}{\phi}
$$
##### Primitive of classic functions

 Continue with discussion above:

Suppose $f \in L_s(\R )$ has **classical primitive** $F = \int_0^t f(t) dt + c$ for $c \in \C$. Clearly $F \in L_s(\R\to\C)$.
$$
\pd {\bI f}{\phi} = \int F \chi = \int F(\phi - \phi_0\int \phi) = \int\left [(F - \int F\phi_0) \phi\right] = \pd {F - \int F \phi_0}{ \phi}
$$
It is guaranteed that $F - \int F \phi_0 \in L_\loc(\R )$. So $If = F - \int F \phi_0$.

So the primitive for such $f$ in classical and distributional sense are the same.

##### Derivative and Primitive in distribution

Suppose $f\in \S'$ and $\phi \in \S$. We have:
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

 Suppose $\lambda \in C^\infty$ and $f \in \S'$. Then
$$
\bI (\lambda\bD f) +  \bI(D\lambda f) = \bI \bD (\lambda f) = \lambda f + c
$$
##### Boundedness property of $\S'$
$$
\forall f \in \S'(\R ): \forall \phi \in \S, \exists C \ge 0, \exists r \in \N:|\langle f, \phi\rangle| \leq C \sup _{t}\left|\left(1+t^{2}\right)^{r} \phi^{(r)}(t)\right|
$$
##### Partial functional

 Suppose $g(t) \in \S'$ and $\phi(t, \tau)\in \S(\R\times \R)$ then
$$
\psi(t) = \pd{g(\tau)}{\phi(t, \tau)} \in \S(\R)
$$
 And
$$
D_t^k \psi(t) = \pd{g(\tau)}{D^k_t\phi(t, \tau)}
$$