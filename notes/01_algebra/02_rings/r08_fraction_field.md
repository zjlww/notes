#### Quotient Fields

##### Quotient subfield

Suppose $D$ is a **subdomain** of **field** $F$. Define $D' := \c{a / b \mid \forall a \in F, \forall b \in (F-\{0\})}$.

- $D'$ is a subfield of field $F$.
- $D'$ is called the **quotient subfield** of the **domain** $D$ inside $F$.
- $D'$ is the minimum subfield of $F$ that contains $D$.

##### Quotient field

Suppose $D$ is an **integral domain**. Define $S:=\{(a,b) \mid a, b \in D, b \neq 0\}$.

- Define $(a, b) \sim (c, d) \iff ad = bc$. This is an **equivalence** relation.
- Define $E = S / \sim$. And define $a/b: = [(a,b)]$ as an equivalent class in $E$.

Define operations on $E$ as following:

- Define $+: E \times E \to E$ as $a/b + c/d = (ad + bc)/bd$.
  - Notice that $bd \neq 0$, so the element $(ad + bc)/bd$ is well defined.
  - Addition is well-defined. (Proof omitted.)
- Define $\times: E \times E \to E$ as $a/b \cdot c/d = ac / bd$.
  - Multiplication is well-defined. (Proof omitted.)


Then $\a{E, +, \times}$ is a field. (Proof omitted.)

- $D$ is isomorphic to subdomain $\widetilde D :=\{d/1 \mid d\in D\}$, given by the ring isomorphism $\phi(x) = x/1$.
  - So we often identify domain $D$ with $\widetilde D$.
- The fraction subfield of subdomain $\widetilde D$ in field $E$ is $E$ itself.

##### Quotient subfields are isomorphic

Suppose $D$ is an subdomain of field $F$ and $H$.

Suppose $E$ and $G$ are the quotient subfields of $D$ in $F$ and $H$. Then $E \simeq G$.

Consider $f: E \to G$ where $a/_Eb \mapsto a/_Gb$. $f$ is a ring isomorphism.

- $f(a / b + c / d) = f((ad+bc)/bd) = (ad+bc)/bd = a/b + c/d = f(a / b) + f(c / d)$.
- $f(a / b \cdot c / d) = f(ac / bd) = ac / bd = f(a/b) \cdot f(c /d)$.

##### Reduced fraction

Suppose $D$ is a **GCD**. And $a, b \in D$ where $b \neq 0$.

$a/b \in D'$ is a **reduced fraction** if $\GCD_D(a, b) = D^*$.

Otherwise it can be reduced by cancelling a GCD.

- Take $c \in \GCD_D(a, b)$.
- Notice that $a / b = (cs) / (ct) = s / t$.
- $s / t$ is a reduced fraction.

##### Field of rational functions

Suppose $F$ is an **ID**. Then $F[x]$ is also an **ID**.

- Define $F(x) := F[x]'$. It is called the field of **rational functions** over $F$.
- Define $F(x_{1}, \cdots, x_{n}) := F[x_1, \cdots, x_n]'$. It is called the field of rational functions in $n$ indeterminants over $F$.

##### Prime subfield

Suppose $F$ is a **field**. $\char (F)$ is either prime or zero.

Consider map $\phi: \Z \to R$ defined by $n \mapsto n 1$. $\phi$ is a ring homomorphism.

- When $\char(F) = p$, $Q=\phi[F]$ is the **prime subfield**.
- When $\char(F) = 0$, the fraction field $Q=\phi[F]'$ is the prime subfield.
  - $\phi[F] \simeq \Z$, therefore $\phi[F]' \simeq \Q$.


All subfield of $F$ contains $Q$, also $Q$ is a subfield of $F$, so

- $Q$ is the intersection of all subfields in $F$.
- $Q$ is the smallest subfield of $F$.

