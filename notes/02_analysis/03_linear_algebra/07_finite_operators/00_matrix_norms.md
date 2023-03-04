##### Matrix function

A function $A(t): I \subseteq \R \to \bF^{n \times m}$ is a matrix function. And $f(t): I \subseteq \R \to \R^n$ is a vector (valued) function.

- Derivative and integrals are defined **element wise**.
- $(A B)'(t) = A'(t)B(t) + A(t) B'(t)$.
  - Expand down to elements $(AB)'(t) = (A_{ij}(t)B_{jk}(t))'$.

- Suppose $A(t): I \to \bF^{n \times n}$ and $\det A(t) \neq 0$. Then $\frac{\dd }{\dd t} A(t)^{-1} = -A(t)^{-1}A'(t) A(t)^{-1}$.
- Function products are defined according to linear algebra rules.

Consider matrix function sequence $(A_k(t))_{k=1}^\infty$, the sequence is said to converge to $A(t)$ in some mode when each element converges in that mode.

##### Review: finite dimensional normed spaces

Recall that for finite-dimensional linear spaces:

- All norms are equivalent, inducing the same topology. Convergence in all norms are equivalent.
- All normed vector spaces are Banach.

##### Vector norm

Given $\bF = \R, \C$, let $V = \bF^n$. A vector norm $\n{\cdot}$ is a norm on $V$.

Common vector norms includes:

- $p$-norms for $p \in [1, \infty)$, $\n{v}_p = \left(\sum_{i}\abs{v_{i}}^p\right)^{1/p}$.
- $\infty$-norm, $\n{v}_\infty = \max_{i} |v_{i}|$.

##### Matrix norm

Given $\bF = \R, \C$, let $S = \mathbb \bF^{n \times m}$. A matrix norm $\n{\cdot}$ is a **norm** on $S$.

- For $A(t)\in C([\alpha, \beta] \to S)$. $\n{\int_{\alpha}^\beta A(t) \dd t} \le \int_\alpha^\beta \n{A(t)} \dd t$.

On operator space $\bF^{n \times n}$ on vector space $\bF^n$.

- $\n{\cdot}$ is called **sub-multiplicative** if $\forall S, T \in \bF^{n \times n}: \n {ST} \le \n S \n T$.
- A matrix norm is **compatible** with a vector norm if $\n{Av} \le \n{A}\n{v}$.

##### Induced matrix norm

On operator space $\bF^{n \times n}$ of vector space $\bF^n$. A vector norm induces a matrix norm:
$$
\n{A} := \sup_{x \in \bF^n, \n{x} = 1} \n{Ax}.
$$

- The induced norm is compatible with the vector norm.
- The induced norm is sub-multiplicative.
  - $\forall x \in \bF^n: \n{ABx}\le \n{A}\n{Bx} \le \n{A}\n{B}\n{x}$.
- In any induced norm $\n{I} = 1$.

