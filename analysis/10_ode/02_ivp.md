(**Functional Banach spaces: Review**)

- $C(I \to \bF^m)$ with norm $\n{x} = \sup_{t \in I}\n{x(t)}$ is a Banach space for compact interval $I \subseteq \R$.
    - Since $I$ is compact, all continuous functions are uniformly continuous.
    - $x_n \to x$ in norm if and only if $x_n \rightrightarrows_I x$.
    - Uniform limit of continuous functions on $I$ remains continuous.
    - Cauchy sequences in $C(I)$ clearly converge pointwise due to completeness of $\R^m$.
- $C_b(I \to \bF^m)$ with norm $\n{x} = \sup_{t \in I}\n{x(t)}$ is a Banach space for any interval $I \subseteq \R$.
    - $C_b$ means bounded continuous functions. Boundedness is required to ensure a finite norm.

(**Newton's method**)

Newton's method is a function $\mathcal I(f, x_0)$ that outputs a sequence following iteration $x_{n + 1} = K(x_n)$ where $K(x_n) := x_n - f(x_n) / f'(x_n)$.

Suppose $f \in C^2(S \to \R)$ and $S \subseteq \R$ is open. For $\bar x \in S$ where $f(\bar x) = 0$, and $f'(\bar x) \neq 0$, there is a closed interval $I$ around $\bar x$ such that $K$ is a contractive mapping on $I$.
- W.L.O.G. we can assume $\bar x = 0$. And only conside an open interval of $0$.
- $K'(x) = f(x)\cdot f''(x) / f'(x)^2$ is continuous and $K'(0) = 0$.
- Now solve for $\abs{K(x)} < \abs{x}$.
    - Notice that $K(x) = \int_0^x K'(s) \dd s$. So $\abs{K(x)} < \int_{0}^{\abs{x}}\abs{K'(s)}\dd s$.
    - Since $K'(x)$ is continuous, for some closed interval $[a, b]$ where $a < 0 < b$ we have $0 \le \abs{K'(x)} < c < 1$.
    - Therefore $\abs{K(x)} < c\abs{x}$ in $[a, b]$.
- $K(x)$ is a contractive mapping on $[a, b]$ therefore has unique fixed point $0$.
    - The convergence is guaranteed to be exponential in $[a, b]$.

(**IVP: Picard-Lindelof**)

Consider the following **initial value problem** for $x \in C^1(J \subseteq \R \to \R^n)$: 

$$
x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n)
$$
where $U$ is open and $(t_0, x_0) \in U$.
- Integrate from $t_0 \to t$ on both sides gives $x(t) = x_0 + \int_{t_0}^t f(s, x(s)) \dd s$.
    - This gives an **integral equation** equivalent to the first-order ODE.
- Let **Picard iteration** on $C^1(I \subseteq \R \to \R^n)$ be $K(x(t)) = x_0 + \int_{t_0}^t f(s, x(s)) \dd s$.
    - A fixed point of the iteration is a solution to the ODE on $I$.

Further assume $f$ is locally Lipschitz continuous in second argument, uniformly respect to the first. Then there is a unique local solution.
- There is a unique local solution to the right:
    - Suppose $V = [t_0, t_0 + T] \times \overline{B(x_0, \delta)} \subset U$, for some $\delta > 0, T > 0$.
    
    - Let $M = \max_{(t, x) \in V} \n{f(t, x)}$.
    
    - Let $L=\sup _{(t, x) \neq(t, y) \in V} {\n{f(t, x)-f(t, y)}}/{\n{x-y}}$. And $0 < L^{-1} - \epsilon < L^{-1}$.
    
    - Let $T_0 = \min(T, \delta/ M, L^{-1} - \epsilon)$.
    
    - Denote $V_0 = [t_0, t_0 + T_0] \times \overline{B(x_0, \delta)} \subseteq V$.
    
    - Picard iteration $K$ on $C^1([t_0, t_0 + T_0] \to \R^n)$ has properties:
        - Consider closed metric space $C = C^1([t_0, t_0 + T_0] \to \overline{B(x_0, \delta)})$.
        
        - $K|_C$ is a contraction map on complete metric subspace $C$.
            - Notice the following:
              $$
              \begin{aligned}
              |K(x)(t)-K(y)(t)| &\leq \int_{0}^{t}|f(s, x(s))-f(s, y(s))| \dd s\\
              &\leq L \int_{0}^{t}|x(s)-y(s)| \dd s\\
              &\leq L t \sup _{0 \leq s \leq t}|x(s)-y(s)|
              \end{aligned}
              $$
            
            - Therefore $\|K(x)-K(y)\| \leq L T_{0}\|x-y\|$ for all $x, y \in C$.
        
    - There is a **unique (local) solution** to the IVP in $[t_0, t_0 + T_0]$.
        - Any possible solution of the IVP must lie in $V_0$ during $[t_0, t_0 + T_0]$.
            - Bad solution must hit the upper / lower wall before $t_0 + T_0$.
            - Contradict by applying IVT between $(t_0, x_0)$ and $(t_0 + \Delta T, \pm \delta)$.
        - There is only a unique solution on $[t_0, t_0 + T_0]$ by fixed point theorem.
    
- Extend on the left and there is a unique local solution $x(t)$ on closed interval $I = [t_0 - \epsilon, t_0 + \epsilon]$.

- $f \in C^1(U \to \R^n)$ implies the time-uniform Lipschitz condition on $f$.

- When $f \in C^k(U \to \R^n)$, the local solution $x(t) \in C^{k + 1}(I \to \R^n)$.
    - When $k = 1$, $x(t) \in C^1(I \to \R^n)$ according to above Theorem.
    - Suppose the theorem is true for $k$, and $f \in C^{k + 1}(U \to \R^n)$.
    - Since $x'(t) = f(t, x(t))$, $x'(t) \in C^{k + 1}(I \to \R^n)$. So $x(t) \in C^{k + 2}(I \to \R^n)$.
    - Now apply induction.

(**Gronwall's inequality**)

Suppose $\psi(t)$ satisfies
$$
\psi(t) \leq \alpha(t)+\int_{0}^{t} \beta(s) \psi(s) \dd s, \quad t \in[0, T]
$$

with $\alpha(t): [0, T] \to \R$ and $\beta(t): [0, T] \to [0, \infty)$. We have
$$
\psi(t) \leq \alpha(t)+\int_{0}^{t} \alpha(s) \beta(s) \exp \left(\int_{s}^{t} \beta(r) d r\right) \dd s, \quad t\in [0, T]
$$

- Define $\phi(t) = \exp\left(-\int_0^t \beta(s) \dd s\right)$.
- $\frac{\dd}{\dd t} \phi(t) \int_{0}^{t} \beta(s) \psi(s) \dd s=\beta(t) \phi(t)\left(\psi(t)-\int_{0}^{t} \beta(s) \psi(s) \dd s\right) \leq \alpha(t) \beta(t) \phi(t)$.
- Integrate on both sides on $t$ gives: $\int_{0}^{t} \beta(s) \psi(s) \dd s \leq \int_{0}^{t} \alpha(s) \beta(s) \frac{\phi(s)}{\phi(t)} \dd s$.
- Now add $\alpha(t)$ on both sides.

Moreover, if in addition $\alpha(s) \leq \alpha(t)$ for $s \leq t$, then
$$
\psi(t) \leq \alpha(t) \exp \left(\int_{0}^{t} \beta(s) \dd s\right), \quad t \in[0, T]
$$
- Hint: enlarge the integrand, then compare by taking derivative.

(**Gronwall's inequality: linear case**)

Suppose $\psi(t): [0, T] \to \R$ satisfies:
$$
\psi(t) \leq \alpha+\int_{0}^{t}(\beta \psi(s)+\gamma) \dd s, \quad t \in[0, T]
$$
where $\alpha \in \R$, $\beta > 0$ and $\gamma \in \R$. Then
$$
\psi(t) \leq \alpha \exp (\beta t)+\frac{\gamma}{\beta}(\exp (\beta t)-1), \quad t \in[0, T]
$$

- Let $\theta(t) = \psi(t) + \gamma / \beta$. And $c = \alpha + \gamma / \beta$.
    - Then $\theta(t) \le c + \int_0^t \beta \theta(s) \dd s$.
    - $\frac{\partial }{\partial t}e^{-\beta  t} \int_0^t \beta \theta(t) \dd s = \beta  e^{\beta  (-t)} \theta (t)-\beta  e^{\beta  (-t)} \int_0^t \beta  \theta (s) \dd s \le \beta  e^{\beta  (-t)} c$. 
- $\int_0^t \beta \theta(t) \dd s \le ce^{\beta t}-c$. Therefore $\theta(t) \le c e^{\beta t}$.

(**IVP: continuity**)

Suppose $U \subseteq \R \times \R^n$ is open, and $f, g \in C(U \to \R^n)$. Consider IVP $x'(t) = f(t, x)$ with $x(t_0) = x_0$ and $y' = g(t, y)$ with $y(t_0) = y_0$.

Let $f$ be locally Lipschitz continuous in the second argument, uniformly with respect to the first.

- If $x(t)$ and $y(t)$ are respective solutions of the IVPs on some interval $[t_0, t_0 + T_0]$.
- W.L.O.G. assume $t_0 = 0$ in the following.
- For $V \subset U$ some set containing the graphs of $x(t)$ and $y(t)$.

$$
	L=\sup _{(t, x) \neq(t, y) \in V} \frac{|f(t, x)-f(t, y)|}{|x-y|}, \quad M=\sup _{(t, x) \in V}|f(t, x)-g(t, x)|,
$$

- We have following inequalities for $s, t \in [0, T_0]$:
    - $|x(t)-y(t)| \leq\left|x_{0}-y_{0}\right|+\int_{0}^{t}|f(s, x(s))-g(s, y(s))| d s$.
    - $|f(s, x(s))-g(s, y(s))|\leq|f(s, x(s))-f(s, y(s))|+|f(s, y(s))-g(s, y(s))|$
    - $|f(s, x(s))-g(s, y(s))|\leq L|x(s)-y(s)|+M$.
- Now following Gornwell's inequality in linear case:
$$
|x(t)-y(t)| \leq\left|x_{0}-y_{0}\right| e ^{Lt}+\frac{M}{L}\left( e ^{Lt}-1\right)
$$

- Therefore the solution $x(t)$ for $t \in [t_0, t_0 + T_0]$ is a continuous function of $x_0$ and $f$.

(**IVP: existence of general solution**)

Consider the following non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:

$$
x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n), \quad (*)
$$

where $U$ is open and $(t_0, x_0) \in U$.

Let $f$ be locally Lipschitz continuous in the second argument, uniformly with respect to the first.

- According to Picard-Lindelof there exists $\epsilon, \delta > 0$ where
    - $I_0 = [t_0 - 4 \epsilon, t_0 + 4 \epsilon]$ and $B_0 = \overline{B(x_0, 4\delta)}$ s.t. $V_0 = I_0 \times B_0 \subset U$.
    - The picard iteration at $(t_0, x_0)$ is a contraction map on $C^1(I_0 \to B_0)$.
- It is easy to verity that for the same $\epsilon, \delta$ we have:
    - Let $I = [t_0 - \epsilon, t_0 + \epsilon]$ and $B = \overline{B(x_0, \delta)}$, $V = I \times B$.
    - For any $(t_1, x_1) \in V$, denote $I_1 = [t_1 - 2\epsilon, t_1 + 2\epsilon]$ and $B_1 = \overline{B(x_1, 2\delta)}$.
    - The Picard iteration at $(t_1, x_1)$ is a contraction map on $C^1(I_1 \to B_1)$.
    - Therefore there is a unique solution on $I_1$ with codomain $B_1$.
- Notice that $I_1$ completely covers interval $I$.
    - Therefore there is a unique solution $\phi(t, s, x)$ on $I$ with codomain $B_1$ for any $(s, x) \in I \times B$.
    - Define general solution $\phi(t, s, x): I \times I \times B \to B_1$. Where $[\phi]_{s,x}$ is the unique solution.
        - We now know $\phi$ is continuous in $s, x$.
        - $\phi$ is continuously differentiable in $t$ by definition.

We can show that $\phi(t, s, x)$ is Lipschitz continuous.
- Let $V = I \times B_1 \subset U$. And
$$
L=\sup _{(t, x) \neq(t, y) \in V} \frac{|f(t, x)-f(t, y)|}{|x-y|}, \quad M=\sup _{(t, x) \in V}|f(t, x)|,
$$

- $\left|\phi\left(t, t_{0}, x_{0}\right)-\phi\left(t, t_{0}, y_{0}\right)\right| \le \left|x_{0}-y_{0}\right| e ^{L\left|t-t_{0}\right|}$.
- $\left|\phi\left(t, t_{0}, y_{0}\right)-\phi\left(t, s_{0}, y_{0}\right)\right| = \left|\int_{t_{0}}^{t} f\left(r, \phi\left(r, t_{0}, y_{0}\right)\right) \dd r-\int_{s_{0}}^{t} f\left(r, \phi\left(r, s_{0}, y_{0}\right)\right) \dd r\right|$.
    - Rearrange the terms on the R.H.S. to get:
    - $\left|\int_{t_{0}}^{s_{0}} f\left(r, \phi\left(r, t_{0}, y_{0}\right)\right) \dd r\right|+\int_{s_{0}}^{t}\left|f\left(r, \phi\left(r, t_{0}, y_{0}\right)\right)-f\left(r, \phi\left(r, s_{0}, y_{0}\right)\right)\right| \dd r$.
    - Let $\Delta (t) = \abs{\phi(t, t_0, y_0) - \phi(t, s_0, y_0)}$.
    - $\Delta(t) \leq\left|t_{0}-s_{0}\right| M+L \int_{s_{0}}^{t} \Delta(r) \dd r$.
    - Now apply Gronwall's inequality. $\Delta(t) \le \abs{t_0 - s_0}M e^{L\abs{t - s_0}}$.
- $\left|\phi\left(t, s_{0}, y_{0}\right)-\phi\left(s, s_{0}, y_{0}\right)\right| = \abs{\int_{s}^{t} f\left(r, \phi\left(r, s_{0}, y_{0}\right)\right) \dd r} \le M\abs{t - s}$.
- Therefore $\abs{\phi\left(t, t_{0}, x_{0}\right)-\phi\left(s, s_{0}, y_{0}\right)} \leq\abs{x_{0}-y_{0}} e ^{L\abs{t-t_{0}}}+M\left(\abs{t-s}+\abs{t_{0}-s_{0}} e ^{L\abs{t-s_{0}}}\right)$.

(**IVP: forms of equations**)

A non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$ takes the form
$$
x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n)
$$

where $U$ is open and $(t_0, x_0) \in U$.
- A general solution takes the form $\phi(t, t_0, x_0): I \times I \times B \to \R^n$ where $I \times I \times B \subset U$.

An autonomous IVP for $x \in C^1(U \subseteq \R \to \R^{n})$ takes the form
$$
x'(t) = f(x(t)), \quad x(0) = x_0, \quad f \in C^1(U \subseteq \R^n \to \R^n)
$$

where $U$ is open and $x_0 \in U$. W.L.O.G. we usually assume $t_0 = 0$.
- A general solution takes the form $\varphi(t, x_0): I \times B \to \R^n$ where $I \times B \subset U$.
    - Due to time-shift invariance, $\varphi$ do not take $t_0$ as input.

A parameterized non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:
$$
x'(t) = f(t, x(t), \lambda), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \times \R^{m} \to \R^n)
$$

where $U$ is open and $(t_0, x_0, \lambda_0) \in U$.
- A general solution takes the form $\Phi(t, t_0, x_0, \lambda_0): I \times I \times B \times \Lambda \to \R^n$ where $I \times I \times B \times \Lambda \subset U$.

(**IVP: Autonomous Transform**)

A non-autonomous IVP can be translated into autonomous IVP with out loss of generality.

Consider the following non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:
$$
x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n), \quad (*)
$$
where $U$ is open and $(t_0, x_0) \in U$.
- Define $W = U - t_0$ as $U$ shifted along time axis.
- Denote $y(s) = [y_0(s), z(s)]$ where $z \in C^1(Q \subseteq \R \to \R^n)$.
- Define $g(s, z) = [1; f(s + t_0, z)]$ where $(s, z) \in W$.

Now consider the following autonomous IVP for $y \in C^1(Q \subseteq \R \to \R^{n + 1})$:
$$
y'(s) = g(y(s)), \quad y(0) = (t_0, x_0), \quad g \in C(W \subseteq \R^{n + 1} \to \R^{n + 1}), \quad(**)
$$
We can translate particular solutions between two systems:
- For $x(t)$ solving $(*)$ on interval $I$.
    - $x'(t) = f(t, x(t))$.
    - Define $y(s) = [s + t_0, x(s + t_0)]$ for $s \in I - t_0$.
    - $y'(s) = [1, x'(s + t_0)] = g(y(s))$.
    - So $y(s)$ is a solution of autonomous IVP on $I - t_0$.
    - then $y(s) = [s + t_0, x(s + t_0)]$ is solving the autonomous IVP on $I - t_0$.
- For $y(s)$ solving $(**)$ on interval $Q$.
    - $y'(s) = g(y(s)) = [1;f(s + t_0, z(s))]$ for $s \in Q$.
    - Define $x(t) = z(t - t_0)$ for $t \in Q +t_0$.
    - $x'(t) = z'(t - t_0) = f(t, x(t))$.
    - So $x(t)$ is a solution of non-autonomous IVP on $Q + t_0$.

We can translate general solutions between two systems:
- Consider the general solution $\phi(t, t_0, x_0): I \times I \times B \to \R^{n}$ for $(*)$.
    - $\varphi(s,(t_0, x_0)) := [s + t_0, \phi(s + t_0, t_0, x_0)]$. $\varphi: (I - t_0) \times (I \times B) \to \R^{n + 1}$.
- Consider the general solution $\varphi: (I - t_0) \times (I \times B) \to \R^{n + 1}$. for $(**)$.
    - Split $[t, \phi(t, t_0, x_0)] := \varphi(t - t_0, (t_0, x_0))$. $\phi: I \times I \times B \to \R^{n}$.

Continuity conditions on $f$ can be translated to conditions on $g$.
- $f(t, x): U \to \R^n$ is Lipschitz in $x$ uniformly in $t$ implies $g(y): W \to \R^{n + 1}$ is Lipschitz continuous.
- $f(t, x) \in C^k(U \to \R^n)$ implies $g(y) \in C^k(W \to \R^{n + 1})$.

(**IVP: Parameter Transform**)

A parameterized non-autonomous IVP can be translated into a non-autonomous IVP with out loss of generality.

Consider the following parameterized IVP for $x \in C^1(J \subseteq \R \to \R^n)$:
$$
x'(t) = f(t, x(t), \lambda), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \times \R^{m} \to \R^n), \quad(*)
$$
where $U$ is open and $(t_0, x_0, \lambda_0) \in U$.
- We can create a new IVP by viewing parameters as constant dimensions in solution.
- Denote $y(t) = [x(t); \lambda]$. Then $y'(t) = [x'(t); 0]$.
- Denote $g(t, y=[x;\lambda]) := f(t, x, \lambda)$ where $(t, y) \in \R \times \R^{n + m}$.

Now consider the following non-Aut. IVP for $y \in C^{1}(J \subseteq \R \to \R^{n + m})$.
$$
y'(t) = g(t, y(t)), \quad y(t_0) = (x_0, \lambda_0), \quad g \in C(U \subseteq \R \times \R^n \times \R^m \to \R^n), \quad(**)
$$
where $U$ is open and $(t_0, x_0, \lambda_0) \in U$.

We can translate particular solutions between two systems.
- For $x(t)$ solving $(*)$ on interval $I$ with parameter $\lambda_0$.
    - Define $y(t) = [x(t); \lambda_0]$.
- For $y(t)$ solving $(**)$ on interval $I$.
    - Split $[x(t), \lambda_0] := y(t)$.
    - The $\lambda_0$ part must be constants in proper range.

We can translate general solutions between two systems.
- Consider general solution $\Phi(t, t_0, x_0, \lambda_0): I \times I \times B \times \Lambda \to \R^n$ of $(*)$.
    - Define $\phi(t, t_0, (x_0, \lambda_0)):=[\Phi(\cdots), \lambda_0]$.
- The converse works similarly.

Continuity conditions on $f$ can be translated to conditions on $g$.
- This part works similarly with **Parameter Transform**.
