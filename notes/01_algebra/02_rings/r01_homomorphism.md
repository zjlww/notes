#### Ring Homomorphisms

##### Ring homomorphisms, isomorphisms, and automorphisms

For rings $R$ and $R'$, a map $\phi: R \rightarrow R^{\prime}$ is a homomorphism if

- $\forall a, b \in R: \phi(a + b) = \phi(a) + \phi(b)$.
- $\forall a, b \in R: \phi(ab) = \phi(a) \phi(b)$.

We have following comments:

- A ring homomorphism is also a **group homomorphism** for the underlying group.
- When $\phi$ is bijective, it is called an **isomorphism**.
- When $R = R'$ and $\phi$ is bijective, it is called an **automorphism**.
- The fiber $\phi^{-1}[\{0\}] = \ker \phi$ is called the **kernel**.
  - The kernel is a **subring** of $R$.


##### Properties of ring homomorphisms

Let $\phi: A \rightarrow B$ be a ring homomorphism. $H \le A$, and $G \le B$ are subrings.

Besides the properties of group homomorphisms, we additionally have:

- Suppose $\phi$ is injective, $\phi^{-1}: \phi[A] \to A$ is a ring homomorphism.
  - $\phi^{-1}(\phi(a) + \phi(b)) = a + b$.
  - $\phi^{-1}(\phi(a) \phi(b)) = ab$.
- Image of subrings are subrings. $H \le A \implies \phi[H] \le \phi[A]$.
  - Addition is closed following a property of group homomorphisms.
  - Multiplication is closed since $\phi(a b) = \phi(a) \phi(b)$.

- Preimage of subrings are subrings. $G \le B \implies \phi^{-1}[G] \le \phi^{-1}[B]$.
  - Addition is closed following a property of group homomorphisms.
  - Multiplication is closed since $a, b \in \phi^{-1}[G]\implies \phi(a) \phi(b) = \phi(ab) \in G \implies ab \in \phi^{-1}[G]$.

- Image of unity is unity. $\phi(1_A) = 1_{\phi[A]}$.
  - $\forall r \in A:\phi(r)=\phi(1_A r)=\phi(r 1_A)=\phi(1_A) \phi(r)=\phi(r) \phi(1_A)$.
  - Note that $1_{\phi[A]}$ may not be $1_{B}$.
