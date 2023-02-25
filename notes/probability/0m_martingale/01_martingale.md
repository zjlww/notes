#### Martingale Theory

##### Martingale

 Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered probability space. 

Suppose $(X_t)$ is a **real** process adapted to $(\F_t)$ and $\forall t \in \I: E|X_t| < \infty$. Then $(X_t)$ is

- a **$(\F_t)$-martingale** if $\forall s < t \in \I: E[X_t | \F_s] = X_s$;
- a **super-martingale** if $\forall s < t \in \I: E[X_t | \F_s] \le X_s$;
- a **sub-martingale** if $\forall s < t \in \I: E[X_t | \F_s] \ge X_s$. (A **favorable** game.)

When $\I \subseteq \Z$ we have following equivalent definitions:

- $(X_n)$ is a submartingale if $\forall n \in \I: E[X_{n + 1} | \F_n] \ge X_n$.
- $(X_n)$ adapted to $(\F_n)$ is a submartingale iff $\forall A \in \F_n: P(1_A X_n) \le P(1_A X_{n + 1})$.
- $(X_n)$ is a $(\F_n^X)$-submartingale iff $E[X_{n + 1} | X_1 = x_1, \ldots, X_n = x_n] \ge x_n$, $P_{X_1\cdots X_n}$ almost surely.
  - By the conversion rule of level set / $\sigma$-algebra conditional expectation.

If $(X_t)$ is a $(\F_t)$-submartingale, then $E[X_{t}] = E[E[X_{t} | \F_s]] \ge E[X_s]$ for $s < t \in \I$.

**Transformations** of martingales:

- $(X_t)$ is a supermartingale iff $(-X_t)$ is a submartingale.
- If $(X_t)$ and $(Y_t)$ are $(\F_t)$-submartingales, then $(\max(X_t, Y_t))$ is a $(\F_t)$-submartingale.
  - Since $E[\max (X_{t}, Y_{t}) | \F_s] \ge E[X_{t} |\F_s] \ge X_s$.
  - Similarly when replacing sub with super and max with min.
- If $(X_t)$ is a $(\F_t)$-submartingale, and $(X_t)$ is adapted to $(\G_t)$ where $\G_t \subseteq \F_t$.
  - Then $(X_t)$ is a $(\G_t)$-submartingale. Since $E[X_{t} | \G_s] = E[X_{t} | \F_s | \G_s] \ge X_s$.
  - In particular $(X_t)$ is a $(\F_t^X)$-submartingale.
- If $(X_t)$ and $(Y_t)$ are $(\F_t)$-martingales and $a, b \in \R$, then $(a X_t + b Y_t)$ is also a $(\F_t)$-martingale.
  - Since $E[(aX_t + bY_t) | \F_s] = (a X_s + b Y_s)$.
- If $(X_t)$ and $(Y_t)$ are $(\F_t)$-submartingales and $a, b \ge 0$, then $(a X_t + b Y_t)$ is a $(\F_t)$-submartingale.
- If $(X_t)$ is a $(\F_t)$-martingale, and $\varphi: I \to \R$ where $I$ is an open interval in $\R$ is convex. Then $(\varphi(X_t))$ is a submartingale if $E|\varphi(X_t)| < \infty$ and $\forall t \in \I: X_t[\Omega] \in I$.
  - $E[\varphi(X_{t}) | \F_s] \ge \varphi(E[X_{t} | \F_s]) = \varphi(X_s)$.
  - To verify the condition $E|\varphi(X_t)| < \infty$, we have following remarks:
    - $E|\varphi(X_t)| < \infty \iff E[\varphi(X_t)^+] < \infty$.
      - Since $\varphi$ is bounded by lines of support.
    - If $E[\varphi(X_t)^+] < \infty$, then $\forall s \le t \in \I: E[\varphi(X_s)^+] < \infty$.
  - When relaxing $(X_n)$ to be $(\F_n)$-submartingale, $\varphi$ need to be **increasing**.


##### Examples of discrete martingales

 Consider probability space $(\Omega, \F, P)$.

- Suppose $(Y_n)_{n = 1}^\infty$ are independent real random variables with $E[Y_n] \ge 0$. Let $X_n = \sum_{k = 1}^n Y_k$. Let $(\F_n) = (\F_n^Y)$. Then $(X_n)$ is a $(\F_n)$-submartingale.
  - $E[X_{n + 1} | \F_n] = E[X_n + Y_{n + 1} | \F_n] \ge X_n$.
- Suppose $(Y_n)_{n = 1}^\infty$ are independent real random variables with $E[Y_n] = a_j \in \R \backslash \{0\}$. Let $X_n = \prod_{j = 1}^n (Y_j / a_j)$. Let $(\F_n) = (\F_n^Y)$. Then $(X_n)$ is a $(\F_n)$-martingale.
  - $E[X_{n + 1} | \F_n] = E[X_n (Y_{n + 1} / a_{n + 1}) | \F_n] = X_n$.
- Suppose $Y \in \L^1(\Omega \to \R, \F, P)$. And $(\F_n)$ is some filtration. Then $X_n = E[Y| \F_n]$ is a $(\F_n)$-martingale.
  - $E[X_{n + 1} | \F_n] = X_n$; $E|X_n| < \infty$ and $X_n \in \F_n$.

##### Increments in Martingales

 Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered space.

Suppose $(M_t)$ is an $(\F_t)$-martingale and $\forall t \in \I: E[M_t^2] < \infty$. Suppose $a \le b \le c \le d \in \I$, then $E[(M_b - M_a)(M_d - M_c)] = 0$.

- $E[\cdots | \F_c] = E[(M_b - M_a)E[M_d - M_c | \F_c]] = 0$.

##### Discrete martingale transform

 Suppose $(\Omega, \F, (\F_n), \N, P)$ is a filtered space.

Let $(X_n)_{n \in \N}, (H_n)$ be $(\F_n)$-adapted real processes. Define
$$
\forall n \in \N: (H \cdot X)_n = \sum_{m = 0}^{n - 1} H_{m} (X_{m + 1} - X_m); \quad (H \cdot X)_0 = 0;
$$
$(I_n) = ((H\cdot X)_n)$ is well defined and adapted to $(\F_n)$.

If $(X_n)$ is a $(\F_n)$-martingale, then $(I_n)$ is called the **martingale transform** of $(X_n)$ by $(H_n)$.

$(X_n)$ is an $(\F_n)$-martingale if and only if for any **adapted locally bounded** $(H_n)$, $(I_n)$ is a martingale.

- $(\to)$ $E[I_{n + 1} | \F_n] = E[I_n + H_{n - 1}(X_{n} - X_{n - 1}) | \F_n] = I_n$.
- $(\leftarrow)$ Take $H_n = 1$.

$(X_n)$ is an $(\F_n)$-submartingale if and only if for any **adapted locally bounded** $(H_n)$ where $H_n \ge 0$, $(I_n)$ is a submartingale. (replace submartingale $\to$ super martingale.)

- $(\to)$ $E[I_{n + 1} | \F_n] = E[I_n + H_{n - 1}(X_{n} - X_{n - 1}) | \F_n] \ge I_n$.
- $(\leftarrow)$ Take $H_n = 1$.

##### Discrete Doob decomposition

 Suppose $(X_n)_{n \in \N}$ is adapted to $(\F_n)$ where $E|X_n| < \infty$.

- Define $M_n:= X_0 + \sum_{k = 1}^n (X_k - E[X_k | \F_{k - 1}])$. Then $M_n$ is a martingale.
- Define $A_n := \sum_{k = 1}^n(E[X_k| \F_{k - 1}] - X_{k - 1})$, $A_0 = 0$. $A_n$ is predictable.
- Such decomposition $X_n = M_n + A_n$ is called the Doob decomposition.
- Doob decomposition is **unique**.
  - Suppose $X_n = M'_n + A'_n$, then $M_n - M'_n = A'_n - A_n$.
  - So $M_n - M'_n$ is predictable and a martingale.
  - $E[M_n - M'_n | \F_{n - 1}] = M_{n} - M'_n = M_{n - 1} - M'_{n - 1} = \cdots = 0$.
- $(X_n)$ is a submartingale if and only if $A_n(\omega)$ is increasing.

##### Square variation

 Suppose $(X_n)_{n \in \N}$ is a $(\F_n)$-martingale and $\forall n \in \I: E[X_n^2] < \infty$ (called **square-integrable**.)

- Since $E[X_n^2] < \infty$, $(X_n^2)$ is an $(\F_n)$-submartingale. Suppose $X_n^2 = M_n + A_n$ by (**Doob**).
- Then $(X_n^2 - A_n)$ is a martingale.
- $A_n = \sum_{i = 1}^n (E[X_i^2 | \F_{i - 1}] - X_{i - 1}^2) = \sum_{i = 1}^n (E[(X_i - X_{i - 1})^2 | \F_{i - 1}])$.

$(A_n)$ is called the **square variation process** of $(X_n)$ denoted by $(\langle X \rangle_n)$.

- $(\langle X \rangle_n)$ is the unique **predictable** process where $(X_n^2 - \langle X\rangle_n)$ is a martingale.
- $E[A_n] = E[\langle X \rangle_n] = E[X_n^2] - E[X_0^2] = \var[X_n - X_0]$.

##### Discrete sampling lemma

 Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered space where $\I$ is **countable**. Suppose $(X_t)$ is an $(\F_t)$-**martingale** and $\tau$ is a **bounded stopping time** where $\tau \le T \in \I$.

Then $X_\tau = E[X_T | \F_\tau]$. And $E[X_\tau] = E[E[X_T | \F_\tau]] = E[X_T]$.

- Only need to show $\forall A \in \F_\tau: E[X_T 1_A] = E[X_\tau 1_A]$.
- Since $A \in \F_\tau$, $\forall t \in \I: \{\tau = t\} \cap A \in \F_t$.
- $E[X_\tau 1_A] = \sum_{t \le T} E[X_\tau 1_{\{\tau = t\} \cap A}] = \sum_{t \le T}E[E[X_T | \F_t] 1_{\{\tau = t\} \cap A}] = E[X_T 1_A]$.

##### Stopped process

 Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered space where $\I$ is **countable**. Suppose $(X_t)$ is **adapted** and $\tau$ is a **stopping time**.

- Define the **stopped process** $X_t^\tau = X_{t \land \tau}$ for $t \in \I$.
- Define the **stopped filtration** $\F_t^\tau = \F_{t \land \tau}$ for $t\in \I$.
  - Clearly $\F_{t \land \tau} \le \F_t, \F_{\tau}$.
  - For $A \in \F_\tau$, $\forall t \in \I: \{\tau \le t\} \cap A \in \F_{t \land \tau}$. (Also works for $\{\tau = t\}$, and $\{\tau < t\}$).
    - Since $A \in \F_\tau$, $\forall s \in \I: \{\tau \le s\} \cap A \in \F_s$.
    - $\forall s \in \I: \{(\tau \land t) \le s\} \cap \{\tau \le t\} \cap A \in \F_s$.
- $(X_{t \land \tau})$ is adapted to $(\F_t)$ and $(\F_{t \land \tau})$.

##### Optional sampling

 Suppose $(\Omega, \F, (\F_n), \N, P)$ is a filtered space.

Suppose $(X_n)$ is a $(\F_n)$-**submartingale** and $\sigma, \tau$ are **stopping times**.

Suppose $\sigma, \tau$ are **bounded**, $\sigma \le \tau \le T \in \N$. Then $X_\sigma \le E[X_\tau | \F_\sigma]$.

- By (**Doob decomposition**), $X_n = M_n + A_n$ where $(M_n)$ is a martingale and $(A_n)$ is increasing and $A_0 = 0$.
- $X_\sigma = M_\sigma + A_\sigma = E[A_\sigma + M_T | \F_\sigma] \le E[A_\tau + M_T | \F_\sigma]$.
- $\cdots  = E[A_\tau + E[M_T | \F_\tau] | \F_\sigma] = E[A_\tau + M_\tau | \F_\sigma] = E[X_\tau | \F_\sigma]$.

Suppose $\sigma, \tau$ are **bounded** $0 \le \sigma \le \tau \le T$. Then $E[X_\sigma] \le E[X_\tau]$.

- This immediately follows from above.

Suppose $(X_n)$ are **nonnegative** and $\sigma \le \tau$ are a.s. **finite**. Then $E[X_0] \le E[X_\tau]$.

- $X_{\tau \land n} \to X_\tau$ almost surely. Since $0 \le (\tau \land n) \le n$, $\forall n \in \N: E[X_0] \le E[X_{\tau \land n}]$.
- $E[X_\tau] = E[\lim_{n \to \infty} X_{\tau \land n}] \ge \limsup_n E[X_{\tau \land n}] \ge E[X_0]$.

Suppose $(X_n)$ are **nonnegative** and $\sigma \le \tau$ are a.s. **finite**. Then $X_\sigma \le E[X_\tau | \F_\sigma]$.

- Let $m, n \in \N$ with $m \ge n$. Then $\sigma \land n \le \tau \land m$. So $X_{\sigma \land n} \le E[X_{\tau \land m} | \F_{\sigma \land n}]$.
- Suppose $A \in \F_\sigma$, $\{\sigma < n\} \cap A \in \F_{\sigma\land n}$ by (**Stopped process**).
- $E[X_\sigma 1_{\{\sigma < n\} \cap A}] = E[X_{\sigma \land n} 1_{\{\sigma < n\} \cap A}] \le E[X_{\tau \land m} 1_{\{\sigma < n\} \cap A}]$.
- $E[X_\tau 1_{\{\sigma < n\} \cap A}] = E[\limsup_m X_{\tau \land m} 1_{\{\sigma < n\} \cap A}] \ge \limsup_m E[X_{\tau \land m} 1_{\{\sigma < n\} \cap A}]$.
- So $E[X_\sigma 1_{\{\sigma < n\} \cap A}] \le E[X_{\tau} 1_{\{\sigma < n\} \cap A}]$.
- Now take $n \to \infty$, by (**MCT**), $\forall A \in \F_\sigma: E[X_\sigma 1_A] \le E[X_\tau 1_A]$.

Suppose $(X_n)$ is **adapted** and $E|X_n| < \infty$. Then $(X_n)$ is a martingale iff $E[X_\tau] = E[X_0]$ for all **bounded** stopping time $\tau$.

- $\to$ direction follows from above.
- $\leftarrow$ direction:
  - $\forall k \in \N: E[X_k] = E[X_0]$.
  - Suppose $n \le m \in \N$ and $A \in \F_n$. Define $\tau = n 1_A + m 1_{A^c}$ which is a bounded stopping time. Then $E[X_\tau] = E[X_n 1_A] + E[X_m 1_{A^c}] = E[X_0]$.
  - $E[X_m 1_A] = E[X_m] - E[X_m 1_{A^c}] = E[X_m] - E[X_\tau] + E[X_n 1_A] = E[X_n 1_A]$.
  - So $E[X_m | \F_n] = X_n$. So $(X_n)$ is an $(\F_n)$-martingale.

Suppose $(X_n)$ is an $(\F_n)$-submartingale. Suppose $(\tau_n)$ is a sequence of **increasing bounded stopping times**. Then $(X_{\tau_n})$ is an $(\F_{\tau_n})$-submartingale.

- Suppose $n \le m \in \N$. Then $X_{\tau_n} \le E[X_{\tau_m} | \F_{\tau_n}]$.

##### Optional skipping

 Suppose $(\Omega, \F, (\F_n), \N, P)$ is a filtered space. Suppose $(X_n)$ is a **submartingale**. Let $(H_n)$ be **$(\F_n)$-adapted** with values in $\{0, 1\}$.

Then $Y_n := X_0 + (H \cdot X)_n$ is a **$(\F_n)$-submartingale** as $H_n$ is binary. And $E[Y_n] \le E[X_n]$.

- $X_0$ is fixed and $(H \cdot X)_n$ is a submartingale.
- $E[Y_n] \le E[X_n]$.
  - $E[X_0] = E[I_0]$ by definition.
  - Now proceed with induction, suppose $0 \le i \le k$ cases are proved.
  - $X_{k + 1} - Y_{k + 1} = X_{k + 1} - Y_k - H_k(X_{k + 1} - X_k) = (1 - H_k)(X_{k + 1} - X_k) + X_k - Y_k$.
  - $E[X_{k + 1} - Y_{k + 1} | \F_k] \ge E[X_k - Y_k | \F_k] = X_k - Y_k$.
  - So $E[X_{k + 1} - Y_{k + 1}] \ge E[X_k - Y_k] \ge 0$.

##### Optional stopping

 Suppose $(\Omega, \F, (\F_n), \N, P)$ is a filtered space. Suppose $(X_n)$ is a **submartingale**. Suppose $\tau$ is a stopping time. Then $(X_{n \land \tau})$ is a $(\F_n)$-submartingale.

- Define $H_n(\omega) = 1(n \le \tau(\omega))$. Then $Y_n := X_0 + (H \cdot X)_n = X_{n \land \tau}$.
- By (**Optional skipping**), $X_{n \land \tau}$ is a $(\F_n)$-sumbartingale.
  - Since $\F_{\tau \land n} \le \F_n$ and $(X_{n \land \tau})$ is adapted to $(\F_{\tau \land n})$. $(X_{n \land \tau})$ is $(\F_{n \land \tau})$-submartingale.
- By (**Optional skipping**), $E[X_{n \land \tau}] \le E[X_n]$.

##### Uniformly integrable martingale

 Suppose $(\Omega, \F, (\F_n), \N, P)$ is a filtered space. Suppose $(X_n)$ is a **uniformly integrable $(\F_n)$-martingale**.

Then the family $\T = (X_\tau: \tau \text{ is finite stopping time})$ is **uniformly integrable**.

- By (**Scaled integrable**) there exists $f: [0, \infty) \to [0, \infty)$ convex and increasing with $\lim_{x \to \infty} f(x) / x = \infty$. And $\sup_n E[f|X_n|] = L < \infty$.
- Define $g: \R \to [0, \infty)$ as $g(x) = f(\abs{x})$, then $g$ is convex.
- Suppose $\tau$ is a **finite** $(\F_n)$-stopping time. By (**Optional sampling**) $E[X_n | \F_{\tau \land n}] = X_{\tau \land n}$.
- $E[f|X_\tau|1_{\tau \le n}] = E[g(X_\tau) 1_{\tau \le n}] = E[g(X_{\tau \land n}) 1_{\tau \le n}] = *$.
- $* = E[g(E[X_n | \F_{\tau \land n}]) 1_{\tau \le n}] \le E[E[g(X_n)| \F_{\tau\land n}] 1_{\tau \le n}] = E[g(X_n) 1_{\tau \le n}] = E[f|X_n| 1_{\tau \le n}]$.
- Now take $n \to \infty$, by (**MCT**), $E[f|X_\tau|] \le L$. So $\T$ is uniformly integrable.

##### Upcrossing

 Suppose $(X_n)_{n \in \I}$ is a $(\F_n)$-submartingale. Suppose $-\infty < a < b < \infty$.

Suppose $J = \{1, \cdots, N\} \subseteq I$. Define $U_{ab}^N$ as the numer of upcrossings of $(a, b)$ by $(X_n)$ as following:

- Let $T_1(\omega)$ be the first time in $J$ where $X_{T_1}(\omega) \le a$.
- Let $T_2(\omega)$ be the first time after $T_1$ in $J$ where $X_{T_2}(\omega) \ge b$.
- Define $T_3 < T_4 < \cdots$ similarly. Set $T_k = \infty$ when the condition can not be satisfied.
- Suppose $T_m < \infty$ and $T_{m + 1} = \infty$. Define $U^N_{ab} = \lfloor m / 2 \rfloor$.

First consider the case $\forall j \in J:X_j \ge 0$, and $a = 0$. $bE[U^N_{ab}] \le E[X_N]$

- Let $(\epsilon_n)_{n = 1}^N$ be indicators adapted to $(\F_n^X)$.
  - $\epsilon_n(\omega) = 1$ when $T_{2k - 1}(\omega) \le n < T_{2k}(\omega)$.
  - $\epsilon_n (\omega) = 0$ otherwise.
  - Notice that $\epsilon_n(\omega)$ only depends on $X_1, \ldots, X_n$.
- Define $Y_1 = X_1$ and $Y_{n + 1} = Y_n + \epsilon_n (X_{n + 1} - X_n)$ for $n \le N - 1$.
- Intuitively, $Y_N$ is summing the total distance of upward crossing movement.
- Now apply (**Optional skipping**), $E[U^N_{ab}] \le E[Y_N]/b \le E[X_N] / b$.

Notice that $(U_{ab}^n)$ is adapted to $(\F_n)$, nonnegative and increases as $n \uparrow \infty$. Define $U_{ab} = \lim_{N \to \infty} U_{ab}^N$. $U_{ab} \in \L(\Omega \to [0, \infty], \F, P)$.

Now consider the general case. Since $X_j \le a \iff X_j - a \le 0 \iff (X_j - a)^+ = 0$. And $X_j \ge b \iff (X_j - a)^+ \ge (b - a)$. Also $(X_j - a)^+$ remains a **submartingale**. So
$$
(b - a)E[U^N_{ab}] \le E[(X_N - a)^+]
$$
##### Submartingale convergence

 Suppose $(\Omega, \F, P)$ is a probability space. Suppose $(X_n)_{n \in \I}$ is a $(\F_n)$-submartingale. If $\sup_n E[X_n^+] < \infty$ there exists $X_\infty \in \L^1(\Omega \to \R, \F, P)$ and $X_n \to X_{\infty}$ $P$.a.e.

- First we show that $X_n$ converge essentially pointwise in $\bar \R$.
  - Consider $O_{a, b} = \left\{\omega \in \Omega: \liminf _{n \rightarrow \infty} X_{n}(\omega)<a<b<\limsup _{n \rightarrow \infty} X_{n}(\omega)\right\}$.
  - Let $O = \cup_{a, b \in \Q, a < b} O_{a, b}$. Suppose $P(O) > 0$, then $E[U_{ab}] = \infty$.
  - But $E[U_{ab}^n] \le (b - a)^{-1}E[(X_n - a)^+] \le (b - a)^{-1}[\sup_nE[X_n^+] + a^-] = B < \infty$.
  - Contradiction! $P(O) = 0$.
- Define the limit of $X_n$ as $X_{\infty} \in L(\Omega \to \bar \R, \F)$. We further claim $X_\infty \in L^1(\Omega \to \bar \R, P)$.
  - $|X_n| = 2X^+_n - X_n$. $E|X_n| = 2E[X_n^+] - E[X_n] \le 2 \sup_n E[X_n^+] - E[X_1]$.
  - So $E|X_n|$ is uniformly bounded. $E|X_{\infty}| \le \liminf_n E|X_n| < \infty$.

