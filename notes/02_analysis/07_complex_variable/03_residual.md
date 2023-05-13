#### Residual Theorem

##### Removable singularity

Suppose $f: \Omega \subseteq \C \to \C$.

Suppose $f$ is holomorphic on some $U(c, r)$ but not at $c$. $c$ is a **singularity** of $f$.

If $f \cup \c{(c, f(c))}$ is holomorphic on $B(c, r)$ it is a **removable singularity**.

##### Zeros and poles

Suppose $f: \Omega \subseteq \C \to \C$ is holomorphic on region $\Omega$.

Suppose $f(c) = 0$ for some $c \in \Omega$.

- $c$ is a **zero** of $f$.
- If $f$ is not constantly zero, $c$ must be **isolated** from other zeros of $f$.
- Since $f$ is analytic at $c$, $f(z) = \sum_{n=0}^\infty a_n (z-c)^n$ in some $B(c, r)$.
- There exists a maximal integer $d \in \N^+$ where $a_{<d} = 0$ and $a_d \neq 0$.
  - $d$ is called the **order** of zero $c$.
  - For $d = 1$, $c$ is a simple zero.
- $f(z) = (z-c)^d \sum_{n=0}^\infty a_{n+d}(z - c)^n = (z - c)^d h(z)$.
  - Where $h(z) := \sum_{n=0}^\infty a_{n + d} (z - c)^n$, convergent in $B(c, r)$.
  - $h(z)$ is non-zero in some neighborhood of $c$.


Suppose $U(c, r_0) \subseteq \Omega$ for $c \notin \Omega$. And $g(z) := 1/f(z) \cup \c{(c, 0)}$ is holomorphic in $B(c, r_0)$.

- $c$ is a **pole** of $f$.
- The order of $c$ as a zero of $g$ is the **order** of the pole of $f$.
  - For $d = 1$, $c$ is a simple pole.
- Suppose $g(z) = (z - c)^d h(z)$. We can write $f(z) = (z - c)^{-d} /h(z)$.
  - Recall that $1/h(z)$ is analytic at $c$ as well since $h(c) \neq 0$.
- Therefore $f(z)$ can be expressed as following in some neighborhood of $c$.
  $$
  f(z) = \frac{b_{-d}}{(z - c)^{d}} + \cdots + \frac{b_{-1}}{(z - c)} + \sum_{n=0}^\infty b_n (z - c)^n
  $$
- The **residual** of $f$ at pole $c$ is $\res_{c} f := b_{-1}$.
- The residual of $f$ at pole $c$ can be computed as following:
  $$
  \res_{c} f = \lim_{z \to z_0} \frac{1}{(d - 1)!}D_{z}^{d - 1}\s{(z  - c)^d f(z)}
  $$
  - We are writing the limit as the inside is not defined as $z = z_0$.
  - The limit is guaranteed to exist as $1/h(z)$ is continuous.

##### Integral around poles

Consider entire function $f(z) = 1$. According to Cauchy's integral formula:
$$
f^{(n)}(0) = 1(n = 0) = \oint_{C} \frac{1}{s^{n+1}} \dd s
$$
Where $C$ is any circle around $0$.

##### The residual formula

Suppose $f$ is holomorphic on region $\Omega$, except at one **pole** $c \in \Omega$ with order $d$.

Suppose $D = B(z_0, r_0) \ni c$ and $\overline D \subseteq \Omega$. Then
$$
(2\pi i)\res_{c} f =  \oint_C f(z) \dd z
$$

- Recall the keyhole contour argument. We can integral around smaller circle around the pole. Make the circle **small** enough where the following expansion is possible
  $$
  f(z) = \frac{b_{-d}}{(z - c)^{d}} + \cdots + \frac{b_{-1}}{(z - c)} + \sum_{n=0}^\infty b_n (z - c)^n
  $$
- Notice that except for $b_{-1} / (z - c)$ all other terms vanishes during integration.

Clearly the theorem can be generalized to other simple contours and multiple poles:
$$
2\pi i \sum_{i=1}^N \res_{c_i} f = \oint_{C} f(z) \dd z
$$

#### Riemann Theorem

##### Morera theorem

Suppose $f: D \subseteq \C \to \C$ is continuous on open disk $D = B(z_0, r_0)$.

Suppose for all $\triangle_{abc} \subseteq D$, we have $\int_{\triangle_{abc}} f(z) \dd z = 0$. Then $f$ is holomorphic on $D$.
- Define $F(z): \int_{z_0}^z f(s) \dd s$. And notice:
  $$
  \frac{F(z + h) - F(z)}{h} = \frac{1}{h}\int_{z}^{z + h} f(s) \dd s \to f(z)
  $$
- Therefore $F(z)$ is holomorphic on $D$.
- Note that the assumption can be relaxed.

##### Limit of holomorphic uniform convergent sequence

Suppose $\Omega \subseteq \C$ is a region. Suppose $f, \p{f_n} :\Omega \to \C$ are holomorphic.

Suppose $f_n$ converge to $f$ uniformly in any compact subset of $\Omega$.

Then $f$ is holomorphic on $\Omega$.

- Suppose $D = B(z_0, r_0)$ and $\overline D \subseteq \Omega$.
- For any triangle $\triangle_{abc} \subseteq D$, notice that
  $$
  \lim_{n \to \infty}\int_{\triangle_{abc}}f_n(z)\dd z = \int_{\triangle_{abc}} f(z) \dd z = 0
  $$
  - Where swapping is legal, as $f_n$ converge uniformly on $\triangle_{abc}$.
- Morera theorem indicate that $f(z)$ is holomorphic on $D$.

Then $f_n'$ converge to $f'$ uniformly in any compact subset of $\Omega$. ==TODO==

##### Holomorphic function defined by integral

Suppose $\Omega \subseteq \C$ is a region. And $F: \Omega \times [0, 1] \to \C$ satisfies the following:

1. For all $t \in [0, 1]$ , $F(\cdot, t)$ is holomorphic.
2. $F$ is continuous on $\Omega \times [0, 1]$

Then $f(z) := \int_{0}^1 F(z, t) \dd t$ is holomorphic on $\Omega$.

- $f(z)$ is continuous everywhere since $F(z, t)$ is uniformly continuous.
- Consider any triangle $\triangle_{abc}$ in $\Omega$.
  $$
  \int_{\triangle_{abc}} \p{\int_0^1 F(z, t) \dd t} \dd z = \int_0^1 \int_{\triangle_{abc}} F(z, t) \dd z \dd t= 0
  $$
- The change of integral order is justified by Fubini's theorem.

##### Riemann's theorem

Suppose $\Omega$ is a region, and $f$ is holomorphic on $\Omega - \c{c}$ for $c \in \Omega$.

Suppose $f$ is **bounded** on $\Omega - \c c$, then $c$ is a removable singularity of $f$.

- Suppose $D = B(z_0, r_0)$ is a disk where $c \in D$, and $\overline D \subseteq \Omega$. Denote $C = \part D$.
- Construct a double keyhole contour, we have:
  $$
  \forall z \in D: \frac{1}{2\pi i}\oint_C \frac{f(s)}{s - z} \dd s = f(z)
  $$
- By a similar argument as in (**Holomorphic function defined by integral**). $f(z)$ is holomorphic on $D$.
- Therefore we can fill in $f(c)$ as
  $$
  f(c) := \frac{1}{2\pi i} \oint_C \frac{f(s)}{s - c} \dd s
  $$

Suppose $\lim_{z \to c} \abs{f(z)} = \infty$, then $c$ is a pole of $f$.

- Just notice that $1/f(z)$ satisfies the results on removable singularity.

##### Essential singularity

Any singularity that is neither removable nor a pole is a **essential singularity**.

##### Casorati-Weierstrass ==TODO==

Suppose $f$ is holomorphic in $U(c, r)$ but $f$ has essential singularity at $c \in \C$.

Then $f\s{U(c, r)}$ is **dense** in $\C$.

