#### The Extended Real

(**The extended real**)

The **extended real number system** $\eR = \R \cup \{+\infty, -\infty\} = [-\infty, \infty]$ has the following properties:

- $\eR$ is homeomorphic to the compact interval $[-1,1]$. Consider the $\tanh(x): \eR \to [-1, 1]$ map.
- It is not a metric space. And there is no metric that is an extension of the ordinary metric on $\mathbb{R}$.
- Intervals of the form $(a, \infty]$ or $[-\infty, a)$are open. Open sets in $\R$ are open sets in $\eR$.
- (**Totally ordered**) The ordering on $\eR$ is extended from $\R$ by $\forall x \in \R:-\infty < x < \infty$.
- Every $A \subseteq \eR$ has a least upper bound, or **supremum**, and a greatest lower bound, or **infimum**, which are denoted by $\sup A$ and $\inf A$.

(**Extended arithmetic on $\eR$**)

- Addition rules, $\infty - \infty$ is undefined.
  $$
  x \pm \infty=\pm \infty(x \in \mathbb{R}), \quad \infty+\infty=\infty, \quad-\infty-\infty=-\infty
  $$

- Multiplication rules:
  $$
  x \cdot(\pm \infty)=\pm \infty(x>0), \quad x \cdot(\pm \infty)=\mp \infty(x<0)
  $$

- We adopt the convention that $0 \cdot(\pm \infty)=0$ unless otherwise stated.

- Think before you apply the usual arithmetic rules in $\R$!

(**Improper sequence limits**)

We additionally have **improper** sequence limits in $\R$.

Consider $\p{x_n} \subseteq \R$.

- $\p{x_n}$ diverge to $+\infty$ if $\forall M \in \R, \exists N \in \Z, \forall n \ge N: x_n >M$.
- Divergence to $-\infty$ is similarly defined.



#### Upper and Lower Limits in $\eR$

(**Upper and lower sequence limits in $\eR$**)

Consider sequences $(a_n)_{n  =1}^\infty, (b_n)_{n = 1}^\infty \in \eR$.

- The **upper limit** of $a_n$ is $U := \limsup_{n \to \infty} a_n = \inf_{n \ge 1}\sup_{k \ge n} a_k$.
- The **lower limit** of $a_n$ is $L := \liminf_{n \to \infty} a_n = \sup_{n \ge 1}\inf_{k \ge n} a_k$.

We have properties:

- $L \le U$.
- A sequence is said to **oscillate** if $L < U$.
- $a_n$ converges to $p \in \R$ if and only if the upper and lower limits are **finite and equal**. $L = U = p$.
- $a_n \to \infty$ if and only $L = U = \infty$.
- $a_n \to - \infty$ if and only if $L = U = -\infty$.
- $\forall n \in \N: a_n \le b_n$  then
  - $\liminf _{n \rightarrow \infty} a_{n} \leq \liminf _{n \rightarrow \infty} b_{n}$;
  - $\limsup _{n \rightarrow \infty} a_{n} \leq \lim _{n \rightarrow \infty} \sup b_{n}$.


(**Upper and lower function limits**)

Suppose $(S, N)$ is a **topological space** with neighborhood topology $N$.

Suppose $f: S \to \eR$. And $a \in S$.

- The **upper limit** is $\limsup_{x \to a} f(x) = \inf\{\sup\{f(x): x \in U \backslash\{a\}\}:U \in N(a)\}$.
- The **lower limit** is $\liminf_{x \to a} f(x) = \sup\{\inf\{f(x): x \in U \backslash\{a\}\}:U \in N(a)\}$.

Suppose $S$ is a **metric space**. Then

- The **upper limit** is $\limsup_{x \to a} f(x) = \inf_{\epsilon > 0}\sup\{ f(x): x \in U(a, \epsilon)\}$.
- The **lower limit** is $\liminf_{x \to a} f(x) = \sup_{\epsilon> 0} \inf\{ f(x): x \in U(a, \epsilon)\}$.

(**Semi-continuity**)

Suppose $S$ is a **topological space**.

Suppose $f: S \to \eR$ and $a \in S$.

$f$ is **upper semicontinuous** at $a$ if any of the following equivalent conditions is true:
- $\forall y > f(a), \exists U \in N(a), \forall x \in U:f(x) < y$.
- $\limsup_{x \to a} f(x) \le f(a)$.

$f$ is **upper semicontinuous** on $S$ if any of the following equivalent conditions is true:
- $f$ is upper semicontinuous at every points in $S$.
- All superlevel sets $f^{-1}[y, +\infty]$ are closed in $S$. (Implies $f$ is Borel measurable.)

$f$ is **lower semicontinuous** at $a$ if any of the following equivalent conditions are true:
- $\forall y < f(a), \exists U \in N(a), \forall x \in U:f(x) > y$.
- $\liminf_{x \to a} f(x) \ge f(a)$.

$f$ is **lower semicontinuous** on $S$ if any of the following equivalent conditions is true:
- $f$ is lower semicontinuous at every points in $S$.
- All sublevel sets $f^{-1}[-\infty, y]$ are closed in $S$.

#### Continuous Real Valued Functions

(**Intermediate Value Theorem**)

Suppose $f: S \to \R$ where $S$ is a **connected topological space**. And $f$ is continuous on $S$.

Suppose $c \in S$ and $f(c) > 0$. Then $f[B_S(c, \delta)] \subseteq (0, \infty)$ for some $\delta > 0$.

- This immediately follows from the definition of continuity.

Suppose $a, b \in f[S]$ with $a < b$, then all of $[a, b] \subseteq f[S]$.

- Otherwise suppose $a < c < b$ and $c \notin f[S]$.
- Since $f^{-1}(c, \infty) \cup f^{-1}(-\infty, c) = S$, $S$ is not a connected subset. Contradiction!

Suppose $S$ is compact. Then $f[S] = [\min f[S], \max f[S]]$.

- $f[S]$ must be compact, therefore closed.
- There is only one connected component in $f[S]$. So $f[S]$ must be an interval.
- So $f[S]$ is an closed interval.

(**One-sided limits**)

Suppose $f: S \subseteq \R \to T$. Since $\R$ is linearly ordered, we additionally define:

- **One-sided limit**:

  - Suppose some $c$ is a **right-accumulation** point of $S$ in $\R$. We can define **right-limit**
    $$
    f(c+) =\lim_{x \downarrow c} f(x) = d \iff \forall \epsilon > 0, \exists \delta > 0: f[S \cap (c, c + \delta)] \subseteq B_{T}(d, \epsilon)
    $$

  - Suppose some $c$ is both left and right-accumulation point of $S$ in $\R$. And $c \in S$.
    - $f$ is continuous at $c \in S$ if, and only if $f(c)=f(c+)=f(c-)$.
    
  - Connection with **sequence limit**:
    
    - Suppose $T$ is a metric space. And $c$ is right-accumulation point of $S$ in $\R$.
    - $f(c+)=b$ if and only if for all $\{x_n\} \subseteq (c, \infty) \cap S$, $x_n \to c$ then $f(x_n)\to b$.

- **One-sided continuity**:

  - $f$ is right-continuous at $p \in S$ if
    $$
    \forall \epsilon > 0, \exists \delta > 0: f[S \cap [p, p + \delta)] \subseteq B_T(f(p), \epsilon)
    $$

    - Suppose $p \in S$ is a right-accumulation point of $S$.
      - $\lim_{x \to p^+} f(x) = f(p)$ if and only if $f(x)$ is right-continuous at $p$.
    - Suppose $p \in S$ is not a right-accumulation point.
      - Then $f(x)$ is always right-continuous at $p$ by definition.

(**Monotonicity**)

**Monotonicity** is defined for $f: S \subseteq \R \to \R$.

Without loss of generality, we only state theorems for increasing case.

- $f$ is called **monotonic** if $f$ is increasing or decreasing.
  - $f$ is **increasing** if $\forall x ,y \in S: x \lt y \to f(x) \le f(y)$.
  - $f$ is **strictly increasing** if $\forall x , y \in S: x \lt y \to f(x ) \lt f(y)$.
- If $f$ is strictly increasing, then $f^{-1}$ exists and is strictly increasing on $f[S]$.
- If $f$ is strictly increasing and continuous on $S = [a, b]$.
  - $f^{-1}$ is continuous and strictly increasing on $f[S]$.
  - $f$ is a homeomorphism.

#### Discontinuities

(**Classification of discontinuities**)

Suppose $f: S \subseteq \R \to T$. Consider point $c \in (a, b) \subseteq S$.

- $c$ is a discontinuity if:
  - (**Essential** discontinuity) $f(c+)$ or $f(c-)$ does not exist.
  - (**Jump** discontinuity) $f(c+)$ and $f(c-)$ exist but have different values.
  - (**Removable** discontinuity) $f(c+)$ and $f(c-)$ exist and $f(c+)=f(c-) \neq f(c)$.
  
- We have names for various jump values.

  > At the boundary points of closed intervals, identify $f(c+) = f(c)$.

  - $f(c)-f(c-)$ is called the lefthand jump of $f$ at $c$.
  - $f(c+)-f(c)$ is called the righthand jump of $f$ at $c$.
  - $f(c+)-f(c-)$ is called the jump of $f$ at $c$.

(**Counting discontinuities**)

Suppose $f: (a, b) \to \R$.

$f$ can have no more than countably many jump / removable discontinuities.

- Consider following definitions:

  - $M(x) := \max(|f(x) - f(x-)|, |f(x) - f(x+)|)$.

  - $J(\epsilon) := \{x \in (a, b): f(x-), f(x+) \text{ exists} \land M(x) > \epsilon\}$.

  - Define $D = \cup_{n} J(1/n)$. $D$ is the set of all jump and removable discontinuities.

- Now let's show that $J(1/n)$ are countable.

  - When $a = f(x-)$ exists, there exists $\delta > 0$ such that $f(x - \delta, x) \in B(a, \epsilon)$ for any $\epsilon > 0$.

  - Suppose $x \in J(1/n)$, $f(x - \delta, x) \in B(f(x-), 1/n)$.

  - Suppose $t \in (x - \delta, x)$, then $t \notin J(1/n)$. So $(x - \delta, x) \cap J(1/n) = \varnothing$.

  - There exists a surjection from $\Q$ to $J(1/n)$, so $J(1/n)$ is countable.

- Therefore $D = \cup_n J(1/n)$ is countable.

(**Increasing real functions**)

Suppose $f: [a, b] \to \R$ is **increasing** on $[a, b]$.

- One-sided limit exists at any $p \in [a, b]$. **All discontinuities in $[a, b]$ are jumps**.

  - Jump at $p \in (a, b)$ is defined as $\hat f(p) = f(p+) - f(p-)$.

- Clearly the sum of all jumps is bounded.

  

