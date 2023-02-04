#### Conditional Probability

(**Conditional probability: over events**)

Suppose $(\Omega, \F, P)$ is a probability space. Let $A \in \F$ and $P(A) > 0$.

- Suppose $X \in \overline{\L}(\Omega \to \eR, P)$, then $E[X|A] := E(1_AX) / P(A)$.
- Suppose $B \in \F$, then $P(B|A) = E[1_B|A] = P(A \cap B)/P(A)$.
    - Denote $P_A(B) = P(B|A)$, then $P_A$ is a probability measure on $(\Omega, \F)$.
    - $P(B|A) = P(B)$ if and only if $A \perp B$.
- Suppose $(A_k)_{k = 1}^\infty \in \F$ and $\Omega = +_k A_k$. Then $E[X] = P(A_k)E[X|A_k]$.
- (**Bayes rule**) Suppose $A, B \in \F$, then $P(A|B)P(B) = P(A \cap B) = P(B|A)P(A)$.

(**Conditional probability: over values**)

Suppose $(\Omega, \F)$ and $(\Omega', \F')$ are measurable spaces. And $P$ is a probability measure on $\F$.

Suppose $X \in \L(\Omega \to \Omega', \F/\F')$ with distribution $P_X$ on $\F'$.

- Fix $A \in \F$, define finite measure $\lambda_A: \F' \to [0, 1]$ as $\lambda_A(B) = P(\{X \in B\} \cap A)$.
- Clearly $\lambda_A \ll P_X$ since $P_X(B) = 0 \implies P(\{X \in B\}) = 0$.
- By (**Radon-Nikodym**) there exists a unique $g_A \in L^1(\Omega'\to [0, \infty], P_X)$ such that $d \lambda_A = g_A dP_X$.
    - Notice that $\forall B \in \F': \lambda_A(B) \le P_X(B)$, therefore $g_A \in [0, 1]$, $P_X$ almost everywhere.

Define **conditional probability** $P(A|X = x) := g_A(x)$ for $A \in \F$.

It is the **unique** function in $L^1(\Omega' \to [0, \infty], P_X)$ such that
$$
\forall B \in \F': P(\{X \in B\} \cap A) = \int_{B} P(A|X = x) P_X(dx)
$$
(**Classical conditional probability**)

This definition of conditional probability is a generalization of the classical definition:

- Suppose $X \in \L(\Omega \to \Omega')$ is discrete with countably many values $(x_i)_{i = 1}^\infty$.
    - $P(A | X = x_i) P(X=x_i) = P(A, X = x_i)$ is the same in classical and new definition.
    - $P(A|X = x)$ can take any value when $x \notin (x_i)$.
    - In this case $P(\{X \in B\} \cap A) = \sum_{x_i \in B} P(A|X = x_i)P(X = x_i)$.
    
- Suppose $(\Omega, \F, P) = (\R^2, \B(\R^2), P_{XY})$. And $X, Y \in \L(\R^2 \to \R)$ with $X(x, y) = x$ and $Y(x, y) = y$. Suppose $P_{XY}$ has joint density $f(x, y) \in \L^1(\R^2 \to [0, \infty])$. And $\Omega' = \R$, $\F' = \B(\R)$.
    - Then $P_X$ has density $f(x) = \int_\R f(x, y) dy$.
    
    - Define $f(y | x) = f(x, y) / f(x)$ when $f(x) > 0$ and $f(y | x) = 0$ when $f(x) = 0$.
    
    - Notice that according to Fubini Theorem:
      $$
      \begin{aligned}
      P(\{X \in B\} \cap A) & = \iint_{x \in B;(x, y) \in A} f(x, y) dx dy = \iint 1_B(x) 1_A(x, y) f(x, y) dx dy\\
      & = \int_\R \left[ \int_\R 1_A(x, y) f(x, y)dy \right] 1_B(x) dx\\
      & = \int_\R \left[ \int_\R 1_A(x, y) f(y | x) dy\right] 1_B(x) f(x) dx\end{aligned}
      $$
    
    - Therefore for $A \in \F = \B(\R^2)$, $P(A|X = x) = \int_{[A]_x} f(y|x) dy$ is a version of the cond.pr.

#### Conditional Expectation

(**Conditional Expectation: over values**)

Suppose $(\Omega, \F)$ and $(\Omega', \F')$ are measurable spaces. And $P$ is a probability measure on $\F$.

Suppose $X \in \L(\Omega \to \Omega', \F / \F')$ with distribution $P_X$ on $\F'$. Suppose $Y \in \overline{\L}(\Omega \to \overline \R, P)$.

- Define **signed measure** $\lambda$ on $\F'$ as $\lambda(B) = \int_{X^{-1}B}Y dP$ for $B \in \F'$.
- Notice that $\lambda \ll P_X$.
    - If $P_X(B) = 0$, then $X^{-1}B$ is a $P$-null set. Therefore $\lambda(B) = 0$.
- By (**Radon-Nikodym**) there exists $g \in \overline{L}(\Omega' \to \eR, P_X)$ such that $d\lambda = g dP_X$.

Define **conditional expectation of $Y$ given $X = x$** as $E[Y|X = x] = [g(x)]$ for $x \in \Omega'$. It is the **unique** function in $\bar L(\Omega' \to \eR, P_X)$ such that
$$
\int_{X \in B} Y dP = \int_B E[Y|X = x] dP_X(x)
$$
- This definition is an extension of conditional probabilities over values.
    - Let $Y = 1_A$ for $A \in \F$. Then $E[1_A|X = x] = P(A|X = x)$.

(**Classical conditional expectation: over value**)

The conditional expectation extends the classical definitions:
- Suppose $X \in \L(\Omega \to \Omega')$ is discrete with countably many values $(x_i)_{i = 1}^\infty$.
    - When $E[Y] \in \R$, a version of $E[Y | X = x_i]$ would be $\int_{X = x_i} Y dP/ P(X = x_i)$.
    - The value of $E[Y|X=x]$ for $x \notin (x_i)$ does not matter.
    
- Suppose $(\Omega, \F, P) = (\R^2, \B(\R^2), P_{XY})$. And $X, Y \in \L(\R^2 \to \R)$ with $X(x, y) = x$ and $Y(x, y) = y$. Suppose $P_{XY}$ has joint density $f(x, y) \in \L^1(\R^2 \to [0, \infty])$. And $\Omega' = \R$, $\F' = \B(\R)$.
    - Define $f(x), f(x | y)$ as in classical definition.
    
    - When $y f(x, y) \in \L^1(\R^2 \to \eR)$, by Fubini:
      $$
      \int_{X \in B} Y dP = \iint_{x\in B} y dP_{XY}(x, y) = \iint_{x\in B} y f(x, y) dx dy = \int_{x \in B} f(x) \left[\int_\R y f(y | x) dy\right] dx
      $$
      
    - Then a version of $E[Y|X = x]$ would be $\int_\R y f(y|x) dy$.
    
    - The procedure here can also be applied to $q(Y)$.

(**Probability kernel and conditional expectation**)

Suppose $(X, \S)$ and $(Y, \T)$ are measurable spaces. $(\Omega, \F) = (X \times Y, \S \otimes \T)$.

- Suppose $P$ is a probability measure on $\S$ and $K(x, B)$ is a probability kernel from $\S$ to $\T$.
- Let $Q = P \times K$ be the iterated product of probability measure.
- Let $X(x, y) = x$ and $Y(x, y) = y$.
- A version of $Q(Y \in B|X = x)$ would be exactly the **kernel** $K(x, B)$.
    - Since $Q(X \in A, Y \in B) = Q(A \times B) = \int_A K(x, B) dP(x)$.
- Suppose $f \in \L(Y \to \overline \R)$ and $E[f(Y)]$ exists. A version of $E[f(Y) | X = x]$ is $\int_Y f(y) K(x ,dy)$.
    - Since $\int_{X \in A} f(Y) dQ = \int 1_A(x) f(y) dQ(x, y) = \iint 1_A(x) f(y) K(x, dy) P(dx)$.

(**Conditional expectation: over $\sigma$-algebra**)

Suppose $(\Omega, \F, P)$ is a probability space, $\G$ is a sub $\sigma$-algebra of $\F$. Suppose $Y \in \overline{\L}(\Omega \to \eR,\F, P)$.

- Define **signed measure** on $\G$ as $\lambda(C) = \int_C Y dP$. $\lambda \ll P$.
- By (**Radon-Nikodym**) there exists $g \in \overline{\L}(\Omega \to \eR, \G, P)$ where $d \lambda = g dP$.

Define **conditional expectation of $Y$ given $\G$** as $E[Y|\G] = g$. It is the **unique** function in $\bar L(\Omega \to \eR, \G, P)$ such that
$$
\forall C \in \G: \int_C Y dP = \int_{C} E[Y|\G] dP
$$
(**Conditional expectation: over random variable**)

Suppose $(\Omega, \F, P)$ is a probability space, $\G$ is a sub $\sigma$-algebra of $\F$.

Suppose $Y \in \overline{\L}(\Omega \to \eR, \F, P)$, $X \in \L(\Omega \to \Omega', \F / \F')$ with distribution $P_X$ on $\F'$.

Define **conditional expectation of $Y$ given $X$** as $E[Y|X] = E[Y|\sigma(X)]$.

(**Conditional probability: over $\sigma$-algebra**)

Suppose $(\Omega, \F, P)$ is a probability space, $\G$ is a sub $\sigma$-algebra of $\F$. Suppose $B \in \F$.

- Define probability measure on $\G$ as $\lambda(C) = P(C \cap B)$ for $C \in \G$. $\lambda \ll P$.
- By (**Radon-Nikodym**) there exists $g \in \L^1(\Omega \to [0, 1], \G, P)$ where $d\lambda = g dP$.

Define **conditional probability of $B$ over $\G$** as $P(B|\G) = [g]$. It is the unique function in $L^1(\Omega \to \eR)$ such that
$$
\forall C \in \G: P(C \cap B) = \int_C P(B|\G) dP
$$
Clearly $P(B|\G) = E[1_B|\G]$ by definition.

(**Conditional expectation: Link between two forms**)

Suppose $(\Omega, \F)$ and $(\Omega', \F')$ are measurable spaces. And $P$ is a probability measure on $\F$. Suppose $X \in \L(\Omega \to \Omega', \F/\F')$ and $Y \in \overline{\L}(\Omega \to \eR, P)$.

Then $E[Y|X](\omega) = E[Y|\sigma(X)](\omega) = E[Y|X = X(\omega)]$.
- Clearly $E[Y | X = X(\omega)] \in \overline L(\Omega \to \eR, \sigma(X), P)$.

- For any $A \in \F'$, $X^{-1} A \in \sigma(X)$.
  $$
  \begin{aligned}
  \int_{X^{-1}A} E[Y|X = X(\omega)] dP & = \int_{\Omega} 1_{A}(X(\omega)) E[Y|X = X(\omega)] dP\\
  & = \int_A E[Y|X = x] dP_X(x) = \int_{X^{-1} A} Y dP
  \end{aligned}
  $$

$E[Y|X = x] = E[Y|X]\circ X^{-1}(x)$.
- Consider the push-forward decomposition of $E[Y|X]$ by $X$. $E[Y|X](\omega) = \varphi \circ X(\omega)$.
    $$
    \forall A \in \F': \int_{A} \varphi(x) \dd P_X(x) = \int_{X^{-1}[A]} \varphi(X) \dd P = \int_{X^{-1}[A]} Y \dd P
    $$

Suppose $\G$ is a sub-$\sigma$-algebra of $\F$. Let $I \in \L(\Omega \to \Omega, \F/\G)$ be an identity map.
- $E[Y|\G] = E[Y|I] = E[Y|\sigma(I)]$.

