#### Meromorphic Functions

##### Extended complex and Riemann sphere

> Read this [wiki](https://en.wikipedia.org/wiki/Riemann_sphere) page on Riemann sphere.

Define $\eC:= \C \cup \c\infty$. Where $\infty$ is a new symbol.

The operations on field $\C$ are partially extended in following ways:

- Addition: $\forall z \in \C: z + \infty = \infty$.
- Multiplication: $\forall z \in \C^*: z \times \infty = \infty$. $\infty \times \infty = \infty$.
- Multiplicative inverse: $1/ 0 = \infty$ and $1 / \infty = 0$.

##### Stereographic projection

Consider $\bS$ the unit sphere in $\R^3$. Identify $\R^3 \simeq \R^2 \times \R \simeq \C \times \R$.

For each $z \in \C$, consider the line through $(c, 0)$ and $(0, 1)$.

- The line intersects the sphere only at $p(c)$ and $(0, 1)$.
- Clearly $p: \C \to \bS$ is an injection.

By defining $p(\infty) := (0, 1)$, $p: \eC \to \bS$ is a **homeomorphism**, called the **stereographic projection** of $\C$ onto $\bS$.

- We can give the coordinate of the map:
  $$
  p(x + iy) = p(z) = \p{\frac{2x}{1 + \abs{z}^2}, \frac{2y}{1 + \abs{z}^2}, \frac{\abs{z}^2 - 1}{1 + \abs{z}^2}} \in \bS
  $$

- Lines and circles in $\C$ are mapped to circles on $\bS$.

  - Circles on $\bS$ are intersections of planes with $\bS$.
    $$
    (A, B, C)^T p(z) = D \implies (C - D) (x^2 + y^2) + 2Ax + 2By - C - D = 0
    $$

  - Apparently, lines in $\C$ are mapped to circles on $\bS$ containing the pole $(0, 1)$.

  - Circles in $\C$ are mapped to circles on $\bS$ not containing the pole $(0, 1)$.

Consider the map $r: \eC \to \eC$ where $z \mapsto 1/z$ and $r(\infty) = 0$.

- The map on sphere $\bS$ is $(x, y, z) \mapsto (x, -y, -z)$.

##### Singularities at infinity

Suppose $f$ is holomorphic in some neighborhood of $\infty$.

Define $g(z) = f(1 / z)$, then $g$ is holomorphic some neighborhood of $0$.

- $f$ has a pole at $\infty$ if $g$ has a pole at $0$.
- $f$ has a removable singularity at $\infty$ if $g$ has a removable singularity at $0$.
- $f$ has an essential singularity at $\infty$ if $g$ has a ... at $0$.

##### Meromorphic

Suppose $\Omega\subseteq \C$ is an open set.

Let $R$ be an at most countable subset of $\Omega$. And $R' = \varnothing$.

$f$ is called **meromorphic** on $\Omega$ if $f$ is holomorphic on $\Omega - R$, and $R$ contains poles of $f$.

##### Meromorphic on $\eC$

$f: \C \to \eC$ is meromorphic on $\eC$ it is meromorphic on $\C$, and $f$ has either a removable singularity or a pole at $\infty$.

##### Rational functions are meromorphic on $\eC$

Consider $p(z) \in \C(z)$. Suppose $p(z) = f(z) / g(z)$ where $f, g \in \C[z]$.

Then $p(z)$ is meromorphic with finitely many poles.

- Suppose $\deg f > \deg g$, and $d = \deg f - \deg g$.
  - $f$ has pole of order $d$ at $\infty$.
- Suppose $\deg f = \deg g$.
  - $f$ has removable singularity at $\infty$.
- Suppose $\deg f < \deg g$ and $d = \deg g - \deg f$.
  - $f$ has zero of order $d$ at $\infty$.

Rational functions have finitely many poles, and holomorphic otherwise.

##### Meromorphic functions on $\eC$ are rational functions

Suppose $f: \C \to \eC$ is meromorphic.

$f$ can only have finitely many poles.

- Suppose $f$ has countably infinitely many poles. These poles on $\bS$ must have a limit point.
- The limit point can only be $(0, 1)$. Otherwise there are converging poles in $\C$.
- But $f$ is meromorphic, so there can be no limit point at all.

Suppose $p_1, \ldots, p_n$ are the poles in $\C$, and $\infty$ is possibly a pole.

- Near pole $p_k$, for some $g_k \in \C[z]$, and holomorphic $h_k(z)$.
  $$
  f(z) = g_k\p{\frac{1}{z - p_k}} + h_k(z)
  $$
  
- For possibly a pole $\infty$, consider $f(1/z)$. Near zero we have:
  $$
  f\p{\frac{1}{z}} = g_\infty\p{\frac{1}{z}} + h_\infty(z)
  $$

- Now consider $F: \C \to \C$ defined as
  $$
  F(z):= f(z) - g_\infty(z) - \sum_{k=1}^n g_k\p{\frac{1}{z - p_k}}
  $$

- Apparently $F(z)$ is holomorphic on $\C$ therefore **entire**. $F(z)$ is also bounded.

- Therefore $F(z)$ is constant on $\C$.

#### Open Mapping Theorem

##### Argument principle

Suppose $\Omega$ is a region. And $f: \Omega \to \C$ is meromorphic on $\Omega$.

Suppose $D = B(z_0, r_0)$ and $\overline D \subseteq \Omega$. Denote $C = \part D$. Then
$$
\frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)} \dd z = \#_{\text{zeros in }D} - \#_{\text{poles in }D}
$$
Where each zero and pole are counted their order times. And there are no poles on $C$.

- Suppose $D$ contains only a zero of order $n$ at $c$.

  - Then near $c$, we have
    $$
    f(z) = (z - c)^n g(z)
    $$

  - $g(z)$ is nonzero near $c$. So near $c$ we have:
    $$
    f'(z) = n(z - c)^{n - 1} g(z) + (z - c)^n g'(z)
    $$

  - By a keyhole contour integral, we have
    $$
    \frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)} \dd z = \frac{1}{2\pi i} \oint_C\frac{n}{z - c} + \frac{g'(z)}{g(z)} \dd z = n
    $$

- Suppose $D$ contains only a pole of order $n$ at $c$.

  - Then near $c$, we have
    $$
    f(z) = (z - c)^{-n} g(z)
    $$

  - $g(z)$ is nonzero near $c$. So near $c$ we have:
    $$
    f'(z) = -n(z - c)^{-(n + 1)} g(z) + (z - c)^{-n} g'(z)
    $$

  - By a keyhole contour integral, we have
    $$
    \frac{1}{2\pi i} \oint_C \frac{f'(z)}{f(z)} \dd z = \frac{1}{2\pi i} \oint_C\frac{-n}{z - c} + \frac{g'(z)}{g(z)} \dd z = -n
    $$

- For the case of multiple poles and zeros, consider a contour with multiple keyholes.

##### Rouche theorem

Suppose $f, g: \Omega \to \C$ are holomorphic on region $\Omega$.

Suppose $D = B(z_0, r_0)$ and $\overline D \subseteq \Omega$. Denote $C = \part D$.

Then if $\forall z \in C: \abs{f(z)} > \abs{g(z)}$. $f$ and $f + g$ have the same number of zeros in $D$.

- For $t \in [0, 1]$, define $f_t(z) = f(z) + tg(z)$.

- The $\abs{f_t(z)} \ge \abs{f(z)} - t\abs{g(z)} > 0$.

- With argument principle, the number of zeros in $D$ changes continuously in $t$. Therefore must be constant.
  $$
  \frac{1}{2\pi i} \oint_C \frac{f_t'(z)}{f_t(z)} \dd z = \#_{\text{zeros in }D}
  $$

##### Open mapping theorem

Suppose $f$ is holomorphic and non-constant on region $\Omega$, $f$ is an **open mapping**.

- We only need to show that $f[\Omega]$ is open in $\C$.
- Suppose $w_0 \in f[\Omega]$, where $f(z_0) = w_0$. And $w \in B(w_0, r_0)$.
- We only need to show that $f(z) - w$ has a zero in $\Omega$.
- We hope to proceed with Rouche theorem here.
  - There exists $\delta > 0$ where $\overline{B(z_0, \delta)} \subseteq \Omega$, and $w_0 \notin f[\overline{B(z_0, \delta)}]$.
    - Otherwise construct a sequence of points where $f$ is constant.
    - Denote the circle $C_\delta = \part B(z_0, \delta)$, and disk $D = B(z_0, \delta)$.
  - There exists $\epsilon > 0$ where $\forall z \in C_\delta: \abs{f(z) - w_0} \ge \epsilon$.
  - Consider $F(z) = f(z) - w_0$ and $G(z) = w_0 - w$. $f(z) - w = F(z) + G(z)$.
    - $F(z)$ has one zero in $D$.
    - $\abs{F(z)} > \abs{G(z)}$ on $C$ if we take $w \in B(w_0, \epsilon / 2)$.
  - Rouche theorem says that $f(z) - w$  has exactly one zero inside $D$ as well.

##### Maximum modulus principle

Suppose $f$ is holomorphic and non-constant on region $\Omega$, $\abs{f}$ cannot attain a maximum on $\Omega$.

- This immediately follows from the open mapping theorem.

