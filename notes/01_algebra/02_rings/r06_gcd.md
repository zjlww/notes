#### GCDs and LCMs

##### Greatest common divisors

Suppose $R$ is a **NC ring**. And $A \subseteq R$. 

- $d \in R$ is a **common divisor** of $A$, if $\forall a \in A: d \mid a$.
- $d \in R$ is a **greatest common divisor** of $A$ in $R$, if
  - $d \in R$ is a common divisor of $A$,
  - and all other common divisors of $A$ in $R$ are multiples of $d$.

Denote the set of all greatest common divisors of $A$ in $R$ as $\GCD_R(A)$.

- We often write $\GCD_R(\c{a, b, c})$ as $\GCD_R(a, b, c)$.
- We often omit $R$ in operator $\GCD_R$ when it is clear from the context.

$\GCD$ has following properties:

- $\GCD_R(\varnothing) = R$. $\GCD_R(a) = aR^*$.
- $\GCD_R(\c{0} \cup A) = \GCD_R(A)$.
- $\GCD_R$ is monotonic decreasing. $A \subseteq B \implies \GCD_R(A) \subseteq \GCD_R(B)$.

$\GCD$ has better properties for less generic rings:

- Suppose $R$ is a **NCU ring**, $\GCD_R(A) = \GCD_R(A)\cdot  R^*$.
- Suppose $R$ is an **integral domain**, $h, g \in \GCD(A) \implies h \sim g$.
  - By definition, $h \mid g$ and $g \mid h$.

Suppose $R$ is an **integral domain**, where $\forall a, b \in R: \GCD_R(a, b) \neq \varnothing$, $R$ is an **GCD domain**.

Suppose $R$ is an **GCD domain**, $\GCD_R(A) \neq\varnothing$ for all finite $A \subseteq R$.

- Suppose $A = \c{a_0, \ldots, a_n}$. Take $g \in \GCD_R(a_0, \ldots, a_{n - 1})$.
- Then $\GCD_R(a_0, a_1, \ldots, a_n) = \GCD_R(g, a_n)$.

##### Least common multiples

Suppose $R$ is a **NC ring**. And $A \subseteq R$.

- $m \in R$ is a **common multiple** of $A$, if $\forall a \in A: a \mid m$.
- $m \in R$ is a **least common multiple** of $A$, if
  - $m \in R$ is a common multiple of $A$,
  - and all other common multiples of $A$ in $R$ are factors of $m$.

Denote the set of all least common divisors of $A$ in $R$ as $\LCM_R(A)$.

- $\LCM_R(\varnothing) = R$. $\LCM_R(\c{a}) = aR^*$.

Suppose $R$ is an **integral domain**, where $\forall a, b \in R: \LCM_R(a, b) \neq \varnothing$, $R$ is an **LCM domain**.

##### PIDs are GCD domains

Suppose $R$ is a **PID**. And $A \subseteq R$. Then $\GCD_R(A) \neq \varnothing$.

- Consider ideal $(A)$, suppose $(A) = (g)$ for $g \in R$.
- Since $A \subseteq (g)$, $g$ is a common divisor of $A$.
- Since $g \in (A)$, $g$ is the sum of finitely many elements in $A\cdot R$.
- Suppose $h$ is another common divisor of $A$. Then $h \mid g$.
- Therefore $\GCD_R(A) = gR^* \neq \varnothing$.

$\GCD_R(A)$ happens to be all generators of the principal ideal $(A)$ in PID $R$.

##### UFDs are GCD domains

> Please compare this proof to the proof in (PIDs are GCD domains).

Suppose $R$ is **UFD**. And $a, b \in R$. Then $\GCD_R(a, b) \neq \varnothing$.

- When $a = 0$, $\GCD_R(a, b) = bR^* \neq \varnothing$.
- Otherwise factorize $a = u\prod_{i=1}^tp_i^{e_i}$ and $b=v\prod_{i=1}^tp_i^{f_i}$.
  - Where $u$ and $v$ are units, and $p_i$ are primes not associates of each other.
- Define $c = \prod_{i=1}^t p_i^{m_i}$ where $m_i = \min(e_i, f_i)$.
- It is easy to see that $\GCD_R(a, b) = cR^*\neq \varnothing$.

##### Relatively prime and coprimes

Suppose $R$ is a **GCD domain**. $A \subseteq R$ is **relatively prime** if $\GCD_R(A) = R^*$.

By "dividing" a GCD, any $A \subseteq R$ can be made relatively prime.

- Suppose $g \in \GCD_R(A)$.
- Define $B := \c{a\mid ag \in A, a \in R}$. $|B| = |A|$.
- Then $\GCD_R(B) = R^*$.
  - Otherwise suppose $h \in \GCD_R(B)$ and $h\notin R^*$.
  - Then $gh \in \GCD_R(A)$. So $gh \sim g$.
  - Therefore $h \in R^*$. Contradiction!

Two elements $a, b \in R$ are **coprime** if $\GCD_R(a, b) = R^*$.

$A \subseteq R$ is **pairwise coprime** if all pairs $a \neq b$ and $a, b \in A$ are coprimes.

- If $A$ is pairwise coprime, $A$ is relatively prime.

##### GCDs in PID chains

Suppose $K < L$ are **PIDs**. And $A \subseteq K$. Then $\GCD_{K}(A) \subseteq \GCD_L(A)$.

- Suppose $(A)_K = (g)_K$, $\GCD_K(A) = gK^*$.
- Suppose $(A)_L = (h)_L$, $\GCD_L(A) = h L^*$.
- $h \mid g$ in $L$.
  - Clearly $(A)_K \subseteq (A)_L$, and $(g)_K \subseteq (h)_L$.
- $g \mid h$ in $L$.
  - $g$ is the sum of finitely many elements in $A\cdot K$.
- Therefore $h \sim g$ in $L$. $\GCD_L(A) = gL^*$.

