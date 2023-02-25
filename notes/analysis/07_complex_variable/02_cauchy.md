#### Contour Integrals

##### Contour integral

Suppose $\gamma: [a, b] \to \C$ is a **smooth path**.

Suppose $f: S \subseteq \C \to \C$ is defined on $\gamma [a, b]$.

The contour integral of $f$ along $\gamma$, denoted by $\int_{\gamma} f$, is defined by the equation
$$
\int_{\gamma} f(z) d z =\int_{\gamma(a)}^{\gamma(b)} f(z) d z = \int_{\gamma} f :=\int_{a}^{b} f[\gamma(t)] \gamma'(t) d t
$$
whenever the **Lebesgue integral** on the right exists.

- (**Linearity**) If the integrals $\int_{\gamma} f$ and $\int_{\gamma} g$ exist, then the integral $\int_{\gamma}(\alpha f+\beta g)$ exists for every pair of complex numbers $\alpha, \beta$, and we have
  $$
  \int_{\gamma}(\alpha f+\beta g)=\alpha \int_{\gamma} f+\beta \int_{\nu} g
  $$

- Let $\gamma_{1}$ and $\gamma_{2}$ denote the restrictions of $\gamma$ to $[a, c]$ and $[c, b]$, respectively, where $a<c<b$. If the right hand side exists:
  $$
  \int_{\gamma} f=\int_{\gamma_{1}} f+\int_{\gamma_{2}} f
  $$

- Let $\gamma$ be a rectifiable path of length $\Lambda(\gamma) .$ If the integral $\int_{\gamma} f$ exists and if $|f(z)| \leq M$ for all $z$ on the graph of $\gamma$, then we have the inequality
  $$
  \left|\int_{\gamma} f\right| \leq M \Lambda(\gamma)
  $$

- Let $\gamma$ be a **piecewise smooth path** with domain $[a, b]$. If the contour integral $\int_{\gamma} f$ exists, we have
  $$
  \int_{\gamma} f=\int_{a}^{b} f[\gamma(t)] \gamma^{\prime}(t) d t
  $$

- (**Integral on equivalent paths**)

  - Let $\gamma$ and $\delta$ be equivalent paths describing the same curve $\Gamma$.

  - If $\int_{\gamma} f$ exists, then $\int_{\delta} f$ also exists. Moreover, we have $\int_{\gamma} f=\int_{\delta} f$.

  - Suppose $\delta(t)=\gamma[u(t)]$ where $u$ is strictly increasing on $[c, d]$.
    $$
    \int_{u(c)}^{u(d)} f[\gamma(t)] d \gamma(t)=\int_{c}^{d} f[\delta(t)] d \delta(t)=\int_{\delta} f
    $$
    
  - This allows us to ignore some details in curve parameterization.

##### Cauchy's Lemma

Suppose $f: \Omega \to \C$ where $\Omega$ is a **region**. $f$ is **continuous and has primitive $F$ on $\Omega$**.

Suppose $\gamma: [a, b] \to \Omega$ is a **smooth path**, then:
$$
\int_{\gamma} f(z) \dd z = \int_{a}^b f(\gamma(t))\gamma'(t) \dd t = \int_a^b D_t[F(\gamma(t))] \dd t = F(\gamma(b)) - F(\gamma(a))
$$
Clearly the theorem also works for piecewise smooth paths.

Suppose $\gamma$ is a closed smooth path, then $\int_\gamma f(z) \dd z = 0$.

##### Goursat's theorem

Define $\triangle_{abc}$ as the **compact triangle** with $a, b, c\in \C$ as vertices.

- With $a, b, c$ in counter-clockwise order.
- Denote the boundary as $\part\triangle_{abc}$.
- Let $d_0$ be the longest edge length.

Suppose $\Omega$ is a region in $\C$. And $\triangle_{abc}^\circ \subseteq \Omega$. Suppose $\phi(z)$ is holomorphic on $\triangle_{abc}$. Then
$$
\int_{\triangle_{abc}} \phi(z) \dd z = 0
$$

- Let $d = (a + b) / 2$, $e = (b + c) / 2$ and $f = (c + a) / 2$.

- Note the following:
  $$
  \int_{\triangle_{abc}} \phi(z) \dd z = \p{\int_{\triangle_{adf}} + \int_{\triangle_{dbe}} + \int_{\triangle_{fec}} + \int_{\triangle_{edf}}} \phi(z) \dd z
  $$

- Therefore we have estimate by integrating on a smaller triangle,
  $$
  \abs{\int_{\triangle_{abc}}\phi(z) \dd z} \le 4 \abs{\max\c{{\int_{\triangle_{adf}},  \int_{\triangle_{dbe}},\int_{\triangle_{fec}} ,\int_{\triangle_{edf}}} \phi(z) \dd z}}
  $$

- Now repeat this process iteratively. We form a decreasing compact triangle chain $\p{\triangle_{n}}_{n=0}^\infty$, where $\triangle_0 = \triangle_{abc}$.

- Suppose $z_0 = \cap_{n} \triangle_n$. And $\phi(z) = \phi(z_0) + \phi'(z_0)(z - z_0) + h(z)(z - z_0))$ where $\lim_{z \to z_0} h(z) = 0$.

- For any $\epsilon > 0$, there exists some $B(z_0, r_\epsilon)$ where $\abs{h(z)} < \epsilon$.

- For some $N > 0$, for all $n > N$, $\triangle_n \subseteq B(z_0, r_\epsilon)$.
  $$
  \begin{aligned}
  \abs{\int_{\triangle_{abc}}\phi(z) \dd z} &\le 4^n \abs{\int_{\triangle_n} \phi(z_0) + \phi'(z_0)(z - z_0) + h(z)(z - z_0) \dd z}\\
  & = 4^n \abs{\int_{\triangle_n} h(z) (z - z_0) \dd z} \le 4^n \abs{\sup_{z \in \triangle_n} h(z) }\abs{2^{-n} d_0} \abs{2^{-n} p_0} \le 3 \epsilon d_0^2
  \end{aligned}
  $$

##### Cauchy's theorem: on a disk

A holomorphic function $f: \Omega \to \C$ in an **open ball** has a primitive in that ball.

- w.l.o.g. assume the open ball is $D = B(0, 1)$.

- For $z \in D$, 

- Define $F(z): D\to \C$ as
  $$
  F(z) = \int_{0}^{\Re z} f(s) \dd s + \int_{\Re z}^{z} f(s) \dd s
  $$

- Now consider $F(z + h) - F(z)$, by drawing a diagram, we can show that:
  $$
  F(z + h) - F(z) = \int_{z}^{z + h} f(s) \dd s = \int_{z}^{z + h} f(z) + f'(z)(s - z) + \varphi(s)(s - z) \dd s
  $$

- Observe that
  $$
  \frac{F(z + h) - F(z)}{h} = f(z) + \frac{f'(z)}{2} h + \int_{z}^{z + h} \varphi(s) (s - z) \dd s
  $$

- Therefore $F(z)$ a primitive of $f(z)$ in $\Omega$.

#### Homotopy and Cauchy's Theorem

##### Homotopy

Let $\gamma_{0}$ and $\gamma_{1}$ be two paths in $\C$ with a common domain $[a, b]$.

Where $\gamma_{0}$ and $\gamma_{1}$ have the same endpoints: $\gamma_{0}(a)=\gamma_{1}(a)$ and $\gamma_{0}(b)=\gamma_{1}(b)$.

Let $\Omega$ be a subset of $\C$ containing the graphs of $\gamma_{0}$ and $\gamma_{1}$.

Then $\gamma_{0}$ and $\gamma_{1}$ are said to be **homotopic** in $\Omega$ if there exists a function $h: [0, 1] \times [a, b] \to \Omega$, 

- $h$ is continuous on $[0, 1] \times [a ,b]$.
- $h(0, t)=\gamma_{0}(t)$ and $h(1, t)=\gamma_{1}(t)$.
- For all $s \in [0, 1]$. $h(s, a)=\gamma_{0}(a)$ and $h(s, b)=\gamma_{0}(b)$.

##### Simply connected

A region $\Omega$ is **simply connected** if any two pair of curves in $\Omega$ with the same end-points are homotopic in $\Omega$.

##### Linear homotopy

Let $\gamma_{0}$ and $\gamma_{1}$ be two paths in $\C$ with a common domain $[a, b]$.

If, for each $t$ in $[a, b]$, the line segment joining $\gamma_{0}(t)$ and $\gamma_{1}(t)$ lies in $D$.

Then $\gamma_{0}$ and $\gamma_{1}$ are homotopic in $D$ as we have
$$
h(s, t)=s \gamma_{1}(t)+(1-s) \gamma_{0}(t)
$$

Clearly **convex regions are simply connected**.

##### Homotopic integral lemma

Suppose $\Omega$ is a region in $\C$. And $f$ is holomorphic on $\Omega$.

If $\gamma_{0}$ and $\gamma_{1}$ are **piecewise smooth paths** which are **homotopic** in $\Omega$. Then
$$
\int_{\gamma_{0}} f(z) dz=\int_{\gamma_{1}} f(z) dz
$$

- Without loss of generality, suppose $\gamma_0$ and $\gamma_1$ are **smooth**.
- Since $\gamma_0$ and $\gamma_1$ are homotopic, there exists continuous $H: [0, 1] \times [a, b] \to \C$.
  - Where $H(0, t) = \gamma_0(t)$ and $H(1, t) = \gamma_1(t)$.
  - Let $K$ be the compact image of $H$ in $\C$.
  - Let $\epsilon = \dist(K, \Omega^c) / 3 > 0$.
  - Since $H$ is uniformly continuous, there exists $\delta > 0$ such that for $h \in B(0, \delta)$, $\abs{H(z_0 + h) - H(z_0)} < \epsilon$.
- Now consider any curve $\gamma_s$ and $\gamma_t$ where $s < t < s + \delta$. We can show that $\int_{\gamma_s} f(z) \dd z = \int_{\gamma_t} f(z) \dd z$.
  - There exists a partition of $[a, b]$ with norm less than $\delta$, $a = w_0 < \cdots < w_n = b$.
  - Consider points $c_k := \gamma_s(w_k)c_k := \gamma_s(w_k)$ for $k \ge 0$.
  - Consider open ball sequence $B_k := B(c_k, 2\epsilon) \subseteq \Omega$.
  - Consider the curve pair $\gamma_s[w_k, w_{k + 1}], \gamma_t[w_k, w_{k+1}]$. Each pair is completely covered by an open ball.
  - Therefore, for each pair, we can use **Cauchy's theorem in a disk**.

##### Cauchy's theorem: on simply connected regions

A holomorphic function $f: \Omega \to \C$ in an **simply connected region** has a primitive on $\Omega$.

- Define $F(z): \Omega\to \C$ as
  $$
  F(z) = \int_\gamma f(z)\dd z
  $$

- Homotopic integral lemma guarantees that $F(z)$ is well defined.

- The process showing $F'(z) = f(z)$ is the same as in the disk case.

#### Cauchy's Integral Formula

##### Cauchy's integral formula

Suppose $\Omega \subseteq \C$ is a region. And $f: \Omega \to \C$ is holomorphic on $\Omega$.

Suppose $D = {B(z_0, r_0)}$ and $\overline D \subseteq \Omega$. Denote $C = \part D$. Then
$$
\forall z \in D: D^n f(z) = \frac{n!}{2\pi i} \oint_{C} \frac{f(s)}{(s - z)^{n + 1}} \dd s; \quad f(z) = \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - z} \dd s
$$

For $n = 0$, Take the "**keyhole**" contour, there are four parts, inner circle, outer circle, and two corridors.

- Let $\epsilon, r$ be the radius of the inner circle $C_\epsilon$ and outer circle $C_r$.

- Let $\delta$ be the width of the corridor $C_\delta$.

- Notice that
  $$
  \frac{f(s)}{s - z} = \frac{f(s) - f(z)}{s - z} + \frac{f(z)}{s - z}
  $$

- Consider $C_\epsilon$ as $\epsilon \to 0$.
  $$
  \int_{C_\epsilon} \frac{f(s)}{s - z} \dd s \to \int_{C_\epsilon} f'(z) + \frac{f(z)}{s - z} \dd s \to f(z) \int_{C_\epsilon}\frac{1}{s - z} \dd s = f(z) (2\pi i)
  $$

- Therefore $n = 0$ is proved.
  $$
  f(z) = \frac{1}{2\pi i} \oint_C \frac{f(s)}{(s - z)} \dd s
  $$

For $n \ge 1$, we proceed with induction.

- Suppose $n - 1$ is true, consider case $n$.
  $$
  \lim_{h \to 0}\frac{f^{(n-1)}(z+h)-f^{(n-1)}(z)}{h} = \lim_{h \to 0}\frac{(n - 1)!}{2\pi i} \int_C f(s)\frac{\s{\p{s - (z + h)}^{-n} - \p{s - z}^{-n}}}{h}  \dd s
  $$

- Consider function $g(s, h)$:
  $$
  g(s, h) := \frac{\s{\p{s - (z + h)}^{-n} - \p{s - z}^{-n}}}{h}
  $$

  - $g(s, h)$ is (uniformly) continuous on $A[z_0, r_0 - \epsilon, r_0 + \epsilon] \times [-\epsilon, \epsilon]$ for $\epsilon$ small enough.
  - So $f(s) g(s, h)$ is uniformly continuous as well.

- Therefore, swapping limit and integration is legal, and a derivative gives the desired result.

##### Cauchy's integral estimate

Suppose $\Omega \subseteq \C$ is a region. And $f: \Omega \to \C$ is holomorphic on $\Omega$.

Suppose $D = {B(z_0, R)}$ and $\overline D \subseteq \Omega$. Denote $C = \part D$. Then
$$
\abs{D^n f(z_0)} \le \frac{n! \sup_{z \in C} \abs{f(z)}}{R^n}
$$

- The result immediately follows from the Cauchy's integral formula.

##### Lemma: power series expansion of $1/(1-z)$

- For $z \in B(0, 1)$ we have ${1}/\p{1 - z} = \sum_{n=0}^\infty z^n$.
- For $z \in A(0; 1, \infty)$ we have $z / (z - 1) = \sum_{n=0}^\infty z^{-n}$.
  - Hint: transform by taking $z \mapsto 1/z$.
- For $z \in A(0; 1, \infty)$ we have $1/(1-z) = \sum_{n=1}^\infty -z^{-n}$.

##### Holomorphic implies analytic

> Reference: wikipedia [page](https://en.wikipedia.org/wiki/Analyticity_of_holomorphic_functions) on Analyticity of holomorphic functions.

Suppose $f: \Omega \to \C$ is **holomorphic** on region $\Omega$.

If $D = B(z_0, r_0)$ where $\overline D \subseteq \Omega$, and $C = \part D$, then $f$ is **analytic** at $z_0$.
$$
\forall z \in B(z_0, r_0): f(z) = \sum_{n = 0}^\infty a_n \p{z - z_0}^n;\quad a_n = \frac{f^{(n)}(z_0)}{n!}
$$

- For $z \in D$ we have:
  $$
  \begin{aligned}
  f(z) & = \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - z} \dd s = \frac{1}{2\pi i} \oint_C f(s)\frac{1}{s - z_0 + z_0 - z} \dd s = \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - z_0} \cdot \frac{1}{1 - \frac{z - z_0}{s - z_0}} \dd s\\
  & = \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - z_0} \cdot \sum_{n=0}^\infty \p{\frac{z - z_0}{s - z_0}}^n \dd s = \sum_{n=0}^\infty \s{\frac{1}{2\pi i} \oint_{C} \frac{f(s)}{(s - z_0)^{n + 1}} \dd s} (z - a)^n
  \end{aligned}
  $$

- The series converges uniformly over $C$, therefore the sum and the integral can be exchanged.

If $D = A(z_0; r_0, \infty)$ where $\overline D \subseteq \Omega$, and $C = \part D$ (clockwise), then $f$ is outer analytic at $z_0$.
$$
\forall z \in A(z_0; r_0, \infty): f(z) = \sum_{n=0}^\infty a_{n} (z - z_0)^{-n}
$$

- For $z \in D$ we have:
  $$
  \begin{aligned}
  f(z) & = \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - z} \dd s =  \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - z_0} \cdot \frac{1}{1 - \frac{z - z_0}{s - z_0}} \dd s \\
  & = \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - z_0} \cdot \sum_{n=1}^\infty -\p{\frac{z - z_0}{s - z_0}}^{-n} \\
  & = \sum_{n=1}^\infty \s{-\frac{1}{2\pi i} \oint_C f(s)(s-z_0)^{n-1}}(z-z_0)^{-n}
  \end{aligned}
  $$

##### Liouville's theorem

Suppose $f: \C \to \C$ is entire (holomorphic on $\C$) and bounded, then $f$ is constant.

- To show $f$ is constant, we only need to show that $f'(z)$ is zero everywhere.
- Notice that $\abs{f'(z_0)} \le \sup_{z \in C} \abs{f(z)} / R$, now let $R \to \infty$.

##### Fundamental theorem of algebra

Suppose $p(z) \in \C[z]$ is non-constant. Then $p$ has one zero in $\C$.

- Suppose $p$ has no zeros. Then $1 / p$ is an analytic function on $\C$.
- Furthermore, $|p(z)| \rightarrow \infty$ as $|z| \rightarrow \infty$, which implies that $1 / p \rightarrow 0$ as $|z| \rightarrow \infty$.
- Thus $1 / p$ is a bounded analytic function on $\C$.
- By Liouville's theorem, every such function is constant.
- But if $1 / p$ is constant, then $p$ is constant, contradicting our assumption that $p$ is nonconstant.

##### Zero function test

Suppose $f: \Omega \subseteq \C \to \C$ is holomorphic on region $\Omega$.

Suppose $\p{z_n} \subseteq \Omega$ are distinct values with a limit point in $\Omega$, and $\forall n \ge 1: f(z_n) = 0$. Then $f[\Omega] = \c{0}$.

- Suppose $c$ is a limit point of $\p{z_n}$.
- Suppose $f$ is analytic at $c$, converge in $B(c, r_0)$. Then $f[B(c, r_0)] = \c{0}$.
  - Suppose $f(a) \neq 0$ for $a \in B(c, r_0)$, some power series coefficients must not be zero.
  - The set $\c{(z - c)^n: n \in \N}$ is linearly independent.
  - $r_0$ can take any value where $\overline{B(c, r_0)} \subseteq \Omega$.
- Consider any point $b \in \Omega$.
  - Since $\Omega$ is connected, there is a compact curve $\Gamma$ joining $b$ and $c$.
  - There exists a finite open cover of $\Gamma$ lying in $\Omega$.
  - Now transmit the zero property through the finite open cover.

