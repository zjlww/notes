#### Unsigned Integral

(**Support**)

The support of function $f: X \to F \cup \{0\}$ is $f^{-1}[F\backslash \{0\}]$. Denoted as $\su f$. 

- Suppose $X$ is a **topological space**, the $\su f$ is defined as $\overline{f^{-1}[F \backslash \c{0}]}$.

(**Unsigned integral**)

Suppose $(X, \M, \mu)$ is a measure space.

Suppose $f \in S(X \to [0, \infty], \M)$ has standard representation $f = \sum_{k=1}^n c_k 1_{A_k}$.

Define integral of $f$ with respect to $\mu$ as $\mu f := \sum_{k=1}^n c_k \mu A_k$.

Assume $f, g \in S(X \to [0, \infty], \M)$. We have following properties:

- $\mu f \le \mu g$ if $f \le g$ $\mu$-a.e.
- $\mu f = \mu g$ if $f = g$ $\mu$-a.e.
- $\mu f = 0$ iff $f$ is zero $\mu$-a.e.
- $\mu f < \infty$ iff $f$ is finite $\mu$-a.e.
- $\mu 1_E = \mu E$ if $E \in \M$.
- $\mu(f + g) = \mu f + \mu g$, $\mu(c f) = c\mu f$ for $c \in [0, \infty]$.

For $f \in \L(X \to [0, \infty], \M)$. Define (lower) integral of $f$ with respect to $\mu$ as:
$$
\mu f := \sup \left \{\mu h: h \in S(X \to [0, \infty]), 0 \le h \le f\right\}
$$
An equivalent definition for $\mu f$ would be:

- Let $P_\M[X]$ as the set of **finite partitions** of $X$ where all atoms are in $\M$.
- For $P \in P_\M[X]$, let $L(f, P) := \sum_{j=1}^m \mu(A_j) \inf_{x \in A_j} f(x)$.
- Define $\mu f := \sup\{L(f, P): P \in P_{\M}[X]\}$.

(**Properties of unsigned integral**)

Suppose $f, g, (f_n)_{n = 1}^\infty \in \L(X \to [0, \infty], \M)$. Then

- $\mu f \le \mu g$ if $f \le g$ $\mu$-a.e.
- $\mu f = \mu g$ if $f = g$ $\mu$-a.e.
- $\mu f = 0$ iff $f$ is zero $\mu$-a.e.
- $\mu f < \infty$ iff $f$ is finite $\mu$-a.e.
- $\mu 1_E = \mu E$ if $E \in \M$.
- $\mu(c f) = c \mu f$ for $c \ge 0$.

(**Monotone Convergence Theorem**)

Suppose $f, (f_n)_{n = 1}^\infty \in \L(X \to [0, \infty], \M)$. Then $\mu f_n \uparrow \mu f$ if $f_n \uparrow_X f$.
- $\lim_n \mu f_n \le \mu f$: $f_n \le f$ so $\mu f_n \le \mu f$. Now take limit.
- $\lim_n \mu f_n \ge \mu f$:
    - Suppose $h \in S(X \to [0, \infty], \M)$ and $f \ge h$. Let $t \in (0, 1)$.
    - Suppose $h = c_j 1(A_j)$ is the standard representation (Einstein sum).
    - For $n \ge 1$ define $E_n := \{x \in X: f_n(x) \ge th(x)\}$. $E_n \uparrow X$.
    - $f_n \ge tc_j 1(A_j \cap E_n)$, so $\mu f_n \ge t c_j \mu(A_j \cap E_n)$.
    - So $\lim_n \mu f_n \ge t c_j\mu (A_j) = t \mu h$. So $\lim_n \mu f_n \ge \mu h$.
    - So $\lim_n \mu f_n \ge \mu f$.
- So $\lim_n \mu f_n = \mu \lim_n f_n = \mu f$.

(**Properties of unsigned integral, cont.**)

Suppose $f, g, (f_n)_{n = 1}^\infty \in \L(X \to [0, \infty], \M)$. Then

- $\mu (f + g) = \mu f + \mu g$.

  - Suppose $(f_k)_{k = 1}^\infty, (g_k)_{k = 1}^\infty \in S(X \to [0, \infty])$. and $f_k \uparrow_X f$ and $g_k \uparrow_X g$.

  - Then $(f_k + g_k) \uparrow_X (f + g)$.

  - $\mu (f + g) = \lim_k \mu (f_k + g_k) = \lim_{k} \mu f_k + \lim_k \mu g_k = \mu f + \mu g$.


(**Series of unsigned integrals**)

Suppose $f \in \L(X \to [0, \infty], \M)$. And $\p{\mu_n}$ are measures on $\M$.

Then $\p{\sum_{n = 1}^\infty \mu_n} f = \sum_{n = 1}^\infty \mu_n f$.

- Suppose $(f_k)_{k = 1}^\infty \in S(X \to [0, \infty], \M)$, $f_k \uparrow f$.
- $\sum_{n = 1}^\infty \mu_n f_k = \sum_n \mu_n (\sum_j c_j 1_{A_j}) = \sum_{n, j} c_j \mu_n A_j = (\sum_{n = 1}^\infty \mu_n)f_k$.
- Define $g_k = f_k - f_{k - 1}$ where $f_0(x) := 0$.
- $\sum_n \mu_n f = \sum_n \mu_n (\sum_k g_k) = \sum_{k} \sum_n\mu_n g_k = (\sum_n \mu_n)f$.

(**Unsigned integral of function series, Tonelli**)

Suppose $(f_n)_{n = 1}^\infty \subseteq \L(X \to [0, \infty], \M)$. Then $\mu (\sum_n f_n) = \sum_n \mu f_n$.

- This immediately follows from MCT.

(**Fatou's Lemma**)

Suppose $(f_n)_{n = 1}^\infty \subseteq \L(X \to [0, \infty], \M)$. Then $\mu(\liminf_n f_n) \le \liminf_n \mu (f_n)$.
- Let $g_n = \inf_{k \ge n} f_k$. So $g_n \uparrow \liminf_{k} f_k$.
- $\forall m \ge n: g_n \le f_m$. So $\forall m \ge n: \mu g_n \le \mu f_m$.
- So $\mu g_n \le \inf_{m \ge n} \mu f_m$.
- Take limit $n \to \infty$, $\mu \liminf_n f_n \le \liminf_{n} \mu f_n$.

(**Density of unsigned measure**)

Suppose $\mu$ is a measure on $(X, \mathcal B)$.

Given $f \in \L(X \to [0, \infty], \mathcal B)$, define $\nu: \mathcal B \to [0, \infty]$ as $\nu(A) = \mu(1_A f)$.

- Then $\nu$ is a measure on $(X, \mathcal B)$.
  - This immediately follows from MCT.
- $f$ is a **density function** of $\nu$ with respect to $\mu$. Denoted by $d\nu = fd\mu$.
  - All density functions are equal $\mu$-a.e.

For any $g \in \L(X \to [0, \infty], \mathcal B)$, $\nu g = \mu (fg)$.

- This immediately follows from MCT.

(**Area under the graph in Lebesgue integral**)

For $f \in \L(\R^d \to [0, \infty], \L(\R^d))$.

- The area under the graph is $A_f = \{(x, t) \in \R^{d + 1}:0 \le t < f(x)\}$.
- The graph is $G_f = \{(x, f(x)): x \in \R^{d+ 1}\}$.
- $f \in \L(\R^d \to [0, \infty], \L(\R^d))$ if and only if $A_f\in \L(\R^{d + 1})$.
  - $\to$ Denote $E_n := \cup_k f^{-1}(k\cdot 2^{-n}) \times [k, k + 1) \in \mathcal L(\R^{d + 1})$.
    - $A_f \subseteq E_n$, and $E_n \downarrow A_f$. Therefore $A_f \in \mathcal L(\R^{d + 1})$.
  - $\from$ $A_f = A + N$ where $A \in \mathcal B(\R^{d + 1})$ and $N$ is some $\lambda$-null set.
    - Therefore the cross section $[A]_{t = T} \in \mathcal B(\R^d)$. And $[A_f]_{t = T} \in \L(\R^d)$.
    - Just notice that $[A_f]_{t=T} = f^{-1}[0, T]$.

#### Signed Integral

(**Signed integral**)

Suppose $(X, \M, \mu)$ is a measure space.

Consider $f \in \L(X \to \eR, \M)$.

Define $f_+(x) = \max(0, f(x))$ and $f_- = \max(0, -f(x))$. Then $f = f_+ - f_-$ and $|f| = f_+ + f_-$.

- Consider $I_+:= \mu f_+$ and $I_- = \mu f_-$.
- If $I_+$ or $I_-$ is finite, $f$ is **extended integrable** with respect to $\mu$, denoted by $f \in \overline \L(X \to \eR, \mu)$.
- If $I_+$ and $I_-$ are finite, $f$ is **absolutely integrable** with respect to $\mu$, denoted by $f \in \L^1(X \to \eR, \mu)$.
  - $f$ is absolutely integrable iff $\mu |f| < \infty$.
  - Clearly $\L^1 (X \to \eR, \mu) \subseteq \overline \L(X \to \eR, \mu)$.

For $f \in \overline \L(X \to \eR, \mu)$. Define integral of $f$ with respect to $\mu$ as $\mu f := \mu f_+ - \mu f_-$.

(**Properties of real integrals**)

Suppose $f, g \in \overline \L(X \to \eR, \F, \mu)$. Then

- $\mu f \le \mu g$ if $f \le g$ $\mu$-a.e.
- $\mu f = \mu g$ if $f = g$ $\mu$-a.e.
- $\mu (cf) = c \mu f$ and $cf \in \overline \L(\mu)$ for any $c \in \R$.
- $|\mu f| = |\mu f _+ - \mu f_-| \le \mu f_+ + \mu f_- = \mu |f|$.
- $\mu(f + g) = \mu f + \mu g$ and $f + g \in \overline \L(X \to \eR, \mu)$ if $(f + g)$ is $\mu$-a.e. well defined and $\mu f + \mu g$ is well defined.
    - Since $f + g$ is well defined, $f = \infty$ and $g = -\infty$ happens only on some $\mu$ null set.
        - And $(f + g)^+ - (f + g)^- = f + g = f^+ - f^- + g^+ - g^-$.
    - $\mu f + \mu g$ is well defined, w.l.o.g. suppose $\mu f, \mu g \in (-\infty, +\infty]$.
        - Then $f^-, g^-, (f + g)^{-} \in (0, \infty)$ $\mu$-a.e.
        - $\mu f^-, \mu g^-, \mu (f + g)^- < \infty$.
        - And $(f + g)^+ + f^- + g^- = (f + g)^- + f^+ + g^+$.
    - So $\mu (f + g)^+ + \mu f^- + \mu g^- = \mu (f + g)^- + \mu f^+ + \mu g^+$.
    - And $\mu (f + g)^+ - \mu(f + g)^- = \mu f^+ - \mu f^- + \mu g^+ - \mu g ^-$.
    - And $\mu(f + g) = \mu f + \mu g$.

Suppose $f, g \in \L^1(X \to \eR, \mu)$. Then

- $f + g \in \L^1(X \to \eR, \mu)$. And $\mu(f + g) = \mu f + \mu g$.

(**Comparison lemma**)

Suppose $\mu$ is $\sigma$-finite. And $f, g \in \overline \L(X \to \eR, \F, \mu)$.

If $\forall A \in \F:\mu_A f \le \mu_A g$, $f \le g$ $\mu$-a.e.

- Let $P_n = \{n \ge f > g \ge -n\}$, $P_\infty = \{f = \infty, g < \infty\}$, $P_{-\infty} = \{g = -\infty, f > -\infty\}$.
- Then $P = \{f > g\} = \cup_n P_n \cup P_\infty \cup P_{-\infty}$.
- Prove the converse, suppose $\mu P > 0$.
    - Suppose for $m \in \N \cup \{- \infty, +\infty\}$, $\mu P_m > 0$.
    - Suppose $A = +_k A_k$ for $A_k \in \F^<$.
    - Then $P_m = +_k (A_k \cap P_m)$. And $\mu (P_m \cap A_k) \in (0, \infty)$ for some $k$.
    - Let $B = P_m \cap A_k$.
- For $m \in \N$, $\mu_B (f - g) = \mu_B f - \mu_B g > 0$.
- For $m = \infty$. Further partition $P_\infty = \cup_n \{f = \infty, g < n\}$.
- For $m = -\infty$. Further partition $P_{-\infty} = \cup_n \{f > -n, g = -\infty\}$.

(**Dominated convergence theorem**)

Suppose $(f_n)_{n = 1}^\infty \subseteq \L^1(X \to \eR, \mu)$, and $f \in \L^1(X \to \eR)$.

Suppose $f_n \to f$ $\mu$-a.e. and for $h \in \L^1(X \to [0, \infty], \mu)$, $|f_n| \le h$.

Then $\mu f_n \to \mu f$.

- $\mu (h + f) \le \liminf_n \mu(h + f_n) = \mu h + \liminf_n \mu f_n$.
- $\mu(h - f) \le \liminf_n \mu (h - f_n) = \mu h - \limsup_n \mu f_n$.
- So $\liminf \mu f_n \ge \mu f \ge \limsup_n \mu f_n$.

(**Signed integral of function series, Fubini**)

Suppose $(f_n)_{n = 1}^\infty \in \L^1(X \to \eR, \mu)$ and $\sum_n \mu \abs{f_n} < \infty$.

Then $\mu (\sum_n f_n) = \sum_n \mu f_n$.

- Define $h = \sum_n |f_n|$. Then $\sum_n \mu |f_n| = \mu h < \infty$. So $h \in \L^1(X \to [0, \infty], \mu)$.
- So $\sum_n f_n$ converge $\mu$-a.e. Define $f = \sum_n f_n$ where it converges.
- $\mu |f| = \mu |\sum_n f_n| \le \mu h < \infty$. So $f \in \L^1(X \to \eR, \mu)$.
- Apply DCT, $\sum_n \mu f_n = \mu f = \mu \sum_n f_n$.

(**Fatou's Lemma II**)

Suppose $f \in \L^1(X \to \eR, \mu)$ and $(f_n)_{n = 1}^\infty \in \overline \L(X \to \eR)$.

Then  $\mu(\liminf_n f_n) \le \liminf_n \mu f_n$ if $f_n \ge f$.

- Let $g_n = \inf_{m \ge n} (f_n - f) \in \L(X \to [0, \infty])$. So $g_n \uparrow \liminf_m (f_m - f)$.
- $\mu(\liminf_n f_n - f) = \lim_n \mu g_n \le \liminf_n \mu (f_n - f)$.
- Remove $\mu f$ from both sides.

(**Monotone convergence theorem II**)

Suppose $g \in \L^1(X \to \eR, \mu)$ and $f, (f_n)_{n = 1}^\infty \in \overline \L(X \to \eR)$. 

Suppose $g \le f_n \uparrow f$, then $\lim_n \mu f_n = \mu f$.

- $0 \le f_n^+ \uparrow f^+$ so $\mu f_n^+ \uparrow \mu f^+$. Also $g^-\ge f_n^- \downarrow f^-$, by (DCT) $\mu f_n^- \downarrow \mu f^- < \infty$.
- So $\mu f_n = \mu (f_n^+ - f_n^-) = \mu f_n^+ - \mu f_n^- \uparrow \mu f^+ - \mu f^- = \mu f$.

#### Complex Integral

(**Complex integral**)

Suppose $(X, \M, \mu)$ is a measure space.

For $f \in \L(X \to \C, \M)$. Define the real and imaginary parts $f = \re f + i\im f$. 

- When $\mu \re f < \infty$ and $\mu \im f < \infty$, $f$ is **absolutely integrable** with respect to $\mu$, denoted by $f \in \L^1(X \to \C, \mu)$.
  - $f$ is absolutely integrable iff $\mu |f| < \infty$.

For $f \in \L^1(X \to \C, \mu)$, define the integral $\mu f:= \mu \Re f + i \mu \im f$.

(**Properties of complex integral**)

Suppose $f, g \in \L^1(X \to \C, \mu)$. Then

- $\mu (f + g) = \mu f + \mu g$ and $f + g \in \L^1(\mu)$.
- $\mu (cf) = c \mu f$ and $cf \in \overline \L(\mu)$ for any $c \in \C$.
- $\overline {\mu f} = \mu \overline f$.
- $|\mu f| = e^{i\theta} \mu f = \mu (e^{i \theta} f) = \mu (\re e^{i \theta}f) \le \mu |e^{i\theta}f| = \mu |f|$.
- $\mu f = \mu g$ if $f = g$ $\mu$-a.e.
- $\mu |f + g| \le \mu |f| + \mu |g|$.

#### Change of Variable

(**Change of variable in integral**)

Suppose $(X, \mathcal B, \mu)$ and $(Y, \mathcal C)$ are measurable spaces.

Suppose $\phi \in \L(X \to Y, \mathcal B / \mathcal C)$. Then $(Y, \mathcal C, \phi_* \mu)$ is a measure space.

- Recall that $\phi_* \mu$ is the push-forward measure. $\phi_*\mu = \mu \circ \phi^{-1}$.

Suppose $f \in \L(Y \to [0, \infty], \mathcal C)$, then $\mu(f \circ \phi) = (\mu\circ \phi^{-1})(f)$, or
$$
\int_X f(\phi(x)) \dd \mu(x) = \int_Y f(y) \dd \phi_* \mu(y) \quad (*)
$$

- Suppose $f = 1_B$. Then $\mu (1_B \circ \phi) = \mu(1_{\phi^{-1}B}) = \mu(\phi^{-1}B) = (\mu\circ \phi^{-1})(1_B)$.
- Suppose $f \in S(Y \to [0, \infty], \mathcal C)$. Then $(*)$ is true by linearity.
- Suppose $f \in \L(Y \to [0, \infty], \mathcal C)$. Some $(f_k)_{k  = 1}^\infty \in S(Y \to [0, \infty], \mathcal C)$ where $f_k \uparrow f$.
    - $f_k \circ \phi \uparrow f \circ \phi$, so $\mu(f_k \circ \phi) \uparrow \mu(f \circ \phi)$.
    - $f_k \uparrow f$, so $(\mu \circ \phi^{-1}) f_k \uparrow (\mu \circ \phi^{-1}) f$.

The codomain of $f$ in the theorem can be extended to $\R, \eR$ and $\C$.

(**Change of variable in Lebesgue integral**) ==TODO==

> When $\mu$ is the Lebesgue measure, and $\phi$ is a $C^1$-diffeomorphism. We can give $\phi_* \mu$ analytically.
>
> This is a rather advanced result. See the following pages:
>
> - [PlanetMath](https://www.planetmath.org/changeofvariablesinintegralonmathbbrn) page on change of variable.
> - [Math StackExchange](https://math.stackexchange.com/questions/1595387/dropping-injectivity-from-multivariable-change-of-variables) question on multiple change of variables.

Suppose $\phi: X \to Y$ on open subsets $X, Y \subseteq \R^d$.

Suppose $\phi$ is a $C^1$-diffeomorphism, $\phi \in C^1[X]$ and $\phi^{-1} \in C^1[Y]$.

Further suppose $\abs{\det D \phi(x)} > 0$ on $X$. For $f \in \L(Y \to [0, \infty])$:
$$
\int_X f(\phi(x)) dx = \int_{Y} \frac{f(y)}{\abs{\det D\phi(x)}} dy \iff \int_X f(\phi(x)) \abs{\det D\phi(x)} \dd x = \int_Y f(y) \dd y
$$

The theorem remains true for codomain $\R, \eR$ and $\C$.

(**Push-forward of density with respect to Lebesgue measure**)

Suppose $\phi: X \to Y$ on open subsets $X, Y \subseteq \R^d$.

Suppose $\phi$ is a $C^1$-diffeomorphism. And $\abs{\det D \phi(x)} \neq 0$.

Suppose measure $\mu$ has density $f: X \to [0, \infty]$ with respect to the Lebesgue measure.

Suppose $B \subseteq Y$, then
$$
\mu(\phi^{-1}[B])= \int_{\phi^{-1}[B]} f(x) \dd x = \int_B \frac{f(\phi^{-1}(y))}{\abs{\det D\phi(x)}} \dd y = \phi_* \mu (B)
$$
Therefore $\phi_* \mu$ has density $\phi_* f: Y \to [0, \infty]$ with respect to Lebesgue measure.


(**Refinement invariant**)

Suppose $(X, \M, \mu)$ and $(X, \M', \mu')$ are measure spaces. And $\mu'$ extends $\mu$ from $\M$ to $\M'$.

Then $f \in \L(X \to [0, \infty], \M)$ implies $f \in \L(X \to [0, \infty], \M')$. And $\mu f = \mu' f$.

#### Riemann Integral

(**Lebesgue Integral**)

Suppose $f \in \L(\R^d \to [0, \infty], \L(\R^d))$. $\lambda_{d} (f)$, the integral with respect to the lebesgue measure, is the Lebesgue integral.

Often denoted as following:
$$
\lambda_d(f) = \int_{\R^d} f(x) \dd x
$$
(**Step functions on $\R^d$**)

$f: \R^d \to F$ is called a **step function** if $f$ can be written as $f = \sum_{i=1}^n c_i 1_{A_i}$. Where $c_i \in F$ and $A_i \in \S_d$.

Denote the set of all step functions as $\square(\R^d \to F)$. Where $F$ can be $[0, \infty]$, $\R$, $\eR$ and $\C$.

(**Riemann Integral**)

Suppose $f: \R^d \to \R$, the lower and upper Riemann integral are defined as:

$$
\underline I(f) := \underline{\int_{\R^d}} f(x) \dd x:=\sup _{g \leq f, g \in \square(\R^d \to \R)}\int_{\R^d} g(x) \dd x;\quad
\overline I(f):=\overline{\int_{\R^d}} f(x) \dd x:=\inf _{g \geq f, g \in \square(\R^d \to \R)}\int_{\R^d} g(x) \dd x
$$
Suppose $\underline I(f) = \overline I(f)$, $f$ is **Riemann integrable**.

If $f(x)$ is Riemann integrable, $f$ must have **bounded support and range**.

Suppose $\overline{\su f} = B \subseteq \R^d$. The following are equivalent:

- $f(x)$ is Riemann integrable.
- The set $G_f = \{(x, f(x)): x \in B\} \subset \R^{d+1}$ is a Jordan null set.
- The area under graph $A_f = \{(x, t): x \in B ; 0 \le t < f(x)\} \subset \R^{d+1}$ is Jordan measurable.
  - $m(A_f) = \int f(x) \dd x$.

(**Lebesgue Integral and Riemann Integral**)

Suppose $f: \R^d \to [0, \infty]$ is Riemann integrable. Suppose $S$ is a compact support of $f$.

Then $f \in \L(\R^d \to [0, \infty), \L(\R^d))$ and the Lebesgue integral is the same as the Riemann integral.

- Suppose $A_f \subseteq \R^{d + 1}$ is the area under the graph for $f$.
- Clearly $A_f \in \J(\R^{d + 1}) \subseteq \L(\R^{d + 1})$.
