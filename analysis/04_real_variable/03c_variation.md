#### Variation of Partitions

(**Partition of compact interval**)

For points $(x_i)_{i=0}^{n} \in [a, b]$, $a = x_0<x_i < x_{i+1} < x_n = b$. $P = (x_i)_{i= 1}^n$ is a **partition** of $[a, b]$.

- $[x_{k-1}, x_k]$ is the $k$-th **subinterval** of $P$.
- Define $\Delta x_{k}=x_{k}-x_{k-1}$, so that $\sum_{k=1}^{n} \Delta x_{k}=b-a$.
- Define $\Delta f_k = f(x_k)  - f(x_{k-1})$, so that $\sum_{k=1}^n \Delta f_k = f(b) - f(a)$.
- $P[a, b]$ is the set of all partitions of $[a, b]$.
- The **norm** of $P$ is $\n{P} :=\max\{\Delta x_k\}$.
- $P'$ is **finer** than $P$ if $P \subset P'$.
  - Clearly $\n{P'} \le \n{P}$.

(**Variation**)

Suppose $f: [a, b] \to \R$ and $P \in P[a, b]$. Define $\Sigma(P, f)$ as following:
$$
\Sigma(P, f) := \sum_{k=1}^{|P| - 1} \abs{\Delta f_k}
$$
$\Sigma(P, f)$ is the variation of $f$ under partition $P$.

- Refinement increases the variation. Suppose $P' \supset P$, $\Sigma(P', f) \ge \Sigma(P, f)$.

(**Bounded variation**)

$f:[a, b] \to \R$ is of **bounded variation** when $\Sigma(\cdot, f)$ is bounded. Denoted by $f \in V[a, b]$.

- $f \in LC[a, b] \implies f \in V[a, b]$.
  - Suppose $f$ is $K$-Lipschitz continuous, $\Sigma(\cdot, f) \le K\abs{b - a}$.

- $f \in V[a,b] \implies f \in B[a, b]$.
  - Clearly if $f$ is unbounded, $\Sigma(\cdot, f)$ is also unbounded.

- $V[a, b]$ is a vector field over $\R$.

(**Total variation**)

Suppose $f: [a, b] \to \R$. Consider set $R := \c{a \le s < t \le b: s, t \in \R}$.

Define $V_f(s, t): R \to [0, \infty]$ as
$$
V_f(s, t) := \sup\left \{\Sigma(P, f): P \in P[s, t]\right\}
$$

- When the range is clear, we also write $V_f = V_f(s, t)$.
- Define $V_f(s, s) = 0$ for $s \in [a, b]$.
- $V_f(s, t) = 0$ if and only if $f$ is constant on $[s, t]$.
- Suppose $f \in C^1(a, b)$, then $V_f(a, t) = \int_a^t |f'(s)|ds$.

We have following bounds on $V_f = V_f(a, b)$:
- $V_{cf} = cV_f$.
- $V_{f \pm g} \le V_f + V_g$.
- $V_{f \cdot g} \le A V_f + B V_g$ where $A = \sup g[a, b]$ and $B = \sup f[a, b]$.
- Suppose $\forall x \in [a, b]: 0 < m \le |f(x)|$, then $h = 1/f$ is of bounded variation and $V_g \le V_f/m^2$.

Let $c \in (a, b)$. Then $V_f(a, b) = V_f(a, c) + V_f(c, b)$.

(**Total variation function**)

Suppose $f: [a, b] \to \R$. Define $V(x):= V_f(a, x)$ for $x \in [a, b]$.
- $V(x)$ is increasing on $[a, b]$.
- $V(x) - f(x)$ is increasing on $[a, b]$.
  - Since for $t > s$: $V(t) - V(s) = V_f(s, t) \ge |f(s) - f(t)| \ge f(t) - f(s)$.
- $V(x)$ is right-continuous at $c \in [a, b]$ iff $f(x)$ is right-continuous at $c$. (resp. left)
  - Hint: Consider the contrapositive.


(**Increasing real functions**)

Suppose $f: [a, b] \to \R$ is **increasing** on $[a, b]$.

- One-sided limit exists at any $p \in [a, b]$. **All discontinuities in $[a, b]$ are jumps**.
  - Jump at $p \in (a, b)$ is defined as $\hat f(p) = f(p+) - f(p-)$.
- For any partition $\{x_k\}$, the total jump size is **bounded** $\sum_{k=1}^{n-1} \hat f(x_k) \le f(b) - f(a)$.
- The set of discontinuous points of $f$ in $[a, b]$ is **countable**.
  - Any convergent nonnegative sum has at most countably many non-zero terms.


(**Decompose bounded variation functions**)

Suppose $f: [a, b] \to \R$.

- $f$ is increasing implies $f \in V[a, b]$.
- $f \in V[a, b]$ implies $f$ is the difference of two increasing functions on $[a, b] \to \R$
  - Consider $V(x) - (V(x) - f(x))$.
- $f \in V[a, b]$ implies $f$ has only jump discontinuities on $[a, b]$.

#### Rectifiable Path in $\R^n$

(**Inscribed polygon of paths**)

Suppose $f: [a, b] \to \R^n$ is a path (**continuous**).

For $P = (t_i)_{i=0}^m \in P[a, b]$. $(f(t_i))_{i = 0}^m$ are the vertices of the **inscribed polygon**.

The **length** of this polygon $\Lambda(P, f)=\sum_{k=1}^{m}\left\|f\left(t_{k}\right)-f\left(t_{k-1}\right)\right\|$.

(**Length of graph**)

Suppose $f: [a, b] \to \R^n$ is a path. Consider the graph $f[a, b]$.

Define the **length of graph** $f[a, b]$ as $\Lambda_f(a, b) = \sup \{\Lambda(P, f): P \in P[a, b]\}$.

- $\Lambda_f(a, b) = \Lambda_f(a, c) + \Lambda_f(c, b)$ for $c \in (a, b)$.

Define length function $\Lambda(x): [a, b] \to [0, \infty]$ as $\Lambda(x) := \Lambda_f(a, x)$.

- $\Lambda(x)$ is continuous and increasing.

(**Rectifiable path**)

Suppose $f: [a, b] \to \R^n$ is a path.

Suppose $\Lambda_f(a, b) < \infty$, $f$ is called a **rectifiable path** on $[a, b]$.

$f[a, b]$ is called a **rectifiable graph / curve**. Otherwise, $f$ is called **noncertifiable** on $[a, b]$.

(**Rectifiability and bounded variation**)

Suppose $f:[a, b] \to \R^n$ is a path.

$f$ is rectifiable on $[a, b]$ iff $\c{f_1, \ldots, f_n}$ are of bounded variation on $[a, b]$.

- Just notice that $V_{f_k}(a, b) \le \Lambda_f(a, b) \le \sum_{i=1}^n V_{f_i}(a, b)$.

(**Change of variable**)

Suppose $f: [a, b] \to \R^n$ is a rectifiable path on $[a, b]$.

Suppose $u: [c, d] \to [a, b]$ is **continuous and strictly monotonic**.

Consider path $g = f \circ u: [c, d] \to \R^n$. $g$ and $f$ are said to be **equivalent**.

  - Clearly $g[c, d] = f[a, b]$.

Suppose $f:[a, b] \to \R^{n}$ and $g: [c, d]\to \R^n$ be two paths in $\R^n$. $f$ and $g$ are injections, and $f[a, b] = g[c, d]$. Then $f, g$ are **equivalent**.

  - $f, g$ are continuous functions on compact sets. So they are homeomorphisms.
  - Consider $u: [a, b] \to [c, d]$ defined by $u = g^{-1} \circ f$. $u$ is continuous and bijective.
  - Such $u$ must be strictly monotonous.
