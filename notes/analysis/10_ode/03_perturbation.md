##### IVP: Equivalent forms of Ck differentiability theorem

 ^ck-equivalance

Take parameterized IVP for $x \in C^1(J \subseteq \R \to \R^n)$:
$$
x'(t) = f(t, x(t), \lambda), \quad x_{\lambda_0}(t_0) = x_0, \quad f \in C^k(U \subseteq \R \times \R^{n} \times \R^{m} \to \R^n), \quad(*)
$$
where $U$ is open and $(t_0, x_0, \lambda_0) \in U$.

The theorem states that:
1. There exists open box $I \times B \times \Lambda \subset U$ with center $(t_0, x_0, \lambda_0)$ where the unique general solution $\Phi(t, s, x, \lambda): I \times I \times B \times \Lambda \to \R^n$ exists.

2. $D_1 \Phi(t, s, x, \lambda) \in C^k$ and $\Phi(t, s, x, \lambda) \in C^k$.

3. $D_2\Phi(t, (s, x, \lambda))$ (using grouped variables) is the solution of the **first variational equation**:
    $$
    \psi'(t) = A(t, (s, x, \lambda)) \psi(t), \quad A(t, (s, x, \lambda)) = D_2 f(t, \Phi(t, (s, x, \lambda)), \lambda), \quad \psi(s) = \mathbb I
    $$
    where $(s, x, \lambda)$ are viewed as a group of constants in the ODE.
    
    - The definition is motivated as following:
        - Assume $D_1 D_2 \Phi(t, (s, x, \lambda)) = D_2 D_1 \Phi(t, (s, x, \lambda))$.
        - $D_1 D_2 \Phi(t, (s, x, \lambda)) = D_2 D_1 \Phi(t, (s, x, \lambda)) = D_2 f(t, \Phi(t, (s, x, \lambda)), \lambda) D_2 \Phi(t, (s, x, \lambda))$.
    - Matrix function $A(t, s, x, \lambda)$ is uniformly continuous on $\overline{I \times I \times B \times \Lambda}$.
    - Since the variational ODE is linear, it has unique solution on $I$ for any $(s, x, \lambda)$.
    - It can be shown that $D_2 \Phi(t, (s, x, \lambda)) = \psi(t)$.
        - Therefore $D_1 D_2 \Phi(t, (s, x, \lambda)) = D_2 D_1 \Phi(t, (s, x, \lambda))$ is actually satisfied.

Modifications of the above theorem for non-parameterized, or autonomous IVPs should be apparent, therefore omitted.
Due to Parameter Transform and Autonomous Transform, all forms of this theorem are equivalent!

##### IVP: Ck differentiability

Due to above equivalence result, we only need to consider autonomous IVPs.

Consider the following autonomous IVP for $x \in C^1(U \subseteq \R \to \R^{n})$:
$$
x'(t) = f(x(t)), \quad x(0) = x_0, \quad f \in C^1(U \subseteq \R^n \to \R^n)
$$
where $U$ is open and $x_0 \in U$.
- Since $f \in C^1(U \to \R^n$, $f(x)$ is Lipschitz continuous on any compact set.
- There exists $I = (-T, T)$ and $B = B(x_0, \delta)$ such that $I \times B \subset U$ and there exists general solution $\varphi(t, x): I \times B \to \R^n$.
    - $\varphi$ is Lipschitz continuous on $I \times B$.
    - $D_1\varphi(t, x) \in C^1$ since $D_1 \varphi(t, x) = f(\varphi(t, x))$.
- We can try to derive $D_2 \varphi(t, x)$ assuming $[\varphi]_t$ is differentiable for all $t \in I$.
    - $D_1 D_2 \varphi(t, x) = D_2 D_1 \varphi(t, x) = D f(\varphi(t, x)) D_2 \varphi(t, x)$.
        - The first equality depends on swapping partial derivatives. This is indeed true when $f \in C^1$.
    - Define $A(t, x) = Df(\varphi(t, x)): I \times B \to \R^{n \times n}$.
    - Therefore $D_2 \varphi(t, x)$ satisfies IVP $\psi'(t) = A(t, x) \psi(t)$ with $\psi(0) = \mathbb I$.
    - Let $\psi(t)$ be the unique solution on $I$.
- We can show that $\varphi(t, x)$ is differentiable in $x$ on $B$. And $D_2\varphi(t, x) = \psi(t)$.
    - We will abbreviate $\varphi(t, x) = \varphi(t)$.
    - Define $\theta(t, h) = (\varphi(t, x + h) - \varphi(t, x) - \psi(t) h) / \n{h}$.
    - We only need to show $\lim_{h \to 0} \theta(t, h) = 0$.
    - Since $f \in C^1(U \to \R^n)$, we have
        - $f(y)-f(x)= f'(x)(y-x)+R(y, x)(y - x)$.
        - Where $R(y ,x) := \int_{0}^{1}\left(f'(x+t(y-x))-f'(x)\right) \dd t$.
        - $\n{R(y, x)} \leq \max_{t \in[0,1]}\n{f'(x+t(y-x))-f'(x)}$.
            - Hint: Use the definition of Riemann integral to prove this fact.
        - $\lim_{y \to x} \n{R(y, x)} = 0$ uniformly for $x \in B$.
    - In following derivation, we view $x, h$ as constants.
        - Define $v(t) = \varphi(t, x + h)$ and $u(t) = \varphi(t, x)$.
        - Then $\theta(t) = (v(t) - u(t) - \psi (t) h) / \n{h}$.
        - $\theta'(t) = (f(v(t)) - f(u(t)) - A(t)\psi(t) h) / \n{h}$.
        - $\theta'(t) = (f'(u)(v - u) + R(v, u)(v - u) - A \psi h) / \n{h}$.
        - $\theta'(t) = A \theta + R(v, u)(v - u) / \n h$.
        - $\theta'(t)$ is continuous on $[-T, T]$ and $\theta(0) = 0$.
        - Integrate from $0 \to t$. W.L.O.G. consider $t > 0$. (The case where $t < 0$ follows from symmetry.)
        - $\theta(t) = \int_0^t A(s)\theta(s) \dd s + \int_0^t R(v, u)(v - u) \dd s / \n{h}$.
        - $\n{\theta(t)} \le \int_0^t \n{A(s)}\n{\theta(s)} \dd s + \int_0^t \n{R(v, u)} \n{v - u} \dd s / \n h$.
        - Recall that $\n{v - u} \le \n{h}e^{LT}$.
            - $\n{\theta(t)} \le \int_0^t \n{A(s)}\n{\theta(s)} \dd s + C(x, h)$.
            - Where $C(x, h) =e ^{L T} \int_{0}^{T}\n{R(v(s), u(s))} \dd s$.
        - $\n{\theta(t)} \le C(x, h) \exp\left( \int_0^T \n{A(s)} \dd s\right)$ by Gronwell's inequality.
    - Clearly $C(x, h) \to 0$ as $h \to 0$ for all $x \in B$.
- $\varphi(t, x) \in C^1(I \times B \to \R^n)$.
    - $D_2\varphi(t, x) = \psi(t)$ for $(t, x) \in (-T, T) \times B$.
    - Since $\psi(t)$ is continuous in initial condition $x$, so is $D_2 \varphi(t, x)$.
    - Since $\psi(t)$ is continuously differentiable in $t$, so is $D_2 \varphi(t, x)$.
- When $f \in C^k(U \to \R^n)$, $\varphi(t, x) \in C^k(I \times B \to \R^n)$, for $k \ge 1$.
    - The case $k = 1$ is already shown above. Proceed with induction.
    - If the result is true for $k$, so $\varphi(t, x) \in C^k(I \times B \to \R^n)$. Let $f \in C^{k + 1}$.
    - $D_1 \varphi(t, x) \in C^k(I \times B \to \R^n)$.
        - Since $D_1 \varphi(t, x) = f(\varphi(t, x))$.
    - $D_2 \varphi(t, x) \in C^{k}(I \times B \to \R^{n \times n})$.
        - $A(t, x) = Df(\varphi(t, x)) \in C^k(I \times B \to \R^n)$.
        - $D_2 \varphi(t, x) = \psi(t)$ is the solution of $\psi'(t) = A(t, x) \psi(t)$.
    - Therefore $\varphi(t, x) \in C^{k + 1}$.









