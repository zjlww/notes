> The grounding paper of the field: Shin, J., & Kim, S.J. (2006). A Mathematical Theory of Communication.
>
> [NCTU Information Theory](https://www.bilibili.com/video/BV14N41197bN) video lectures.

#### Information Measures

##### Shannon entropy

Suppose $X \in \L(\Omega \to \X, \F / \F_\X)$. And $\mu$ is a reference measure on $(\X, \F_\X)$.

- We often omit $\dd \mu(x)$ as $\dd x$, similar to the Lebesgue measure on $\R^d$.

Suppose $\dd P_X(x) = p(x) \dd x$. Then
$$
H(X) := E\s{\log\frac{1}{ p(X)}} = \int_\X p(x) \log \frac{1}{p(x)} \dd x =: H(p)
$$

> We use the convention $1/0 = \infty$ and $0 \cdot \infty = 0$ here $\lim_{x \downarrow 0} x \log x = 0$ gives a hint to this convention.

$\log p(x)$ is also called the information of symbol $x \in \mathcal X$.

The conditional entropy of $X$ over event $A \in \mathcal F$ is defined as:
$$
H(X | A):= H(p_{X|A}) = \int p_{X|A}(x) \log \frac{1}{p_{X|A}(x)} \dd x = E[-\log p_{X|A}(X)|A]
$$

##### Joint Shannon entropy

Suppose $X \in \L(\Omega \to \X, \F / \F_\X)$ and $Y \in \L(\Omega \to \Y, \F / \F_\Y)$. And $\mu$ is a reference measure on $(\X \times \Y, \F_\X \otimes \F_\Y)$. And all density and conditional density functions are well defined.
$$
H(X, Y) := E\s{\log \frac{1}{p_{XY}(X, Y)}} = \iint \log \frac{1}{p(x, y)} p(x, y) \dd x \dd y = : H(p_{XY})
$$
The conditional entropy over event $Y = y$ is a function of $y$ defined as:
$$
H(X | Y = y) := H(p_{X|y}) = \int p(x|y) \log \frac{1}{p(x|y)} \dd x = E[-\log p(X|y) | Y = y]
$$
The conditional entropy of $X$ over random variable $Y$ is defined as:
$$
H(X|Y) = \iint p(x, y) \log \frac{1}{p(x | y)} \dd x \dd y = E[-\log p(X|Y)]
$$
In general, we define the following form formula as:
$$
H(X, Y | Z, W = w) = \iiint p(x, y, z | w) \log \frac{1}{p(x, y | z, w)} \dd x \dd y \dd z
$$
More generally, define,
$$
H(X, Y | Z, W = w) = \int p(z|w) H(X, Y|Z = z, W = w) \dd z
$$
We have following properties:

- The joint entropy is connected with the conditional entropy:
  $$
  H(X, Y) = \iint p(y)p(x | y) [-\log p(y) - \log p(x | y)] \dd x \dd y =H(Y) + H(X|Y)
  $$

- Adding conditions to entropies:
  $$
  H(X, Y) = H(X) + H(Y | X)\\
  H(X, Y|W) = H(X|W) + H(Y|X, W)\\
  H(X, Y|W, S = s) = H(X|W, S = s) + H(Y|X, W, S = s)
  $$

##### Example: Entropy of a Bernoulli r.v.

Suppose $X \sim \operatorname{Bernoulli}(p)$, then 
$$
H(p):= H(X) = - p \log p - (1 - p) \log (1 - p)
$$

- The maximum is obtained at $p = q = 1/2$, $H(X) = 1$.
- The minimum is obtained at $p \to 0$, $H(X) = 0$.

##### Shannon mutual information

Define the mutual information of $X; Y$ as:
$$
I(X;Y) = \iint p(x, y) \log \frac{p(x, y)}{p(x)p(y)} \dd x \dd y = E\left[\log \frac{p(X, Y)}{p(X)p(Y)}\right] = \d{p(x, y)}{p(x)p(y)}
$$
The conditional mutual information of $X, Y$ over event $A \in \F$ is defined as:
$$
I(X; Y | A) = \iint p_A(x, y) \log \frac{p_A(x, y)}{p_A(x)p_A(y)} \dd x \dd y = E\left [\frac{p_A(X, Y)}{p_A(X)p_A(Y)}\right]
$$
The conditional mutual information of $X, Y$ over $W = w$ is defined as:
$$
I(X; Y | W = w) = \iint p(x, y | w) \log \frac{p(x, y|w)}{p(x|w)p(y|w)} \dd x \dd y
$$
The conditional mutual information of $X, Y$ over random variable $W$ is defined as:
$$
I(X; Y | W) = \int  p(w) I(X; Y|W = w) \dd w = \iiint p(x, y, w) \log \frac{p(x, y|w)}{p(x |w)p(y|w)} \dd x \dd y \dd w
$$
In general, we define the following:
$$
I(X; Y | W, S = s) = \iiint p(x, y, w | s) \log \frac{p(x, y | w, s)}{p(x | w, s) p(y | w ,s)} \dd x \dd y \dd w
$$
We have following properties:

- $I(X; Y) \ge 0$, from the fundamental inequality $1 - 1/z \le \ln z \le z - 1$ for $z > 0$,
  $$
  \iint p(x, y) \log \frac{p(x, y)}{p(x) p(y)} \dd (x, y) \ge \iint p(x, y)\p{1 - \frac{p(x) p(y)}{p(x, y)}} \dd (x, y) \ge 0
  $$

##### Venn diagram and information measures

We have many relationships:
$$
I(X; Y | Z) = \iiint p(x, y, z) \left(\log \frac{p(x, y | z)}{p(x|z)p(y|z)}\right) \dd(x, y, z) = H(X | Z) + H(Y | Z) - H(X, Y | Z)\\
H(X|Y) = H(X, Y) - H(Y); \quad H(X, Y | Z) = H(X, Y, Z) - H(Z)
\\
H(X|Y, Z = z) = H(X, Y | Z = z) - H(Y | Z = z); \quad H(X|Y, Z) = H(X, Y | Z) - H(Y |Z)\\
$$
These equations allows us to organize them into Venn diagrams:

| <img src="images/Venn-diagram-for-two-random-variables.png" alt="Venn diagram for two random variables. " style="zoom:60%;" /> | <img src="images/Venn-diagram-for-three-random-variables.png" alt="Venn diagram for three random variables. " style="zoom: 60%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                      2 random variables                      |                     3 random variables.                      |

Notice that $I(X; Y; Z)$ is not a standard information measure. But we have:
$$
I(X; Y; Z) = I(X; Y) - I(X; Y | Z)
$$

##### Properties of Shannon information measures

- The following are equivalent:
  1. $X \perp Y$.
  2. $H(X, Y) = H(X) + H(Y)$.
  3. $H(X) = H(X | Y)$ or $H(Y) = H(Y|X)$.
  4. $I(X; Y) = 0$.
- The following are equivalent for countable $\X \times \Y$.
  1. $H(X, Y) = H(X)$.
  2. $H(Y | X) = 0$.
  3. $\exists f \in \mathcal X \to \mathcal Y: P(Y = f(X)) = 1$.
- When $X$ is discrete, the entropy $H(X) \ge 0$. The proofs do not work for the non-discrete case.

  - $H(X) = I(X; X)\ge 0$.
  - $H(X|A) = I(X; X | A) \ge 0$.
  - $H(X|Z=z) = I(X; X | Z = z) \ge 0$.
  - $H(X|Z) = I(X; X|Z) \ge 0$.
  - $H(X, Y) = I((X, Y);(X, Y)) \ge 0$.
  - $H(X, Y | Z, W = w) \ge 0$ in general.

##### Chain rules of Shannon information measures

Suppose $(X_1, \ldots, X_n), Y$ are random variables on $(\Omega, \F, P)$ with all density functions well defined.

- $p(x_1, \cdots, x_n) = \prod_{k = 1}^n p(x_k | x_{< k})$.
- $p(x_1, \cdots, x_n | y) = \prod_{k = 1}^n p(x_k | x_{< k}, y)$.

It is easy to derive the chain rule of Entropy by definition:

- $H(X_1, \cdots, X_n) = \sum_{k = 1}^n H(X_{k} | X_{< k})$.
- $H(X_1, \cdots, X_n | Y = y) = \sum_{k = 1}^\infty H(X_k|X_{< k}, Y = y)$.
- $H(X_1, \cdots, X_n| Y) = \sum_{k = 1}^\infty H(X_k | X_{<k}, Y)$.

Further, we have the chain rule of mutual information:

- $I(X_1, \cdots, X_n; Y) = \sum_{k = 1}^\infty I(X_k; Y| X_{<k})$.
- $I(X_1, \cdots, X_n; Y | Z = z) = \sum_{k = 1}^\infty I(X_k; Y|X_{<k}, Z = z)$.
- $I(X_1, \cdots, X_n; Y| Z) = \sum_{k = 1}^\infty I(X_K; Y|X_{< k}, Z)$.

##### Independence Bound of Entropy
$$
H(X_1, \cdots X_n) = \sum_{k = 1}^n H(X_k | X_{< k}) \le \sum_{k = 1}^n H(X_k)
$$
with equality iff $\forall 1 \le k \le n: X_k \perp X_{<k}$ iff $\{X_1, \cdots, X_n\}$ is an independent family.

##### Upper bound of entropy on finite alphabet

 Suppose $\mathcal X$ is finite.
$$
H(X) \le \log |\mathcal X|
$$
With equality if and only if $X \sim \operatorname{Uniform}(\mathcal X)$. Suppose $u(x) = 1 / |\mathcal X|$.
$$
D(p \| u) = \sum_{x \in \mathcal X} p(x) \log \frac{p(x)}{u(x)} = \log |\mathcal X| - H(p) \ge 0
$$

##### Fano's inequality

Suppose $X \in \L(\Omega \to \X, \F / \F_\X)$ and $Y \in \L(\Omega \to \Y, \F/\F_\Y)$. Where $\X$ is finite and $|\X| \ge 2$.

Consider $g: \Y \to \X$. Let $\what X := g(Y)$. And given $P(\what X \neq X) = p_e$.

- Define $A = 1\p{X \neq g(Y)}$.

- Observe
  $$
  \begin{aligned}
  H(X | Y) & = H(X | Y) + H(A | X, Y) = H(A, X | Y) = H(X | Y, A) + H(A | Y)\\
  & \le H(A) + H(X | Y, A) = H(p_e) + p_e H(X | Y, A = 1) + (1 - p_e) H(X | Y, A = 0)\\
  & = H(p_e) + p_e H(X | Y, A = 1)
  \end{aligned}
  $$

- With equality if and only if $A \perp Y$.

- Further notice that
  $$
  H(X | Y, A = 1) = \iint p(x, y | A = 1) \log \frac{1}{p(x | y, A = 1)} \dd x \dd y \le \log (|\X| - 1)
  $$

- With equality if and only if $p(x | y, A = 1)$ is always uniform for all $y \in \Y$.

- Therefore
  $$
  H(X | Y) \le H(p_e) + p_e \log (|\X| - 1)
  $$

- Very often, we only need the simplified version:
  $$
  H(X | Y) \le 1 + p_e \log |\X|
  $$

- 

