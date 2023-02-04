#### Probability Space

(**Probability measure**)

Suppose $\F$ is a $\sigma$-algebra on $\Omega$.

- A **probability measure** on $(\Omega, \F)$ is a measure $P$ on $(\Omega, \F)$ such that $P(\Omega)=1 .$
- $\Omega$ is called the **sample space**. Elements $\omega \in \Omega$ is an outcome of the experiment or an **sample**.
- An **event** is an element of $\F$.
- If $A$ is an event, then $P(A)$ is called the **probability** of $A$.
- If $P$ is a **probability measure** on $(\Omega, \F )$, then the triple $(\Omega, \F , P)$ is called a **probability space**.
- A event $A$ is to happen almost surely if $P(A) = 1$.

(**Random variables**)

Suppose $(\Omega, \F)$ and $(S, \mathcal S)$ are **measurable spaces**.

A function $X: \Omega \rightarrow S$ is called $S$-valued random variable if it is **measurable function** from $(\Omega, \mathcal A )$ to $(S, \mathcal S )$.

- $\{X \in U\}$ where $U \subseteq S$ means $\{\omega \in \Omega: X(\omega) \in U\}$, or $X^{-1}[U] \subseteq \Omega$.
    - Suppose $U\in \mathcal S$, $\{X \in U\} \in \F$ is an event.
- The notation $\{X = x\}$ where $x \in \mathcal S$ means $X^{-1}\{x\} \in \F$.
- The notation $P(X \in U)$ means $P\{X \in U\}$, and $P(X = x)$ means $P\{X = x\}$.

A **(real-valued) random variable** $X$ requires that $S = \R$ and $\mathcal S = \B[\R]$.
- The notation $\{X \le x\}$ where $x \in \R$ means $\{\omega \in \Omega: X(\omega) \le x\}$.

(**Distributions**)

Suppose $(\Omega, \F , P)$ is a probability space and $X \in \L(\Omega \to \Omega', \F/\F')$ is a random variable.

- Probability measure $P_X := P \circ X^{-1}$ is the **distribution** of $X$ on $\Omega'$.
- We write $X \sim \mu$ if $X$ has distribution $\mu$.
- Random variables with the same distribution are called **identically distributed** (i.d.).

Suppose $(X_i)_{i \in I} \in \L(\Omega \to \Omega_i, \F / \F_i)$. Then $(\times_i \Omega_i, \otimes_i \F_i, \times_iP_{X_i})$ is a measure space. And $\times_i P_{X_i}$ is the **joint distribution** of $(X_i)_{i \in I}$.

(**Distribution functions**)

Distribution $P$ on $\B(\R^n)$ have the **distribution function** $F_P: \R^n \to [0, 1]$ defined by $F_P(x) := P(-\infty, x]$.

- $F_P$ is distributional.
- $\lim_{x_k \to -\infty} F_P(x) = 0$ and $\lim_{x_k \to \infty} F_P(x) = 1$ for all $k = 1, \ldots, n$.

Conversely define Lebesgue-Stieltjes measure on $\R^n$ by $F_P$ gives measure $P$ on $\B(R^n)$.

Distribution $P$ on $\R^n$ has a **density function** $f: \R^n \to [0, \infty]$ if $dP = f dx$.

- $f$ is normalized, $\int_{\R^n} f(x) dx = 1$.
- $F(x) = \int_{(-\infty, x]} f(x) dx$.

Random variables also have **distribution / density functions**.
- Suppose $X$ is a real (vector) valued random variable. The **distribution / density function** of $X$ is the distribution / density function of $P_X$, denoted by $F_X$ and $f_X$.
- Suppose $\mathcal X = (X_i)_{i = 1}^n \in \L(\Omega \to \R, \F)$. The **joint distribution / density function** of them is the distribution / density function of $\times_i P_{X_i}$, denoted by $F_\mathcal X$ and $f_{\mathcal X}$.

(**Expectation**)

Suppose $(\Omega, \F , P)$ is a **probability space**. 

And $X, Y, \bX=(X_1, \ldots, X_n) \in \L(\Omega \to \R)$. Define the following when the integrals exists.

- Define **expectation** $E[X]:= P(X)$ and $E[\bX] = (EX_1, \ldots, EX_n)$.
- Define kth **moment** $m_k(X):= E[X^k]$.
- Define kth **absolute moment** $M_k(X):= E|X|^k$.
- Define **variance** $\var[X]:= E[(X - EX)^2] = E[X^2] - E^2[X]$.

Suppose $X \in \L(\Omega \to \R^n)$. $E[X] = P(X) = \int_{\R^n} x d P_X = \int_{\R^n} x d F_X(x) = \int_{\R^n} x f_X(x) dx$.

(**Jensen's Inequality**)

Suppose $(\Omega, \F, P)$ is a **probability space**.

Suppose $X \in \L^1(\Omega \to \R^m, P)$ (in each dimension).

Suppose $\varphi \in \bar \L(\R^m \to \bar \R)$ is convex and lower semi-integrable. Then $E[\varphi(X)] \ge \varphi(E[X])$.

- Since $\varphi$ is convex and lower semi-integrable., $\exists a \in \R^{n}: a^T(X - EX) \le \varphi(X) - \varphi(EX)$.
- Now integrate on both sides gives $0 \le E[\varphi(X)] - \varphi(EX)$.

Important special case in 1D include:
- $\varphi(x) = \abs {x}^p$ where $p \ge 1$. This gives $E^p |X| \le E|X|^p$.

(**Covariance**)

Suppose $(\Omega, \F , P)$ is a **probability space**.

And $X, Y, \bX=(X_1, \ldots, X_n) \in \L(\Omega \to \R)$. Define the following when the integrals exists.

- Define **covariance** $\operatorname{Cov}(X, Y) = E[(X - EX)(Y - EY)]$.
- Define **covariance matrix** $C = \cov (\bX) = E[(\bX - E\bX)(\bX - E\bX)^T]_{ij} = \operatorname{Cov}(X_i, X_j)$.
    - The covariance matrix is **positive** (self-adjoint and positive semi-definite). Since $$
    \forall x \in \R^n :\pd{C x}{x}= E[(X_i - E X_i)x_ix_j(X_j - EX_j)] = E\left[\sum_i (X_i - EX_i)x_i\right]^2 \ge 0$$
    Consider the covariance function restricted to square integrable random variables $\cov: \L^2(\Omega \to \R,P)^2 \to \R$.
- Let $X, (X_n)_{n = 1}^\infty, Y, Z \in \L^2(\Omega \to \R, P)$ and $c \in \R$, then:
    - $\cov(X + Y, Z) = \cov(X, Z) + \cov(Y, Z)$.
    - $\cov (X, Y) = \cov(Y, X)$.
    - $\cov(X + c, Y) = \cov(X, Y)$, $\cov(cX, Y) = c\cov(X, Y)$.
    - $\cov(X, X) = \var(X)$. $\var(cX) = c^2 \var X$.
    - $\var(X_1 + \cdots + X_n) = \sum_{i = 1}^n \var X_i + \sum_{i \neq j} \cov(X_i, X_j)$.
    - (**Cauchy-Schwarz**) $\cov(X, Y)^2 \le \var(X) \var (Y)$. When $\var(Y) > 0$.
        - Let $\theta = -\cov(X, Y) / \var(Y)$.
        - $0 \le \var(X + \theta Y)\var(Y) = (\var(X) + 2 \theta \cov(X, Y) + \theta^2 \var(Y))\var(Y)$.
        - So $\var(X)\var(Y) - \cov(X, Y)^2 \ge 0$.
        - With equality iff $X + \theta Y$ is a.e. constant.

#### Random Processes

(**Stochastic / random processes**)

Suppose $(\Omega, \F, P)$ is a probability space. Suppose $T$ is the index set. A family of indexed random variables $\mathbf X(\omega) = (X_t(\omega))_{t\in T}$ is a random process.
- $\cup_{t \in T} \range(X_t)$ is called the state space.
- $\mathbf X(\omega)$ for some $\omega \in \Omega$ is called a **sample function** or a **realization**.
- We can classify stochastic processes according to the state space and index set:
    - Cardinality of the index set: continuous-time and discrete-time processes.
    - Cardinality of the state space:
        - Real-valued processes, or processes with continuous state spaces.
        - Integer-valued processes, or processes with discrete state spaces.

Some times $X(t) = X_t$ notation is used when there is not confusion.

(**Independent increment processes**)

Let $\left(X_{t}\right)_{t \in T}$ be a stochastic process, and $T$ is linearly ordered.

Then the stochastic process has **independent increments** if and only if for every $m \in \mathbb{N}$ and any choice $t_{0}, t_{1}, t_{2}, \ldots, t_{m-1}, t_{m} \in T$ with $t_{0}<t_{1}<t_{2}<\cdots<t_{m}$, the random variables $\left(X_{t_{1}}-X_{t_{0}}\right),\left(X_{t_{2}}-X_{t_{1}}\right), \ldots,\left(X_{t_{m}}-X_{t_{m-1}}\right)$ are independent.

(**Stationary increment processes**)

Let $\left(X_{t}\right)_{t \in T}$ be a stochastic process, and $T$ is linearly ordered.

Then the stochastic process has **stationary increments** if and only if the distribution of $X_{t+s} - X_t$ is $t$ invariant.

(**Stationary process**)

Let $\left(X_{t}\right)_{t \in T}$ be a stochastic process, for $T = \Z$ or $\R$.

$X_t$ is strictly / strongly stationary if for all $n \in \N$, for all $t_1, \ldots, t_n \in T$, and for all $\tau \in T$ we have:
$$
F_{X_{t_1}, \ldots, X_{t_n}}(x_{1},\cdots, x_{n}) = F_{X_{t_1 + \tau}, \ldots, X_{t_n + \tau}} (x_1, \cdots, x_n)
$$
- If the above is true for $n \le N$, $X$ is called N-th-order stationary.
- $X_t$ is weak / wide-sense stationary (WSS) if it is second order stationary.
