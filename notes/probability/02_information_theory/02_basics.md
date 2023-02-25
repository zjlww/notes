Consider a countable alphabet (support) $\mathcal X$. $(\mathcal X, \mathcal {PX})$ is a measurable space. The set of all probability measures (probability distributions) is denoted as $\mathcal{P_X}$.

We accept the convension that $1 / 0 = \infty$ for nonnegative values. And $0 / 0$ is undefined. $0 \cdot \infty = 0$ as in measure theory.

#### Probability Metrics

##### Metric spaces

 Suppose $V$ is a set. Suppose $d: V \times V \to [0, \infty]$ follows the following properties for all points $x, y, z$ in $V$. Then $d$ is a **metric / distance** on the space $V$. $(V, d)$ is a **metric space**.

1. $d(x, x)=0$.
2. $d(x, y)>0$ if $x \neq y$.
3. $d(x, y)=d(y, x)$.
4. $d(x, y) \leq d(x, z)+d(z, y)$.

##### Variational distance of probability distributions

 The variational distance on $\mathcal P_{\mathcal X}$ is defined as:

$$
\forall p, q \in \mathcal P_{\mathcal X}: V(p, q) := \sum_{x \in \mathcal X}|p(x) - q(x)|
$$
$(\mathcal{P_X}, V)$ is a metric space.

##### Continuity of Shannon's information measures

For $f: \mathcal P_{\mathcal X} \to [0, \infty]$. Suppose $\lim_{q \to p} f(q) = f(p)$, $f$ is called continuous. Write in full:
$$
\forall \epsilon > 0, \exists \delta > 0, \forall q \in \mathcal P_{\mathcal X}: V(p, q) < \delta \to |f(p) - f(q)| < \epsilon \iff \lim_{q \to p} f(q) = f(p)
$$
When fixing the alphabet $\mathcal X$, $\mathcal X \times \mathcal Y$, .... $H(X)$, $H(X|Y)$, $I(X; Y)$, etc. can be viewed as functions from $\mathcal{P_{X\times Y}}$ to $[0, \infty]$.

- When the alphabet is fixed and finite, all Shannon's information measures are **continuous** 
- When the alphabet is countably infinite, information measures are **everywhere discontinuous**.

##### Kullback-Leibler distance

 The **information divergence** / **relative entropy** / **KL-distance** between two   discrete probability distribution $P, Q \in \mathcal {P_X}$ with PMF $p, q$. (We do not distinguish $p$ and $P$ for the discrete case).
$$
D(p \| q)=\sum_{x \in \mathcal X} p(x) \log \frac{p(x)}{q(x)} = E_{p} \log \frac{p(X)}{q(X)}
$$
The values where $p(x) = 0$ are ignored since they are of measure-zero.

Where $E_p$ means treating $X$ as a random variable with distribution $p$. 

- The divergence is defined when $Q \ll P$, that is $q(x) = 0 \implies p(x) = 0$.
- When $Q \not \ll P$, define $D(P\| Q) = D(p \| q) = \infty$.
- Unfortunately $D(p \| q)$ is **NOT** a true distance on $\mathcal{P_X}$. It only satisfies first two of the axioms.
- $I(X; Y) = D(p(x, y) \| p(x) p(y))$ on $\mathcal {P}_{\mathcal X \times \mathcal Y}$.

##### Pinsker's Inequality, TODO

 Suppose $p, q \in \mathcal{P_X}$. Then we have a lower bound for KL divergence:
$$
D(p \| q) \ge \frac{1}{2 \ln 2} V^2(p, q)
$$
##### Examples: Two probability metrics

Consider $D_{1}(X, Y):=H(X | Y)+H(Y | X)$.

- $D_1(X, Y) = 0$ if $X \simeq Y$.
- $D_1(X, Y) > 0$ if $X \not\simeq Y$.
- $D_1(X, Y) = D_1(Y, X)$.
- $D_1(X, Y) + D_1(Y, Z) \ge D_1(X, Z)$ can be shown using the Wenn diagram.

$d_1(X, Y) =D_1(X, Y) / H(X, Y)$ gives a normalized metric.

Consider $D_{2}(X, Y):=\max(H(X | Y), H(Y | X))=\max(H(X), H(Y))-I(X ; Y)$.

The proof is similar. The most challenging part is the triangle inequality. (Hint: Without loss of generality, we can order $X, Y, Z$ so that the max is determined.)

$d_2(X, Y) = D_2(X, Y) / \max(H(X), H(Y))$ gives a normalized metric.

#### Information Inequalities

##### Logarithm inequality
$$
\forall x > 0: 1 - \frac{1}{x} \le \ln x \le x - 1
$$
Both equalities are obtained if and only if $x = 1$.

Notice that the left and right sides are equivalent by substitution $x \to 1 /x$.

##### Jessen Inequality

 Suppose $f: \R \to \R$ is convex. Suppose $X$ is a discrete real random variable. Suppose $E|X| < \infty$. Then
$$
E[f(X)] \ge f(E[X])
$$
Suppose $P(X = x_i) = \lambda_i$ for $i \in I$, where $I$ is countable.
$$
\sum_{i \in I} \lambda_{i} f\left(x_{i}\right) \ge f\left(\sum_{i \in I} \lambda_{i} x_{i}\right)
$$
##### Relative entropy inequality

 Suppose $p, q \in \mathcal{P_X}$, then
$$
D(p \| q) = \sum_{x \in \mathcal X} p(x)\log \frac{p(x)}{q(x)} \ge 0
$$
Suppose $q \not \ll p$ then define $D(p \| q) = \infty \ge 0$.

Suppose $q \ll p$ then $D(p \| q) < \infty$ and $\forall x \in \mathcal X: p(x) / q(x) \in (0, \infty)$. Then
$$
\forall x \in \mathcal X: p(x) \log \frac{p(x)}{q(x)} \ge p(x) \left(1 - \frac{q(x)}{p(x)}\right) = p(x) - q(x)\\
D(p\|q) = \sum_{x \in \mathcal X} p(x) \log \frac{p(x)}{q(x)} \ge \sum_{x \in \mathcal X} [p(x) - q(x)] = 0
$$
Suppose $D(p \| q) = 0$, then when $p(x) > 0$, $q(x) = p(x) = 1$. Therefore $p(x) = q(x)$.

##### Log-sum inequality

Suppose $(a_k)_{k \in I}$ and $(b_k)_{k \in I}$ are nonnegative real numbers. Suppose $I$ is countable.

Suppose $\sum_{k \in I} a_k = a \in (0, \infty)$ and $\sum_{k \in I} b_k = b \in (0, \infty)$. Then
$$
\sum_{k \in I} a_k \log \frac{a_k}{b_k} \ge a \log \frac{a} {b}
$$
Define $p_k = a_k / a$ and $q_k = b_k / b$.
$$
a \sum_{k \in I} p_k \log \frac{p_k}{q_k} + a \log \frac{a}{b} \ge a \log \frac{a}{b} \iff \sum_{k \in I} p_k \log \frac{p_k}{q_k} \ge 0
$$
Since $D(p \| q) \ge 0$, the log-sum inequality is proved. The equality is obtained when $p_k = q_k$.

Similarly the Log-sum inequality can prove $D(p \| q) \ge 0$. So they are equivalent.

##### Upper bound of entropy on finite alphabet

 Suppose $\mathcal X$ is finite.
$$
H(X) \le \log |\mathcal X|
$$
With equality if and only if $X \sim \operatorname{Uniform}(\mathcal X)$. Suppose $u(x) = 1 / |\mathcal X|$.
$$
D(p \| u) = \sum_{x \in \mathcal X} p(x) \log \frac{p(x)}{u(x)} = \log |\mathcal X| - H(p) \ge 0
$$
##### Fano's Inequality

 Suppose $\mathcal X$ is finite. Suppose $\widehat X$ is an discrete random variable with alphabet $\mathcal X$. $\widehat X$ is an estimate of the value of $X$. And $P(X \neq \widehat X) = p_e$.

Define $Y = 1(X \neq \widehat X)$. This is the indicator of error event. Clearly $H(Y|X, \widehat X) = 0$.
$$
\begin{aligned}
H(X | \widehat X) & = H(X | \widehat X) + H(Y | X, \widehat X)\\
& = H(X, Y | \widehat X) = H(X |\widehat X, Y) + H(Y |\widehat X)\\
& \le H(X | \widehat X, Y) + H(Y)\\
& = p_e H(X | \widehat X, Y = 1) + (1 - p_e) H(X | \widehat X, Y = 0) + H(p_e)\\
\end{aligned}
$$
with equality if and only if $\widehat X \perp Y$.

Notice that $H(X | \widehat X, Y = 0) = 0$ since $X$ is determined by $\widehat X$.
$$
H(X | \widehat X = \hat x, Y = 1) \le \log (|\mathcal X| - 1)\\
H(X | \widehat X , Y = 1) = \sum_{\hat x \in \mathcal X} p(\hat x) H(X|\widehat X = \hat x, Y = 1) \le \log (|\mathcal X| - 1)
$$
with equality if and only if $p_{Y = 1}(x| \hat x)$ is uniform.

Therefore we the **Fano's Inequality**:
$$
H(X | \widehat X) \le p_e \log (|\mathcal X| - 1) + H(p_e)
$$
with equality if and only if $\widehat X \perp Y$ and $p_{Y = 1}(x | \hat x)$ is uniform for all $\hat x \in \mathcal X$.

Very often, we only need the simplified version:
$$
H(X | \widehat X) \le 1 + p_e \log |\mathcal X|
$$
##### Maximum entropy distributions with constraints, TODO

 Suppose $r_i: \mathcal X \to \R, 1 \le i \le m$.

Maximize $H(p)$ over following constraint:
$$
\sum_{x \in \mathcal X} p(x) r_i(x) = a_i \quad (1 \le i \le m); \quad p \in \mathcal{P_X} \leftrightarrow \sum_{x \in \mathcal X} p(x) = 1
$$
Without proof, we give the solution:
$$
p^{*}(x)=\exp\left({-\lambda_{0}-\sum_{i=1}^{m} \lambda_{i} r_{i}(x)}\right)
$$
for all $x \in S$, where $\lambda_{0}, \lambda_{1}, \ldots, \lambda_{m}$ are chosen such that the constraints are satisfied. Then $p^{*}$ maximizes $H(p)$ over all probability distribution $p$ on $S$, subject to the constraints.

#### Entropy of Random Processes

Suppose $X_n, n \ge 1$ is a discrete state, discrete time random process. Image of $X_n$ is in countable set $\mathcal X$.

##### Stationary source**) Suppose $X_n, n \ge 1$ is a **stationary random process** (in the **strict sense

. $X_n$ is called a stationary source.

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

##### Entropy rate of hidden Markov process, TODO

 Suppose $X_n, n \ge 1$ is a stationary Markov process.

Suppose $f: \mathcal X \to \mathcal Y$. Then $Y_n = f(X_n), n \ge 1$ is a stationary *but not necessarily* Markov process.

> Suppose $f: \mathcal X \to \mathcal Y$ is injective or constant, $Y_n$ remains a Markov chain. Otherwise this is not necessarily true.
>
> https://math.stackexchange.com/questions/2262424

Without proof:
$$
H(Y_n | X_1, Y_{< n}) \le H_Y = \lim_{n \to \infty} H(Y_n | Y_{< n})
$$

#### Markov Chains

Suppose $X_n, n \ge 0, Y, Z$ are discrete valued random variables on probability space $(\Omega, \mathcal F, P)$.

##### Finite length markov chains

 $X, Y, Z$ forms a **(finite discrete) Markov chain**, denoted by $X \to Y \to Z$ if $X \perp Z \mid Y$. Then

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
  - Notice that $I(X; Y, Z) = I(X; Y) + I(X; Z | Y)$ is the chain rule.
  - Since $X\perp Z | Y$, so $I(X; Z| Y) = 0$.
- $I(X; Y) \ge I(X; Z)$.
  - Notice that $I(X; Y, Z) = I(X; Z) + I(X; Y | Z)$ is the chain rule.
  - So in general $I(X; Z) \le I(X; Y, Z)$.
- $I(X; Y) \ge I(W; Y) \ge I(W; Z)$.
  - Apply the rule above twice.

