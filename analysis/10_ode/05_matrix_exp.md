(**IVP: Improved Picard-Lindelof**)

See the set up in (**IVP: Picard-Lindelof**).

The requirement on $f(t, x)$ is **weakened** to ***BASICALLY***  locally Lipschitz continuous. See the theorem for details.

Again, W.L.O.G. let $t_0 = 0$, and we only consider the right side of $t_0$.

- Suppose $V = [0, T] \times \overline{B(x_0, \delta)} \subset U$, for some $\delta > 0, T > 0$.

- First we need to apply some restriction on the time range:

  - Define $M_0 := \sup_{(t, x) \in V} \n{f(t, x)}$.
  - Define $M(t):=\int_0^{t} \sup _{x \in B_{\delta}\left(x_{0}\right)}\n{f(s, x)} \dd s$.
    - $M(t): [0, T] \to [0, \infty)$ is increasing, $M(0) = 0$, continuous and bounded.

  - One possibility is to let $T_{0}:=\sup \left\{0<t \leq T \mid M\left(t\right) \leq \delta\right\}$.
  - A coarser choice is $T_0 = \delta / M_0$.

- Define $I = [0, T_0]$ and $C = C^1(I \to \overline{B(x_0, \delta)})$.

  - For $x\in C$, define $\n{x}_{t} := \sup_{0 \le s \le t} \n{x(s)}$.
  - The **Picard iteration** on $C$ is $K(x(t)) = x_0 + \int_{0}^t f(s, x(s)) \dd s$.

- The constraints guarantees the following bounds for any $x \in C$.

  - $\n{K(x)(t) - x_0} = \n{\int_0^t f(s, x(s)) \dd s} \le \int_0^t \n{f(s, x(s))} \dd s \le M(t) \le \delta$.
  - Also $\n{K(x)(t) - x_0} \le M_0 t$.

- Define $L(t):=\sup _{x \neq y \in B_{\delta}\left(x_{0}\right)} {|f(t, x)-f(t, y)|}/{|x-y|}$.

- Define $L_1(t):= \int_{0}^t L(t) \dd t$.

  - $L_1(t): [0, T] \to [0, \infty)$ is increasing, $M(0) = 0$, continuous and bounded.

- $K: C \to C$ satisfies (**Weissinger fixed point theorem**).

  - $\forall t \in [0, T_0],\forall x, y \in C: \n{K^m(x)(t) - K^m(y)(t)} \le \frac{L_1(t)^m}{m!} \n{x - y}_{t}$.

    - Proceed with induction. Clearly true for $m = 0$.

    - Now suppose inequality is true with $m$.
      $$
      \begin{aligned}
      \n{K^{m + 1}(x)(t)-K^{m + 1}(y)(t)} &\le \int_0^t \n{f(s, K^m(x)(s)) - f(s, K^m(y)(s))}\dd s\\
      & \le \int_0^t L(s) \n{K^m(x)(s) - K^m(y)(s)} \dd s\\
      & \le \int_0^t L(s)\frac{L_1(s)^m}{m!} \n{x - y}_s \dd s\\
      & \le \n{x - y}_t \int_0^t L'(s)\frac{L_1(s)^m}{m!} \dd s\\
      & = \frac{L_1(t)^{m + 1}}{(m + 1)!}\n{x - y}_t
      \end{aligned}
      $$

  - Therefore we have
    $$
    \n{K^{m}(x) - K^m(y)} \le \frac{L_1(T_0)^{m + 1}}{(m + 1)!} \n{x - y}
    $$

  - Where $\sum_{m=0}^\infty \frac{L_1(T_0)^{m + 1}}{(m + 1)!} = e^{L_1(T_0)} - 1 < \infty$.

(**IVP: homogeneous constant coefficient linear first-order system**)

Consider following IVP for $x(t) \in C^1(\R \to \C^{n})$:
$$
x'(t) = A x(t), \quad x(0) = x_0,\quad A \in \C^{n \times n}
$$

- Improved Picard-Lindelof guarantees existence and uniqueness in any compact interval.
  - Suppose $M = \n{A}$, for time $[-T, T]$, any solution $\n{x(t) - x_0} \le M\abs{t}$.
- Examine the Picard iteration starting from $x_0$.
  - $x_0(t) = x_0$.
  - $x_1(t) = x_0 + \int_0^t Ax_0(s) \dd s = x_0 + tAx_0$.
  - $x_2(t) = x_0 + \int_0^t A(x_0 + sAx_0) \dd s = x_0 + tAx_0 + \frac{t^2}{2}A^2 x_0$.
  - $x_m(t) = \sum_{j=0}^m \frac{t^j}{j!}A^j x_0$.
  - $x(t) = \lim_{m\to \infty}x_m(t) = \sum_{j=0}^\infty \frac{t^j}{j!} A^j x_0$.
    - The limit is guaranteed to exist by Picard-Lindelof.
- Define $\exp(A): \C^{n \times n} \to \C^{n \times n}$  as $\exp(A) = \sum_{j=0}^\infty A^j/j!$.
- Then the unique solution is given by $x(t) = \exp(tA)x_0$ on $\R$.
  - Since we can show that $\exp(tA)$ is invertible.
  - $x_0 \mapsto \exp(tA) x_0$ is an isomorphism. So the solution space is isomorphic to $\C^n$.

- Therefore matrix exponential $e^A = x(1)$ is uniquely defined.
- By definition $\part \exp(tA)/\part t = A \exp(tA)$.

(**Matrix exponential**)

Define matrix exponential $\exp: \C^{n \times n} \to \C^{n \times n}$ as $\exp(A) = \sum_{j = 0}^\infty A^j / j!$.

Suppose $A, B, U \in \C^{n \times n}$.

- Suppose $[A, B] = 0$, $e^{A + B} = e^A e^B$.

  - $B e^{A}=\sum_{j=0}^{\infty} \frac{B A^{j}}{j !}=\sum_{j=0}^{\infty} \frac{A^{j} B}{j !}=e^{A} B$.
  - For any $v \in \C^n$ and define $y(t) = e^{(A + B)t}v$, $z(t) = e^{At}e^{Bt}v$.
  - Then $y(0)= v$, and $y'(t) = (A + B)e^{(A + B)t}v = (A + B)y(t)$.
  - Also $z(0) = v$ and $z'(t) = Ae^{At}e^{Bt} v + e^{At}Be^{Bt}v = (A + B)z(t)$.
  - The result follows from uniqueness of solution.

- Suppose $U$ is invertible. $U^{-1}e^A U = e^{U^{-1} A U}$.

  - This follows from continuity of matrix product.

- $\det(\exp(A)) = \det(\exp(U^{-1}AU)) = \exp(\tr(U^{-1}AU)) = \exp(\tr(A))$.

  - As expected $e^A$ is always invertible.
  - But $e^A$ is not always self-adjoint or positive.

- Further analysis $\exp(A)$ with Jordan basis.

  - Suppose $U^{-1}AU$ is in Jordan form $U^{-1} A U=\left(\begin{array}{lll}
    J_{1} & & \\
    & \ddots & \\
    & & J_{m}
    \end{array}\right)$.

  - Observe that:
    $$
    U^{-1}\exp(A)U = \exp \left(U^{-1} A U\right)=\left(\begin{array}{lll}
    \exp \left(J_{1}\right) & & \\
    & \ddots & \\
    & & \exp \left(J_{m}\right)
    \end{array}\right)
    $$

- Now consider a single Jordan block $J_k$ in $U^{-1}AU$.

  - Suppose $J_k = \alpha I + N \in \C^{k \times k}$ where $N$ is the upper identity matrix. 

  - Since $[I, N] = 0$, $e^{J_k}=e^{\alpha I} e^{N} = e^\alpha \sum_{j=0}^{k-1} N^{j}/j!$. That is
    $$
    \exp (J_k)= e ^{\alpha}\left(\begin{array}{ccccc}
    1 & 1 & \frac{1}{2 !} & \cdots & \frac{1}{(k-1) !} \\
    & 1 & 1 & \ddots & \vdots \\
    & & 1 & \ddots & \frac{1}{2 !} \\
    & & & \ddots & 1 \\
    & & & & 1
    \end{array}\right)
    $$

- Clearly we have $G(\alpha, A) = G(e^\alpha, e^A)$ by observing the form of $\exp(A)$.

  - Notice that $\alpha + 2ik\pi$ are mapped to the same $e^\alpha$.

