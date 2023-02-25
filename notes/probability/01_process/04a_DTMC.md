#### Discrete-Time Markov Chains

> Suppose $(\Omega, \F, P)$ is a probability space. Suppose $S$ is **at most countable**, endowed with the counting measure.
>
> For discrete-time Markov chain, we assume that $\I = \N$.

##### Discrete-time Markov chain

Consider stochastic process $\p{X_n}_{n \in \N}$ with values in $S$.

- Let $\p{\F_n}$ and $\p{\G_n}$ be the forward and backward natural filtration of $\p{X_n}$.

The **Markov property** of $\p{X_n}$ with respect to the natural filtration has more definitions now: ==TODO, verify equivalence==

1. $\F_n \perp \G_n \mid X_n$ for all $n \in \N$. Which means that
   $$
   \forall A \in \F_n, \forall B \in \G_n: P(A, B \mid X_n) = P(A \mid X_n) P(B \mid X_n)
   $$

2. $P(X_{n + 1} =x \mid \F_n) = P(X_{n + 1} =x \mid X_n)$ for any $x \in S$.

   - This replaces the $X_{n + m}$ by $X_{n + 1}$ from the general definition.

3. $E[f(X_{n + 1}) \mid \F_n] = E[f(X_{n + 1}) \mid X_n]$ for any bounded function $f$ on $S$ to $\R$.

4. For all $n \in \N$ and all sequence of states $(x_0, x_1, \ldots, x_{n - 1}, x, y)$ we have
   $$
   P(X_{n + 1} = y \mid X_0 = x_0, \ldots, X_n = x) = P(X_{n + 1} = y \mid X_n = x)
   $$

A Markov chain $\p{X_n}$ is **time homogeneous** if
$$
\forall x, y \in S, \forall k, n \in \N: P(X_{n + k} = y \mid X_k = x) = P(X_n = y \mid X_0 = x)
$$
We will now assuming $\p{X_n}$ is a time homogeneous Markov chain from now on.

##### Transition matrix

For $n \in \N$, for $x, y \in S$, define the $n$-step transition matrix as
$$
p_{xy}^{(n)} = P_n(x, y):= P(X_n = y \mid X_0 = x)
$$

- $P_n$ can be viewed as a Markov probability kernel.
  $$
  P_n(x, A) := \sum_{y \in A}P_n(x, y) = P(X_n \in A \mid X_0 = x)
  $$
  
- Acting on the right, $P_n(x, \cdot)$ gives $\int P_n(x, \dd y) f(y) = E[f(X_n) \mid X_0 = x]$ since
  $$
  \int_{A} \p{\int P_n (x, \dd y) f(y)} \dd x = \iint 1_{A}(x) f(y) \dd Q(x, y) = \int_A E[f(X_n)\mid X_0 = x] \dd x
  $$

- Acting on the left, for $f: S \to [0, \infty]$, define
  $$
  (f  P_n)(y) := \sum_{x \in S} f(x) P_n(x, y)
  $$

  - $f$ is invariant for the Markov chain if $fP_1 = fP_n = f$.
  - Suppose $f$ is probability density of $P_{X_0}$, $fP_n$ is the density of $P_{X_n}$.

##### Chapman-Kolmogorov equation
$$
P_{n + m}(x, y) = \sum_{z \in S} P_n(x, z) P_m(z, y)
$$

- Observe that the conditional
  $$
  \begin{aligned}
  P(X_{n + m} = y \mid X_0 = x) & = \sum_{z\in S}P(X_{n + m} = y, X_n = z\mid X_0 = x)\\
  & = \sum_{z \in S} P(X_{n + m} = y \mid X_n = z, X_0 = x) P(X_n = z \mid X_0 = x)
  \end{aligned}
  $$
  
- We can also view $P_n$ as a matrix when $S$ is finite.

##### Higher order Markov chain

Consider random process $X_n, n \ge 0$ with state space $S$.

$X_n$ has $k$th order Markov property if:
$$
\forall n \ge k, \forall s \in S: P[X_n = s \mid X_{n-1}, \cdots ,X_{0}] = P[X_n = s \mid X_{n-1}, X_{n-2}, \ldots, X_{n-k}]
$$
We could redefine the states space as $S^{k}$, and define $Y_{n} = (X_{n-k+1}, \cdots, X_{n})$. Now notice:
$$
\forall n \ge k, \forall \mathbf s \in S^{k}: P[Y_n = \mathbf s \mid Y_{n-1}, \cdots, Y_{0}] = P[Y_n = \mathbf s\mid Y_{n-1}]
$$

- Now the initial state is $Y_{k-1} = (X_0, \cdots, X_{k-1})$. We may shift time to start with $Y_0$.
- Suppose $S$ is finite, each $\mathbf s \in S^k$ now only transition to $|S|$ other states. So the transition matrix is quite sparse.

#### Connectedness of States

##### Transition graph of Markov chains

The transition graph of a DTMC $\p{X_n}_{n \in \N}$ is a **single weighted directed graph** $G = (S, E)$, where
$$
E := \{(i, j) \in S^2: p_{ij} > 0\}
$$
##### Path and cycles in directed graphs

Consider graph $G = (S, E)$, where $S$ are vertices, and $E$ is the set of edges.

- A $n$-step walk is any tuple $(i_0, \cdots, i_n), n \ge 1$, where $(i_k, i_{k+1}) \in E$.
- A **path** is a walk in which no nodes are repeated. 
- A **cycle** is a walk where $i_0 = i_n$ and no other node is repeated.

##### Accessibility of states

Consider Markov chain $X_n, n \ge 0$ and its transition graph $(S, E)$.

- $i$ leads to $j$, denoted as $i \to j$ if there exists a **walk** from $i$ to $j$.
  - $i \to j \iff \exists n \ge 0: P_n(i, j) > 0$.
  - $i \to j \land j \to k \implies i \to k$.
    - Since $P_n(i, j) > 0 \land P_m(j, k) > 0 \implies P_{n + m}(i, k) > 0$.

- $T \subseteq S$ is called **closed** if $\forall i \in T, \forall j \notin T: i \not \to j$.

  - The sub-matrix $P|_T$ is a probability matrix.

  - And $(P|_T)^n = (P^n)|_T$.

    - Suppose $s, t \in T$, then
      $$
      P_n(s, t) = \sum_{k \in S} P_{n -1}(s, k) P(k, t) = \sum_{k \in T} P_{n - 1}(s, k) P(k, t)
      $$

- For $i \neq j$, suppose $i \to j$ and $j \to i$, then $i$ and $j$ **communicate**.
  - $i \lr j \land j \lr k \implies i \lr k$.
  - $\lr$ is an **equivalence** relationship in $S$.

- The equivalence classes of $\lr$ are called just **classes** of the Markov chain.
  - A path starts inside a class **cannot** go outside then **go back** in.

- $T$ is **irreducible** if $T$ is a closed class.

  - Equivalently, if $T$ is closed and has no proper closed subsets.

- If $S$ is irreducible, the Markov chain is called **irreducible**.


##### Source and sink states

- Suppose $p_{tt} = 1$, then $t \in S$ is called an **sink** state.
  - Each sink state forms a singleton class $\c t$ that is closed.
  - Equivalently: $\forall s \in S: t \not \to s$.
- Suppose for all $s \in S$, $p_{st} = 0$, then $t \in S$ is called an **source** state.
  - Each inessential state forms a singleton class $\c{t}$.
  - Equivalently: $\forall t \in S: s \not \to t$.

##### The class graph

Let classes be nodes. Define edge $[i] \to [j]$ if $i \to j$. Such a graph is called the class graph.

The class graph must be a **directed acyclic graph**.

- The leaf nodes are exactly the closed classes.

#### Period of States

##### Period of a sequence

The **period** of sequence $\p{a_n}_{n = 1}^\infty$ is defined as
$$
M_a = \{n \ge 1: a_n > 0\}; \quad d(a_n) = \gcd M_a
$$

- Define $\gcd \varnothing := 0$.
- A sequence is **periodic** if $d(a) > 1$. Otherwise it is **aperiodic**.

##### Period of states

The period of state $i \in S$ denoted by $d(i)$ is defined by:
$$
d(i):= d\p{P_n(i, i)} = \gcd\c{n \ge 1: P_n(i, i) > 0}
$$

- Suppose $d(i) = 1$, the state is called **aperiodic**.
- Suppose $d(i) > 1$, the state is **periodic** with period $d(i)$.

Suppose $i \lr j$. Then $d(i) = d(j)$.

- Consider $i \to j$, loop at $j$, then $j \to i$. This path implies $d(j) \mid d(i)$.
- By symmetry, $d(i) \mid d(j)$.

The **period of a class** $T \subseteq S$ is the period of any of its states, denoted by $d(T)$.

- Suppose $d(T) = 1$, the class is called aperiodic.
- Otherwise the class is called periodic with period $d(T)$.

##### Cyclic subclasses of a periodic class

Suppose $T \subseteq S$ is a periodic class with period $d > 1$. It can be further partitioned into cyclic subclasses $T_0, \ldots, T_{d - 1}$. Where $T_{k}$ only points to $T_{k + 1 \bmod d}$.

- Pick a starting node $s \in T$ to assign number $0$.
- If there is a walk from $s$ to $t$ with length $l$, **tag** $t$ by $l \bmod d$.
- It is not possible to tag two different numbers to a single node, due to periodicity.
- Collect states into sets $T_0, \cdots, T_{d-1} \subseteq T$ by tags on states.

Under new transition matrix $P' := P^d$, $\c{T_0, \ldots, T_{d - 1}}$ becomes separate classes!

- The structure of the class graph may be very different.
