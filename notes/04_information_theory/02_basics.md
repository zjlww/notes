#### Entropy of Random Processes

Suppose $X_n, n \ge 1$ is a discrete state, discrete time random process. Image of $X_n$ is in countable set $\mathcal X$.

##### Stationary source

Suppose $X_n, n \ge 1$ is a **stationary random process** in the strict sense. $X_n$ is called a stationary source.

##### Entropy rate

The entropy rate of $(X_n)$ is defined when the following limit exists.
$$
H_X = \lim_{n \to \infty} \frac{H(X_{\le n})}{n}
$$
Suppose $X_n$ is a stationary source,
$$
\forall n \in \N^+: 0 \le H(X_n | X_{1:n}) \le H(X_n | X_{2:n}) = H(X_{n-1}|X_{1:n-1})
$$
Therefore $H(X_n | X_{<n})$ **decreases and converges**. Suppose $H(X_n | X_{<n}) \to h$.

Therefore $H_X$ exists and:
$$
H_X = \lim_{n \to \infty} \frac{\sum_{k=1}^n H(X_n | X_{<n})}{n} = \lim_{n \to \infty} H(X_n | X_{< n})
$$
Further suppose $X_n$ is a Markov source, $H_X = \lim_{n \to \infty}H(X_n | X_{n-1})$.

Further suppose $X_n$ is a stationary Markov source, $H_X = H(X_2 | X_1)$.

##### Entropy rate of hidden Markov process ==TODO==

Suppose $X_n, n \ge 1$ is a stationary Markov process.

Suppose $f: \mathcal X \to \mathcal Y$. Then $Y_n = f(X_n), n \ge 1$ is a stationary *but not necessarily* Markov process.

> Suppose $f: \mathcal X \to \mathcal Y$ is injective or constant, $Y_n$ remains a Markov chain. Otherwise this is not necessarily true.
>
> https://math.stackexchange.com/questions/2262424

Without proof:
$$
H(Y_n | X_1, Y_{< n}) \le H_Y = \lim_{n \to \infty} H(Y_n | Y_{< n})
$$

#### Markov processes and information measures

Suppose $X_n, n \ge 0, Y, Z$ are random variables on probability space $(\Omega, \mathcal F, P)$.

##### Finite length Markov processes

 $X, Y, Z$ forms a Markov process, denoted by $X \to Y \to Z$ if $X \perp Z \mid Y$. 

- The splitting form: $p(x, z | y) = p(x | y) p(z | y)$.
- The symmetric form: $p(x, y, z) p(y) = p(x, y) p(y, z)$.
- The jumping form: $p(x, y, z) = p(x) p(y | x)p(z|y)$.
- The shortened form: $p(z | x, y) = p(z|y)$.
- $X \to Y \to Z \iff Z \to Y \to X \iff X \perp Z \mid Y$.

$X_1 \to X_2 \to X_3 \to \cdots \to X_n$ for $n > 3$ forms a Markov chain if

- The symmetric form:
  $$
  p(x_1, \cdots, x_n) p(x_2) p(x_3)\cdots p(x_{n-1}) = p(x_1, x_2) p(x_2, x_3) \cdots p(x_{n-1}, x_n)
  $$

- The jumping form:
  $$
  p(x_1, \cdots, x_n) = p(x_1) p(x_2 | x_1) p(x_3 | x_2) \cdots p(x_n | x_{n-1})
  $$

- The shortened form:
  $$
  \forall t \in \{1, \cdots, n\}: p(x_t | x_{<t}) = p(x_t| x_{t-1})
  $$

##### Transforms of finite Markov chains

If $X_1 \to X_2 \to \cdots \to X_n$ is a Markov chain of finite length $n > 3$. We have the following results:

- Removing r.v.s on the end: $X_1 \to \cdots \to X_n \implies X_1 \to X_2 \to \cdots \to X_{n-1}$.

  - Sum over $x_n$ in $p(x_1, \cdots, x_n) p(x_2) \cdots p(x_{n-1}) = p(x_1, x_2) \cdots p(x_{n-1}, x_n)$.

- Removing r.v.s in the middle: $X_1 \to \cdots \to X_n \implies X_1 \to \cdots X_{k - 1} \to X_{k + 1} \to \cdots \to X_n$.

  - Since $X_{k - 1} \to X_k \to X_{k + 1}$ we have:
    $$
    p(x_{k-1}, x_k, x_{k+1}) p(x_k) = p(x_{k-1}, x_{k}) p(x_k, x_{k+1})
    $$

  - Plug this into the symmetric form definition, then sum over $x_k$.

- Combining r.v.s: $X_1 \to X_2 \to \cdots \to (X_k, X_{k+1}) \to \cdots \to X_n \,(1 \le k \lt n)$.

  - Rather straight forward using the jumping form.

##### Information inequalities for Markov chains

Suppose $W \to X \to Y \to Z$.

- $I(X; Y, Z) = I(X; Y) + I(X; Z | Y) = I(X; Y)$.
  - Notice that $I(X; Y, Z) = I(X; Y) + I(X; Z | Y)$ following from the chain rule.
  - Since $X\perp Z | Y$, so $I(X; Z| Y) = 0$.
- $I(X; Y) \ge I(X; Z)$.
  - Notice that $I(X; Y, Z) = I(X; Z) + I(X; Y | Z)$ is the chain rule.
  - So in general $I(X; Z) \le I(X; Y, Z)$.
- $I(X; Y) \ge I(W; Y) \ge I(W; Z)$.
  - Apply the rule above twice.

