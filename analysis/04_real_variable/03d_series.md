#### Infinite Series

(**Vector series**)

Consider **infinite sequence** $(c_n)_{n = 1}^\infty \in V$. Where $V$ is a **normed vector space** over $\mathbf F = \R, \C$.

A **series** is the **action** of adding $c_n$ together. $\sum c_n$ denote both the action and the result.

- $s_n = \sum_{i = 1}^n c_n$ is the sequence of **partial sums**.
- If $s = \lim_n s_n$ exists, we say $\sum c_n$ **converges** to $s$. Or just write $\sum_{k = 1}^\infty c_k = s$.
- $\sum c_n$ converges iff $\sum_{k = n}^\infty c_k \to 0$ as $n \to \infty$.
- If $V$ is **Banach** (a complete normed linear space), $\sum c_n$ converges iff $s_n$ is **Cauchy**.
- $\sum c_n$ converges then $c_n \to 0$ as $n \to \infty$.

$\sum c_n$ is **absolutely convergent** if $\sum\left\|c_{n}\right\|$ converges in $[0, \infty)$.

(**Complex series**)

A complex sequence $(c_n)_{n = 1}^\infty \in \C$  can be decomposed into real sequences.

- $(\re c_n) = (a_n)$ and $(\im c_n) = (b_n)$ are the **real / imaginary parts** of $(c_n)$.
- $\sum c_n$ converge if and only if $\sum a_n$ and $\sum b_n$ converge.
- $\sum |c_n|$ converge if and only if $\sum |a_n|$ and $\sum|b_n|$ converge.

(**Harmonic series**)

Consider the **harmonic series** $\sum_{n=1}^\infty 1/n$.

The harmonic series diverges. We can show that the partial sum is not Cauchy.
$$
\forall m \in \N: \frac{1}{2^{m}+1}+\cdots+\frac{1}{2^{m}+2^{m}} \geq \frac{2^{m}}{2^{m}+2^{m}}=\frac{1}{2}
$$
(**Merge and splitting terms**)

Suppose $(a_n)_{n = 1}^\infty \subseteq V$ where $V$ is a normed space.

Suppose $p: \N \to \N^+$. And $p$ is **strictly increasing**. And $p(0)=0$.

Define $b_n = \sum_{k=p(n-1) +1}^{p(n)} a_k$ for $n \ge 1$.

- $(b_n)$ is obtained from $(a_n)$ by merging terms. And $(a_n)$ is obtained from $(b_n)$ by splitting terms.
- $(a_n)$ is obtained from $(b_n)$ by removing parentheses.
- Suppose $(t_n), (s_n)$ are partial sums of $(b_n)$ and $(a_n)$. Then $t_n = s_{p(n)}$.
- $\sum_{n = 1}^\infty a_n = s \implies \sum_{n = 1}^\infty b_n = s$ (but the reverse is not true).

(**Alternating real series**)

Suppose $(a_n)_{n = 1}^\infty \subseteq (0, \infty)$. Then $b_n = (-1)^{n + 1}a_n$ is an **alternating series** of $(a_n)$.

Suppose $a_n \downarrow 0$, then $\sum b_n$ converges.

- Let $s_n = \sum_{i = 1}^n b_n$ and $s = \sum_{n = 1}^\infty b_n$. $(s - s_n) \to 0$.

  - $(-1)^{n}(s-s_{n})=\sum_{k=1}^{\infty}(-1)^{k+1} a_{n+k}=\sum_{k=1}^{\infty}(a_{n+2 k-1}-a_{n+2 k})>0$.

  - $(-1)^{n}(s-s_{n})=a_{n+1}-\sum_{k=1}^{\infty}(a_{n+2 k}-a_{n+2 k+1})<a_{n+1}$.

(**Rearranging terms and conditional convergence**)

Suppose $(a_n)_{n = 1}^\infty, (b_n)_{n = 1}^\infty \subseteq V$ where $V$ is a normed space.

Suppose $f: \N^+ \to \N^+$ is **bijective**. Suppose $b_n = a_{f(n)}$. Then $(b_n)$ is a **rearrangement** of $(a_n)$.

- $\sum a_n$ is **unconditionally convergent** if every rearrangement of the series has same sum.
- $\sum a_n$ is **conditionally convergent** if $\sum a_{n}$ converges but not unconditionally converges.

If $V$ is **Banach**, absolute convergence implies unconditional convergence.

- Suppose $(a_n)$ is absolutely convergent, any rearrangement of $\p{a_n}$ is Cauchy.

If $V$ is **finite-dimensional**, unconditional convergence implies absolute convergence.

- This result follows from the [Riemann Rearrangement Theorem](https://en.wikipedia.org/wiki/Riemann_series_theorem) on $\R$. ==TODO==
- So we do not distinguish unconditional / absolute convergence in this case.s

(**Decimating terms**)

Suppose $(a_n)_{n = 1}^\infty, (b_n)_{n = 1}^\infty \subseteq V$ where $V$ is a normed space.

Suppose $f: \N^+ \to \N^+$ is **injective**. Suppose $b_n = a_{f(n)}$. Then $(b_n)$ is a subsequence / **subseries** of $(a_n)$.

- Decimation preserves unconditional convergence.
- Decimation preserves absolute convergence.

(**Partitioning terms**)

Suppose $(a_n)_{n = 1}^\infty \subseteq V$ where $V$ is a normed space.

Suppose $(f_k)_{k = 1}^\infty : \N^+ \to \N^+$ are injective. And $\{f_k[\N^+]\}_{k = 1}^\infty \in \P(\N^+)$ is a partition of $\N^+$.

Suppose $s_k = \sum_{n=1}^\infty a_{f_k(n)}$. Consider the sequence $\p{s_k}_{k=1}^\infty \subseteq V$.

- $\sum_{k = 1}^\infty s_k = \sum_{k = 1}^\infty \sum_{n = 1}^\infty a_{f_k(n)}$ by definition.

$\sum s_k$ is absolutely convergent if $\sum a_k$ is absolutely convergent.

- $\sum_{k = 1}^\infty \n{s_k} = \sum_{k = 1}^\infty \n{\sum_{n = 1}^\infty a_{f_k(n)}} \le \sum_{k=1}^\infty \sum_{n=1}^\infty \n{a_{f_k(n)}} = \sum_{n=1}^\infty \n{a_n}$.

$\sum_{k = 1}^\infty s_k = \sum_{n = 1}^\infty a_n$  if $\sum a_k$ is absolutely convergent.

- Given any $\epsilon > 0$.
  - There exists $N$, s.t. $\sum_{k=N+1}^\infty \n{a_n} < \epsilon / 2$.
  - There exists $R$, s.t. $\cup_{k=1}^R f_k[\N^+] \supseteq \c{1, \ldots, N}$.
  - There exists $M \ge R$, s.t. $\sum_{k=M+1}^\infty \n{s_k} < \epsilon / 2$.

- Now $\norm{\sum_{k=1}^\infty s_k - \sum_{k=1}^M s_k} < \epsilon / 2$. And $\norm{\sum_{k=1}^M s_k - \sum_{n = 1}^\infty a_n} < \epsilon / 2$.

#### Convergence Tests

(**Comparison test**)

Suppose $(a_n), (b_n) \subseteq [0, \infty)$.

- Suppose $a_n \le b_n$. Then $\sum b_n$ converge implies $\sum a_n$ converge.
- Suppose $a_n / b_n \to 1$. $\sum a_n$ converges if and only if $\sum b_n$ converges.
- Suppose $a_n = o(b_n)$. $\sum b_n$ converges implies $\sum a_n$ converges.

(**Riemann Zeta function**)

For $s > 1$, $\sum 1 / n^s$ converges.

- Consider the function $f(x) = x^{-s}$.
- For $s \neq 1$, $f(x)$ has primitive $F(x) = x^{-s + 1} / (1 - s)$.
- Since $\int_1^{n} f(x) \dd x$ converges, $\sum 1/n^s$ converges.

$\sum 1 / n$ diverges. For $s \in (0, 1)$, $\sum 1 / n^s$ diverges.

- Since $\int_1^n 1/x \dd x = \ln n$, the integral diverges.

For $s > 1$, $\zeta(s) := \sum_{n=1}^\infty 1 / n^s$ is the **Riemann Zeta function**.

(**Ratio Test**)

Given a series $\sum a_{n}$ of nonzero complex terms, let
$$
r=\liminf _{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|, \quad R=\limsup _{n \rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|
$$
- The series $\sum a_{n}$ converges absolutely if $R<1$.
- The series $\sum a_{n}$ diverges if $r>1$.
- The test is inconclusive if $r \leq 1 \leq R$.

(**Root Test**)

Given a series $\sum a_{n}$ of complex terms, let
$$
\rho=\limsup _{n \rightarrow \infty} \sqrt[n]{\left|a_{n}\right|}
$$
- The series $\sum a_{n}$ converges absolutely if $\rho<1$.
- The series $\sum a_{n}$ diverges if $\rho>1$.
- The test is inconclusive if $\rho=1$.

(**Sum by part**)

If $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are two sequences of complex numbers, suppose $A_n = \sum_{k=1}^n a_n$. Then we have the identity
$$
\sum_{k=1}^{n} a_{k} b_{k}=A_{n} b_{n+1}-\sum_{k=1}^{n} A_{k}\left(b_{k+1}-b_{k}\right)
$$
Therefore, $\sum_{k=1}^{\infty} a_{k} b_{k}$ converges if both the series $\sum_{k=1}^{\infty} A_{k}\left(b_{k+1}-b_{k}\right)$ and the sequence $\left\{A_{n} b_{n+1}\right\}$ converge.

(**Dirichlet's Test**)

Suppose $\sum a_{n}$ is a complex series, $A_n = \sum_{k=1}^n a_k$ is bounded by $M > 0$.

Suppose $\p{b_n}$ is decreasing and positive, and $b_n \downarrow 0$.

Then $\sum a_{n} b_{n}$​ converges.

- $\sum A_k (b_{k+1} - b_k)$ converges. As it is clearly Cauchy.
- $A_n b_{n+1}$ converges, as $A_n$ is bounded and $b_{n + 1} \downarrow 0$.

(**Abel's Test**)

Suppose $\sum a_n$ is a converging complex series.

Suppose $\p{b_n}$ is a real monotonic bounded sequence.

Then $\sum a_n b_n$ converges.

- $\sum A_k (b_{k+1} - b_k)$ converges. As it is clearly Cauchy.
- $A_n b_{n+1}$ converges, since $A_n$ and $b_{n + 1}$ converges.

#### Unordered Series

(**Unsigned unordered series**)

Suppose $\c{x_\alpha}_{\alpha \in A} \subseteq [0, \infty]$. Define
$$
\sum_{\alpha \in A} x_\alpha := \sup_{F \in \mathcal P(A), |F| < \infty} \sum_{n \in F} x_n \in [0, +\infty]
$$
- $S = \{\alpha \in A : x_\alpha > 0\}$ is the **support** of $\c{x_\alpha}$.
- Suppose $\abs{S} > \abs{\N}$, $\sum x_\alpha = \infty$.
  - Hint: define $S_n := \c{x_\alpha > 1/n: \alpha \in S}$.
  - Clearly $S = \cup_n S_n$, and one of the $S_n$ must be uncountable.
- Suppose $\abs{S} = \abs{\N}$, $\sum x_\alpha = \sum x_{g(n)}$ for any rearrangement $g: \N^+ \to A$.

(**Tonelli's Theorem for unsigned unordered series**)

Suppose $x_{\alpha, \beta} \in [0, \infty]$, where $(\alpha, \beta) \in A \times B$.
$$
\sum_{(\alpha, \beta) \in A \times B} x_{\alpha, \beta}=\sum_{\alpha \in A} \sum_{\beta \in B} x_{\alpha, \beta}=\sum_{\beta \in B} \sum_{\alpha \in A} x_{\alpha, \beta}
$$

- This is a generalization of the **partition** theorem with countable $A, B$.

(**Unordered series**)

Suppose $\left\{f_{k}\right\}_{k \in \Gamma}$ is a set in a normed space $V$.

The unordered sum $\sum_{k \in \Gamma} f_{k}$ is said to converge if there exists $g \in V$ such that for every $\varepsilon>0$, there exists a finite subset $\Omega$ of $\Gamma$ such that
$$
\left\|g-\sum_{j \in \Omega^{\prime}} f_{j}\right\|<\varepsilon
$$
for all finite sets $\Omega^{\prime}$ with $\Omega \subseteq \Omega^{\prime} \subseteq \Gamma$.

- If this happens, the $g$ must be **unique**, we set $\sum_{k \in \Gamma} f_{k}=g$.
- If there is no such $g \in V$, then $\sum_{k \in \Gamma} f_{k}$ is left undefined.
- Suppose $\sum_{k \in \Gamma} \n{f_k} < \infty$, the series is **absolutely convergent**.

#### Double Sequences and Double Series

(**Double limit**)

Suppose $V$ is a normed space. And $(f_{p,q})_{p, q \in \N^+} \subseteq V$.

$(f_{p, q})$ is a **double sequence**. And we can define the **double limit**:
$$
\lim_{p, q \to \infty} f_{p, q} = a \iff \forall \epsilon > 0, \exists N \in \N, \forall p, q \ge N: f_{p, q} \in B(a, \epsilon)
$$

- If the limit exists, $\p{f_{p, q}}$ is **double convergent**.  
- $\lim_{p \to \infty} \lim_{q \to \infty} f_{p, q}$ is called a **iterated limit**.
- Suppose $\lim_{p, q \to \infty} f_{p, q} = a$ and $\forall p \in \N^+: \lim_{q \to \infty} f_{p, q} = c_p$. Then the iterated limit $\lim_{p \to \infty}  (\lim_{q \to \infty} f_{p, q}) = a$.
  - Hint: proof with contradiction.


(**Double series**)

Suppose $V$ is a normed space. Consider double sequence $(f_{p,q})_{p, q \in \N^+} \subseteq V$.

$s_{p, q}:=\sum_{m=1}^{p} \sum_{n=1}^{q} f_{m, n}$ is the **double partial sum**.

The double series $\sum f_{p, q}$ is **convergent** if the double partial sum is double convergent.

- Suppose $(f_{p, q}) \in [0, \infty)$. Then $\sum_{p, q} f_{p, q}$ converges if $\{s_{p, q}\}_{p, q \ge 1}$ is bounded.
- $\sum f_{p, q}$ is **absolutely convergent** if $\sum \|f_{p, q}\|$ is **double convergent**.
- Suppose $\sum f_{p, q}$ is absolutely convergent. And $a_p = \sum_{q=1}^\infty f_{p, q}$. Then $\sum a_p$ is absolutely convergent.
  - $\sum_p \norm{a_p} = \sum_p \norm{\sum_{q=1}^\infty f_{p, q}} \le \sum_{p} \sum_{q} \norm{f_{p, q}} = \sum_{p, q} \norm{f_{p, q}} < \infty$.

(**Rearranging double series**)

Suppose $V$ is a normed space. Consider double sequence $(f_{p,q})_{p, q \in \N^+} \subseteq V$.

- Suppose $g: \N^+ \to \N^+ \times \N^+$ is **bijective**. And $G_n = f_{g(n)}$.
- Then $(G_n)$ is a **flattening** of $(f_{p, q})$.
- $\sum G_n$ is absolutely convergent iff $\sum f_{p, q}$ is absolutely convergent.
  - Since $\sum_{n = 1}^\infty \|G_n\| = \sum_{p, q = 1}^\infty \|f_{p, q}\|$.

Suppose $\sum f_{p, q}$ is absolutely convergent. And $\sum f_{p, q} = s$.

- $\sum G_n = s$.
- $\sum_{p=1}^{\infty} \sum_{q=1}^{\infty} f_{p, q}=\sum_{q=1}^{\infty} \sum_{p=1}^{\infty} f_{p, q}= \sum_{p, q}^\infty f_{p, q} = s$. (**Fubini**)
  - This immediately follows from the result for iterated limits.

(**Factorizable Double Series**)

Suppose $\p{a_n}, \p{b_n} \subseteq \C$. And $\sum a_n$ and $\sum b_n$ converges absolutely.

Consider the double sequence $f_{m, n} := a_m b_n$.

- $\sum a_m b_n$ is absolutely convergent.
  $$
  \sum_{m=1}^{\infty}\left|a_{m}\right| \sum_{n=1}^{\infty}\left|b_{n}\right|=\sum_{m=1}^{\infty}\left(\left|a_{m}\right| \sum_{n=1}^{\infty}\left|b_{n}\right|\right)=\sum_{m=1}^{\infty} \sum_{n=1}^{\infty}\left|a_{m}\right|\left|b_{n}\right| = \sum_{m, n}^\infty |a_m b_n|
  $$

- $\sum_{m, n} a_m b_n = \p{\sum_m a_m} \p{\sum_n b_n}$.

  - This immediately follows from the Fubini theorem for double series.

(**Uniform convergence and double sequences**)

Suppose $V$ is a normed space over $\bF$.

- Suppose $f: \Z^+ \times \Z^+ \to V$ is a double sequence.
- Suppose $\lim_{n\to\infty} f(m, n) \rightrightarrows^m_{\Z^+} g(m)$.
- Suppose $\lim_{m \to \infty} g(m) = A$.

Then $\lim_{m, n \to \infty} f(m, n)$ exists and
$$
\lim_{m, n \to \infty} f(m, n) = \lim_{m \to \infty} g(m) = \lim_{m \to \infty} \lim_{n \to\infty} f(m, n)
$$

- Consider any $\epsilon > 0$.
- There exists $N$ where $d(f(m, n), g(m)) < \epsilon$ for all $n > N$.
- There exists $M$ where $d(g(m), A) < \epsilon$ for all $m > M$.

#### Cauchy Product and Multiplication of Series

(**Convolution, Cauchy Product**)

Suppose $V$ is an **algebra** over $\R, \C$.

Suppose $\p{a_n}_{n=0}^\infty, \p{b_n}_{n=0}^\infty \subseteq V$. Define the **convolution** of $\p{a_n}$ and $\p{b_n}$ as
$$
c_n = a_n * b_n = \sum_{k = 0}^n a_k b_{n-k}
$$
$\sum c_n$ is the **Cauchy product** of series $\sum a_n$ and $\sum b_n$.

(**Lemma 1: limit of average**)

Suppose $V$ is a normed space.

Suppose $\p{a_n} \subseteq V$ and $a_n \to a$. Then $(a_1 + \cdots + a_n) / n \to a$.

- Without loss of generality, take $a = 0$.

- There exists $N_0$ where for $n > N_0$, $\n{a_n} < \epsilon / 2$.

- There exists $N_1 > N_0$ where for $n > N_1$, $\n{a_1 + \cdots + a_N}/n < \epsilon / 2$.

- Notice that for $n > N_1$,
  $$
  \norm{\frac{a_1 + \cdots + a_n}{n}} \le \frac{\norm{a_1 + \cdots + a_N}}{n} + \frac{\epsilon (n - N)}{2n} < \epsilon
  $$

(**Lemma 2**)

Suppose $V$ is a normed algebra over $\bF$.

Suppose $\p{a_n}, \p{b_n} \subseteq V$ and $a_n \to a, b_n \to b$. Then
$$
\lim_{n \to \infty} \frac{a_1 b_n + \cdots + a_n b_1}{n} = ab
$$

- Without loss of generality, take $b = 0$.

- $a_n$ is bounded by $M > 0$.

- Notice that
  $$
  \norm{\frac{a_1 b_n + \cdots + a_n b_1}{n}} \le M \p{\frac{\norm{b_1} + \cdots + \norm{b_n}}{n}} \to 0
  $$

(**Cauchy product convergence theorem**)

Suppose $V$ is a **Banach algebra** (**complete** normed algebra) over $\bF$.

Suppose $\sum a_n = A$, $\sum b_n = B$ and $\sum c_n = \sum (a* b)_n = C$. Then $C = A B$.

- Let $A_n = \sum_{n=1}^k a_k$, $B_n$ and $C_n$ similarly defined.

- Just notice that
  $$
  \frac{1}{N} \sum_{n=1}^N C_n = \frac{1}{N} \sum_{n=1}^N A_n B_{N-n} = AB \implies C_n \to AB
  $$



(**Mertens' convergence theorem**)

Suppose $V$ is a **Banach algebra** over $\bF$.

Suppose $\sum a_n$ converge absolutely and $\sum b_n$ converges. Then $\sum c_n$ also converges. And $\sum c_n = (\sum a_n) (\sum b_n)$.

- Let $A = \sum a_n$ and $B = \sum b_n$, and $\alpha = \sum \n{a_n}$.

- Let $A_n = \sum_{k=0}^n a_k$, and $B_n = \sum_{k=0}^n b_n$, and $C_n = \sum_{k=0}^n c_k$.

- Let $\beta_n =  B_n - B$. Clearly $\beta_n \to 0$.

- $C_n = a_0B_n + \ldots + a_n B_0 = a_0(B + \beta_n) + \ldots + a_n (B + \beta_0) = A_n B + (a_0\beta_n + \ldots + a_n \beta_0)$.

- Let $\gamma_n = a_0 \beta_n + \ldots + a_n \beta_0$. Then $C_n = A_n B + \gamma_n$.

- We only need to show that $\gamma_n \to 0$.

  - Let $\epsilon > 0$ be given. There exists $N$ s.t. $\forall n > N: \abs{\beta_n} \le \epsilon$.

  - Notice the following:
    $$
    \begin{aligned}
    \abs{\gamma_n} &\le \abs{\beta_0 a_n + \ldots + \beta_N a_{n - N}} + \abs{\beta_{N+1}a_{n - N - 1} + \ldots + \beta_n a_0}\\
    & \le \abs{\beta_0 a_n + \ldots + \beta_N a_{n - N}} + \epsilon \cdot \alpha
    \end{aligned}
    $$

  - Now take limit $n \to \infty$, $\abs{\gamma_n} \le \epsilon \cdot \alpha$.


If $\sum a_n$ and $\sum b_n$ are both absolutely convergent, $\sum c_n$ is absolutely convergent.

#### Infinite Product

Definition 8.49. Given a sequence $\left\{u_{n}\right\}$ of real or complex numbers, let
$$
p_{n}=u_{1} u_{2} \cdots u_{n}=\prod_{k=1}^{n} u_{k}
$$
The ordered-pair of sequences $\left(\left\{u_{n}\right\},\left\{p_{n}\right\}\right)$ is called an **infinite product** (or simply, a product). The number $p_{n}$ is called the $n$th **partial product** and $u_{n}$ is called the $n$th **factor** of the product.

- Infinitely many factors of $u_n$ are zero, the product **diverges to zero**.
- Finitely many factors of $u_n$ are zero, $u_{n>N}$​ are nonzero
  - Convergence of $\prod u_k$ is determined by $\prod u_{k+N}$.
- No factors of $u_n$​ are zero
  - if $p_n \to p \neq 0$, the product **converges** to $p$.
  - if $p_n \to p = 0$​, the product **diverges to zero**.
  - If $p_n$​​ does not converge, the product **diverges**.

Properties of this definition:

- The convergence is not affected by **inserting or removing finite number of factors**.
- Convergent products has finite zero factors.

(**Cauchy condition for products**) The infinite product $\prod u_{n}$ converges if, and only if
$$
\forall \epsilon > 0, \exists N \in \Z, \forall n > N, \forall k \in \N: 
\left|u_{n} u_{n+1} \cdots u_{n+k}-1\right|<\epsilon
$$
(**Absolutely Converge Product**)

- Assume that each $a_{n}>0$. Then the product $\prod\left(1+a_{n}\right)$ converges if, and only if, the series $\sum a_{n}$ converges.

- The product $\prod \left(1+a_{n}\right)$​ is said to **converge absolutely** if $\prod \left(1+\left|a_{n}\right|\right)$​ converges.

- $\prod (1 + a_n)$ converge absolutely then $\prod(1 + a_n)$ converges.

  Assume that each $a_{n} \geq 0$. Then the product $\prod\left(1-a_{n}\right)$ converges if, and only if, the series $\sum a_{n}$ converges.

(**Euler's Zeta Function**) Let $p_{k}$ denote the $k$ th prime number. Then if $s>1$ we have
$$
\zeta(s)=\sum_{n=1}^{\infty} \frac{1}{n^{s}}=\prod_{k=1}^{\infty} \frac{1}{1-p_{k}^{-s}}
$$
The product converges absolutely.

