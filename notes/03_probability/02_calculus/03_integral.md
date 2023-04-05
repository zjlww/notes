#### Stochastic Integrals

> Øksendal, B. (1987). Stochastic differential equations : an introduction with applications. *Journal of the American Statistical Association, 82*, 948.

##### Spaces of random processes

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space.

- Define $\bM(0, T) := \L(\Omega \times [0, T]\to \R, \F \times \B[0, T])$.
- Define $\bA(0, T) \subset \bM(0, T)$ as the subspace of all processes adapted to $(\F_t)$.
- Define $\bL(0, T) \subset \bA(0, T)$ as the subspace of all progressively measurable stochastic processes.
- Define $\bS(0, T)\subset \bL(0, T)$ as the subspace of all simple processes.
  $$
  \bS(0, T) := \c{
  (X_t) \in \bL(0, T): X_t = Y_0 1_{\c{0}}(t) +\sum_{j = 0}^{n - 1} Y_j 1_{(t_j, t_{j + 1}]}(t), (t_j)_{j = 0}^n \in P[0, T], Y_j \in \L(\Omega \to \R, \F_{t_j},P)
  }
  $$
  - For $(X_t) \in \bS(0, T)$, we have $(X_t) \in \bS^p(0, T)$ if and only if all $Y_j \in \L^p(P)$ in the above definition.

For further restrictions on the classes of processes, we make following definitions:

- Add superscript $p \in [1, \infty)$ to denote restriction to processes with finite $\L^p$ norms.
  - e.g. $\bM^p(0, T) := \L^p(\Omega \times [0, T] \to \R, \F \times \B[0, T], P \times m)$.
  - They are real vector spaces with semi-norm
    $$
    \n{X_t}_p =\n{X_t}:= E\s{\int_0^T \abs{X_t(\omega)}^p \dd t}^{1/p}
    $$
- Add subscript $b$ to assert that the all paths are uniformly bounded by some $B > 0$.
- Add subscript $m$ to assert that the process is a martingale with regard to $(\F_t)$.
- Add subscript $c$ to assert that paths are continuous in $t$ almost surely.
- Add subscript $[p]$ for $p \ge 1$ to assert that $E[|X_t|^p] < \infty$ for all $t \in [0, T]$.
- Add subscript $p \ge 1$ to assert that $\int_0^T |X_t|^p \dd t < \infty$ almost surely.
- Add subscript $(m \times n)$ to assert that the process has values in $\R^{m \times n}$.

##### Non-anticipating processes

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space.

Let $(B_t) \in \bL^2_{c, m, [2]}(0, T)$ be a **standard Brownian motion** and $(X_t)$ is a real-valued random process.

$(X_t)$ is called not anticipating with respect to $(B_t)$ if $\boxed{\forall t \in [0, T]:\sigma(X_{\le t}) \perp (B_{t + s} - B_t)_{s \ge 0}}$.

Notice that when $\F_t = \sigma(B_{\le t})$ this is automatically true.

##### A collection of dense subspace results

The following dense subspace results are important in our proof. For non-anticipating processes, we require the approximating sequence to be non-anticipating as well. This can be achieved that the approximation at time $t$ only depends on $\le t$.

$\bS^p(0, T)$ is dense in $\bA_{c, [p]}^p(0, T)$ for $p \ge 1$.

- Consider any $(X_t) \in \bA^p_{c, [p]}(0, T)$.
- Suppose $P_n = (t_{n, j})_{j = 0}^{n_j}$ is **the shrinking dyadic** partition sequence in $P[0, T]$.
- For each $n$, define $(X_t^{(n)})$ as $X_0 1_{\c{0}}(t) + \sum_{j = 0}^{n_j - 1} X_{t_{n, j}}1_{(t_{n, j}, t_{n, j + 1}]}(t)$.
- It is easy to see that $(X_t^{(n)}) \subseteq \bS^p(0, T)$, and that $(X_t^{(n)} - X_t)^p \downarrow 0$ monotonically pointwise in $t$.
- By dominated convergence theorem, $(X_t^{(n)}) \to (X_t)$ in $\L_p$ norm.

$\bA_{c, b}^2(0, T)$ is dense in $\bA_b^2(0, T)$. ==TODO== (see Øksendal p.28).

$\bA_b^p(0, T)$ is dense in $\bA^p(0, T)$ for $p \ge 1$.

- Consider any $(X_t) \in \bA^p(0, T)$.
- Define the process $(X_t^{(n)})$ as truncation of $(X_t)$ into range $[-n, n]$.
- By dominated convergence, theorem $(X_t^{(n)}) \to (X_t)$ in $\L_p$.

Note that $X_t^{(n)} \in \sigma(X_{\le t})$ is always guaranteed. This is essential for the following proof.

##### Integrate $\bS^2(0, T)$ with integrators in $\bL_{c, m, [2]}^2(0, T)$

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space.

Notice that the 1D standard Brownian motion $(B_t) \in \bL_{c, m, [2]}^2(0, T)$.

Suppose $(M_t) \in \bL_{c, m, [2]}^2(T)$ and $(X_t), (Z_t) \in \bS^2(0, T)$.

- We will assume $X_t=Y_01_{\c{0}}(t) + \sum_{j = 0}^nY_j1_{(t_j,t_{j+1}]}(t)$ for some partition $(t_j)_{j = 0}^n \in P[0, T]$.

For $t \in [0, T]$, define random process $I_t$ as the following:
$$
(X \cdot M)_t = I_t = \int_0^t X_s dM_s := \sum_{j = 0}^{n - 1} Y_j(M_{t \land t_{j + 1}} - M_{t \land t_j})
$$

- $(I_t)$ is continuous and adapted to $(\F_t)$. Which is clear from the definition.
- $\forall t \in [0, T]: I_t \in \L^1(\Omega \to \R, \F_t, P)$. By triangle inequality and Hölder's inequality:
  $$
  E|I_t| \le \sum_{j = 0}^{n - 1} E|Y_j(M_{t \land t_j} - M_{t \land t_{j + 1}})| \le \sum_{j = 0}^{n - 1} \sqrt{E[Y_j^2] E[(M_{t \land t_j} - M_{t \land t_{j + 1}})^2]} < \infty
  $$
- $(I_t)$ is a **martingale** on the filtered space.
  - Consider each term, for simplicity denoted by  $E[Y(M_b - M_a) | \F_s]$.
    - Suppose $a < b \le s$, $E[Y(M_b - M_a)|\F_s] = Y(M_b - M_a)$.
    - Suppose $a < s < b$, $E[Y(M_b - M_a)|\F_s] = Y(M_s - M_a)$.
    - Suppose $s \le a < b$, $E[\cdots] = 0$.
- $I_t$ has **zero mean** for all $t \in [0, T]$.
  - $E[(X \cdot M)_t] = E[E[(X \cdot M)_t | \F_0]] = E[(X \cdot M)_0] = 0$.
- $(X \cdot M)_t$ is **linear** in the integrand.
  - $(a X \cdot M)_t = a(X \cdot M)_t$ and $((X + Z) \cdot M)_t = (X \cdot M)_t + (Z \cdot M)_t$.

##### Itô stochastic integral of $\bS^2(0, T)$ processes

Suppose $(\Omega, \F, (\F_t), T = [0, T], P)$ is a complete filtered probability space.

Consider **standard Brownian motion** $(B_t)$ and **non-anticipating** process $(X_t) \in \bS^2(0, T)$ 

- We will assume $X_t = Y_j 1_{(t_j, t_{j + 1}]}(t)$ for some partition $(t_j)_{j = 0}^n \in P[0, T]$.

Let $I_t = (X \cdot B)_t$. All the properties in previous discussion are true. $(I_t) \in \bL_{c, m}^1(0, T)$.

We have $\|I_T\|_2 = \|(X_t)\|_2$, which is called the **Itô isometry**.

- First notice that $Y_j (B_{t_{j + 1}} - B_{t_j}) \in \L^2(P)$. So $Y_j Y_i (B_{t_{i + 1}} - B_{t_i}) \in \L^1(P)$.
  $$
  E\s{Y_j^2(B_{t_{j + 1}} - B_{t_j})^2} = E\s{Y_j^2E\s{(B_{t_{j + 1}} - B_{t_j})^2 \mid \F_{t_j}}} = E[Y_j^2](t_{j + 1} - t_j) < \infty
  $$
- Therefore by expectation of the product of independent integrable variables, for $i < j$ we have
  $$
  E\s{Y_{j} Y_{i}(B_{t_{j+1}}-B_{t_{j}})(B_{t_{i+1}}-B_{t_{i}})} = E\s{Y_{j} Y_{i}(B_{t_{i+1}}-B_{t_{i}})}E\s{B_{t_{j+1}}-B_{t_{j}}} = 0
  $$
- Now expand $\n{I_T}^2_2$ as following
  $$
  \n{I_T}_2^2 = E[I_T^2] = E\s{\sum_{j = 0}^{n - 1} Y_j(B_{t_{j + 1}} - B_{t_{j}})}^2 = E\s{\sum_{j = 0}^{n - 1} Y_j^2(B_{t_{j + 1}} - B_{t_j})^2 + 2 \sum_{i < j}Y_{j} Y_{i}(B_{t_{j+1}}-B_{t_{j}})(B_{t_{i+1}}-B_{t_{i}})}
  $$
- Therefore
  $$
  \n{I_T}_2^2 = E[I_T^2] = \sum_{j = 0}^{n - 1} E[Y_j^2](t_{j + 1} - t_j) = \int_0^T E[X_t^2] \dd t = \n{(X_t)}_{2}^2
  $$
- In this case $(I_t) \in \bL_{c, m, [2]}^2(0, T)$.

##### Doob's martingale inequality ==TODO==

Suppose $(M_t)$ is a martingale such that $t \to M_t(\omega)$ is almost surely continuous. Then for $p \ge 1$, $T > 0$ and $\lambda > 0$ we have
$$
P\s{\sup_{t \in [0, T]} \abs{M_t} \ge \lambda} \le \frac{1}{\lambda^p} E \abs{M_T}^p
$$

##### Itô stochastic integral of $\bA^2(0, T)$

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space.

Consider **standard Brownian motion** $(B_t)$ and **non-anticipating** process $(X_t)\in \bA^2(0, T)$.

Define $I_T = (X \cdot B)_T = \int_0^T X_t \dd B_t$ as following

- Construct non-anticipating sequence $(X_t^{(n)}) \in \bS^2(0, T)$ such that $(X_t^{(n)}) \to (X_t)$ in $\L_2$.
- $I_T^{(n)}$ is a Cauchy sequence in $L^2(\Omega \to \R, \F_T, P)$. Since $\n{I_t^{(n)} - I_t^{(m)}} = \n{(X_t^{(n)}) - (X_t^{(m)})}$.
- So $I_T^{(n)}$ **converges** to $I_T \in L^2(\Omega \to \R, \F_T, P)$ in $\L_2$ norm.
- The limit does not depends on the approximating sequence $(X_t^{(n)})_{n=1}^\infty$.
  - Suppose $J_T^{(n)}$ is the result of another integral sequence by $(\what X_t^{(n)})_{n = 1}^\infty$.
  - Then $\n{I_T^{(n)} - J_T^{(n)}}$ goes to zero due to
    $$
    \norm{I_T^{(n)} - J_T^{(n)}} = \norm{\p{X_t^{(n)} - \what X_t^{(n)}}} \le \norm{\p{X_t^{(n)}} - \p{X_t}} + \norm{\p{\what X_t^{(n)}} - (X_t)} \to 0
    $$
    

The defined integral is linear:

- $(a X \cdot B)_T = a(X \cdot B)_T$ for $a \in \R$. Since $(aX_t^{(n)}) \to (aX_t)$ in $\L_2$.
- $((X + Y) \cdot B)_T = (X \cdot B)_T + (Y \cdot B)_T$.
  - Suppose $(X_t^{(n)}) \to (X_t)$ and $(Y_t^{(n)}) \to (Y_t)$ in $\L_2$, $(X_t^{(n)}+Y_t^{(n)}) \to (X_t + Y_t)$ in $\L_2$.

In $L^2(P)$ we have
$$
\int_0^T X_s \dd B_s = \int_0^a X_s \dd B_s + \int_a^T X_s \dd B_s
$$
Itô isometry still works, $\|I_T\|_2 = \|(X_t)\|_2$. Since
$$
\|(X_t)\|\leftarrow \|(X_t^{(n)})\| = \|I_T^{(n)}\| \to \|I_T\|, \quad n \to \infty
$$
$E[I_T] = 0$. Since convergence in $\L_2$ implies convergence in mean and $E[I_T^{(n)}] = 0$.

Let $(Y_t) \in \bA^2(0, T)$, let $J_T = (Y \cdot B)_T$ then
$$
E \s{\int_0^T Y_t \dd B_t \int_0^T X_t \dd B_t} = E \s{\int_0^T X_t Y_t \dd t}
$$

- Clearly $(X_t + Y_t) \in \bA^2(0, T)$. Now following Itô isometry:
  $$
  \begin{aligned}
  E\s{\int_0^T X_t \dd B_t + \int_0^T Y_t \dd B_t}^2 & =E\s{\int_0^T(X_t + Y_t) \dd B_t}^2 = \int_0^T E[(X_t + Y_t)^2]\dd t\\
  E\s{\int_0^T X_t \dd B_t}^2 + E\s{\int_0^T Y_t \dd B_t}^2 + 2 E\s{\int_0^T X_t \dd B_t \int_0^T Y_t \dd B_t}&= \int_0^T (E[X_t^2] + E[Y_t^2] + 2E[X_t Y_t]) \dd t
  \end{aligned}
  $$
- Now cancellation on both sides gives the desired result.

Suppose $(X_t^{(n)})_{n = 1}^\infty \subset \bA^2(0, T)$ and $(X_t^{(n)}) \to (X_t)$ in $\L_2$. Then $(X^{(n)} \cdot B)_T \to (X \cdot B)_T$ in $\L_2$.

##### Itô stochastic integral of $\bA^2(0, T)$ processes with variable time

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space.

Consider **standard Brownian motion** $(B_t)$ and **non-anticipating** process $(X_t)\in \bA^2(0, T)$.

For all $t \in [0, T]$ define $I_t := \int_0^t X_s \dd B_s$. Then $(I_t)_{t \in [0, T]}$ is a stochastic process.

$(I_t)$ is a **martingale** with regard to $(\F_t)$. Consider any $0 \le s \le t \le T$.

- Recall that $L^2(P)$ is a Hilbert space. And that $E[I_t | \F_s]$ can be viewed as a linear projection.
- $I_t^{(n)} \to I_t$ in $\L_2$, therefore $E[I_t^{(n)}|\F_s] \to E[I_t | \F_s]$ in $\L_2$.
- But $E[I_t^{(n)} | \F_s] = I_s^{(n)}$ and $I_s^{(n)} \to I_s$ in $\L_2$.
- Therefore $E[I_t | \F_s] = I_s$.

Suppose $0 \le s \le t \le T$, we have
$$
E[I_s I_t] = E[I_s(I_t - I_s + I_s)] = E[I_s^2] + E[I_s E[I_t - I_s | \F_s]] = E[I_s^2] = \int_0^s E[X_t^2] \dd t
$$

There exists a **modification** of $(I_t)$ with almost surely continuous paths. (Proof by Øksendal)

- Pick a sequence of $(X_t^{(n)}) \subseteq \bS^2(0, T)$ converge to $(X_t)$ in $\L_2$. And define
  $$
  I_t^{(n)}(\omega) := \int_0^t X_s(\omega) \dd B_s(\omega)
  $$
- We have demonstrated that $\forall n \in \N^+: (I_t^{(n)}) \in \bL^2_{c, m, [2]}(0, T)$. Therefore $(I_t^{(n)} - I_t^{(m)}) \in \bL_{c, m, [2]}^2(0, T)$.
- By martingale inequality we have for any $\epsilon > 0$
  $$
  \begin{aligned}
  P\s{\sup_{0 \le t \le T} \abs{I_t^{(n)}(\omega) - I_t^{(m)}(\omega)} > \epsilon } \le \frac{1}{\epsilon^2} E\s{\abs{I_T^{(n)}(\omega) - I_T^{(m)}(\omega)}^2} = \frac{1}{\epsilon^2} E\s{\int_0^T \p{X_t^{(n)} - X_t^{(n)}}^2 \dd t}
  \end{aligned}
  $$
- As $m, n \to \infty$, the probability goes to zero.
- There exists a subsequence $(I_{t}^{(n_k)})$ where $n_k \uparrow \infty$ such that
  $$
  P\s{\sup_{0 \le t \le T} \abs{I_t^{(n_{k + 1})}(\omega) - I_t^{(n_k)}(\omega)} > 2^{-k} } < 2^{-k}
  $$
- By Borel-Cantelli lemma,
  $$
  \forall k \in \N, \exists K \in \N, \forall m > K: P\s{\sup_{0 \le t \le T} \abs{I_t^{(n_{m + 1})}(\omega) - I_t^{(m_k)}(\omega)} > 2^{-k} } = 0
  $$
- Therefore $(I_{t}^{(n_k)})$ is uniformly convergent on $[0, T]$ for essentially all $\omega \in \Omega$.
- Let $(J_t)$ be the limit of subsequence $(I_{t}^{(n_k)})$.
  - $\forall t \in [0, T]: P(J_t = I_t) = 1$ due to uniqueness of limit in $\L_2$.
  - $(J_t)$ has almost surely has continuous paths.
- We will always take some continuous modification as the result of the $\int_0^t X_s \dd B_s$.

Based on our discussion, we have $(I_t) \in \bL_{c, m, [2]}^2(0, T)$.
$$
\n{(I_t)}_2^2 = \int_0^T E[I_t^2] \dd t = \int_0^T \int_0^t E[X_s^2] \dd s \dd t \le \int_0^T \n{(X_t)}_2^2 \dd \tau = T \n{(X_t)}_2^2 < \infty
$$

##### Itô stochastic integral of $\bA_2(0, T)$ processes with variable time ==TODO==

The class $\bA^2(0, T)$ is overly restrictive, actually it is possible to generalize Itô stochastic integral to $\bA_2(0, T)$.

- The integral still has almost surely continuous path.
- Such integral may not be a martingale.
- Such integral may not have finite moments.

#### Wiener Integrals

##### Wiener integrals

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space.

Let $(B_t)$ be a **standard Brownian motion**. Suppose $f \in \L^2([0, T] \to \R, \B[0, T])$.

View $f(t, \omega) \in \bL^2(0, T)$ and define $\p{I_t} := \p{\int_0^t f(s)\dd B_s}$.

- There exists a sequence $f^{(n)}(t) \in \bS^2[0, T]$ such that $f^{(n)} \to f$ in $\L_2$.
- Define $\p{I^{(n)}_t} := \p{\int_0^t f^{(n)}(s) \dd B_s}$.
- $(I_t^{(n)})$ is a Gaussian process by definition of the integral.
- The covariance is given by $E[I_s I_t] = \cov(I_s, I_t) = \int_0^{t\land s} f(\tau)^2 d\tau$.
- Then $I_t$ is a Gaussian process as well. ==TODO==
  - Hint: consider a fixed set of time points $(t_j)_{j = 1}^m \in [0, T]$.

##### Wiener integrals for $C^1[0, T]$ functions

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a complete filtered probability space. Let $(B_t)$ be a **standard Brownian motion**.

Suppose $g \in C^1([S, T] \to \R)$, function $g$ can be viewed as a deterministic stochastic process.

Suppose $(t_{n, k})_{k = 0}^{m_n} \subseteq P[S, T]$ are a sequence of shrinking partitions on $[S, T]$. Then
$$
\begin{aligned}
\int_S^T g(t) \dd B_t & = \lim_{n \to \infty}\sum_{k = 1}^{m_n} g(t_{n, k - 1}) \p{B_{t_{n, k}} - B_{t_{n, k - 1}}}\\
& = \lim_{n \to \infty}\sum_{k = 1}^{m_n} \s{g(t_{n, k}) B_{t_{n, k}} - g(t_{n, k - 1}) B_{t_{n, k - 1}} + B_{t_{n, k}}(g(t_{n, k - 1}) - g(t_{n, k}))}\\
& = g(T) B_T - g(S)B_S - \lim_{n \to \infty} \sum_{k = 1}^{m_n} B_{t_{n, k}} g'(t^*_{n, k - 1}) (t_{n, k} - t_{n, k - 1}) ,\quad t_{n, k - 1}^* \in[t_{n, k - 1}, t_{n, k}]
\end{aligned}
$$

Therefore we have a nice pathwise integral result, which is consistent with our previous definitions.
$$
\int_S^T g(t) \dd B_t =  g(T) B_T - g(S) B_S - \int_S^T g'(t) B_t \dd t = g(T) B_T - \int_S^T g'(t) \p{B_t - B_S} \dd t
$$
