#### 01 Laws

##### Limit of events

 Suppose $(\Omega, \F, P)$ is a probability space and $(A_n)_{n = 1}^\infty \in \F$​.


$A_* \subseteq A^*$. And $P(A_*) \le \liminf_n P(A_n) \le \limsup_n P(A_n) \le P(A^*)$.

- Let $B_n = \cap_{k = n}^\infty A_k$ and $C_n = \cup_{k = n}^\infty A_k$. Then $B_n \uparrow \liminf_n A_n$ and $C_n \downarrow \limsup_n A_n$.
- $P(A_n) \ge P(B_n)$, so $\liminf_n P(A_n) \ge P(\liminf_n A_n)$.
- $P(A_n) \le P(C_n)$, so $\limsup_n P(A_n) \le P(\limsup_n A_n)$.

Suppose $A_n \to A$, then $A \in \F$ and $P(A_n) \to P(A)$.

##### Cantelli

Suppose $(X, \A, \mu)$ is a measure space. And $(A_n)_{n = 1}^\infty \in \A$. And $\sum_n \mu(A_n) < \infty$. Then $\mu(A^*) = 0$.

- Recall that $A^* = \limsup_n A_n = \cap_{n = 1}^\infty \cup_{k = n}^\infty A_k$.
- Hence $\mu(\limsup_n A_n) \le \mu(\cup_{k = n}^\infty A_k) \le \sum_{k = n}^\infty \mu (A_k) \to 0$.

##### Cantelli II

Suppose $(\Omega, \F, P)$ is a probability space. And $(A_n)_{n = 1}^\infty \in \F$ .

Suppose $\{A_n\}_{n = 1}^\infty$ is independent. Then $\sum_{n = 1}^\infty P(A_n) = \infty$ implies $P(A^*) = 1$.

- Notice that
  $$
  \begin{aligned}
  P(A^*)^c & = P(\cup_{n = 1}^\infty \cap_{k = n}^\infty A_k^c) = \lim_{n \to \infty} P(\cap_{k = n}^\infty A_k^c) = \lim_{n\to \infty}\prod_{k = n}^\infty (1 - P(A_k^c)) =\\ & = \lim_{n \to \infty} \exp \sum_{k = n}^\infty \log (1 - P(A_k^c)) \le \exp \left(-\sum_{k = n}^\infty P(A_k)\right)
  \end{aligned}
  $$

- So $\sum_{n = 1}^\infty P(A_n) = \infty$ implies $P(A^*)^c = 0$, so $P(A^*) = 1$.

##### Cantelli III ==TODO==

(Cantelli II) can be enhanced to pairwise independent $(A_n)$.

##### Tail $\sigma$-algebra

Consider probability space $(\Omega, \F, P)$. Define the **tail (sigma)-algebra** on **sequences**:

- For $\mathscr A = (\A_n)_{n = 1}^\infty$ where $\A_n$ are $\sigma$-algebras in $\F$. $\A_{\infty} = \T(\mathscr A) = \cap_{n = 1}^\infty \sigma(\cup_{m = n}^\infty \A_m)$.
- For $\A = (A_n)_{n = 1}^\infty$ where $A_n \in \F$. $\T(\A) = \cap_{n = 1}^\infty \sigma\{A_m\}_{m = n}^\infty$.
- For $\X = (X_n)_{n = 1}^\infty \in \L(\Omega \to \Omega_n, \F / \F_n)$. $\T(\X) = \cap_{n = 1}^\infty \sigma\{X_{m}\}_{m = n}^\infty$.

Events in the tail $\sigma$-algebra are called **tail events**. Functions measurable with respect to the tail $\sigma$-algebra are called **tail functions**.

- $\T (\mathscr A) \subseteq\sigma(\mathscr A)$, $\T(\A) \subseteq \sigma(\A)$, $\T(\X) \subseteq \sigma(\X)$.
- The indexing order of $\mathscr A, \A, \X$ does not matter.
- A tail event / tail function is not changed by changing finitely many elements in $\mathscr A, \A, \X$.

Examples of tail events: 

- Suppose $\A = (A_n)_{n = 1}^\infty \in \F$. Then $A^*, A_* \in A_{\infty}$.

Examples of tail functions:

- Suppose $\X = (X_n)_{n = 1}^\infty \in \L(\Omega\to \bar \R, \F)$. $X^* = \limsup_n X_n, X_* = \liminf_n X_n \in \T(\X)$.
- Suppose $\X = (X_n)_{n = 1}^\infty \in \L(\Omega \to \R, \F)$. Let $Y_n = \sum_{i = 1}^n X_i / n$. Then $Y^*, Y_* \in \T(\X)$.
  - $Y_* = \liminf_n Y_n$ and $Y^* = \limsup_n Y_n$ are called **Cesàro limits** of sequence $(X_n)_{n = 1}^\infty$.

##### Komologov's 0-1 law

 Consider probability space $(\Omega, \F, P)$.

For $\mathscr A = (\A_n)_{n = 1}^\infty$ where $\A_n$ are **independent** $\sigma$-algebras in $\F$. Suppose $A \in \A_{\infty}$. $P(A) \in \{0, 1\}$.

- Let $\S_n = \{\cap_{k = 1}^n A_k: A_k \in \A_k\}$. And $\S = \cup_n \S_n$, $\S$ is a **semi-ring**.
- $\S \subseteq \sigma(\cup_{n = 1}^\infty \A_n)$ and $\cup_{n = 1}^\infty \A_n \subseteq \S$. So $\sigma(\S) = \sigma(\cup_{n = 1}^\infty \A_n) \supseteq \T(\mathscr A)$.
- $\forall \epsilon > 0, \exists B \in \bar \S: P(B \Delta A) \le \epsilon$.
- There exists $N \in \N$ where $B \in \sigma(\cup_{n = 1}^N \A_n)$ and $A \in \sigma(\cup_{n = N+1}^\infty \A_n)$. So $A \perp B$.
- $\epsilon > P(B - A) = P(B \cap A^c) = P(B)(1 - P(A)) \ge P(A)(1 - P(A) - \epsilon)$.
- Take $\epsilon \downarrow 0$ yields $0 = P(A) (1 - P(A))$.

#### Law of Large Numbers

##### Law of large numbers

Suppose $(X_n)_{n = 1}^\infty \in \L^1(\Omega \to \R, \F, P)$. Define $S_n = \sum_{i = 1}^n (X_i - E[X_i])$.

- $(X_n)$ fulfils the **weak law of large numbers** if $S_n / n \to 0$ in probability.
- $(X_n)$ fulfils the **strong law of large numbers** if $S_n / n \to 0$ essentially pointwise.

##### WLLN

Suppose $(X_n)_{n = 1}^\infty \in \L^2(\Omega \to \R, \F, P)$. And $V = \sup_n \var (X_n) < \infty$.

Define $S_n = \sum_{i = 1}^n (X_i - E[X_i])$. Then $P(|S_n / n| \ge \epsilon) \to 0$. So $(X_n)$ fulfils the WLLN.

- $\var(S_n / n) = n^{-2} \sum_{i = 1}^n \var (X_i) \le V/n$.
- $P(|S_n / n| \ge \epsilon) \le \epsilon^{-2}\var(S_n / n)$ by (Markov).

##### Weierstraß approximation

Suppose $f \in C[0, 1]$. There exists $f_n(x) \in \R[x]$ with $\deg f_n \le n$ such that $\|f_n - f\|_\infty \to 0$. By the way $\|\cdot \|_\infty$ is a true norm on $C[0, 1]$.

- Define $f_{n}(x):=\sum_{k=0}^{n} f(k / n)C_n^k x^{k}(1-x)^{n-k}$ for $x \in [0, 1]$.
- Since $f \in C[0, 1]$, $\forall \delta > 0, \exists \epsilon > 0, \forall x, y \in [0, 1]: |x - y| < \delta \to |f(x) - f(y) < \epsilon|$.
- Fix $p \in [0, 1]$, let $(X_n)_{n = 1}^\infty \sim b_{1, p}$ and $S_n:= X_1 + \cdots + X_n \sim b_{n, p}$.
- ${E}[f(S_{n} / n)]=\sum_{k=0}^{n} f(k / n) {P}[S_{n}=k]=f_{n}(p)$.
- By UC, $|f(S_{n} / n)-f(p)| \le \epsilon+2\|f\|_{\infty} 1_{\{|(S_{n} / n)-p| \ge \delta\}}$.
- $|f_n(p) - f(p)| \le E|f(S_n / n) - f(p)| \le \epsilon + 2^{-1} \delta^{-2}n^{-1}\|f\|_\infty$ by (WLLN) on $(X_n)$.

##### Toeplitz lemma

Consider double sequence $A_{nj}$ where $n, j \ge 1$ such that $A_{nj} \to 0$ as $n \to \infty$. And $\sum_{j = 1}^\infty \abs{A_{nj}} \le c$ for all $n$.

When $(x_j)_{j = 1}^\infty \in \R$ is bounded, $y_n = \sum_{j = 1}^\infty a_{nj} x_j$ is well defined. Further:

- $y_n = \sum_{j = 1}^\infty a_{nj} x_j \to 0$ if $x_n \to 0$.
  - $\abs{y_n} \le \sum_{j = 1}^N \abs{a_{nj}}\abs{x_j} + \sum_{j = N + 1}^\infty \abs{a_{nj}}\abs{x_j}$.
  - Choose fixed $N \ge 0$ where $|x_j| \le \epsilon / c$ for $j \ge N$. So $\sum_{j = N + 1}^\infty \abs{a_{nj}}\abs{x_j} \le \epsilon$.
  - Let $n \to \infty$, $\sum_{j = 1}^N \abs{a_{nj}}\abs{x_j} \to 0$ as well.
- $y_n = \sum_{j = 1}^\infty a_{nj} x_j \to x$ if $\sum_{j = 1}^\infty a_{nj} \to 1$ and $x_n \to x$ as $n \to \infty$.
  - $(y_n - x\sum_{j = 1}^\infty a_{nj}) = \sum_{j = 1}^\infty a_{n j}(x_j - x) \to 0$ as $n \to \infty$.
  - Also $(y_n - x \sum_{j = 1}^\infty a_{nj}) \to y_n - x$ as $n \to \infty$. So $y_n \to x$ as $n \to \infty$.

Suppose $(a_n)_{n = 1}^\infty \in [0, \infty)$ and $b_n = \sum_{j = 1}^n a_j$. Further $b_n > 0$ and $b_n \to \infty$. Suppose $(x_n)_{n = 1}^\infty \in \R$ and $x_n \to x$. Then $(\sum_{j = 1}^n a_j x_j)/b_n \to x$ as $n \to \infty$.

- Define $A_{nj} = 1_{j \le n} a_j/b_n$. Then $A_{nj} = a_j / b_n \to 0$ as $n \to \infty$. And $\sum_{j = 1}^\infty A_{nj} = 1$.
- The result immediately follows.

##### Kronecker lemma

Suppose $(b_n)_{n = 1}^\infty \in (0, \infty)$ and $b_n \to \infty$. Suppose $(x_n)_{n = 1}^\infty \in \R$ and $\sum_{n = 1}^\infty x_n = x \in \R$. Then $(\sum_{j = 1}^n b_j x_j )  / b_n \to 0$ as $n \to \infty$.

- Define $s_n = \sum_{j = 1}^n x_j$ and $s_0 = 0$. Define $b_0 = 0$.
- $\sum_{j = 1}^n b_j x_j = \sum_{j = 1}^n b_j (s_j - s_{j - 1}) = b_n s_n - \sum_{j = 1}^n s_{j - 1}(b_j - b_{j - 1})$.
- $(\sum_{j = 1}^n b_j x_j)/b_n = s_n - \sum_{j = 1}^n s_{j - 1}(a_j)/b_n$. Where $a_j = b_j - b_{j - 1} > 0$.
- Now apply (Toeplitz lemma), $\sum_{j = 1}^n a_j s_{j - 1} / b_n \to x$. Also $s_n \to x$.

##### Kolmogorov' inequality

Recall that by (Markov): Suppose $Y \in \L^1(\Omega \to \R, \F, P)$ then $P(\abs{Y - EY} \ge \epsilon) \le E[(Y - EY)^2]/\epsilon ^2 = \operatorname{Var}(Y)/\epsilon^2$.

Suppose $(X_i)_{i = 1}^n \in \L^1(\Omega \to \R, \F, P)$ are independent. Define $S_j = \sum_{i = 1}^j X_i$. Then
$$
P\left( \max_{1 \le j \le n} \abs{S_j - ES_j} \ge \epsilon\right) \le \frac{\operatorname{Var}S_n}{\epsilon ^2}
$$

- Without loss of generality, assume $E(X_j) = 0$ so $E(S_j) = 0$.
- Define $A_k = \{\forall j < k: |S_j| < \epsilon, |S_k| \ge \epsilon\}$. Define $A = \{\max_{1 \le j \le n}|S_j| \ge \epsilon\}$. So $A = +_k A_k$.
- Express the variance as integral:
  $$
  \var S_{n}=\int_{\Omega} S_{n}^{2} d P \geq \int_{A} S_{n}^{2} d P=\sum_{k=1}^{n} \int_{A_{k}} S_{n}^{2} d P
  $$
- Notice that $S_n = S_k + Y_k$ where $Y_k = X_{k + 1} + \cdots + X_n$. So:
  $$
  \int_{A_{k}} S_{n}^{2} d P=\int_{A_{k}} S_{k}^{2} d P+2 \int_{A_{k}} S_{k} Y_{k} d P+\int_{A_{k}} Y_{k}^{2} d P \ge \int_{A_k} S^2_k dP \ge \epsilon^2 P(A_k)
  $$
- So $\var S_n \ge \epsilon^2 P(A)$.

##### Independent sum

Suppose $(\Omega, \F, P)$ is a probability space. Suppose $(X_n)_{n = 1}^\infty \in \L^1(\Omega \to \R, P)$ are **independent**, and $\sum_{n = 1}^\infty \var X_n < \infty$. Then $\sum_{n = 1}^\infty (X_n - E X_n)$ converges $P$.a.e. in $\L(\Omega \to \R, P)$.

- Without loss of generality assume $EX_n = 0$.
- Define $S_n = \sum_{i = 1}^n X_i$. $S_n$ converges $P$.a.e. if $S_n(\omega)$ is $P$.a.e. **Cauchy**.
- We only need to show $P\left( \cup_{j, k \ge n} \{\abs{S_j - S_k} \ge \epsilon\}\right) \to 0$ as $n \to \infty$.
- Equivalently $P(\cup_{k = 1}^\infty \{\abs{S_{m + k} - S_m} \ge \epsilon\}) \to 0$ as $m \to \infty$. Now observe:
  $$
  \begin{aligned}
  P\left[\bigcup_{k=1}^{\infty}\left\{\left|S_{m+k}-S_{m}\right| \geq \varepsilon\right\}\right] & = \lim _{n \rightarrow \infty} P\left[\bigcup_{k=1}^{n}\left\{\left|S_{m+k}-S_{m}\right| \geq \varepsilon\right\}\right] \\
  & = \lim _{n \rightarrow \infty} P\left\{\max _{1 \leq k \leq n}\left|S_{m+k}-S_{m}\right| \geq \varepsilon\right\} \\
  & = \lim _{n \rightarrow \infty} \frac{\var (S_{m + n} - S_m)}{\epsilon^2} \to 0
  \end{aligned}
  $$

##### Kolmogorov SLLN

Suppose $(\Omega, \F, P)$ is a probability space.

Suppose $(X_n)_{n = 1}^\infty \in \L^1(\Omega \to \R, P)$ and $\var X_n < \infty$. Suppose $(b_n)_{n = 1}^\infty \in (0, \infty)$ and $b_n \to \infty$.

If $\sum_{n = 1}^\infty \var X_n / b_n^2 < \infty$. Then $(S_n - E(S_n)) / b_n \to 0$ essentially pointwise.

- Consider $Y_n = (X_n - E(X_n)) / b_n$. By (**Independent sum**), $Y_n \to 0$ $P$.a.e.
- Fix $\omega \in \Omega$. $(\sum_{k = 1}^n b_k Y_k(\omega)) / b_n \to 0$ $P$.a.e. by (**Kronecker lemma**).

Specifically, let $(X_n)$ be independent with $E[X_n] = m$ and $\var X_n = \sigma^2$. And take $b_n = n$.

- Then $(S_n - nm) / n \to 0$ essentially pointwise.
- So $(S_n / n) \to m$ essentially pointwise.

Specifically, let $(X_n)$ be independent with $E[(X_n - EX_n)^4] \le B < \infty$. And take $b_n = n$.

- By (**Holder**) $\var X_n = E[(X_n - EX_n)^2 \cdot 1] \le B^{1/2}$.
- Then $(S_n - E(S_n)) / n \to 0$ essentially pointwise.

##### Positive expectation inequality

 Suppose $(\Omega, \F, P)$ is a probability space. And $Y \in \L(\Omega \to [0, \infty),P)$. Then $\sum_{n=1}^{\infty} P\{Y \geq n\} \leq E(Y) \leq 1+\sum_{n=1}^{\infty} P\{Y \geq n\}$. Since
$$
\begin{aligned}
\sum_{n = 1}^\infty P(Y \ge n) &=\sum_{n=1}^{\infty} \sum_{k=n}^{\infty} P(k \leq Y<k+1)=\sum_{k=1}^{\infty} \sum_{n=1}^{k} P(k \leq Y<k+1) \\
&=\sum_{k=1}^{\infty} k P(k \leq Y<k+1)=\sum_{k=0}^{\infty} \int_{\{k \leq Y<k+1\}} k d P \\
&\leq \sum_{k=0}^{\infty} \int_{\{k \leq Y<k+1\}} Y d P=E(Y) \leq \sum_{k=0}^{\infty}(k+1) P(k \leq Y<k+1) \\
&=\sum_{n=1}^{\infty} P(Y \geq n)+\sum_{k=0}^{\infty} P(k \leq Y<k+1)=\sum_{n=1}^{\infty} P(Y \geq n)+1
\end{aligned}
$$

##### SLLN ==TODO==

Suppose $(\Omega, \F, P)$ is a probability space.

Suppose $X, (X_n)_{n = 1}^\infty \in \L^1(\Omega \to \R, \F, P)$ are i.i.d. With $E[X] = m$.

Define $S_n = \sum_{i = 1}^n X_i$. Then $S_n / n \to m$ essentially pointwise.

- If $E[X]$ is either $+\infty$ or $-\infty$, the result still holds.
