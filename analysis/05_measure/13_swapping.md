#### Results on Swapping Limits

(**Function limit $\leftrightarrow$ integral**)

Consider the following assumptions:

- $(X, \M, \mu)$ is a **measure space**.
- $(T, d)$ is a **metric space**. Where $t_0 \in T'$.
- $f(x,t): X \times T \to \eR$.
  - For $\mu$-a.e. $x \in X$, $\lim_{t \to t_0}f(x, t) = h(x) \in \L^1(X \to \eR, \mu)$.
  - For all $t \in U_T(t_0)$, $[f]_t(x) \in \L^1(X \to \eR, \mu)$.
  - For all $t \in U_T(t_0)$, $\abs{[f]_t(x)}$ is bounded by $g(x) \in \L^1(X \to [0, \infty], \mu)$.

Then
$$
\lim_{t \to t_0} \int_X f(x, t) \dd\mu(x) = \int_X \lim_{t \to t_0} f(x, t) \dd\mu(x) = \int_X h(x) \dd \mu(x)
$$

- For all sequence $(t_n)_{n = 1}^\infty \in U(t_0)$ where $t_n \to t_0$, $\mu([f]_{t_n}) \to \mu(h)$.
  - $\lim_n \mu [f]_{t_n} = \mu (\lim_n [f]_{t_n}) = \mu (h)$ by dominated convergence.

(**Derivative $\leftrightarrow$ integral**)

Consider the following assumptions:

- $(X, \M, \mu)$ is a measure space.
- $T \subset \R$ is an open interval. Where $t_0 \in T$.
- $f(x, t): X \times T \to \eR$.
  - For all $(x, t) \in X \times T$, $D_t f(x, t)$ exists.
  - For all $t \in T$, $[f]_t(x) \in \L^1(X \to \eR, \mu)$.
  - For all $t \in T$, $\abs{D_t f(x, t)}$ is bounded by $g(x) \in \L^1(X \to [0, \infty], \mu)$.

Then
$$
D_t\s{\int_X f(x, t) \dd \mu (x)}\p{t_0} = \int_X D_t f(x, t_0) \dd \mu(x)
$$

- For all sequence $(t_n)_{n = 1}^\infty \in U(t_0)$ where $t_n \to t_0$, $D_t \mu\p{[f]_{t}}(t_n) \to \mu(D_t f(x, t_0))$.

  - Define $f_n(x) = (f(x, t_n) - f(x, t_0))/(t_n - t_0)$.

  - By mean value theorem of derivative, $\abs{f_n'(x)}$ is bounded by $g(x)$.

  - Now apply the above theorem on swapping limit and integrals.
    $$
    D_t \s{\int_X f(x, t) \dd \mu(x)}(t_0) = \lim_{n \to \infty} \int_X f_n(x) \dd \mu(x) = \int_X \lim_{n \to \infty} f_n(x) \dd \mu(x) = \int_X D_tf(x, t_0) \dd \mu(x)
    $$

(**Sequence limit $\leftrightarrow$ Derivative**)

Suppose

- $\p{f_n}_{n=1}^\infty: (a, b) \to \R$. Where $f_n \in D(a, b)$.
- $f'_n \rightrightarrows g$ on $(a, b)$.
- For some $c \in (a, b)$, $f_n(c)$ converges to $f(c)$.

Then there exists $f: (a, b) \to \R$, $f_n \rightrightarrows f$ on $(a,b)$, $f \in D(a, b)$ and $f' = g$. Therefore when LHS and RHS are defined:
$$
\lim_{n \to \infty} \p{\frac{\part}{\part x} f_n(x)} = \frac{\part}{\part x} \p{\lim_{n \to \infty} f_n}
$$
Proof:

- Define $f_n^*(x)$ as following:
  $$
  f_n^*(x) = \left\{\begin{array}{cl}
  (f_{n}(x)-f_{n}(c))/(x-c) & \text { if } x \neq c \\
  f_{n}^{\prime}(c) & \text { if } x=c
  \end{array}\right.
  $$

- With mean value theorem of derivative, for each $n, m$, there exists a $x_1$ between $x$ and $c$ where
  $$
  f_n^*(x) - f_m^*(x) =
  \left\{\begin{array}{cl}
  f'_{n}(x_1) - f'_{m}(x_1) & \text { if } x \neq c \\
  f_{n}^{\prime}(c) - f_{m}^{\prime}(c) & \text { if } x=c
  \end{array}\right.
  $$

- Therefore $f_n^*(x)$ is Cauchy. Suppose $\lim_{n \to \infty} f_n^*(x) \to f^*(x)$.

- Since $\sup_x\abs{f_n^*(x) - f_m^*(x)}$ converges to zero. $f_n^*(x) \rightrightarrows_{(a, b)} f^*(x)$.

- Notice that $f_n(x) = f_n(c) + f_n^*(x)(x - c)$.

- Define $f(x) = f(c) + f^*(x) (x - c)$.

- Since $\sup_x \abs{f_n(x) - f(x)} \to 0$, $f_n(x) \rightrightarrows_{(a, b)} f(x)$.

#### Mean Convergence ==TODO==

Suppose $f_n, f: S \subset \R \to F$. Suppose $f_n, f \in R[a, b]$. The sequence $f_n$ **converge in the mean** to $f$ on $[a, b]$ if
$$
\lim _{n \rightarrow \infty} \int_{a}^{b}\left|f_{n}(x)-f(x)\right|^{2} d x=0
$$
Denoted by $\lim_{n\to\infty} f_n \rightsquigarrow f$ on $[a, b]$. Or $f_n(x) \rightsquigarrow^x_{[a, b]}  f(x)$.

- The definition requires that $f_n, f \in R[a, b]$.
- If $f_n \rightsquigarrow f$ on $[a, b]$, it converge in the mean on any **closed subinterval**.

(**UC implies MC**) Suppose $f_n, f \in R[a, b]$.
$$
\lim_{n\to\infty} f_n(x) \rightrightarrows_{[a, b]} f(x) \implies \lim_{n\to \infty} f_n(x) \rightsquigarrow_{[a, b]} f(x)
$$
(**MC implies UC I**) Suppose $f_n \rightsquigarrow f$ on $[a, b]$. Suppose $g \in R[a, b]$. Then we have:
$$
\lim_{n \to \infty} \int_{a}^{x} f_{n}(t) g(t) d t \rightrightarrows^x_{[a, b]} \int_a^x f(t) g(t) dt
$$
(**MC implies UC II**) Suppose $f_n \rightsquigarrow f$ and $g_n \rightsquigarrow g$ on $[a, b]$. Then
$$
\lim_{n \to \infty} \int_{a}^{x} f_{n}(t) g_n(t) d t \rightrightarrows^x_{[a, b]} \int_a^x f(t) g(t) dt
$$


#### Differentiating Parameterized Riemann Integral

(**Differentiating Parameterized Riemann Integral**) ==TODO==

Consider the following function $G: [a, b] \times [a, b] \times [c, d] \to \R$:
$$
G(u, v, w) := \int_{u}^v f(x, w) \dd x
$$

- Suppose $f: S = [a, b] \times [c, d] \to \R$. And $f, D_2 f \in C[S]$.
- 

Consider the following Riemann integral:
$$
 \quad F(y):=\int_{p(y)}^{q(y)} f(x, y) \dd x; \quad y \in [c, d], \quad F(y) = G(p(y), q(y), y); \quad
$$

- 
- Let $S = [a, b] \times [c, d]$.
- Suppose $F: S \to \R$ and $f, D_2 f \in C[S]$.
- Suppose $p, q: [c, d] \to [a, b]$ and $p, q \in D(c, d)$.



Suppose $S = [a, b] \times [c, d]$. Suppose $f: S \to F$. Suppose $f, D_2f \in C[S]$. Suppose $p, q: [c, d] \to [a, b]$ Suppose $p, q \in D(c, d)$.

For $y \in [c, d]$ define

Consider $G(x_1, x_2, x_3) = \int_{x_1}^{x_2} f(t, x_3) dt$. For $x_1, x_2 \in [a, b]$ and $x_3 \in [c, d]$.

- $D_1 G(x_1, x_2, x_3) = -f(x_1, x_3)$.
- $D_2G(x_1, x_2, x_3) = f(x_2, x_3)$.
- $D_3G(x_1, x_2, x_3) = \int_{x_1}^{x_2} D_2 f(t, x_3) dt$.

define $H(y) = (p(y), q(y), y)$, so $F(y) = G \circ H(y)$. 

Clearly $H(y) \in D(c, d)$. Notice that $D_k G \in C[a, b] \times [a, b] \times [c, d]$, so $G \in D[a, b] \times [a, b] \times [c, d]$. Now apply the chain rule, wee have:

$F \in D(c, d)$ and $F'$ is given by:
$$
F^{\prime}(y)=\int_{p(y)}^{q(y)} D_2 f(x, y) d x+f(q(y), y) q^{\prime}(y)-f(p(y), y) p^{\prime}(y)
$$

