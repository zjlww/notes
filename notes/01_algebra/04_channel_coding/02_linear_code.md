#### Linear Code

> Suppose $\bF$ is a finite field. Then $\bF^n$ is a vector space over $\bF$.

##### Linear code

A **linear code** $L$ is a **linear subspace** of $\bF^n$.

The class of all linear codes in $\bF^n_q$ of dimension $k$ and minimum distance $d$ is denoted as $[n, k, d]_q$.

In coding theory, we use the convention where codewords correspond to **row vectors** $u \in \bF^{1 \times k}$.

- $r = n - k$ is called the **redundancy** of the linear code.
- Any matrix $G \in \bF^{k \times n}$ whose row space $\row(G) = \col(G^T) = \span\p{G_{i, \cdot}}_{i = 1}^k = L$, is called a **generator matrix** of linear code $L$.
- Any matrix $H \in \bF^{(n - k) \times n}$ whose null space $\null(H) = \c{x \in \bF^{n}: Hx = 0} = L$, is called a **parity check matrix** of linear code $L$.

##### Permutation equivalence

Suppose $\sigma \in S_n$ is a permutation on $\c{1, \ldots, n}$.

- For $c = (c_1, \ldots, c_n) \in \bF^n$, define $\sigma(c) := (c_{\sigma(1)}, \ldots, c_{\sigma(n)})$.
- Define $P_{\sigma} \in \c{0, 1}^{n \times n}$ as $(P_\sigma)_{ij} = 1(i = \sigma(j))$.
  - It is called the **column permutation matrix**.
  - It permutes columns by $\sigma$ when acting on the right. Since
    $$
    (AP_{\sigma})_{ik} = A_{ij} (P_{\sigma})_{jk} = A_{ij} 1(j = \sigma(k)) = A_{i, \sigma(k)}
    $$
  - It is straight forward to give the inverse matrix of $P_{\sigma}$, since
    $$
    (P_{\sigma^{-1}})_{ij} = 1(i = \sigma^{-1}(j)) = 1(j = \sigma(i)) = (P_\sigma)^{-1} = P_{\sigma}^T
    $$
  - $\det P_\sigma = \operatorname{sgn}(\sigma)$, which is a basic fact from linear algebra.
- Block code $C \subseteq \bF^n$ and $\sigma[C]$ are called **permutation-equivalent**.
  - It is an equivalence relationship on block codes on $\bF^n$.

##### Standard form of the generating matrix

Given a generating matrix $G \in \bF^{k \times n}$ of linear code $L$.

- First reduce $G$ into RREF by row operations, represented by left application of $E \in \bF^{k \times k}$.
- Next, permute all leading columns to the left by apply $P_{\sigma}$ to the right.

$$
G' = EGP_\sigma =\left[\begin{array}{ccccccc}
1 & 0 & \ldots & 0 & b_{1, m+1} & \ldots & b_{1 n} \\
0 & 1 & \ldots & 0 & b_{2, m+1} & \ldots & b_{2 n} \\
& \vdots & & \vdots & & \vdots & \\
0 & 0 & \ldots & 1 & b_{m, m+1} & \ldots & b_{m n}
\end{array}\right] = [I_k | A]
$$

where $I_k \in \bF^{k \times k}, A \in \bF^{k \times (n - k)}$. $G'$ is a generating matrix of **permuted linear code** $L' = \sigma[L]$.

The generating matrix $G'$ is said of the **standard form**.

Similarly, we can transform any parity check matrix $H$ into $EHP_{\sigma} = H' = [B| I_{n - k}]$, which is the **standard form** of a parity check matrix.

##### Compute $H$ from $G$

Given generating matrix $G \in \bF^{k \times n}$, first transform it into the standard form.

- Reduce $G$ into RREF by left application of $E$.
- Permute columns of $G$ into $[I_k | A]$ with right application of $P_{\sigma}$.

That is $G' = EGP_{\sigma} = [I_k | A]$. Now define $H' = [-A^T | I_{n - k}]$.

- Clearly $H'$ has full rank, and $H' (G')^T = \O$.
- Observe that
  $$
  H'(G')^T = H'(EGP_{\sigma})^T = H'P_{\sigma^{-1}} G^T E^T = \O \implies H' P_{\sigma^{-1}}G^T = \O
  $$
- Now define $H = H'P_{\sigma^{-1}}$.

$H$ is the desired parity check matrix.

##### Compute $G$ from $H$

Given parity check matrix $H \in \bF^{(n - k) \times n}$, first transform it into the standard form.

- Reduce $H$ into RREF by left application of $E$.
- Permute columns of $H$ into $[B|I_{n -k}]$ with right application of $P_{\sigma}$.

That is $H' = EHP_{\sigma} = [B|I_{n - k}]$. Now define $G' := [I_k | -B^T]$.

- Clearly $G'$ has full rank, and $H' (G')^T = \O$.
- Observe that
  $$
  H'(G')^T = EHP_{\sigma}(G')^T = E H (G'P_{\sigma^{-1}})^T = \O \implies H(G' P_{\sigma^{-1}})^T = \O
  $$
- Now define $G = G'P_{\sigma^{-1}}$.

$G$ is the desired generating matrix.

##### Dual code

Given linear code $L \subseteq \bF^n$, with a generating matrix $G$ and parity check matrix $H$.

There exists a unique linear code $L^\perp \subseteq \bF^n$ with generating matrix $H$ and parity check matrix $G$.

$L^\perp$ is called the dual code of $L$.

- Since $GH^T = \O_{k \times(n - k)}$, we have $HG^T = \O_{(n - k) \times k}$.
- $\dim L + \dim L^\perp = n$.

##### Minimum weight and distance of linear codes

Suppose $L \subseteq \bF^n$ is a linear code with generator matrix $G \in \bF^{k \times n}$ and parity check matrix $H \in \bF^{(n - k) \times n}$.

We have $d(L) = w(L)$ (minimum distance = minimum weight).
$$
d(L) = \min_{x, y \in L} d(x, y) = \min_{x, y \in L} d(0, y - x) = \min_{z \in L} w(z) = w(L)
$$
$w(L)$ is directly encoded in $H$. Note that $w(L) = i$ if and only if:

- Any $i - 1$ columns in $H$ are linearly independent.
  - Otherwise there would be a codeword of weight less than $w(L)$.
- There exists $i$ columns in $H$ that are linearly dependent.

##### Syndrome and cosets

Given linear code $L \subseteq \bF^n$ with parity check matrix $H$.

Suppose $w \in \bF^k$ is encoded into $x \in \bF^n$. And the received word is $y \in \bF^n$.

Suppose $y = x + e$ where $e \in \bF^n$ is the **error**. The **syndrome** of $y$ is defined as
$$
\syn(y):= H y^T = H(x + e)^T = H e^T
$$
- $\syn: \bF^n \to \bF^{n - k}$ is a linear map by definition.
- $\syn$ is surjective, since $H$ has full rank.
- $\null(\syn) = L$, since $H$ is the parity check matrix of $L$.
- $\syn(y) = \syn(x + e) = \syn(e)$.

There is a one-to-one correspondence between cosets in $\bF^n / L$ and syndromes in $\bF^{n - k}$.

- By fundamental theorem of linear maps, $\bF^{n - k} \simeq \bF^n / L$.

##### Syndrome decoding

Syndrome decoding is an efficient way to implement minimum distance decoding of linear codes.

Consider $[n, k]$-linear code $L \subseteq \bF^n$.

- Define the **weight of coset** $w(x + L)$ as the minimum weight of all vectors in $x + L$.
- $v \in x + L$ is called the leader of coset $x + L$ if $w(v) = w(x + L)$.
- A coset of weight at most $P_r(L)$ has a unique coset leader.
  - Suppose $v$ is a coset leader of $x + L$ where $w(x + L) \le P_r(L)$.
  - Then for all $u \in x + L$, $d(u, v) \ge d(L)$.
  - Therefore $d(u, 0) = w(u) \ge {d(L) - w(v)} > w(v)$.

**Syndrome decoding** is the following implementation of minimum distance decoding:

1. Precompute a table pairing syndromes with coset leaders.
   - Note that some syndromes may not have a unique coset leader.
2. For each received $y \in \bF^n$, compute the syndrome $s = \syn(y)$.
3. Suppose $e \in \bF^n$ is the coset leader, return ${\hat x} =y - e$.
