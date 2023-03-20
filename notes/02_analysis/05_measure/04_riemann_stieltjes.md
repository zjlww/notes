#### Riemann-Stieltjes Integral

##### Riemann-Stieltjes integral

Suppose $f, \alpha: [a, b] \to \R$, are **bounded**.

Suppose $P = \{x_i\}^n_{i=0}$ is a partition of $[a, b]$.

Suppose $T = \{t_k\}_{k=1}^n$ and $t_k \in [x_{k-1}, x_k]$, $T$ is an interleaving set of $P$, denoted as $T \triangledown P$.

Define a **Riemann-Stieltjes sum** of $f$ with respect to $\alpha$ as
$$
S(P,T, f, \alpha)=\sum_{k=1}^{n} f\left(t_{k}\right) \Delta \alpha_{k} = \sum_{k=1}^n f(t_k) \p{\alpha_{k} - \alpha_{k-1}}
$$
Suppose the following is true:
$$
\exists A \in \R,\forall \epsilon > 0, \exists P_\epsilon \in P[a, b], \forall P\supset P_\epsilon, \forall T \triangledown P: |S(P, T, f, \alpha) - A| \lt \epsilon
$$

- We write $f \in R(\alpha)[a, b]$, and say $f$ is called Riemann-Stieltjes integrable with respect to $\alpha$ on $[a, b]$.

- When such $A$ exists, it must be unique following the definition.

- $f$ is the **integrand** and $\alpha$ is the **integrator**. 

- When the integral exists, $x$ is called the **dummy variable**.
  $$
  A = \int_a^b f(x) \dd \alpha (x) = \int_{a}^b f \dd \alpha
  $$

- $f \in R(\alpha)[a, b]$ implies $f \in R(\alpha)[c, d]$ for any $[c, d] \subset [a, b]$.

- We extend the definition of RS integral to $a > b$:

  - When $a > b$, define $\int_a^b f \dd\alpha = - \int_b^a f \dd\alpha$ if the latter exists.
  - When $a = b$, define $\int_a^b f \dd\alpha = 0$.


When $\alpha(x) = x$, the integral is exactly the Riemann integral.

- And we write $A = \int_a^b f(x) \dd x$, $f \in R[a, b]$.
- Change $f(x)$ at **finite points** in $[a, b]$ does not change Riemann Integrability or the Integral value.
- For Riemann Integral, $f$ is allowed to be **undefined** at finite points in $[a, b]$. But $f$ must be bounded at defined points.

##### Inverted and complex RS integral

Suppose $f, \alpha : [a, b] \to \C$ are bounded.

And $f(x) = u(x) + iv(x)$, $\alpha(x) = \theta(x) + i\rho(x)$. Where $u, v, \theta, \rho :[a, b] \to \R$ are bounded.

Define $f \in R(\alpha)[a, b]$ if $u \in R(\theta)[a, b]$ and so on. And define $\alpha(f)$ as:
$$
\int_{a}^{b} f \dd \alpha=\left(\int_{a}^{b} u \dd \theta-\int_{a}^{b} v \dd \rho\right)+i\left(\int_{a}^{b} u \dd \rho + \int_{a}^{b} v \dd \theta\right)
$$

##### Linearity of RS integral

Suppose $f, g, \alpha, \beta : [a, b] \to \R$.

- For $f, g \in R(\alpha)[a, b]$, $\alpha (f + g) = \alpha f + \alpha g$.
- For $c \in \R$, $\alpha(cf) = c (\alpha f) = (c\alpha)(f)$.
- For $f \in R(\alpha)[a,b]$ and $f \in R(\beta)[a, b]$. $(\alpha + \beta)(f) = \alpha(f) + \beta(f)$.
- For $a < c < b$: any two implies the other exists, $\int_{a}^{c} f \dd \alpha+\int_{c}^{b} f \dd \alpha=\int_{a}^{b} f \dd \alpha$.

##### Integral by parts I

$f \in R(\alpha)[a, b]\implies \alpha \in R(f)[a, b]$. Further
$$
\int_{a}^{b} f(x) \dd \alpha(x)+\int_{a}^{b} \alpha(x) \dd f(x)=f(b) \alpha(b)-f(a) \alpha(a)
$$

- $f \in R(\alpha)[a, b] \implies \exists A \in \C,\forall \epsilon > 0, \exists P_\epsilon > 0, \forall P' \supseteq P_\epsilon, \forall T \triangledown P':|S(P', T, f, \alpha) - A| < \epsilon$
- For **any** $P\supseteq P_\epsilon$ contains $a = x_0 < \cdots < x_n = b$ and $T$ is $1 \le k \le n$, $t_k \in [x_{k - 1}, x_k]$.
- $E = S(P, T, \alpha, f) = \sum_{k = 1}^n \alpha(t_k) \Delta f_k = \sum_{k = 1}^n \alpha(t_k)f(x_k) - \sum_{k = 1}^n \alpha(t_k) f(x_{k - 1})$
- $D = (f\alpha)(b) - (f\alpha)(a) = \sum_{k = 1}^n f(x_k)\alpha(x_k) - \sum_{k = 1}^n f(x_{k - 1})\alpha(x_{k - 1})$.
- $D - E = \sum_{k = 1}^n f(x_k)(\alpha(x_k) - \alpha(t_k)) + \sum_{k = 1}^n f(x_{k - 1})(\alpha(t_k) - \alpha(x_{k - 1}))$.
- Let $P' = P \cup T \in P[a, b]$. Then $P' \supseteq P \supseteq P_\epsilon$, and $P \triangledown P'$. So $|E - (D - A)| < \epsilon$.
- So $\exists A \in \C, \forall \epsilon > 0, \exists P_\epsilon > 0, \forall P \supseteq P_\epsilon, \forall T \triangledown P: |S(P, T, \alpha, f) - (D - A)| < \epsilon$.

##### Change of variable

Suppose $f \in R(\alpha)[a, b]$.

And $g: [c, d] \to [a, b]$ is strictly increasing and continuous on $[c, d]$.

Then $f\circ g \in R(\alpha \circ g)[c, d]$, and we have:
$$
\int_{c}^{d} f[g(x)] \dd\{\alpha[g(x)]\} = \int_{g(c)}^{g(d)} f(t) \dd \alpha(t)
$$

For a proof, consider image partition $g[P_\epsilon] \in P[c, d]$.

##### Reduce RS integral to Riemann I

 

Suppose $f \in R(\alpha)[a, b]$ and $\alpha \in C^1[a, b]$. Then $f\alpha' \in R[a, b]$ and
$$
\int_{a}^{b} f(x) \alpha^{\prime}(x) \dd x = \int_{a}^{b} f(x) \dd \alpha(x)
$$
Proof:

- $\exists A \in C,\forall \epsilon > 0, \exists P_\epsilon \in P[a, b], \forall P \supseteq P_\epsilon, \forall T \triangledown P: |S(P, T, f, \alpha) - A| < \epsilon$.
- $B = S(P, T, f \alpha', x) = \sum_{k = 1}^n f(t_k) \alpha'(t_k)\Delta x_k$.
- $C = S(P, T, f, \alpha) = \sum_{k = 1}^n f(t_k)\Delta \alpha_k = \sum_{k = 1}^n f(t_k) \alpha'(v_k)\Delta x_k$, $v_k \in (x_{k - 1}, x_k)$.
- Since $\alpha' \in C[a, b]$, $\alpha'$ is uniformly continuous on $[a, b]$.
- $|B - C| \le \sum_{k = 1}^n |f(t_k)||\alpha'(t_k) - \alpha'(v_k)|\Delta x_k \le M (b - a) \epsilon$.
- So $\exists A \in C, \forall \epsilon > 0, \exists P_\epsilon > 0, \forall P \supseteq P_\epsilon, \forall T \triangledown P: |S(P, T, f\alpha', x) - A| < \epsilon$.

##### Upper and lower RS integral

Suppose $f, \alpha: [a, b] \to \R$ are **bounded**.

- Suppose $P = \{x_k\}_{k=0}^n \in P[a, b]$.

- Define $M_{k}(f)=\sup \left\{f(x): x \in\left[x_{k-1}, x_{k}\right]\right\}$ and $m_{k}(f)=\inf \left\{f(x): x \in\left[x_{k-1}, x_{k}\right]\right\}$.

- Define the **upper and lower Stieltjes sums** of $f$ with respect to $\alpha$ for the partition $P$ as:
  $$
  U(P, f, \alpha):=\sum_{k=1}^{n} M_{k}(f) \Delta \alpha_{k};\quad L(P, f, \alpha):=\sum_{k=1}^{n} m_{k}(f) \Delta \alpha_{k}
  $$

- Define the **upper and lower RS integral** of $f$ with respect to $\alpha$ as:

$$
\overline \alpha(f) =\overline{\int_{a}^{b}} f \dd \alpha :=\inf \{U(P, f, \alpha): P \in P[a, b]\}; \quad \overline \alpha(f) =\underline{\int_{a}^{b}} f \dd \alpha :=\sup \{L(P, f, \alpha): P \in P[a, b]\}
$$

##### Properties of upper and lower integral

Suppose $f, g, \alpha: [a, b] \to \R$ are **bounded**. And $\alpha \nearrow [a, b]$, then

- $L(P, f, \alpha) \leq S(P, T, f, \alpha) \leq U(P, f, \alpha)$ since
  $$
  \forall T =\{t_k\}_{k = 1}^n \triangledown P: m_k(f) \Delta \alpha_k \le f(t_k) \Delta \alpha_k \le M_k(f) \Delta \alpha_k
  $$

- $P' \supseteq P \implies L(P, f, \alpha)\le L(P', f, \alpha)\le U(P', f, \alpha) \le U(P, f, \alpha)$.

  - The difference $U(P, f, \alpha) - L(P, f, \alpha)$ **decreases** as $P$ gets **finer**.

- For any $P_1, P_2 \in P[a, b]$, $L(P_1, f, \alpha) \le \underline \alpha(f) \le \overline \alpha(f) \le U(P_2, f, \alpha)$.

- The upper and lower integral has sub-linearity:

  - For $a < c < b$, $\overline{\int_{a}^{b}} f \dd \alpha=\overline{\int_{a}^{c}} f \dd \alpha+\overline{\int_{c}^{b}} f \dd \alpha$ and $\underline{\int_{a}^{b}} f \dd \alpha=\underline{\int_{a}^{c}} f \dd \alpha+\underline{\int_{c}^{b}} f \dd \alpha$.
  - For $c \in [0, \infty)$, $\overline \alpha(cf) = (c \overline\alpha)(f) = c(\overline \alpha (f))$.
  - $\overline \alpha (-f) = - \underline \alpha f$.
  - But $\overline \alpha(f + g) \le \overline \alpha(f) + \overline \alpha (g)$ and $\underline \alpha(f + g) \ge \underline \alpha (f) + \underline \alpha(g)$.


##### Riemann's condition

Suppose $f,\alpha: [a, b] \to \R$ are bounded.

$f$ satisfies Riemann's condition with respect to $\alpha$ on $[a, b]$ if and only if 
$$
\forall \epsilon > 0, \exists P_\epsilon \in P[a, b], \forall P \triangle P_\epsilon: 0 \le U(P, f, \alpha) - L(P, f, \alpha) \le \epsilon
$$

Further suppose $\alpha \nearrow [a, b]$. **The following are equivalent**:

1. $f \in R(\alpha)[a, b]$.
2. $f$ satisfies **Riemann's condition** with respect to $\alpha$ on $[a, b]$.
3. $\underline \alpha(f) = \overline \alpha (f)$.

##### RS integral and total variance

Suppose $f, g, \alpha: [a, b] \to \R$ are bounded, and $\alpha \nearrow [a, b]$, and $f, g \in R(\alpha)[a, b]$.

- $\forall x \in [a, b]: f(x) \le g(x) \implies \int_{a}^{b} f(x) \dd \alpha(x) \leq \int_{a}^{b} g(x) \dd \alpha(x)$.

Suppose $f, \alpha: [a, b] \to \R$ are bounded, and $\alpha \in V[a, b]$.

- $f \in R(\alpha)[a, b]$ implies $|f| \in R(\alpha)[a, b]$.
- $f \in R(\alpha)[a, b]$ implies $f^2 \in R(\alpha)[a, b]$.
- $f, g \in R(\alpha)[a, b]$ implies $f \cdot g \in R(\alpha)[a, b]$.

Suppose $f, \alpha: [a, b] \to \R$ are bounded, and $\alpha \nearrow [a, b]$.

- Notice that $-f\le |f|$ and $f \le |f|$, so

$$
\left|\int_{a}^{b} f(x) \dd \alpha(x)\right| \leq \int_{a}^{b}|f(x)| \dd \alpha(x)
$$

Suppose $f, \alpha: [a, b] \to \R$ are bounded, and $\alpha \in V[a, b]$.

- Consider function $V(x) = V_\alpha(a, x) \nearrow [a, b]$.
- (**==TODO==, Apostol, p.157**) $f \in R(\alpha)[a, b] \implies f \in R(V)[a, b]$.
  - So $f \in R(\alpha)$ iff $f \in R(V - \alpha)$ and $f \in R(V)$.
  - And $\alpha (f) = V(f) - (V - \alpha)(f)$.

##### Integral by Parts II

Suppose $f, g, \alpha: [a, b] \to \R$ are bounded, and $\alpha \nearrow [a, b]$.

- Then $\alpha(fg) = G(f)$. Where $G = \int_a^x gd \alpha$ for $x \in [a, b]$.

Proof:

- Suppose $P \in P[a, b]$, where $a = x_0 < \cdots < x_n = b$. And $T \triangledown P = \{t_k\}_{k = 1}^n$.
- $S(P, T, f, G) = \sum_{k=1}^{n} \int_{x_{k-1}}^{x_{k}} f\left(t_{k}\right) g(t) d \alpha(t)$. And $\int_{a}^{b} fgd \alpha =\sum_{k=1}^{n} \int_{x_{k-1}}^{x_{k}} fg d \alpha$.
- $|S(P, T, f, G) - \int_a^b fg d\alpha| \le M_{g} \sum_{k=1}^{n} \int_{x_{k-1}}^{x_{k}}\left[M_{k}(f)-m_{k}(f)\right] d \alpha(t)$.
- So $f \in R(G)[a, b]$, and $G(f) = \alpha(f g)$.

##### A sufficient condition for RS integrability

Suppose $f, \alpha: [a, b] \to \R$ are bounded.

- Then $f \in C[a, b] \land \alpha \in V[a, b] \implies f \in R(\alpha)[a, b]$.

##### A sufficient condition for Non-RS integrability

Suppose $f, \alpha: [a, b] \to \R$ are bounded. $\alpha \nearrow [a, b]$. $\int_a^b f d\alpha$ can not exist when

- None of $f, \alpha$ is right-continuous at some $c \in [a, b)$. Or
- None of $f, \alpha$ is left-continuous at some $c \in (a, b]$.

##### MVT

Suppose $f, \alpha: [a, b] \to \R$ are bounded. Suppose $f \in R(\alpha)[a, b]$ and $\alpha \nearrow [a, b]$. 

Then for some $c \in [\inf f[a, b], \sup f[a, b]]$: $\alpha(f) = c(\alpha(b) - \alpha(a))$.

##### Primitives

For $f: [a, b] \to \R$. Suppose $F \in C[a, b] \cap D(a, b)$ and $F' = f$ on $(a, b)$. 

Then $F$ is a **primitive** of $f$ on $[a, b]$, also called **indefinite integral**, or **antiderivative**.

- Primitives of $f$ differ by constants.
  - Suppose $F, G$ are primitive of $f$. $F'(x) = G'(x) = f(x)$ for $x \in (a, b)$.
  - So $H(x) = F - G$. $H' = F' - G' = 0$. So $F - G$ is constant.

##### RS Integral interval functions

Suppose $\alpha \nearrow [a, b]$ and $f \in R(\alpha)[a, b]$.

Define $F(x) = \int_a^x f d\alpha$ for $x \in [a, b]$.

- For $(x, y) \in [a, b]^2$ define $c: [a, b]^2 \to \R$ as the mean value of $\int_x^y f \dd \alpha$.
  - Where $F(y) - F(x) = \int_x^y f d\alpha = c(x, y)[\alpha(y) - \alpha(x)]$.
  - And $c(x, y)\in[\inf f[x, y], \sup f[x, y]]$.
- $F \in V[a, b]$.
- $F$ is left / right **continuous** in $[a, b]$ where $\alpha$ is left / right continuous in $[a, b]$.
- (**FTC I**) $F$ is left / right **differentiable** in $[a, b]$ where $\alpha$ is left / right differentiable and $f$ is left / right continuous. Where $F'_{\pm}(x) = f(x) \alpha'_{\pm}(x)$.

Consider the Riemann integral where $\alpha = x$.

- $F \in V[a, b]$ and $F \in C[a, b]$.
- (**FTC II**) $F'_\pm(x) = f(x)$ when $f(x)$ is left / right continuous at $x \in [a, b]$.
- Suppose $f \in C(a, b)$, then $F$ is a primitive of $f$ on $[a, b]$.

#### Further Properties of Riemann Integral

##### FTC III

Suppose $f \in R[a, b]$. Suppose $F$ is a primitive of $f$ on $[a, b]$. Then we have $\int_{a}^{b} f(x) d x = F(b) - F(a)$.

- $\forall \epsilon > 0, \exists P_\epsilon \in P[a, b], \forall P \supseteq P_\epsilon, \forall T \triangledown P: |S(P, T, f, x) - A| < \epsilon$.
- $F(b) - F(a) = \sum_{k = 1}^n f'(v_k)\Delta x_k$. So $|F(b) - F(a) - A| < \epsilon$ as well.

Notice that $F(x) - F(a) = \int_a^x f(x) \dd x$.

##### IBP for Riemann

Suppose $f, g: [a, b] \to \R$ and $f, g \in C[a, b]$. Suppose $F, G$ are primitives of $f, g$. Then by (**FTC III**) and (**Reduce to Riemann**) and (**IBP I**).
$$
\int_a^b f(t) G(t) \dd t + \int_a^b F(t) g(t) \dd t = \left [ F(t) G(t)\right]_a^b
$$
##### Reduce to Riemann II

Suppose $f \in R[a, b]$, $\alpha \in D(a, b)$ and $\alpha' \in R[a, b]$ (might not be defined on end points).

- $\alpha(x) - \alpha(a) = \int_a^x \alpha' \dd t$ by (**FTC III**).
- Since $f, \alpha' \in R[a, b]$. So $f \in R(\alpha)[a, b]$ and $\int_a^b f d \alpha = \int_a^b f \alpha' \dd x$.

##### Change of Variable for Riemann I

Suppose $g \in C^1[c, d]$ and $f \in C[g[c, d]]$.
$$
\int_c^d f[g(t)] g'(t) \dd t = \int_{g(c)}^{g(d)} f(t) \dd t
$$
##### Change of Variable for Riemann II

- Suppose $h \in R[c, d]$. $g(x) = \int_a^x h$ for some $a \in [c, d]$ and $x \in [c,d]$.
- Suppose $f \in R\,g[c, d]$.

Then $(f \circ g) \cdot h \in R[c, d]$ and the following is true:
$$
\int_c^d f[g(t)] h(t) \dd t = \int_{g(c)}^{g(d)} f(t) \dd t
$$

##### Mean Value Theorem for Riemann I

Suppose $f \in R[a, b]$.

- There is a unique $c \in [\inf f[a, b], \sup f[a, b]]$.

$$
  \int_{a}^{b} f(x) \dd x =c (b - a)
$$

- Can treat $c$ as a function $c(a, b)$ of the end points.
- Suppose further $f \in C[a, b]$, $\exists x_0 \in [a, b]: f(x_0) = c(a, b)$.

$$
  \int_{a}^{b} f(x) \dd (x)= f(x_0) (b - a)
$$

##### Mean Value Theorem for Riemann II

Suppose $f \nearrow [a, b]$. Suppose $g \in C[a, b]$.

- There exists a point $x_0 \in [a, b]$ such that 
  $$
  \int_{a}^{b} f(x) g(x) \dd x=f(a) \int_{a}^{x_{0}} g(x) d x+f(b) \int_{x_{0}}^{b} g(x) \dd x
  $$

- (**Bonnet**) Further suppose $\forall x \in [a, b]: f(x) \ge 0$. There exists a $x_0 \in [a, b]$ such that:
  $$
  \int_{a}^{b} f(x) g(x) d x=f(b) \int_{x_{0}}^{b} g(x) \dd x
  $$

- Since modify $f(a)$ and $f(b)$ does not change Riemann integrals. You can replace $f(a)$ with any $A \le f(a+)$ and $f(b)$ with $B \ge f(b-)$.

##### Parameterized RS Integral is Continuous

Suppose $f: [a, b] \times [c, d] \to \R$ is continuous. Suppose $\alpha \in V[a, b]$. Define
$$
F(y) = \int_a^b f(x, y) \dd \alpha(x)
$$
Then $F \in C[c, d]$. For any $y_0 \in [c, d]$:
$$
\lim _{y \to y_{0}} \int_{a}^{b} f(x, y) d \alpha(x) =\int_{a}^{b} \lim _{y \to y_{0}} f(x, y) d \alpha(x)=\int_{a}^{b} f\left(x, y_{0}\right) d \alpha(x)
$$
Suppose $g \in R[a, b]$, and $G = \int_a^x g \in C[a, b]$. Replace $\alpha(x)$ by $G$ gives:
$$
\lim _{y \to y_{0}} \int_{a}^{b} f(x, y)g(x) \dd x = \int_{a}^{b} \lim _{y \to y_{0}} f(x, y) g(x)\dd x = \int_{a}^{b} f\left(x, y_{0}\right) \dd G(x)
$$
