#### Integral Domains

> - Primes are irreducibles in integral domains.

##### Irreducible and reducible elements

Suppose $D$ is an **integral domain**. And $p \in D$ is a **nonzero nonunit** element.

$p$ is **irreducible** if $p = ab$ implies either $a$ or $b$ is a unit. Otherwise $p$ is **reducible**.

Reducibles and irreducibles do not associate in integral domains.

- Suppose $p \in D$ is irreducible.
- Suppose $q \in D$ is reducible with $q = st$ where $s, t$ are nonzero nonunit elements.
- Then $p \sim q$ implies $p = uq = u(st) = (us) t$.
- So $p$ must be reducible. Contradiction!

##### Primes in IDs are irreducible

Suppose $D$ is an **integral domain**. Prime elements in $D$ are irreducible.

- Prove with contradiction. Suppose $p \in D$ is reducible.
- And $p = st$, where $s, t$ are **nonzero nonunit** elements. Clearly $s \mid p$ and $t \mid p$.
- Then $p \mid st$. As $p$ is prime, $p \mid s$ or $p \mid t$.
- So $p \sim s$ or $p \sim t$. w.l.o.g. let's suppose $p \sim s$.
- $p = us = ts$ where $u$ is some unit. So $u = t$.
- Therefore $t$ must be a unit. Contradiction!

#### UFDs and PIDs

> - Definition of UFDs and PIDs.
> - $p$ is irreducible iff $(p)$ is nonzero maximal in PIDs.
> - Irreducibles are primes in UFDs and PIDs.

##### Unique factorization domains

An **integral domain** $D$ is a unique factorization domain if:

1. Every **nonzero nonunit** elements is a product of a finite number of irreducibles.
2. If $p_{1} \cdots p_{r}=q_{1} \cdots q_{s}$ are two product of irreducibles in $D$. Then
   - $r = s$.
   - There is a permutation $\sigma$ on $\c{1, \ldots, r}$ such that $p_i \sim q_{\sigma(i)}$ for all $1 \le i \le r$.

A field $F$ is a UFD since it contains only the zero and units.

##### Irreducibles are primes in UFDs

Suppose $D$ is a **UFD**. Irreducibles are primes.

- Suppose $p, a, b \in D$ and $p \mid ab$, and $p$ is irreducible.
- The case where $a$ or $b$ is zero or unit is trivial.
- Suppose $a, b$ are nonzero nonunit. Consider the complete factorization.

##### Principal ideal domain

An **integral domain** $D$ is a **principal ideal domain (PID)** if every ideal in $D$ is a principal ideal.

##### Irreducibles and maximal ideals in PIDs

Suppose $D$ is a PID. $\p p$ is nonzero maximal iff $p$ is irreducible.

- $\from$ Suppose $\p p$ is the zero ideal or not a maximal ideal.
  - Suppose $(p) = (0)$ then $p = 0$.
  - Suppose $\p p \subset \p s \sqsubset D$, then $p = s t$ where $s$ and $t$ are nonzero nonunit.
  - So either case, $p$ is not irreducible.
- $\to$ Suppose $p$ is a unit or $p$ is reducible, or $p$ is zero.
  - Suppose $p$ is zero. $(p) = \c{0}$.
  - Suppose $p$ is a unit. $(p) = D$.
  - Suppose $p$ is reducible. $p = st$, where $s$ and $t$ are nonzero nonunit. Then $\p p \subset \p s \sqsubset D$.
  - So in all cases, $(p)$ is not a nonzero maximal.

##### Irreducibles are primes in PIDs

Suppose $D$ is a **PID**. Irreducibles are primes.

- Suppose $p$ is irreducible. $\p{p}$ is a nonzero maximal ideal.
- So $(p)$ is a nonzero prime ideal. So $p$ is prime.

#### PIDs are UFDs

##### Ascending chain condition

Suppose $R$ is a **NC ring**. $R$ satisfies the **ascending chain condition** if for all increasing sequences of ideals $(N_i)_{i = 0}^\infty$, there exists $M \in \N$ where $\forall k\in \N: N_{M + k} = N_M$.

- In this case $N_M = \cup_i N_i$.

Suppose $R$ is a **PID**, $R$ satisfies the ascending chain condition.

- Consider any ascending chain of ideals $(N_i)_{i = 1}^\infty$
- Suppose $N = \cup_i N_i = \p c$ for $c\in R$.
- There exists $M \in \N$ where $c \in N_M$.
- Therefore $\forall k \in \N: N_{M + k} = (c) = N_{M}$.

##### Reducibles in PID factorizes into irreducibles

Suppose $D$ is a **PID**. Reducibles in $D$ can be factorized into product of irreducibles.

- Suppose $A$ is the set of all nonzero nonunit elements in $D$.
- Suppose $G \subseteq A$ is the set of irreducibles and their products.
- Let $B = A - G$. We now prove that $B = \varnothing$ by contradiction.
  - Suppose $B\neq \varnothing$.
  - There exists an element $b_1 \in B$, which is reducible.
    - There must exist nonzero nonunit $s$ and $t$, $b = st$.
      - We have $\p b \subset \p s$ and $\p b \subset \p t$.
      - One of $s, t$ is in $B$. Let $b_2 = s$ or $b_2 = t$ be the one in $B$.

  - By induction, there is a infinite sequence $(b_i)_{i=1}^\infty$ such that $\p {b_i} \subset \p{b_{i+1}}$.
  - But $D$ is a PID satisfying the ascending chain condition. Contradiction!

- This is a contradiction, $B = \varnothing$.

##### PIDs are UFDs

Suppose $D$ is a **PID**. $D$ is also a **UFD**.

- Consider nonzero nonunit element $a \in D$.

- Suppose there are two factorization of $a$ into irreducibles.
  $$
  a=p_{1} p_{2} \cdots p_{r} = 
  q_{1} q_{2} \cdots q_{s}, \quad s \ge r
  $$

- Then we have $p_{1} \mid\left(q_{1} q_{2} \cdots q_{s}\right),$ which implies that $p_{1} \mid q_{j}$ for some $j$.

- By changing the order of the $q_{j}$ if necessary, we can assume that $j=1$ so $p_{1} \mid q_{1}$.

- By symmetry $q_1 \mid p_1$ and $p_1 \mid q_1$. So $p_1 \sim q_1$.

- Suppose $q_1 = p_1 u_1$ for some unit $u_1 \in D$. Then
  $$
  p_{1} p_{2} \cdots p_{r}=p_{1} u_{1} q_{2} \cdots q_{s}
  $$

- By left and right cancellation law in $D$,
  $$
  p_{2} \cdots p_{r}=u_{1} q_{2} \cdots q_{s}
  $$

- Continuing this process, starting with $p_{2}$ and so on, we finally arrive at

$$
1=u_{1} u_{2} \cdots u_{r} q_{r+1} \cdots q_{s}
$$
- Since the $q_{j}$ are irreducibles, they are not units, so we must have $r=s$.
