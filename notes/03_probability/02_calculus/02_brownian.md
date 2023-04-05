#### Brownian Motion

> Evans, L.C. (2014). An Introduction to Stochastic Differential Equations.

##### Brownian motion

A real-valued stochastic process $(B_t)_{t \in [0, T]}$ on $(\Omega, \F, P)$ is a **Brownian motion** (BM) if

- $P(B_0 = 0) = 1$.
- $(B_t)$ has the **independent inc.** property.
- $\forall 0 \le s \le t \le T: B_t - B_s \sim N(0, t - s)$.

Immediately following this definition:

- $(B_t)$ has a **continuous** modification by (**Kolmogorov's continuity theorem**).
- $(B_t)$ is a **centered** process since $\forall t\in [0, T]: E[B_t] = 0$.
- $(B_t)$ is a **Gaussian process** with $\cov(B_s, B_t) = \min(s, t) = s\land t$.
  $$
  s \le t \implies E[B_sB_t] = E\s{(B_s + B_t - B_s) B_s} = E\s{B_s^2} + E\s{(B_t - B_s) B_s} = s
  $$

A Brownian motion with **continuous path** is called a **standard Brownian motion**.

For $s \ge 0$. Define $X_t = B_{s + t} - B_s$. Then $(X_t)$ is a standard BM.

##### Construction of Brownian motion ==TODO==

> See Evans, L.C. (2014). An Introduction to Stochastic Differential Equations.

We can construct a standard Brownian motion from countably infinite $\mathcal N(0, 1)$ distributed random variables.

##### BM is nowhere differentiable ==TODO==

Suppose $(B_t)_{t \ge 0}$ on $(\Omega, \F, P)$ is a Brownian motion. The paths $B_t$ are almost surely nowhere differentiable.

##### Multivariate Brownian motion

A $\R^d$-valued process $(B_t)_{t \in [0, T]}$ on $(\Omega, \F, P)$ is a **Brownian motion** (BM) if

- For each coordinate $i \in \c{1, \ldots, d}$, $(\Omega, \F, (\F_t), (B_t^{(i)}), P)$ is a 1D Brownian motion.
- $\F^{(i)} = \sigma(B_t^{(i)}, t \ge 0)$ are independent.

Immediately following this definition:

- $(B_t)$ has a **continuous** modification by (**Kolmogorov's continuity theorem**).
- For $z \in \R^d$, $X_t = \pd{z}{B_t}$ is a 1D Brownian motion. $E[(z^TB_s)(z^T B_t)] = \pd zz s \land t$.

#### Properties of Brownian Sample Paths

##### Review: Hölder continuity

Suppose $E, F$ are metric spaces.

A function $f:E \rightarrow F$ is called **uniformly Hölder continuous** with exponent $\gamma > 0$ if
$$
\exists K > 0, \forall s, t \in I:d\p{f(t)-f(s)} \leq Kd\p{t-s}^\gamma
$$
Function $f$ is **Hölder continuous** with exponent $\gamma>0$ at the point $s$ if
$$
\exists K > 0, \forall s, t \in E:d\p{f(t)-f(s)} \leq Kd\p{t-s}^\gamma
$$

##### Kolmogorov's continuity theorem ==TODO==

> [Almost sure blog](https://almostsuremath.com/2020/10/20/the-kolmogorov-continuity-theorem/) on a more general form of the theorem.

Let $(X_t)_{t \ge 0}$ a $\R^d$ valued random process on $(\Omega, \F, P)$.

Suppose there exist $\alpha>0, \beta>0, c>0$ satisfying
$$
\forall y, z \ge 0:E\left[\left|X_{y}-X_{z}\right|^{\beta}\right] \leq c|y-z|^{1+\alpha}
$$
For almost all $\omega \in \Omega$,
$$
\forall T > 0, \forall 0 < \gamma < \frac{\alpha}{\beta},\exists K > 0, \forall s, t \in [0, T]: \n{X_s(\omega) - X_t(\omega)} \le K |s - t|^\gamma
$$
There exists a **modification** of $(X_t)$ denoted $(\widetilde X_t)$, such that a.e. sample path is **uniformly Hölder continuous** with exponent $\gamma$ for every $0 < \gamma<\frac{\alpha}{\beta}$ on every $[0, T]$ interval.

##### Hölder continuity of paths

Suppose $(B_t)_{t \ge 0}$ is a standard Brownian motion.

We have for all integers $m \in \N^+$. For all $t > s \ge 0$, let $r = t - s > 0$, then
$$
\begin{aligned}
E\s{\abs{B_t - B_s}^{2m}} &= \frac{1}{(2\pi r)^{n / 2}} \int_{\R} |x|^{2m} \exp\p{-\frac{x^2}{2r}} \dd x\\
&= \frac{1}{(2\pi)^{n /2}} r^m \int_{\R} |y|^{2m} \exp\p{-\frac{y^2}{2}} \dd y\\
& = cr^m = c|t - s|^{1 + (m - 1)}
\end{aligned}
$$
Now apply Kolmogorov's theorem for $\beta = 2m$ and $\alpha = m - 1$. Paths are almost surely Hölder continuous with exponents $0 < \gamma < 1 / 2$.

##### Roughness of paths ==TODO==

Suppose $(B_t)_{t \ge 0}$ is a standard Brownian motion.

For each $\gamma \in (1/2, 1]$, for almost all $\omega \in \Omega$, path $B_t(\omega)$ is nowhere Hölder continuous with exponent $\gamma$.

Take $\gamma = 1$ shows that almost surely, path $B_t(\omega)$ is nowhere differentiable.

#### Quadratic Variations

##### Quadratic variation of functions

Suppose $f, g : [a, b] \to \R$. We say the **quadratic variation (QV)** of $g$ on $[a, b]$ exists if
$$
\exists Q \in \R, \forall (P_r = (t_{r, i})_{i = 0}^{n_r})_{r = 1}^\infty \in P[a, b]: \|P_r\| \to 0 \implies \lim_{r \to \infty} \sum_{i = 1}^{n_r} (\Delta_{r, i} g)^2 = Q
$$
where $\Delta_{r, i} g := (g(t_{r, i}) - g(t_{r, i - 1}))$.

Denote by $[g](a, b) = Q$ when such $Q$ exists for the interval $[a, b]$.

- $[f](0, t)$ is often abbreviated as $[f]_t$.

For a continuous function with bounded variations $g \in C[a, b]\cap V[a, b]$, $[g](a, b) = 0$.
$$
\forall (t_i)_{i = 0}^n \in P[a, b]:\sum_{i = 1}^n (g(t_{i}) - g(t_{i - 1}))^2 \le \max_{i} |g(t_{i}) - g(t_{i - 1})| V_g(a, b)
$$
Suppose $X_t(\omega)$ is a real valued random processes on $t \in [a, b]$. We extend the above definition.

- $\sum_{i = 1}^{n_r} (\Delta_{r, i} X(\omega))^2$ is now a sequence of random variables.
- The limit is considered to be in various **modes of convergence** on $\L(\Omega \to \R)$.
- When stating the quadratic variation of a random process, we also state the mode of convergence.
- The same need of stating the mode of convergence also crop up in the definition of stochastic integral with limit of sums.

##### Covariation of functions

Suppose $f, g: [a, b] \to \R$. We say the **covariation (CoV)** of $f, g$ on $[a, b]$ exists if
$$
\exists Q \in \R, \forall (P_r = (t_{r,i})_{i = 0}^{n_r})_{r = 1}^\infty \in P[a, b]: \|P_r\| \to 0 \implies \lim_{r \to \infty} \sum_{i = 1}^{n_r} (\Delta_{r, i} g\Delta_{r, i} f) = Q
$$
where $\Delta_{r, i} g := g(t_{r, i}) - g(t_{r, i - 1})$.

Denote by $[f, g](a, b) = Q$ when such $Q$ exists for the interval $[a, b]$.

- $[f, g](0, t)$ is often abbreviated as $[f, g]_t$.

When $f \in C[a, b]$ and $g \in V[a, b]$ we have $[f, g](a, b) = 0$.
$$
\forall (t_i)_{i = 0}^n \in P[a, b]:\sum_{i = 1}^n (f(t_{i}) - f(t_{i - 1}))(g(t_{i}) - g(t_{i - 1})) \le \max_{i} |f(t_{i}) - f(t_{i - 1})| V_g(a, b)
$$
Suppose $X_t(\omega), Y_t(\omega)$ are real valued random processes on $t \in [a, b]$ on the same probability space. We extend the above definition.

- $\sum_{i = 1}^{n_r} (\Delta_{r, i} X(\omega)\Delta_{r, i} Y(\omega))$ is now a sequence of random variables.
- The limit is considered to be in various **modes of convergence** on $\L(\Omega \to \R)$.

##### The polarization identity

Suppose $(X_t)_{t \ge 0}$ and $(Y_t)_{t \ge 0}$ are real random processes on the same probability space.

Suppose $[X + Y]_t, [X]_t, [Y]_t$ all exists in some mode. Then $[X, T]_t$ exists in the same mode and
$$
[X, Y]_t = \frac{\p{[X + Y]_t - [X]_t - [Y]_t}}{2}
$$

##### QV of Brownian motion

Suppose $(B_t)_{t \ge 0}$ is a standard Brownian motion.

For all $T > 0$, $[B_t(\omega)]_T = T$ essentially pointwise on $\Omega$. ==TODO== (See Klebaner). We prove two weaker results here.

For all $T > 0$, $[B_t(\omega)]_T = T$ in $\L_2$ (by Arguin).

- Consider a fixed partition $P = (t_i)_{i = 0}^n \in P[0, T]$.
- Define $S = \sum_{j = 0}^{n - 1}(B_{t_{j + 1}}-B_{t_j})^2$.
- Define $X_j = (B_{t_{j+1}} - B_{t_j})^2 - (t_{j + 1} - t_j)$ for $j \in \c{0, \ldots n - 1}$.
- Then observe
  $$
  \norm{S - t}_2^2= E\s{\sum_{j = 0}^{n - 1}X_j}^2 =\sum_{i = 0}^{n - 1}E[X_i^2]= \sum_{i = 0}^{n - 1}2(t_{i + 1} - t_i)^2 \le \|P\| \cdot t \to 0
  $$

For all $T > 0$, $[B_t(\omega)]_T = T$ essentially pointwise for fast shrinking partition sequences $(P_r) \in P[0, T]$ where $\sum_r\|P_r\| < \infty$. (For example the dyadic sequence).

- Following the same procedure as above. Notice that $\norm{T - t}^2_2 \le \norm{P}\cdot t$.
- Now apply (**Fast III**) fast convergence theorem.

The following properties of the Brownian path $B_t(\omega)$ immediately follows:

- For any $l > 0$, $B_t(\omega)$ is **not** of bounded variation on any interval with length $l$ for probability one.
- For any $l > 0$, $B_t(\omega)$ is **not** monotone on any interval with length $l$ for probability one.

##### Covariation of independent Brownian motions

Suppose $(X_t)$ and $(Y_t)$ are independent standard Brownian motions. Then $[X, Y]_t = 0$ in $\L_2$.

Consider any sequence of shrinking partitions. And suppose one of the partitions is $(t_i)_{i = 0}^n \in P[0, t]$.
$$
E\s{\sum_{i = 0}^{n - 1} \Delta X_i \Delta Y_i - 0}^2 = \sum_{i = 0}^{n - 1} E \Delta X_i^2 E\Delta Y_i^2 = \sum_{i = 0}^{n - 1} \Delta t_i^2 \to 0
$$

