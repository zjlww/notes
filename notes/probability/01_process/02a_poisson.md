#### Gamma Family

> Many distributions are special cases of Gamma distribution. Recall that
> $$
> \Gamma(k) = \int_0^\infty x^{k - 1} e^{-x} \dd x = \lambda^k \int_0^\infty x^{k - 1} e^{-\lambda x} \dd x;\quad \lambda > 0, k > 0
> $$

##### Gamma distribution

Suppose $X$ is a real random variable with the following density function
$$
f_X(x) = \frac{\lambda^k}{\Gamma(k)} x^{k - 1} e^{-\lambda x}; \quad x > 0
$$
$X$ has the Gamma distribution.

- Denoted as $X \sim \Gamma(k, \lambda)$.
- $f_X^*(s) = \lambda^k / (\lambda + s)^k$.
  - Hint: first take $s \in \R$, and then do analytic continuation.
- $E[X] = k / \lambda$, $E[X^2] = k(k+1)/\lambda^2$, $\var(X) = k / \lambda^2$.

##### Exponential distribution

Suppose $X \sim \Gamma(1, \lambda)$, $X$ has exponential distribution.

- Denoted as $X \sim \operatorname{Exp}(\lambda)$.
- $f_X(x) = \lambda e^{-\lambda x}$, for $x \ge 0$.
- $F(x) = P(X \le x) = 1 - e^{-\lambda x}$ for $x > 0$.
- $f_X^*(s) = \lambda / (\lambda + s)$.
- $E[X] = 1/\lambda$, $E[X^2] = 2 / \lambda^2$, $\var(X) = 1 / \lambda^2$.

##### Memoryless variable

A positive random variable $X$ is called **memoryless** if
$$
\forall x \ge 0, t \ge 0: P(X > t + x) = P(X > x) P(X > t)
$$
$X$ is memoryless if and only if $X \sim \operatorname{Exp}(\lambda)$, $\lambda \in (0, \infty)$.

- $\from$ Suppose $X \sim \operatorname{Exp}(\lambda)$.
  - $P(X > t + x) = e^{-\lambda t} e^{-x t} = P(X > x) P(X> t)$.
- $\to$ Suppose $X$ is memoryless. ==TODO==
  - $\ln P(X > t + x) = \ln P(X > t) + \ln P(X > x)$.
  - See this [page](https://math.stackexchange.com/questions/1801830/on-the-proof-that-every-positive-continuous-random-variable-with-the-memoryless).

We generalize distribution $\Exp(\lambda)$ to $\lambda \in \c{0, \infty}$.

- When $\lambda = 0$, $\Exp(0)$ means $P(X = \infty) = 1$.
- When $\lambda = \infty$, $X \sim \Exp(\infty)$ means $P(X = 0) = 1$.

##### Erlang-K distribution

Consider integer $k$ and $X \sim \Gamma(k, \lambda)$. Then $X$ has the Erlang-$k$ distribution with parameter $\lambda$.

- Denoted by $X \sim \operatorname{Erlang}(k, \lambda)$.
- $f_X^*(s) = (\lambda)^k / (\lambda + s)^k$.
- $E[X] = 1 / \lambda$, $E[X^2] = (k + 1) / (k\lambda^2)$, $\var (X) = 1 / (k \lambda^2)$.

Suppose $\p{Y_i}_{i = 1}^k \sim_{\iid} \Exp(\lambda)$. Then $Y = Y_1 + \ldots + Y_k \sim \Gamma(k, \lambda)$.

#### Definition of Poisson Process

##### Arrival process

On a underlying probability space $(\Omega, \F, P)$.

An **arrival process** on $[0, \infty) $ can be characterized in the following **equivalent** ways.

- **Arrival times**, $(S_n)_{n = 1}^\infty \in \L(\Omega \to [0, \infty), \F)$.
  - We have following requirements:
    - Sequence $\p{S_n}$ is increasing almost surely.
    - $S_n \to \infty$ as $n \to \infty$ almost surely.
  - $S_n$ is interpreted as the arrival time of $n$th event.
  - We define $S_0 = 0$ for convenience.
  
- **Arrival intervals** $(X_n)_{n = 1}^\infty \in \L(\Omega \to [0, \infty), \F)$.

  - We have following requirements:
    - All $X_n$ with $P(X_n > 0) > 0$.
    - $\sum X_n \to \infty$ almost surely.
  - $X_n$ is interpreted as the interval of the $(n-1)$th and the $n$th event.
  - Given $(S_n)$, define $X_n := S_n - S_{n - 1}$.
  - Given $(X_n)$, define $S_n := \sum_{i = 1}^n X_i$.
    - $S_n \to \infty$ is guaranteed by Cantelli's Lemma II.
  
- **Arrival count** $(N(t))_{t \in [0, \infty)} \in \L(\Omega \to [0, \infty), \F)$.

  - We have following requirements:
    - Path $N(t)$ is right-continuous and increasing almost surely.
    - $N(t) \to \infty$ as $t \to \infty$ almost surely.
  - $N(t)$ is interpreted as the number of arrivals in $[0, t]$.
  - Given $\p{S_n}$, define $N(t) := \sum_{k = 1}^\infty 1(S_k \le t)$.
  - Given $N(t)$, define $S_n := \inf \c{N(t) \ge n: t \ge 0}$.
  - Two important translation:
    - $\{S_n \le t\} = \{N(t) \ge n\}$, and $\c{S_n > t} = \c{N(t) < n}$.
    - $\c{N(t) = n} = \c{S_n \le t < S_{n + 1}}$.
  
- The arrival process is generalized to measurable sets in $\B[0, \infty)$:
  $$
  N(A) := \# \c{n \ge 1: S_n \in A} = \sum_{n = 1}^\infty 1(S_n \in A)
  $$

An arrival process has **stationary increment** if for all $s > t > 0$, $N(s - t)$ and $N(s) - N(t)$ have the same distribution.

An arrival process with i.i.d. arrival intervals is a **renewal process**.

##### Poisson process I: interval definition

A **Poisson process** is an **renewal process** where arrival intervals $\p{X_n} \sim_{\iid} \operatorname{Exp}(\lambda)$.

- $\lambda$ is called the **rate** of the process.
- The arrival time of $n$th event $S_n \sim \Gamma(n, \lambda)$.

##### Poisson process: restart

For Poisson process $N(t)$ with rate $\lambda$. 

When $N(t) = n$, define $Z_1 := X_{n + 1} - t$, and $Z_k = X_{n + k}$ for $k \ge 2$.

Then $\p{Z_k} \sim _{\iid} \Exp(\lambda)$. This is called a **restart** of Poisson process at $t$.

- We can show that $P(Z_1 > z \mid N(t) = n, S_n = \tau) = e^{-\lambda z}$ for $\tau < t$.

  - Define it as the Radon-Nikodym derivative of measure $P(Z_t > z, S_n \in I \mid N(t) = n)$ with respect to $P(S_n \in I \mid N(t) = n)$.

  - Therefore for $\tau < t$, we have
    $$
    \begin{aligned}
    P(Z_1 > z \mid N(t) = n, S_n = \tau) & = P(X_{n + 1} > z + t - \tau \mid X_{n + 1} > t - \tau, S_n \approx \tau)\\
    & = P(X_{n + 1} > z + t - \tau \mid X_{n + 1} > t - \tau) = e^{-\lambda z}
    \end{aligned}
    $$

    - The derivation is based on taking limit $S_n \in [\tau - \epsilon, \tau + \epsilon]$ where $\epsilon \to 0$.
  
- Therefore $Z_1 \sim \Exp(\lambda)$, and $\p{Z_k}$ are independent.
  - Prove by definition, sum over values of $N(t)$.

Therefore the Poisson process has **stationary increments**. Since $N(s) - N(t)$ has the same distribution as $N(s - t)$.

For all $k \ge 1$, $Z_k \perp \F_t$. Where $\F_t$ is the natural filtration of $N(t)$.

- With a similar argument as above, we have:
  $$
  P(Z_k > z \mid N(t) = n, X_1 = x_1, \ldots, X_n = x_n) = e^{-\lambda z},\quad k \ge 1
  $$

- Therefore $Z_k \perp \F_t \mid \c{N(t) = n}$. And $Z_k \perp \F_t$.

  - Notice that the boxes in $\F_t$ translates to regions in $x_1, \ldots, x_n$.

$\sigma(Z_k) \perp \F_t$. ==Needs better proof==

- With a similar argument as above, replacing $Z_k > z$ with multiple $Z_m > z_m$.
- Just verify independence on boxes in $\sigma(Z_k)$ and boxes in $\F_t$.

Therefore the Poisson process has **independent increments**.

##### Poisson distribution

$X: \Omega \to \N$ has Poisson distribution if
$$
P(X = k) = \frac{\lambda^k}{k!} e^{-\lambda}
$$

- Denoted as $X \sim \operatorname{Poisson}(\lambda)$.

- $E[z^X] = e^{z \lambda - \lambda}$.

- $E[X] = \lambda$, $E[X^2] = \lambda^2 + \lambda$, $\var(X) = \lambda$.

- (**Splitting**) Suppose $N \sim \operatorname{Poisson}(\lambda)$ and $X \sim \operatorname{Binomial}(N, p)$. Then $X \sim \operatorname{Poisson}(\lambda p)$.
  $$
  P(X = k) = \sum_{n = k}^\infty P(X = k | N = n) P(N = n) =\sum_{n = k}^\infty \frac{\lambda^n}{n!} e^{-\lambda} C_{n}^k p^k q^{n-k} = \frac{(\lambda p)^k}{k!} e^{-\lambda p}
  $$

- (**Merging**) Suppose $X_1 \sim \operatorname{Poisson}(\lambda_1)$ and  $X_ 2\sim \operatorname{Poisson}(\lambda_2)$. And $X_1 \perp X_2$. Define $X = X_1 + X_2$. Then $X \sim \operatorname{Poisson}(\lambda_1 + \lambda_2)$.

  - $E[z^X] = E[z^{X_1 + X_2}] = E[z^{X_1}] E[z^{X_2}] = e^{(\lambda_1 +\lambda_2) z - (\lambda_1 + \lambda_2)}$.

##### Poisson process II: distribution definition

An **arrival process** $N(t)$ with following properties is a Poisson process.

- $N(0) = 0$ almost surely.

- $N(t)$ has **stationary and independent** increments.

- $N(t) \sim \operatorname{Poisson}(\lambda t)$.
  $$
  p_n(t) := P(N(t) = n) = \frac{e^{-\lambda t} (\lambda t)^n}{n!}\quad (n \ge 0, t \ge 0)
  $$

Notice that $\lambda = E[N(t)] / t$, so it is called the **rate** of the process.

##### Poisson process I > II

Suppose $N(t)$ follows definition I, with rate $\lambda$.

We have proved that $N(t)$ has stationary and independent increments.

We only need to show that $N(t) \sim \operatorname{Poisson}(\lambda t)$.

- Recall that $\c{N(t) < n} = \c{S_n > t}$.

- And $S_n = X_1 + \cdots + X_n$, so $S_n \sim \Gamma(n, \lambda)$.
  $$
  f_{S_n}(t) = \frac{\lambda^n}{\Gamma(n)}t^{n - 1} e^{-\lambda t},\quad n \ge 0, t \ge 0
  $$

- Therefore
  $$
  P(N(t) < n) = P(S_n > t) = \int_t^\infty f_{S_n}(s) \dd s = \int_t^\infty \frac{\lambda^n}{\Gamma(n)} s^{n - 1} e^{-\lambda s} \dd s
  $$

- By partial integration
  $$
  \frac{\lambda^n}{\Gamma(n)}\int_t^\infty s^{n - 1}e^{-\lambda s} \dd s = \frac{\lambda^{n-1}}{\Gamma(n)} t^{n - 1} e^{-\lambda t} + \frac{\lambda^{n-1}}{\Gamma(n - 1)} \int_t^\infty s^{n - 2} e^{-\lambda s} \dd s
  $$

- Repeat partial integration $n - 1$ times, we have
  $$
  P(N(t) < n)  = \sum_{k = 0}^{n - 1} \frac{\lambda^{k}}{k!} t^k e^{-\lambda t} \implies P(N(t) = n) = \frac{\lambda^n}{n!} t^n e^{-\lambda t}
  $$

##### Poisson process III: infinitesimal definition

An **arrival process** $N(t)$ with following properties is a Poisson process.

- $N(0) = 0$ almost surely.

- $N(t)$ has **stationary and independent** increments.

- As $h \downarrow 0$. We have infinitesimal probability:
  $$
  P(N(t, t+h] = 0) = 1 -\lambda h + o(h), \quad P(N(t, t+h] = 1) = \lambda h + o(h)
  $$

##### Poisson process II > III

Suppose arrival process $N(t)$ follows definition II. Then we immediately have:

- $P(N_{t + h} - N_t = 0) = P(N_h = 0) = e^{-\lambda h} = 1 - \lambda h + o(h)$.
- $P(N_{t+ h} - N_t = 1) = \lambda h + o(h)$.
- $N_t$ has independent increments.

##### Poisson process III > II

Suppose arrival process $N(t)$ follows definition III. Denote $p_n(t) = P(N(t) = n)$.

We can obtain a **differential-difference equation** on $t \ge 0$ and $n \ge 0$.

1. $p'_{n + 1}(t) + \lambda p_{n + 1}(t) - \lambda p_n(t) = 0$.

   - $p_{n+1}(t + h) = p_{n+1}(t)(1 - \lambda h) + p_{n}(t)(\lambda h) + o(h)$ for $n \ge 0$ and $t, h > 0$.

   - Take $h \downarrow 0$ gives the differential difference equation.

2. $p_n(0) = \delta[n]$. Since $N(0) = 0$ almost surely.

3. $p_0'(t) = - \lambda p_0(t)$. Since $p_0(t + h) = p_0(t) (1 - \lambda h) + o(h)$.

The **unique solution** is given by:

- Suppose $P_n(s)$ is the Laplace transform of $p_n(t)$.

- Laplace transform on $3$ shows $sP_0(s) - 1 = -\lambda P_0(s)$. So $P_0(s) = 1/(s + \lambda)$.

- Laplace transform on $1$ gives $P_{n + 1}(s) = P_{n}(s) \lambda / (s + \lambda)$.

- Therefore $P_n(s) = \lambda^n / (s + \lambda)^{n+1}$.

- Therefore $N(t) \sim \operatorname{Poisson}(\lambda t)$.
  $$
  P(N(t)= n) = p_n(t) = \frac{e^{-\lambda t} (\lambda t)^n}{n!}\quad (n \ge 0, t \ge 0)
  $$

##### Poisson process II > I

Suppose $N(t)$ is a arrival process following definition II.

- For $n \ge 1$, define $S_n := \inf\{t > 0: N(t) \ge n\}$. Define $S_0 := 0$.
- Define $X_k = S_k - S_{k-1}$ for $k \ge 1$.

Then $\p{X_k}_{k = 1}^\infty \sim_{\iid} \Exp(\lambda)$.

- $X_1 \sim \Exp(\lambda)$, since $P(X_1 > t) = P(S_1 > t) = P(N(t) = 0) = e^{-\lambda t}$ for $t \ge 0$.

- $X_{k+1} \sim \Exp(\lambda)$, and $X_{k + 1} \perp \c{S_1, \ldots, S_k}$. 
  
  - For $0 < \tau_1 < \cdots < \tau_k < t$, we have
    $$
    \begin{aligned}
     \, &  \,P(X_{k + 1} > t \mid S_1 = \tau_1, \ldots, S_k = \tau_k)\\
     = &\, P(N_{t + \tau_k} - N_{\tau_k + \delta} = 0 \mid N_{\tau_1 - \delta} = 0, N_{\tau_1 + \delta} - N_{\tau_1 - \delta} = 1, \ldots, N_{\tau_k + \delta} - N_{\tau_k - \delta} = 1)\\
    = & \, P(N_{t + \tau_k} - N_{\tau_k + \delta} = 0) = e^{-\lambda t}
    \end{aligned}
    $$
  
- Therefore $\c{X_k}_{k = 1}^\infty$ is independent.

- Note that we are using right continuity in the first approximation.

