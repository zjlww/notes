#### Introduction to ODEs

##### Systems of ODEs

Equations of $x \in C^k(J \subseteq \R \to \R^n)$ of the form 
$$
x_i^{(k)}(t) = f_i(t, x, x^{(1)}, \ldots, x^{(k - 1)}), \quad f_i: V_i \subseteq \R^{nk + 1} \to \R
$$
is called an ODE system of order $k$.
- It is said to be **linear** if it is of the following form
$$
x_i^{(k)}(t) = g_i(t) + \sum_{l=1}^n \sum_{j=0}^{k-1}f_{i,j,l} x_l^{(j)}(t)
$$
- It is said to be **autonomous** if all $f_i$ do not depend on time $t$.
    - Suppose $\phi(t)$ is a solution, the time-shift $\phi(t - t_0)$ remains a solution.
    - W.L.O.G. for initial conditions, we can always assume $t_0 = 0$.

##### First-order 1D autonomous ODE

Consider the following ODE for $x \in C^1(J \subseteq \R \to \R)$.
$$
x'(t) = f(x(t)), \quad x(0) = x_0, \quad f \in C(U \subseteq \R \to \R)
$$
where $U$ is open.

- Now suppose $f(x_0) > 0$.
    - Let $0 \in I = (x_1, x_2)$ be the maximal interval where $\forall x \in I: f(x) > 0$.
    - Define $F(x) = \int_{x_0}^x f(y)^{-1} \dd y$ for $x \in I$.
        - $F(x) \in C^1[I]$, $F(0) = 0$.
        - $F(x)$ is strictly increasing since $\forall x \in I: F'(x) > 0$.
        - Define the range as $F(x_1, x_2) = (T_-, T_+) = T$.
    - Clearly $F(x)$ is invertible. Define $\phi(t) = F^{-1}(t): (T_-, T_+) \to (x_1, x_2)$.
        - $\phi(T_-, T_+)= (x_1, x_2)$.
    - $\phi(t)$ is a solution to the ODE.
        - $F(\phi(t)) = t$ by definition.
        - $\phi'(t)/f(\phi(t)) = 1$ by differentiating it.
        - Therefore $\phi'(t) = f(\phi(t))$.
    - In some cases solution $\phi(t)$ can be extended.
        - W.L.O.G. consider the right hand side only. The negative side can be similarly extended.
        - Suppose $x_2 < \infty$ and certainly $f(x_2) = 0$. And also $T_{+} < \infty$.
        - $F'_-(x_2) = 0$ and $\phi_-(T_+) = 0$.
        - It is possible to extend $\phi$ on the right-side with $\varphi(t)$ where $\varphi'_+(T_+) = 0$.
            - For example, the trivial solution $\phi(t) = x_2$ for $t \ge T_+$.
    - Further suppose $f(x) \in C^1(\R)$. Then $\phi(t)$ is the unique solution satisfying the condition $\phi(0) = x_0$.
        - Suppose $\varphi(t) \in C^1[K \to (x_1, x_2)]$ is a solution to the ODE. Where $K$ is some open interval around $0$ and $K \subseteq T$.
        - $\varphi'(t) = f(\varphi(t))$. Therefore $\varphi'(t) / f(\varphi(t)) = 1$.
        - Integrate over $[0, s]$ on both sides: $F(\varphi(s)) = s$.
        - Therefore $\varphi(t) = \phi(t)$ on $K$. ==This is fishy, TODO==.
- Now consider the case $f(x_0) = 0$.
    - $\phi(t) = x_0$ is one trivial solution for $t \in \R$.
    - Let $I = (0, x_2)$ be the maximal interval where $\forall x \in I: f(x) > 0$.
    - In the case where $x_2 > 0$. Consider $F(x) = \int_{x_0}^x f(y)^{-1} \dd y$ for $x \in I$.
    - Similar to $f(x_0) > 0$ case. $\phi(t) = F^{-1}(x)$ is a solution of the ODE on $I$.
    - Similar to $f(x_0) > 0$ case. Right-side extension is possible.

##### Separable equations

Consider the following separable ODE for $x \in C^1(J \subseteq \R \to \R)$.

$$
x'(t) = f(x(t))g(t), \quad x(t_0) = x_0, \quad f, g \in C^1(\R)
$$
- The situation is more complex compared to first-order homogeneous case.
- Now suppose $f(x_0) \neq 0$.
    - Define $F(x) = \int_{x_0}^x f(y)^{-1} \dd y$ for $x \in I$.
        - $F(x): (x_1, x_2) \to (T_-,T_+)$ in the same way as before.
    - Define $G(t) = \int_{t_0}^t g(s) \dd s$.
    - Suppose a solution $x(t): J \to (x_1, x_2)$ exists. Then
        - $x'(t)/f(x(t)) = g(t)$. So $\int_{t_0}^t x'(t)/f(x(t))\dd t = \int_{t_0}^t g(t) \dd t$ for $t \in J$.
        - That is $F(x(t)) = G(t)$.

##### Exact equations

Consider the following ODE of $y \in C^1(J \subseteq \R \to \R)$.
$$
p(x, y) y' + q(x, y) = 0, \quad p, q \in C^1(\R^2 \to \R)
$$

- When $D_1 p = D_2 q$, the equation is called **exact**.
- There is a unique (up to constant) $F(x, y) \in C^2(\R^2 \to \R)$ s.t. $p = D_2 F$ and $q = D_1 F$.
    - Existence is easy, just integrate along axises.
    - To show uniqueness, suppose $G(x, y)$ is another solution.
    - Notice $F, G \in D^*(\R^2 \to \R)$ and $DF - DG = 0$. Therefore $F - G = c$.
- Therefore $\dd F(x, y(x))/\dd x = p(x, y(x)) y' + q(x, y(x)) = 0$.
- Hence $F(x, y(x)) = c$ for $x \in \R$.

##### Integrating factors

Consider the following ODE of $y \in C^1(J \subseteq \R \to \R)$.
$$
p(x, y) y' + q(x, y) = 0, \quad p, q \in C^1(\R^2 \to \R)
$$
Suppose $\mu(x, y) \in C^1(\R^2 \to \R)$ is making the ODE exact:
$$
\mu(x, y) p(x, y) y' + \mu(x, y)q(x, y) = 0
$$
$\mu(x, y)$ is called an integrating factor.

##### 1D Linear ODE

Consider the following first-order linear ODE of $x \in C^1(J \subseteq \R \to \R)$.
$$
x'(t) = a(t) x(t) + g(t)
$$
- Suppose an integrating factor $\mu(t)$ exists.
- $\mu(t) x'(t) - \mu(t) a(t) x(t) - \mu(t) g(t) = 0$.
- We would require $\mu'(t) = -\mu(t) a(t)$. $\mu(t) = -\exp \int a(t)$ is a solution.
- Therefore $(\mu x)'(t) = (\mu g)(t)$. $\mu x = \int \mu g \dd t + c$.

