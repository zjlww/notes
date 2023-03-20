#### Stochastic Integrals

##### Stochastic integral for $C^1$ functions

Suppose $g \in C^1([0, T] \to \R)$, and $g(0) = g(T) = 0$. Then define
$$
\int_{0}^T g(t) \dd B_t := -\int_0^T g'(t) B_t \dd t
$$
According to Tonelli's theorem, for some $C > 0$,
$$
\int_{\Omega}\int_0^T |B_t(\omega)| \dd t \dd P(\omega) = \int_0^T \int_{\Omega} |B_t(\omega)| \dd P(\omega) \dd t = C \int_0^T t \dd t = \frac{C}{2} T^2 < \infty
$$
Now apply Fubini's theorem,
$$
E\s{\int_0^T g(t) \dd B_t} = \int_{\Omega} \int_{[0, T]} g'(t) B_t(\omega) \dd t \dd P(\omega) = \int_0^T E[B_t(\omega)] \dd t = 0
$$
By repeated application of integration by parts, we have
$$
\begin{aligned}
E\s{\int_0^T g(t) \dd B_t}^2 & = E\s{\int_0^T g'(t) B_t \dd t \int_0^T g'(s) B_s \dd s}\\
& = \int_0^T \int_0^T g'(t) g'(s) E\s{B_t B_s} \dd s \dd t = \int_0^T \int_0^T g'(t) g'(s) \min(s, t) \dd s \dd t\\
& = \int_0^T g'(t) \p{\int_0^t sg'(s) \dd s + \int_t^T t g'(s) \dd s} \dd t\\
& = \int_0^T g'(t) \p{tg(t) - \int_0^t g(s) \dd s - t g(t)}\dd t\\
& = \int_0^T g'(t) \p{-\int_0^t g(s) \dd s} \dd t = \int_0^T g^2(t) \dd t\\
\end{aligned}
$$

##### Stochastic integral for $\L^2$ functions.

Suppose $g \in L^2([0, T] \to \R)$. There exist $(g_n)_{n = 1}^\infty \subseteq C^1([0, T] \to \R)$ such that $g_n(0) = g_n(T) = 0$ and $g_n \to g$ in $\L_2$.

Notice that
$$
E\s{\int_0^T g_m(t) \dd B_t - \int_0^T g_n(t) \dd B_t}^2 = \int_0^T (g_m(t) - g_n(t))^2 \dd t = \n{g_m - g_n}_2^2
$$
Therefore $\int_0^T g_n(t) \dd B_t$ is a Cauchy sequence in $L^2(\Omega \to \R)$, therefore is convergent. Define

$$
\int_0^T g(t) \dd B_t := \lim_{n \to \infty} \int_0^T g_n(t) \dd B_t
$$

##### Spaces of random processes

Suppose $(\Omega, \F, (\F_t), T = [0, T], P)$ is a filtered probability space.

- Define $\bM(0, T) := \L(\Omega \times [0, T]\to \R, \F \times \B[0, T])$.

  - Define $\bM^p(0, T) \subseteq \bM(0, T)$ as $\bM^p(0, T) := \L^p(\Omega \times [0, T] \to \R, \F \times \B[0, T], P \times m)$ for $p \in [1, \infty)$.
  - $\bM^p(0, T)$ are vector spaces over $\R$ with semi-norm $\n{X_t}_p =\n{X_t}:= E\s{\int_0^T \abs{X_t(\omega)}^p \dd t}^{1/p}$.

- Define $\bA(0, T) \subseteq \bM(0, T)$ as the space of all processes adapted to $(\F_t)$.

- Define $\bL(0, T) \subseteq \bA(0, T)$ as the space of all real-valued progressively measurable stochastic processes.

- Define $\bS(0, T)\subseteq \bL(0, T)$ as the space of all simple processes.
  $$
  \bS(0, T) := \c{
  (X_t) \in \bL(0, T): X_t = \sum_{j = 0}^{n - 1} Y_j 1_{(t_j, t_{j + 1}]}(t), (t_j)_{j = 0}^n \in P[0, T], Y_j \in \L(\Omega \to \R, \F_{t_j},P)
  }
  $$

  - For $(X_t) \in \bS(0, T)$, we have $(X_t) \in \bS^p(0, T)$ if and only if all $Y_j \in \L^p(P)$ in the above definition.

- 

##### Spaces of random processes

- Define $\V(T) < \L^2(0, T)$ containing $(X_t) \in \L^2(0, T)$ **adapted** to $(\F_t)$.
  - $\V(T)$ contains adapted, square-integrable processes.
- Define $\W(T) < \L(0, T)$ containing $(X_t) \in \L(0, T)$ **adapted** to $(\F_t)$ and $\int_0^T X_t^2 dt < \infty$ pathwise.
  - $\W(T)$ contains adapted, pathwise square-integrable processes.
  - For $(X_t) \in \W(T)$, $\|(X_t)\|_2^2 = E[\int_0^T X_t^2 dt] = \int_0^T E[X_t^2] dt < \infty$ by (**Tonelli**).
- Define $\A(T) < \L(0, T)$ containing $(X_t) \in \L(0, T)$ **adapted** to $(\F_t)$ and $\int_0^T |X_t| dt < \infty$ pathwise.
  - $\A(T)$ contains adapted, pathwise integrable processes.
- Define $\mathcal B(T) < \V(T)$ containing $(X_t) \in \V(T)$ with uniformly **bounded** values.
  - $\mathcal B(T)$ contains adapted, uniformly bounded processes.
- Define $\M(T) < \V(T)$ containing $(M_t) \in \V(T)$ that are **martingales**.
  - $\M(T)$ contains square-integrable martingales.
- Define $\V_c(T),\mathcal B_c(T), \M_c(T)$ as the subspaces with **continuous** paths.
  - The important standard Brownian motion $(B_t)$ is in $\M_c(T)$ when $(\F_t)$ is the natural filtration.
