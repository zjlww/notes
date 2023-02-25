### Extrema

Suppose $f: S \subseteq \R \to \R$.

##### Necessary condition of extrema

 Suppose $f$ is differentiable at $c \in S^\circ$. $f$ has a local extremum at $c$ then $f'(c) = 0$.

##### Sufficient condition of extrema

 Suppose $f \in C^n(a, b)$. And for some $c \in (a, b)$
$$
f^{\prime}(c)=f^{\prime \prime}(c)=\cdots=f^{(n-1)}(c)=0, \quad f^{(n)}(c) \neq 0
$$

- Then for $n$ even
  - $f$ has a local minimum at $c$ if $f^{(n)}(c)>0$,
  - $f$ has a local maximum at $c$ if $f^{(n)}(c)<0$.
- If n is odd, there is neither a local maximum nor a local minimum at $c$.

Suppose $S$ is an open set. $f: S \subseteq \R^n \to \R$.

##### Stationary point

 Suppose $f$ is differentiable at $a$ and $\nabla f(a) = 0$. Then $a$ is a stationary point of $f$.

A stationary point is a saddle point if $\forall \epsilon > 0, \exists x, y \in B(a, \epsilon):f(x) < f(a) < f(y)$.

##### Necessary condition of extrema

 Suppose $f \in D[S]$. $f$ has local extremum at $c \in S$ then $D_kf(c) = 0$. Any existing directional derivative at $c$ should be zero.

##### Sufficient condition of extrema

 Suppose $f \in D^2 [S]$, and $D_{i, j} f$ are continuous at $a\in S$. The hessian matrix must be real symmetrical.

Clearly $f \in D^*[S]$. Suppose $\nabla f(a) = 0$. Consider the quadratic form:
$$
Q(t)=\frac{1}{2} f^{\prime \prime}(a;t)=\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} D_{i, j} f(a) t_{i} t_{j} = \frac{1}{2} t^T H_f(a) t
$$

- If $Q(t)>0$ for all $t \neq 0, f$ has a local minimum at $a$.
- If $Q(t)<0$ for all $t \neq 0$, $f$ has a local maximum at $a$.
- If $Q(t)$ takes both positive and negative values, then $f$ has a saddle point at a.

$$
f(a + t) - f(a) = \frac{1}{2} t^T H_f(a) t + \|t\|^2 E(t)
$$
