#### Rings

##### Rings

$\langle R, +, \cdot \rangle$ where $+$ and $\cdot$ are binary operators on $R$ is a ring when:

- $\langle R, +\rangle$ is an abelian group, called the additive group of the ring $R$.
- Multiplication $\cdot$ is associative.
- Multiplication $\cdot$ distributes over addition $+$.
  - $a(b+c) = ab + ac$ and $(a + b)c = ac + bc$.

The following properties immediately follows from the definition:

- $0\cdot a = a\cdot 0 = 0$, where $0$ is the additive identity.
  - since $0\cdot a = (0 + 0)\cdot a = 0\cdot a + 0\cdot a$.
- For $0 \in \Z$, $0a = 0$ by definition.
- Negation commutes with multiplication:
  - $a(-b) = -(ab) = (-a)b$.
    - $ab + a(-b) = ab + (-a)b = ab + (-(ab)) = 0$.
  - $(-a)(-b) = - a(-b) = -(-(ab)) = (ab)$.

##### Ring operations on subsets

Suppose $\langle R, +, \cdot \rangle$ is a ring. Suppose $H, K \subseteq R$, and $a \in R$.

We generalize $+$ and $\cdot$ to accept subsets of $R$ as operands. See (Binary operations on subsets).

- The generalized $+$ is commutative. e.g. $aH = Ha$.
- The generalized $+, \cdot$ are associative.
- The generalized $\cdot$ distributes over generalized $+$.

##### Integral domains and fields

- A ring with commutative multiplication is called a **commutative (C)** ring.
- A ring with multiplicative identity (the unity), is called a ring **with unity (U)**.
  - $\forall r \in R: r1 = 1r = r$.
  - The unity is unique if it exists. Since $1'1 = 1' = 1$.
  - Elements with **multiplicative inverse** are called **units**.
  - The inverse of a unit is unique.
- The unity is $0$ if and only if the ring is the **zero / null** ring.

In ring $R$, elements $a, b \in R$ are **zero divisors** if $a \neq 0 \land b\neq0 \land ab = 0$.

In **nonzero** rings with **unity**, if every **nonzero** element of $R$ is a unit, then $R$ is a **division** ring.

For **nonzero commutative rings with unity (NCU)** rings.

- A **NCU ring** with **no zero divisors** is an **integral domain (ID)**.
- A **NCU ring** where **all nonzero elements are units** is a **field**.
  - Fields are integral domains.

##### Group of units in NCU rings

Suppose $\a{R, +, \cdot}$ is a **NCU ring**. Define $R^*$ as the set of all units.

- $\a{R^*, \cdot}$ is an abelian multiplicative group.
- The unity in ring $R$ is the multiplicative unit in group $R^*$.

##### Direct product of rings

Suppose $\a{R_1, +_1, \cdot_1}, \ldots, \a{R_k, +_k, \cdot_k}$ are rings.

Then $R_1 \times \cdots \times R_k$ is a ring with coordinate-wise operations. It is the **direct product** of rings $R_1$ to $R_k$.

- A direct product of integer domains is not in general an integer domain.
- A direct product of fields is not in general a field.
- For example, consider $\Z_2 \times \Z_2$, it has zero divisor $(1, 0), (0, 1)$.

##### Subrings, subdomains, and subfields

Given a ring $\a{R, +, \cdot}$, and $S \subseteq R$. When $\a{S, +|_{S^2}, \cdot |_{S^2}}$ is a ring, it is called a **subring** of ring $R$.

- Subring $S \subseteq R$ contains $0 \in R$.
  - Since $\a{S, +}$ is a subgroup of $\a{R, +}$.


Subdomains and subfields are similarly defined as subrings.

- Subdomain $S \subseteq R$ has the unity $1_R \in R$.
  - Consider equation $x^2 = x$ in $S$.
  - It solves to $x \in \c{0, 1_S}$ in $S$, and $x \in \c{0, 1_R}$ in $R$.
  - Therefore $1_S = 1_R$.

When the context is clear, we write $S \le R$ to denote algebraic substructure relationships, such as subgroups, subrings, and subfields.

> Fraleigh in *A First Course in Algebra*, p.173
>
> ... In fact, let us say here once and for all that if we have a set, together with a certain type of algebraic structure (group, ring, field, integral domain, vector space, and so on), then any subset of this set, together with the natural induced algebraic structure that yields an algebraic structure of the same type, is a substructure. If $K$ and $L$ are both structures, we shall let $K \leq L$ denote that $K$ is a substructure of $L$ and $K<L$ denote that $K \leq L$ but $K \neq L$.

##### Subfield test

Suppose $F$ is a field. And $\c{0, 1} \subset E \subseteq F$. $E$ is a subfield of $F$ if
$$
\forall a \in E, \forall b\in (E-\{0\}): a - b \in E \land a b^{-1} \in E
$$
To prove this test, consider the definition of field:

- $E$ is a nonzero commutative ring.
- $E$ has the unity: $a a^{-1} = 1 \in E$.
- All nonzero elements are units: $1a^{-1} \in E$.

##### Finite integral domains are fields

Suppose $R$ is a **finite ID**. Then $R$ is also a field.

- For any $a\in R$, $a\neq 0$, define $\lambda_a(x) = ax$.
  - $\forall x_1, x_2 \in R: ax_1 = ax_2 \implies x_1 = x_2$ so $\lambda_a$ is injective.
- Since $R$ is finite, $\lambda_a$ is bijective.
- There must be some $b \in R$, $ab = 1 = ba$. So $R$ is a field.

##### Association

Suppose $R$ is a **NCU ring**.

- $r, s \in R$ **associates** if $r = us$ for some unit $u \in R$.
- Association is an **equivalence relation**, denoted as $r \sim s$.
- $\{0\}$ and $R^*$ are two equivalence classes under $\sim$.


##### Characteristic of a ring

Suppose $R$ is a **ring**, $\char R := \min \{n \in \N^+\mid \forall a \in R:na = 0\}$.

- When $\c{n \in \N^+ \mid \forall a \in R: na = 0} = \varnothing$, we define $\char R := 0$.
  - $\char \Z = \char \Q = \char \R = \char \C = 0$.
- $\char(R) = 1$ if and only if $R$ is the zero ring.
- $\char (\Z_n) = n$.
- Suppose $R$ is a **NCU ring**, $\char R = \min\c{n \in \N^+ \mid n 1 = 0}$.

We have following statements:

- Characteristic of direct product of rings.
  - Suppose one of the ring has characteristic $0$, the product has characteristic $0$.
  - Otherwise it is the LCM of all characteristics.
- When $\char R = 0$, $R$ must be infinite.
- When $R$ is an integral domain, $\char R$ is either zero or a prime.
  - Suppose $\char R$ is not a prime. And $\char R = m n$ where $m, n \neq 1$.
  - Then $(m1)(n1) = (mn)1 = 0$. So $(m1)$ is a zero divisor.

##### The prime subring

Suppose $R$ is a **NCU ring**.

Consider map $\phi: \Z \to R$ defined by $n \mapsto n 1$. $\phi$ is a ring homomorphism.

- $\phi(m + n) = m1 + n1 = \phi(m ) + \phi(n)$.
- $\phi(mn) = (mn)1 = (m1)(n1) = \phi(m)\phi(n)$.

The image $\phi[\Z] = \{n1 : n \in \Z\}$ is called the **prime subring** of $R$.

The prime subring is a **NCU ring**.

- When $\char (R) = n$, $\phi[R] \simeq \Z/n\Z \simeq \Z_n$.
- When $\char(R) = 0$, $\phi[R] \simeq \Z$.

##### Binomial formula for NCU rings with prime characteristic

Suppose $R$ is a NCU ring prime characteristic $p$.

- $p \mid C_p^r$ where $0 < r < p$.
  - Note that
    $$
    C_{p}^r = {p!}/\p{r!(p - r)!} \implies r ! C_{p}^r = \frac{p!}{(p - r)!} = p(p - 1) \cdots (p - r + 1)
    $$
  - Therefore $p \mid r! C_p^r$. Since $p$ is prime, and $p \nmid r!$, we have $p \mid C_{p}^r$.
- For any $a, b \in R$, we have:
  $$
  (a+b)^{p}=a^{p}+b^{p}+\sum_{r=1}^{p-1}C_p^ra^{p-r} b^{r} \implies
  (a+b)^{p} = a^{p}+b^{p}
  $$
- Apply this rule repeatedly gives for all $k \in \N$,
  $$
  (a + b)^{p^k} = a^{p^k} + b^{p^k}
  $$
- Make substitution $b \mapsto b - a$ and $a \mapsto a$ gives:
  $$
  b^{p^k} - a^{p^k} = (b - a)^{p^k}
  $$
- Make substitution $b \mapsto b + c$ gives:
  $$
  (a + b + c)^{p^k} = a^{p^k} + b^{p^k} + c^{p^k}
  $$

##### Linear spaces

Suppose $\a{V, +}$ is an abelian group, and $F$ is a field.

With a **scalar multiplication** $\cdot: F \times V \to V$, $\a{V, +, \cdot}$ is a **linear space** over $F$ if for $a, b \in F$ and $u, v \in V$ we have:

- Scalar multiplication distributes over addition:
  - $a(u+v)=a u+a v$.
  - $(a+b) v=a v+b v$.
- Scalar multiplication is associative:
  - $(ab) v = a(bv)$.
- Scalar identity: $1 v=v$ for $1 \in F$.

Elements of $V$ are called **vectors**, and elements of $F$ are **scalars**.

Examples of vector spaces:

- For any field $F$, $F[x]$ is a $F$-vector space.
- For any fields $F < E$, $E$ is a $F$-vector space.

##### Algebras over fields

Suppose $\a{V, +, \cdot_F}$ is a linear space over $F$.

Given a multiplication on $V$ denoted as $\cdot_V: V\times V \to V$, $\a{V, +, \cdot_F, \cdot_V}$ is an **algebra over $F$** if for all $a, b \in F$ and $x, y, z \in V$ we have:

- Multiplication on $V$ distributes over addition:
  - $(x + y)z = x z + y z$.
  - $z(x + y) = zx = zy$.

- Scalar multiplication is compatible with multiplication on $V$:
  - $(a x)(by) = (ab)(x y)$.

If multiplication $\cdot_V$ is associative, $\a{V, +, \cdot_F, \cdot_V}$ is called an **associative algebra**.

- In this case, $\a{V, +, \cdot_V}$ is a ring.
- Note that some authors use the term algebra to refer to an associative algebra.

Examples of associative algebras:

- Suppose $K/F$ is an field extension, $K$ is an algebra over $F$.
- $F[x]$ is an algebra over $F$.

