### Ito Integral

(**Spaces of random processes**)

Suppose $(\Omega, \F, (\F_t), T = [0, T], P)$ is a filtered probability space.
- Define $\L(T) = \L(\Omega \times [0, T]\to \R, \F \times \B[0, T])$.
- Define $\P(T) < \L(T)$ as $\P(T) = \L^2(\Omega \times [0, T] \to \R, \F \times \B[0, T], P \times m)$.
    - $\P(T)$ is a vector space over $\R$ with semi-norm $\|\cdot\|_2$. We will just denote this norm as $\|\cdot\|$.
- Define $\S(T) < \P(T)$ containing **simple processes adapted to $(\F_t)$**. $$
  \S(T) := \left \{
  (X_t): X_t = \sum_{j = 0}^{n - 1} Y_j 1_{(t_j, t_{j + 1}]}(t), (t_j)_{j = 0}^n \in P[0, T], Y_j \in \L^2(\Omega \to \R, \F_{t_j},P)
  \right \}$$
    - $\S(T)$ contains adapted, square-integrable simple processes.
- Define $\V(T) < \P(T)$ containing $(X_t) \in \P(T)$ **adapted** to $(\F_t)$.
    - $\V(T)$ contains adapted, square-integrable processes.
- Define $\W(T) < \L(T)$ containing $(X_t) \in \L(T)$ **adapted** to $(\F_t)$ and $\int_0^T X_t^2 dt < \infty$ pathwise.
    - $\W(T)$ contains adapted, pathwise square-integrable processes.
    - For $(X_t) \in \W(T)$, $\|(X_t)\|_2^2 = E[\int_0^T X_t^2 dt] = \int_0^T E[X_t^2] dt < \infty$ by (**Tonelli**).
- Define $\A(T) < \L(T)$ containing $(X_t) \in \L(T)$ **adapted** to $(\F_t)$ and $\int_0^T |X_t| dt < \infty$ pathwise.
    - $\A(T)$ contains adapted, pathwise integrable processes.
- Define $\mathcal B(T) < \V(T)$ containing $(X_t) \in \V(T)$ with uniformly **bounded** values.
    - $\mathcal B(T)$ contains adapted, uniformly bounded processes.
- Define $\M(T) < \V(T)$ containing $(M_t) \in \V(T)$ that are **martingales**.
    - $\M(T)$ contains square-integrable martingales.
- Define $\V_c(T),\mathcal B_c(T), \M_c(T)$ as the subspaces with **continuous** paths.
    - The important standard Brownian motion $(B_t)$ is in $\M_c(T)$ when $(\F_t)$ is the natural filtration.

For these spaces we have the following properties:

- $(X_t) \in \S(T), \V_c(T)$ are left-continuous and **progressively measurable**.
- $\S(T)$ is **dense** in $\V_c(T)$.
    - Suppose $(X_t) \in \V_c(T)$.
    - Suppose $P_n = (t_j^{(n)})$ is **the shrinking dyadic** partition sequence in $P[0, T]$.
    - Define the process $(X_t^{(n)})$ as $\sum_j X_{t_j} 1_{(t_j, t_{j + 1}]}(t)$.
    - In this case $(X_t^{(n)} - X_t)^2 \downarrow 0$ **pointwise** due to the dyadic sequence.
    - By (**DCT**), $(X_t^{(n)}) \to (X_t)$ in $\L_2$.
- $\V_c(T)$ is **dense** in $\mathcal B(T)$. (**==TODO==, see Oksendal p.28**)
- $\mathcal B(T)$ is **dense** in $\V(T)$.
    - Suppose $(X_t) \in \V(T)$.
    - Define the process $(X_t^{(n)})$ as truncation of $(X_t)$ into range $[-n, n]$.
    - By (**DCT**), $(X_t^{(n)}) \to (X_t)$ in $\L_2$.

(**Integrate $\S$ with integrator in $\M_c$**)

Suppose $(\Omega, \F, (\F_t), T = [0, T], P)$ is a filtered probability space.

Suppose $(M_t) \in \M_c(T)$ and $(X_t), (Z_t) \in \S(T)$.

- $(X_t)$ is an adapted, square-integrable simple process.
  - We will assume $X_t = Y_j 1_{(t_j, t_{j + 1}]}(t)$ for some partition $(t_j)_{j = 0}^n \in P[0, T]$.
- $(M_t)$ is a continuous square-integrable martingale.

Define $(X \cdot M)_t = I_t = \int_0^t X_s dM_s := \sum_{j = 0}^{n - 1} Y_j(M_{t \land t_{j + 1}} - M_{t \land t_j})$ for $t \in [0, T]$.

- $(I_t)$ is **continuous**.
    - $(M_t)$ is continuous. This is clearly true for each $\omega \in \Omega$.
- $(I_t)$ is **adapted** to $(\F_t)$.
    - This is apparent by definition.
- $I_t$ is **integrable** for all $t \in [0, T]$, that is $\forall t \in [0, T]: I_t \in \L^1(\Omega \to \R, \F_t, P)$.
    - $E|I_t| \le \sum_{j = 0}^{n - 1} E|Y_j(M_{t \land t_j} - M_{t \land t_{j + 1}})| < \infty$, by (Holder).
- $(I_t)$ is a **martingale** on the filtered space.
    - $E[I_t | \F_s] = \sum_{i = 0}^{n - 1} E[Y_i(M_{t \land t_{j + 1}} - M_{t \land t_j})|\F_s]$.
    - Consider each term, for simplicity denoted by  $E[Y(M_b - M_a) | \F_s]$.
      - Suppose $a < b \le s$, $E[Y(M_b - M_a)|\F_s] = Y(M_b - M_a)$.
      - Suppose $a < s < b$, $E[Y(M_b - M_a)|\F_s] = Y(M_s - M_a)$.
      - Suppose $s \le a < b$, $E[\cdots] = 0$.
- $I_t$ has **zero mean** for all $t \in [0, T]$.
    - $E[(X \cdot M)_t] = E[E[(X \cdot M)_t | \F_0]] = E[(X \cdot M)_0] = 0$.
- $(X \cdot M)_t$ is **linear** in the integrator.
    - $(a X \cdot M)_t = a(X \cdot M)_t$ and $((X + Z) \cdot M)_t = (X \cdot M)_t + (Z \cdot M)_t$.

This integral is also called the **continuous martingale transform**.

(**Integrate $\S$ with a standard Brownian motion**)

Suppose $(\Omega, \F, (\F_t), T = [0, T], P)$ is a filtered probability space.

Let $(B_t)$ be a **standard Brownian motion** and $(X_t) \in \S(T)$.

- By definition $(B_t) \in \M_c(T)$ is a continuous square-integrable martingale.
- $(X_t)$ is an adapted, square-integrable simple process.
  - We will assume $X_t = Y_j 1_{(t_j, t_{j + 1}]}(t)$ for some partition $(t_j)_{j = 0}^n \in P[0, T]$.

Let $I_t = (X \cdot B)_t$. Then we have the following additional results:
- (**Ito isometry**) $\|I_T\|_2 = \|(X_t)_{t\in[0, T]}\|_2$.j
    - Notice that the LHS is a norm on $\L^2(\Omega \to \R, \F_T)$ and the RHS is $\L^2(\Omega \times [0, T]\to \R, \F \times \B[0, T])$.
    - Equivalently written as $E[I_T]^2 = \int_0^T E[X_t^2]dt = E[\int_0^T X_t^2 dt]$.
    - Suppose $i < j$, $E[Y_j Y_i (B_{t_{j + 1}} - B_{t_j})(B_{t_{i + 1}} - B_{t_i})] = 0$.
        - Since $${E}[Y_{j} Y_{i}(B_{t_{j+1}}-B_{t_{j}})(B_{t_{i+1}}-B_{t_{i}})]={E}[Y_{j} Y_{i}(B_{t_{i+1}}-B_{t_{i}}) {E}[B_{t_{j+1}}-B_{t_{j}} | \mathcal{F}_{t_{j}}]]=0$$

    - So $E[I_T^2] = \sum_{j = 0}^{n - 1} E[Y_j^2E[(B_{t_{j + 1}} - B_{t_j})^2|\F_{t_j}]] = \sum_{j = 0}^{n - 1} E[Y_j^2](t_{j + 1} - t_j)$.

- $(I_t) \in \M_c(T)$. It is a continuous square-integrable martingale.
    - $(I_t)$ is a continuous martingale as it is integrating $\S$ with $\M_c$.
    - $\forall t \in [0, T]: I_t \in \L^2(\Omega \to \R, \F_t, P)$ according to **Ito isometry**.

(**Integrate $\V$ with a standard Brownian motion**)

Suppose $(\Omega, \F, (\F_t), T = [0, T], P)$ is a filtered probability space.

Let $(B_t)$ be a **standard Brownian motion** and  And $(X_t), (Y_t) \in \V(T)$.

- $(X)_t \in \V(T)$ is only adapted and square integrable.
- $(B_t) \in \M_c(T)$ is a continuous square-integrable martingale.

Define $I_t = (X \cdot B)_t = \int_0^t X_t dB_t$ for a fixed $t \in [0, T]$ as following:
- Construct sequence $(X_t^{(n)}) \in \S(T)$ such that $(X_t^{(n)}) \to (X_t)$ in $\L_2$.
    - Clearly $(X_t^{(n)})_n$ is Cauchy in $\L_2$.
- Define $I_t^{(n)} = \int_0^t X_s^{(n)} dB_s$.
    - $I_t^{(n)}$ is a Cauchy sequence in $\L^2(\Omega \to \R, \F_t, P)$. Since $\n{I_t^{(n)} - I_t^{(m)}} = \n{X^{(n)}_{[0, t]} - X^{(m)}_{[0, t]}}$.
- So $I_t^{(n)}$ **converges** to some $I_t \in L^2(\Omega \to \R, \F_t, P)$.
- The limit does not depends on the approximating sequence $(X_t^{(n)})_{n=1}^\infty$.
    - Suppose $J_t^{(n)}$ is the result of another approximating sequence.
    - Then $\n{I_t^{(n)} - J_t^{(n)}}$ goes to zero by definition.


For $0 \le a < b \le t$ define $\int_a^b X_t dB_t = \int_0^T 1_{(a, b]}(t) X_t dB_t$.

We have following properties:

- Linearity.
    - $(a X \cdot B)_t = a(X \cdot B_t)$ for $a \in \R$.
        - Since $a(X_t^{(n)}) \to a(X_t)$.

    - $((X + Y) \cdot B)_t = (X \cdot B)_t + (Y \cdot B)_t$.
        - Suppose $(Y_t^{(n)}) \to (Y_t)$ in $\L_2$, then $(X_t^{(n)}) + (Y_t^{(n)}) \to (X_t + Y_t)$ in $\L_2$.

- $\int_a^t X_s dB_s = \int_a^b X_s dB_s + \int_b^t X_s dB_s$.
- (**Ito isometry**) $\|I_T\| = \|(X_t)_{t=0}^T\|$.
    - $\|(X_t)\|\leftarrow \|(X_t^{(n)})\| = \|I_T^{(n)}\| \to \|I_T\|$.
- $\forall t \in [0, T]: E[I_t] = 0$.
    - Since convergence in $\L_2$ implies convergence in expectation. $E[I_t^{(n)}] \to E[I_t] = 0$.
- $\forall t\in [0, T]: I_t \in \L^2(\Omega \to \R, \F_t, P)$.
- $(I_t)$ is a **martingale**.
    - $E[I_t^{(n)}|\F_s] = I_s^{(n)} \to E[I_t | \F_s]$ in $\L_2$. And $I^{(n)}_s \to I_s$ in $\L_2$.
    - Therefore $E[I_t | \F_s] = I_s$ when $0 \le s < t \le T$.
- $E[I_s I_{t}] = \int_0^{t \land s} E[X_u^2] du$.
    - Recall that increments of martingales are uncorrelated.
    - Suppose $s \le t$, then $E[I_s I_t] = E[I_s (I_s + I_t - I_s)] = E[I_s^2]$.
- Let $J_t = (Y \cdot B)_t$. $\pd{I_t}{J_t} = E[I_t J_t] = \pd{(X_s)_{s \le t}}{(Y_s)_{s \le t}} = \int_0^t E[X_s Y_s] ds$.
    - Clearly $(X_s + Y_s)_s \in \V(T)$.
    - $E[\int_0^t(X_s + Y_s) dB_s]^2 = \int_0^t E[(X_s + Y_s)^2]ds = \int_0^t (E[X_s^2] + E[Y_s^2] + 2E[X_s Y_s]) ds$.
    - Also by linearity $\cdots = E[(\int_0^t X_s dB_s + \int_0^t Y_s dB_s)]^2$.
    - Now expand and cancel.
- Suppose $(X_t^{(n)}) \in \V(T)$ and $(X_t^{(n)}) \to (X_t)$ in $\L_2$. Then $(X^{(n)} \cdot B)_t \to (X \cdot B)_t$ in $\L_2$.

There exists a **continuous modification** of $I_t$ in this case. ==TODO==

- Recall that $(A_t)$ is a modification of $(B_t)$ if $\forall t \in T: P(X_t = Y_t) = 1$.
- We will **always assume** this modification as $(X \cdot B)_t$ from now on.

(**Wiener integral**)

Suppose $(\Omega, \F, (\F_t), T = [0, T], P)$ is a filtered probability space. 

Suppose $(B_t)_{t \in [0, T]}$ is a standard Brownian motion and $(B_t) \in \M_c(T)$.

Suppose $f \in \L^2([0, T] \to \R, \B[0, T])$ and it is continuous.

Define $(I_t) = (\int_0^t f(s)dB_s)$, where $f(s)$ is viewed as in $\V_c(T)$.

- Find a sequence $f^{(n)}(t)$ of deterministic processes in $\S(T)$ such that $f^{(n)} \to f$ in $\L_2$.
- Define $I^{(n)}_t = \int_0^t f^{(n)}(s) dB_s$.
- $(I_t^{(n)})$ is a Gaussian process.
  - Since for any time points $(t_j)_{j = 1}^m \in [0, T]$. $(I_{t_j}^{(n)})_{j=1}^m$ is jointly Gaussian.

- $I_t$ is a Gaussian process as well.
  - Since for any time points $(t_j)_{j = 1}^m \in [0, T]$. $(I_{t_j})_{j=1}^m$ is the $\L^2$ limit of $(I_{t_j}^{(n)})_{j=1}^m$ (after concatenating dimensions).
  - And the $\L^2$ limit of Gaussian vectors remains Gaussian. ==TODO==
  - $E[I_t] = 0$.
  - $E[I_s I_t] = \cov(I_s, I_t) = \int_0^{t\land s} f(\tau)^2 d\tau$.


(**Ito process**)

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered probability space.

- Suppose $(B_t)$ is a **standard Brownian motion** and $(B_t) \in \M_c(T)$.
- Suppose $(V_t) \in \V(T)$ and $(U_t) \in \A(T)$. Note that there are still extensions.
- Suppose $X_0 \in \L(\Omega \to \R, \F_0)$.

Then the process $X_t = X_0 + \int_0^t V_s dB_s + \int_0^t U_s ds$ is called an **Ito process**.

- When $X_0 = 0$ is deterministic, the process has **zero start**.
- $(V_t)$ is called the **local volatility**, $(U_t)$ is called the **local drift**.
- $dX_t = V_t dB_t + U_t dt, X_0, t\ge 0$ defines the same process.
- $X_t$ is **continuous**. Since both integrals are continuous.

Some immediate examples of Ito processes:

- $(B_t)$. Take $V_t = 1$ and $U_t = 0$.
- $(\sigma B_t + \mu t)$. Take $V_t = \sigma$ and $U_t = \mu$.

(**Higher dimensional Ito process**)

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered space.

- Suppose $(\mathbf V_t) = (V^{(i, j)}_t) \in \V^{n \times m}(T)$ are real stochastic processes.

- Suppose $(\mathbf U_t) = (u_t^{(i)}) \in \A(T)$ are $n$ real stochastic processes.

- Suppose $(\mathbf B_t) = (B_t^{(j)}) \in \M_c^m(T)$ is a $\R^m$ standard BM.

- Then $d\mathbf X_t = \mathbf V_t d\mathbf B_t + \mathbf U_t dt$ is called an ($n$-dimensional) **Ito process**. Where (Einsum notation)
  $$
  \forall 1 \le i \le n: dX_t^{(i)} = V_t^{(i, j)} dB_t^{(j)} + U_t^{(i)}dt
  $$

(**QV of Ito process**)

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered probability space.

Suppose $(X_t)$ is an **Ito process**, $dX_t = V_t dB_t + D_t dt$. Then $[X]_t = \int_0^t V_s^2 ds$ **in probability**.
$$
(dX_t)^2 = (V_t dB_t + D_t dt)^2 = V_t^2 dB_t^2 + D_t^2 dt^2 + 2V_t D_t dB_t dt = V_t^2 dt
$$

- By definition $(V_t) \in \V(T)$ and $(D_t) \in \A(T)$.

- Denote $I_t = \int_0^t V_s dB_s$ and $R_t = \int_0^t D_t dt$ for $t \le T$.

- Let $(t_j)_{j = 0}^n \in P[0, t]$ be inside the sequence of shrinking partitions for a fixed $t \in (0, T]$.

- $[X]_t = [I]_t$ **pointwise**, since:

  - $(X_{t_{j+1}}-X_{t_{j}})^{2}=(I_{t_{j+1}}-I_{t_{j}})^{2}+2(I_{t_{j+1}}-I_{t_{j}})(R_{t_{j+1}}-R_{t_{j}})+(R_{t_{j+1}}-R_{t_{j}})^{2}$.
  - $\sum_{j=0}^{n-1}(I_{t_{j+1}}-I_{t_{j}})(R_{t_{j+1}}-R_{t_{j}}) \leq\{\sum_{j=0}^{n-1}(I_{t_{j+1}}-I_{t_{j}})^{2}\}^{1 / 2}\{\sum_{j=0}^{n-1}(R_{t_{j+1}}-R_{t_{j}})^{2}\}^{1 / 2}$.
  - Clearly $\sum_{j}(R_{t_{j + 1}} - R_{t_j})^2 \to 0$ pointwise.

- $[I]_t = \int_0^t V_s^2 ds$ in $\L_2$ when $(V_t) \in \S(T)$ since:

  - $\sum_{j = 0}^{n - 1} (I_{t_{j + 1}} - I_{t_j})^2 \to \sum_{j = 0}^{n - 1}V_{t_j}^2(B_{t_{j + 1}} - B_{t_j})^2$ pointwise.
  - $\sum_{j = 0}^{n - 1} V_{t_j}^2 (B_{t_{j + 1}} - B_{t_j})^2 \to \sum_{j = 0}^{n - 1} V_{t_j}^2(t_{j + 1} - t_j)$ in $\L_2$.
  - $\sum_{j = 0}^{n - 1} V_{t_j}^2(t_{j + 1} - t_j) \to \int_0^t V_s^2 ds$ pointwise.

- $[I]_t = \int_0^t V_s^2 ds$ in $\L_1$ when $(V_t) \in \V(T)$ since:

  - Fixing $\epsilon > 0$, there exists $(V_t^\epsilon) \in \S(T)$ such that $\|(V_t^\epsilon) - (V_t)\|^2_2 < \epsilon$. 
  - Denote $I^{\epsilon}_t = \int_0^t V^\epsilon_s dB_s$.
  - $\|\sum_{j = 0}^{n - 1} (I_{t_{j + 1}} - I_{t_j})^2 - \int_0^t V_s^2 ds\|_1$ is less then the sum of following terms:
    1. $\|\sum_{j = 0}^{n - 1} (I_{t_{j + 1}} - I_{t_j})^2 -(I^{\epsilon}_{t_{j + 1}} - I^{\epsilon}_{t_j})^2 \|_1$.
    2. $\|\sum_{j = 0}^{n - 1} (I^{\epsilon}_{t_{j + 1}} - I^{\epsilon}_{t_j})^2  - \int_0^t (V_s^\epsilon)^2 ds\|_1$.
    3. $\|\int_0^t (V_s^\epsilon)^2ds - \int_0^t V_s^2 ds\|_1$.
  - $(3)\le \|(V_s^\epsilon - V_s)(V_s^\epsilon + V_s)\|_1 \le \|(V_s^\epsilon - V_s)\|_2\| \|(V_s^\epsilon + V_s)\|_2 \to 0$ as $\epsilon \downarrow 0$.
  - $(2) \downarrow 0$ as $\epsilon \downarrow 0$ is proved in previous step.
  - $(1)$ expand the terms back to Ito integral:

  $$
  \begin{aligned}
  (1) & = \left\|\sum_{j=0}^{n-1}\left(\int_{t_{j}}^{t_{j+1}}\left(V_{s}^{\epsilon}-V_{s}\right) d B_{s}\right)\left(\int_{t_{j}}^{t_{j+1}}\left(V_{s}^{\epsilon}+V_{s}\right) d B_{s}\right)\right\|_1\\
  
  & \le \left\|\left(\sum_{j=0}^{n-1}\int_{t_{j}}^{t_{j+1}}\left(V_{s}^{\epsilon}-V_{s}\right) d B_{s}\right)
  \left(\sum_{j=0}^{n-1}\int_{t_{j}}^{t_{j+1}}\left(V_{s}^{\epsilon}+V_{s}\right) d B_{s}\right)\right\|_1\\
  
  & \le \left\|\left(\sum_{j=0}^{n-1}\int_{t_{j}}^{t_{j+1}}\left(V_{s}^{\epsilon}-V_{s}\right) d B_{s}\right)\right\|_2
  \left\|
  \left(\sum_{j=0}^{n-1}\int_{t_{j}}^{t_{j+1}}\left(V_{s}^{\epsilon}+V_{s}\right) d B_{s}\right)\right\|_2\\
  
  & = \sqrt{E\left [
  \sum_{j = 0}^{n - 1} \left (\int_{t_j}^{t_{j + 1}} (V_s^\epsilon - V_s)dB_s\right)^2
  \right ]} \sqrt{E\left [
  \sum_{j = 0}^{n - 1} \left (\int_{t_j}^{t_{j + 1}} (V_s^\epsilon + V_s)dB_s\right)^2
  \right ]}\\
  
  & = \sqrt{E\left[ \int_0^t (V_s^\epsilon - V_s)^2 ds \right]} \sqrt{E\left [ \int_0^t (V_s^\epsilon + V_s)^2 ds\right]}\\
  
  & = \norm{(V_s^\epsilon - V_s)}_2 \norm{(V_s^\epsilon + V_s)}_2 \to 0
  \end{aligned}
  $$

- Suppose $dY_t = U_t dB_t + E_t dt$. The covariation $[X, Y]_t$ is given by **polarization** identity:
  $$
  [X, Y]_t = \frac{1}{2} \left ( [X + Y]_t - [X]_t - [Y]_t\right) = \frac{(U_t + V_t)^2 - U_t^2 - V_t^2}{2} = U_tV_t
  $$

