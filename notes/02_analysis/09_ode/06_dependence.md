#### Sensitivity Analysis

Sensitivity analysis is a set of techniques used to study how the behavior of a system (in our case, the solution of an IVP) changes when its initial conditions or parameters are perturbed. By understanding the sensitivity of a system, we can gain insights into its stability, robustness, and performance under various conditions.

One common approach to sensitivity analysis for IVPs is to use variational equations, which are derived by linearizing the system of differential equations around the original solution. This linearization helps us understand how small perturbations in the initial conditions propagate through the system over time.

The simplest variational equation, called the first-order variational equation, deals with the first derivative of the solution with respect to the initial condition. Higher-order variational equations involve higher-order derivatives and can provide more information about the sensitivity of the system.

##### IVP: $C^1$ differentiability theorem

Consider the following autonomous IVP for $x \in C^1(J \subseteq \R \to \R^{n})$:
$$
\boxed{x'(t) = f(x(t)), \quad x(0) = x_0, \quad f \in C^1(U \subseteq \R^n \to \R^n)}
$$
where $U$ is open and $x_0 \in U$.

- Clearly $f$ is locally Lipschitz continuous.
  
- There exists $I = (-T, T)$ and $B = B(x_0, \delta)$ such that $\overline{I \times B} \subset U$ and there exists general solution $\varphi(t, x): I \times B \to \R^n$.
  
  - $\varphi$ is Lipschitz continuous on $I \times B$.
  - $D_1\varphi(t, x) \in C^1$ since $D_1 \varphi(t, x) = f(\varphi(t, x))$.
  
- If $D_2 \varphi (t, x)$ exists for all $(t, x) \in I \times B$, $D_2 \varphi(t, x)$ is the solution to the **first variational equation**
  $$
  \boxed{\psi'(t, x) = f'(\varphi(t, x)) \psi(t, x), \quad \psi(0, x) = \I, \quad f'(\varphi(\cdot, x)) \in C(I \to \R^{n \times n})}
  $$
  - $D_1 D_2 \varphi(t, x) = D_2 D_1 \varphi(t, x) = f'(\varphi(t, x)) D_2 \varphi(t, x)$.
    - The first equality depends on swapping partial derivatives. This is indeed true when $f \in C^1$.
  
- Let $\psi(t, x)$ the solution of the first variational equation on $I$ given $x \in B$ as a constant.

- We can show that $D_2 \varphi(t, x) = \psi(t, x)$ for all $(t, x) \in I \times B$.
  - Denote $\Delta\varphi(t, x, h) :=\varphi(t, x + h) - \varphi(t, x)$.
  
  - Define $\theta: I \times B \times  B(0, \delta) \to \R^n$. We only need to show that $\lim_{h \to 0} \theta(t, h) = 0$ for all $t \in I$.
    $$
    \theta(t, x, h) = \frac{\Delta\varphi(t, x, h) - \psi(t, x) h}{\n{h}}
    $$
  
  - Denote $D_1 \theta(t, x, h)$ as $\theta' (t, x, h)$. Then
    $$
    \theta'(t, x, h) = \frac{f(\varphi(t, x + h)) - f(\varphi(t, x)) - f'(\varphi(t, x))\psi(t, x) h}{\n{h}}
    $$
  
  - Define $R(y, x): B \times B \to \R^n$ as
    $$
    R(y, x) := \int_{0}^1\p{f'(x + \tau (y - x)} - f'(x) \dd \tau
    $$
  
  - Since $f \in C^1(U \to \R^n)$, $f'$ is bounded and uniformly continuous on $B$. Therefore
    $$
    \n{R(y, x)} \le \max_{\tau \in [0, 1]} \n{f'(x + \tau(y - x)) - f'(x)}
    $$
  
  - Therefore $\n{R(y, x)} \to 0$ uniformly on $B$ as $y \to x$.
    
  - Observe that $f(y) - f(x)$ can be decomposed in the following way
    $$
    f(y) - f(x) = (y - x)\int_0^1 f'(x + \tau(y - x))  \dd \tau = f'(x)(y - x) + R(y, x) (y - x)\\
    $$
  
  - Then $\theta'(t, x, h)$ can be further transformed, 
    $$
    \begin{aligned}
    \theta'(t, x, h) &= \frac{\s{f'(\varphi(t, x)) + R(\varphi(t, x + h), \varphi(t, x))}\Delta\varphi(t, x, h) - f'(\varphi(t, x)) \psi(t, x) h}{\n{h}}\\
    & = f'(\varphi(t, x)) \theta(t, x, h) + \frac{R(\varphi(t, x + h), \varphi(t, x))\Delta \varphi(t, x, h)}{\n h}
    \end{aligned}
    $$
  
  - It is easy to see that $\theta'(t, x, h)$ is **continuous** in $t$. Also notice that
    $$
    \theta(0, x, h) = \frac{\Delta\varphi(0, x, h) - \psi(0, x) h}{\n{h}} = \frac{h - h}{\n{h}} = 0
    $$
  
  - With integration on both sides, we have for $t \in I$:
    $$
    \theta(t, x, h) = \int_0^t f'(\varphi(\tau, x)) \theta(\tau, x, h) \dd \tau + \frac{1}{\n{h}}\int_0^t R(\varphi(\tau, x + h), \varphi(\tau, x)) \Delta \varphi(\tau, x, h) \dd \tau
    $$
  
  - Now take norm on both sides, for $t \in I$:
    $$
    \n{\theta(t, x, h)} \le \int_0^t \n{f'(\varphi(\tau, x))} \n{\theta(\tau, x, h)} \dd \tau + \frac{1}{\n{h}}\int_0^t \n{R(\varphi(\tau, x + h), \varphi(\tau, x))}\n{\Delta\varphi(\tau, x, h)} \dd \tau
    $$
  
  - From previous discussion about the Lipschitz continuity of $\varphi(t, x)$, we have
    $$
    L = \sup_{x \neq y \in B} \frac{f(x) - f(y)}{|x - y|} \implies \forall t \in I, \forall x, y \in B:\n{\varphi(t, x) - \varphi(t, y)} \le \n{x - y} e^{LT}
    $$
    
  - Define $C(x, h): B \times B(0, \delta) \to \R$ as following:
    $$
    C(x, h):= e^{LT}\int_0^T \n{R(\varphi(\tau, x + h), \varphi(\tau, x))} \dd \tau
    $$
  
  - Therefore
    $$
    \n{\theta(t, x, h)} \le \int_0^t \n{f'(\varphi(\tau, x))} \n{\theta(\tau, x, h)} \dd \tau + C(x, h)
    $$
  
  - Now apply Gronwall's inequality, for some $K > 0$, we have
    $$
    \n{\theta(t, x, h)} \le C(x, h) \exp\p{\int_0^T \n{f'(\varphi(\tau, x)} \dd \tau} \le C(x, h) e^{T K}
    $$
  
  - Since $C(x, h) \to 0$ as $h \to 0$ for all $x \in B$. We have
    $$
    \forall t, x \in I \times B: \lim_{h \to 0} \n{\theta(t, x, h)} = 0
    $$
  
- $\varphi(t, x) \in C^1(I \times B \to \R^n)$.
  - Since $\psi(t, x)$ is the solution to the first variational equation $\psi(t, x)$ is continuous in $x$.
  - Since $D_2\varphi(t, x) = \psi(t, x)$ for $(t, x) \in I \times B$, $\varphi(t, x)$ is continuously differentiable in $x$.
  - As the general solution $\varphi(t, x)$ is continuously differentiable in $t$.

##### IVP: $C^k$ differentiability theorem

Consider the following autonomous IVP for $x \in C^1(J \subseteq \R \to \R^{n})$:
$$
\boxed{x'(t) = f(x(t)), \quad x(0) = x_0, \quad f \in C^k(U \subseteq \R^n \to \R^n)}
$$
where $U$ is open and $x_0 \in U$. Continue above discussion.

- Clearly $f$ is locally Lipschitz continuous.
- There exists $I = (-T, T)$ and $B = B(x_0, \delta)$ such that $\overline{I \times B} \subset U$ and there exists general solution $\varphi(t, x): I \times B \to \R^n$.
  - $\varphi(t, x) \in C^1$ according to the $C^1$ differentiability theorem.
  - $D_1\varphi(t, x) \in C^1$ since $D_1 \varphi(t, x) = f(\varphi(t, x))$.

We can demonstrate that $\varphi(t, x) \in C^k$, and $D_1 \varphi(t, x) \in C^k$. Let's proceed with induction.

- Suppose the result is true for $k$ now consider $f \in C^{k + 1}$.
- $D_1 \varphi(t, x) = f(\varphi(t, x)) \in C^{k}$.
- $D_2 \varphi(t, x) \in C^k$.
  - $f'(\varphi(t, x)) \in C^k$. Since $f' \in C^k$ and $\varphi(\cdot, \cdot) \in C^k$.
  - $D_2 \varphi(t, x)$ is the solution of $\psi'(t, x) = f'(\varphi(t, x)) \psi(t, x)$.
  - By induction hypothesis, $D_2 \varphi(t, x) \in C^k$.
- Therefore $\varphi(t, x) \in C^{k + 1}$.

##### IVP: Equivalent forms of $C^1$ differentiability theorem

Consider the following parameterized IVP for $x \in C^1(J \subseteq \R \to \R^n)$:
$$
\boxed{x'(t) = f(t, x(t), \lambda), \quad x_{\lambda_0}(t_0) = x_0, \quad f \in C^k(U \subseteq \R \times \R^{n} \times \R^{m} \to \R^n)}
$$
where $U$ is open and $(t_0, x_0, \lambda_0) \in U$.

- There exists open box $I \times B \times \Lambda \subset U$ with center $(t_0, x_0, \lambda_0)$ where the unique general solution $\Phi(t, (s, x, \lambda)): I \times (I \times B \times \Lambda) \to \R^a$ exists.
- $D_1 \Phi(t, (s, x, \lambda)) \in C^k$ and $\Phi(t, (s, x, \lambda)) \in C^k$.
  - $D_1 D_2 \Phi(t, (s, x, \lambda)) = D_2 D_1 \Phi(t, (s, x, \lambda))$.
  - $D_1 D_2 \Phi(t, (s, x, \lambda)) = D_2 D_1 \Phi(t, (s, x, \lambda)) = D_2 f(t, \Phi(t, (s, x, \lambda)), \lambda) D_2 \Phi(t, (s, x, \lambda))$.

Due to the equivalence of parameterized IVP and homogeneous IVP, we could derive the generalized first variational equation. But the notation may be a little tricky. Denote $a := n + m + 1$.

- Define $\Psi(t, (s, x, \lambda)) := (t, \Phi(t, (s, x, \lambda)), \lambda): J \times\R^{a} \to \R^a$.

- Define $F(t, x, \lambda):= (t, f(t, x(t), \lambda), \lambda): \R^a \to \R^a$.

- Then $D_2\Psi(t, (s, x, \lambda))$ is the solution of the **first variational equation**:
  $$
  \boxed{
  \begin{aligned}
  \psi'(t, (s, x, \lambda)) & = A(t, (s, x, \lambda)) \psi(t, (s, x, \lambda))\\
  A(t, (s, x, \lambda)) &:= J_F(t, \Phi(t, (s, x, \lambda)), \lambda), \quad \psi(s, (s, x, \lambda)) = \I_{a}
  \end{aligned}
  }
  $$

- $A(t, (s, x, \lambda))$ has the following blocked structure by definition of $F$:
  $$
  A(t,(s, x, \lambda))=
  \s{
  \begin{array}{ccc}
  1 & 0 & 0 \\
  D_1 f(t, \Phi(t,(s, x, \lambda)), \lambda) & D_2 f(t, \Phi(t,(s, x, \lambda)), \lambda) & D_3 f(t, \Phi(t,(s, x, \lambda)), \lambda) \\
  0 & 0 & \I_{m}
  \end{array}
  }
  $$

- $D_2 \Psi(t, (s, x, \lambda))$ or the solution $\psi(t, (s, x, \lambda))$ has the following structure:
  $$
  \psi(t, (s, x, \lambda)) =D_2 \Psi(t, (s, x, \lambda)) =
  \s{
  \begin{array}{ccc}
  0 & 0 & 0 \\
  \frac{\part \Phi(t, (s, x, \lambda))}{\part s} & \frac{\part \Phi(t, (s, x, \lambda))}{\part x} & \frac{\part \Phi(t, (s, x, \lambda))}{\part \lambda} \\
  0 & 0 & \I_{m}
  \end{array}
  }
  $$

Now the original variational equation can be split into three equations through blocked matrix product:

- Matrix function $A(t, s, x, \lambda)$ is uniformly continuous on $\overline{I \times I \times B \times \Lambda}$.

- Since the first variational equation is linear, it has unique solution on $I$ for any $(s, x, \lambda)$.

- The first equation is related to the sensitivity with respect to the initial time $s$:
  $$
  \begin{aligned}
  \frac{\dd}{\dd t} \frac{\partial \Phi(t,(s, x, \lambda))}{\partial s} & = D_2 f(t, \Phi(t,(s, x, \lambda)), \lambda) \frac{\partial \Phi(t,(s, x, \lambda))}{\partial s}\\
  \frac{\partial \Phi(s,(s, x, \lambda))}{\partial s} & = 0 \in \R^{n\times 1}
  \end{aligned}
  $$

- The second equation is related to the sensitivity with respect to the initial state $x$:
  $$
  \begin{aligned}
  \frac{\dd}{\dd t} \frac{\partial \Phi(t,(s, x, \lambda))}{\partial x} & = D_2 f(t, \Phi(t,(s, x, \lambda)), \lambda) \frac{\partial \Phi(t,(s, x, \lambda))}{\partial x}\\
  \frac{\partial \Phi(s,(s, x, \lambda))}{\partial x} & = \I_n \in \R^{n\times n}
  \end{aligned}
  $$

- The third equation is related to the sensitivity with respect to the parameter $\lambda$:
  $$
  \begin{aligned}
  \frac{\dd}{\dd t} \frac{\partial \Phi(t,(s, x, \lambda))}{\partial \lambda} & = D_2 f(t, \Phi(t,(s, x, \lambda)), \lambda) \frac{\partial \Phi(t,(s, x, \lambda))}{\partial \lambda} + D_3 f(t, \Phi(t,(s, x, \lambda)), \lambda)\\
  \frac{\partial \Phi(s,(s, x, \lambda))}{\partial \lambda} & = 0 \in \R^{n\times m}
  \end{aligned}
  $$

