#### Linear IVP

##### Non-homogeneous constant coefficient first-order linear system

Consider following IVP for $x(t) \in C^1(I \to \C^{n})$:
$$
\boxed{x'(t) = A x(t) + g(t), \quad x(0) = x_0,\quad A \in \C^{n \times n}, \quad g \in C(I \to \C^{n})}
$$

where $I$ is a closed interval.

- According to previous discussions, there exists a unique solution on $I$.
- Multiply "integration factor" $\exp(-tA)$ on both sides and observe:
  - $\exp(-tA) x'(t) = \exp(-tA)A x(t) + \exp(-tA) g(t)$.
  - Therefore $(\exp(-tA)x(t))' = \exp(-tA) g(t)$.
  - Integrate on both sides gives:
    $$
    \exp(-tA)x(t) - x_0 = \int_0^T \exp(-sA) g(s) \dd s
    $$
  - Therefore a particular solution is given by
    $$
    x(t)=\exp (t A) x_{0}+\int_{0}^{t} \exp ((t-s) A) g(s) \dd s
    $$
    it is the sum of the homogeneous solution and a part caused by $g(t)$.
- Denote the homogeneous solution $x_h(t)$ as the solution assuming $g(t) = 0$.
- Denote the particular solution $x_p(t) = x(t) - x_h(t)$.

##### Example: Homogenous first-order planar constant linear system

Consider following IVP for $x(t) \in C^1(\R \to \C^{2})$:
$$
\boxed{x'(t) = A x(t), \quad x(0) = x_0 \in \R^2,\quad A \in \R^{2 \times 2}}
$$

- Recall the unique solution on $\R$ is $x(t) = e^{tA}x_0$.
- Suppose $U^{-1} A U=\left(\begin{array}{cc} \alpha_{1} & 0 \\ 0 & \alpha_{2} \end{array}\right) = \Lambda$. Where $U = [u_1; u_2]$ are orthonormal eigenvectors.
  - Now define $y(t) = U^{-1} x(t)$, the IVP is transformed to:
    $$
    y'(t) = U^{-1}A U y(t) = \Lambda y(t), \quad y(0) = U^{-1}x_0 = y_0, \quad \Lambda = U^{-1} A U
    $$
  - Therefore $y(t) = e^{t\Lambda} y_0 =\left(\begin{array}{cc} e ^{\alpha_{1} t} & 0 \\ 0 & e ^{\alpha_{2} t} \end{array}\right) y_{0}$.
  - Since $x(t) = Uy(t)$. $x(t) = y_{0, 1} e^{\alpha_1 t} u_1 + y_{0, 2} e^{\alpha_2t} u_2$.
  - When $\alpha_1, \alpha_2 \in \R$.
    - $U \in \R^{2 \times 2}$.
    - And $x(t), y(t)$ are both real.
  - When $\alpha_1, \alpha_2 \in \C$.
    - $\alpha_1 = \alpha = \lambda + i \omega$ and $\alpha_2 = \alpha^* =  \lambda - i\omega$. $u_2 = u_1^*$.
    - $x(t)$ is real, but $y(t)$ and $u_1, u_2$ are not.
    - $x_0^* = x_0$ implies $y_{0,1} u_{1}+y_{0,2} u_{2}=y_{0,1}^{*} u_{2}+y_{0,2}^{*} u_{1}$. So $y_{0, 1}^* = y_{0, 2}$.
    - Recall that $e^{\alpha t} = e^{\lambda t} (\cos(\omega t) + i \sin (\omega t))$.
    - $y_{0, 1} e^{\alpha_1 t} u_1$ is complex conjugate of $y_{0, 2} e^{\alpha_2t} u_2$.
    - So $x(t) = 2\re(y_{0, 1} e^{\alpha t} u_1) = 2 \cos (\omega t) e ^{\lambda t} \re\p{y_{0,1} u_{1}}-2 \sin (\omega t) e ^{\lambda t} \im\p{y_{0,1} u_{1}}$.
- Suppose $U^{-1} A U=\left(\begin{array}{cc} \alpha & 1 \\ 0 & \alpha \end{array}\right) = \Lambda$. $U = [u_1; u_2]$ contains generalized eigenvectors.
  - $\alpha \in \R$ is guaranteed.
  - Now define $y(t)$ and new IVP similar to diagonal case.
  - $x(t) = (y_{0, 1} + y_{0, 2}t)e^{\alpha t}u_1 + y_{0, 2}e^{\alpha t} u_2$.

##### Homogeneous $n$-th order constant coefficient equation

Consider the IVP for $x \in C^n(\R \to \C)$,
$$
\boxed{x^{(n)} + c_{n - 1} x^{(n - 1)} + \cdots + c_1 x' + c_0x = 0, \quad c_k \in \C, \quad x(0) = x_0, \cdots, x^{(n-1)} = x_{n-1}}
$$
Define $y = (x, x^{(1)}, \ldots, x^{(n-1)}) \in C^n(\R \to \C^n)$ and equivalent IVP:
$$
y'(t) = A y(t), \quad A=\left(\begin{array}{ccccc}
0 & 1 & & & \\
& 0 & 1 & & \\
& & \ddots & \ddots & \\
& & & 0 & 1 \\
-c_{0} & -c_{1} & \cdots & \cdots & -c_{n-1}
\end{array}\right) \in \C^{n \times n}, \quad y(0) = \left(\begin{array}{c}
x_0\\
x_1\\
\vdots\\
x_{n-2}\\
x_{n-1}
\end{array}\right)
$$

- $A$ is called the **companion matrix** of the ODE and $p(z)$.
  - Characteristic of $A$ is $p(z) = \det(zI - A) = z^{n}+c_{n-1} z^{n-1}+\cdots+c_{1} z+c_{0}$.
  - $(A^k e_n)_{k = 0}^{n - 1}$ is a basis of $V$. Such a vector is called a cyclic vector of $A$.
- Since $A$ has a cyclic vector $v$. All of its eigenvalues have geometric multiplicity $1$.
  - Let $m$ be the smallest integer such that $\span(v, A v, \ldots, A^{m} v)$ intersects $\ker(A-\lambda I)$.
  - Then we have a vector $\sum_{k=0}^{m} c_{k} A^{k} v$ such that $c_{m} \neq 0$ and
    $$
    A \sum_{k=0}^{m} c_{k} A^{k} v=\lambda \sum_{k=0}^{m} c_{k} A^{k} v
    $$
  - So $A^{m+1} v$ is a linear combination of $v, \ldots, A^{m} v$.
  - Since $v$ is cyclic, $m$ must be $n-1$. Thus $E(\lambda, A)$ must be one-dimensional.
- Minimal polynomial of $A$ must be $p(z)$ as all eigenvalues have the highest indexes.
  - Otherwise, there must exist an eigenvalue with geometric multiplicity higher than one.
- We can easily find a basis for the solution space by following observation.
  - First suppose $U^{-1}A U$ is in Jordan form $J_1 \oplus \cdots \oplus J_m$.
  - Note that Jordan block $J_k = \lambda I + N \in \C^{a \times a}$ gives:
    $$
    \exp(tJ_k) = \exp(\lambda tI)\exp(tN) = e ^{\lambda t}\left(\begin{array}{cccc}
    1 & t & \frac{t^{2}}{2 !} & \cdots & \frac{t^{m-1}}{(m-1) !} \\
    & 1 & t & \ddots & \vdots \\
    & & 1 & \ddots & \frac{t^{2}}{2 !} \\
    & & & \ddots & t \\
    & & & & 1
    \end{array}\right)
    $$
  - Suppose $J_i$ corresponds to $\lambda_i$ with multiplicity $a_i$. $1 \le i \le m$.
  - Suppose $\lambda_i$ is an eigenvalue with multiplicity $a_i$ where $1 \le i \le m$.
  - Then define $x_{\lambda_i, k}(t): = t^k e^{\lambda_i t}$ where $0 \le k < a_i$ and $1 \le i \le m$.
  - It is easy to see that the solution set is indeed spanned by these functions.
  - This particular basis can be directly read-off from the characteristic polynomial!

##### Non-homogeneous $n$-th order constant coefficient equation

Consider the IVP for $x \in C^n(I \subseteq \R \to \C)$,
$$
x^{(n)} + c_{n - 1} x^{(n - 1)} + \cdots + c_1 x' + c_0x = g(t), \quad c_k \in \C, \quad x(0) = x_0, \cdots, x^{(n-1)}(0) = x_{n-1}, \quad g \in C(I \to \R)
$$
Define $A$ and initial condition $y(0)$ in the same way as in homogeneous case. Let
$$
y'(t) = Ay(t) + G(t), \quad u_0 = \left(\begin{array}{c}
0\\
\vdots\\
0\\
1
\end{array}\right), \quad G(t) = u_0 g(t)
$$

- Let $x_h(t)$ be the homogeneous solution assuming $g(t) = 0$.
- Recall that $x_p(t) = \int_0^t \exp((t - s)A)G(s) \dd s = \int_0^t \exp((t - s)A)u_0 g(s)\dd s$.
- Define $u(t) = e^{(t - s)A}u_0$. Clearly $u(t)$ can be found through solving a new homogeneous IVP.
- And then $x_p(t) = \int_0^t u(t - s)g(s)\dd s$, $x(t) = x_g(t) + x_p(t)$.

##### Homogeneous linear first-order system

Consider following ODE for $x(t) \in C^1(I \subseteq \R \to \C^{n})$:
$$
\boxed{x'(t) = A(t) x(t),\quad A \in C(I \to \C^{n \times n})}
$$

where $I$ is a closed interval.

- Improved Picard-Lindelof guarantees existence and uniqueness on $I$ given any initial $x(t_0)$ value.
  - We could take $I = \R$, and the existence and uniqueness of solution apparently holds.
- Let $\phi(t, t_0, x_0): I \times I \times \C^n \to \C^n$ be the unique general solution.
- The space of all solutions is a $n$ dimensional subspace of $C^1(I \to \C^n)$.
  - Superposition: $\forall x_0, x_1 \in \C^n: \phi(t, t_0, x_0) + \phi(t, t_0, x_1) = \phi(t, t_0, x_0 + x_1)$.
  - Scaling: $\phi(t, t_0, cx_0) = c\phi(t, t_0, x_0)$.
- Define $\Pi(t, t_0) := [\phi(t, t_0, e_1); \ldots; \phi(t, t_0, e_n)]: I \times I \to \C^{n \times n}$.
  - $\phi(t, t_0, x_0) = \Pi(t, t_0) x_0 = \sum_{j = 1}^n \phi(t, t_0, e_j) x_{0, j}$.
    - This can be viewed as a linear isomorphism, from $\C^n$ to $C^1(I \to \C^n)$.
  - For any $s, t \in I$, $\Pi(s, t) \in \C^{n \times n}$ is an invertible matrix.
    - Uniqueness of solution based on the initial value guarantees invertibility.
  - For any $t_0 \in I$, $\Pi(t, t_0): I \to \C^{n \times n}$ is called the **principal matrix solution** at $t_0$.
    - And we will call $\Pi: I\times I \to \C^{n \times n}$ the **principal matrix**.
  - For any $t_0 \in I$, $\Pi(t, t_0)$ is the unique solution of following matrix valued IVP.
    $$
    D_1\Pi(t, t_0) = A(t) \Pi(t, t_0), \quad \Pi(t_0, t_0) = \I
    $$
  - Suppose $A(t) = A$ is a constant, $\Pi(t, s) = e^{(t - s)A}$.
    - Recall that the solution for $x'(t) = Ax(t)$ starting from $(0, x_0)$ is $\exp(tA)x_0$.
    - Therefore $\Pi(t, s) = \exp({(t - s)A})$.
  - We have the bound $\n{\Pi(t, s)} \le \exp{{\int_{s}^t \n{A(\tau)} \dd \tau}}$.
    - Since $\Pi(t, s) = \int_s^t A(\tau) \Pi(\tau, s) \dd \tau$.
    - Therefore $\n{\Pi(t, s)} \le \int_s^t \n{A(\tau)} \n{\Pi(\tau,s)} \dd s$.
    - Now apply Gronwall's inequality gives the result
  - $\forall s, t, u \in I: \Pi(s, t)\Pi(t, u) = \Pi(s, u)$.
    - Take $u = s$, then $\forall s, t \in I: \Pi(s, t) = \Pi(t, s)^{-1}$.
  - Observe the following:
    - $D_1\Pi(t, s) = A(t) \Pi(t, s)$.
    - $D_1(\Pi(t, s)^{-1}) = -\Pi(t, s)^{-1}D_1 \Pi(t, s) \Pi(t, s)^{-1} = - \Pi(t, s)^{-1}A(t)$.
      - For the derivative of matrix inverse, observe that
        $$
        (I)' = (\Pi \Pi^{-1})' = \Pi' \Pi^{-1} + \Pi (\Pi^{-1})' \implies (\Pi^{-1})' = -\Pi^{-1}\Pi' \Pi^{-1}
        $$
    - Therefore $D_2 \Pi(s, t) = -\Pi(s, t) A(t)$.
- Suppose $\phi_1, \ldots, \phi_n \in C^1(I \to \C^n)$ are $n$ solutions. Define $U(t) = [\phi_1(t); \ldots; \phi_n(t)]: I \to \C^{n \times n}$.
  - The determinant of $U(t)$ is called Wronski determinant. $W(t)= \det(\phi_1, \ldots, \phi_n) := \det U(t)$.
  - Due to the linearity of solutions $\exists t \in I: W(t) \neq 0 \implies \forall t \in I: W(t) \neq 0$.
  - If $W(t) \neq 0$, $U(t)$ is called a **fundamental matrix solution**. 
  - For any $t_0 \in I$, $\Pi(t, t_0)$ is also a fundamental matrix solution.
- A fundamental matrix solution $U(t)$ contains information about all solutions.
  - The columns of $U$ spans the entire solution space.
  - $\Pi(t, t_0)$ can be derived from $U(t)$.
    - Let $X_0 = (x_0^{(1)}, \ldots, x_0^{(n)}) \in \C^{n \times n}$.
    - Suppose $U(t) = \Pi(t, t_0) X_0$.
    - Then $U(t) U(s)^{-1} = \Pi(t, t_0) \Pi(t_0, s) = \Pi(t, s)$.
  - Therefore $\phi(t, t_0, x_0)$ can also be derived from $U(t)$.
    $$
    \phi(t, t_0, x_0) = \Pi(t, t_0) x_0 = U(t)U(t_0)^{-1} x_0
    $$

##### Linear first-order system

Consider following IVP for $x(t) \in C^1(I \subseteq \R \to \C^{n})$:
$$
\boxed{x'(t) = A(t) x(t) + g(t),\quad x(t_0) = x_0, \quad A \in C(I \to \C^{n \times n}), \quad g \in C(I \to \C^n)}
$$

where $I$ is a compact interval.

- Improved Picard-Lindelof guarantees existence and uniqueness of solution on $I$.
- Let $\phi(t, t_0, x_0): I \times I \times \C^n \to \C^n$ be the unique general solution to the IVP.

**Variation of parameters** gives a method to find a particular solution:

- Recall that the general solution of the homogeneous part is $x(t) = \Pi(t, t_0)x_0$.
- Now assume the solution is of the following form where parameter $x_0$ is replaced with a unknown function $c(t)$.
  $$
  x(t) = \Pi(t, t_0) c(t),\quad c(t) \in C^1(I \to \C^n), \quad x(t_0) = x_0 = c(t_0)
  $$
- Then we have
  $$
  x'(t) = D_1 \Pi(t, t_0) c(t) + \Pi(t, t_0) c'(t) = A(t) x(t) + \Pi(t, t_0) c'(t)
  $$
- Compare this with $x'(t) = A(t) x(t) + g(t)$ shows we must have $g(t) = \Pi(t, t_0)c'(t)$.
- Therefore $c'(t) = \Pi(t_0, t) g(t)$. This is a linear homogeneous IVP.
- A solution for $c(t)$ would be $c(t) = x_0 + \int_{t_0}^t \Pi(t_0, s) g(s) \dd s$.
- Therefore the full solution is given by
  $$
  x(t) = \Pi(t, t_0) x_0 + \int_{t_0}^t \Pi(t, s) g(s) \dd s
  $$

**The method of integrating factor** gives an equivalent method to find the solution:

- Suppose $\Psi(t) \in C^1(I \to \C^{n \times n})$ is an integrating factor.
  - $\Psi(t) x'(t) = \Psi(t)A(t)x(t) + \Psi(t) g(t)$.
  - We hope that $\Psi(t)x'(t) - \Psi(t)A(t) x(t) = (\Psi(t)x(t))'$.
  - Therefore $\Psi'(t) = -\Psi(t)A(t)$.
- Since $D_2 \Pi(t_0, t) = -\Pi(t_0, t) A(t)$. $\Pi(t_0, t)$ is a integrating factor.
  - $\Pi(t_0, t) x'(t) = \Pi(t_0, t)A(t) x(t) + \Pi(t_0, t)g(t)$.
  - $D_t(\Pi(t_0, t) x(t)) = \Pi(t_0, t) g(t)$. Now integrate on both sides.
  - $\Pi(t_0, t)x(t) - x_0 = \int_{t_0}^t \Pi(t_0, s)g(s) \dd s$.
- Again, the full solution is given by
  $$
  x(t) = \Pi(t, t_0) x_0 + \int_{t_0}^t \Pi(t, s) g(s) \dd s
  $$
