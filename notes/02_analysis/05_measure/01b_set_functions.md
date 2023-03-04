#### Set Functions

##### Properties of nonnegative set functions

A function $\mu: \S \to [0, \infty]$ on $\S \subseteq \P(X)$ is

- **finitely additive** if for $A, (A_i)_{i = 1}^n \in \S$, and $A = +_i A_i$, then $\mu(+_iA_i) = \mu(A)$.
- **subtractive** if $A, B \in \S$ and $A - B \in \S$ and $\mu(B) \in \R$. Then $\mu(A - B) = \mu(A) - \mu(B)$.
  - $\mu$ is subtractive if $\mu$ is finitely additive.
- **countably additive** if for $A, (A_i)_{i = 1}^\infty \in \S$ and $A = +_i A_i$, $\mu(+_i A_i) = \mu(A)$.
- **countably subadditive** if for $A, (A_i)_{i = 1}^\infty \in \S$ and $A = \cup_i A_i$, $\mu(A) \le \sum_{i = 1}^\infty \mu(A_i)$.
  - Finitely additive + countably subadditive $\to$ countably additive.
- **monotone** if $A, B \in \S$ and $A \subseteq B$, then $\mu(A) \le \mu(B)$.
- **monotone from below** if for $A, (A_i)_{i = 1}^\infty \in \S$ and $A_i \uparrow A$, $\mu(A_i) \uparrow \mu(A)$.
- **monotone from above** if for $A, (A_i)_{i = 1}^\infty \in \S$ and $A_i \downarrow A$, $\mu(A_1) < \infty$, $\mu(A_i) \downarrow \mu(A)$.
- **$\sigma$-finite** on $\A \subseteq \S$ if some $(A_i)_{i = 1}^\infty \in \A$ and $\mu(A_i) < \infty$, and $\cup_i A_i = X$.
  - **Disjoint $\sigma$-finite** if $+_i A_i = X$.
- **finite** if $X \in \S$ and $\mu(X) < \infty$.

##### Measures

Suppose $\S$ is a **proto-ring** on $X$. A unsigned set function $\mu: \S \to [0, \infty]$ is called:

- a **proto-measure** if $\mu(\varnothing)=0$.
- a **finitely additive measure** if it is a proto-measure and finitely additive.
- a **measure** if it is a proto-measure and countably additive.

##### Set functions on semi-rings

Suppose $\S$ is a **semi-ring** on $X$. Suppose unsigned set function $\mu: \S \to [0, \infty]$.

- Suppose $\mu$ is finitely additive. Then $\mu$ is monotone and finitely subadditive.
- Suppose $\mu$ is finitely additive and countably subadditive. Then $\mu$ is countably additive.
  - Suppose $A, (A_i)^\infty_{i = 1} \in \S$, and $A = +_i A_i$. Then $\mu(A) \le \sum_{i} \mu(A_i)$.
  - Due to monotonicity, $\sum_{i = 1}^n \mu(A_i)\le \mu(A)$. Take limit $n \to \infty$. 
- Suppose $\mu$ is $\sigma$-finite on $\S$ and monotone. Then $\mu$ is disjoint $\sigma$-finite on $\S$.
- Suppose $\mu$ is countably additive, it is countably subadditive.

##### Series of measures

Suppose $(\mu_k)_{k = 1}^\infty$ are measures on proto-ring $\S$. Then $\sum_{k=1}^\infty \mu_k$ is a measure.

- $\sum \mu_k(\varnothing) = 0$.
- Suppose $\p{A_n} \subseteq \S$ where $A = +_n A_n$. $\sum \mu_k(A) = \sum_k \sum_n \mu_k(A_n) = \sum_k \mu_k(A)$.

##### Restriction of measures

Suppose $\mu: \A \to [0, \infty]$ is a (finitely additive) measure on $\pi$-system $\A$.

- Suppose $Y \in \A$. Then $\A|_Y:= \{A \cap Y: A \in \A\} \subseteq \A$ is a $\pi$-system on $Y$.
- Denote $\mu|_Y:= \mu|_{\A|_Y}$. It is a (finitely additive) measure on $\pi$-system $\A|_Y$.

#### Measure Spaces

##### Measures on $\sigma$-algebras

Suppose $\mu$ is a **measure** on $\sigma$-algebra $\S$. Then:

- $\mu$ is monotone.
- $\mu$ is countably subadditive.
- $\mu$ is monotone from above.
- $\mu$ is monotone from below.

##### Measure spaces

- Suppose $\mu$ is a measure on algebra $\A$ on $X$. $(X, \A, \mu)$ is called a **premeasure space**.
- Suppose $\mu$ is a measure on $\sigma$-algebra $\M$ on $X$. $(X, \M, \mu)$ is called a **measure space**.

##### Atomic measure space

Suppose $X$ is a set. And $\p{A_{\alpha}}_{\alpha \in I}$ where $X = +_\alpha A_\alpha$ is a set of **atoms**.

Consider the algebra generated $\mathcal B = \A(A_\alpha)_{\alpha \in I}$.

$\mathcal B$ is called the **atomic algebra** with **atoms** $A_\alpha$.

- $\mathcal B =\{\cup_{\alpha \in J} A_\alpha:J \subseteq I, \abs{J} \le \abs{\N}\}$.
- $\mathcal B$ is also a $\sigma$-abgebra. So $\sigma(A_{\alpha})_{\alpha \in I} = \A(A_\alpha)_{\alpha\in I}$.

$(X, \mathcal B)$ is called an **atomic measurable space**.

- Any measure $\mu$ on $\mathcal B$ is completely **determined** by $\mu\p{A_\alpha}$.

##### Concentrated measure

Suppose $(X, \M, \mu)$ is a measure space. $\mu$ is concentrated on $B \in \M$ if $\mu(X - B) = 0$.

#### Completeness of Measures

##### Null sets

If $(X, \M, \mu)$ is a measure space, a set $E \in \M$ such that $\mu(E) = 0$ is a **null set**. 

- If $P(x)$ is true in $X$ except for some null set, we say that it is true **almost everywhere**, or **for almost every** $x$.

##### Complete measure space

Suppose $(X, \M, \mu)$ is a measure space.

Suppose $\M$ contains all subsets of any null set with respect to $\mu$, $(X, \M, \mu)$ is a **complete** measure space.

##### Completion

Suppose $(X, \M, \mu)$ is a measure space.

- Suppose $\mathcal N$ is the set of all null sets in $\M$ with respect to $\mu$.
- Define the **completion** of $\M$ with respect to $\mu$ as $\widehat \M$:
  - $\widehat \M = \{E \cup F \mid E \in \M, N \in \mathcal N, F \subseteq N\}$.
  - $\widehat \M$ is the minimum $\sigma$-algebra containing $\M$ that is complete.
- The completion of $\mu$ is $\widehat \mu$. $\widehat \mu(E \cup F) := \mu(E)$ for $E \cup F \in \widehat \M$.
- $\widehat \mu$ is a well defined function on $\widehat \M$.
  - Suppose $A_1 \cup B_1 = A_2 \cup B_2$ where $A_1, A_2 \in \M$ and $B_1 \subseteq N_1$ and $B_2 \subseteq N_2$ where $N_1, N_2 \in \mathcal N$.
  - Then $A_1 \cup B_1 = A_2 \cup B_2 = (A_1 \cap A_2) \cup (B_1 \cup B_2) = A_0 \cup B_0$.
  - $\mu(A_0) \le \mu(A_i) \le \mu(A_0) + \mu(N_1 \cup N_2) = \mu(A_0)$. So $\mu(A_1) = \mu(A_2)$.
- Clearly $\widehat \mu$ is a measure.
- Then $(X, \widehat \M, \widehat \mu)$ is the completion of $(X, \M, \mu)$.

#### Outer Measures

> Outer measure can be defined given any proto-measure.
>
> The outer measurable sets together with the generated outer measure defines a **complete** measure space.

##### Outer measure

A function $\mu^*: \P(X) \to [0,\infty]$ is an **outer measure** on $X$ if:

- $\mu^*(\varnothing) = 0$.
- $\mu^*$ is monotone.
- $\mu^*$ is countably subadditive.

##### Outer measurable

Suppose $\mu^*$ is an **outer measure** on $X$. Set $A \in \P(X)$ is **outer measurable** if
$$
\forall B \in \P(X): \mu^*(B)=\mu^*(B \cap A)+\mu^*\left(B \cap A^{c}\right)
$$
Equivalently $A \in \P(X)$ is outer measurable if
$$
\forall B \in \P(X) \land \mu^*(B) < \infty: \mu^*(B)\ge\mu^*(B \cap A)+\mu^*\left(B \cap A^{c}\right)
$$

- When $\mu^*(B) = \infty$, the equation is always true.
- When $\mu^*(B) < \infty$, $\mu^*(B)\le \mu^*(B \cap A)+\mu^*\left(B \cap A^{c}\right)$ due to sub-additivity.

Let $\M_{\mu^*}$ be the set of all **outer measurable** sets in $\P(X)$.

- $\M_{\mu^*}$ contains all the subsets of any null sets.

Actually $(X, \M_{\mu^*}, \mu^*)$ is a **complete measure space**.

- First of all, $\M_{\mu^*}$ is a $\sigma$-algebra. 
  - $\varnothing \in \M_{\mu^*}$.
  - $\M_{\mu^*}$ is closed under complementation.
    - $\M_{\mu^*}$ is closed under union (and intersection, subtraction).
      - Suppose $A, B \in \M_{\mu^*}$. To show $A \cup B \in \M_{\mu^*}$.
      - Consider any $G \in \P(X)$. Consider the following Wenn Diagram:
        ![outer_wenn](images/outer_wenn.svg)
      - Just notice that $\mu(C_3) + \mu(C_4) = \mu(C_{34})$. And
        $$
        \mu(C_{123}) + \mu(C_4) \le \mu(C_{12}) + \mu(C_3) + \mu(C_4) = \mu(C_{12}) + \mu(C_{34}) = \mu(G)
        $$
  - $\M_{\mu^*}$ is closed under countable union.
    - Suppose $\p{E_i} \subseteq \M_{\mu^*}$ are disjoint, and $E = +_i E_i$.
    - Consider any $G \in \P(X)$.
    - Let $F_m = +_{i = 1}^m E_i \in \M_{\mu^*}$. Notice that
      $$
      \begin{aligned}
      \mu^*(G) & = \mu^*(G \cap F_n) + \mu^*(G \cap F_n^c) \ge \mu^*(G \cap F_n) + \mu^* (G \cap E^c)\\
      & = \sum_{i=1}^n \mu^*(G \cap E_i) + \mu^*(G \cap E^c)
      \end{aligned}
      $$
    - Take the limit $n \to \infty$ and using subadditivity: 
      $$
      \mu^*(G) \ge \sum_{i=1}^\infty \mu^*(G \cap E_i) + \mu^* (G \cap E^c) \ge \mu^*(G \cap E) + \mu^*(G \cap E^c)
      $$
- Also $\mu^*$ is a measure on $\M_{\mu^*}$.
  - $\mu^*(\varnothing) = 0$.
    - $\mu^*$ is finitely additive.
      - Suppose $A, B \in \M_{\mu^*}$. $\mu(A + B) = \mu(A) + \mu(B)$.
  - $\mu^*$ is countably additive.
    - Suppose $(E_i)_{i = 1}^\infty \in \M_{\mu^*}$ are disjoint. And $E = +_iE_i$.
      - By subadditivity $\mu^*(E) \le \sum_{i=1}^\infty \mu^*(E_i)$.
      - Notice that $\mu^*(E) \ge \mu^*(+_{i=1}^n E_i) = \sum_{i=1}^n \mu^*(E_i)$.
      - Now take limit $n \to \infty$.
