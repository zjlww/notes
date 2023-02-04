#### Continuous Maps and Homeomorphism

(**Function limit**)

Suppose $(S, N_S)$ and $(T, N_T)$ are **topological spaces**. And $T$ is **Hausdorff**.

Suppose $A \subseteq S$. Suppose $f: A \to T$, $p \in A'$ in $S$, and $b \in T$.

It is said that the limit of $f$ as $x$ approaches $p$ is $b$, denoted as $\lim_{x \to p} f(x) = b$ if
$$
\forall B \in N_T(b), \exists U \in N_S(p): f[U - \c{p}] \subseteq B
$$
Suppose $S$ and $T$ are **metric spaces**. $\lim_{x \to p} f(x) = b$ if
$$
\forall \epsilon > 0, \exists \delta > 0: f[U_A(p, \delta)] \subseteq B_T(b, \epsilon)
$$
And equivalently in **metric spaces** $\lim_{x \to p} f(x) = b$ if
$$
\forall (x_n)_{n = 1}^\infty \in A \backslash \{p\}: \p{x_n \to p \implies f(x_n) \to b}
$$
(**Function continuity**)

Suppose $S, T$ are topological spaces.

Suppose $f: S \to T$. And $p \in S$.

Function $f$ is **continuous** at $p$ if
$$
\forall B \in N_T(f(p)), \exists U \in N_S(p): f[U] \subseteq B
$$

- Suppose $p \in S$ is isolated, that is $p \in S \backslash \overline S$. Then $f(x)$ is continuous at $p$.
  - There exists $U_0 \in N_S(p)$, where $U_0 = \c{p}$.
- Suppose $p \in S'$, and $T$ is Hausdorff. Then $\lim_{x \to p} f(x) = f(p)$ in $S$ iff $f(x)$ is continuous at $p$.
  - This immediately follows from the definition.


Suppose $S$ and $T$ are metric spaces. Function $f$ is continuous at $p$ if

$$
\forall \epsilon > 0, \exists \delta >0: f[B_S(p,\delta)] \subseteq B_T(f(p), \epsilon)
$$

Equivalently, $f$ is continuous at $p$ if
$$
\forall \p{x_n}_{n=1}^\infty \subseteq S: \p{x_n \to p \implies f(x_n) \to f(p)}
$$
(**Preimage and continuity**)

Suppose $S, T$ are topological spaces. Suppose $f: S \to T$. And $p \in S$.

The following are equivalent definitions of $f$ is **continuous on** $S$.

1. $f$ is continuous at every point in $S$.
2. For any open set $O$ in $T$, $f^{-1} [O]$ is open in $S$.
3. For any closed set $U$ in $T$, $f^{-1}[U]$ is closed in $S$.

Proof:

- $(1 \to 2)$. Suppose $f$ is continuous at every point in $S$.
  - Suppose $x \in f^{-1}[O]$ and $y = f(x) \in O$.
  - There exists open neighborhood $N_x \subseteq f^{-1}[O]$. Where $f[N_x] \subseteq O$.
  - $x \in N_x$, so $x \in f^{-1}[O]^\circ$. Therefore $f^{-1}[O]$ is open in $S$.
- $(2 \to 3)$. And similarly $(3 \to 2)$.
  - Suppose $U \subseteq T$ is closed.
  - Just notice that $\s{f^{-1}\s{U^c}}^c = f^{-1}\s{U}$.
  - Therefore $f^{-1}[U]$ is closed.
- $(2 \to 1)$.
  - Consider $x \in S$ and $y = f(x) \in T$.
  - Consider any open neighborhood $N_y$ of $y$ in $T$.
  - $f^{-1}\s{N_y}$ is open in $S$. $x \in f^{-1}[N_y]$.
  - There exists an open neighborhood $N_x$ of $x$ and $N_x \subseteq f^{-1}[N_y]$.

(**Composition of continuous functions**)

Suppose $S, T, U$ are topological spaces.

Suppose $f: S \to T$, $g: f[S]\to U$ and $h = g\circ f : S \to U$.

- Suppose $f$ is continuous at $p$ and $g$ is continuous at $f(p)$, then $h$ is continuous at $p$.
- Suppose $f$ is continuous on $S$ and $g$ is continuous on $f[S]$, then $h$ is continuous on $S$.

(**Homeomorphism**)

Suppose $X, Y$ are topological spaces.

A bijection $T: X \to Y$ where $T, T^{-1}$ are both continuous, is a **homeomorphism**.

- Also called a **topological isomorphism / embedding**.
- $X$ and $Y$ are called **homeomorphic**.
- Homeomorphism forms an equivalence relation on the *class* of all topological spaces.
- The equivalence classes are called **homeomorphism classes**.
- Properties of topological spaces that are **invariant under homeomorphism** are called **topological invariants**.

(**Isometry**)

Suppose $S, T$ are metric spaces. Consider $f: S \to T$.

Suppose $\forall x, y \in S: d_{T}(f(x), f(y))=d_{S}(x, y)$, $f$ is called an **isometry**.

- $S$ and $T$ are called **isometric**.
- $f: S \to f[S]$ is a homeomorphism.
  - $f$ is injective and the inverse $f^{-1}$ exists.
  - $f^{-1}: f[S] \to S$ is also an isometry.
  - $f$ and $f^{-1}$ are both continuous on their domains.
- An **isometric isomorphism** is a **bijective isometry**.

(**Continuous maps on compact sets**)

Let $S, T$ be topological. Suppose $f: S \to T$.

Suppose $f$ is continuous on $S$, and $S$ is compact.

**Then $f[S]$ is compact.**

- Suppose $\p{G_\alpha}_{\alpha \in I}$ is an open cover of $f[S]$.
- Define $H_\alpha = f^{-1}[G_\alpha]$, $H_\alpha$ is open.
- $\p{H_\alpha}_{\alpha \in I}$ is an open cover of $S$.
- Since $S$ is compact. There is a finite open subcover. $\p{H_\alpha}_{\alpha \in J}$.
- Consider $\p{G_{\alpha}}_{\alpha \in J}$, this is an finite open subcover of $f[S]$.

**Further suppose $f$ is injective, then $f^{-1}: f[S] \to S$ is continuous on $f[S]$.**

- We only need to show that $f$ maps closed sets to closed sets.
  - Suppose $U \subseteq S$ is closed, then $U$ is compact.
  - Therefore $f[U]$ is compact.
  - Since $f[U] \subseteq f[S]$ and $f[S]$ is compact, $f[U]$ is closed.
- Therefore $f$ is a homeomorphism. $S$ and $f[S]$ are homeomorphic.

#### Uniform Continuity

(**Uniformly continuity**)

Suppose $S$ and $T$ are metric spaces. Suppose $f: S \to T$.

$f$ is **uniformly continuous** on $S$ if
$$
\forall \epsilon > 0, \exists \delta > 0, \forall p \in S: f[B_S(p,\delta)]\subseteq B_T(f(p),\epsilon)
$$

- Uniform continuity clearly implies continuity.
- Denote the set of uniformly continuous functions on $S$ as $UC\p{S \to T}$.

(**Heine-Cantor Theorem**)

Suppose $S$ and $T$ are metric spaces. Suppose $f: S \to T$ is continuous.

Suppose $S$ is compact. Then $f$ is uniformly continuous on $S$.

> The following brief proof is based on this [wiki page](https://en.wikipedia.org/wiki/Heine%E2%80%93Cantor_theorem).

- Consider any given $\epsilon > 0$.
- Define $\delta_x: S \to (0, \infty)$ where $f\s{B_S(x, \delta_x)} \subseteq B_T(f(x), \epsilon /2)$.
- Consider open cover $O:= \c{B_S(x, \delta_x): x \in S}$.
- There exists an open subcover $O' = \c{B_S(x_i, \delta_{x_i})}_{i=1}^n$.
- Take $\delta = \min_{i} \delta_{x_i} / 2$.
- Now for any $a, b \in S$ where $d(a, b) < \delta$. $a, b \in B_S(x_j, \delta_{x_j})$ for some $1 \le j \le n$.
- Therefore $d(f(a), f(x_j)) < \epsilon / 2$ and $d(f(b), f(x_j)) < \epsilon / 2$.
- Therefore $d(f(a), f(b)) < \epsilon$ by triangle inequality of metric.

#### Lipschitz Continuity

(**Lipschitz continuity**)

Suppose $(S, d_S)$ and $(T, d_T)$ are metric spaces.

$f: S \to T$ is called Lipschitz continuous if there exists a real constant $K \ge 0$ such that
$$
\forall x, y \in S: d_T(f(x), f(y)) \le K d_S(x, y)
$$

- $K$ is called a Lipschitz constant of $f$. And $f$ is called $K$-Lipschitz.
- Lipschitz continuouity implies uniform continuity.
- Denote the set of Lipschitz continuous functions as $LC\p{S \to T}$.

(**Contraction and fixed points**)

Suppose $S$ is a metric space.

$f: S \to S$ is called a **contraction** if $f$ is $K$-Lipschitz where $K \in [0, 1)$.

- $K$ is called a contraction constant.

$p \in S$ is called a **fixed point** of $f: S\to S$ if $f(p) = p$.

(**Lipschitz fixed-point theorem**)

Suppose $S$ is a **complete metric space** and $f$ is a **contraction** with constant $K \in [0, 1)$.

Then $f$ has a unique fixed point $p \in S$.

- The fixed point is unique.

  - Suppose $p, q \in S$ are both fixed points.
  - Then $d(f(p), f(q)) = d(p, q) \le Kd(p, q)$.
  - Therefore $d(p, q) = 0$ and $p = q$.

- There exists one fixed point.

  - For any $p_0 \in S$, consider $p_n = f^n(p_0)$.
  - $d(p_n, p_{n+1}) \le Kd(p_{n-1},p_n) \le K^n \n{p_0}$.
  - Clearly $(p_n) \in S$ is Cauchy and converges to $p \in S$.
  - $f(p) = f(\lim_{n} p_n) = \lim_n f(p_n) =p$.

- We have an estimate of the norm of the fixed point $p \in S$.
  $$
  \n{p} = \norm{\sum_{i=0}^\infty p_{i+1}-p_i} \le \sum_{i=0}^\infty K^i\n{f(0) - 0} \le 1/(1-K)\n{f(0)}
  $$

(**Weissinger fixed-point theorem**)

Suppose $S$ is a **complete metric space**.

Suppose sequence $\p{\theta_n}_{n=1}^\infty \subseteq (0, \infty)$ with $\sum_{n =1}^\infty \theta_n < \infty$.

And operator $f: S \to S$ satisfies
$$
\forall x, y \in C: \forall n: d\p{f^n(x), f^n(y)} \le \theta_n d(x, y)
$$
Then $f$ has a unique fixed point $p \in S$.

- Since $\theta_n \downarrow 0$. For $N$ large enough, $f^N: S \to S$ is a contraction.

- Suppose $p, q \in S$ are both fixed points. Then $p = q$.

  - $d(f^N(p), f^N(q)) \le \theta_N d(p, q)$.

- For any $p_0 \in S$, consider $\p{p_n}_{n=1}^\infty := \p{f^n(p_0)}_{n=1}^\infty$.

  - $d(p_n, p_{n + 1}) \le \theta_k d(p_{ n-k}, p_{n - k + 1})$.
  - Clearly $(p_n) \in S$ is Cauchy and converges to some $p \in S$.

- Consider the sequence $a_n = f^n(p)$.

  - $f^N(p) = f^N(\lim_{n} p_n) = \lim_n f^N(p_n) =p$.
  - But notice that we can pick any $N$ large enough.
  - We can pick co-prime $N, M$, so the sequence has period $1$.
  - That is $f(p) = p$.

- Suppose $p$ is the fixed point. We have following bound
  $$
  \n{f^n(x) - x} \le \p{\sum_{j = n}^\infty \theta_j} \n{f(x) - x}
  $$
