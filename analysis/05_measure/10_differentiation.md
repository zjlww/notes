#### Generalized Differentiation Theory

(**Continuity of measure**)

Suppose $(\Omega, \F)$ is a measurable space and $\mu, \lambda$ are signed measures on $\F$.

- $\lambda$ is **absolutely continuous** with respect to $\mu$ if
  $$
  \forall A \in \F: \mu(A) = 0 \to \lambda(A) = 0
  $$

  - Denoted by $\lambda \ll \mu$.

- $\lambda$ is **uniformly continuous** with respect to $\mu$ if
  $$
  \forall \epsilon > 0, \exists \delta > 0, \forall A \in \F: |\mu|(A) < \delta \to |\lambda|(A) < \epsilon
  $$

  - Denoted by $\lambda \lll \mu$.

- $\lambda$ is **Lipschitz continuous** with respect to $\mu$ if
  $$
  \exists K \ge 0: \forall \epsilon > 0, \forall A \in \F: |\mu|(A) \le \epsilon \to |\lambda|(A) \le K\epsilon
  $$

  - Denoted by $\lambda \lll_K \mu$.

(**Various continuity of measure**)

Suppose $(\Omega, \F, \mu)$ is a measure space and $\lambda$ is a signed measure on $\F$.

- When $\lambda$ is finite. $\lambda \ll \mu$ implies $\forall (A_n)_{n = 1}^\infty \in \F: (\mu A_n \to 0 \implies |\lambda| A_n \to 0)$.
  - Otherwise, suppose $(A_n)_{n = 1}^\infty \in \F$ where $\mu A_n < 2^{-n}$ and $|\lambda| A_n > \epsilon$.
  - $\mu A^* = 0$ by (**Cantelli**).
  - $|\lambda|A^* = |\lambda|(\cap_{n = 1}^\infty \cup_{k = n}^\infty A_k) = \lim_n |\lambda|(\cup_{k = n}^\infty A_k)$. (Requires finite $|\lambda|\cup_{n = 1}^\infty A_n$)
  - $|\lambda|(\cup_{k = n}^\infty A_k) \ge |\lambda|(A_n) > \epsilon$. So $|\lambda| A^* \ge \epsilon$.
- $\lambda \ll \mu$ implies $\forall (A_n)_{n = 1}^\infty \in \F: (\mu A_n \to 0\land |\lambda|(\cup_n A_n) < \infty \implies |\lambda|A_n \to 0)$.
  - Similar to the first result.
- When $\lambda$ is finite. $\lambda \ll \mu$ implies $\lambda \lll \mu$.
  - Otherwise we can construct $(A_n)_{n = 1}^\infty \in \F$ that contradicts previous one.
- $\lambda \lll_K \mu \implies \lambda \lll \mu \implies \lambda \ll \mu$.

(**Absolutely continuous**)

$f: [a, b] \to \R$ is **absolutely continuous** on $[a, b]$ if
$$
\forall \epsilon > 0, \exists \delta > 0, \forall A=+_{i = 1}^n(a_i, b_i)\subset [a, b]: m(A) \le \delta \to \sum_i |f(b_i) - f(a_i)| \le \epsilon
$$
 Where $m$ is the Lebesgue measure on $[a, b]$.

- Change $n$ to infinity gives an equivalent definition.
- The definition can be generalized by changing $[a, b]$ to any subset $I$ of $\R$.
- The collection of absolutely continuous function on $I$ is denoted as $AC[I]$.

(**AC in function and measure**)

Suppose $\mu$ and $\nu$ are **finite** LS measures on $[a, b]$ induced by $F, G: [a, b] \to \R$.

Let $f = F - G$ and $\lambda = \mu - \nu$.

Then $\lambda \ll m \iff f \in AC[a, b]$. Where $m$ is Lebesgue measure.

- Suppose $\lambda \ll m$.
  - Since $\lambda$ is finite, $\lambda \lll m$. So when $m(\cup_n(a_i, b_i)) < \delta$.
  - $\sum_n |f(b_i) - f(a_i)| = \sum_n |\lambda(a_i, b_i]| \le \sum_n |\lambda|(a_i, b_i] \le |\lambda|(\cup_n(a_i, b_i)) \le \epsilon$.
- Conversely, suppose $f \in AC[a, b]$.
  - Suppose $A \in \B[a, b]$ and $m(A) = 0$.
  - By definition of Lebesgue outer measure. $\lambda(A) = 0$. So $\lambda \ll m$.
- The theorem may be extended to $\R$, given $F$ and $G$ are **bounded** and $\mu$ and $\nu$ are **finite**.

(**Total variation and absolute continuous**)

Suppose $f: [a, b] \to \R$.

- $f \in LC[a, b] \implies f \in AC[a, b] \implies f \in V[a, b]$.
  - Take $\epsilon > 0$ and $\delta > 0$ as given in AC.
  - For any $Q \in P[a, b]$ such that $\|Q\| \le \delta / 2$.
  - Define $(i_k)_{k = 1}^r$ such that $i_0 = 0$, $i_r = n$ and $x_{i_k} - x_{i_{k - 1}} \in [\delta / 2, \delta]$.
  - $r \in [(b - a)/\delta, 2(b - a) / \delta]$.
  - By AC, $\Sigma(Q, f) \le r \epsilon \le 2(b - a)\epsilon/\delta$.
- If $f: [a, b] \to \R$ is monotone, $f$ is of bounded variation.
- If $f \in V[a, b]$ then $f = F - G$ where $F, G$ are increasing. If $f \in AC[a, b]$, then $F, G$ can be absolutely continuous as well.
  - Let $F(x) = V_f(a, x)$ when $x \in [a, b]$. $F \nearrow [a, b]$.
  - Let $G(x) = F(x) - f(x)$. $G \nearrow [a, b]$.
    - $G(t) - G(s) = F(t) - F(s) - (f(t) - f(s)) \ge V(s, t) - |f(t) - f(s)| \ge 0$.

  - Now assume $f \in AC[a, b]$. For $\epsilon > 0$, exists $\delta > 0$ as in definition of AC.
    - Then clearly $F \in AC[a, b]$. So $G \in AC[a, b]$.

(**Fundamental Theorem of Calculus IV**)

$f \in AC[a, b]$ if and only if $f(x) - f(a) = \int_a^x g(t) dt$ for some $g \in \L^1([a, b] \to \eR)$.

- $\leftarrow$ direction.
  - Define $\mu$ as $d\mu = g dm$. $f(x_1) - f(x_0) = \mu(x_0, x_1]$.
  - So $\mu$ has distribution function $f(x)$. Since $\mu \ll m$, $f \in AC[a, b]$.
- $\to$ direction. w.l.o.g. assume $f$ is increasing. 
  - Suppose $\mu$ is the LS measure defined by $f$ on $\B[a, b]$. Then $\mu \ll m$.
  - Notice that $\mu, m$ are both finite measures on $\B[a, b]$. So
  - By Radon-Nikodym theorem, for some $g \in \L^1([a, b] \to [0, \infty], \mu)$, $d \mu = g dm$.

Bounded $f \in AC[\R]$ **if and only if** $f(x) - f(a) = \int_a^x g(t) dt$ for some $g \in \L^1(\R \to \eR)$. The proof is similar.

(**Open cubes**)

Define $C(x; r)$ as the open cube centered at $x$ with radius $r$. Let $\mathcal C_d$ be the set of open cubes in $\R^d$.

(**Signed LS measure**)

Suppose $\mu$ is a signed measure on $\B(\R^d)$ where $\mu$ is finite on bounded sets.

Then $\mu$ is a **signed Lebesgue-Stieltjes measure**.

(**Differentiation of measure**)

Suppose $(\R^d, \B(\R^d), m)$ is the **Lebesgue measure** space.

Suppose $\mu$ is a **signed LS measure** on $\B(\R^d)$.

- Let $B_r(x) := \{\mu(E) / m(E): E = C(y;\rho), y \in \R^d, \rho < r, x \in E\} \subseteq \R$.
    - $B_r(x)$ shrinks as $r \downarrow 0$.
    - $\sup B_r(x) > a$ is an open set in $\R^d$. So $\sup B_r(x) \in \L(\R^d \to \eR)$.
        - Suppose $x$ is in the set.
        - Suppose $x \in E = C(y; \rho)$ and $\mu(E) / m(E) = a + \epsilon$.
        - $E \subseteq \sup B_r(x) > a$. So $x$ is an interior point.
- Define $(\overline D \mu)(x) \in \L(\R^d \to \eR)$ as $x \mapsto \inf_{r > 0}\sup B_r(x)$.
- Define $(\underline D \mu)(x)\in \L(\R^d \to \eR)$ as $x \mapsto \sup_{r> 0} \inf B_r(x)$.
- $\mu$ is **differentiable** at $x$ if and only if $\overline D \mu(x) = \underline D \mu(x) < \infty$. 
    - Denote the common value as $D\mu(x)$, the **derivative** of $\mu$ at $x$.
- $D\mu (x) =A$ **iff** $\forall x \in C_n = C(a_n, r_n)_{n = 1}^\infty: (r_n\downarrow 0 \implies \mu(C_n)/m(C_n) \to A)$.

(**Vitali**)

Suppose $(\R^d, \B(\R^d), m)$ is the **Lebesgue measure** space. Suppose $\mathcal A = (C_n)_{n = 1}^N$ are open cubes. (Balls also works.)

- Suppose $(C_n)$ has increasing diameter. Start with empty list $\mathcal B$. Add $C_1$ in $\mathcal B$.
- For $i = 1 \to n$, add $C_i$ not intersecting with $\cup \mathcal B$ to $\mathcal B$.
- Let $3\mathcal B$ be the list with open cubes in $\mathcal B$ but $3$ times the raidus. $\cup \mathcal A \subseteq \cup 3 \mathcal B$.
- So $m(\cup \mathcal A) \le 3^d \sum_{B \in \mathcal B}m(B)$.

(**Lebesgue differentiation**)

Suppose $(\R^d, \B(\R^d), m)$ is the **Lebesgue measure** space.

Suppose $\mu$ and $\nu$ are **signed LS measures** on $\B(\R^d)$. Suppose $D\mu(x)$ and $D\nu(x)$ exists at $x \in \R^d$.

- Then $D(\mu + \nu)(x) = D\mu(x) + D\nu(x)$.
- And $D(c \mu)(x) = c (D\mu)(x)$ for $c \in \R$.

Suppose $\mu$ is a **LS measure** on $\B(\R^d)$. Let $A \in \B(\R^d)$ and $\mu(A) = 0$. Then $D\mu = 0$ on $A$ $m$-a.e.

- $D\mu = 0$ on $A$ $m$-a.e **only if** $\overline D\mu = 0$ on $A$ $m$-a.e.
- **Only if** $B = \{x \in A: (\overline D \mu)(x) > 0\}$ is a $m$-null set.
- **Only if** $B_a = \{x \in A: (\overline D\mu)(x) > a\}$ is a $m$-null set for any $a > 0$.
- **Only if** any **compact subset** $K \subseteq B_a$ is a $m$-null set. By (**inner regularity**).
    - For any $r > 0$, for all $x \in K$, some $C_x = C(y; \rho)$ contains $x$ where $\rho < r$ and $\mu(C) / m(C) > a$.
    - Then $K$ has open cover $(C_x)_{x \in K}$.
    - Then $K$ has finite open cover $(C_j)_{j = 1}^n$ where $(C_j) \subset (C_x)$.
    - By (**Vitali**) $(C_{k})_{k = 1}^r \subset(C_j)$ exists where $(3C_k)$ is a finite open cover of $K$.
    - $m(K) \le m(\cup_j C_j) \le 3^d \sum_km(C_k) \le 3^d/a \sum_k\mu(C_k) \le 3^d/ a \mu(K_r)$.
        - Where $K_r: = \{x \in \R^k: \operatorname{dist}(x, K) < r\}$ is an open set.
        - And $K = \cap_{n = 1}^\infty K_{1/n}$.
    - So $m(K) \le 3^d \mu(K) / a \le 3^d \mu(A) / a = 0$.

Suppose $\mu$ is a **signed LS measure** on $\B(\R^d)$ and $\mu \ll m$. By (**Radon-Nikodym**) there exists $\dd\mu/\dd m = g \in \overline \L(\R^d \to \eR)$ that is finite $m$-a.e. Then $D \mu = g$ $m$-a.e.

- Define $A = \{g < a\}$ for some $a \in R$. b 
- Define **LS measure** $d\lambda = 1_{A^c} (g - a) dm$ on $\B(\R^d)$, then $\lambda(A) = 0$.
- So $D\lambda = 0$ on $A$ $m$-a.e.
- So $\overline D\lambda(x) = \inf_{r > 0} \sup B_r(x) = 0$ for $m$-almost all $x \in A$.
- So for $m$-almost all $x \in A$, for any $\epsilon > 0$, exists $r > 0$, for any $C = C(y; \rho) \ni x$ where $\rho < r$. $\lambda(C)/m(C) \le \epsilon$. $\mu_c(C)/m(C) \le a + \epsilon$.
- So $\overline D\mu \le a$ for $m$-almost all $x \in A$.
- So $\overline D \mu \le g$ $m$-a.e. on $\R^d$. By symmetry $\underline D \mu \ge g$ $m$-a.e. on $\R^d$.
- So $D \mu = g$ $m$-a.e. on $\R^d$.

Suppose $\mu$ is a **signed LS measure** on $\B(\R^d)$ and $\mu \perp m$.

- Suppose $|\mu|(A) = 0$ and $m(A^c) = 0$ for some $A \in \B(\R^d)$.
- Then $\mu^+(A) = \mu^-(A) = 0$.
- So $D \mu^+ = 0 = D\mu^-$ $m$-a.e. So $D \mu = 0$ $m$-a.e.

For any **signed LS measure** $\mu$ on $\B(\R^d)$.

- By Lebesgue decomposition, a unique decomposition exists $\mu = \mu_c + \mu_s$ where $\mu_c \ll m$ and $\mu_s \perp m$. Where $\mu_c$ and $\mu_s$ are both signed LS measures. Then $D\mu = D\mu_c = \dd\mu_c/\dd m$ where equalities are $m$-a.e.

(**Monotone decomposition**)

Suppose $F: \R \to \R$ is **increasing and bounded**.

- Left and right limit always exists. $F(x-) \le F(x) \le F(x+)$.
- Define $c_x = F(x +) - F(x-)$. Define $D = \{x \in \R: c_x > 0\}$.
- $\forall x \in D, \exists q \in \Q:F(x-) < q < F(x+)$. So $|D| \le |\N|$.
- $\forall t \in D: J_t(x) := 1_{x \ge t} (F(x) - F(x-)) + 1_{x > t}(F(x+) - F(x))$. ($J_t$ is shifted unit step.)
- Define $F_{pp}(x) = \sum_{t \in D} c_t J_t(x)$. Since $\sum_{t \in D} c_t < \infty$, $F_{pp}(+\infty) < +\infty$.
- Define $F_c(x) = F(x) - F_{pp}(x)$. $F_c$ is clearly continuous.
- $F_c$ is still increasing.
  - We hope $F(b-) - F(a+) \ge F_{pp}(b-) - F_{pp}(a+)$.
  - $m(F(a+), F(b-)] = F(b-) - F(a+)$.
  - $F_{pp}(b-) - F_{pp}(a+) \le m(\cup_{t \in D \cap (a, b)}(F(t-), F(t+)]) \le m(F(a+), F(b-)]$.

The decomposition $F = F_c + F_{pp}$ is unique up to constants. $F_c$ is the **continuous component**, and $F_{pp}$ is the **jump component**.

- Suppose $F' = F_c' + F'_{pp}$ where $F_{pp} \neq F_{pp}'$. Since $F_{pp} = F - F_c$ and $F_{pp}' = F - F'_c$.
- So $F_{pp} - F'_{pp} = F_c - F'_c$ is continuous. So the decomposition is unique up to a constant.

Suppose $F: [0, \infty) \to \R$ is **increasing and sparsely piecewise continuous**. Then the decomposition $F = F_c + F_{pp}$ exists and is unique up to constants.

(**Monotone differentiation**)

Suppose $f: \R \to \R$ is bounded and increasing. Then $f$ is left / right differentiatble $m$-almost everywhere. We prove right differentiability only:

- Suppose $D$ contains all countably many discontinuity points of $f$.
- Alter $f$ at $t \in D$ to $f(t) = f(t-)$ making $f(t)$ **left-continuous**. This does not alter derivatives on $D^c$.
- Consider the unsigned LS measure $\mu$ on $\B(\R)$ defined by $\mu[s, t) = f(t) - f(s)$.
- $D\mu$ exists $m$-a.e. Consider $x \in \R$ where $D\mu(x)$ exists.
- We claim $f_+'(x) = D\mu(x) = c$.
  - $f$ must be continuous at $x$ by definition of $D\mu$.
  - Fix $\epsilon > 0$, there exists $r > 0$ where $B_r(x) \subset B(c, \epsilon / 2)$.
  - For some $0 < h < r / 2$, $|(f(x + h) - f(x))/h - c| \ge \epsilon$.
  - That is $|\mu[x, x + h)/m[x, x + h) - c| \ge \epsilon$.
  - We can find $r/2>g > 0$ where $\mu(x - g, x + h)$ is very close to $\mu[x, x + h)$.
  - So $|\mu(x - g, x + h)/m(x - g, x + h) - c| \ge \epsilon / 2$. Contradiction!
  - So $f'_+(x) = D\mu(x) = c$.
- Similarly $f_-'(x) = D\mu(x) = c$.
- So $f' = D\mu$ $m$-a.e.

The theorem applies to functions with bounded variations.

(**FTC V**)

$f \in AC[a, b]$ then $f$ is differentiable $m$-almost everywhere. $f' \in \L^1([a, b] \to \eR)$ and $f(x) - f(a) = \int_a^x f'(t) dt$.

- w.l.o.g. suppose $f$ is bounded increasing.
- By (**FTC IV**) some $g \in \L^1([a, b] \to [0, \infty])$ where $f(x) - f(a) = \int_a^x g(t) dt$.
- Define $d\mu = g dm$ then $\mu$ is a LS measure on $\B[a, b]$.
- $\mu(a, x] = \int_a^x g(t) dt = f(x) - f(a)$.
- So $f' = D\mu = g$ where all equalities are $m$-a.e.

