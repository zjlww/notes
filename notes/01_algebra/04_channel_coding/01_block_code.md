#### Block Code

> In this section, we assume that $Q$ is a finite set where $q:=|Q|$.
>
> For $c \in Q$, we sometimes denote $c^n := (c,\cdots, c) \in Q^n$.
>
> Reference: https://feog.github.io/

##### Hamming distance

Suppose $a, b \in Q^n$. The hamming distance is defined as:
$$
d(a, b) := \sum_{i = 1}^n 1(a_i \neq b_i)
$$
$(Q^n, d)$ is a **bounded metric space**, as the reader should verify.

- Define **closed ball** $B_{\rho}(x): = \{y \in Q^n: d(x, y) \le \rho\}$, (also called Hamming spheres).
- Define **annulus** $A_\rho (x) : \{y \in Q^n: d(x, y) = \rho\}$.
- The **volume of the annulus** of radius $\rho$ is $|A_\rho(x)| = C_n^\rho (q - 1)^\rho$.
- The **volume of the ball** of radius $\rho$ is $|B_\rho(x)| = \sum_{r = 0}^\rho |A_r(x)|$.
  - $|B_\rho(x)| = \sum_{i = 0}^\rho C_n^i$ when $q = 2$.
- We can just write $|B_\rho|$, $|A_\rho|$, since they do not depend on the center.

The **hamming weight** of $a \in Q^n$ is defined as $w(a) := d(a, 0^n)$ if $Q$ is a finite field.

##### Block code

Any nonempty subset of $Q^n$ is called a **block code** on $Q^n$.

An **injective** function $E: Q^k \to Q^n$ is called an **encoding (function)**.

- It maps the **message** $m \in Q^k$ to its **codeword** $E(m)$.

$C = E[Q^k]$ is called a $(n, k)$ **block code** over $Q$.

- $n$ is called the **block length**.
- $k$ is called the **message length** / **dimension**.
- $R = k / n$ is called the **code rate**.

##### Minimum distance and weight

For block code $C$, define

- $d(C):= \min\{ d(a, b): a, b \in C, a \neq b \}$ as the **minimum distance** of code $C$.
- $w(C):= \min\{w(v): v \in C, v \neq 0\}$ as the **minimum weight** of code $C$.

##### Transforming block codes

Given block code $C \subseteq Q^n$. We can represent it as a table (matrix) in $A = Q^{M \times n}$. Define the following transforms on $A$ and $C$.

- Drop a column in $A$ to obtain $C'$ with $A' \in Q^{M \times(n - 1)}$, where $n \ge 2$.
  - $d(C') \in \c{d(C), d(C) - 1}$.
- Zero a column in $A$ to obtain $C'$.
  - $d(C') \in \c{d(C), d(C) - 1}$.
- Add a column to $A$ to obtain $C'$.
  - $d(C') \in \c{d(C), d(C) + 1}$.


##### Classes of block code

Define $(n, M, d)_q$ as the class of block codes with $M$ codewords of length $n$ and minimum distance $d$ over a $q$-ary alphabet. Define $(n, k, d)_q$ as the class of codes with $M = q^k$.

We write $(n, M)_q$ and $(n, k)_q$ to remove the restriction on the minimum distance.

When $(n, M, d)_q$ is non-empty. $(n, M, d')_q$ for $1 \le d' < d$, and $(n - 1, M, d-1)_q$ are non-empty.

- By zeroing / dropping columns in $C \in (n, M, d)_q$.

A non-standard notation we use is $(n, M, [a, b])_q := \cup_{d = a}^b (n, M, d)_q$.

##### Maximum block code size given minimum distance

Define $A_q(n, d)$ for $n, q, d \in \N^+$ as the maximum $M$ where the block code class $(n, M, d)_q$ is not empty.
- $A_q(n, 1) = q^n$, since all codes are allowed.
- $A_q(n, n) = q$. Obtained by $0^n, 1^n, 2^n, \cdots, (q-1)^n$.

##### Packing radius of block code

Suppose block code $C\subseteq Q^n$. The **packing radius** of $C$ is
$$
P_r(C) := \max\{r \in \N: \forall a \neq b \in C: B_r(a) \cap B_r(b) = \varnothing \}
$$
- Suppose $d(C)$ is odd, $2P_r(C) = d(C) - 1$.
- Suppose $d(C)$ is even, $2P_r(C) = d(C) - 2$.
- In general, $P_r(C) = \lfloor (d(C) - 1) / 2\rfloor$.

##### Covering radius of block code

Suppose block code $C \subseteq Q^n$. The covering radius of $C$ is
$$
C_r(C) := \min\left \{\rho \in \N: Q^n \subseteq \bigcup_{c \in C} B_\rho (c)\right\} =^* \max_{x \in Q^n} \min_{c \in C} d(x, c)
$$
The proof for $(*)$ is straight forward, notice that for any $\rho \in \N$:
$$
\rho < \max_{x \in Q^n} \min_{c \in C} d(x, c) \iff \exists x \in Q^n, \exists c \in C: d(x, c) > \rho \iff \rho < C_r(C)
$$
##### Perfect code

Consider block code $C \subseteq Q^n$. In general, we have $P_r(C) \le C_r(C)$.

A block code $C$ is called **perfect**, if $P_r(C) = C_r(C)$.

- Intuitively, the union of all closed balls of radius $P_r(C)$ around each codeword $c \in C$ completely fills $Q^n$ in perfect codes.
- The Hamming code, and Golay code are perfect.

A block code $C$ is called **quasi-perfect** if $P_r(C) + 1 = C_r(C)$.

#### Bounds for Block Codes

##### Singleton bound

Suppose $C \in (n, M, d)_q$. Remove $d - 1$ columns from $C$ to get $C' \in (n - d + 1, M, [1, d])_q$.

Therefore
$$
|C| = |C'| = M \le A_{q}(n - d + 1, 1) = q^{n - d + 1}
$$
Therefore $A_{q}(n, d) \le q^{n - d + 1}$, which is the **singleton bound**.

##### Hamming bound

Suppose $C \in (n, M, d)_q$. Let $r = P_r(C) = \lfloor (d - 1)/2\rfloor$. We have:
$$
\sum_{c \in C}|B_{r}(c)| = M |B_r| = M \sum_{i = 0}^r C_n^i (q - 1)^i \le q^n
$$
The equality is obtained if and only if $C$ is perfect.

Equivalently, $A_q(n, d) \le q^n/|B_r|$, which is the **Hamming bound** / **Sphere packing bound**.

##### Gilbert bound

Consider a block code $C \in (n, M, d)_q$, where $M = A(n, d)_q$.

For all $x \in Q^n$, there exists a $c \in C$ where $d(x, c) \le d - 1$.

- Otherwise, $C' = \c{x} \cup C \in (n, M+1, d)_q$. A contradiction to $M = A(n, d)_q$.

Therefore $Q^n \subseteq \bigcup_{c \in C} B_{d - 1}(c)$, and we have the **Gilbert bound**:
$$
A_q(n, d)  \ge \frac{q^n}{\abs{B_{d - 1}}} = \frac{q^n}{\sum_{i = 0}^{d-1} C_n^i (q-1)^i}
$$
#### Decoding Block Codes

##### Error detection and correction

Suppose $C \subseteq Q^n$ is a block code.

- The code $C$ can **detect** up to $d(C) - 1$ errors.
  - Since changing $c \in C$ in at most $d(C) - 1$ coordinates does not give another codeword in $C$.
- The code $C$ can **correct** up to $P_r(C)$ errors.
  - Since changing $c \in C$ in at most $P_r(C)$ coordinates does not change the closest codeword in $C$.

#### Decoding Block Code

##### Discrete channel

A **discrete channel** is described by a pair of discrete random variable $(X, Y)$ on some probability space $(\Omega, \F, P)$. $X$ represents the input and $Y$ represents the output.
$$
P(X = x, Y = y) = P(Y = y \mid X = x) P(X = x) = p(y|x) p(x)
$$

- $p(y|x)$ and $p(x)$ are abbreviations for $P(Y = y | X = x)$ and $P(X = x)$.
- $\X = X[\Omega]$ and $\Y = Y[\Omega]$ are finite sets.

When $\X = \Y = Q$ where $|Q| = q$, the channel is called a **$q$-ary channel**.

A $q$-ary channel with the following probability density for $p \in (0, 1/2)$ is called a **$q$-ary symmetric channel**.
$$
p(y | x) = \begin{cases}
1 - p & x = y\\
p / (1 - q)& x \neq y
\end{cases}
$$
##### Independent symmetric channel

For block code on $Q^n$, we often assume the following channel.

- Let $\symbf X = (X_1, \ldots, X_n)$ be $Q$-valued random variables representing the sent block.
- Let $\symbf Y = (Y_1, \ldots, Y_n)$ be $Q$-valued random variables representing the received block.
- The channel add noise to each bit independently:
  $$
  p(y_1\ldots y_n \mid x_1\ldots x_n) = \prod_{i = 1}^n p(y_i | x_i)
  $$
- And for each bit the channel acts like a $q$-ary symmetric channel with error probability $p \in (0, 1/2)$.
  $$
  p(y_i | x_i) = \begin{cases}
  1 - p & x_i = y_i\\
  p / (1 - q)& x_i \neq y_i
  \end{cases}
  $$

##### Decoding methods

Consider block code $C \subseteq Q^n$, and discrete channel $p(y| x)$.

Suppose the received word is $y \in Q^n$, and the decoding result is $\hat x \in C$.

We have the following decoding methods:

- (Maximum likelihood, ML) $\hat x = \arg\max_{x \in C} p(y | x)$.
- (Maximum a posteriori probability, MAP) $\hat x = \arg\max_{x \in C} p(x | y)$.
  - Note that $p(x | y) \propto p(y | x) p(x)$. $p(x)$ is called the prior distribution.
  - ML is equivalent to MAP with uniform prior.
- (Minimum distance, MD) $\hat x = \arg\min_{x \in C} d(x, y)$.
  - MD is equivalent to ML under independent symmetric channel.
