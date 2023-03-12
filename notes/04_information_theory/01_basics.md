> Shin, J., & Kim, S.J. (2006). A Mathematical Theory of Communication.

#### Information Measures in the Discrete Case

Suppose $X, Y, Z, W$ are discrete random variables on $(\Omega, \F, P)$. There image $\mathcal {X, Y, Z, W}$ are countable supports, denoted by $\su X = \mathcal X$.

##### Probability mass function

 We allow the following abbreviation:
$$
p_{X,Y|Z}(x, y | z) = p(x, y | z):= \Pr(X = x, Y = y \mid Z = z)
$$
$p(x, y | z)$ is called the **probability mass function** of $X, Y$ conditioned on $Z$.

In this case, we have:

- Independence of a pair of d.r.v. $X$ and $Y$ if:
  $$
  \forall x \in \mathcal X,\forall y \in \mathcal Y: p(x, y) = p(x) p(y)
  $$

- Independence of a family of d.r.v. $\mathbf X$ is independent if for any finite subset of $\mathbf X$, the joint PMF of $X_{1}, \cdots, X_n$:
  $$
  \forall x_k \in \mathcal X_k:p_{X_1\cdots X_n}(x_1, \cdots, x_n) = p(x_1)\cdots p(x_n)
  $$

  - Mutual independence does not imply independence of a family of r.v.s.

- Conditional independence. $X \perp Y \mid Z$ if:

$$
\forall z \in \mathcal Z, \forall x \in \mathcal X, \forall y \in \mathcal Y: p(x, y | z) = p(x | z) p(y | z)
$$

##### Shannon entropy

 Suppose $(\mathcal X, \mathcal{PX})$ is a measurable space where $\mathcal X$ is at most countable. The set of all PMFs on $\mathcal{PX}$ is denoted $\mathcal P_{\mathcal X}$.

The Shannon entropy $H(\cdot): \mathcal{P_X} \to [0, \infty]$ is defined as:
$$
\forall p \in \mathcal{P_X}: H(p) = \sum_{x \in \mathcal X} p(x) \log \frac{1}{p(x)}
$$

> We use the convension $1/0 = \infty$ and $0 \cdot \infty = 0$ here.
>
> $\lim_{x \downarrow 0} x \log x = 0$ gives hint to this convension.

Suppose $X: \Omega \to E$ is a random variable. Suppose $p_X$ is the PMF of $X$. The Shannon entropy $H(X)$ of $X$ is defined as:
$$
H(X) := H(p_X) = \sum_{x \in \mathcal X} p_X(x) \log \frac{1}{p_X(x)} = E[-\log p_X(X)]
$$

- $\log p(x)$ is called the information of symbol $x \in \mathcal X$.

Suppose $X: \Omega \to E$ and $Y: \Omega \to F$ are random variables. Suppose $p_{XY}$ is the joint PMF of $(X, Y)$. Then the joint entropy is defined as:
$$
H(X, Y):= H(p_{XY}) = \sum_{x, y} p(x, y) \log \frac{1}{p(x, y)} = E_{XY}[-\log p_{XY}(X, Y)]
$$
The conditional entropy of $X$ over event $A \in \mathcal F$ is defined as:
$$
H(X | A):= H(p_{X|A}) = \sum_{x} p_{X|A}(x) \log \frac{1}{p_{X|A}(x)} = E[-\log p_{X|A}(X)|A]
$$
The conditional entropy over event $Y = y$ is a function of $y$ defined as:
$$
H(X | Y = y) := H(p_{X|y}) = \sum_{x} p(x|y) \log \frac{1}{p(x|y)} = E[-\log p_{X|y}(X)|Y = y]
$$
The conditional entropy of $X$ over random variable $Y$ is defined as:
$$
H(X|Y) = \sum_{x, y} p(x, y) \log \frac{1}{p(x | y)} = E_{XY}[-\log p(X|Y)]
$$
The joint entropy is connected with the conditional entropy:
$$
\begin{aligned}
H(X, Y) &= \sum_{y} \sum_{x} p(y)p(x | y) [-\log p(y) - \log p(x | y)] \\
&= \sum_{y} p(y)\log \frac{1}{p(y)} + p(y) H(X|Y = y) = H(Y) + H(X|Y)
\end{aligned}
$$
In general, we define the following form formula as:
$$
H(X, Y | Z, W = w) = \sum_{x, y, z} p(x, y, z | w) \log \frac{1}{p(x, y | z, w)}\\
$$
We can *activate a dead variable*.
$$
H(X, Y | Z, W = w) = \sum_{z} p(z|w) H(X, Y|Z = z, W = w)\\
H(X, Y | Z, W) = \sum_{z, w} p(z, w) H(X, Y| Z = z, W = w)
$$
We can *add conditioning to all terms*:
$$
H(X, Y) = H(X) + H(Y | X)\\
H(X, Y|W) = H(X|W) + H(Y|X, W)\\
H(X, Y|W, S = s) = H(X|W, S = s) + H(Y|X, W, S = s)
$$
##### Entropy of a Bernoulli r.v.

 Suppose $X \sim \operatorname{Bernoulli}(p)$. Define:
$$
H(p):=H(p, 1-p) = - p \log p - (1 - p) \log (1 - p)
$$

- $H(p) = H(1 - p)$.
- The maximum is obtained at $p = q = 1/2$, $H(p) = 1$.
- The minimum is obtained at $p \to 0$, $H(p) = 0$.

##### Examples: computing entropy

- Suppose $p(x) = 2^{-x}, x \ge 1$. Then $H(X) = \sum_{x = 1}^\infty x 2^{-x} = 2$.

- Suppose the support is $\left\{(i, j): 1 \leq i<\infty \text { and } 1 \leq j \leq \frac{2^{2^{i}}}{2^{i}}\right\}$ and $p(i, j) = 2^{-2^{i}}$.
  $$
  H(X) = \sum_{i = 1}^\infty \sum_{j = 1}^{2^{2^i}/2^i} - \log (2^{-2^i}) 2^{-2^i} =  \sum_{i = 1}^\infty \sum_{j = 1}^{2^{2^i}/2^i} 2^{-2^i} 2^i = \infty
  $$

##### Minimal entropy

 The min of all informations of symbols is called the minimal entropy, 
$$
H_{\infty}(X):= \log \frac{1}{\max_{x \in \mathcal X} p(x)} = \min_{x \in \mathcal X} \log\frac{1}{ p(x)}
$$

- Suppose $|\mathcal X| = n$, $0 \le H_{\infty}(X) \le \log n$.
- The maximum bound is obtained when $X$ is uniform.
- The minimum bound is obtained when $X$ is determined.
- $\forall x \in \mathcal X: H_{\infty}(X) \le -\log p(x)$.

##### Independent and Identical r.v.s and entropy

The following are equivalent. $Y$ is independent from $X$.

- $X \perp Y$.
- $\forall x \in \mathcal X, y \in \mathcal Y: p(x, y) = p(x) p(y)$.
- $H(X, Y) = H(X) + H(Y)$.
- $H(X) = H(X | Y)$.

The following are equivalent. $Y$ is a function of $X$.

- $\exists f \in \mathcal X \to \mathcal Y: Y = f(X)$.
- $\exists f \in \mathcal X \to \mathcal Y, \forall x \in \mathcal X, y \in \mathcal Y: p(x, y) = 1(y = f(x))$.
- $\forall x \in \mathcal X, \forall y \in \mathcal Y: p(x, y) = 0 \lor p(y|x) = 1$.
- $H(X, Y) = H(X)$.
- $H(Y | X) = 0$.
- $\forall x \in \mathcal X, \exists! y \in \mathcal Y: p(y | x) = 1$.

The following are equivalent. $X$ and $Y$ are isomorphic, or just $X \simeq Y$.

The notation $\mathcal X \leftrightarrow \mathcal Y$ is the set of all bijections from $\mathcal X$ to $\mathcal Y$.

- $\exists f \in \mathcal X \leftrightarrow \mathcal Y: Y(\omega) = f(X(\omega))$.
- $\exists f \in \mathcal X \leftrightarrow \mathcal Y,\forall x \in \mathcal X, y \in \mathcal Y: p(x, y) = 1(y = f(x))$.
- $H(X, Y) = H(X) = H(Y)$.
- $H(X|Y) = 0$ and $H(Y | X) = 0$.
- $\forall x \in \mathcal X, \exists! y \in \mathcal Y: p(y | x) = 1$ and $\forall y \in \mathcal Y, \exists! x \in \mathcal X: p(x | y) = 1$.

##### Example: computing conditional entropy

 Let $(X, Y)$ have the following distributions:
$$
\begin{array}{c|cccc} 
_Y\backslash^X& 1 & 2 & 3 & 4 \\
\hline 1 & \frac{1}{8} & \frac{1}{16} & \frac{1}{32} & \frac{1}{32} \\
2 & \frac{1}{16} & \frac{1}{8} & \frac{1}{32} & \frac{1}{32} \\
3 & \frac{1}{16} & \frac{1}{16} & \frac{1}{16} & \frac{1}{16} \\
4 & \frac{1}{4} & 0 & 0 & 0 \\
\hline
\end{array}
$$
The marginal distribution of $X$ is $\left(\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8}\right)$ and the marginal distribution of $Y$ is $\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right)$, and hence $H(X)=\frac{7}{4}$ and $H(Y)=2$. Also,
$$
\begin{aligned}
&H(X \mid Y) =\sum_{i=1}^{4} P(Y=i) H(X \mid Y=i) \\
&=\frac{1}{4} H\left(\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8}\right)+\frac{1}{4} H\left(\frac{1}{4}, \frac{1}{2}, \frac{1}{8}, \frac{1}{8}\right)
+\frac{1}{4} H\left(\frac{1}{4}, \frac{1}{4}, \frac{1}{4}, \frac{1}{4}\right)+\frac{1}{4} H(1,0,0,0) \\
&=\frac{1}{4} \times \frac{7}{4}+\frac{1}{4} \times \frac{7}{4}+\frac{1}{4} \times 2+\frac{1}{4} \times 0 =\frac{11}{8} \text { bits}
\end{aligned}
$$
Similarly, $H(Y \mid X)=\frac{13}{8}$ bits and $H(X, Y)=\frac{27}{8}$ bits.

##### Shannon mutual information

 

Define the mutual information of $X; Y$ as:
$$
I(X;Y) = \sum_{x, y} p(x, y) \log \frac{p(x, y)}{p(x)p(y)} = E\left[\log \frac{p(X, Y)}{p(X)p(Y)}\right]
$$
The conditional mutual information of $X, Y$ over event $A \in \F$ is defined as:
$$
I(X; Y | A) = \sum_{x, y} p_A(x, y) \log \frac{p_A(x, y)}{p_A(x)p_A(y)} = E\left [\frac{p_A(X, Y)}{p_A(X)p_A(Y)}\right]
$$
The conditional mutual information of $X, Y$ over event $W = w$ is defined as:
$$
I(X; Y | W = w) = \sum_{x, y} p(x, y | w) \log \frac{p(x, y|w)}{p(x|w)p(y|w)}
$$
The conditional mutual information of $X, Y$ over random variable $W$ is defined as:
$$
I(X; Y | W) = \sum_{w} p(w) I(X; Y|W = w) = \sum_{x, y, w} p(x, y, w) \log \frac{p(x, y|w)}{p(x |w)p(y|w)}
$$
In general, we define the following formula:
$$
I(X; Y | W, S = s) = \sum_{x, y, w} p(x, y, w | s) \log \frac{p(x, y | w, s)}{p(x | w, s) p(y | w ,s)}
$$
We can *activate a dead variable*.
$$
I(X; Y | Z, W = w) = \sum_{z} p(z|w) I(X;Y|Z = z, W = w)\\
I(X, Y | Z, W) = \sum_{z, w} p(z, w) I(X; Y| Z = z, W = w)
$$
We can *add conditioning to all terms*:
$$
I(X; Y) = H(X) - H(Y | X)\\
I(X; Y|W) = H(X|W) - H(Y|X, W)\\
I(X; Y|W, S = s) = H(X|W, S = s) - H(Y|X, W, S = s)
$$
##### Nonnegativity of information measures

Derived from the fundamental inequality $1 - 1/z \le \ln z \le z - 1$ for $z > 0$.
$$
\begin{aligned}
&\forall z > 0:\ln z \ge 1 - 1/z \implies \ln \frac{p(x, y)}{p(x) p(y)} \ge 1 - \frac{p(x)p(y)}{p(x, y)} \\ &\implies p(x, y) \ln \frac{p(x, y)}{p(x) p(y)} \ge p(x, y) - p(x) p(y)\\
&\implies I(X;Y)/\log(e) \ge \sum_{p(x, y) > 0} \left(p(x, y) - p(x)p(y)\right)\ge 1 - \sum_{p(x)p(y) > 0} p(x) p(y) = 0
\end{aligned}
$$
Notice that $\su(X, Y) \subseteq \mathcal X \times \mathcal Y$, so we have the last inequality.
$$
\begin{aligned}
I(X; Y)  = 0 &\iff \forall (x, y) \in \su(X, Y): \ln \frac{p(x, y)}{p(x)p(y)} = 1 - \frac{p(x)p(y)}{p(x, y)}\\
& \iff \forall (x, y) \in \su (X, Y): p(x, y) = p(x)p(y)\\
& \iff \forall (x, y) \in \mathcal X \times \mathcal Y: p(x, y) = p(x) p(y) \iff X \perp Y\\
& \implies \mathcal X \times \mathcal Y = \su(X, Y)
\end{aligned}
$$


We can show that the mutual information with conditions are positive:

- $I(X; Y | A) \ge 0$, by replacing $p(\cdot) \to p_A(\cdot)$ in the above proof.
- $I(X; Y | Z = z) \ge 0$, by noticing that $Z= z$ is just an event.
- $I(X; Y | Z) \ge 0$, by noticing that this is the weighted sum of $I(X; Y | Z = z)$.
- $I(X; Y| Z, W = w) \ge 0$ in general, by combining above ideas.

We can show that the discrete entropy with conditions are positive:

- $H(X) = I(X; X)\ge 0$.
- $H(X|A) = I(X; X | A) \ge 0$.
- $H(X|Z=z) = I(X; X | Z = z) \ge 0$.
- $H(X|Z) = I(X; X|Z) \ge 0$.
- $H(X, Y) = I((X, Y);(X, Y)) \ge 0$.
- $H(X, Y | Z, W = w) \ge 0$ in general.

##### Venn diagram and information measures

We have many relationships:
$$
I(X; Y | Z) = \sum_{x, y, z} p(x, y, z) \left(\log \frac{p(x, y | z)}{p(x|z)p(y|z)}\right) = H(X | Z) + H(Y | Z) - H(X, Y | Z)\\
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
Since $X \perp Y$ does not imply $X \perp Y | Z$, $I(X; Y; Z)$ can be negative.

> Similarly $X \perp Y | Z$ does not imply $X \perp Y$.

##### Example: Perfect secrecy

 Suppose $X$ is the plaintext, $Y$ is the ciphertext, and $Z$ is the key.

Perfect secrecy is defined by $H(X | Y, Z) = 0$ and $I(X; Y) = 0$.
$$
H(X|Y, Z) = 0 \land I(X; Y) = 0 \implies H(Z) \ge H(X)
$$
To achieve perfect secrecy, $H(Z) \ge H(X)$, the entropy of the key is even larger than that of the information. SO perfect secrecy is expensive.

##### Chain rules

 Suppose $X_1, \cdots, X_n$ are discrete random variables on $(\Omega, \mathcal F, P)$.

Recall that the chain rule in PMF is written as:

- $(1) \quad p(x_1, \cdots, x_n) = \prod_{k = 1}^n p(x_k | x_{< k})$.
- $(2) \quad p(x_1, \cdots, x_n | y) = \prod_{k = 1}^n p(x_k | x_{< k}, y)$.

It is easy to derive the chain rule of Entropy follows from the above:

- $(3) \quad H(X_1, \cdots, X_n) = \sum_{k = 1}^n H(X_{k} | X_{< k})$.
- $(4) \quad H(X_1, \cdots, X_n | Y = y) = \sum_{k = 1}^\infty H(X_k|X_{< k}, Y = y)$.

The conditional over random variable version is:

- $(5) \quad H(X_1, \cdots, X_n| Y) = \sum_{k = 1}^\infty H(X_k | X_{<k}, Y)$.
  - By weighting sum $(4)$ over $y \in \mathcal Y$.
  - By treating $Y$ in $(4)$ as $X_0$. And notice the following: $H(X_1, \cdots, X_n | X_0) + H(X_0) = \sum_{k = 1}^\infty H(X_k | X_{< k}, X_0) + H(X_0)$. 

Further, we have the chain rule of mutual information:

- $(6) \quad I(X_1, \cdots, X_n; Y) = \sum_{k = 1}^\infty I(X_k; Y| X_{<k})$. By $(3) - (4)$.
- $(7)\quad I(X_1, \cdots, X_n; Y | Z = z) = \sum_{k = 1}^\infty I(X_k; Y|X_{<k}, Z = z)$.
- $(8) \quad I(X_1, \cdots, X_n; Y| Z) = \sum_{k = 1}^\infty I(X_K; Y|X_{< k}, Z)$.
  - By weighted sum of $(7)$ over $y \in \mathcal Y$.
  - By applying $(5)$ twice for $H(\cdots | Y)$ and $H(\cdots | Y, Z)$ then subtract.

##### Condition does not increase entropy
$$
I(X; Y) + H(Y | X)  = H(Y) \implies H(Y|X) \le H(Y)
$$
with equality iff $X \perp Y$ iff $I(X; Y) = 0$.

##### Independence Bound of Entropy
$$
H(X_1, \cdots X_n) = \sum_{k = 1}^n H(X_k | X_{< k}) \le \sum_{k = 1}^n H(X_k)
$$
with equality iff $\forall 1 \le k \le n: X_k \perp X_{<k}$ iff $\{X_1, \cdots, X_n\}$ is an independent family.

