#### Derivative

**(Landau notation**)

Suppose $(a_n)_{n = 1}^\infty, (c_n)_{n = 1}^\infty \in \C$ and $(b_n)_{n = 1}^\infty \in (0, \infty)$.

- $a_n = O(b_n) \iff \exists M > 0, \forall n \ge 1: |a_n| \le M b_n$.
- $a_n = o(b_n) \iff \lim_{n \to \infty} a_n / b_n = 0$.
- $a_n = c_n + O(b_n) \iff a_n - c_n = O(b_n)$.
- $a_n = c_n + o(b_n) \iff a_n - c_n = o(b_n)$.

Suppose $S$ is some topological space. Suppose $a(x): S \to \C$ and $b(x): S \to (0, \infty)$.

- $a(x) = o(b(x))$ as $x \to a$ iff $\lim_{x \to a} a(x) / b(x) = 0$.

##### Derivative

Consider $f: [a, b] \to \R$. Define $f^*: [a, b] \to \R$ for $c \in [a, b]$ as 
$$
f^*(x) := \frac{f(x) - f(c)}{x - c}
$$

- $f^*$ has a **removable discontinuity** at $c$.

When $f'(c): = \lim_{x \to c} f^*(x)$ exists in $\R$. $f$ is called **differentiable** at $c$. And $f'(c)$ is the **derivative** of $f$ at $c$.

- $f$ is continuous at $c$ if $f$ is differentiable at $c$.
- $f': F \to \R$ is called the derivative of $f$ where $f'(x)$ exists.
- The **$n$-th derivative** of $f$, denoted by $f^{(n)}$, is the derivative of $f^{(n-1)}$.

We extend the definition of $f'(c)$ when $f$ is continuous at $c$ and $\lim_{x \to c} f^* (x)$ exists in $\eR$.

For $c = a$, $f'(c)$ is called the **right-derivative**, and also denoted as $f'_{+}(c)$. $f(x)$ is called right-differentiable if $f'_+(c)$ is defined.

##### Derivative chain rule

Consider the following situation:

- Suppose $f: S \to \R$ is differentiable at $c \in S^\circ$.
- Suppose $g: T \to \R$ is differentiable at $f(c) \in T^\circ$.
- Suppose $h = g \circ f: S \to \R$.

Then $h$ is differentiable at $c$ and $h'(c) = g'(f(c))f'(c)$.

- $f(x) = f(c) + f'(c)(x - c) + R_0(x-c)$ for $x \in B(c, \delta_0)$.
- $g(y) = g(f(c)) + g'(f(c)) (y - f(c)) + R_1(y - f(c))$ for $y \in B(f(c), \delta_1)$.
- w.l.o.g. take $\delta_0$ small enough where $f[B(c, \delta_0)] \subseteq B(f(c), \delta_1)$.
- $h(x) = g(f(c)) + g'(f(c))f'(c) (x - c) + g'(f(c)) R_0(x - c) + R_2(x - c)$.
  - Where $R_2(x - c) := R_1(f'(c) (x - c) + R_0(x - c))$.
- For $x \in B(c, \delta_2)$ with $\delta_2$ small enough, we have $\lim_{x \to c}\frac{R_2(x - c)}{x - c} = 0$.
  - Just notice that for $\delta_2$ small enough $f'(c) (x - c) + R_0(x - c)$ is bounded by $K\abs{x - c}$.

##### Derivative Arithmetic

For $f, g: S \to \R$ differentiable at $c \in S^\circ$, rules for $(f + g)', (fg)', (f/g)'$ in Calculus are true.

> See any Calculus book for the derivations of these rules.

##### Sets of Differentiable Functions

For $f:S \subseteq \R \to \R$.

- $f \in C^k[S]$ means $f^{(k)}$ exists and is continuous on $S$.
- $f \in C^\infty[S]$ means $f$ is infinitely differentiable on $S$.
- $f \in D[S]$ means $f$ is differentiable on $S$.
- $f \in D'[S]$ means $f'(x) \in \eR$ is defined on $S$.

##### Extrema of real functions

For $f:S \subseteq \R \to \R$.

- Minima and maxima of $f$ are **extrema**.
- $f$ have a **local maximum** at **local maximum point** $a$ if for all points in $B_S(a, \delta)$, $f(x) \le f(a)$.
- $f$ have a **global maximum** at **global maximum point** $a$ if $\forall x \in S: f(x) \le f(a)$.

#### Mean Value Theorems

##### Rolle

Suppose $f: [a, b] \to \R$. Suppose $f \in C[a, b]$ and $f \in D'(a, b)$, and $f(a) = f(b)$.

There is some $c \in (a, b)$ such that $f'(c) = 0$.

- w.l.o.g. suppose $f(a) = f(b) = 0$, and $\sup f(x) > 0$.
- Suppose for $x \in (a, b)$, $f(x) = \max f[a, b]$.
  - Since $f[a, b]$ is compact.
- $f_+'(x) \le 0$ and $f'_-(x) \ge 0$. So $f'(x) = 0$.

##### Mean Value Theorem

Suppose $f: [a, b] \to \R$. Suppose $f \in C[a, b]$ and $f \in D'(a, b)$.

Then there is some $c \in (a, b)$ such that $f(b)  - f(a) = f'(c) (a - b)$.

- Take $g(x) = f(x) - (x-a)(f(b) - f(a))/(b -a)$ then apply (**Rolle**).

Immediately results from MVT I:

- If $\forall x \in (a, b): f'(x) \gt 0$, $f$ is strictly increasing on $[a, b]$.
- If $\forall x \in (a, b): f'(x) = 0$, $f$ is constant on $[a, b]$.
- Suppose $f, g \in D'(a, b)$ and $f, g \in C[a, b]$. If $f' - g' = 0$ on $(a, b)$ then $f - g = 0$ on $[a, b]$.

##### Cauchy Mean Value Theorem

Suppose $f, g: [a, b] \to \R$.

Suppose $f, g \in C[a, b]$ and $f, g \in D'(a, b)$, and $f'(x)$ and $g'(x)$ are not simultaneously infinite.

For some $c \in (a, b)$, $f^{\prime}(c)[g(b)-g(a)]=g^{\prime}(c)[f(b)-f(a)]$.

- Define $h(x) = f(x)[g(b) - g(a)] - g(x)[f(b) - f(a)]$.
- Notice that $h(a) = h(b) = f(a) g(b) - f(b) g(a)$.
- $h \in C[a, b]$ and $h \in D'(a, b)$.
- The result follows from Rolle.

#### Intermediate Value Theorem of Derivative

##### Intermediate Value Theorem of Derivative

Consider $f: (a, b) \to \R$. Suppose $f \in C(a, b)$ and $f \in D'(a, b)$.

**$f'(a, b)$ obtains all intermediate values.**

- Define the triangle region $S := \c{a < x < y < b: x, y \in \R}$ where $S \subseteq \R^2$.
  - Clearly $S$ is open and connected.
  
- Consider function $g(x, y): S \to \R$. Defined as
  $$
  g(x, y) := \frac{f(y) - f(x)}{y - x}
  $$

  - $g$ is continuous on $S$.
  - Since $S$ is connected, $g[S]$ obtains all intermediate values.
  - According to intermediate value theorem, $g[S] \subseteq f'(a, b)$.
  
- Notice that $f'(a, b) = \overline{g[S]}$.

  - Even though $g[S] \neq f'(a, b)$ in general. $g[S]$ is clearly dense in $f'(a, b)$.

- So $f'(a, b)$ obtains all intermediate values.

##### Discontinuities of derivative

Consider $f: (a, b) \to \R$. Suppose $f \in D'(a, b)$.

$f'$ does not have jump or removable discontinuities.

##### Monotonicity and derivative

For $f: (a, b) \to \R$. Suppose $f \in D'(a, b)$.

Suppose $0 \notin f'(a, b)$ then $f$ is strictly monotonic on $[a, b]$.

- Either $f'(a, b) \subseteq (0, \infty]$ or $f'(a, b) \subseteq [-\infty, 0)$.

Suppose $f'$ is monotonic on $(a, b)$, $f' \in C(a, b)$.

- Since $f'$ is monotonic, there can only be jump and removable discontinuities.

#### Convexity

##### Convex real functions

Suppose $g: I \to \R$ where $I$ is an open interval in $\R$. $g$ is called **convex** if
$$
\forall x, y \in I, \forall a \in [0, 1]: g(ax + (1 - a)y) \le ag(x) + (1 - a)g(y)
$$

- Intuitively, the function is always **below** any line segment.

Suppose $g(x)$ is convex the following are rather apparent:

- $g_+'$ exists on $I$.
  - $\forall 0 < a < b: [g(x+a)-g(x)]/a \leq [g(x+b)-g(x)]/b$.
- $g'_-$ exists on $I$.
  - $\forall 0 < a < b: [g(x) - g(x-b)]/b \geq [g(x) - g(x-a)]/a$.
- $g(x)$ is continuous on $I$. Since $g'_+$ and $g'_-$ exists on $I$.
- $\forall x \in I: g'_-(x) \le g'_+(x)$.
  - For $a > 0$ and $b > 0$, $[g(x) - g(x - a)]/a \le [g(x + b) - g(x)]/b$.
- $g'_+, g'_-$ are increasing on $I$.
  - $g_+'(x_1) \le [g(x_2) - g(x_1)]/(x_2 - x_1) \le g_-'(x_2) \le g_+'(x_2)$.
- For any $c \in I$ there exists a linear $L_c(x): I \to \R$ where $\forall x \in I: L_c(x) \le g(x)$.
  - There exists some $g_-'(x) \le k \le g_+'(x)$.
  - Clearly $\forall x\in I: g(x) \ge g(c) + k(x - c)$.
- Such a function $L_c(x)$ is called a **line of support** for $g$ at $c$.
  - $g(x) = \sup_{c \in I \cap \Q}L_c(x)$.

#### Taylor's Theorem

##### Taylor polynomial

Consider $f: [a, b] \to \R$. Suppose $f \in D^{n}[a, b]$. Where $n \in \N$.

Define **n-th order Taylor polynomial** $P_n(x): [a, b] \to \R$:
$$
P_n(x) := \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x - a)^k = f(a) + f'(a)(x - a) + \frac{f''(a)}{2} (x - a)^2 + \cdots
$$
The **n-th order Taylor remainder** is $R_n(x) := f(x) - P_n(x)$.

##### Lagrange remainder

Consider $f: [a, b] \to \R$. Suppose $f \in D^{n}[a, b]$, and $f \in D^{n+1}(a, b)$.
$$
\forall x \in (a, b],\exist \xi_x \in (a, x): R_n(x) = \frac{f^{(n+1)}(\xi_x)}{(n+1)!}(x - a)^{n+1}
$$

- Define $F(x) := R_n(x) = f(x) - P_n(x)$. And $G(x):= (x - a)^{n + 1}$.

  - $F(a) = F'(a) = \cdots = F^{(n)}(a) = 0$.
  - $G(a) = G'(a) = \cdots = G^{(n)} = 0$.
  - $F^{(n+1)}(x) = f^{(n+1)}(x)$ for $x \in (a, b)$.
  - $G^{(n+1)}(x) = (n+1)!$

- By Cauchy's MVT, we have (division should be expanded to products):
  $$
  \frac{F(x)}{G(x)} = \frac{F'(c_1)}{G'(c_1)} = \cdots = \frac{F^{(n+1)}(c_{n+1})}{G^{(n+1)}(c_{n+1})}; \quad a < c_{n+1} < \cdots < c_1 < x
  $$

