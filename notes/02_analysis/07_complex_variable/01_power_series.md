#### Holomorphic Functions

##### Open regions

Recall that open connected sets in $\C$ are **path-connected**.

- There exists a polygonal path with finite segments between two points. 

Open connected sets in $\C$ are called **regions**.

##### Annulus

Define closed annulus $A \s{a; r_1, r_2} := \c{z: r_1 \le \abs{z - a} \le r_2} \subseteq \C$.

Define open annulus $A \p{a; r_1, r_2} := \c{z: r_1 < \abs{z - a} < r_2} \subseteq \C$.

##### Complement of graphs

Suppose $\gamma$ is a path. $\Gamma$ is its curve. $\Gamma$ is compact. So $\C - \Gamma$ is a open set.

$\C - \Gamma$ is the union of countably many open connected components $O_k$.

Open set $O \in \R^n$ is said to be connected to $\infty$ if there is a path going to infinity.

Clearly only one of the $O_k$ is connected to $\infty$. Only this component is unbounded. Call this component the **outer component** of $\C - \Gamma$.

##### Complex valued functions

We identify $\R^2 \simeq \C$ in complex analysis.

Suppose $f: S \subseteq \mathbb C \to \mathbb C$. We also view $f: S \subseteq \R^2 \to \R^2$.
$$
f(z) = f(x + iy) = f(x, y) = (u(x, y), v(x, y)) = (u(z), v(z)) = u(z) + iv(z)
$$

##### Holomorphic

Consider $f: S\subseteq \C \to \C$. Where
$$
f(x + iy) = f(x, y) = u(x, y) + i v(x, y) = (u(x, y), v(x, y))
$$
$f$ is **holomorphic** at $c \in S^\circ$ if it is differentiable when viewed as $\C \to \C$ function.

- Suppose $f'(c) = a + bi$, and rewrite $h = (x + yi)$, we have:
  $$
  \begin{aligned}
  f(c + h) & = f(c) + f'(c) h + o(\n{h})\\
  f(c + h) & = f(c)  + (a + bi) (x + yi) + o(\n{(x, y)})
  \end{aligned}
  $$
- So $f$ is differentiable (viewing as a $\R^2 \to \R^2$ function), with derivative
  $$
  Df(c) = \s{
  \begin{array}{cc}
  a &-b \\
  b &a
  \end{array}
  }; \quad \det Df (c) = a^2 + b^2 = \n{f'(c)}^2
  $$
- The following relationship guarantees the working of chain rule is "consistent":
  $$
  (a_1 + b_1 i)(a_2 + b_2 i) = (a_1 a_2 - b_1 b_2) + (a_1 b_2 + a_2 b_1) i\\
  \s{
  \begin{array}{cc}
  a_1 &-b_1 \\
  b_1 &a_1
  \end{array}
  }
  \s{
  \begin{array}{cc}
  a_2 &-b_2 \\
  b_2 & a_2
  \end{array}
  } = \s{
  \begin{array}{cc}
  a_1 a_2 - b_1 b_2 & -a_1 b_2 - a_2 b_1 \\
  a_1 b_2 + a_2 b_1 & a_1 a_2 - b_1 b_2
  \end{array}
  }
  $$

Suppose $u_x(c) = v_y(c)$ and $u_y(c) = - v_x(c)$, $f$ is said to satisfies the **Cauchy-Riemann condition** at $c$.

##### Primitive function

Suppose $F, f: \Omega \subseteq \C \to \C$.

$F$ is a primitive of $f$ on $\Omega$ if $F$ is holomorphic on $\Omega$ and $\forall z \in \Omega: F'(z) = f(z)$.

#### Power Series

##### Power series

Suppose $a_n, z, z_0 \in \C$:
$$
f(z) = \sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}
\quad
f_n(z) = \sum_{k=0}^n a_n(z-z_0)^n
$$
The RHS is a **power series** in $(z - z_0)$.

By replacing $(z - z_0)^n$ with $(z - z_0)^{-n}$ we will obtain similar results. We call these outer power series.

##### Disk of Convergence I

Consider complex series $\sum a_n z^n$.

Examine $\sqrt[n]{\abs{a_n z^n}} = \abs{z} \sqrt[n]{\abs{a_n}}$. Denote $\gamma_n := \sqrt[n]{\abs{a_n}}$. Define
$$
\frac{1}{r}:=\limsup _{n \rightarrow \infty} \sqrt[n]{\left|a_{n}\right|}
$$


- $\sum_{n=0}^{\infty} |a_{n}|\left|z-z_{0}\right|^{n}$ converges if $|z - z_0| < r$. The **disk of convergence** is $B(z_0, r) = D$.
- The series diverges if $|z - z_0| > r$.
- The series **converges uniformly** on all **compact subset** $S$ inside $B(z_0, r)$.
  - $f_n$ are continuous on $D$, so $f$ must be continuous on $D$.
- Denote $\eta_n = a_n / a_{n + 1}$ for $n \ge 1$, then:
  $$
  \liminf_{n \to \infty} \abs{\eta_n} \le r \le \limsup_{n \to \infty}\abs{\eta_n}
  $$
  - Suppose $\abs{\eta_n}$ converges, the limit is the radius $r$.

##### Shift of center in power series

Suppose $f(z) = \sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}$ has convergence radius $r_0$.

Suppose $B(z_1, r_1) \subseteq B(z_0, r_0)$​. For $z \in B(z_1, r_1)$, we have:

$$
\begin{aligned}
f(z) = \sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n} &=\sum_{n=0}^{\infty} a_{n}\left(z-z_{1}+z_{1}-z_{0}\right)^{n} \\
&=\sum_{n=0}^{\infty} a_{n} \sum_{k=0}^{n}\left(\begin{array}{l}
n \\
k
\end{array}\right)\left(z-z_{1}\right)^{k}\left(z_{1}-z_{0}\right)^{n-k}\\
&= \sum_{k=0}^{\infty} \left (\sum_{n=k}^{\infty}\left(\begin{array}{l}
n \\
k
\end{array}\right) a_{n}\left(z_{1}-z_{0}\right)^{n-k}\right)\left(z-z_{1}\right)^{k}\\
&= \sum_{k = 0}^\infty b_k (z - z_1)^k = b_0 + \sum_{k=1}^\infty b_k (z - z_1)^k
\end{aligned}
$$

- The new coefficients are
  $$
  b_k = \sum_{n=k}^{\infty}\left(\begin{array}{l}n \\k \end{array}\right) a_{n}\left(z_{1}-z_{0}\right)^{n-k};\quad b_0 = f(z_1)
  $$
- Exchanging the sum in the middle requires $z \in B(z_1, r_1) \subseteq B(z_0, r_0)$.
- The derivation is only true inside $B(z_1, r_1)$.

##### Derivatives of the Power Series

Continue with the above derivation.

Suppose $z \in U(z_1, r_1) \subset B(z_0, r_0)$ we have
$$
\frac{f(z) - f(z_1)}{z - z_1} = \sum_{k=0}^\infty b_{k+1}(z - z_1)^{k}
$$
Notice that $\sum_{k=0}^\infty b_{k+1}(z - z_1)^{k}$ has radius $r_1$, and is continuous at $z_1$.

Take limit to $z_1$ on both side. So $f'(z_1)$ is defined. $f$ is differentiable on $B(z_0, r_0)$.
$$
f'(z_1) = b_1 = \sum_{n=1}^{\infty}n a_{n}\left(z_{1}-z_{0}\right)^{n-1}
$$
Notice that $f'(z) = \sum_{n=1}^{\infty}n a_{n}\left(z-z_{0}\right)^{n-1}$ also has convergent radius $r_0$.

Repeat this process, we have
$$
f^{(k)}(z_1)= k! b_k =\sum_{n=k}^{\infty} \frac{n !}{(n-k) !} a_{n}\left(z_1-z_{0}\right)^{n-k}
$$
Clearly $f(z) \in C^\infty[B(z_0, r_0)]$.

##### Complex exponential

Recall $e^x = \sum_{n=0}^\infty x^n / n!$, this series converges for all $x \in \R$.

Now extend the definition to $z \in \C$.

- $e^z$ is well-defined, since $\sum z^n / n!$ is absolutely convergent.
- The power series has convergence radius $\infty$.
- $e^{z}e^{w} = e^{z + w}$.
  $$
  e^{z + w} = \sum_{n = 0}^\infty \frac{(z + w)^n}{n!} = \sum_{n = 0}^\infty \sum_{m = 0}^\infty \frac{z^m}{m!} \cdot \frac{w^{n-m}}{(n-m)!} = e^z e^w
  $$
- Let $\theta \in [0, 2\pi)$, then we obtain **Euler's formula**:
  $$
  e^{i\theta} = \sum_{n=0}^\infty \frac{(i\theta)^n}{n!} = \sum_{n=0}^\infty \frac{(-1)^n  \theta^{2n}} {(2n)!} + i \sum_{n=0}^\infty \frac{(-1)^n\theta^{2n + 1}}{(2n +1)!} = \cos \theta + i \sin \theta
  $$

##### Analytic function

$f: S \subseteq \C \to \C$ is **analytic** at $c \in S^\circ$ if in some $B(c, r)$, $f = \sum a_n (z - c)^n$.

$f: S \subseteq \C \to \C$ is **outer analytic** at $c$ if in some $A(c; r, \infty)$, $f = \sum_{n=0}^\infty a_{-n} (z - c)^{-n}$.

##### Power series is completely encoded in derivatives

Suppose $f(z) = \sum_{n=0}^{\infty} a_{n}\left(z-z_{0}\right)^{n}$ in some $B(z_0)$.

The coefficients $\p{a_n}$ are completely determined by the derivatives.
$$
f(z)=\sum_{n=0}^{\infty} \frac{f^{(n)}(z_{0})}{n !}\left(z-z_{0}\right)^{n}
$$

##### Transformation of power series

Suppose $f(z)=\sum_{n=0}^{\infty} a_{n} z^{n}$ on $B(0, r_a)$ and $g(z)=\sum_{n=0}^{\infty} b_{n} z^{n}$ on $B(0, r_b)$.

- Addition. Converge at least in $B(0, r_a) \cap B(0, r_b)$.
  $$
  f(z) + g(z) = f(z) g(z)=\sum_{n=0}^{\infty} (a_{n}+b_n) z^{n}
  $$
- Multiplication. Converge at least in $B(0, r_a) \cap B(0, r_b)$.
  $$
  f(z) g(z)=\sum_{n=0}^{\infty} (a*b)_n z^{n}=\sum_{n=0}^{\infty} \left( \sum_{k=0}^n a_k b_{n-k}\right) z^{n}
  $$
  - Convergence is guaranteed by Merten's convergence theorem.
- Take power $p$. Convergence at least in $B(0, r_a)$.
  $$
  f(z)^p = \sum_{n=0}^\infty \left( \sum_{m_{1}+\cdots+m_{p}=n} a_{m_{1}} \cdots a_{m_{p}}\right) z^n = \sum_{n=0}^\infty a_n^{(p)} z^n
  $$
- Substitution. Convergence at least in $g^{-1}[B(0, r_a)] \cap B(0, r_b)$.
  $$
  f[g(z)] = \sum_{n=0}^\infty a_n g(z)^n = 
  \sum_{n=0}^\infty a_n \left (\sum_{k=0}^\infty b_k^{(n)} z^k \right)
  = \sum_{k=0}^\infty \left(\sum_{n=0}^\infty a_k b_k^{(n)}\right) z^n
  $$
  - The interchange is justified by Fubini's theorem.
- Reciprocal. Suppose $f(0) = a_0 \neq 0$. Converge in some $B(0, r_c) \subseteq B(0, r_a)$.
  $$
  \frac{1}{f(z)} = \frac{1}{a_n} + \sum_{n=1}^\infty c_n z^n
  $$
  - $1/f$ is holomorphic in some neighborhood, therefore analytic.
