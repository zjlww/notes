#### BCH Bound

##### BCH bound

Suppose $C \subseteq \bF^n$ is a cyclic code with generator polynomial $g(x)$. $h(x) = (x^n - 1) / g(x)$.

Suppose $\deg g(x) = r$ and $\deg h(x) = k$.

Suppose $\omega \in \Omega_n$ is a $n$-th primitive root of unity. Then in $\bF[\omega]$ we have
$$
(x^n - 1) = (x - \omega^1) (x - \omega^2) \cdots (x - \omega^{n})
$$
Let $R$ be the zeros of $C$. Define $\delta(C)$ as following:
$$
\delta (C) = \max \c{
\delta \ge 2 
\bigm| 
\exists b \in \Z:R \supseteq \c{\omega^{b}, \omega^{b + 1}, \ldots, \omega^{b + \delta - 2}}
}
$$
The **BCH bound** says $d(C) = w(C) \ge \delta(C)$. Here is a proof by contradiction:

- Suppose $R \supseteq \c{\omega^{b}, \omega^{b + 1}, \ldots, \omega^{b + \delta - 2}} = Z$ for some $b \in \Z$ and $\delta = \delta(C)$.

- Suppose there exists $\symbf c \in C$ and $c(x) = c_0 + c_1 x + \cdots + c_{n - 1} x^{n - 1}$. Where $w = w(\symbf c) < \delta$.
  $$
  c(x) = \sum_{j = 1}^{w} c_{i_j} x^{i_j},\quad 0 \le i_j \le n - 1, \quad c_{i_j} \neq 0
  $$

- Then $c[Z] = \c{0}$. Which is equivalent to the following linear equation:
  $$
  \left[\begin{array}{cccc}
  \omega^{i_1 b} & \omega^{i_2 b} & \ldots & \omega^{i_w b} \\
  \omega^{i_1(b+1)} & \omega^{i_2(b+1)} & \ldots & \omega^{i_w(b+1)} \\
  \vdots & \vdots & & \vdots \\
  \omega^{i_1(b+\delta-2)} & \omega^{i_2(b+\delta-2)} & \ldots & \omega^{i_w(b+\delta - 2)}
  \end{array}\right]_{(\delta - 1) \times w}\left[\begin{array}{c}
  c_{i_1} \\
  c_{i_2} \\
  \vdots \\
  c_{i_w}
  \end{array}\right]= \symbf 0
  $$

- Since $w \le \delta - 1$, we have:
  $$
  \underbrace{\left[\begin{array}{cccc}
  \omega^{i_1 b} & \omega^{i_2 b} & \ldots & \omega^{i_w b} \\
  \omega^{i_1(b+1)} & \omega^{i_2(b+1)} & \ldots & \omega^{i_w(b+1)} \\
  \vdots & \vdots & & \vdots \\
  \omega^{i_1(b+w-1)} & \omega^{i_2(b+w-1)} & \ldots & \omega^{i_w(b+w-1)}
  \end{array}\right]}_{M \in \bF^{w \times w}}\underbrace{\left[\begin{array}{c}
  c_{i_1} \\
  c_{i_2} \\
  \vdots \\
  c_{i_w}
  \end{array}\right]}_{\symbf c \in \bF^{w}}= \symbf 0
  $$

- Since $M$ has linearly dependent columns, $\det(M) = 0$. But note the following fact:
  $$
  M = \underbrace{\left[\begin{array}{ccc}
  1 & \cdots & 1 \\
  \omega^{i_1} & \ldots & \omega^{i_w} \\
  \vdots & & \vdots \\
  \omega^{i_1(w-1)} & \ldots & \omega^{i_w(w-1)}
  \end{array}\right]}_{\text {Vandermonde }} \operatorname{diag}(\omega^{i_1 b}, \ldots, \omega^{i_w b}) \implies \det(M) \neq 0
  $$

**BCH codes** are cyclic codes designed based on the BCH bound by the following procedure.

- Given finite field $\bF = \bF_q$, and $n \in \N^+$ where $x^n -1 \in \bF[x]$ is separable.
  - For $n = q^m - 1$, the code $C$ is **primitive BCH code**. $U_n = \bF_{q^m}^*$ in this case.
- Find a primitive $n$-th root of unity $\omega \in \Omega_n$. Then $U_n = \a{\omega} = \c{\omega^1, \ldots, \omega^{n}}$.
- Let $m_j := \irr(\omega^j, \bF)$. Then $(x^n - 1) = \lcm(m_1, \ldots, m_n)$.
- Choose $b$ and $\delta$. Therefore the generator polynomial is $g(x) = \lcm(m_{b}, \ldots, m_{b + \delta - 2})$.
  - For $b = 1$, the code $C$ is a **narrow-sense BCH code**.

The BCH bound guarantees that the designed code satisfies $d(C) \ge \delta(C) \ge \delta$.

