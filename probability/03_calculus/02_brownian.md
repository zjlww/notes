### Brownian Motion

(**Continuous independent increment**)

Suppose $(X_t)_{t \in [0, T]}$ is an **independent inc.** **a.s. continuous** process and $X_0$ is Gaussian, then $(X_t)$ is a **Gaussian process**. ==TODO==

(**Kolmogorov's continuity theorem**)

Let $\T \subset \mathbb{R}^{m}$ be an open set and $(X_t)_{t \in \T}$ a family of $\R^d$ valued r.v.'s on $(\Omega, \F, P)$ such that there exist $\alpha>0, \beta>0, c>0$ satisfying
$$
E\left[\left|X_{y}-X_{z}\right|^{\beta}\right] \leq c|y-z|^{m+\alpha}
$$
Then there exists a **modification** of $(X_t)$ denoted $(\widetilde X_t)$ that is **Hölder continuous** with exponent $\gamma$ for every $\gamma<\frac{\alpha}{\beta}$ on every compact subset of $T$. ==TODO==.

(**Brownian motion**)

A real-valued stochastic process $(B_t)_{t \in [0, T]}$ on $(\Omega, \F, P)$ is a **Brownian motion** (BM) if

- $P(B_0 = 0) = 1$.
- $(B_t)$ has the **independent inc.** property.
- $\forall 0 \le s \le t \le T: B_t - B_s \sim N(0, t - s)$.

Immediately following this definition:

- $(B_t)$ has a **continuous** modification by (**Kolmogorov's continuity theorem**).
- $(B_t)$ is a **centered** process since $\forall t\in [0, T]: E[B_t] = 0$.
- $(B_t)$ is a **Gaussian process** with $\cov(B_s, B_t) = \min(s, t) = s\land t$.

Equivalently, a real-valued Gaussian process $(B_t)_{t \in [0, T]}$ on $(\Omega, \F, P)$ with zero mean and covariance $\cov(B_s, B_t) = s \land t$ is a **Brownian motion**.

- $(B_t)$ has the **independent inc.** property.
- $\forall 0 \le s \le t:(B_t - B_s) \sim N(0, t - s)$ since
    - $E[(B_t - B_s)^2] = E B_t^2 + EB_s^2 - 2 EB_t B_s = t + s - 2s = t - s$.

A Brownian motion with **continuous path** is called a **standard Brownian motion**.

(**BM and GP**)

Suppose $(X_t)_{t \in [0, T]}$ is a **real Gaussian process**.

- Suppose $X_t$ has the **independent inc.** property, $\cov(X_s, X_t) = \operatorname{Var}(X_s)$.
- Further suppose the increments of same time difference are **identically distributed**, then $E[X_s] = k \cdot s$ and $\cov(X_s, X_t) = \sigma^2 s \land t$. (approximately true).

(**BM is nowhere differentiable: TODO**)

Suppose $(B_t)_{t \ge 0}$ on $(\Omega, \F, P)$ is a Brownian motion. The paths $B_t$ are almost surely nowhere differentiable.

(**Multivariate BM**)

A $\R^d$-valued process $(B_t)_{t \in [0, T]}$ on $(\Omega, \F, P)$ is a **Brownian motion** (BM) if

- $P(B_0 = \mathbf 0) = 1$.
- $(B_t)$ has the **independent inc.** property.
- $\forall 0 \le s \le t: B_t - B_s \sim N(\mathbf 0, (t - s)I_d)$.

Immediately following this definition:

- $(B_t)$ has a **continuous** modification by (**Kolmogorov's continuity theorem**).
- $(\Omega, \F, (\F_t), (B_t)_i, P)$ is a 1D Brownian motion.
- Each coordinate $B_t^{(k)}$ of $B_t$ is a 1D Brownian motion.
- $\F^{(i)} = \sigma(B_t^{(i)}, t \ge 0)$ are independent.
    - With some reasoning, we only need to show $B_t^{(i)}$ and $B_s^{(j)}$ are independent.
    - Suppose $s \le t$, $E[B_t^{(i)} B_s^{(j)}] = E[(B_t^{(i)} - B_s^{(i)} + B_{s}^{(i)}) B_s^{(j)}] = 0$.
- For $z \in \R^d$, $X_t = \pd{z}{B_t}$ is a 1D Brownian motion. $E[(z^TB_s)(z^T B_t)] = \pd zz s \land t$.

Equivalently, a real-valued Gaussian process $(B_t)_{t \in [0, T]}$ on $(\Omega, \F, P)$ with zero mean and covariance  $\cov(B_s, B_t) = s \land t$ is a **Brownian motion**.

- $(B_t)$ has the **independent inc.** property.
- $\forall 0 \le s \le t \le T:(B_t - B_s) \sim N(0, t - s)$ since
  - $E[(B_t - B_s)^2] = E B_t^2 + EB_s^2 - 2 EB_t B_s = t + s - 2s = t - s$.

(**Blumenthal**)

Suppose $(B_t)_{t \ge 0}$ is a **BM** with **the natural filtration** $(\F_t)$. If $A \in \F_{0+}$, then $P(A) \in \{0, 1\}$.

- $\forall t > 0:\F_t \perp \F_{0+}$. (Only works with the natural one.)
- Since $A \in \F_{0+}\subseteq \F_{1}$. So $P(A \cap A) = P(A)P(A)$. So $P(A) \in \{0, 1\}$.

(**Zero recurrence**)

Suppose $(B_t)_{t \ge 0}$ is a **BM** with **the natural filtration** $(\F_t)$. Then $P(\forall s > 0: (\max_{t \in [0, s]} B_t) > 0) = 1$.

- Clearly the event $A = \{\forall s > 0: (\max_{t \in [0, s]} B_t) > 0\} \in \F_{0 + }$.
- Now we claim that $P(A) = 1$.
  - $B_t$ is **not Lipschitz (TODO)** at $t = 0$. So for some $t_k \downarrow 0$, $|B_{t_k}| \ge t_k$.

Now since $t B_{1/t}$ is also a Brownian motion, $B_t$ returns to zero almost surely as $t \to \infty$.

(**Brownian Bridge**)

A real valued **Gaussian process** $(B_t)_{t \in [0, T]}$ on $(\Omega, \F, P)$ with zero mean and covariance function $\cov(B_s, B_t) = s(T - t)/T$ if $s \le t$ is called a **Brownian Bridge**.

- $(B_t)$ has a **continuous** modification.
- $P(B_0 = 0) = 1$ and $P(B_T = 0) = 1$.
- When $T = 1$, the process is called a standard Brownian Bridge.

(**Transformation of standard BM**)

Suppose $(B_t)$ is a standard BM on $(\Omega, \F, P)$. Then

- (**Time shift**) Suppose $s \ge 0$. Define $X_t = B_{s + t} - B_s$.
    - Then $(X_t)$ is a standard BM.
    - Suppose $(B_t)$ is adapted to $(\F_t)$, $(X_t)$ is adapted to $(\F_{s + t})$.
- (**Scale**) Suppose $\sigma > 0$. Define $X_t = \sigma B_t$.
    - Then $(X_t)$ is a **scaled standard BM** where $\cov(X_s, X_t) = \sigma^2 s\land t$.
- (**Bridge**) Define $Z_t = B_t - tB_1$ on $t \in [0, 1]$.
    - Then $Z_t$ is a **standard Brownian Bridge**.
    - Random variable families $\{Z_t: t \in [0, 1]\} \perp \{B_t: t \ge 1\}$.
        - As for $s \le 1 \le t$, $E[Z_sB_t] = E[(B_s - s B_1)B_t] = 0$.
- (**Time reversal**) Define $Z_t = B_1 - B_{1 - t}$ on $t \in [0, 1]$. Then $Z_t$ is a natural BM.
- (**Weak reflection**) Suppose $s \ge 0$. Define $X_t = B_t 1_{t \le s} + (2B_s - B_t) 1_{t> s}$.
    - Then $(X_t)$ is a standard BM.
    - Suppose $(B_t)$ is adapted to $(\F_t)$, clearly $(X_t)$ is also adapted to $(\F_t)$.
- (**Time inverse**) Let $Z_t = t B_{1 / t}$ when $t > 0$ and $Z_t = 0$ when $t = 0$.
    - Then $(Z_t)$ is a Brownian motion.
        - When $0 < s \le t$, $\cov(Z_s, Z_t) = \cov(sB_{1/s}, t B_{1/t}) = st/t = s$.
    - When $(B_t)$ is continuous, $(Z_t)$ is continuous on $(0, \infty)$, and a.s. continuous at $0$.
        - Continuous at $0$ is derived via distribution argument.
- (**OU process**) Let $X_t = e^{-2t} B_{e^{4t}}/\sqrt 2$ for $t \in \R$. Then $X_t$ is an **OU process**.

(**Quadratic variation**)

Suppose $f, g : [a, b] \to \R$. We say the **quadratic variation (QV)** of $g$ on $[a, b]$ exists if $$
\exists Q \in \R, \forall (P_r = (t^r_i)_{i = 0}^{n_r})_{r = 1}^\infty \in P[a, b]: \|P_r\| \to 0 \implies \lim_{r \to \infty} \sum_{i = 1}^{n_r} (\Delta^r g_i)^2 = Q$$
- Denote $[g](a, b) = Q$ when such $Q$ exists. Where $\Delta^r g_i = (g(t^r_i) - g(t^r_{i - 1}))$.
- If $g \in C[a, b]\cap V[a, b]$, then $[g](a, b) = 0$.
    - $\forall (t_i)_{i = 0}^n \in P[a, b]:\sum_{i = 1}^n (g(t_{i}) - g(t_{i - 1}))^2 \le \max_{i} |g(t_{i}) - g(t_{i - 1})| V_g(a, b)$.

We say the **covariation (COV)** of $f, g$ on $[a, b] \to \R$ exists if $$
\exists Q \in \R, \forall (P_r = (t^r_i)_{i = 0}^{n_r})_{r = 1}^\infty \in P[a, b]: \|P_r\| \to 0 \implies \lim_{r \to \infty} \sum_{i = 1}^{n_r} (\Delta^r g_i\Delta^r f_i) = Q$$
- Denote $[f, g](a, b) = Q$ when such $Q$ exists.
- If $f \in C[a, b]$ and $g \in V[a, b]$, then $[f, g](a, b) = 0$.
    - The proof is similar to above.

For $[f](0, t)$ is often abbreviated as $[f]_t$ and $[f, g]_t$ similarly.

More generally, suppose $X_t(\omega), Y_t(\omega)$ are real valued random processes on $t \in [a, b]$, the limit is interpreted in various **modes of convergence** on $\L(\Omega \to \R)$. Denoted by $[X]_t(\omega) = f(t, \omega)$ in $\L_2$, in $P$, etc.

(**Polarization identity for Covariation**)

Suppose $[X + Y]_t, [X]_t, [Y]_t$ all exists in some mode, then $[X, Y]_t$ exists in the same mode and $[X, Y]_t = \left([X + Y]_t - [X]_t - [Y]_t\right)/2$.

(**QV of Brownian motion**)

Suppose $(B_t)_{t \ge 0}$ is a Brownian motion.
- (**Arguin**) $[B_t(\omega)](0, T) = [B]_T = T$ in $\L_2$ for all $T > 0$.
    - Consider a fixed partition $P = (t_i)_{i = 0}^n \in P[0, T]$.
    - Define $T = \sum_{j = 0}^{n - 1}(B_{t_{j + 1}}-B_{t_j})^2$. Define $X_j = (B_{t_{j+1}} - B_{t_j})^2 - (t_{j + 1} - t_j)$. $$
    \norm{T- t}_2^2= E\left[\sum_{j = 0}^{n - 1}X_j\right]^2 =\sum_{i = 0}^{n - 1}E[X_i^2]= \sum_{i = 0}^{n - 1}2(t_{i + 1} - t_i)^2 \le \|(t_i)\| \cdot t \to 0$$
- (**Arguin**) $[B]_T = T$ $P$.a.e. for all $T > 0$ when restricting to partition sequences $(P_r) \in P[0, T]$ where $\sum_r\|P_r\| < \infty$. (For example the dyadic sequence).
    - Following the same procedure as above. Notice that $\norm{T - t}^2_2 \le \norm{P}\cdot t$.
    - Now apply (**Fast III**) fast convergence theorem.
- (**Klebaner**) $[B]_T = T$ $P$.a.e. for all $T > 0$ for any shrinking partition sequences. ==TODO==

The following properties of the Brownian path $B_t(\omega)$ immediately follows:
- For any $l > 0$, $B_t(\omega)$ is **not** of bounded variation on any interval with length $l$ for probability one.
- For any $l > 0$, $B_t(\omega)$ is **not** monotone on any interval with length $l$ for probability one.

