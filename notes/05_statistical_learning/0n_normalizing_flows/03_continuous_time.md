#### Continuous-time Normalizing Flow

> Chen, T.Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D.K. (2018). Neural Ordinary Differential Equations. *Neural Information Processing Systems*.

##### Neural ODE

Consider the following parameterized IVP for $x \in C^1([0, 1] \to \R^n)$:
$$
\boxed{x'(t) = f(t, x(t), \lambda), \quad \lambda = \lambda_0,\quad x(0) = x_0, \quad f \in C^1([0, 1] \times \R^{n} \times \R^{m} \to \R^n)}
\label{equ:neural_ode}
$$
When $f$ is specified by a neural network, $\lambda$ are network parameters. The system is called a **Neural ODE**.

Let $\Phi(t, (s, x, \lambda))$ be the unique general solution $x(t)$ at $t$ for the IVP starting from $(s, x, \lambda)$.

##### Jacobi's formula

Suppose $A(t) \in D(\R \to \R^{n \times n})$. First notice that
$$
\frac{\part \det A}{\part A_{ij}} = \frac{\part (A \adj A)_{ii}}{\part A_{ij}} = \frac{\part (A_{ik} C_{ik})}{\part A_{ij}} = C_{ij} = (\adj A)_{ji} = (\adj A)^T
$$
Then we have
$$
\frac{\part \det A(t)}{\part t} = \frac{\part \det A(t)}{\part A(t)_{ij}} \frac{\part A(t)_{ij}}{\part t} = (\adj A(t))_{ji} \frac{\part A(t)_{ij}}{\part t} = \tr \p{\adj A(t) \frac{\part A(t)}{\part t}}
$$

##### Abel's identity

Consider following IVP for $x(t) \in C^1(I \subseteq \R \to \R^{n})$:
$$
\boxed{x'(t) = A(t) x(t),\quad x(0) = x_0, \quad A(t) \in C([0, T] \to \R^{n \times n})}
$$

Suppose $U(t)$ is a fundamental matrix solution, such that $x(t) = U(t) x_0$. Let $W(t) := \det U(t)$.

- By definition, we have $U'(t) = A(t) U(t)$. So $\det U'(t) = \det A(t) W(t)$.

- By Jacobi's formula
  $$
  \begin{aligned}
  W'(t) & = (\det U(t))' = \tr\p{(\adj U(t)) U'(t)} = \tr \p{\adj U(t) A(t) U(t)} \\
  & = \tr \p{A(t) U(t) \adj U(t)} = \tr\p{A(t)} W(t)
  \end{aligned}
  $$

- Therefore $W(t)$ is the unique solution of the linear ODE:
  $$
  W'(t) = \tr\p{A(t)} W(t), \quad \tr A(t) \in C([0, T] \to \R)
  $$
  
- Therefore we have
  $$
  W(t) = W(0) \exp \int_{0}^t \tr(A(s)) \dd s
  $$

- Now suppose $\Pi(t, t_0)$ is the principal matrix solution, and $U(t) = \Pi(t, t_0)$, we have $W(0) = 1$.

##### Instantaneous change of variable: from Abel's identity

Consider the neural ODE in equation $\ref{equ:neural_ode}$. Let $x(t) \in C^1([0, 1] \to \R^n)$ be a particular solution with $x(0) = x_0$ and parameter $\lambda$.

Let $A(t) = D_2f(t, x(t), \lambda)$. And consider the following IVP system about the perturbation for $\Delta(t) \in C^1([0, 1] \to \R^n)$.
$$
\Delta'(t) = A(t)\Delta(t), \quad \Delta(0) = \Delta_0
\label{equation:ode_path_linearize}
$$
The first variational equation of this system is the same as equation $\ref{equ:neural_ode}$, given by:
$$
\psi'(t) = A(t) \psi(t) = D_2 f(t, x(t), \lambda) \psi(t)
$$
Therefore $\part \Delta(t) / \part \Delta_0$ equals to $\part x(t) / \part x_0$. It should be obvious that by Abel's identity:
$$
\log \abs{\det {\frac{\part x(t)}{\part x_0}}} = \int_0^t \tr D_2 f(s, x(s), \lambda) \dd s
$$

##### Instantaneous change of variable: from the FPK equation

> Proof given by Chen T.Q.

Following above discussion, the equation is also related to the FPK equation.
$$
D_2p(x, t) = - D_{x_i} \p{f_{i}(t, x, \lambda) p(x, t)}
$$
Suppose $x(t)$ is a solution of the Neural ODE. Denote $D_ip(x, t):= \part p(x, t) /\part x_i$ and $D_i f(t, x, \lambda) := \part f(t, x, \lambda) / \part x_i$. Then
$$
\begin{aligned}
\frac{\part p(x(t), t)}{\part t} & = D_i p(x(t), t) x_i'(t) + D_2 p(x(t), t)\\
& = D_i p(x(t), t) x_i'(t) - D_{i} \p{f_{i}(t, x(t), \lambda) p(x(t), t)}\\
& = D_i p(x(t), t) x_i'(t) - D_i f_i(t, x(t), \lambda) p(x(t), t) - f_i(t, x(t), \lambda) D_i p(x(t), t)\\
& = -D_i f_i(t, x(t), \lambda) p(x(t), t) = -p(x(t), t)\tr D_2 f(t, x(t), \lambda)
\end{aligned}
$$

Now notice that
$$
\frac{\part \log p(x(t), t)}{\part t} = \frac{1}{p(x(t), t)} \frac{\part p(x(t), t)}{\part t} = - \tr D_2 f(t, x(t), \lambda)
$$
By expanding the Neural ODE, we can solve its log probability in a single pass:
$$
\frac{\dd}{\dd t}\left[\begin{array}{c} x (t) \\ \log p( x (t), t)\end{array}\right]=\left[\begin{array}{c}f(t, x (t), \lambda) \\ -\tr D_2 f(t, x(t), \lambda)\end{array}\right]
$$

Here directly finding $\tr D_2 f(t, x, \lambda)$ is computationally intractable. One solution is to use stochastic trace estimators, which only requires availability of vector-Jacobian product $v D_2 f(t, x, \lambda)$ where $v \in \R^n$.

> More on stochastic trace estimation can be found [here](https://www.ethanepperly.com/index.php/2023/01/26/stochastic-trace-estimation/).
>
> Hutchinson, M.F. (1989). A stochastic estimator of the trace of the influence matrix for laplacian smoothing splines. *Communications in Statistics - Simulation and Computation, 18*, 1059-1076.
>
> Meyer, R.A., Musco, C., Musco, C., & Woodruff, D.P. (2020). Hutch++: Optimal Stochastic Trace Estimation. *Proceedings of the SIAM Symposium on Simplicity in Algorithms, 2021*, 142-155 .

Suppose we want to compute $\tr A$, which is not directly accessible. Suppose $X \sim p(x)$ in $\R^n$ where $E[X] = 0$, and $E[XX^T] = \bI_n$. We have the Hutchinson trace estimator described as following:

- $E[X^T A X] = E[\tr(X^T A X)] = E[\tr(A X X^T)] = \tr(A E[XX^T]) = \tr (A)$.

- Now suppose we have $m$ i.i.d. random variables $(X_1, \ldots, X_m)$.
  $$
  \what \tr := \frac{1}{m} \sum_{i = 1}^m X_{i} ^T A X_i, \quad E[\what \tr] = \tr A, \quad \var(\what \tr) = \frac{\var(X^T A X)}{m}
  $$

- There are better unbiased estimators with faster convergence than the naïve estimator.



