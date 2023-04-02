#### Product Measure and Integral

##### Completion lemma

Suppose $(X, \S, \mu)$ is a measure space, and $(X, \overline \S, \overline \mu)$ is its **completion**.
- For any $E \in \overline \S$, $E = F + N$ where $F \in \S$ and $N$ is a subset of a $\mu$-null set.

For $f \in \L(X \to [0, \infty], \overline \S)$. There exists $g \in \L(X \to [0, \infty], \S)$, where $f = g$ $\mu$.a.e.
- First construct $(f_n) \in S(X \to [0, \infty], \overline \S)$ such that $f_n \uparrow f$ pointwise.
- Now approximate $f_n$ with $g_n \in S(X \to [0, \infty], \S)$ except on null set $G_n$.
    - Suppose $f_n = \sum_{i = 1}^\infty c_i 1_{A_i}$ for $A_i \in \overline \S$. Suppose $A_i = F_i + N_i$ where $A_i \in \S$ and $N_i$ is a subset of a $\mu$-null set.
    - Let $g_n = \sum_{i = 1}^\infty c_i 1_{F_i} \in \L(X \to [0, \infty], \S)$. So $f_n = g_n + \sum_{i = 1}^\infty c_i 1_{N_i}$.
    - Denote $G_n = \cup_i N_i$, clearly $G_n$ is a $\mu$-null set.
- Denote $G = \cup_n G_n$. On $X \backslash G$, $g_n \uparrow f$ pointwise.
- Denote $g = \lim_{n\to \infty} g_n$ on $X \backslash G$ and $g = 0$ on $G$.

##### Cross sections

Suppose $(X_\alpha)_{\alpha \in A}$ and $X = \times_\alpha X_\alpha$.

In the following we assume $\beta \in A$ is a particular index. And $b \in X_\beta$ is a particular value.

We first introduce two operations on a **coordinate** $x \in X$.
- (**Delete coordinate**) For $x \in \times_\alpha X_\alpha$, $x_{-\beta}$ is the **unique** element in $\times_{\alpha \neq \beta} X_\alpha$ where $(x_{-\beta})_\gamma = x_\gamma$ for $\gamma \neq \beta$.
- (**Insert coordinate**) For $y \in \times_{\alpha \neq \beta}X_\alpha$,  $\hat y_b$ is the **unique** element in $\times_\alpha X_\alpha$ where $(\hat y_b)_\gamma = y_\gamma$ for $\gamma \neq \beta$ and $(\hat y_b)_\beta = b$.

Slicing sets:
- When $E \subseteq X$, and $b \in X_\beta$, define the **slice** of $E$ at $x_\beta = b$ as $[E]_b$.
- $[E]_{x_\beta = b} = [E]_b :=\{x_{-\beta}: x \in E, x_\beta = b\} 	\subseteq \times_{\alpha \neq \beta}X_\alpha$.
- Slicing keeps union / intersection. $[\cap_k F_k]_b = \cap_k[F_k]_b$, $[\cup_k F_k]_b = \cup_k[F_k]_b$.
- Slicing keeps complementation $[E^c]_b = [E]_b^c$.

Slicing measurable sets:
- Suppose $(X_\alpha, \S_\alpha)_{\alpha \in A}$ are **measurable spaces**, and $E \in \otimes_\alpha \S_\alpha$. Then $[E]_{b} \in \otimes_{\alpha \neq \beta} \S_\alpha$.
    - Let $\G$ be the good sets in $\otimes_\alpha \S_\alpha$. $\G$ contains all $\pi_\alpha^{-1}[\S_\alpha]$.
    - $\G$ is a $\sigma$-algebra on $\otimes_\alpha \S_\alpha$. So $\G = \otimes_\alpha \S_\alpha$.

Slicing functions:
- Suppose $f: X \to Y$. Define the slice of $f$ at $x_\beta = b$, $[f]_b: \times_{\alpha \neq \beta} X_\alpha \to Y$ as $[f]_b(x) := f(\hat x_b)$.
- (Slicing indicator) For $E \subseteq X$, $[1_E]_b = 1_{[E]_b}$.
- (Slicing limits) $[\lim_n f_n]_b = \lim_n [f_n]_b$.

Slicing measurable functions:
- Suppose $f \in \L(X \to \overline \R, \otimes_\alpha \S_\alpha)$. Then $[f]_b \in \L(\times_{\alpha \neq \beta}X_\alpha \to \overline \R, \otimes_{\alpha \neq \beta} \S_\alpha)$.
    - Suppose $f = 1_E$ for $E \in \otimes_\alpha \S_\alpha$. Then $[1_E]_b = 1_{[E]_b}$ is $\otimes_{\alpha \neq \beta} \S_\alpha$ measurable.
    - For $f \in S(X \to \overline \R, \otimes_\alpha \S_\alpha)$, the result is true.
    - For $f \in \L(X \to \overline \R)$, $f = \lim_n f_n$ where $f_n \in S(X \to \overline \R)$.

##### Tonelli

Suppose $(X, \S, \mu)$ and $(Y, \T, \nu)$ are **$\sigma$-finite measure spaces**.

For $f \in \L(X \times Y \to [0, \infty], \S \otimes \T)$, $\nu[f]_x \in \L(X \to [0, \infty], \S)$.
- For $E \in \S \otimes \T$, $\nu([E]_x) \in \L(X \to [0, \infty], \S)$.
    - Let $\G$ be the good sets in $\S \otimes \T$ where $f \in \L$.
    - Clearly $\G$ contains all cylinders $\E$. $\S \otimes \T = \sigma(\E)$.
    - Suppose $U \in \G$ then $U^c \in \G$.
        - Suppose $Y = +_{n = 1}^\infty Y_n$ where $\nu(Y_n) < \infty$.	
        - $\nu([U^c]_x) = \nu(Y - [U]_x) = \nu(\cup_n (Y_n - [U]_x)) = \sum_n \nu(Y_n - [U]_x) = \sum_n(\nu(Y_n) - \nu[U]_x)$
    - Suppose disjoint $(U_n)_{n = 1}^\infty \in \G$, then $+_n U_n \in \G$.
        - $\nu([+_n U_n]_x) = \nu(+_n[U_n]_x) = \sum_{n} \nu([U_n]_x)$.
    - So $\G$ is a $\sigma$-algebra. So $\G = \S \otimes \T$.
- For $1_E$ where $E \in \S\otimes \T$, $\nu[1_E]_x = \nu(1_{[E]_x}) = \nu[E]_x \in \L(X \to [0, \infty], \S)$.
- For $f \in S(X\times Y \to [0, \infty], \S \otimes \T)$. $\nu[f]_x \in \L(X \to [0, \infty], \S)$.
- For $f \in \L(X \times Y \to [0, \infty], \S \otimes \T)$. Suppose simple $f_n \uparrow f$.
    - Then $\nu[\lim_n f_n]_x = \nu(\lim_n [f_n]_x) = \lim_n \nu[f_n]_x \in \L(X \to [0, \infty], \S)$.

Define $\gamma: \S\otimes \T \to [0, \infty]$ as $\gamma(E) = \mu(\nu[E]_x)$. Then $\gamma = \mu \times \nu$ on $\S \otimes \T$. And $\gamma(E) = \nu(\mu[E]_y)$.
- Let $\E = \{A \times B: A \in \S, B \in \T\}$ then $\sigma(\E) = \S \otimes \T$.
- $\gamma(\varnothing) = 0$ and $\gamma(+_n E_n) = \mu(\nu[+_n E_n]_x) = +_n \gamma(E_n)$.
- So $\gamma$ is the unique measure on $\S \otimes \T$ where $\gamma = \mu \times \nu$ on $\E$.

For $f \in \L(X \times Y \to [0, \infty], \S \otimes \T)$. $\gamma(f) = \mu(\nu[f]_x) = \nu(\mu[f]_y)$.
- For $1_E$ where $E \in \S \otimes \T$, $\gamma(1_E) = \mu(\nu[1_E]_x) = \nu(\mu[1_E]_y)$.
- For $f \in S(X \times Y \to [0, \infty])$.
    - $\gamma(c_i1_{A_i}) = c_i \gamma A_i = c_i \mu(\nu [A_i]_x) = \mu(\nu[c_i1_{A_i}]_x) = \nu(\mu([c_i 1_{A_i}]_y))$.
- For $f \in \L(X \times Y \to [0, \infty])$. Suppose simple $f_n \uparrow f$.
    - $\gamma(f) = \gamma(\lim_n f_n)= \lim_n \gamma f_n = \lim_n\mu(\nu [f_n]_x) = \mu(\lim_n \nu [f_n]_x) = \mu(\nu[f]_x)$.
    - Similarly $\gamma(f) = \nu(\mu[f]_y)$.

##### Tonelli: Corollary

Suppose $E \in \S \otimes \T$ and $(\mu \times \nu)(E) = 0$. Then
$$
\int_{X \times Y} 1_E(x, y) \dd \mu \times \nu(x, y) = \int_X \int_Y 1_E(x, y) \dd \nu(y) \dd \mu(x) = \int_Y \int_X 1_E(x, y) \dd \mu(x) \dd \nu(y) = (\mu \times \nu)(E) = 0
$$

- $[E]_x$ is a $\nu$-null set $\mu$-almost everywhere.
- $[E]_y$ is a $\mu$-null set $\nu$-almost everywhere.

##### Fubini

Suppose $(X, \S, \mu)$ and $(Y, \T, \nu)$ are **$\sigma$-finite measure spaces**.

Suppose $f \in \L^1(X \times Y \to \overline \R, \mu \times \nu)$. Apply (**Tonelli**) to $|f|$ gives:
- $(\mu \times \nu)|f| = \mu(\nu |f|_x) = \nu(\mu|f|_y) < \infty$.
- $\nu|f|_x < \infty$ $\mu$-a.e. and $\mu|f|_y < \infty$ $\nu$-a.e.

Also $f_+, f_- \in \L^1(X \times Y \to [0, \infty], \mu \times \nu)$. Apply (**Tonelli**) again. $\gamma(f) = \mu(\nu[f]_x) = \nu(\mu[f]_y)$.
- $\nu [f_+]_x, \nu[f_-]_x \in \L^1(X \to [0, \infty], \mu)$ and $\mu[f_+]_y, \mu[f_-]_y \in \L^1(Y \to [0, \infty], \nu)$.
- $\nu[f]_x = \nu[f_+ - f_-]_x = \nu([f_+]_x - [f_-]_x) = \nu[f_+]_x - \nu[f_-]_x \in \L^1(X \to \overline \R, \mu)$.
- Similarly $\mu[f]_y = \mu[f_+]_y - \mu[f_-]_y \in \L^1(Y \to \overline \R, \nu)$.
- Notice that $\mu[f]_y$ and $\nu[f]_x$ might be **undefined** on some null sets where $+\infty - (+\infty)$ occurs.
  - Set the undefined values to zero.

- $\gamma(f) = \gamma(f_+ - f_-) = \gamma(f_+)  - \gamma(f_-) = \mu(\nu[f_+]_x) - \mu(\nu[f_-]_x) = \mu(\nu[f]_x) = \nu(\mu[f]_y)$.

##### Area under graph

Suppose $(X, \S, \mu)$ is a measure space. Suppose $f: X \to [0, \infty]$.

- Define $A_f := \{(x, t): x \in X, t \in [0, f(x))\}$, called the **region under graph**.
- $A_f \in \S \otimes \B[0, \infty) \iff f \in \L(X \to [0, \infty], \S)$.
  - $\leftarrow$
    - There exists a simple sequence $f_n \uparrow f$, and $A_f = \cup_n A_{f_n}$.
    - $A_{f_n} \in \S \otimes \mathcal B[0, \infty)$, so $A_f \in \S\otimes \B[0, \infty)$.
  - $\to$
    - $[A_f]_{y} = f^{-1}[y, \infty) \in \S$ so $f \in \L(X \to [0, \infty], \S)$.
- Suppose $\mu$ is $\sigma$-finite. And $f \in \L(X \to [0, \infty], \S)$. Then $(\mu \times \lambda)(A_f) = \mu f$.
  - By (**Tonelli**) $\mu \times \lambda(A_f) = \mu(\lambda[1_{A_f}]_x) = \mu(f) = \lambda(\mu[1_{A_f}]_y)$.

##### Graph

Suppose $(X, \S, \mu)$ is a measure space. Suppose $f: X \to [0, \infty]$.

- Define $G_f:= \{(x, f(x)): x \in X\}$, called the **graph** of $f$.
- $f \in \L(X \to \R, \S) \implies G_f \in \S \otimes \B(\R)$.
  - Hint: intersection of slices.
- Suppose $\mu$ is $\sigma$-finite. And $f \in \L(X \to\R, \S)$. Then $G_f$ is a null set.
  - Hint: In each section, $G_f$ is a null set. $G_f$ is the union of sections.

##### Convolution

Suppose $\mu$ and $\nu$ are finite measures on $\B(\R^d)$. Define $\mu * \nu$ on $\B(\R^d)$ as
$$
\mu * \nu (A) = \mu \times \nu \{x + y \in A: x, y \in \R^d\} = \iint 1_{A}(x + y) \dd \mu(x)\dd \nu(y)
$$
Now suppose $\dd \mu(x) = f \dd x$ and $\dd\nu(y) = g \dd y$ where $f, g \in \L(\R^d \to [0, \infty], \B(\R^d))$ Than by linear shearing.
$$
\mu * \nu (A) = \iint 1_{A}(x + y) f(x) g(y) \dd x \dd y
$$
- Consider transform $\c{u = x + y, v = y}$, then $\mu * \nu$ has density $h(u) := \int f(u - v) g(v) \dd v$.
  $$
  \mu * \nu (A) = \int 1_A(x + y) f(x) g(y) \dd x \dd y = \int 1_A(u) f(u - v) g(v) \dd u \dd v
  $$
- Consider transform $\c{u = x + y, v = x}$, then $\mu * \nu$ has density $h(u) = \int f(v) g(u - v) \dd v$.
  $$
  \mu * \nu (A) = \int 1_A(u) f(v) g(u - v) \dd u \dd v
  $$

#### Iterative Product Measure

##### Markov kernel

Suppose $(X, \S)$ and $(Y, \T)$ are measurable spaces.

Function $\kappa: X \times \T \to [0, \infty]$ is called a **Markov kernel** if

- For all $x \in X$, $[\kappa]_x: \T \to [0, \infty]$ are measures on $\T$.
- For all $T \in \T$, $[\kappa]_T(x) \in \L(X \to [0, \infty], \S)$.

$(X, \S)$ is the **source space**, and $(Y, \T)$ is the **target space**.

- $\kappa$ is **uniformly $\sigma$-finite** if
  - For some $(T_n)_{n = 1}^\infty \in \T$ where $Y = +_n T_n$.
  - For all $T_n$ we have $\sup_{x \in X}[\kappa]_{T_n}(x) < \infty$.
- $\kappa$ is a probability kernel if $[\kappa]_x$ are all probability measures.

##### Iterative product measure

Suppose $(X, \S)$ and $(Y, \T)$ are measurable spaces.

Suppose $\mu$ is a **$\sigma$-finite** measure on $\S$, and $\nu$ is a **uniformly $\sigma$-finite kernel** from $\S$ to $\T$.

Define $\lambda(A \times B) := \mu_A(\nu(x, B))$ on **the semi-algebra of rectangles** in $\S \otimes \T$.

Then $\lambda$ is a measure on the semi-algebra.

- $\lambda$ is a proto-measure.
- $\lambda$ is $\sigma$-finite on $\S$.
  - Since $\mu$ is $\sigma$-finite, there exists $\p{X_i}_{i=1}^\infty$ where $X = \cup X_i$ and $\mu(X_i) < \infty$.
  - Since $\nu$ is uniformly $\sigma$-finite, there exists $\p{Y_j}_{j=1}^\infty$ where $Y = \cup Y_j$, and $\sup_{x \in X} [\kappa]_{Y_j}(x) < \infty$.
  - Now just consider $\p{X_i \times Y_j}_{i, j}$.
- $\lambda$ is countably additive.
  - Suppose $A = C \times D, (B_i)_{i = 1}^\infty \in \S$. And $A = +_i B_i$. Where $B_{i} = C_i \times D_i$.
  - Then $1_{A}(x, y) = \sum_{i = 1}^\infty 1_{B_i}(x, y)$.
  - Now observe the following:
    $$
    \sum_{i=1}^\infty 1_{C_i}(x) \nu(x, D_i) = \sum_{i=1}^\infty \nu(x, [B_i]_x) = 1_C(x) \nu(x, D) = \nu(x, [A]_x)
    $$
  - Now integrate on both sides, $\lambda(A) = \sum_{i = 1}^\infty \lambda(B_i)$.

Therefore $\widetilde \lambda$ is the unique extension of $\lambda$ to $\S \otimes \T$. Define $\mu \times \nu := \widetilde \lambda$.

The following are clear generalizations of this theorem:

- $\mu$ can also be a **uniformly $\sigma$-finite kernel**.
- There can be more than two measure / kernel. And the result is again unique.

##### Iterative Tonelli

Suppose $(X, \S)$ and $(Y, \T)$ are measurable spaces. Suppose $\mu$ is a **$\sigma$-finite** measure on $\S$, and $\nu: X \times \T \to [0, \infty]$ is a **uniformly $\sigma$-finite kernel**. Let $\gamma = \mu \times \nu$.

For $f \in \L(X \times Y \to [0, \infty], \S \otimes \T)$, $[\nu]_x[f]_x \in \L(X \to [0, \infty], \S)$.

- For $E \in \S \otimes \T$, $[\nu]_x[E]_x \in \L(X \to [0, \infty], \S)$.
  - Let $\G$ be the good sets in $\S \otimes \T$ where $f \in \L$.
  - Clearly $\G$ contains all cylinders $\E$. Recall that $\S \otimes \T = \sigma(\E)$.
  - Suppose $U \in \G$ then $U^c \in \G$.
    - Suppose $Y = +_{n = 1}^\infty Y_n$ where $\sup_x[\nu]_x(Y_n) < \infty$.
      $$
      \begin{aligned}\
      [\nu]_x[U^c]_x & = [\nu]_x(Y - [U]_x) = [\nu]_x(+_n (Y_n - [U]_x)) \\ &=
      \sum_n [\nu]_x(Y_n - [U]_x) = \sum_n([\nu]_xY_n - [\nu]_x[U]_x)
      \end{aligned}
      $$
    - So $[\nu]_x[U^c]_x$ is the sum of $\L(X \to [0, \infty])$ functions.
  - Suppose disjoint $(U_n)_{n = 1}^\infty \in \G$, then $+_n U_n \in \G$.
    - $[\nu]_x[+_n U_n]_x = [\nu]_x(+_n[U_n]_x) = \sum_{n} [\nu]_x[U_n]_x$.
  - So $\G$ is a $\sigma$-algebra. So $\G = \S \otimes \T$.
- For $1_E$ where $E \in \S\otimes \T$, $[\nu]_x[1_E]_x = [\nu]_x(1_{[E]_x}) = [\nu]_x[E]_x \in \L(X \to [0, \infty], \S)$.
- For $f \in S(X\times Y \to [0, \infty], \S \otimes \T)$. $[\nu]_x[f]_x \in \L(X \to [0, \infty], \S)$.
- For $f \in \L(X \times Y \to [0, \infty], \S \otimes \T)$. Suppose simple $f_n \uparrow f$.
  - Then $[\nu]_x[\lim_n f_n]_x = [\nu]_x(\lim_n [f_n]_x) = \lim_n [\nu]_x[f_n]_x \in \L(X \to [0, \infty], \S)$.

For $f \in \L(X \times Y \to [0, \infty], \S \otimes \T)$. $\gamma(f) = \mu([\nu]_x[f]_x)$.

- For $1_E$ where $E \in \S \otimes \T$, $\gamma(1_E) = \gamma(E) = \mu([\nu]_x[E]_x) = \mu([\nu]_x[1_E]_x)$.
- For $f \in S(X \times Y \to [0, \infty])$. Suppose $f = c_i 1_{A_i}$.
  - $\gamma(c_i1_{A_i}) = c_i \gamma A_i = c_i \mu([\nu]_x [A_i]_x) = \mu([\nu]_x[c_i1_{A_i}]_x) = \mu([\nu]_x[f]_x)$.
- For $f \in \L(X \times Y \to [0, \infty])$. Suppose simple $f_n \uparrow f$.
  - $\gamma(f) = \gamma(\lim_n f_n)= \lim_n \gamma f_n = \lim_n\mu([\nu]_x [f_n]_x) = \mu(\lim_n [\nu]_x [f_n]_x) = \mu([\nu]_x[f]_x)$

In classical notation, the theorem says:
$$
\int_{X \times Y} f (\mu \times \nu)(dx, dy) = \int_X \left( \int_Y f(x, y) d \nu(x, dy)\right) \mu(dx)
$$

##### Iterative Fubini

Suppose $(X, \S)$ and $(Y, \T)$ are measurable spaces. Suppose $\mu$ is a **$\sigma$-finite** measure on $\S$, and $\nu: X \times \T \to [0, \infty]$ is a **uniformly $\sigma$-finite kernel**. Let $\gamma = \mu \times \nu$.

Suppose $f \in \L^1(X \times Y \to \overline \R, \mu \times \nu)$. Apply (**Iterative Tonelli**) to $|f|$ gives:

- $(\mu \times \nu)|f| = \mu([\nu]_x |f|_x) < \infty$.
- $[\nu]_x|f|_x < \infty$ $\mu$-a.e.

Also $f_+, f_- \in \L^1(X \times Y \to [0, \infty], \mu \times \nu)$. Apply (**Tonelli**) again. $\gamma(f) = \mu([\nu]_x[f]_x)$.

- $[\nu]_x [f_+]_x, [\nu]_x[f_-]_x \in \L^1(X \to [0, \infty], \mu)$.
- $[\nu]_x[f]_x = [\nu]_x[f_+ - f_-]_x = [\nu]_x([f_+]_x - [f_-]_x) = [\nu]_x[f_+]_x - [\nu]_x[f_-]_x \in \L^1(X \to \overline \R, \mu)$
- $[\nu]_x[f]_x$ might be **undefined** on some $\mu$-null sets where $+\infty - (+\infty)$ occurs. Assume the extended subtraction is applied and $+\infty - (+\infty) = 0$.
- $\gamma(f) = \gamma(f_+ - f_-) = \gamma(f_+)  - \gamma(f_-) = \mu([\nu]_x[f_+]_x) - \mu([\nu]_x[f_-]_x) = \mu([\nu]_x[f]_x)$.

#### Infinite Product Space

##### Countable product of measurable spaces

Suppose $(\Omega_j, \F_j)_{j = 1}^\infty$ are measurable spaces.

We will be using the following indexing notations:

- Define $\Omega_{\infty} := \times_{j = 1}^\infty \Omega_j$ and $\Omega_{s:} := \times_{j = {s}}^\infty \Omega_j$.
- Define $\F_\infty := \otimes_{j = 1}^\infty \F_j$ and $\F_{s:} := \otimes_{j={s}}^\infty \F_j$.
- Define $\Omega_{s : t} := \Omega_{s} \times \cdots \times \Omega_t$.

For $B \in \Omega_{s:t}$, define **cylinder** with base $B$ as the causal extension of $B$.
$$
[B] := \c{\omega_{s:}:\omega \in \Omega_{\infty},\omega_{s:t} \in B}
$$

- When $B = A_{s} \times \cdots \times A_{t}$, $[B]$ is a **rectangular cylinder**.
- When $B \in \F_{s:t}$, $[B]$ is a **measurable cylinder**.

For a fixed $s \ge 0$.

- Let $\E_s := \c{[B]:B \in \F_{s:t}, t > s}$.
  - $\E_s$ is an algebra. $\E := \E_{1:}$.
    - $\E_s$ clearly contains $\varnothing$ and $\Omega_{s \backslash \infty}$.
    - $\E_s$ is closed under complement.
    - $\E_s$ is closed under intersection.
- Let $\mathcal B_s := \c{[B]: B = \times_{i={s}}^{t-1} A_{i}, A_i \in \F_i,t > s}$.
  - $\mathcal B_s$ is the set of all measurable rectangles.
  - $\mathcal B_s$ is a semi-algebra. $\mathcal B := \mathcal B_0$.
- $\sigma(\E_s) = \sigma(\mathcal B_s) = \F_{s:}$ .

##### Countable product of probability spaces

Consider the following assumptions:

- $(\Omega_j, \F_j)_{j = 1}^\infty$ are measurable spaces.
- $(\Omega_1, \F_1, P_1)$ is a **probability space**.
- For $j > 1$, $P_j: \Omega_{:j} \times \F_j \to [0, 1]$ are **probability kernels**.

All finite measures / kernels $P_{s:t}$ are well defined and unique.

Now we attempt to define $P_\infty$ and kernel $P_{s:}$ based on $P_{s:t}$.

- For $[B_{:t}] \in \mathcal B_{\infty}$ define $P_\infty([B_{:t}]) := P_{:t}(B_{:t})$.
- For $[B_{s\backslash t}] \in \mathcal B_{s \backslash \infty}$ define $P_{s \backslash \infty}(\omega_{0 \backslash {s-1}}, [B_{s \backslash t}]) := P^{s\backslash t}(\omega^s,{B^{s\backslash t}})$.
- $P^\infty$ is a proto-measure on $\mathcal B$. $P^\infty$ is finite. $P^\infty$ is finitely additive by definition.
- Suppose $(B_n)_{n = 1}^\infty \in \mathcal B^\infty$ and $B_n \downarrow \varnothing$. Then $P^\infty(B_n) \downarrow 0$.
  - Prove the contrapositive. Suppose $P^\infty(B_n) \downarrow a > 0$.
  - $P^\infty(B_n) = P^1 \times P^{1\backslash t_n} (B_n) = P^1([P^{1\backslash t_n}]_{\omega_1}[B_n]_{\omega_1})$.
  - Define $g_n^{(1)}(\omega_1) = [P^{1\backslash t_n}]_{\omega_1} [B_n]_{\omega_1} \in \L(\Omega_1 \to [0, \infty])$.
  - Then $g_n^{(1)} \downarrow g^{(1)}$ where $g^{(1)} \in \L(\Omega_1 \to [0, \infty])$.
  - Since $P^\infty(B_n) > 0$, there exists $\omega_1 \in \Omega_1$ where $g^{(1)}(\omega_1) > 0$.
  - Fix this $\omega_1 \in \Omega_1$. Clearly $[B_n]_{\omega_1} \neq \varnothing$ for all $n$.
  - Now define $Q_s = [P_{s + 1}]_{\omega_1}$, $C_{n} = [B_n]_{\omega_1}$. Define $Q^\infty = [P^{1 \backslash \infty}]_{\omega_1}$.
  - Now $Q^\infty(C_n) \downarrow a_1 > 0$.
  - Repeat above process to obtain $\omega_2 \in \Omega_2$ where $[B_n]_{\omega_1, \omega_2} \neq\varnothing$ for all $n$.
  - So we can construct $\omega \in \Omega^\infty$ where $\omega \in \cap_n B_n$. Contradiction!
- Therefore $P^\infty$ is countably additive on $\mathcal B^\infty$.
- So there is a **unique extension** of $P^\infty$ from $\mathcal B^\infty$ to $\F^\infty$.
- $P^s \times P^{s \backslash \infty} = P^\infty$ on $\F^\infty$. (Hint: verify all rectangles is enough.)

#### Kolmogorov Extension ==TODO==

##### Uncountable product

Suppose $(\Omega_t, \F_t)_{t \in T}$ are measurable spaces.

- Define $\Omega^T = \times_{t \in T} \Omega_t$. Define $\F^T = \times_{t \in T} \F_t$.
- Define $T^<:= \{(v_n)_{n = 1}^m: v_n \in T, m \in \N^+\}$ be the set of finite lists in $T$.
- For $\tau = (\tau_i)_{i = 1}^n \in T^<$ define $\Omega^\tau := \times_{i = 1}^n \Omega_{\tau_i}$. Similarly define $\F^\tau$.
- For $B^\tau \subset \Omega^\tau$, define **cylinder** with **base** $B^\tau$ as $[B^\tau] = \{\omega \in \Omega^T: \omega_{\tau} \in B^\tau\}$.
  - When $B^\tau = A_{\tau_1} \times \cdots \times A_{\tau_n}$ where $A_{\tau_k} \in \Omega_{\tau_k}$. $[B^\tau]$ is a **rectangle**.
  - Cylinder $[B^\tau]$ is **measurable** if $B^\tau \in \F^\tau$.
- Denote the set of all measurable cylinders in $\F^T$ as $\E$. $\E$ is an algebra.
- Denote the set of all measurable rectangles in $\F^T$ as $\mathcal B$. $\mathcal B$ is a semi-algebra.

$\sigma(\E) = \sigma(\mathcal B) = \F^T$. $(\Omega^T, \F^T)$ is a measurable space.

- For $\tau \in T^<$, a probability measure on $\F^\tau$ is often denoted as $P^\tau$.
- A subsequence $\rho = (\tau_{n_k})_{k = 1}^m$ of $\tau$ is denoted as $\rho < \tau$.
- The projection of $P^\tau$ on $\rho$ is $\pi_\rho P^\tau$, defined by $[\pi_\rho P^\tau](B) = P^\tau\{y \in \Omega^\tau:y_\rho \in B\}$.
- Suppose $P^T$ is a probability measure on $\F^T$, projection of $P^T$ is similarly defined.

##### Kolmogorov extension theorem ==TODO==

Suppose $(\Omega_t, \F_t)_{t \in T}$ are measurable spaces where $\Omega_t$ are complete separable metric spaces. And $\F_t$ are corresponding Borel $\sigma$-algebras.

- Most commonly we take $\Omega_t = \R^d$ and $\F_t = \B(\R^d)$.

$\mathcal P = (P^\tau)_{\tau \in T^<}$ where each $P^\tau$ is a probability measure on $\F^\tau$ is called a **consistent finite time probability family** if:

- For any finite time sets $\tau, \rho \in T^<$.
- When $\tau, \rho \in T^<$ are permutation of each other, $P^\tau, P^\rho$ are "permutation" of each other.
- When $\rho$ is a subsequence of $\tau$, $[\pi_\rho P^\tau](\omega^\rho) = P^\rho(\omega^\rho)$.

Then there is a unique probability measure $P$ on $(\times_{t \in T} \Omega_t, \otimes_{t \in T} \F_t)$ where $\pi_\tau P = P^\tau$ for all $\tau \in T^<$.
