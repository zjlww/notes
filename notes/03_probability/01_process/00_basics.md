#### Stochastic Process

> The time index of processes are in general $\I \subseteq \R$.
>
> The generic interval $[0, T]$ means $[0, \infty)$ when $T = \infty$.

##### Filtration

Suppose $(\Omega, \F, P)$ is a probability space. Suppose $(\F_t)_{t \in \I}$ are sub-$\sigma$-algebras of $\F$.

- If $\forall s < t \in \I: \F_s \le \F_t$. Then $(\F_t)$ is called an **filtration** on $\F$.
  - $(\Omega, \F, (\F_t), \I, P)$ is called a **filtered probability space**.
- If $\forall s < t \in \I: \F_s \ge \F_t$. Then $(\F_t)$ is called an **reverse filtration**.
- If $\F$ is **complete** and $\F_t$ contains all $P$-null sets, $(\Omega, \F, (\F_t), \I, P)$ is called **complete**.
  - $\p{\overline \F_t} := \p{\sigma(\F_t \cup \mathcal N)}$ is the **completion** of $(\F_t)$. $\mathcal N$ are subsets of null sets in $\F$.
- Define $\F_{t+} := \cap_{s > t, s \in \I} \F_s$. In general $\F_t \neq \F_{t+}$.
  - $(\F_t)$ is called **right-continuous** if $\forall t\in \I:\F_{t+} = \F_t$.

##### Stochastic process

Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered probability space.

$(X_t)_{t \in \I} \in \L(\Omega \to E, \F / \E)$ is called a **stochastic process** on the filtered space.

- $E$ is called the set of **states**.
- $(X_t)$ is called **adapted** to **filtration** $(\F_t)$ on $\F$ if $\forall t \in T: X_t \in \L(\Omega \to E, \F_t/\E)$.
- $(\F_t^X)$ defined by $\F_t = \sigma(X_s, s \le t)$ is called the **natural filtration** of $(X_t)$.
- Suppose $\mu = (t_j)_{j = 1}^n \in T$, $X^\mu := (X_{t_1}, \ldots, X_{t_n})$.
  - Distribution of $X^\mu$ is a **finite-dimensional distribution** of $X$.

Suppose $(X_t)$ and $(Y_t)$ are stochastic processes with same state space on the filtered space.

- $(X_t)$ and $(Y_t)$ are **equivalent** if they have the same finite-dimensional distributions.
- $(X_t)$ and $(Y_t)$ are called **modification of the other** if $\forall t \in T: P(X_t = Y_t) = 1$.
  - Clearly $(X_t)$ and $(Y_t)$ are **equivalent** in this case.
- $(X_t)$ and $(Y_t)$ are **indistinguishable** if $P(\forall t \in T: X_t = Y_t) = 1$.
  - Clearly $(X_t)$ and $(Y_t)$ are **modifications** of the other in this case.
  - When $\I$ is countable, all modifications are indistinguishable.

Suppose $\I = \N$.

- $(X_n)$ is called **predictable** on the space if $X_0 = 0$ and $\forall n \ge 1: X_{n + 1} \in \F_n$.

Suppose $\I = [0, T]$, $T \in (0, \infty]$. And $E$ is **topological** with $\E$ the **Borel** $\sigma$-algebra.

- $(X_t)$ is **continuous** if $\forall \omega \in \Omega: (X_t(\omega)) \in C[\I]$.

- $(X_t)$ is **a.s. continuous** if $P(X_t \in C[\I])) = 1$.
  - Indistinguishable relationship preserves a.s. continuity.
  - Modification does not preserve a.s. continuity.
  
- We similarly define right / left-continuous and a.s. right / left-continuous.

- $(X_t)$ is **progressively measurable** with regard to $(\F_t)$.
  $$
  \forall t \in (0, T):X_u(\omega) \in \L([0,t] \times \Omega \to E, \B[0, t] \otimes \F_t/\E)
  $$

  - Progressively measurability implies adapted.
  - $(X_t)$ that is left / right-continuous is progressively measurable.
    - Consider fixed $t \in T$.
    - Consider the staircase $p_n(s): [0, t] \to [0, t]$ with step size $2^{-n}$.
      - Let $g_n(s) = (k + 1)t/2^n$ for $s \in [kt/2^n, (k+1)t/2^n)$.
      - And $p_n(s) := \min(t, g_n(s))$.
    - Define $(X_s^{(n)}) = (X_{p_n(s)})$. For each $s \in [0, t]$, $p_n(s)\downarrow s$. So $(X_s^{(n)}) \to (X_s)$ pointwise.
    - Obviously $(X_s^{(n)}) \in \B[0, t] \otimes \F_t$. So $(X_s) \in \B[0, t] \otimes \F_t$ as well.

##### Independent increment

Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered space. And $(B_t)$ is an adapted real process.

We say $(B_t)$ has **independent increments** with respect to $(\F_t)$ if any of the following is true:

1. For $s \ge 0$, $(B(s, t + s])_{t \ge 0} \perp \F_s$.

2. For all $A \in \F_s$, and any $(t_i)_{i = 1}^n > 0$, all measurable functions $F: \R^n \to \R$ that are **box indicators**.
   $$
   E\s{1_A \cdot F\p{B(s, s + t_i])_{i=1}^n}} = P(A) E\s{F\p{B(s, s + t_i])_{i = 1}^n}}
   $$

   - Notice that expectation over box indicators is equivalent to
     $$
     P(A, (B(s, s + t_i] \in A_i)_{i = 1}^n) = P(A) P((B(s, s + t_i] \in A_i)_{i = 1}^n)
     $$
     where $(A_i)_{i = 1}^n \in \B(\R)$ are intervals.

   - $1 \leftrightarrow 2$ is apparent, since testing independence on $\pi$-generator is enough.

3. Replace box indicators in 2, with bounded measurable functions.

   - $3 \to 2$ is easy to see.
   - $2 \to 3$: notice that bounded measurable functions are series of box indicators. Then apply dominated convergence.

4. Replace box indicators in 2 with bounded continuous functions.

   - The proof is similar to $3$.

Suppose $(B_t)$ is adapted to $(\F_t)$ and has independent increments with respect to $(\F_t)$. Then

- So is $\overline \F_t$. Since only null events are added.
- So is $\F_{t+}$ when $(B_t)$ is right-continuous.
  - Replace $s$ with $s + 1/n$ in $*$, then apply dominated convergence.

When we do not specify the filtration $\p{\F_t}$, the natural filtration of $\p{B_t}$ is assumed. And we have more equivalent definitions of independent increments:

5. For all $t_0 < t_1 < \cdots < t_n$ in $\I$. The random variables $\c{B_{t_0}, B(t_0, t_1], \ldots, B(t_{n - 1}, t_n]}$ are independent.

   - $1 \to 4$ is apparent.

   - $4 \to 1$ due to $\c{B_{t_0} \in A_0, B(t_0, t_1] \in A_1,\ldots}$ is a $\pi$-generator of $\F_s$.

   - When $B_0 = 0$ almost surely, $B_{t_0}$ can be dropped from the list. Otherwise, it is a mistake to drop the anchor variable $B_{t_0}$.
     - Consider the counter example $B_t(\omega) := B(\omega)$, all paths are constants, and all $B(s, t]$ are independent since they are single valued.

##### Markov process

Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered space. And $(X_t)$ is adapted real process.

$(X_t)$ is **Markov with respect to** $(\F_t)$ if any of the following is true:

1. For all $B \in \B(\R)$, $\forall s \le t \in \I: P(X_t \in B | \F_s)= P(X_t \in B | X_s)$.

2. For all **bounded continuous** $g: \R \to \R$:
   $$
   \forall s \le t \in \I: E[g(X_t) | \F_s] = E[g(X_t) | X_s] \quad (*)
   $$

   - $2 \to 1$, indicators are increasing limits of $g_n$, now apply MCT.
   - $1 \to 2$, $g$ is the sum of multiple indicator functions. Now apply DCT.
   
3. Replace bounded continuous functions in $2$ with bounded measurable functions.

$(X_t)$ is a Markov process if $(X_t)$ is Markov with respect to $(\F_t^X)$.

When we do not specify the filtration $\p{\F_t}$, the natural filtration of $\p{X_t}$ is assumed.

A Markov process $\p{X_t}$ is **time homogeneous** if for all $s, t \in \I$ and $A \in \B[\R]$ we have
$$
P(X_{s + t} \in A \mid X_s = x) = P(X_t \in A \mid X_0 = x)
$$

- For any bounded measurable $f: \R \to \R$ we have
  $$
  E[f(X_{s + t}) \mid X_s = x] = E[f(X_t) \mid X_0 = x]
  $$

##### Independent increments > Markov

Suppose $(\Omega, \F, P)$ is a probability space.

And $(X_t)_{t \in \I}$ is an adapted real process with the **independent increment** property. Then $(X_t)$ is **Markov**. (With respect to the natural filtration.)

- Only need to prove that for any $s \le t \in \I$, and $B \in \B(\R)$:
  $$
  E[1_B(X_t) | \F_s^{X}] = E[1_B(X_t) | X_s]
  $$

- First notice the following:

  - $E[1_B(X_t) | X_s = x] = E[1_B(X_t - X_s + x)]$.
  - $E[1_B(X_t)|X_{\le s} = x_{\le s}] = E[1_B(X_t - X_s + x)]$.

- Then notice:

  - $E[1_B(X_t)| X_s] = E[1_B(X_t)| X_s = X_s(\omega)]$.
  - $E[1_B(X_t) | \F_s^X] = E[1_B(X_t) | X_{\le s} = X_{\le s}(\omega)]$.

##### Delay operation and ergodic sets

Suppose $(X_t)_{t = 1}^\infty$ is a random process on $(\Omega, \F, P)$. Where $\X = \cup_t X_t[\Omega]$.

Define time delay function $\bT: \X^\infty \to \X^\infty$ as $(x_1, x_2, \ldots) \mapsto (x_2, x_3, \ldots)$.

A set of values $A \subseteq \X^\infty$ is called **$\mathbb T$-invariant** if $\bT[A] \subseteq A$.

- Clearly $\bT^k [A] \subseteq \cdots \subseteq A$ by repeated application of $\bT$.
- For any $a \in A$, denote $[a]:=\c{\mathbb T^k(a):k \in \N}$, called the $\bT$-invariant group containing $a$.

A set of values $A \subseteq \X^\infty$ is called **ergodic** if it satisfies $A = \bT^{-1}[A]$.

- Then $\bT[A] = A$.

$(X_t)$ is **ergodic** if for all ergodic sets $A \in \bX_* \F$ are either $P(A) = 1$ or $P(A) = 0$.

#### Stopping Time

##### Stopping time

Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered probability space.

$\tau \in \L(\Omega \to \I \cup \{\infty\}, \F)$ is called a **random time**.

- $\tau$ is a ($(\F_t)$-) **stopping time** if $\forall t\in \I: \{\tau \le t\} \in \F_t$.
  - When $\I$ is countable, $\tau$ is a stopping time if $\forall t\in \I: \{\tau = t\} \in \F_t$.
- $\tau$ is called **finite** if $\tau < \infty$.
- $\tau$ is called **a.s. finite** if $P(\tau < \infty) = 1$.
- $\tau$ is called **bounded** if $\tau < B < \infty$.

##### Past $\sigma$-algebra

Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered probability space.

Suppose $\sigma, \tau$ are $(\F_t)$-stopping times.

Define the **$\sigma$-algebra of $\tau$-past** as $\F_\tau := \{A \in \F: \forall t \in \I: A \cap \{\tau \le t\} \in \F_t\}$.

- $\F_\tau$ is a sub-$\sigma$-algebra of $\F$.
- $\tau \in \F_\tau$ since $\{\tau \le s\} \cap \{\tau \le t\} = \{\tau \le s\land t\} \in \F_{s \land t} \subseteq \F_t$.
- (**Monotonicity**) Suppose $\sigma \le \tau$, then $\F_\sigma \subseteq \F_\tau$.
  - Suppose $A \in \F_\sigma$, then $A \cap \{\tau \le n\} = A \cap \{\sigma \le n\} \cap \{\tau \le n\} \in \F_n$. So $A \in \F_\tau$.

##### Sampled process

Suppose $(\Omega, \F, (\F_t), \I, P)$ is a filtered probability space.

Suppose $\tau$ is a $(\F_t)$-stopping time. And $(X_t)$ is adapted to $(\F_t)$.

Then $X_\tau$ is the **sampled process**.

- Suppose $\I$ is **countable**. $X_\tau \in \F_\tau$. As $X_\tau^{-1}(B) \cap \{\tau = n\} = X_n^{-1}(B)\cap \{\tau = n\} \in \F_n$.

Suppose $\I = [0, T]$, $T \in (0, \infty]$.

- Random time $\tau$ is a **weakly stopping time** if $\forall t \in \I: \{\tau < t\} \in \F_t$.
  - Stopping implies weakly stopping. Since $\{\tau < t\} = \cup_{n}\{\tau \le t - 1/n\}$.
  - When $(\F_t)$ is **right-continuous**, and $T = \infty$ weakly stopping implies stopping.
    - Since $\{\tau \le t\} = \cap_n \{\tau < t + 1/n\} \in \F_{t+} = \F_t$.
  - When $(\F_t)$ is **right-continuous** and $T = \infty$ we have an equivalent definition of $\F_\tau = \{A \subseteq \Omega: \forall t \in [0, T]: A \cap \{\tau < t\} \in \F_t\}$.
- Define the **upper dyadic approximation** of $\tau(\omega)$ as $\tau_n(\omega):= 2^{-n}\lceil 2^n \tau\rceil \land T$ for $n \ge 1$.
  - $\tau_n \ge \tau$. When $\tau \in 2^{-n}(k - 1, k]$, $\tau_n = 2^{-n}k$.
  - $\tau_n$ are **stopping times**. Since $\{\tau_n \le t\} = \cup_{2^{-n}k \le t} \{\tau \in 2^{-n}(k - 1, k]\} \in \F_t$.
  - $\tau_n \downarrow \tau$ pointwise, so $\F_{\tau_n} \downarrow \F_\tau$.
  - When $(\F_t)$ is **right-continuous** and $T = \infty$. $\F_\tau = \cap_{n = 1}^\infty \F_{\tau_n}$.
    - $\F_\tau \subseteq \cap_n \F_{\tau_n}$ is immediate by (Monotonicity).
    - $\F_\tau \supseteq \cap_n \F_{\tau_n}$.
      - Suppose $A \in \cap_n \F_{\tau_n}$, then $A \in \F_\tau$.
      - Since $A \cap \{\tau < t\} = \cup_{n}(A \cap \{\tau_n < t\})$. So $A \in \F_\tau$.

Suppose $\sigma, \tau$ are stopping times:

- $\sigma \land \tau$ and $\sigma \lor \tau$ are stopping times.
- Constant times $s \in \I$ are stopping times.
- If $\sigma, \tau \ge 0$, then $\sigma + \tau$ is a stopping time.

##### Wald's equation

Suppose $\p{X_k}_{k = 1}^\infty \sim_{\iid} P_X$ are non-negative. And $N$ is a $(\F_n^X)$-**stopping time** of sequence $\p{X_k}$.

Let $S_k := X_1 + \ldots + X_k$. Then $E[S_N] = E[N]E[X]$.
$$
E[S_N] = E\s{\sum_{i = 1}^\infty X_i1(i \le N)} = \sum_{i = 1}^\infty E[X_i 1(i \le N)] = \sum_{i = 1}^\infty E[X] P(N \ge i)
$$
##### Strong independent inc.

Suppose $(\Omega, \F, (\F_t), [0, \infty), P)$ is a filtered space. And $(B_t)$ is an adapted real process.

$(B_t)$ has **strong independent increments** with respect to $(\F_t)$ if for any finite stopping time $\tau$:

1. $(B_{\tau + t} - B_\tau)_{t \ge 0}$ is **independent** of $\F_\tau$.

2. For all $A \in \F_\tau$, and any $(t_i)_{i = 1}^n > 0$, all **bounded continuous** $F: \R^n \to \R$:
   $$
   E[1_A \cdot F(B_{t_1 + \tau} - B_\tau, \cdots ,B_{t_{n} + \tau} - B_\tau)] = P(A) E[F(B_{t_1 + \tau} - B_\tau, \cdots ,B_{t_{n} + \tau} - B_\tau)] \quad (*)
   $$

3. For all $A \in \F_\tau$, and any $(t_i)_{i = 1}^n > 0$ and $(A_i)_{i = 1}^n \in \B(\R)$.
   $$
   P(A, \cap_i (B_{t_i + \tau} - B_\tau \in A_i)) = P(A) P(\cap_i(B_{t_i + \tau} - B_\tau \in A_i))
   $$

When no filtration is mentioned, the natural filtration of $\p{B_t}$ is assumed.

##### Strong Markov

Suppose $(\Omega, \F, (\F_t), [0, \infty), P)$ is a filtered space. And $(X_t)$ is adapted real process.

$(X_t)$ is **strongly Markov** with respect to $(\F_t)$ if for any **finite stopping time** $\tau$:

1. For all **bounded continuous** $g: \R \to \R$:
   $$
   \forall t \ge 0: E[g(X_{t + \tau}) | \F_\tau] = E[g(X_{t + \tau}) | X_\tau] \quad (*)
   $$

2. For all $B \in \B(\R)$, $\forall t \ge 0: P(X_{t + \tau} \in B | \F_\tau)= P(X_{t + \tau} \in B | X_\tau)$.

When no filtration is mentioned, the natural filtration of $\p{B_t}$ is assumed.