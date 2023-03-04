#### Euclidean Domains

##### Euclidean norms

Suppose $D$ is an **ID**.

An **Euclidean norm** on $D$ is a function $v: D\to \mathbb N \cup \c{-\infty}$, where $v^{-1}[\c{-\infty}] = \c{0}$, that satisfies the following conditions:

1. (Euclidean division)
   $$
   \forall a \in D,\forall b \in D-\c{0}, \exists q, r \in D: \s{a = bq + r \land v(r) < v(b)}
   $$
   - $q$ and $r$ are called respectively a **quotient** and a **remainder** of the **Euclidean division** of $a$ by $b$.

2. For all nonzero $a, b \in D$, $v(a) \le v(ab)$.

An integral domain is a **Euclidean domain (ED)** if it can be endowed with a Euclidean norm.

Suppose $D$ is a **ED** with norm $v$. Suppose $a, b, c \in D$.

- $v(1) = \min\c{v(a): a \in D, a \neq 0}$.
  - Since for all nonzero $a \in D$, $v(1) \le v(1a) = v(a)$.
- $u \in D^* \iff v(u) = v(1)$.
  - $\to$ Suppose $u$ is unit. $v(u) \le v(u u^{-1}) = v(1)$. So $v(u) = v(1)$.
  - $\from$ Suppose $v(u) = v(1)$, $1 = ux + r$, we must have $r = 0$, so $u$ is unit.
- $a \mid b \implies v(a) \le v(b)$ and $a \sim b \implies v(a) = v(b)$.

##### EDs are PIDs

Suppose $D$ is a **ED** with norm $v$. Then $D$ is a **PID**. (Therefore a **UFD** and **GCD domain**.)

- Consider any ideal $N \sqsubseteq D$.
- Suppose $N$ is the zero ring. $N = \p 0$.
- Suppose $N$ contain nonzero elements.
  - There exists a $p$ of the lowest $v(p)$ in $N$.
  - For all $a \in N$, there exists $p, r \in D$, such that $a = bp + r$, and $v(r) < v(p)$.
  - But $r = a - bp \in N$ as well. So $r = 0$, and $a = bp$.
  - So $N = \p p$.

##### Euclidean algorithm

Suppose $D$ is a **ED** with norm $v$. Given $a, b \in D$, we can compute $\GCD_D(a, b)$ in the following way:

- Start with $r_0 = a, r_1 = b$, where $r_1 \neq 0$.
- Given $r_{i}$ and $r_{i + 1} \neq 0$, by division with remainder,
  $$
  \exists r_{i + 2}, q_{i + 1} \in D: \s{r_{i} = r_{i + 1} q_{i + 1} + r_{i + 2}\land v(r_{i + 2})<v(r_{i + 1})}
  $$
- Since $v(r_i)$ is strictly decreasing, there exists a minimum $N \in \N$ where $r_{N + 1} = 0$.
- For $i < N$, we have $\GCD(r_{i}, r_{i + 1}) = \GCD(r_{i + 1}, r_{i + 2})$.
- Therefore $\GCD(a, b) = \GCD(r_N, 0) = r_N D^*$.

##### Uniqueness of Euclidean division

Suppose $D$ is a ED with norm $v$.

Suppose $a, b \in D$, and $b \neq 0$, there exists $q, r \in D$ such that $a = qb + r$, where $v(r) < v(b)$.

Uniqueness of division is guaranteed in at least two trivial cases:
- $a = 0$ then we must have $q = r = 0$.
- $a = -b$ then we must have $q = -1, r = 0$.

Now consider $a, b \in D - \c{0}$ and $(a + b) \neq 0$. Division is unique in this case if and only if
$$
v(a + b) \le \max\c{v(a), v(b)}
$$

- $\to$ Prove the contrapositive. Suppose $v(a + b) > \max\c{v(a), v(b)}$.
  - Division of $a$ by $a + b$ with remainder has at least two distinct solution:
    - $a = (a + b)0 + a$.
    - $a = (a + b)1 + (-b)$.
- $\from$ Prove by contradiction. Suppose the Euclidean division of $a$ by $b$ has two distinct solutions.
  - $a = qb + r$ and $a = q' b + r'$, where $q \neq q'$ and $r \neq r'$.
  - Therefore $0 = (q - q') b + (r - r')$.
  - $v(b) \le v((q - q')b) = v(r - r') \le \max(v(r), v(r')) < v(b)$. Contradiction!

