### Continuous Time Martingales

(**Brownian Martingales**)

Suppose $(\Omega, \F, P)$ is a probability space. Suppose $(B_t)$ is a standard BM with **natural filtration** $(\F_t)$.

- $(B_t)$ is a $(\F_t)$-martingale. As $E[B_t | \F_s] = E[B_t - B_s + B_s | \F_s] = B_s$.
- $(B_t^2 - t)$ is a martingale. As $E[B_t^2 - t | \F_s] = E[(B_t - B_s + B_s)^2 - t| \F_s] =\cdots = B_s^2 - s$.
- For $u \in \R$, $(e^{uB_t - tu^2/2})$ is a martingale. As $E[e^{u B_t}|\F_s] = E[e^{u(B_t - B_s + B_s)}|\F_s] = e^{u^2s/2}e^{uB_s}$.

(**Levy's backward convergence**)

Suppose $(\Omega, \F, P)$ is a probability space. And $Y \in \L^1(\Omega \to \R, P)$. Let $\G_0 \ge \G_1 \ge \ldots$ a decreasing sequence of sub-$\sigma$-algebras. If we set $\G_\infty := \cap_{j = 1}^\infty \G_j$, then $E[Y | \G_j] \to E[Y | \G_\infty]$ essentially pointwise and in $\L_1$. ==TODO==.

(**Martingale Characteristic**)

Suppose $(\Omega, \F, (\F_n), \N, P)$ is a filtered space.

Suppose $(X_n)$ is a adapted real process. The following are equivalent by reviewing **discrete martingale** theory:

1. $(X_n)$ is a $(\F_n)$-martingale.
2. (**Doob**) For all bounded stopping times $\tau$, $X_\tau \in \L^1(\Omega \to \R, P)$ and $E[X_\tau] = E[X_0]$.
   - $(1 \leftrightarrow 2)$ see discrete time (Optional sampling).
3. (**Optional sampling**) For all bounded stopping times $\sigma, \tau$ where $\sigma \le \tau$, $X_{\tau} \in \L^1(\Omega \to \R, P)$ and $E[X_\tau | \F_\sigma]  =X_\sigma$.
   - $(1 \to 3)$ see discrete time (Optional sampling).
   - $(3 \to 2)$ just take $\sigma = 0$.
4. (**Optional stopping**) For all stopping times $\tau$, $(X_{\tau \land n})$ is an $(\F_n)$-martingale.
   - $(4 \to 1)$ just take $\tau = +\infty$.
   - $(1 \to 4)$ see discrete time (Optional stopping).

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered probability space. Suppose $(X_t)$ is a **adapted** process that is **a.s. right-continuous**. The following are equivalent:

1. $(X_t)$ is a $(\F_t)$-**martingale**.
2. (**Doob**) For all **bounded** stopping times $\tau$, $X_\tau \in \L^1(\Omega \to \R, P)$ and $E[X_\tau] = E[X_0]$.
   - $(1 \to 2)$. Since $\tau$ is a **bounded stopping time**, there exists $T' \in (0, T]$ and $\tau(\omega) \le T'$.
     - Consider dyadic partitioning of $[0, T']$, $(s_{n, k} = kT' / 2^n)$ for some fixed $n \in \N^+$.
     - Define $\tau_n$ as the upper dyadic approximation of $\tau$.
     - $(X_{s_{n, k}})_{k = 0}^{2^n}$ is now a discrete-time $(\F_{s_{n, k}})$-**martingale**.
     - Then for all $n > 0$, $X_{\tau_n} \in \L^1(\Omega \to \R, P)$ and $E[X_{\tau_n}] = E[X_0]$.
     - Let $\G_n = \F_{\tau_n}$ and $\G_\infty = \cap_{n = 1}^\infty \G_n$. Then $\G_n \downarrow \G_\infty$.
     - By discrete-time (**Optional sampling**), $X_{\tau_n} = E[X_{T'} | \G_n]$.
     - By (**Levy's backward convergence**), $X_{\tau_n} \to E[X_{T'} | \G_\infty]$ in $\L_1$.
     - Since $\tau_n \downarrow \tau$ pointwise, and $X_t$ is right-continuous. $X_{\tau_n} \to X_\tau$ $P$.a.s.
     - By uniqueness of convergence, $X_\tau \in L^1(\Omega \to \R, P)$ and $E[X_\tau] = E[X_{T'}] = E[X_0]$.
   - $(2 \to 1)$ just take $\tau = t$.
3. (**Optional sampling**) For all **bounded** stopping times $\sigma, \tau$ where $\sigma \le \tau$, $X_{\tau} \in \L^1(\Omega \to \R, P)$ and $E[X_\tau | \F_\sigma] = X_\sigma$.
4. (**Optional stopping**) For all stopping times $\tau$, $(X_{\tau \land t})$ is an $(\F_t)$-martingale.

Proof: ==TODO==

(**Doob**)

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered space. Suppose $(M_t)$ is a continuous $(\F_t)$-martingale. And $\tau$ is a.s. **finite** stopping time.

Suppose stopped process $(M_{\tau \land t})$ is bounded. Then $E[M_\tau] = E[M_0]$.

- Since $M_{\tau \land t}$ is a martingale and $(t \land \tau)$ is bounded, $E[M_{t \land \tau}] = E[M_0]$.
- $\lim_{t \to \infty} M_{t \land \tau} = M_\tau$ $P$.a.e. since $\tau$ is finite.
- Since $M_{t \land \tau}$ is bounded, by (**DCT**) $E[M_\tau] = E[\lim_{t \to \infty} M_{t\land \tau}] =\lim_{t \to \infty} E[M_{t \land \tau}] = E[M_0]$.

(**Hitting time**)

Suppose $(X_t)_{t \ge 0}$ is a **continuous** real stochastic process on $(\Omega, \F, P)$ adapted to $(\F_t)$. For $B \in \B(\R)$, define the **hitting time** $\tau_B = \inf\{t > 0: X_t \in B\}$.

- $\tau_B$ is a weakly stopping time if $B$ is **open**.
  - $\{\tau_B < t\} = \cup_{\gamma \in \Q \cap [0, t)} \{X_\gamma \in B\} \in \F_t$.
- $\tau_B$ is a stopping time if $B$ is **closed**.
  - $\{\tau_B \le t\} = \cup_{\gamma \in \Q \cap [0, t]}\cap_{n} \{\operatorname{dist}(X_\gamma, B) < 1/n\} \in \F_t$.

(**Strong Markov property of Brownian Motion**)

Suppose $(\Omega, \F, (\F_t), [0, \infty), P)$ is a filtered space with right-continuous filtration $(\F_t)$. Suppose $(B_t)$ is adapted to and has independent increments with respect to $(\F_t)$.

Let $(\tau_n)_{n = 1}^\infty$ be the **upper dyadic approximation** of $\tau$. Then

- $B_{\tau_n} \in \F_{\tau_n}$.
    - Suppose $U \in \B(\R)$.
    - Notice that $\{B_{\tau_n} \in U\} \cap \{\tau_n = 2^{-n} k\} \in \F_{2^{-n}k}$.
    - Therefore $\{B_{\tau_n} \in U\} \cap \{\tau_n \le t\} \in \F_t$ for any $t \ge 0$.
- $B_\tau \in \F_\tau$.
    - Notice that $B_\tau = \lim_{n \to \infty} B_{\tau_n}$. Suppose $U \in \B(\R)$.
    - Then $\{B_\tau \in U\} = \lim_{n \to \infty} \{B_{\tau_n} \in U\} = \cap_{k = 1}^\infty \cup_{n = k}^\infty \{B_{\tau_n} \in U\} \in \cap_{n = 1}^\infty \F_{\tau_n} = \F_\tau$.

Now let $\tau$ be a **finite stopping time**. Then $(B_{t + \tau} - B_\tau)_{t \ge 0}$ is a **standard BM** independent of $\F_\tau$.

- Suppose $A \in \F_\tau$ and $F: \R^n \to \R$ is **continuous bounded**. We need to show $$
  E[1_A \cdot F(B_{t_1 + \tau} - B_\tau, \cdots ,B_{t_{n} + \tau} - B_\tau)] = P(A) E[F(B_{t_1 + \tau}, \cdots ,B_{t_{n} + \tau})] \quad (**)$$
- We can first show $**$ replacing $\tau$ with $\tau_n$. Then take the limit $n \to \infty$. $$
  E[1_A \cdot F(B_{t_1 + \tau_n} - B_{\tau_n}, \cdots)] = \sum_{k = 1}^\infty E[1_A 1_{\tau_n = 2^{-n}k} F(B_{t_1 + \tau_n} - B_{\tau_n}, \cdots)] =^* P(A) F(\cdots)$$
  where $=^*$ is true since $A \in \F_\tau \subseteq \F_{\tau_n}$, so $A \cap \{\tau_n = 2^{-n} k\} \in \F_{2^{-n}k}$.

So $(B_t)$ has strong independent increment property with respect to $(\F_t)$.

(**BM Recurrence and Transience I**) Suppose $(B_t)_{t \ge 0}$ is a standard BM adapted to filtration $(\F_t)$.

Consider $a, b > 0$ and $\tau_a, \tau_{-b}$ are hitting times. Define $\tau = \tau_a \land \tau_{-b}$ is the time of escaping $[-b ,a]$.

- $P(\tau < \infty) = 1$. So $\tau$ is a.s. finite.
  - Break down $B_t$ into $\Delta_n = B_{n} - B_{n - 1}$.
  - Then $B_n = \sum_{i = 1}^n \Delta_n$. $P(\tau < \infty) \le P(\cap_n |\Delta_n| < (a + b)) = 0$.
- $P(B_\tau = a) = b / (a + b)$. And $P(B_\tau = -b) = a / (a + b)$.
  - $E[B_\tau] = aP(B_\tau = a) + b(1 - P(B_\tau = a)) = 0$. Solve this to get the result.
- $E[\tau] = ab < \infty$.
  - Recall that $M_t = B_t^2 - t$ is a martingale. Actually $E[M_\tau] = E[M_0] = 0$.
    - Hint: $E[M_{t \land \tau}] = E[B_{t \land \tau}^2 - t \land \tau] = E[B_{t \land \tau}^2] - E[t \land \tau]$.
    - Notice that $B_{t \land \tau}^2 \to B_\tau^2$ $P$.a.e. and $E[B_\tau^2] < \infty$. Apply (DCT).
    - Notice that $t \land \tau \uparrow \tau$ $P$.a.e. Apply (MCT).
  - Further $E[B_\tau^2 -\tau] = a^2 b / (a + b) + b^2a / (a + b) - E[\tau]$. So $E[\tau] = ab$.
- $\tau_a \uparrow \infty$ pointwise as $a \uparrow \infty$.
- $E[\tau_a] = \infty$.
  - Since $\lim_{b \to -\infty} E[\tau_a \land \tau_{-b}] = +\infty$. Now apply (MCT).

