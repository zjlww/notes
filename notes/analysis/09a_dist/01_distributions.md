#### Testing Function Spaces

##### Linearity of convergence

Suppose $V$ is a topological vector space with convergence defined. We say convergence is linear if:

- for $f_k \to f$ in $V$ and $g_k \to g$ in $V$, we have $(f_k + g_k) \to (f + g)$ in $V$.
- for $f_k \to f$ in $V$ we have $\alpha f_k \to \alpha f$ in $V$.

##### Testing function space $\D^m(\R^n)$

- Define $\D^{m}(\R^n \to \C):=C_c^m(\R^n\to \C)$. These are $m$-times continuous differentiable functions with compact supports.
- Denote $\D^\infty$ just as $\D$.

Define **topology** on $\D^m(\Omega)$ by defining convergence:

- Suppose $\phi_k, \phi \in \D^m(\Omega)$. $\phi_k \to \phi$ in $\D^m(\Omega)$ if
  - $D^\alpha \phi_k \rightrightarrows_\Omega D^\alpha \phi$ for any $|\alpha|\le m$.
  - The supports of all $\phi_k$ are in the same compact set.

- The convergence is linear.

##### Testing function space $\E^m(\R^n)$

- Define $\E^m(\R^n \to \C) := C^m(\R^n \to \C)$. Denote $\E^\infty$ just as $\E$.

Define **topology** on $\E^m(\R^n)$ by defining convergence:

- Suppose $\phi_k, \phi \in \E^m(\R^n)$. $\phi_k \to \phi$ in $\E^m(\Omega)$ if
  - $D^\alpha \phi_k \rightrightarrows_\Omega D^\alpha \phi$ for any $|\alpha| \le m$, **on any compact set** $\Omega$ of $\R^n$.

- The convergence is linear.

##### Multiplier for space $\D$

A function $\psi \in C^\infty(\R^n)$ is a **multiplier** for space $\D(\R^n)$ if the linear map $\phi \mapsto \psi\cdot \phi$ is continuous.

- Suppose $\psi$ is a multiplier. Then $\phi_k \to \phi$ in $\D$ implies $\phi_k \psi \to \phi \psi$ in $\D$.

##### Partition of unity in $\D$

Suppose $K \subseteq \R^n$ is compact and $(U_i)_{i = 1}^n$ is a open covering with bounded sets.

- There exists $e_i \in \D: \R^n \to [0, 1]$ such that $\su(e_i) \subset U_i$, and $\forall x \in K: \sum_{i}e_i(x) = 1$.
  - Select compact sets $K_i \subseteq U_i$. Where $K \subseteq \cup_i K_i$.
  - For each $K_i$, it is possible to construct $\psi_i \in \D$ where $\su \psi_i \subseteq U_i$ and $\psi_i^{-1}\c{1} \supseteq K_i$.
  - Define $\varphi_1 = \psi_1$, $\varphi_2 = \psi_2 (1 - \psi_1)$, and $\varphi_3 = \psi_3(1 - \psi_1)(1 - \psi_2)$, and so on.
  - Therefore $\varphi = \sum_{i} \varphi_i$ satisfies the requirement.
- For $\varphi \in \D$ and $\su(\varphi) \subseteq K$. We have $\varphi = \sum_{i = 1}^n e_i \varphi$.

##### Approximate $C_c$ with $C_c^\infty$

Suppose $f \in C_c(\R^n )$, there is a sequence $f_k \in C_c^\infty(\R^n )$ such that $f_k \rightrightarrows_{\R^n} f$.

Consider the following kernel for $\alpha > 0$:
$$
\zeta(x)= \begin{cases}0 & |x| \geq 1 \\ \exp \frac{1}{|x|^{2}-1} & |x|<1\end{cases}; \quad \gamma_{\alpha}(x)=\frac{\zeta(x / \alpha)}{\int_{\R^d} \zeta(x / \alpha) \dd t}
$$
Clearly $\gamma_\alpha \in C^\infty_c$. Define $f_{\alpha}: \R^n \to \C$ as
$$
f_{\alpha}(x)=\int_{\R^n} f(y) \gamma_{\alpha}(x - y) \dd y
$$
It is straight forward to verify that $f_\alpha \rightrightarrows f$ as $\alpha \downarrow 0$.

##### Distribution

The (topological) dual space of $\D$ is $\D'$, called the distribution space.

- The distribution spaces are also vector spaces over $\C$.
- For $f \in V'$ and $\phi \in V$, denote $f(\phi) = \pd{\phi}{f}$.

##### Locally integrable functions

Suppose $f \in \L(\R^n )$. $f \in \L^1_\loc(\R^n )$ if
$$
\forall K \subseteq \R \land K \text{ is compact}: \int_K |f| dx < \infty
$$
- $f$ is called **locally (absolute) integrable**.
- $\L^1(\R^n)\subset \L^1_\loc(\R^n)\subset \L(\R^n)$ and $C(\R^n) \subset \L^1_\loc(\R^n)$.
- Functions in $\L^1_\loc$ that almost agree everywhere are considered equivalent, and the quotient space is $L^1_\loc(\R^n )$.

##### Regular distributions in $\D'$

Suppose $f \in L^1_\loc(\R^n)$, for $\phi(t) \in \D$ define $f \in \D'$ as following:
$$
\pd{\phi}{f} := \int_{\R^n} \phi(x) \overline{f(x)} \dd x
$$

- $f\in \D'$ is indeed linear and continuous.
- $f \in L^1_\loc(\R^n)$ is the **generating function** of the distribution $f \in \D'(\R^n)$.
- Distributions generated are called **regular distributions**.
- All other distributions are called **singular distributions**.
- Suppose $f, g \in L^1_\loc$ and if their corresponding regular distributions agree, then $f = g$.

##### Delta functional

Delta functional $\delta \in \D'(\R^n)$ is defined by $\pd{\phi}{\delta}:= \phi(0)$.

##### Heaviside unit step

The Heaviside unit step $u(t): \R$ is defined as
$$
u(t)\triangleq \begin{cases}0 & t<0 \\ 1 & t\ge0\end{cases}
$$

##### Support of distributions

Suppose $A \subseteq \R^n$ is open. Suppose $f \in \D (\Omega )'$. 

- $f$ is **null** on $A$ if $\forall \varphi \in \D(\R^n)$ with $\su(\varphi) \subset A$ we have $\pd{\varphi}{f}=0$.
  - We also say $f = 0$ on $A$.
- The union of all open sets in $\R^n$ where $f = 0$ is the **null set** of $f$. Denoted as $\null(f)$.
- $\Omega \backslash \null f$ is called the **support** of $f$. The support is closed in $\Omega$, denoted as $\su(f)$.

##### Locality of distributions

 ==TODO==

Suppose $f \in \D (\Omega )'$, and $\phi, \psi \in \D(\Omega )$, $\phi = \psi$ on some open neighbor $N$ of $\su(f)$.

- Then $\pd{\phi  - \psi}{f} = \pd{\phi}{f} - \pd{\psi}{f} = 0$. 
- $\phi = \psi$ on the support is not sufficient for this result.

##### Shifting distributions

Suppose $f \in \D'(\R^n)$ we define some simple transformations. Suppose $\phi \in \D$. Define
$$
\pd{\phi(x)}{f(x - y)} := \pd{\phi(x + y}{f(x)}
$$
##### Scaling distributions

Suppose $f \in \D'(\R^n )$, $\psi \in C^\infty(\R^n )$, define $\psi f$ as the following:
$$
\forall \phi \in \D(\R^n): \pd{\phi}{\psi f} := \pd{\overline{\psi} \phi}{f}
$$

- $\psi f$ is clearly a linear functional.
- When $\psi$ is a multiplier of $\D(\R^n)$. $\psi f \in \D'$ is continuous.

##### Topology of $\D'$

Define a particular topology by convergence on space $\D'$.

- $(f_k)_{k = 1}^\infty \in \D'$ converge in $\D'$ if for all $\phi \in \D$, $f_k(\phi)$ converges in $\C$.
- Suppose $f \in \D'$ where $\forall \phi \in \D: \lim_{n \to \infty} \pd{\phi}{f_k} = \pd{\phi}{f}$. We say $f_k \to f$ in $\D'$.
- The convergence defined is clearly linear.
- $\D'$ is closed. ==TODO==

##### Series of distributions

Suppose $f_k \in \D'$, $h_m = \sum_{k=1}^n f_k$ are partial sums. If $h_m \to h$ in $\D'$, the series is said to converge in $\D'$.
