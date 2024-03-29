#### Measurable Morphisms

##### Pushing set systems

Suppose $f: X \to Y$. Denote $f^{-1} \c{\mathcal C}:= \{f^{-1}B: B \in \mathcal C\}$ for $\mathcal C \subseteq \P(Y)$.

Given a set system $\Y \subseteq \P(Y)$. $f^{-1}\c{\Y}$ is the **pull-back** of $\Y$ by $f$.

Given a set system $\X \subseteq \P(X)$. Let $f_*\c{\X} := \{B \subseteq Y: f^{-1}\s{B} \in \X\}$. $f_*\c{\X}$ is the **push-forward** of $\X$ by $f$.

- Many properties of set systems are preserved during push-back and push-forward.
- Including closed under intersection, union, countable union, complement.

##### Measurable morphism

Suppose $(X, \mathcal B)$ and $(Y, \mathcal C)$ are measurable spaces.

$f: X \to Y$ is called $\mathcal B / \mathcal C$-measurable if $f^{-1}\c{\mathcal C} \subseteq \mathcal B$. Denoted by $f \in \mathcal B/\mathcal C$.

- Denote the set of all $\mathcal B/\mathcal C$-measurable functions from $X$ to $Y$ as $\L(X \to Y)$ or $\L(X \to Y, \mathcal B/\mathcal C)$.
- Suppose $Y$ is a **topological space**. $f$ is $\mathcal B$-measurable if it is $\mathcal B/\B[Y]$ measurable.
- Suppose $X, Y$ are topological spaces. $f: X \to Y$ is **Lebesgue / Borel measurable** if it is $\L[X]$ / $\B[X]$-measurable.
- Suppose $f: X \to Y$ is continuous except for countably many points. Then $f$ is Borel measurable.

We have following properties for general measurable morphisms.

- (**Restriction**) Suppose $f \in \L(X \to Y, \mathcal B / \mathcal C)$. And $E \in \mathcal B$. Then $f|_E \in \L(E \to Y, \mathcal B|_E/\mathcal C)$.
- (**Composition**) Composition of measurable morphisms remains measurable morphisms.
- (**Generator test**) Suppose $\mathcal C = \sigma(\E)$. $f: X \to Y$ is $\mathcal B/ \mathcal C$ measurable iff $f^{-1}\mathcal E \subseteq \mathcal B$.
  - We prove the $\to$ direction:
  - Define $\G:= \{G \in \mathcal C: f^{-1}[G] \in \mathcal B\}$. Then show $\E \subseteq \G$.
  - Inverse image property guarantees $\mathcal G$ is a $\sigma$ algebra. So $\G = \mathcal C$.

##### Coordinates

Suppose $(X, \M)$ and $(Y_\alpha, \S_\alpha)_{\alpha \in A}$ are measurable spaces. $(Y, \S) := \otimes(Y_\alpha, \S_\alpha)$.

Then $f: X \to Y$ is $\M/\S$ measurable iff $f_\alpha = \pi_\alpha \circ f$ are $\M/\S_\alpha$ measurable.

- $\to$ Composition of measurable sets.
- $\from$ Just notice that $\sigma(\E) = \sigma(\cup_\alpha \pi_\alpha^{-1}\c{\S_\alpha}) = \otimes \S_\alpha = \S$.
  - Clearly $f^{-1} \c{\E} \subseteq \M$.

##### Push-forward measure

Suppose $(X, \mathcal B, \mu)$ is a measure space. Suppose $(Y, \mathcal C)$ is a measurable space. And $f \in \L(X \to Y, \mathcal B / \mathcal C)$.

Define the **push-forward measure** of $\mu$ by $f$ on $\mathcal C$ as
$$
f_*\mu: \mathcal C \to [0, \infty]; \quad f_* \mu (E): =\mu \circ f^{-1}(E) = \mu(f^{-1}E)
$$

##### Measurable isomorphism

Suppose $(X, \mathcal B)$ and $(Y, \mathcal C)$ are measurable spaces.

$f: X \to Y$ is a **measurable isomorphism** if

- $f$ is bijective;
- $f \in \L(X \to Y, \mathcal B / \mathcal C)$ and $f^{-1} \in \L(Y \to X, \mathcal C / \mathcal B)$.

The measurable space $(X, \mathcal B)$ and $(Y, \mathcal C)$ are called **isomorphic**.

- Denoted by $(X, \mathcal B) \simeq (Y, \mathcal C)$.

Suppose $(X, \mathcal B) \simeq ([0, 1], \B[0, 1])$ it is a **Borel measurable space**.
- $(\eR, \B(\eR))$ is a Borel measurable space.

##### Measurable functions on atomic measure spaces

Suppose $(X, \M)$ is an **atomic measurable space**, with **countably many** **atoms** $(A_\alpha)_{\alpha \in I}$.

Suppose $Y$ is a **Hausdorff space**, which includes $\R$, $\C$, $[0, \infty]$, $\eR$.

- Single elements in Hausdorff spaces are Borel sets.

Then
$$
f\in \L(X \to Y, \M / \B[Y])\iff\exists (c_\alpha)_{\alpha \in I} \in Y: f(x) = \sum_{\alpha \in I} c_\alpha 1_{A_\alpha}(x)
$$

##### Simple function

Suppose $(X, \M)$ is a **measurable space**. And $Y$ is a **Hausdorff space**.

A function is called **simple** if it takes on finitely many values.

Suppose $f: X \to Y$ is a simple function.

- Suppose $c_1, \cdots, c_n \in Y$ are the distinct **nonzero** values of $f$.
- Define $E_k := f^{-1}\{c_k\}$. Then $f = c_1 1_{E_1} + \cdots + c_n 1_{E_n}$.
  - This is the **standard representation** of $f$.

Denote the set of all $\M$-measurable **simple functions** as $S(X \to Y, \M)$.

- $f$ is $\M$-measurable iff $\p{E_k} \subseteq \M$.

##### $\sigma$-algebra generated by functions

Suppose $(Y_\alpha, \mathcal N_\alpha)_{\alpha \in A}$ are measurable spaces. Suppose $f_\alpha: X \to Y_\alpha$ are some functions.

Define $\M = \sigma(\cup_\alpha f_\alpha^{-1} \c{\mathcal N_\alpha})$ the **minimum $\sigma$-algebra** where $f_\alpha$ are all $\M/ \mathcal N_\alpha$-measurable.

$\M$ is called the $\sigma$-algebra **generated by functions** $\p{f_\alpha}$.

##### Restriction and $\sigma$-algebras

Suppose $\E \subseteq \P(X)$, and $A \subseteq X$. Then $\sigma_A(\E|_A) = \sigma_X(\E)|_A$.

- $\sigma_A(\E|_A) \subseteq \sigma_X(\E)|_A$.
  - $\E \subset \sigma_X(\E)$ so $\E|_A \subseteq \sigma_X(\E)|_A$.
  - Also $\sigma_X(\E)|_A$ is an $\sigma$-algebra on $A$.
- $\sigma_A(\E|_A) \supseteq \sigma_X(\E)|_A$.
  - Define $\S:= \{S\in \sigma_X(\E): S \cap A \in \sigma_A(\E|_A)\}$. $\S$ is a $\sigma$-algebra.
  - $\S$ contains $\E$.

Suppose $(X, G)$ is a topological space. And $A \subseteq X$. Then $\B(X, G)|_A = \B(A, G|_A)$.

#### Measurable Real-valued Functions

##### Number system reduction

Suppose $(X, \M)$ is a **measurable space**.

- $f: X \to \C$ is measurable if and only if $\im f$ and $\re f$ are measurable.
- $f: X \to \eR$ is measurable if and only if $f_+$ and $f_-$ are measurable.

##### Function arithmetics

Suppose $f, g \in \L(X \to \eR, \M)$. Define $h: X \to \eR^2$ as $h(x) := (f(x), g(x))$. $h \in \L(X \to \eR^2)$.
- For $c \in \R$, $cf \in \L(X \to \eR, \M)$.
- $f + g \in \L(X \to \eR, \M)$.
  - Addition is continuous on $E := \eR^2 - \c{(-\infty, \infty), (\infty, -\infty)}$.
  - We assume $h \in \L(X \to E, \M)$.
- $f\cdot g \in \L(X \to \overline \R, \M)$.
  - Multiplication is continuous on $F := \eR^2 - \c{(\pm\infty, 0), (0, \pm\infty)}$.
  - We assume $h \in \L(X \to F, \M)$.
- $1/f \in \L(X \to \R, \M)$.
  - $x \mapsto 1/x$ is continuous on $G:= \eR - \c{0}$.
  - We assume $f \in \L(X \to G, \M)$.
- For $H \in \M$, define $v: X \to \eR$ as $v(x) = 1_{H}(x) f(x) + 1_{H^c}(x) g(x)$. Then $v \in \L(X \to \eR, \M)$.
  - This immediately follows from definition.

##### Function limits

Suppose $(f_n)_{n=1}^\infty \in \L(X\to\eR, \M)$.

- $\inf f_n$ and $\sup f_n$ are in $\L(X \to \eR, \M)$.
- Suppose $f_n \to_X f$ pointwise, then $f \in \L(X \to \eR, \M)$. Since $\lim_n f_n = \limsup_{n} f_n = \inf_n \sup_{k \ge n} f_k$.

Therefore the following sets are in $\M$:

- $C_{\infty} := (\liminf_n f_n)^{-1}(\infty)$ and $C_{-\infty} := (\liminf_n f_n)^{-1}(-\infty)$.
- $C^{\infty} := (\limsup_n f_n)^{-1}(\infty)$ and $C^{-\infty} := (\limsup_n f_n)^{-1}(-\infty)$.
- $C := \{x \in X \backslash(C^{\pm\infty}\cup C_{\pm \infty}): \limsup_n f_n - \liminf_n f_n = 0\}$.
  - Note that $C$ is the set where $\p{f_n}$ converges.


##### Simple approximation of real-valued functions

Suppose $(X, \M)$ is a **measurable space**, and $f\in \L(X \to [0, \infty])$.

$f$ is the limit of an increasing sequence of simple functions.

- Construct function sequence $f_k(x) := \min(\lfloor 2^k f(x) \rfloor / 2^k, k)$.
  - $f_k \in S(X \to \R, \M)$.
  - $\forall x \in X: f_{k}(x) \le f_{k+1}(x) \le f(x)$.
- $f_k \to_X f$, furthermore $f_k \rightrightarrows_X f$ if $f$ is bounded.

$f$ is the countable sum of scaled indicator functions.

- Let $g_k = f_k - f_{k -1} = \sum_{i = 1}^{n_k} c_{ki}1({A_{ki}})$.
- Therefore for some $(A_j)_{j=1}^\infty \in \M$ and $c_{j = 1}^\infty \in (0, \infty)$, $f = \sum_{j = 1}^\infty a_j 1(A_j)$.

Therefore $\L(X \to [0, \infty], \M)$ is the smallest class containing $S(X \to [0, \infty])$ that is closed under pointwise limits.

##### Monotone real functions are measurable

- Suppose $f: X \subseteq \R \to \R$ is increasing, it is continuous at $X\backslash N$, where $N$ is countable.
- Monotone functions in $f: X \subseteq \R \to \R$ are $\B[\R]$-measurable.
- Suppose $f: \R \to \R$ is strictly increasing, $f^{-1}: f[\R] \to \R$ is continuous.
- Suppose $f: X \subseteq \R \to \R$ is increasing, and $X \in \B[\R]$. Then $f[X] \in \B[\R]$.

##### Push-forward decomposition

Suppose $(\Omega, \A)$ and $(\Omega', \A')$ are measurable spaces.

- The two spaces are linked by $\omega \in \L(\Omega \to \Omega', \A / \A')$ where $\A = \omega^{-1}\c{\A'}$.

Suppose $f \in \L(\Omega \to [0, \infty], \A)$.

There exists $\varphi \in \L(\Omega' \to [0,\infty], \A')$ and we have **decomposition** $f = \varphi\circ \omega$.

- Suppose $f = \sum_{j = 1}^\infty a_j 1_{A_j}$ for $a_j > 0$ and $A_j \in \A$.
- Define $\varphi = \sum_{j=1}^\infty a_j 1_{\omega[A_j]}$.

The above result can be generalized to $\R, \eR, \C$ and $\R^n$.

$\varphi$ is called the **push-forward** of $f$ by $\omega$, denoted by $\omega_* f:= \varphi$ or $\varphi = f \circ \omega^{-1}$ symbolically.

##### Atomic set lemma

Suppose $(\Omega, \G, \mu)$ is a **measure space**.

$B \in \G$ is called an **atom** of $\G$ **relative** to $\mu$ if $\mu(B) > 0$ and $\forall A \in \G\land A\subset B:  \mu(A) = 0$.

Now suppose $f \in \L(\Omega \to \eR, \G, \mu)$. And $B$ is an atom relative to $\mu$. Then $f$ is $\mu$-a.e. constant on $B$.

- $g(c):= c\mapsto\mu_B\p{f^{-1}[-\infty, c]}$.
- Suppose $B$ is an atom, $g(c)$ must have one and only one jump up from $0$ to $\mu(B)$.

