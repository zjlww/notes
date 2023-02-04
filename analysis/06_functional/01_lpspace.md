#### Abstract $\L^p$ Spaces

(**Dense subspaces of $L^p$**)

Consider $p \in [1, \infty)$, and space $\L^p(X \to \bF, \F, \mu)$.

- Bounded $\L^p$ functions are dense in $\L^p$.
  - This follows from monotone convergence theorem.
- Simple $\L^p$ functions are dense in $\L^p$.
  - Denoted by $S^p(X \to \bF, \mu)$.

Suppose $\mu$ is $\sigma$-finite. There exists increasing $\p{E_n} \subseteq \F$ where $X = \cup_n E_n$. Therefore:

- Bounded $\L^p$ functions with finite measure support is dense in bounded $\L^p$ functions.
  - Restrict the functions by $E_n$.
- Simple $\L^p$ functions with finite measure support is dense in the above space.
  - This follows from staircase approximation.
  - Denoted by $S^p_f(X \to \bF, \mu)$.

(**Testing $L^p$ norm with $L^q$ testing functions**)

Suppose $(X, \F, \mu)$ is a measure space. Suppose $p \in [1, \infty]$ and $q = p'$.

And $f \in L^p(X \to \bF, \mu)$ with $\n{f}_p \in (0, \infty)$.

Notice that by Holder's inequality and triangle inequality:
$$
|\pd{f}{g}| \le \mu |fg| = \n{fg}_1 \le \n{f}_p \n{g}_q \implies \sup_{g \in L^q, \n{g}_q = 1} \abs{\pd{f}{g}} \le \n{f}_p
$$
Suppose $p \in [1, \infty)$, the upper bound is achieved:
$$
\n{f}_p = \max_{g \in L^q, \n{g}_q = 1} \abs{\pd fg}
$$

- Suppose $p = 1$ and $q = \infty$.

  - Let $g(x) := f(x) / \abs{f(x)}$ when $f(x) \neq 0$ and $g(x) = 0$ otherwise.

- Suppose $p, q > 1$.

  - Let $g(x)$ be the following:
    $$
    g(x) = f(x)|f(x)|^{p - 2} / \n{f}_p^{p-1}
    $$

  - Compute the norm:
    $$
    \n{g}_q^q = \int \abs{g}^q \dd \mu = \int\frac{\abs{f}^{p}}{\n{f}_p^p} \dd \mu = 1
    $$

  - Compute the **inner product** $\pd {f}{g}$:
    $$
    \int f\overline g \dd \mu = \int |f|^{p} / \n{f}_p^{p-1} \dd \mu = \n{f}_p
    $$

Suppose $p = \infty$ and $q = 1$, the upper bound may not be achieved, but we still have: (Given $\sigma$-finiteness)
$$
\n{f}_\infty = \sup_{g \in L^1, \n{g}_1 = 1} \pd fg
$$

- Let $M = \n{f}_{\infty} < \infty$, and $\epsilon > 0$.
- The set $A = \c{|f| > M - \epsilon}$ is not null. Suppose $B \subseteq A$ and $\mu(B) = \delta > 0$.
  - **Caveat: this requires that the set $B$ exist.**
- Define $g(x):= \frac{f(x)}{|f(x)|}\frac{1_{B}(x)}{\delta}$. Then $\n{g}_1 = \mu|g| = 1$.
- And $\pd fg \ge M - \epsilon$.

(**Testing $L^p$ norm with $L^q$ simple testing functions**)

Suppose $(X, \F, \mu)$ is a measure space. Suppose $p \in [1, \infty]$ and $q = p'$.

Suppose $g \in \L(X \to \bF)$. Then we can bound $L^p$ norm of $g$ with simple functions in $L^q$.
$$
\sup_{\phi \in S^q(X \to \bF, \mu), \n{\phi}_q = 1} \abs{\pd g \phi} \le M < \infty \implies g \in L^p(\mu)\land \n{g}_p \le M
$$

- Suppose $p, q \in (1, \infty)$.

  - Let $\psi_k$ be a sequence of simple functions where $\psi_k \uparrow |g|^{1/(q-1)}$.

  - Define $\phi_k = \psi_k \cdot g/|g|$. Now
    $$
    \begin{aligned}
    \pd{g}{\phi_k} &= \pd{g}{\psi_k \cdot g / |g|} = \int \psi_k \cdot |g| \dd \mu \to \mu|g|^{\frac{1}{q-1} + 1} = \mu|g|^p = \n{g}_p^p\\
    \pd{g}{\phi_k} &\le M \n{\phi_k}_q = M \p{\int \abs{\phi_k}^q \dd \mu}^{1/q} = M \p{\int \abs{\psi_k\cdot\frac{g}{|g|}}^p \dd \mu}^{1/q} = M(\mu |g|^p)^{1/q} = M \n{g}_p^{p/q}
    \end{aligned}
    $$

  - Therefore $\n{g}_{p}^p \le M \n{g}_{p}^{p/q}$ so $\n{g}_p \le M$.

- Suppose $q = \infty$ and $p = 1$.

  - Let $\phi = g / |g|$. Then $\n{\phi}_q = 1$. $\pd{g}{\phi} = \n{g}_p \le M$.

- Suppose $q = 1$, and $p = \infty$. (Requires $\sigma$-finiteness)

  - $g \in L^\infty$.
    - Suppose $g \notin L^\infty$, define $A_k:= \c{|g| \ge k}$. $\mu(A_k) > 0$.
    - Define $\phi_k := 1_{A_k}/\mu(A_k)$. Then $\n{\phi_k}_1 = 1$.
    - But $\pd{g}{\phi_k} \ge k$, this is a contradiction.
  - $\n{g}_{\infty} \le M$.
    - Suppose $\n{g}_\infty = \widetilde M > M$. Let $A:= \c{|g| > (\widetilde M + M) / 2}$. $\mu(A) > 0$.
    - Take $B \subseteq A$ where $\mu(B) \in (0, \infty)$.
      - **Caveat: This requires the set $B$ to exist.**
      - $\sigma$-finiteness of $\mu$ is a sufficient condition.
    - Define $\phi:= 1_B/\mu(B)$. Then $\n{\phi} _1= 1$.
    - But $\pd{g}{\phi} \ge M$, this is a contradiction.

(**Inner product functionals on $L^p$**)

Suppose $p \in [1, \infty]$ and $q = p'$ is the dual power.

Suppose $(X, \F, \mu)$ is a **measure space**. And $\bF$ is either $\R$ or $\C$.

Recall that $L^p(X \to \bF, \mu)$ is a **Banach space**.

Suppose $g \in L^q$, define the map $\ell_{g}: L^p \to \bF$ as following:
$$
\ell_g(f): = \pd{f}{g} = \int_X f(x) \overline{g(x)} \dd \mu(x)
$$
Immediately $\ell_g \in (L^p)'$. And $\n{\ell_g} = \n{g}_{q}$ by norm testing theorems.

(**Dual of $L^p$ is $L^q$**)

Suppose $(X, \F ,\mu)$ is a **$\sigma$-finite measure space**. Suppose $p \in [1, \infty)$, and $q = p'$.

Recall the space $L^p(X \to \bF, \mu)$ is Banach space.

Suppose $\lambda \in (L^p)' = \mathcal B(L^p, \bF)$. There exists a unique $g \in L^q$ where $\lambda = \ell_g$.

- The uniqueness is apparent.
- Suppose $\mu$ is finite.
  - Define $\nu(E):= \lambda(1_E)$ for $E \in \F$. It is a complex measure.
    - Since $\nu$ is a proto-measure, and countably additive.
  - $\nu \ll \mu$. By Radon-Nikodym, there exists $g \in \L^1(X \to \bF)$ where $\dd \nu = g\dd \mu$.
  - Then $\lambda(f) = \pd{f}{g}$ for all simple functions $f \in S^p(X \to \bF, \mu)$.
    - For indicators, $\lambda(1_E) = \pd{1_E}{g}$ by previous argument.
    - For simple functions, by linearity of $\lambda$ and integral.
  - By norm testing with simple functions, $\n{g}_q \le \n{\lambda} < \infty$. So $g \in L^q(\mu)$.
  - Therefore $\pd{\cdot}{g}$ is a continuous linear map.
  - Two continuous linear map agree on a dense subspace are equal.
- Suppose $\mu$ is $\sigma$-finite.
  - Since $\mu$ is $\sigma$-finite, there exists a sequence of increasing $\p{E_n} \subseteq \F$ where $\cup E_n = X$. And $\mu(E_n) < \infty$.
  - Now generate $g_n$ according to the finite case. They must agree due to uniqueness.

#### $\L^p(\R^d)$ Spaces

(**Sobolev space $W^{k,p}(\R^d)$**)

Suppose $f \in L^p(\R^d \to \bF, \lambda)$. Where $\lambda$ is the Lebesgue measure on $\R^d$.

Suppose for all $\alpha \in \N^d$ where $|\alpha| \le k$, there exists $g_\alpha \in L^p$ such that for all testing functions $\phi \in C_{c}^\infty(\R^d)$.
$$
\int_{\R^d} g_\alpha \phi = (-1)^{|\alpha|} \int_{\R^d} f D_{}^\alpha \phi
$$

- We say that $f$ has **weak derivatives** in $L^p$ up to order $k$.
- We call $g_\alpha$ the **weak derivative**, denoted as $g_\alpha = \part^\alpha f$.
- The subspace of $L^p$ of such functions is the **Sobolev space** $L_k^p(\R^d \to \bF, \lambda)$.
  - Also denoted as $W^{k, p}(\R^d)$ in some books.

(**Dense subspaces of $\L^p(\R^d)$**)

Suppose $(\R^d, \B(\R^d), \mu)$ is a LS measure space. (Clearly $\sigma$-finite.)

Suppose $f \in \L^p(\R^d \to \bF, \mu)$. Where $p \in [1, \infty)$.

- $S_f^p(\mu)$ is dense in $\L^p(\mu)$. Due to $\sigma$-finiteness.
- The set of simple functions with compact support is dense in $\L^p(\mu)$.
  - Denoted by $S_c^p(\mu)$.
- The set of step functions with compact support is dense in $\L^p(\mu)$.
  - Consider any $\epsilon > 0$. And function $f \in \L^p(\mu)$.
  - We now show that there is a $s \in \square(\R^d \to \R)$ such that $\|f - s\|_p \le \epsilon$.
    - There exists $g \in S_c^p(\R^d \to \R, \mu)$ such that $\|f - g\|_p \le \epsilon$.
    - Suppose $g = \sum_ic_i 1_{A_i}$ with $A_i \in \B(\R^d)$ and $\mu(A_i) < \infty$.
    - Approximate $A_i$ by $C_i = +_{k = 1}^{n_i} B_{ij}$ for $B_{ij} \in \S_d^+$ where $\|c_i1_{A_i} - c_i1_{C_i}\|_p < \epsilon / 2^i$.
      - This follows from an approximation theorem of outer measures.
    - Define $s = \sum_i c_i 1_{C_i}$. Then $\|f - s\|_p \le \|f - g\|_p + \|g - s\|_p \le 2 \epsilon$.
    
  - Denoted the space by $\square_c(\R^d \to \bF, \mu)$.

Suppose $(\R^d, \B(\R^d), m)$ is the Lebesgue space.

- The set of infinitely continuous functions with bounded supports are dense in $\L^p(\R^d)$.
  - There exists $s \in \square_c(\R^d \to \bF)$ such that $\|f - s\|_p \le \epsilon$.
  - Create a small continuous slope on the edges of the boxes in $s$. ==TODO==

(**Luzin's Theorem**)

Suppose $g: \R^d \to \R$ is Borel measurable. For every $\epsilon > 0$ there exists a closed set $F \subset \R^d$ such that $|\R - F| \le \epsilon$ and $g \in C[F]$.

> TODO: Verify the following when you have time.

(**Step 1**) Consider the case where $g$ is **Borel measurable simple function**.

Suppose $g = \sum_{k=1}^n d_k 1_{D_k}$ where $D_k \in \mathcal B(\R^d)$ are disjoint, $d_k \in \R$.

Suppose $F_k$ is inner closed approximation of $D_k$ and $G_k$ is the outer open approximation. The open gap $G_k - F_k$ can be very small.

Merge all $F_k$ into $F$. Intersect all $G_k$ into $G$. The total gap $G - F$ can be very small.

$g$ is continuous on closed set $\R^d - (G - F)$, $(G - F)$ can be arbirartarily small.

(**Step 2**) Suppose $g$ is Borel measurable. Approximate $g$ with simple functions in $g_k \in S(X \to \R)$ by above definition. 

Suppose each $g_k$ is continuous on closed set $C_k$ where $\R^d - C_k$ can be very small.

Consider set $C = \bigcap_{k=1}^\infty C_k$, the rest $\R^d - C$ can be very small.

(**Step 3**) Combine Egorov's Theorem to derive continuity.

Consider unit boxes $(B_m)_{m=1}^\infty$ that covers $\R^d$. In each box, $g_k \to_{B_m} g$. Except for a set $E_m$ that can be very small. $g_k \rightrightarrows_{B_m - E_m} g$. So $g$ is continuous at all points in $(B_m - E_m)^\circ$.

Consider $D = (\R^d - C)\cup \bigcup_m E_m$ which can be very small. This set is Borel set. And $g \in C[\R^d - D]$.

There is a inner closed approximation of $\R^d - D$. This is what we need.

(**Tietze extension theorem**)

==TODO== Suppose $X$ is a normal space, and $f: A\subseteq X \to \R$, where $A$ is closed in $X$. There is a **continuous extension** of $f$ to $X$, that is, there exists a continuous map $F: X \to \R$, $F|_A = f$.

Moreover, $F$ may be chosen such that
$$
\sup \{|f(a)|: a \in A\}=\sup \{|F(x)|: x \in X\}
$$
$\R^d$ is a normal space.

(**Luzin's Theorem II**)

Suppose $g: E \subseteq \R^d \to \R$ is a $\R^d$ Borel measurable function.

For all $\epsilon > 0$, there exists a closed set $F \subseteq E$ and a continuous function $h: \R^d \to \R$ such that $m^*(E - F) < \epsilon$, and $h|_F = g|_F$.

