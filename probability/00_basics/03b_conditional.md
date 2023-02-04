(**Properties of conditional expectation**)

Suppose $(\Omega, \F, P)$ is a probability space. Suppose $Y, (Y_n)_{n = 1}^\infty \in \overline{\L}(\Omega \to \eR, \F, P)$, $X \in \L(\Omega \to \Omega', \F/\F')$.

Suppose $\G < \F$ is a $\sigma$-algebra.

**Comparisons** and **limits** should be interpreted as $P$-a.e. for $E[Y|\G]$, or $P_X$-a.e. for $E[Y|X = x]$ if not otherwise stated.

- (**Constant**) Suppose $Y = k$ $P$-a.e. then

  - $E[Y|\G] = k$.
  - $E[Y|X = x] = k$.

- (**Monotone**) Suppose $Y_1 \le Y_2$ $P$.a.e. then

  - $E[Y_1 | \G] \le E[Y_2 | \G]$.
  - $E[Y_1|X = x] \le E[Y_2|X = x]$.

- (**Triangle**) Since $-|Y| \le Y \le |Y|$. The following directly follows from (**Monotone**).

  - $|E[Y | \G]| \le E[\abs{Y}| \G]$.
  - $\abs{E[Y|X = x]} \le E[\abs{Y}|X = x]$.

- (**Linearity**)

  - For $a \in \R$, $aE[Y|\G] = E[aY|\G]$ and $aE[Y|X=x] = E[aY|X=x]$.
  - $E[Y_1 | \G] + E[Y_2|\G] = E[Y_1 + Y_2|\G]$.
    - requires $E[Y_1] + E[Y_2]$ to be well defined, and $Y_1+Y_2$ a.e. well defined.
    - Recall the additivity of integrals in $\overline{\L}(\Omega \to \eR, P)$.
  - $E[Y_1|X = x] + E[Y_2 | X = x] = E[Y_1 + Y_2|X = x]$
    - requires $E[Y_1] + E[Y_2]$ to be well defined, and $Y_1 + Y_2$ a.e. well defined.

- (**MCT**) Suppose $(Y_n)_{n = 1}^\infty \in \L(\Omega \to [0, \infty])$. And $Y_n \uparrow Y$ $P$.a.e.

  - $E[Y_n | \G] \uparrow E[Y | \G]$.
  - $E[Y_n | X = x] \uparrow E[Y|X = x]$.

- (**Countably additive**) Suppose $(B_n)_{n = 1}^\infty \in \F$ are disjoint.

  - $\sum_n P(B_n | \G) = P(+_n B_n|\G)$.
  - $\sum_n P(B_n | X = x) = P(+_n B_n |X = x)$.
  - These directly follows from (**MCT**).
  - So $P(\cdot |\G)$ and $P(\cdot |X = x)$ are **measures** on $\F$.

- (**Tower law**)

  - $E[E[Y|\G]] = E[Y]$.
  - $E[E[Y|X = X(\omega)]] = E[Y(\omega)]$.

- (**DCT**) Suppose $Z \in \L^1(\Omega \to [0, \infty], P)$ and $|Y_n| \le Z$ and $Y_n \to Y$ $P$.a.e.

  - $E[Y_n | \G] \to E[Y|\G]$.
  - $E[Y_n | X = x] \to E[Y|X = x]$.

- (**MCT II**) ==TODO== Suppose $Z \in \L^1(\Omega \to \eR, P)$ and $Y, (Y_n)_{n = 1}^\infty \in \overline{\L}(\Omega \to \eR, P)$. $Z \le Y_n$.

  - $Y_n \uparrow Y$ then $E[Y_n | \G] \uparrow E[Y|\G]$.
  - $Y_n \uparrow Y$ then $E[Y_n | X = x] \uparrow E[Y | X = x]$.

- (**Fatou II**) ==TODO== Suppose $Z \in \L^1(\Omega \to \eR, P)$ and $Y, (Y_n)_{n = 1}^\infty \in \overline{\L}(\Omega \to \eR, P)$. $Z \le Y_n$.

  - $E[\liminf_n Y_n | \G] \le \liminf_n E[Y_n | \G]$.
  - $E[\liminf_n Y_n | X = x] \le \liminf_n E[Y_n | X = x]$.

- (**Boundary cases**) Let $\G = \{\varnothing, \Omega\}$.

  - $E[Y|\G] = E[Y]$, $E[Y|\F] = Y$.

- (**Atomic sets**) Suppose $B \in \G$ is atomic. $1_BE[Y|\G] = 1_BE[Y|B]$.

- (**Atomic algebra**) Suppose $(B_n)_{n = 1}^\infty \in \F$ and $\Omega = +_n B_n$ and $P(B_n) > 0$. $\G = \sigma(B_n)_{n = 1}^\infty$.

  - $E[Y|\G] = \sum_{n = 1}^\infty 1_{B_n}E[Y|B_n]$.

- (**Smoothing**) Suppose $\G_1 \subset \G_2$ are both sub-$\sigma$-algebras.

  - $E[E[Y|\G_1]|\G_2] = E[E[Y|\G_2]|\G_1] = E[Y|\G_1]$ (coarse one wins).

- (**Product: over fields**) Suppose $Z \in \L(\Omega \to \eR, \G)$ and $Y, YZ$ are integrable. Then $E[YZ|\G] = ZE[Y|\G]$.

  - Suppose $B \in \G$ and $Z = 1_B$. The result is true.
    $$
    \forall C \in \G: \int_C 1_B Y \dd P = \int_C 1_B E[Y|\G]\dd P = \int_{C \cap B} E[Y | \G] \dd P
    $$

  - Suppose $(B_j)_{j=1}^n \in \G$ and $Z = \sum_{j = 1}^n z_j 1_{B_j}$ and $(z_j) \in \R$.

    - Results follows from additivity.

  - Suppose $Z \in \L(\Omega \to \eR, \G)$. The result is true.

    - There exists $(Z_n)_{n=1}^\infty \in S(\Omega \to \R, \G)$ and $|Z_n| \uparrow |Z|$.
    - $E[YZ_n|\G] = Z_n E[Y|\G]$. By previous result.
    - $E[YZ_n|\G] \to E[YZ|\G]$.
      - $YZ_n \to YZ$ dominated by $|YZ|$.
      - So $E[YZ_n|\G] \to E[YZ|\G]$ by (**DCT**).
    - $Z_nE[Y|\G] \to ZE[Y|\G]$.
      - $|Y|$ is integrable, so $E[Y|\G]$ is **finite** $P$.a.e.

  - Let $Y = 1$ then $Z = E[Z|\G]$ when $Z$ is integrable.

- (**Product: over values**) Suppose $f \in \L(\Omega' \to \eR, \F')$ and $Y, Yf(X)$ are integrable. Then $E[Yf(X)|X = x] = f(x)E[Y|X = x]$.

  - Suppose $B \in \F'$ and $f = 1_B$. The result is true.
    $$
    \int_{X^{-1}[A]} Y f(X) \dd P = \int_{X^{-1}[A \cap B]} Y \dd P = \int_{A} 1_B(x) E[Y|X=x]\dd P_X(x)
    $$

  - Extension to simple and any measurable function is similar.

  - Let $Y = 1$, then $E[f(X)|X = x] = f(x)$ when $f(X)$ is integrable.

- (**Independence**)

  - Suppose $Y \perp \G$, then $E[Y|\G] = E[Y]$.
    - Suppose $B \in \F$ and $Y = 1_B$ is an indicator. $E[1_B | \G] = E[1_B]$.
      - $\forall C \in \G: \int_C Y dP = P(C \cap B) = P(C)P(B) = \int_C E[Y] dP$.
    - Suppose $(B_j) \in \G$ and $Y = \sum_{j = 1}^n a_j 1_{B_j}$ and $(a_j) \in \R$.
      - The result follows by additivity.
    - Suppose $Y \in \L(\Omega \to [ 0, \infty])$. $E[Y|\G] = E[Y]$.
      - Let $(Y_n) \in \L(\Omega \to [0, \infty])$ and $Y_n \uparrow Y$. For a fixed $C \in \G$.
      - $\int_C E[Y] dP = P(C) E[Y]$. And
      - $\int_C Y dP = \lim_n \int_C Y_n dP = \lim_n \int_C E[Y_n] dP = P(C)E[Y]$.
    - Suppose $Y \in \overline{\L}(\Omega \to \eR, P)$. $E[Y|\G] = E[Y]$.
      - $E[Y^+|\G] = E[Y^+]$ and $E[Y^-|\G] = E[Y^-]$.
      - Since $E[Y^+] + E[Y^-]$ is well defined, add left and right together.
  - Suppose $Y \perp X$, then $E[Y|X] = E[Y]$. Directly follows above.
  - Suppose $Y \perp X$, then $E[Y|X = x] = E[Y]$.
    - Suppose $B \in \F$ and $Y = 1_B$ is an indicator. $E[1_B|X= x] = E[1_B]$.
      - $\forall A\in \F': \int_A E[1_B]dP_X = P(X \in A)P(B) = P(\{X \in A\} \cap B) = \int_{X \in A} 1_B dP$
    - The rest proceeds in the same as above.

- (**Independent substitution**) Suppose $X \in \L(\Omega \to \Omega', \F / \F')$ and $Y \in \L(\Omega \to \Omega'', \F/\F'')$. And $\phi \in \L(\Omega' \times \Omega'' \to \eR, \F' \otimes \F'')$. And $X \perp Y$.

  - Suppose Fubini's Theorem is applicable, e.g. $\phi(X, Y) \in \L^1(\Omega \to \eR, \F, P)$.

  - For $y \in \Omega''$, $E[\phi(X, Y)|Y = y] = E[\phi(X, y)]$. Consider $\forall A \in \F''$.
    $$
    \begin{aligned}
    \int_A E[\phi(X, y)] \dd P_Y(y) 
    & = \int_{\Omega''} \s{\int_{\Omega'} \phi(x, y) \dd P_X(x)} 1_{A}(y) \dd P_Y(y)\\
    & = \iint_{\Omega'\times \Omega''} 1_A(y)\phi(x, y) \dd (P_X \times P_Y)(x , y)
    \\
    &= \int_{Y \in A}\phi(X, Y) dP = \int_{A} E[\phi(X, Y)|Y = y]\dd P_Y(y)
    \\
    \end{aligned}
    $$

- (**Projection in L2**) Suppose $V= L^2(\Omega \to \eR, \F, P)$ a Hilbert space.

  - $U = L^2(\Omega\to \eR, \G, P)$ is a closed subspace of $V$.
  - Suppose $Y \in V$ then $E[Y|\G] = P_U Y$.

- (**Jensen**) Suppose $I \subseteq \R$ is a open interval and $g: I \to \R$ is convex. And $Y(\omega) \in I$. Suppose $E[Y]$ is finite. If $\H \le \F$, then $E[g(Y) | \H] \ge g \circ E[Y | \H]$.

  - Clearly $E[Y | \H] \in I$. Thus $g(E[Y|\H])$ is well defined.
  - Suppose $g(y) = \sup_n (a_n y + b_n)$ for $y \in I$. So $\forall n \ge 1: g(Y) \ge a_n Y + b_n$.
  - $E[g(Y) | \H] \ge a_n  E[Y| \H] + b_n$. So $E[g(Y) | \H] \ge g(E[Y| \H])$.
  - (Ash) The condition may be generalized to $E[Y]$ and $E[g(Y)]$ exists, and $E[X | \H] \in I$.

(**Conditional independence**)

Suppose $(\Omega, \F, P)$ is a probability space. Suppose $\G \subseteq \F$ is a sub-$\sigma$-algebra. Suppose $\mathscr A$ is a set of families of events in $\F$.

- $\mathscr A$ is **(conditionally) independent given** $\G$ if for $\A_1 ,\ldots, \A_n \in \mathscr A$, and any $A_k \in \A_k$, $P(\cap A_k | \G) = \prod P(A_k | \G)$ almost surely.
  - Replace $\A \in \mathscr A$ in following ways does not alter conditional independence of $\mathscr A$.
    - Replace $\A$ with $\{A^c : A \in \A\} \cup \A$.
    - Replace $\A$ with $\{+_k B_k: (B_k)_{k \in I \subseteq \N} \in \A\} \cup \A$.
    - Replace $\pi$-system $\A$ with $\sigma(\A)$ and vice versa.
- $\mathscr A$ is **(conditionally) independent given $\G$** if and only if all subsets of $\mathscr A$ are cond. indep.
- $\mathscr A$ is **(conditionally) independent given $\G$**, $(\mathscr A_k)_{k \in K}$ is a partition of $\mathscr A$. Let $\mathcal B_k = \bigcup \mathscr A_k$ and $\mathscr B = \{\mathcal B_k\}_{k \in K}$. Then $\mathscr B$ is **(conditionally) independent given** $\G$.

Concept of conditional independence is extended to random variables:

- $\X = (X_i)_{i \in I}$ is **(conditionally) independent given $\G$** if $\mathscr A = (\sigma(X_i))_{i \in I}$ is indep. given $\G$.
  - Suppose $X_i \in \L(\Omega \to \Omega_i, \F / \F_i)$. And $\E_i$ is a $\pi$-generator of $\F_i$.
    - Replace $X_i \in \X$ with $f \circ X_i$ where $f\in \L(\Omega_i \to \Omega_i')$ keeps $\X$ indep. given $\G$.
    - $X_i^{-1} \E_i$ is a $\pi$-generator of $\sigma(X_i)$.
    - $\X$ is independent given $\G$ iff $(X_i^{-1}\E_i)_{i \in I}$ is independent given $\G$.
- By saying $\mathscr A$ or $\mathcal X$ is conditionally independent given $Y \in \L(\Omega \to \Omega')$ we mean $\G = \sigma(Y)$.
- $\X = (X_i)_{i\in I}$ is **(conditionally) independent given** $\G$. Let $(\X_k)_{k \in K}$ be a partition of $\X$. Then $\mathscr A = (\sigma(\X_k))_{k \in K}$ is **(conditionally) independent given** $\G$.

