#### Conditional Distributions in Poisson Process

##### Conditional distributions on $S_n$

Consider Poisson process $N(t)$ with rate $\lambda$, and $\p{X_k}, \p{S_k}$ defined as in previous notes.

$X_1, X_2, \ldots, X_{k - 1}, S_{k}$ has **joint density** $f(x_1, \ldots, x_{k - 1}, s_{k}) = \lambda^{k} e^{-\lambda s_{k}}$.

- Denote $f(x) = \lambda e^{-\lambda t}$ for $t > 0$. And $F(x) = 1 - e^{-\lambda t}$.

- Consider the joint distribution, take $k = 2$ for example:
  $$
  \begin{aligned}
  P(X_1 \le x_1, S_2 \le s_2) &= P(X_1 \le x_1, X_1 + X_2 \le s_2) = \int_0^{x_1} \p{\int_0^{s_2 - x_1} f(y) \dd y} f(x)\dd x\\
  & = \int_0^{x_1} \p{1 - e^{-\lambda(s_2 - x)}} \lambda e^{-\lambda x} \dd x = F(x_1) - \lambda x_1 e^{-\lambda s_2}
  \end{aligned}
  $$

- By some observation, this immediately gives:
  $$
  P(X_1 \le x_1, X_2 \le x_2, \ldots, X_{k - 1} \le x_{k - 1}, S_k \le s_k) = \prod_{i = 1}^{k - 1} F(x_i) - \lambda^{k - 1} \prod_{i = 1}^{k - 1}x_i e^{-\lambda s_k}
  $$

- Now take derivative:
  $$
  f(x_1, \ldots, x_{k - 1}, s_k) = \lambda^{k} e^{-\lambda s_k}
  $$

$S_1, \ldots, S_k$ has joint density $f(s_1, \ldots, s_k) = \lambda^{k} e^{-\lambda s_k}$.

- The measure of triangle $\triangle := \c{0 < s_1 < \cdots < s_{k - 1} < s_k}$ is $s_k^{k - 1} / \Gamma(k)$. Note:
  $$
  f(s_k) = \int_\triangle f(s_{< k}, s_k) \dd s_{< k} = \frac{s_k^{k - 1}}{\Gamma(k)} \lambda^k e^{-\lambda s_k} = \Gamma(s_k; k, \lambda)
  $$

- Notice that $(S_1, \ldots, S_{k - 1})$ is a linear transform of $(X_1, \ldots, X_{k - 1})$, with determinant one.

##### Conditional distributions on $N(t)$

Consider Poisson process $N(t)$ with rate $\lambda$, and $\p{X_k}, \p{S_k}$ defined as in previous notes.

Conditional on $\c{N(t) = n}$, $S_1, \ldots, S_n$ has uniform density.

- Let $F_{S_1, \ldots, S_n \mid N(t) = n}(s_1, \ldots, s_n)$ be the joint distribution function of $S_1, \ldots, S_n$ in subspace.

- Recall that
  $$
  p_n(t) = e^{-\lambda t} \frac{\lambda^n}{n!} t^n, \quad p_0(t) = e^{-\lambda t}
  $$

- For $h_1, \ldots, h_n > 0$ small enough, and $0 < s_1 < \cdots < s_n < t$.
  $$
  \begin{aligned}
  F(s_k + h_k) - F(s_k) &= \frac{P(S_k \in (s_k, s_k + h_k], N(t) = n)}{P(N(t) = n)}\\
  &= \frac{P(N_{s_k + h_k} - N_{s_k} = 1, N_{s_k} - N_{s_{k - 1} + h_{k - 1}} = 0,\cdots)}{P(N(t) = n)}\\
  & = \frac{p_0(t)\prod_{i = 1}^n \lambda h_{i}}{p_n(t)} = \frac{n! \prod_{i=1}^n h_i}{t^n}
  \end{aligned}
  $$

- Therefore $F$ is almost surely differentiable. It admits density
  $$
  f(s_1, \ldots, s_n) = \frac{n!}{t^n}
  $$
  
- Note that $t^n / n!$ happens to be the measure of all allowed values of $s_1, \ldots, s_n$.

Conditional on $\c{N(t) = n}$, $X_1, \ldots, X_n$ has uniform density.

- Since $(X_1, \ldots, X_n)$ is a linear transform of $\p{S_n}$ with unit determinant.

Conditional on $\c{N(t) = n}$, consider the density of $S_k$ where $1 \le k \le n$.

- Since $f_{S_k \mid N(t) = n}(s_1, \ldots, s_n)$ is known constant. Marginalize:
  $$
  f(s_k) = \frac{n!}{t^n} \frac{s_k^{k - 1}}{(k - 1)!} \frac{(t - s_k)^{n - k}}{(n - k)!} = \frac{n}{t} C_{n - 1}^{k - 1} \p{\frac{s_k}{t}}^{k - 1}\p{\frac{t - s_k}{t}}^{n - k}
  $$

  - The intuition is integrate over two triangular regions.
  
- Or we could directly compute $F_{S_k}(s_k)$ then differentiate:

  - Take $h > 0$ near zero.
    $$
    \begin{aligned}
    F(s_k + h) - F(s_k) & = \frac{P(S_k \in (s_k, s_k + h], N(t) = n)}{P(N(t) = n)}\\
    & = \frac{p_{k - 1}(s_k - h) \lambda h p_{n - k}(t - s_k - h)}{p_n(t)}
    \end{aligned}
    $$

  - Therefore
    $$
    f(s_k) = \frac{\lambda p_{k - 1}(s_{k}) p_{n - k}(t - s_k)}{p_n(t)} = \frac{n!}{(n - k)!(k - 1)!} \frac{s_k^{k - 1} (t - s_k)^{n - k}}{t^n}
    $$

Conditional on $\c{N(t) = n}$, the distribution of $N(s) \sim \operatorname{Binomial}(n, s/t)$ for $s \in (0, t)$.

- Compute $P(N(s) = k \mid N(t) = n)$ with brute force:
  $$
  P(N(s) = k \mid N(t) = n) = \frac{p_{n - k}(t - s) p_k (s)}{p_n(t)} = C_n^k \p{\frac{s}{t}}^k \p{\frac{t - s}{t}}^{n - k}
  $$

#### Merging and Splitting Poisson Processes

##### Sum of independent Poisson processes

Suppose $N_1(t)$ and $N_2(t)$ are independent Poisson processes with rates $\lambda_1$ and $\lambda_2$.

Define $N(t) = N_1 (t) + N_2(t)$. Then $N(t)$ is a Poisson process with rate $\lambda = \lambda_1 + \lambda_2$.

- Verify the infinitesimal definition III:
  - $N(t)$ clearly has stationary and independent increments.
  - $N(t)$ clearly obeys the differential equations for rate $\lambda_1 + \lambda_2$.
  - $N(t)$ clearly is a counting process.
- distributional definition II also works:
  - $N(t)$ clearly is a counting process with stationary and independent increments.
  - $N(t) \sim \operatorname{Poisson}((\lambda_1 + \lambda_2) t)$ since $N(t) = N_1(t) + N_2(t)$.


##### Splitting a Poisson process

Suppose $N(t)$ is a Poisson process with rate $\lambda$.

Suppose there are **i.i.d. Bernoulli** random variables $\p{B_{k}}_{k = 1}^\infty \sim_{\iid} \operatorname{Bernoulli}(m, \mathbf p)$. Where $\c{B_k} \perp \c{N(t)}$.

Define a split Poisson process as $N_r(t) = \sum_{k = 1}^\infty 1(B_k = r, S_k \le t)$.

Then $N_0(t), N_1(t)$ are Poisson processes with rates $\lambda q, \lambda p$. And $\c{N_0(t)} \perp \c{N_1(t)}$!

- $N_0(s) - N_0(t) \perp N_1(s) - N_1(t)$.

  - The independence is true, by direct computation of the probability.
    $$
    P\p{N_0(t) = m, N_1(t) = k} = \cc{m + k}{m} p^k q^m \frac{(\lambda t)^{m + k}e^{-\lambda t}}{(m + k)!}
    $$

  - This expression is separable.
    $$
    P(N_0(t) = m, N_1(t) = k) = \frac{(q \lambda t)^{m} e^{-\lambda q t}}{m !} \frac{(p \lambda t)^{k} e^{-\lambda p t}}{k !}
    $$

  - Clearly $N_0(t), N_1(t)$ have **stationary** increments.

  - And the distribution of $N_0(a, b]$ is the correct Poisson distribution.

- $N_0(t), N_1(t)$ have **independent** increments.

  - Hint: Conditioning on value of $N(a, b]$ and $N(c, d]$, $N_0(a, b] \perp N_0(c, d]$.
  - Now summation on both sides over all possible values.

- $\c{N_0 (t)} \perp \c{N_1(t)}$.

  - Hint: We only need to show that the following independence for $t_1 < \cdots < t_n$.
    $$
    \c{N_0(t_1, t_2], \ldots, N_0(t_{n - 1}, t_n]} \perp \c{N_1(t_1, t_2], \ldots, N_1(t_{n - 1}, t_n]}
    $$

  - Hint: Apply the same trick by conditioning on values of $\c{N(t_1, t_2],\ldots}$.

  - Then split, separate, and take summation.

#### Non-homogeneous Poisson Process

##### Rate functions

$\lambda(t)\in \L([0, \infty)\to [0, \infty))$ is a **rate function** if

- $\lambda(t)$ is continuous.
- Denote $\lambda(s, t] := \int_s^t \lambda(\tau) \dd \tau$, which is **not** bounded as $t \to \infty$.

##### Non-homogeneous Poisson process I: infinitesimal definition

A counting process $N(t)$ is a **non-homogeneous Poisson process** with rate $\lambda(t)$ if

- $N(t)$ has independent increments.
- $P(N(t, t+h] = 0) = 1 - \lambda(t) h + o(h)$, as $h \downarrow 0$.
- $P(N(t, t +h] = 1) = \lambda(t) h + o(h))$, as $h \downarrow 0$.

##### Non-homogeneous Poisson process II: distributional definition

A counting process $N(t)$ is a **non-homogeneous Poisson process** with rate $\lambda(t)$ if

- $N(t)$ has independent increments.

- $N(t)$ has following distribution.
  $$
  P(N(s, t] = n) = \frac{\lambda^n(s, t] e^{-\lambda(s, t]}}{n!}
  $$

##### Non-homogeneous Poisson process: I = II

II > I direction is simple, consider I > II direction.

Without loss of generality, assume $s = 0$.

Define $p_n(t) = P(N(0, t] = n)$. For $h \downarrow 0$ we have:

- $p_{n + 1}'(t) = -\lambda(t) p_{n + 1}(t) + \lambda(t) p_n(t)$ for $n, t \ge 0$.
  - Since $p_{n + 1}(t + h) = p_{n +1}(t)(1 - \lambda(t) h) + p_{n}(t)\lambda(t) h + o(h)$.
- $p_n(0) = \delta[n]$.
- $p'_0(t) = -\lambda(t) p_0(t)$ for $t \ge 0$.
  - Since $p_{0}(t + h) = p_0(t)(1 - h\lambda(t)) + o(h)$.

This is a differential-difference equation IVP. Solve with induction.

- We guess that the solution is
  $$
  p_{n}(t) = \frac{\lambda^n(0, t] e^{-\lambda(0, t]}}{n!}
  $$

- $p_0(t) = e^{-\lambda(0, t]}$, satisfies the solution.

- Now suppose the solution is correct for $n$, consider $n + 1$.
  $$
  p_{n + 1}'(t) = -\lambda(t) p_{n + 1}(t) + \lambda(t) p_{n}(t)
  $$

##### Existence of non-homogeneous Poisson process: time change

Given rate function $\lambda(t)$, there exists a Non-homogeneous Poisson process.

- There exists a homogeneous Poisson process $N(t)$ of unit rate on some space.
- Consider process $N(\lambda(0, t])$. This is the desired process.

#### Compound Poisson Process

##### Compound Poisson process: I

Suppose $N(t)$ is a Poisson process with rate $\lambda$.

Suppose $U, \p{U_k}_{k = 1}^\infty$ are i.i.d. real random variables. And $\c{U, \p{U_k}} \perp \c{N(t)}$.

Let $S_n: = \sum_{i = 1}^n U_i$. Define $M(t) := \sum_{i = 1}^\infty U_i 1(S_i \le t) = S_{N(t)}$.

- Suppose $U$ has density $f(u)$

$M(t)$ is called a **compound Poisson process** with jump distribution $P_U$.

- $M(t)$ has stationary increments.
  - Hint: Consider the distribution of $M(s, t]$ conditioning on $N(s, t] = n$.
- $M(t)$ has independent increments.
  - Hint: Consider the distribution of $M(t_0), \ldots, M(t_{k - 1}, t_k]$ conditioning on $N(t_0), \ldots$.
- Following from Wald's identity:
  - $E[M(t)] = \lambda t E[U]$.
  - $\var(M(t)) = \lambda t(E^2[U] + \var(U)) = \lambda t E[U^2]$.


##### Compound Poisson process: generating function

Consider the (probability, moment, characteristic) generating function of $M(t)$.

- Let $M_t(z) = E[z^{M(t)}]$, $N_t(z) = E[z^{N(t)}]$ and $U(z) = E[z^D]$.
- $E[z^{M(t)}] = E[z^{S_{N(t)}}] = E[E[z^{S_{N(t)}}\mid N(t)]] = N_t(U(z))$.
  - $N_t(z) = e^{\lambda t(z - 1)}$. So $M_t(z) = \exp[\lambda t(U(z) - 1)]$.

##### Compound Poisson process: finite values

Suppose $N(t)$ is a Poisson process with rate $\lambda$.

Suppose $U, \p{U_k}_{k = 1}^\infty$ are i.i.d. real random variables. And $\c{U, \p{U_k}} \perp \c{N(t)}$.

Suppose $U$ obtains only **finitely** many values $\c{a_k}_{k = 1}^r$ with probability $\mathbf p = \c{p_k}_{k = 1}^r$.

Let $M(t)$ be a compound Poisson process with jump distribution $P_U$.

The compound Poisson process $M(t)$ can be generated by a split and reweighing.

- Let $B_k$ be categorical variables where $B_k = m$ when $U_k = a_m$.
- Split $N(t)$ with $\p{B_k}$ into independent Poisson processes $N_k(t)$.
- Then $M(t) = \sum_{k = 1}^r a_k N_k(t)$.

