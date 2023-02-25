#### Cyclic Code

> We use the non-standard notation where $A \sqsubseteq R$ means $A$ is an ideal of $R$.

##### Cyclic code

A **cyclic code** $C \subseteq \bF^n$ of length $n$ over field $\bF$ is a linear code where
$$
(a_0, \cdots, a_{n - 1}) \in C \implies (a_{n - 1}, a_0, \cdots, a_{n - 2}) \in C
$$
Let's associate $\bF^n$ with $R_n := \bF[x] / \p{x^n - 1}$.

- For $f(x) \in \bF[x]$, define $[f] := f + \p{x^n - 1} \in R_n$.

  - We abuse the notation a little bit by writing $[A] := \c{[a]: a \in A}$ for $A \subseteq \bF[x]$.

  - Then we have
    $$
    R_n = \bF[x] / (x^n - 1) = [\bF[x]] = \c{[f]: f \in \bF[x], \deg f < n}
    $$

- Define injective linear map $\phi: \bF^n \to \bF[x]$ as:
  $$
  \phi(c_0, c_1, \ldots, c_{n - 1}) := c_0 + c_1 x + \cdots + c_{n - 1}x^{n - 1}
  $$

- Define bijective linear map $\varphi: \bF^n \to R_n$ as:
  $$
  \varphi(c_0, c_1, \cdots, c_{n-1}) := \s{c_0 + c_1 x + \cdots  +c_{n-1}x^{n-1}}
  $$

- Shift right in $\bF^n$ is equivalent to a multiplication by $[x]$ in $R_n$.
  $$
  [x] \varphi(c_0, \cdots, c_{n - 1}) = \varphi(c_{n - 1}, c_0, \cdots, c_{n - 2})
  $$

There is a one-to-one correspondence between cyclic codes on $\bF^n$ and ideals of $R_n$. For linear code $C \subseteq \bF^n$, the following statements are equivalent:

1. $C$ is cyclic.
1. $\forall [f(x)] \in \varphi[C]: [x][f(x)] \in C$.
1. $\forall [f(x)] \in \varphi[C], \forall [p(x)] \in R_n: [p(x)][f(x)] \in C$.
1. $\varphi[C]$ is an ideal of $R_n$.


##### Ideals of ring $R_n$

The ring $R_n = \bF_q[x] / (x^n - 1)$ is a **principal ideal ring**.

Consider any ideal $I \sqsubseteq R_n$. It can be shown that $I$ is a principal ideal.

- Let $r = \c{\deg f(x): [f] \in I, f \in \bF[x], f \neq 0}$. Clearly $0 \le r < n$.
- There exists a **unique monic** $g(x) \in \bF[x]$ where $[g] \in I$ and $\deg g = r$.
  - Suppose $g_1$ and $g_2$ are both such polynomials and $\deg g_1 = \deg g_2 = r$.
  - Then $[g_1 - g_2] \in I$, and $\deg (g_1 - g_2) < \deg g = r$. Contradiction!
- Clearly $\a{[g]} \subseteq I$. It can be shown that $\a{[g]} \supseteq I$.
  - Consider any $[p] \in I$, where $p \in \bF[x]$.
  - With division algorithm on $\bF[x]$, $p = u \cdot g + v$ where $\deg v < r$.
  - Therefore $[p] = [u \cdot g + v] = [v]$. So $v = 0$.
  - Therefore $[p] \in \a{[g]}$.

$g$ is called the **generator polynomial** of $I$.

- Note that $g$ is not the only polynomial $f \in \bF[x]$ where $\a{[f]} = I$.

Suppose $\deg g = r$, we have $\dim I = (n - r)$.

- $g \mid x^n - 1$.
  - With division algorithm on $\bF[x]$, $x^n - 1 = u \cdot g + v$, where $\deg v < \deg g$.
  - Therefore $[x^n - 1] = [0] = [u \cdot g + v]$. So $[v] = [-u \cdot g]$.
  - This is only possible when $v = 0$.
- Let $h(x) = (x^n - 1) / g(x)$. $\deg h = n - \deg g = n - r$.
- $I$ is a $(n - r)$ dimensional linear space over $\bF$.
  - Consider any $[f][g] \in I$, where $f \in \bF[x]$.
  - With division algorithm on $\bF[X]$, $f = u \cdot h + v$, where $\deg v < n - r$.
  - Then $[f][g] = [u \cdot h + v][g] = [v\cdot g]$.
  - Therefore $I = \c{[v][g]: v \in \bF[x], \deg v < n - r}$.
- A basis of $I$ is $\c{[g], [x][g], \ldots, [x^{n - r - 1}] [g]}$.
  - $\sum_{i = 0}^{n - r - 1} c_i[x^i][g] = \s{\sum_{i = 0}^{n - r - 1} c_i x^i}[g] = 0$ has only the trivial solution.

Let $h = (x^n - 1) / g$. Then $I = \c{[p] \in R_n: [p \cdot h] = [0]}$.

- Define $A$ to be the set on the right hand side.
- $A \supseteq I$.
  - For $[fg] \in I$ where $f \in \bF[x]$, $[fg\cdot h] = [f (x^n - 1)] = 0$.
  - Therefore $[fg] \in A$.
- $A \subseteq I$.
  - For $[p] \in A$ where $[p h] = 0$.
  - With division algorithm on $\bF[x]$, $p = u \cdot g + v$, where $\deg v < \deg g$.
  - Then $[ph] = [u g h + v h] = [vh] = 0$. So $v = 0$.
  - Therefore $[p] = [u][g] \in I$.

Any monic polynomial $p(x) \in \bF[x]$ where $p(x) \mid x^n - 1$ is a generator polynomial of some ideal $I_p \sqsubseteq R_n$.

- Define $I_p := \a{[p]}$. Suppose $I_p$ has generator polynomial $g$.
- We need to show that $g = p$.
  - Let $x^n - 1 = p \cdot f$.
  - Since $[g] \in I_p$, $[g] = [a][p]$ for some $a \in \bF[x]$. So $[gf] = [apf] = [0]$. So $\deg g \ge \deg p$.
  - But $\deg g < \deg p$, by the definition of generator polynomial. Contradiction!

There is a one-to-one correspondence between factors of $x^n - 1$, ideals of $R_n$, and cyclic codes on $\bF^n$.

##### Cyclic generator matrix and parity check matrix of cyclic codes

Consider cyclic code $C \subseteq \bF^n$. Suppose $\varphi[C]$ has generator polynomial $g \in \bF[x]$, with $\deg g = r$.

- We also call $g(x)$ the **generator polynomial** of code $C$;
- $h(x) = (x^n - 1) / g(x)$ is called the **parity check polynomial** of code $C$.

A **cyclic generator matrix** $G$ of $C$ can be directly generated from coefficients of $g(x)$.

- Suppose $g(x) = \sum_{i = 0}^r g_i x^i$. Recall that a basis of $\varphi[C]$ is $\c{[g], [x][g], \cdots, [x^{n - r - 1}][g]}$.

- Therefore a generator matrix of $C$ is given by:
  $$
  G=\left[\begin{array}{ccccccc}
  g_0 & g_1 & \cdots & g_{r} & 0 & 0 & 0 \\
  0 & g_0 & g_1 & \cdots & g_{r} & 0 & 0 \\
  \vdots & \vdots & \ddots & \ddots & \ddots & \ddots & 0 \\
  0 & 0 & 0 & g_0 & \cdots & g_{r-1} & g_{r}
  \end{array}\right] \in \bF^{(n - r) \times n}
  $$
  
- Encoding a message with $G$ is equivalent to polynomial multiplication in $R_n$.

  - For message $\mathbf m = (m_0, \ldots, m_{k - 1})$, define $[m(x)] := [m_0 + m_1 x + \cdots + m_{k - 1} x^{k - 1}]$.
  - $\varphi(\mathbf m G) = [m(x) g(x)]$.


A **cyclic parity check matrix** $H$ of $C$ can be directly generated from coefficients of $h(x)$.

- Suppose $h(x) = \sum_{i = 0}^{k} h_i x^i$ where $k = n - r$.

- A parity check matrix of $C$ is given by:
  $$
  H=\left[\begin{array}{ccccccc}
  h_k & h_{k-1} & \cdots & h_0 & 0 & 0 & 0 \\
  0 & h_k & h_{k-1} & \cdots & h_0 & 0 & 0 \\
  \vdots & \vdots & \ddots & \ddots & \ddots & \ddots & 0 \\
  0 & 0 & 0 & h_k & \cdots & h_1 & h_0
  \end{array}\right] \in \bF^{r \times n}
  $$

  - Clearly $\rank H = r$.
  - $HG^T = \O$.
    - Recall that $g(x) h(x) = x^n - 1$. Define $a_{n} = a_0 = 1$ and $a_{m} = 0$ for $1 \le m \le n - 1$.
    - Let $0 \le i \le r - 1$ and $0 \le j \le k - 1$.
    - $(HG^T)_{i+1, j + 1} = \prod_{k = 1}^nH_{i + 1, k} G_{j+ 1, k} = a_{k + i - j}$.
    - Since $1 \le k + i - j\le n - 1$, all elements in $HG^T$ are zero.
  
- Parity check with $H$ is equivalent to polynomial multiplication in $R_n$.

  - Suppose codeword $\mathbf c = (c_0, \ldots, c_{n - 1})$ is transmitted.
  - Suppose $\mathbf r = (r_0, \ldots, r_{n - 1})$ is received with error vector $\mathbf e$. And $\mathbf r = \mathbf c + \mathbf e$.
  - Recall that the syndrome is $\mathbf s = H \mathbf r^T = H \mathbf e^T$.
  - Let $c(x) = \phi(\mathbf c)$, $r(x) = \phi(\mathbf r)$, $e(x) = \phi(\mathbf e)$, and $s(x) = \phi(\mathbf s)$.
  - $[h(x) r(x)] = [h(x) e(x)]$.
  - And $\mathbf s =H \mathbf r^T$ happens to be the coefficients of $x^k, x^{k + 1}, \ldots, x^{n - 1}$ in $h(x) r(x)$.

##### Dual codes of cyclic codes

Consider the dual linear code $C^\perp \subseteq \bF^n$. Proceed in the field $\bF(x)$.

Given cyclic code $C \subseteq \bF^n$ with generator polynomial $g(x)$, and $h(x) = (x^n - 1) / g(x)$. Where $\deg g(x) = r$ and $\deg h(x) = k$.

- $C^\perp$ is cyclic with generator polynomial $g^{\perp}(x) := x^k h(x^{-1}) \in \bF[x]$.
- $g^\perp(x) \mid x^n - 1$. Since $x^n - 1 = g^\perp(x) (-x^r g(x^{-1}))$.

##### Standard generator matrix of cyclic codes

Consider cyclic code $C \subseteq \bF^n$ with generator polynomial $g(x) \in \bF[x]$ and $\deg g(x) = r$.

Suppose $m(x) = \phi(\mathbf m)$ is the message polynomial, observe the following:

- With division algorithm in $\bF[x]$, $x^r m(x) = u(x) g(x) + v(x)$ where $\deg v(x) < r$.
- Therefore $[x^r m(x) - v(x)] = [u(x) g(x)]$.
- Consider encoding function $E(\mathbf m) := \varphi^{-1}\p{[x^k][x^r \phi(\mathbf m) - \phi(\mathbf m) \bmod g(x)]}$.
  - $E$ is clearly linear over $\bF$, since all functions involved are linear over $\bF$.
  - $E: \bF^k \to \bF^n$ is injective. Since $\null E = \c{\mathbf 0}$.
- The matrix of $E$ under the standard basis of $\bF^k$ and $\bF^n$ is a standard generator matrix $G = [I_k | A] \in \bF^{k \times n}$.


##### Zeros of cyclic code

Consider cyclic code $C \subseteq \bF^n$ with generator polynomial $g \in \bF[x]$, with $\deg g = r$.

Now let's work in some algebraic closure $\overline \bF$ of $\bF$. The following are clearly equivalent for all $f \in \bF[x]$:

1. $g \mid f$.
2. $f[R] = \c{0}$.
   - $R := \c{\alpha_1, \ldots, \alpha_r} \in \overline \bF$ contains the roots of $g(x)$ in $\overline \bF$.
   - $R$ is called the **set of zeros** of $C$.
   - Actually, considering all roots in $R$ is redundant.
     - Recall that $f(\alpha) = 0$ implies $\irr(\alpha, \bF) \mid f$. All conjugates of $\alpha$ are also roots of $f(x)$.
     - Suppose $g = m_1^{r_1} \cdots m_d^{r_d}$ where $m_1,\ldots, m_d \in \bF[x]$ are irreducible.
   - Any $R$ that contains at least one root from each $m_k$ is fine.
3. $[fh] = [0]$.
4. $[f] \in I$.

Therefore we have:
$$
\varphi[C] = \c{[f] \in R_n: [f h] = [0]} = \c{[f] \in R_n: f[R] = 0}
$$
Suppose $R = \c{\alpha_1, \ldots, \alpha_m}$, the condition $f[R] = 0$ can be expressed as the following matrix vector product for $f(x) = f_0 + f_1 x + f_2 x^2 + \cdots + f_{n - 1} x^{n - 1}$.
$$
\left[\begin{array}{ccccc}
\alpha_1^0 & \alpha_1^1 & \alpha_1^2 &\cdots & \alpha_1^{n-1} \\
\alpha_2^0 & \alpha_2^1 & \alpha_2^2 &\cdots & \alpha_2^{n-1} \\
\vdots & \vdots & \vdots & & \vdots\\
\alpha_m^0 & \alpha_m^1 & \alpha_m^2 &\cdots & \alpha_m^{n-1}
\end{array}\right]\left[\begin{array}{c}
f_0 \\
f_1 \\
f_2 \\
\vdots \\
f_{n-1}
\end{array}\right]= \mathbf 0
$$
The parity check matrix $\mathcal H \in \bF[K]^{m \times n}$ can be transformed into a matrix in $\bF^{r \times n}$.

##### Binary Hamming code

The binary Hamming codes are $[n, k]_2$ cyclic codes with $r = n - k$ and $n = 2^r - 1$.

A primitive polynomial in $\bF_2[x]$ of degree $r$ generates a binary Hamming code.

- Let $\omega$ be a $n$-th primitive root of unity. And $g(x) := \irr(\omega, \bF)$.

  - Note that $x(x^n - 1)$ is the defining polynomial of finite field $\bF_{2^r}$.
  - Therefore $\deg g(x)= r$. And $o(g) = o(\omega) = n$.

- Hamming code is the cyclic code with generator polynomial $g(x)$.

- A parity check matrix $\mathcal H$ in $\bF_{2^r}$ is given by
  $$
  \mathcal H = [\omega^0, \omega^1, \ldots, \omega^{n - 1}]
  $$

  - The corresponding matrix $H$ in $\bF_2$ contains **all possible non-zero columns** of length $r$.

- The rate of Hamming codes is $R = k / n = 1 - r / (2^r - 1)$.

##### Example: [7, 4]-Hamming Code

Take $r = 3$, $n =2 ^ 3 - 1 = 7$. Recall that $1 + x + x^3$ and $1 + x^2 + x^3$ are both primitive.
$$
x^7 - 1 = (1 + x) (1 + x + x^3) (1 + x^2 + x^3)
$$
Take $g(x) = 1 + x + x^3$ and suppose $g(\omega) = 0$ for $\omega \in \bF_{8}$. Therefore
$$
\begin{aligned}
\omega^0 &= 1 & \omega^1 &= x & \omega^2 & = x^2 & \omega^3 & = 1 + x\\\omega^4 & = x + x^2 &
\omega^5 & = 1 + x + x^2 & \omega^6 & = 1 + x^2 & \omega^7 & = 1
\end{aligned}
$$
A parity check matrix is given by:
$$
\mathcal H  = [\omega^0, \omega^1, \ldots, \omega^{6}] \to H = \left[\begin{array}{lllllll}
1 & 0 & 0 & 1 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 & 1 & 1 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 & 1
\end{array}\right]
$$
