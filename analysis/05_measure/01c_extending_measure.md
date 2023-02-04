#### Measure Extensions and Uniqueness

> Suppose $\mu$ is a (c.f. finitely additive) measure on semi-ring $\S$.
>
> - $\overline \mu$ is the unique (c.f. finitely additive) measure extension on $\overline \S$.
>
> Suppose $\mu$ is a measure on semi-ring $\S$.
>
> - $\widetilde \mu$ is the unique measure extension on $\widetilde \S$.
>
> Measures that agree on a $\pi$-system $\P$ and $\sigma$-finite on the system, also agree on $\sigma(\P)$.

(**Extending finitely additive measures, semi-ring $\to$ ring**)

Suppose $\mu$ is a **finitely additive** measure on semi-ring $\S$.

Define $\overline \mu: \overline \S \to [0, \infty]$ for disjoint $\p{S_i}_{i=1}^n \subseteq \S$ as
$$
\overline \mu\p{+_{i=1}^n S_i} := \sum_{i=1}^n \mu(S_i)
$$
$\overline \mu$ is the **unique finitely additive measure** extending $\mu$ on $\overline \S$.

- $\overline \mu$ is a **well-defined** function:
  - Suppose $+^n_{j = 1} T_j = +^m_{i = 1} S_i$ where $\p{T_j}, \p{S_i} \subseteq \S$.
  - Consider $+_{i, j} S_i \cap T_j$.
  - Then $\overline \mu(+_{i, j}S_i \cap T_j) = \sum_{i,j}\mu(S_i \cap T_j) = \overline \mu(+_i S_i) = \overline \mu(+_j T_j)$.
- $\overline \mu(\varnothing) = 0$.
- $\overline \mu$ is **finitely additive**:
  - Suppose $A, (B_i)_{i = 1}^n \in \overline \S$, and that $A = +_i B_i$.
  - Suppose $B_i = +^{n_i}_{j = 1} S_{i, j}$ where $S_{i, j} \in \S$.
  - Then $\overline{\mu}(A)=\sum_{i, j} \mu\left(S_{i, j}\right)=\sum_{i} \overline{\mu}\left(B_{i}\right)$.

(**Extending measures, semi-ring $\to$ ring**)

Suppose $\mu$ is a **measure** on semi-ring $\S$.

Define $\overline \mu: \overline \S \to [0, \infty]$ for disjoint $\p{S_i}_{i=1}^n \subseteq \S$ as
$$
\overline \mu\p{+_{i=1}^n S_i} := \sum_{i=1}^n \mu(S_i)
$$
Then $\overline \mu$ is the **unique measure extending** $\mu$ on $\overline \S$:

- $\overline \mu$ is countably additive on $\overline \S$.
  - Suppose $A, (B_i)_{i = 1}^\infty \in \overline \S$ and $A = +_i B_i$.
  - $\overline \mu(A) \le \sum_{i} \overline \mu(B_i)$:

    - Suppose $B_i = +_{j = 1}^{n_i} S_{i, j}$ where $S_{i, j} \in \S$.
    - Suppose $A = +_{k = 1}^{m_i} T_k$ where $T_k \in \S$. And $T_k = +_i(T_k \cap B_i)$.
    - Then $\overline \mu(A) = \sum_{k} \mu(T_k) \le \sum_i \sum_k \mu(T_k \cap B_i) = \sum_i \mu(B_i)$.
  - $\overline \mu(A) \ge \sum_{i} \overline \mu(B_i)$:

    - For $n \ge 1$, define $A_n:= +_{i = 1}^n \in \overline \S$.
    - $\overline{\mu}(A) \geq \overline \mu(A_n) = \sum_{i=1}^n\overline{\mu}(B_{i})$.
    - Take limit, then $\overline \mu(A) \ge \sum_i \overline \mu(B_i)$.
  - So $\overline \mu(A) = \sum_i \overline \mu(B_i)$.

(**Extending measures, semi-ring $\to$ $\sigma$-ring**)

Suppose $\mu$ is a **measure** on semi-ring $\S$.

Define $\widetilde \mu: \widetilde \S \to [0, \infty]$ for disjoint $\p{S_i}_{i=1}^\infty \subseteq \S$ as
$$
\widetilde \mu(+_{i=1}^\infty S_i) = \sum_{i = 1}^\infty \mu(S_i)
$$
Then $\widetilde \mu$ is the **unique measure extending** $\mu$ on $\widetilde \S$.

- $\widetilde \mu$ is a well defined function:
  - Suppose $+^\infty_{j = 1} T_j = +^\infty_{i = 1} S_i$. For $S_i, T_j \in \S$.
  - Consider $+_{i, j} S_i \cap T_j$.
  - Then $\widetilde \mu(+_{i, j}S_i \cap T_j) = \sum_{i,j}\mu(S_i \cap T_j) = \widetilde \mu(+_i S_i) = \widetilde \mu(+_j T_j)$.
- $\widetilde\mu(\varnothing) = 0$.
- $\widetilde \mu$ is countably additive:
  - Suppose $A, (B_i)_{i = 1}^\infty \in \widetilde \S$, and that $A = +_i B_i$.
  - Suppose $B_i = +^\infty_{j = 1} S_{i, j}$ where $S_{i, j} \in \S$.
  - Then $\widetilde{\mu}(A)=\sum_{i, j} \mu(S_{i, j})=\sum_{i} \widetilde{\mu}(B_{i})$.

(**Measures that agree on $\pi$-system**)

Suppose $X$ is a set.

- Suppose $(X, \F_1, \nu_1)$ and $(X, \F_2, \nu_2)$ are measure spaces.
- Suppose $\nu_1$ and $\nu_2$ agree on $\pi$-system $\P \subseteq \F_1 \cap \F_2$.
- And $\nu_1$ and $\nu_2$ are $\sigma$-finite on $\P$.

Then $\nu_1$ and $\nu_2$ agrees on $\sigma(\P)$.

- $\mathup M(\P) = \sigma(\P)$.
  - Suppose $A, B \in \P$, $A \cap B \in \P \subseteq \mathup M(\P)$ and $A^c \in \mathup M(\P)$.
  - Since $\P$ is a $\pi$-system $A \cap B \in \P$.
  - Suppose $A \in \P$, consider $C_n := A_n - A \in \P$. Clearly $C_n \uparrow A^c$.
  - Therefore $A^c \in \mathup M(\P)$.
  - By Monotone Class Theorem, $\mathup M(\P) = \sigma(\P)$.
- For $A \in \P$ where $\nu_i(A) < \infty$, define $\L_A: = \{B \in \sigma(\P): \nu_1(A \cap B) = \nu_2 (A \cap B)\}$.
  - $\L_A \supseteq \P$. And $\L_A$ is clearly a monotone class.
  - Therefore $\mathup M(\P) = \sigma(\P) \subseteq \L_A$.
- $\forall A_n \in \P, \forall B \in \sigma(\P): \nu_1(A_n \cap B) = \nu_2(A_n \cap B)$.
- Now take $n \to \infty$. $\forall B \in \sigma(\P): \nu_1(B) = \nu_2(B)$.

#### Outer Extension of Measures

> Suppose $\mu$ is a $\sigma$-finite measure on semi-ring $\S$.
>
> $\mu^*$ is the unique extension to $\sigma$-algebra $\M \subseteq \M_{\mu^*}$.
>
> Consider $E \in \M_{\mu^*}$.
>
> Suppose $\mu$ is a proto-measure on proto-ring $\S$.
>
> - There exists $A \in \S_\sigma \subseteq \M_{\mu^*}$ containing $E$, and $\mu^*(A) \le \mu^*(E) + \epsilon$.
> - There exists $A \in \S_{\sigma\delta} \subseteq \M_{\mu^*}$ containing $E$, and $\mu^*(A) = \mu^*(E)$.
>
> Suppose $\mu$ is finitely-additive on semi-ring $\S$. And $\mu^*(E) < \infty$.
>
> - There exists $A \in \overline \S \subseteq \M_{\mu^*}$ where $\mu^*( A \Delta E) \le \epsilon$.
>
> Suppose $\mu$ is a $\sigma$-finite finitely-additive measure on semi-ring $\S$.
>
> - $\widetilde \S$ is an $\sigma$-algebra, implied by $\sigma$-finiteness. So $\S_\sigma = \widetilde \S = \sigma(\S) = \S_{\sigma\delta} \subseteq \M_{\mu^*}$.
> - $E$ is the union of $A \in \widetilde S$ and a $\mu^*$-null set.
> - $\M_{\mu^*} = \M_{\overline \mu^*} = \M_{\widetilde \mu^*}$ and $\mu^* = \overline \mu^* = \widetilde \mu^*$ on $\M_{\mu^*}$.
>

(**Induced outer measure**)

Suppose $\mu$ is a **proto-measure on proto-ring** $\S$ on $X$.

Define the **induced outer measure** $\mu^*: \P(X) \to [0, \infty]$ as:
$$
\forall E \in \P(X): \mu^{*}(E):=\inf \left\{\sum_{j = 1}^{\infty} \mu\left(A_{j}\right): A_{j} \in \S , E \subseteq \bigcup_{j = 1}^{\infty} A_{j}\right\}
$$
define $\inf \varnothing=\infty$.

- $\mu^{*}$ is an **outer measure** on $X$. (Just verify the three axioms.)
- $\forall S \in \S: \mu^*(S) \le \mu(S)$ by definition.

(**Outer measure lemma**)

Suppose $\mu$ is **countably subadditive and monotone on photo-ring $\S$**. Then $\mu|_\S = \mu^*|_\S$.

- Consider any $A \in \S$. $\mu^*(A) \le \mu(A)$ by definition.
- $\mu^*(A) \ge \mu(A)$:
  - For any $\epsilon > 0$, exists $(A_n)_{n = 1}^\infty \subseteq \S$.
  - Where $A \subseteq \cup_{n}A_n$ and $\sum_{n}\mu(A_n) \le \mu^*(A) + \epsilon$.
  - Therefore $\mu(A) \le \sum_{n}\mu(A_n) \le \mu^*(A) + \epsilon$.

Suppose $\mu$ is a **finitely additive measure on semi-ring** $\S$. Then $\S \subseteq \M_{\mu^*}$.

- We only need to show that:
  $$
  \forall A \in \S, \forall B \in \P(X) \land \mu^*(B) < \infty: \mu^*(B)\ge\mu^*(B \cap A)+\mu^*(B \cap A^{c})
  $$

- Now consider any $A \in \S$ and $B \in \P(X)$.

- For any $\epsilon > 0$ there exists $(B_j)_{j = 1}^\infty \in \S$ where $B \subseteq \cup_j B_j$. And $\sum_j \mu(B_j) \le \mu^*(B ) + \epsilon$.

  - $\mu^*(B \cap A) \le \sum_j \mu^*(B_j \cap A) \le \sum_j\mu(B_j \cap A)$.

  - $\mu^*(B \cap A^c) \le \sum_j \mu^*(B_j - A)$.

- Let $B_j - A= +_{k=1}^{m_j} C_{jk}$ for $C_{jk} \in \S$.

- Now $\mu^*(B_j - A) \le \sum_{j,k} \mu(C_{jk})$.

- Since $B_j = \p{B_j \cap A} + (+_{k}C_{jk})$, $\mu(B_{j} \cap A)+\sum_{k=1}^{m_{j}} \mu(C_{j k})=\mu(B_{j})$.

- Therefore $\mu^{*}(B \cap A)+\mu^{*}(B \cap A^{c}) \leq \sum_{j=1}^{\infty} \mu(B_{j})<\mu^{*}(B)+\epsilon$.

(**The outer extension**)

Suppose $\mu$ is a **measure on semi-ring $\S$**.

**Then $\mu^*$ is a measure extending $\mu$ on $\sigma$-algebra $\M_{\mu^*}$.**

- Since $\mu$ is a finite-additive measure, $\S \subseteq \M_{\mu^*}$.
- Since $\mu$ is countably subadditive and monotone. $\mu^*$ agrees with $\mu$ on $\S$.

Suppose $\nu$ is **another** measure extending $\mu$ from semi-ring $\S$ to $\sigma$-algebra $\M \subseteq \M_{\mu^*}$.

**Then $\mu^* = \nu$ for $A \in \M$ where $\mu^*(A) < \infty$.**

- For $\epsilon > 0$. There exists $(A_i)_{i = 1}^\infty \in \S$ where $A \subseteq +_i A_i$ and $\sum_i \mu(A_i)\le \mu^*(A) + \epsilon$.
  - $\nu(A) \le \mu^*(A)$. Since
    $$
    \nu(A) \le \nu(+_i A_i) = \sum_i \nu(A_i) = \sum_i \mu(A_i) \le \mu^*(A) + \epsilon
    $$
    
  - $\mu^*(A) \le \nu(A)$. Since
    $$
    \begin{aligned}
    \mu^*(A) & \le \mu^*(+_i A_i) = \sum_i \mu(A_i) = \sum_i \nu(A_i) = \nu(+_i A_i)\\
    & = \nu(A) + \nu(+_i A_i - A) \le \nu(A) + \mu^*(+_iA_i - A) \\
    & \le \nu(A) + \mu^*(+_i A_i) - \mu^*(A)\\
    & = \nu(A) + \sum_i \mu(A_i) - \mu^*(A) \le \nu(A) + \epsilon
    \end{aligned}
    $$

**Suppose $\mu$ is $\sigma$-finite. Then $\mu^* = \nu$ on $\M$.**

- For $A \in \M$ where $\mu^*(A) = \infty$. Then $\nu(A) = \mu^*(A) = \infty$.

- There exists $(B_i)_{i = 1}^\infty \in \S$ where $+_i B_i = X$ and $\mu(B_i) < \infty$. Then
  $$
  \nu(A) = \nu(\cup_i(A \cap B_i)) = \sum_i \nu(A \cap B_i) =^* \sum_i \mu^*(A \cap B_i) = \mu^*(A) = \infty
  $$
- Where the $=^*$ step follows from $\mu^*(A) < \infty$ case.

(**$\S_\sigma$ and $\S_\delta$**)

Suppose $\S$ is a set system on $X$.

- $\S_\sigma$ contains all the sets that are **countable unions** of sets in $\S$.
- $\S_\delta$ contains all the sets that are **countable intersections** of sets in $\S$.
- $\S_{\sigma\delta} = (\S_\sigma)_\delta$.

Suppose $X$ is a topological space.

- Let $G_\delta$ be the set of all countable intersections of open sets.
- Let $F_\sigma$ be the set of all countable union of closed sets.

(**Outer approximation of $\P(X)$ by $\S_\sigma$**)

Suppose $\mu$ is a proto-measure on proto-ring $\S$.

For $E \in \P(X)$ where $\mu^*(E) < \infty$. For any $\epsilon > 0$.
$$
\exists A \in \S_\sigma: E \subseteq A\land \mu^*(A) \le \mu^*(E) + \epsilon
$$

- By definition of $\mu^*$, for some $(A_i)_{i = 1}^\infty \in \S$, $A = \cup_i A_i \supseteq E$. So $\sum_i \mu(A_i) \le \mu^*(E) + \epsilon$.

- Also by definition $\mu^*(A) \le \sum_i \mu(A_i)$.

(**Outer approximation of $\P(X)$ by $\S_{\sigma\delta}$**)

Suppose $\mu$ is a proto-measure on proto-ring $\S$.

For $E \in \P(X)$ where $\mu^*(E) < \infty$.
$$
\exists C \in \S_{\sigma \delta}: E \subseteq C \land \mu^*(C) = \mu^*(E)
$$

- There exists $\p{A_n}_{n=1}^\infty \subseteq \S_\sigma$ where $\mu^*(A_n) \le \mu^*(E) + 1/n$, and $E \subseteq A_n$.
- Let $C = \cap_n A_n \in \S_{\sigma\delta}$. Then $C \supseteq E$ and $\mu^*(C) \ge \mu^*(E)$.
  - Since $\mu^*(C) \le \mu^*(A_n) \le \mu^*(E) + 1/ n$. $\mu^*(C) \le \mu^*(E)$.

(**Approximation of $\M_{\mu^*}$ by $\overline \S$**)

Suppose $\mu$ is a finitely-additive measure on semi-ring $\S$. 

- So $\S \subseteq \M_{\mu^*}$.

For $E \in \M_{\mu^*}$ where $\mu^*(E) < \infty$. For any $\epsilon > 0$.
$$
\exists B \in \overline \S: \mu^*(B \Delta E) \le 2 \epsilon
$$

- Some $(A_i)_{i = 1}^\infty \in \S$, $A = \cup_i A_i \supseteq E$, where $\mu^*(A) \le \sum_i \mu(A_i) \le \mu^*(E) + \epsilon$.
- $\mu^*(A - E) = \mu^*(A) - \mu^*(E) \le \epsilon$.
  - Notice that $A \in \S_\sigma \subseteq \M_{\mu^*}$.
- There exists some $n$ where $B_n = \cup_{i = 1}^n A_i \in \overline \S$, and $\mu^*(A - B_n) \le \epsilon$.
- $\mu^*(B_n \Delta E) = \mu^*(B_n - E) + \mu^*(E - B_n) \le 2 \epsilon$.
  - $\mu^*(E - B_n) \le \mu^*(A - B_n) \le \epsilon$.
  - $\mu^*(B_n - E) \le \mu^*(A - E) \le \epsilon$.

(**Approximation by $\widetilde \S$**)

Suppose $\mu$ is a $\sigma$-finite finitely-additive measure on semi-ring $\S$.

- $\S \subseteq \M_{\mu^*}$ due to finite-additivity.
- $\widetilde \S$ is an $\sigma$-algebra, implied by $\sigma$-finiteness. So $\S_\sigma = \widetilde \S = \sigma(\S) = \S_{\sigma\delta} \subseteq \M_{\mu^*}$.

For $E \in \M_{\mu^*}$. Then:
$$
\exists A \in \sigma(\S): E \subseteq A\land \mu^*(A - E) = 0
$$

- There exists $\p{X_i}_{i=1}^\infty \in \S$ s.t. $\mu^*(X_i) \le \mu(X_i) < \infty$ and $X = \cup_i X_i$.
- Define $E_i:= E \cap X_i \in \M_{\mu^*}$. Clearly $\mu^*(E_i) \le \mu^*(X_i) < \infty$.
- There exists $\p{A_{in}} \subseteq \S_\sigma$ where $A_{i, n} \supseteq E_i$ and $\mu^*(A_{in}) \le \mu^*(E_i) + 2^{-i}/n$.
- Define $A_n := \cup_i A_{in}$, then $A_n \supseteq E$, and $A_n - E \subseteq \cup_i (A_{in} - E_i)$.
- So $\mu^*(A_n - E) \le \sum_{i} \mu^*(A_{in} - E_i) \le 1/n$.
- Define $A:= \cap_n A_n$.
- Then $A \supseteq E$, $A \in \S_{\sigma\delta} = \sigma(\S)$. And $\mu^*(A - B) = 0$.

The following immediately follows from this result:

- For $N \in \M_{\mu^*}$ and $\mu^*(N) = 0$, there exists $\overline N \in \sigma(\S)$ where $\mu^*(\overline N) = 0$ and $N \subseteq \overline N$.
- For any $A \in \mathcal{M}(\mu^{*})$, there are sets $A_{-}, A_{+} \in \sigma(\mathcal{A})$ with $A_{-} \subseteq A\subseteq A_{+}$ and $\mu\left(A_{+} \backslash A_{-}\right)=0$.
- $(X, \M_{\mu^*}, \mu^*)$ is the **completion** of $(X, \sigma(\S), \mu^*)$.
- For all $\mu$, $\overline \mu$, $\widetilde \mu$, they have the same induced outer measure $\mu^*$.
  - $\sigma(\overline \S) = \sigma(\widetilde \S)$. Therefore $\M_{\mu^*} = \M_{\overline \mu^*} = \M_{\widetilde \mu^*}$.
  - Now due to the uniqueness of outer extension, $\mu^* = \overline \mu^* = \widetilde \mu^*$ on $\M_{\mu^*}$.

