#### Field Extensions

##### Field extensions

The pair of fields $(F, E)$ is a **field extension** if $F \leq E$, denoted by $E/F$.

- $E$ is called an **extension field** of $F$.

The sequence of fields $(F_1, F_2, \ldots, F_n)$ is a **tower of fields** if $F_1 \le \cdots \le F_n$, denoted by $F_n/\cdots /F_1$.

##### Degree of field extension $[E:F]$

Consider field extension $E/F$. $E$ is a $F$-vector space.

- The **degree of field extension** $E/F$ is the dimension of the vector space. Denoted $[E:F]$.
- Extensions of finite degree are **finite extensions**, otherwise are **infinite extensions**.

$[E: F]=1$ if and only if $E=F$.
- Suppose $E = F$, clearly $F$ is a one-dimensional vector space over $F$ itself.
- Suppose $[E:F] = 1$, so $E$ is a one-dimensional vector space. $\{1\}$ is a basis, so $E = F$.

##### Multiplicativity of extension degree

Consider the tower of fields $K / E / F$. $[K:F] = [K:E][E:F]$.

- Suppose $(e_i)_{i \in I}$ is a basis of $E/F$. And $(k_j)_{j \in J}$ is a basis of $K/E$.
- Consider the list $(a_{ij})_{(i, j) \in I \times J} = (e_ik_j)$.
  - Clearly $(a_{ij})$ spans $K/F$.
  - And $(a_{ij})$ is clearly linearly independent.

- So $(a_{ij})$ is a basis of $K/F$.

##### Kronecker's Theorem

Let $F$ be a **field** and let $f(x)$ be a **non-constant** polynomial in $F[x]$.

Then there exists an extension field $E$ of $F$ and an $\alpha \in E$ such that $f(\alpha)=0$.

- Since $F[x]$ is a PID, each $f(x) \in F[x]$ are products of irreducibles.
- We only need to show that all **non-constant irreducibles** have zeros in some extension field.

Suppose $p$ is a irreducible in $F[x]$. There exists extension $E/F$ where $\alpha \in E$ and $f(\alpha) = 0$.

- Since $p$ is irreducible, $\p p$ is maximal. $F[x]/\p p$ is a field.

- Define $E = F[x]/\p p$.

- Define $\phi: F \to E$ as $\phi(a) = a + \p p$. And $\varphi$ is its polynomial extension.

  - $\phi$ and $\varphi$ are injective.
  - Therefore $F \simeq \phi[F] < E$, and $F[x] \simeq \varphi[F[x]] < E[x]$.

- Let $\alpha = x + \p p$, then
  $$
  \varphi(p)(x + \p p) = \sum_{i=0}^n (a_i + \p p) (x^p + \p p) = p + \p p = 0 + \p p
  $$

Consider the structure of $E = F[x] / \p p$. $[E:\phi[F]] = [E:F] = \deg p$.

- For any element $h(x) + \p p \in E$.
- Apply division algorithm to $h(x) / p(x)$, $h(x) = a(x) p(x) + r(x)$.
- So $h(x) + \p p = r(x) + \p p$.
- Clearly $\c{x^i + \p p: 0 \le i < n}$ is a basis of $E$ over $\phi[F]$.

Further suppose $F$ is a finite field. Then $|E| = |F|^n$.

##### Algebraic and transcendental

Consider field extension $E/F$.

- $\alpha \in E$ is **algebraic** over $F$ if $\alpha$ is the root of some polynomial in $F[x]$.
- Otherwise $\alpha \in E$ is transcendental over $F$.

Field extension $E/F$ is **algebraic**, or $E$ is an algebraic extension of $F$ if all elements in $E$ are algebraic over $F$.

Otherwise $E/F$ is **transcendental**, or $E$ is a transcendental extension of $F$.

##### Minimal polynomial

Consider field extension $E/F$, where $\alpha \in E$ is algebraic over $F$.

- Consider evaluation ring homomorphism $\phi: F[x] \to E$ where $\phi(x) = \alpha$.
- Suppose $\ker \phi = \p p$ for some $p \in F[x]$.
  - $\alpha$ is algebraic if and only if $p \neq 0$.
- $p(x)$ is irreducible in $F[x]$.
  - Suppose $p(x) = s(x) t(x)$ in $F[x]$ where $s, t$ are not constant.
  - $p(\alpha) = s(\alpha) t(\alpha)$. So $s \in \p p$. But all polynomials in $\p p$ can not have lower degree. Contradiction!

- The monic generator of $\p p$ is called **irreducible polynomial** for $\alpha$ over $F$ or the **minimal** **polynomial** for $\alpha$ over $F$.
  - Denoted as $\operatorname{irr}(\alpha, F)$.
  - The function $\operatorname{irr}(\alpha, F)$ is **not defined** for trancendental elements in $E$.

- Define $\deg(\alpha, F):= \deg p(x)$ as the **degree** of $\alpha$ over $F$.

It is easy to show that the following definition of $\irr(\alpha, F) \in F[x]$ are also equivalent:

1. $p$ is a monic irreducible where $p(\alpha) = 0$.
2. $p$ is a monic of minimal degree in $\ker \phi$.
3. $p$ is a monic, and $\forall f \in F[x]: f(\alpha) = 0 \to p \mid f$.

##### Ring and field adjunctions

Consider field extension $E/F$. Suppose $S \subseteq E$.

- $F[S]$ is the subdomain that is the **intersection** of all **subrings** of $E$ containing $F$ and $S$.
  - Suppose $S = \c{\alpha}$, $F[\alpha] = F[S] = \c{f(\alpha): f\in F[x]}$.
  - $F[S]$ contains elements $f(\alpha_1, \ldots, \alpha_n)$ where $\alpha_i \in S$ and $f \in F[x_1, \ldots, x_n]$, for $n \ge 1$.

- $F(S)$ is the subfield that is the **intersection** of all **subfields** of $E$ containing $F \cup S$.
  - Suppose $S = \c{\alpha}$, $F(\alpha) = F[\alpha]' = \c{f(\alpha) / g(\alpha): f, g \in F[x], g \neq 0}$.
  - $F(S)$ is the fraction field of $F[S]$.

- Clearly $F[S] \subseteq F(S)$. And $F(S)$ is a quotient field of $F[S]$.

##### Simple algebraic extensions

Consider field extension $E/F$. Suppose $\alpha \in E$.

Consider evaluation homomorphism $\phi: F[x] \to E$ where $\phi(x) = \alpha$.

- $\phi[F[x]] = F[\alpha]$.

Suppose $\alpha \in E$ is **algebraic** over $F$.

- Let $p = \irr (\alpha, F)$. $\ker \phi = \p p$ is maximal. And $F[x] / \p p$ is a field.
- Now apply the fundamental theorem of ring homomorphisms.
  - Decompose $\phi: F[x] \to E$  into $\phi = \gamma \circ \mu$.
  - $\gamma: F[x] \to F[x] / \p p$ by $f(x) \mapsto f(x) + \p p$.
  - $\mu: F[x] / \p p \to F[\alpha]$ is an isomorphism.
- Consider isomorphism $\mu$.
  - $F[\alpha] \simeq F[x] / \p p$ is a field.
  - $[F[\alpha] : F] = \deg p = n$.
  - A basis of $F[\alpha]$ over $F$ is $\c{1, \alpha, \ldots, \alpha^{n-1}}$.
  - We can write $\beta \in F[\alpha]$ as $g(\alpha)$ for $g \in F[x]$ with $\deg g(x) < n$.

Suppose $\beta \in F[\alpha]$ is algebraic over $F$. Consider the tower of fields $F[\alpha] / F[\beta] / F$.

- $F[\beta]$ is a **subspace** of $F[\alpha]$, so $\deg(\beta, F) = \dim F[\beta]\le \dim F[\alpha] = \deg(\alpha, F)$
- $\deg(\alpha, F) = [F[\alpha]: F[\beta]] \deg (\beta, F)$. So $\deg(\beta, F) \mid \deg(\alpha, F)$.
  - Since $[F[\alpha] : F] = [F[\alpha]:F[\beta]][F[\beta]: F]$.

Arithmetic in $F[\alpha]$ can be done based on $F[\alpha] \simeq F[x] / \p {p(x)}$.

- Multiplication $r(\alpha) = g(\alpha)h(\alpha)$.
  - Compute division $g(x) h(x) = q(x)p(x) + r(x)$ in $F[x]$.
  - Then we have $r(\alpha) = g(\alpha)h(\alpha)$ in $F[\alpha]$.
- Find inverse of $f(\alpha) \in F[\alpha]$.
  - Use extended Euclidean algorithm to solve for $s(x) f(x) + t(x) p(x) = 1$.
  - Then we have $s(\alpha)f(\alpha) = 1$.

##### Simple transcendental extensions

Continue above discussion. Suppose $\alpha \in E$ is transcendental over $F$.

- Then $\ker \phi = (0)$.
- By fundamental theorem of ring homomorphisms, $F[x] \simeq F[x]/(0) \simeq \phi[F[x]] = F[\alpha]$.
- So $F(x) \simeq F(\alpha)$, as isomorphic domain have isomorphic quotient fields.

##### Finite field extensions are algebraic

Consider field extension $E/F$ where $[E:F] = n \in \N$. Then $E/F$ is algebraic.

- We can construct a basis $\alpha_1, \cdots, \alpha_n$. Clearly we have $E = F(\alpha_1, \cdots, \alpha_n)$.
- For any $\alpha \in E$, the list $1, \alpha, \cdots, \alpha^{n}$ cannot be linearly independent elements.
- So there exist nonzero sequence $(a_{i})_{i=0}^n$ such that $a_{n} \alpha^{n}+\cdots+a_{1} \alpha+a_{0}=0$.
- Then $f(x)=a_{n} x^{n}+\cdots+a_{1} x+a_{0}$ is a nonzero polynomial in $F[x]$ $\operatorname{and} f(\alpha)=0$. Therefore, $\alpha$ is algebraic over $F$.

##### Field extension $\C / \R$

Consider $p(x) = x^2 + 1$, is irreducible in $\mathbb R[x]$, so $(x^2 + 1)$ is maximal, consider field $\C = \mathbb R[x] / (x^2 + 1)$.

- Relabel $a\in \mathbb R, a + (x^2 + 1) = a$. So $\mathbb R$ is a subfield of $\C$.
- $\{1, i\}$ is a basis of $\C$ over $\R$.
- Consider $i = x + (x^2 + 1)$. Notice that $i^2 = -1$. This is the imaginary unit.

##### Example: field extension $\Z_2[\alpha] / \Z_2$, $x^2 + x + 1 = \irr(\alpha, \Z_2)$.

We demonstrate the extension of a finite field $\Z_2$ with $p(x) = x^2 + x + 1 \in \Z_2[x]$.

- $x^2 + x + 1$ is an irreducible in $\mathbb Z_2[x]$, since it does not have zeros in $\{0, 1\} = \mathbb Z_2$.

- There is guaranteed to be a field $E$ that extends $\mathbb Z_2$, such that there is a zero $\alpha$ of $x^2 + x + 1$.

- We know $\operatorname{irr}(\alpha, \mathbb Z_2)$ is just $p(x) = x^2 + x + 1$.

- Note that
  $$
  \Z_2(\alpha) = \Z_2[\alpha] = \c{0 + 0\alpha, 0 + 1\alpha, 1 + 0\alpha, 1 + 1\alpha}
  $$

- Finally we can construct the arithmetic table of addition and multiplication:

$$
\begin{aligned}
&\begin{array}{c||c|c|c|c}
+ & 0 & 1 & \alpha & 1+\alpha \\
\hline 0 & 0 & 1 & \alpha & 1+\alpha \\
\hline 1 & {1} & 0 & 1+\alpha & \alpha \\
\hline \alpha & \alpha & 1+\alpha & 0 & 1 \\
\hline 1+\alpha & 1+\alpha & \alpha & 1 & 0
\end{array}\quad
&\begin{array}{c||c|c|c|c} 
\cdot& 0 & 1 & \alpha & 1+\alpha \\
\hline 0 & \quad0\quad & 0 & 0 & 0 \\
\hline 1 & 0 & 1 & \alpha & 1+\alpha \\
\hline \alpha & 0 & \alpha & 1+\alpha & 1 \\
\hline 1+\alpha & 0 & 1+\alpha & 1 & \alpha
\end{array}
\end{aligned}
$$

