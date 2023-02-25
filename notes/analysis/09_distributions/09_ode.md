$$
\newcommand{D}{{\mathcal D}}
\newcommand{H}{{\mathcal H}}
\newcommand{G}{{\mathcal G}}
\newcommand{loc}{{\operatorname{loc}}}
\newcommand{M}{\mathcal M}
\newcommand{P}{\mathcal P}
\newcommand{B}{\mathbb B}
\newcommand{E}{\mathcal E}
\newcommand{F}{\mathcal F}
\newcommand{J}{\mathcal J}
\newcommand{A}{\mathcal A}
\newcommand{L}{\mathcal L}
\newcommand{S}{\mathcal S}
\newcommand{su}{\operatorname{supp}}
\newcommand{re}{\operatorname{Re}}
\newcommand{im}{\operatorname{Im}}

\newcommand{pf}{\operatorname{Pf}}
\newcommand{pv}{\operatorname{Pv}}
\newcommand{pd}[2]{\left \langle #1, #2 \right\rangle}
\newcommand{dp}{\mathbf{D}}
\newcommand{ip}{\mathbf{I}}
\newcommand{cas}{\D'_+}
\newcommand{acas}{\D'_-}
\newcommand{f}{\mathfrak F}
\newcommand{fi}{\mathfrak F^{-1}}
\newcommand{Fi}{\mathcal F^{-1}}
\newcommand{l}{\mathfrak L}
\newcommand{li}{\mathfrak L^{-1}}
\newcommand{Li}{\mathcal L^{-1}}
\newcommand{u}{1_+}
$$

### Review: Classical Theory of Linear Ordinary Differential Equations

Consider the following linear ordinary differential equation:
$$
\frac{ d ^{n} x}{ d t^{n}}+a_{1}(t) \frac{ d ^{n-1} x}{ d t^{n-1}}+\cdots+a_{n-1}(t) \frac{ d x}{ d t}+a_{n}(t) x=f(t);\quad (*)\\
\frac{ d ^{n} x}{ d t^{n}}+a_{1}(t) \frac{ d ^{n-1} x}{ d t^{n-1}}+\cdots+a_{n-1}(t) \frac{ d x}{ d t}+a_{n}(t) x=0;\quad (**)
$$
When $f(t) = 0$​​​​​, the LODE is called **homogeneous**, otherwise **nonhomogeneous**.

Assume $a_k(t)$​ and $f(t)$​ are **continuous** on any interval $I$​​ for the following discussion.

----

##### Existence and uniqueness

  given $x^{(k)}(t_0)$​​​​​​​​ for any $t_0 \in I$​​​​​​​​​​​, and $0 \le k < n$​​ there is a **unique solution** in $C^n[t_0, \infty)$ to $(*)$​. (Prove it!)

---

##### Linearity**) Consider the subspace of all solutions $S \subseteq {^{I}\C}$​ to $(

$. 

This is a vector space over $\C$​. Definition of linear independence and basis follows from general infinite dimensional vector spaces.

---

##### Wronskian determinant

 Suppose $x_1(t), \ldots, x_k(t): I \to \C$, and $x_m \in D[I]$, then
$$
W(t)=\left[\begin{array}{cccc}
x_{1}(t) & x_{2}(t) & \cdots & x_{k}(t) \\
x_{1}^{\prime}(t) & x_{2}^{\prime}(t) & \cdots & x_{k}^{\prime}(t) \\
\vdots & \vdots & & \vdots \\
x_{1}^{(k-1)}(t) & x_{2}^{(k-1)}(t) & \cdots & x_{k}^{(k-1)}(t)
\end{array}\right];\quad |W|(t) = |W(t)|
$$
Suppose $x_1, \ldots, x_k$​ are linearly dependent, $|W|(t) = 0$​.

----

Suppose $x_1(t), \ldots, x_k(t)$​​​​ are solutions to $(**)$​​​​​​, then $\exists t \in I :|W|(t) = 0$​​​​ implies $x_1, \ldots, x_k$​​​​​ are linearly dependent.

----

##### Solutions to homogeneous equation

Suppose $x_1, \ldots, x_n$ are $n$ solutions to $(**)$, either they are linearly dependent and $|W|(t) = 0$; Or they are linearly independent, and $|W|(t) \neq 0$ for $t \in I$.

Now consider particular $n$ solutions to the following initial conditions. $t_0 \in I$.
$$
x_{1}\left(t_{0}\right)=1, x_{1}^{\prime}\left(t_{0}\right)=0, \cdots, x_{1}^{(n-1)}\left(t_{0}\right)=0, \\
x_{2}\left(t_{0}\right)=0, x_{2}^{\prime}\left(t_{0}\right)=1, \cdots, x_{2}^{(n-1)}\left(t_{0}\right)=0, \\
\cdots \cdots \cdots \cdots\cdots \cdots\cdots\cdots\cdots\cdots\cdots\cdots\cdots \\
x_{n}\left(t_{0}\right)=0, x_{n}^{\prime}\left(t_{0}\right)=0, \cdots, x_{n}^{(n-1)}\left(t_{0}\right)=1
$$
Since $|W|(t_0) \neq 0$, $x_1, \ldots, x_k$​ are linearly independent.

This is a finite basis of the solution space! The solution space to $(**)$ has dimension $n$!

----

##### Solutions to nonhomogeneous equation $(*)$

- A solution to $(**)$ is a general solution, denoted as $x_g(t)$.
- A solution to $(*)$ is a particular solution, denoted as $x_p(t)$​.
- $x_g + x_p$ gives a particular solution.

Suppose $x_p$ is a particular solution, all solutions to $(*)$ are of the form $x_p + x_g$​.

### Review: Convolutional Algebra

Suppose $\A'$ is a convolutional algebra. Suppose $f, g \in \A'$​​. Consider the equation $f \star u = g$​​. And the solutions in $\A'$​​.

- $f \star u = 0$ is called the **homogeneous equation**.
- Solutions to the $f \star u = 0$ are **general solutions**.
- Solutions to $f \star u = \delta$ are the **elementary solutions**.
- Solutions to $f \star u = g$ are the **particular solutions**.

----

Suppose $f \in \cas$ and $g \in \cas$. Consider the **equation** $f \star u = g$.

- Suppose $f \star u  = g$ always has a solution in $\cas$ for all $g \in \cas$. Then $f$ is invertible.
- Suppose $f$​ is invertible then $u = f^{*,-1} \star g$​ is the unique solution.

---

##### Laplace transform and convolutional equation

Suppose $f \in \cas$​​, we can try to find it's inverse using Laplace transform if it is **Laplace transformable**.

Suppose $f$​ is invertible, then $f \star u = \delta$​ for some $u \in \cas$​​​.

Assume $u$ is Laplace transformable, then $F(s)U(s) = 1$​​.

Suppose $U(s) = 1 / F(s)$​​​ (far right) is the Laplace transform of $u(t)$​​​, then we must have $f \star u = \delta$.

Consider $f \star u = g$, the unique solution is $u = f^{*-1} \star g$. Further suppose $g$ is Laplace transformable. Then $\L[f^{*-1}\star g] = G(s) / F(s)$.

### Constant Coefficient Ordinary Differential Equations

A **CCOD operator** is of the form
$$
L \triangleq a_{n} \frac{d^{n}}{d t^{n}}+a_{n-1} \frac{d^{n-1}}{d t^{n-1}}+\cdots+a_{1} \frac{d}{d t}+a_{0}
$$
where the $a_k \in \C$ are constants, $a_{n} \neq 0$, and $n \geq 1$​.

----

Consider the equation $L u(t)=g(t)$ for $u(t), g(t):\R \to \C$. Convert this into
$$
L \delta=a_{n} \delta^{(n)}+a_{n-1} \delta^{(n-1)}+\cdots \cdot+a_{1} \delta^{(1)}+a_{0} \delta \implies (L \delta) \star u=g
$$

---

(Solution to the **homogeneous equation** $L\delta \star u = 0$​​)

Consider the **characteristic function** of $L$, $P \in \C[D]$. Suppose it has $q$ isolated zeros.
$$
P(D) =a_{n} D^{n}+a_{n-1} D^{n-1}+\cdots+a_{1} D+a_{0} =a_{n} \prod_{\mu=1}^{q}\left(D-\gamma_{\mu}\right)^{k_{\mu}}; \quad \sum_{\mu=1}^{q} k_{\mu}=n
$$
We can obtain a **basis** to the solution space and every **general solution** is of the form:
$$
u(t)=\sum_{\mu=1}^{q} \sum_{\nu=1}^{k_{\mu}} c_{\mu \nu} t^{\nu-1} e^{\gamma_{\mu} t};\quad c_{\mu \nu} \in \C
$$
When providing constraints $t_0 \in I$ and $u^{(k)}(t_0) = u_k$ for $k = 0, \ldots, n - 1$. The initial conditions will **uniquely determine** the coefficients $c_{\mu \nu}$​​​​.

---

##### Solution to the nonhomogeneous equation

 

First find a particular solution $x_p(t)$. Then find the general solution $x_g(t, c_1, \ldots, c_n)$. Solve the unknown coefficients by using the given conditions.

### Distributional Solution of CCODEs

##### Green function

 Consider homogeneous equation $Lu = 0$. Suppose $h(t)$ is a solution that satisfies:
$$
h(0)=h^{(1)}(0)=\cdots=h^{(n-2)}(0)=0; \quad h^{(n-1)}(0)=\frac{1}{a_{n}}
$$
Now $\u(t)h(t) \in \cas(\R)$​ is called the Green function, notice that:
$$
\left(1_{+} h\right)^{(\nu)}=1_{+} h^{(\nu)} \quad \nu=1,2, \ldots, n-1;\quad
\left(1_{+} h\right)^{(n)}=1_{+} h^{(n)}+{ \delta}/{a_{n}}
$$
Therefore $(L\delta) \star (\u h) = L(\u h) = \u(t) (Lh) + \delta = \delta$. So $(\u h) = (L\delta)^{*-1}$.

----

##### Laplace transform and Green function

Clearly $L\delta$​ is **Laplace transformable**, and $F(s)$​ is an entire analytic function and polynomial.
$$
F(s) := \L[L \delta] = a_{n} s^{n}+a_{n-1} s^{n-1}+\cdots+a_{0}
$$
Hence $1/F(s)$ is a Laplace transform of some function, and
$$
(L \delta)^{*-1} =\Li \frac{1}{F(s)} 
=\Li \frac{1}{a_{n} s^{n}+a_{n-1} s^{n-1}+\cdots+a_{0}} \quad \re s>\sigma_{I}
$$
Make a partial fraction of $F(s)$​ and take the inverse Laplace transform gives:
$$
(L\delta)^{*-1} = \u(t) h(t); \quad h(t) = \sum_{\mu=1}^{q} \sum_{\nu=1}^{k_{\mu}} c_{\mu \nu} t^{\nu-1} e^{\gamma_{\mu} t};\quad \sum_{\mu=1}^{q} k_{\mu}=n
$$
Here $\gamma_\mu$ are isolated zeros of $F(s)$ and isolated **poles** of $1/F(s)$.

----

##### Initial value problem using distribution

 

Consider **CCODE** $Lu(t) = g(t)$​​​​​ for some $g(t) \in C[t_0, \infty)$​​​​​. Solve for the **existent and unique** $u(t)$​​​. Give initial conditions $u_k = D^k u(t_0)$​​​ for $0 \le k < n$​​​​​.

Now try to solve this in $\cas(\R)$​. Assume the solution is $\u(t) u(t) \in \cas(\R)$​​. Where $u(t) \in C^n[\R]$.
$$
D^k[\u(t - t_0)u(t)] = \u(t - t_0) u^{(k)}(t) + \sum_{m=0}^{k-1} \delta^{(m)}(t - t_0) u^{(k-m-1)}(t_0)
$$
Suppose $b_{\nu}=a_{\nu+1} u_{0}+a_{\nu+2} u_{1}+\cdots+a_{n} u_{n-\nu-1}$, we have:
$$
L[\u(t-t_{0}) u(t)]=\u(t-t_{0}) g(t)+\sum_{\nu=0}^{n-1} b_{\nu} \delta^{(\nu)}(t-t_{0})
$$
Now convolve both sides with the **Green function** $\u(t) h(t)$ and we get:
$$
\begin{aligned}
\u(t-t_0) u(t)&=\u(t-t_{0}) \int_{t_{0}}^{t} h(t-\tau) g(\tau) d \tau +\sum_{\nu=0}^{n-1} b_{\nu}\left[\u(t-t_{0}) h\left(t-t_{0}\right)\right]^{(v)}\\
&= \u(t-t_{0}) \int_{t_{0}}^{t} h(t-\tau) g(\tau) d \tau + \sum_{\nu=0}^{n-1} b_{\nu} h^{(\nu)}(t-t_{0}) \u(t-t_{0})
\end{aligned}
$$
Hinted by the above derivation, define
$$
u(t) = \int_{t_{0}}^{t} h(t-\tau) g(\tau) d \tau + \sum_{\nu=0}^{n-1} b_{\nu} h^{(\nu)}(t-t_{0}) 
$$
It can be verified that $u(t)$​​ satisfies the requirements, and must be the unique solution as ordinary function.

