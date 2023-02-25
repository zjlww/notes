#### Continuous-Time Markov Chains

##### Continuous-time Markov chain

Consider stochastic process $\p{X_t}_{t \in [0, \infty)}$ with values in $S$.

- Let $\p{\F_t}$ and $\p{\G_t}$ be the forward and backward natural filtration of $\p{X_t}$.

The **Markov property** of $\p{X_t}$ with respect to the natural filtration has more definitions now: ==TODO==

1. $\F_t \perp \G_t \mid X_t$ for all $t \in \I$. Which means that
   $$
   \forall A \in \F_t, \forall B \in \G_t: P(A, B \mid X_t) = P(A \mid X_t) P(B \mid X_t)
   $$

2. For all $n \in \N$ and all sequence of states $(x_0, x_1, \ldots, x_{n - 1}, x, y)$ and time sequence $t_0 < t_1 < \cdots < t_n$ we have
   $$
   P(X_{t_{n + 1}} = y \mid X_{t_0} = x_0, \ldots, X_{t_n} = x) = P(X_{t_{n + 1}} = y \mid X_{t_n} = x)
   $$

The definition of time homogeneity is similar to DTMC. We only consider homogeneous Markov chains.

We assume that $\p{X_t}$ is **right-continuous** as a regularity constraint.

#### Jump Process

##### Holding time

Suppose $\tau = \inf \c{t \ge 0: X_t \neq X_0}$.

Then $\tau \sim \Exp \lambda(x)$ given $X_0 = x$ where $\lambda(x): S \to [0, \infty)$.

- First notice the following:
  $$
  \begin{aligned}
  P(\tau \ge t + s \mid X_0 = x, \tau \ge s) & = P(\tau \ge t + s \mid X_0 = x, X_s = x, \tau \ge s)\\
  &= P(\tau \ge t \mid X_0 = x)
  \end{aligned}
  $$

- Since $X_t$ is **right-continuous**. Then in general $\c{\tau \ge t} = \c{\tau > t}$. So we have:
  $$
  P(\tau > t + s \mid \tau > s, X_0 = x) = P(\tau > t \mid X_0 = x)
  $$

- $\tau$ is a stopping time, since $\c{\tau > t} \in \F_t$, the natural filtration.

- Since it is memoryless, $\tau \sim \Exp(\lambda(x))$ conditioning on $\c{X_0 = x}$.

  - For $\lambda(x) \in (0, \infty)$, $x$ is called a **stable state**.
  - For $\lambda(x) = 0$, $x$ is called an **absorbing state**.

- And that $X_\tau \neq X_0$ when $\tau < \infty$.

##### Jump process

 ==TODO==

Let $\tau_0 = 0$, $\tau_1 = \tau$, and define $\p{\tau_n}_{n = 2}^\infty$ recursively:

- $\tau_{n + 1} = \infty$ if $\tau_n = \infty$. $\tau_{n + 1} = \inf\c{t \ge \tau_n: X_t \neq X_{\tau_n}}$.
- $\tau_n$ is the time of $n$th state change for path $X_t(\omega)$.

Apparently $\tau_0 \le \tau_1 \le \cdots$. Define $\tau_{\infty}:= \lim_{n \to \infty} \tau_n$.

- The event $\c{\tau_{\infty} < \infty}$ is called **explosion**.
  - $X_t(\omega)$ is making infinitely many transitions within finite time!

- $\p{X_t}$ is called **regular** if $P(\tau_{\infty} = \infty) = 1$.

Let $M:= \sup \c{n \in \N: \tau_n \neq \infty}$.

- $M(\omega)$ is the total number of state change of path $X_t(\omega)$.

Define the jump chain $\p{Y_n}_{n = 0}^\infty$ as $Y_n := X_{\tau_n}$ if $\tau_n < \infty$ and $Y_n := X_{\tau_M}$ if $\tau_n = \infty$.

Then the jump chain $\p{Y_n}$ is a time homogeneous DTMC on $S$. ==TODO==.

Let $Q(x, y): S^2 \to [0, 1]$ be the transition matrix of $\p{Y_n}$.

- $Q(x, y) = P(X_\tau = y \mid X_0 = x)$ when $x$ is **stable**.
  - $Q(x, x) = 0$ when $x$ is stable.
- $Q(x, y) = \delta_{xy}$ when $x$ is **absorbing**.
  - $Q(x, x) = 1$ when $x$ is absorbing.

##### Decomposition of jump process

 ==TODO==

For $x, y \in S$,  $t \ge 0$, and $x$ is stable, we have:
$$
\begin{aligned}
P(Y_1 = y, \tau_1 > t \mid Y_0 = x) & = P(X_\tau = y, \tau > t \mid X_0 = x)\\
&= P(X_\tau = y \mid \tau > t, X_0 = x) P(\tau > t, X_0 = x)\\
& =^* P(X_\tau = y \mid X_0 = x) P(\tau > t, X_0 = x)\\
& = Q(x, y) e^{-\lambda(x) t}
\end{aligned}
$$
Suppose $n \ge 1$ and $(x_0, \ldots, x_n)$ are stable states, and $(t_1, \ldots, t_n)$ is a sequence on $[0, \infty)$.
$$
P(Y_1 = x_1, \tau_1 > t_1, \ldots, Y_n = x_n, \tau_n - \tau_{n - 1} > t_n \mid Y_0 = x_0)\\
= Q(x_0, x_1) \cdots Q(x_{n - 1}, x_n) e^{-\lambda (x_0) t_1} \cdots e^{-\lambda(x_{n - 1}) t_{n}}
$$
#### Transition Matrix

##### Transition matrix

The transition probability matrix for $t$ is
$$
P_t(x, y) := P(X_t = y \mid X_0 = x)
$$
The transition semigroup is $\mathbf P = \c{P_t: t \in [0, \infty)}$.

- $P_0(x, y) = \delta_{x, y}$ is the identity matrix.


$\bP$ is called **standard** if $P_t(x, x) \to 1$ as $t \downarrow 0$ for all $x \in S$.

- Suppose $\bP$ is standard, $P_h(x, y) \to I(x, y)$ as $h \downarrow 0$.

  - For $x \neq y$, $P_h(x, y) \le 1 - P_h(x, x) \to 0$ as $h\downarrow 0$.

  - And $P_h(x, x) \to 1$ by definition.

  - So $P_h(x, y) \to I(x, y)$ as $h \downarrow 0$.

- Suppose $\bP$ is standard, $t \mapsto P_t(x, y)$ is right continuous for all $x ,y \in S^2$.

  - Notice that by dominated convergence, as $h\downarrow 0$
    $$
    P_{t + h}(x, y) = \sum_{z \in S}P_t(x, z) P_h(z, y) \to P_t(x, y)
    $$

  - So for all $x, y \in S^2$, $t \mapsto P_t(x, y)$ is right continuous.

- Suppose $\p{X_t}$ is right continuous, $\bP$ is **standard**.

  - Notice the following:
    $$
    P_t(x, x) = P(X_t = x \mid X_0 = x) \ge P(\tau > t \mid X_0 = x) = e^{-\lambda(x) t}
    $$

  - So $P_t(x, x) \to 1$ as $t \downarrow 0$.

##### Fundamental integral equation

- Suppose $x \in S$ is an absorbing state.
  $$
  P_t(x, y) = I(x, y)
  $$

- Suppose $x \in S$ is a stable state.
  $$
  \begin{aligned}
  P_t(x, y) &= P(X_t = y \mid X_0 = x) \\
  &= P(X_t = y, \tau_1 > t \mid X_0 = x) + P(X_t = y, \tau \le t \mid X_0 = x)\\
  & = I(x, y) e^{-\lambda(x) t} + 
  \end{aligned}
  $$
