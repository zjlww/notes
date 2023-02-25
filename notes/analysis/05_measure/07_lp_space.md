#### $L^p$ Function Spaces

##### p-norm

Suppose $(X, \S, \mu)$ is a measure space.

$f \in \L(X \to \bF, \S)$. Where $\bF$ is either $\R$ or $\C$.

- For $0 < p < \infty$ define $\|f\|_{p} = (\mu |f|^p)^{1 / p}$.
- For $p = \infty$ define $\|f\|_\infty = \inf\{K \ge 0: \mu\{|f| \ge K\} = 0\}$.
  - $\|f\|_\infty$ is also called the **essential supremum** of $f$.

For $p \in (0, \infty]$, define $\L^p(\mu) = \L^p(X \to \bF, \mu) := \{f \in \L(X \to \bF, \mu): \|f\|_p < \infty\}$.

- $\bF \subset \L^p$ is bounded if $\sup_{f \in \bF}\|f\|_p < \infty$.

$\L^p(X \to \bF, \mu)$ is a vector space over $\bF$.

- $\L^p(X \to \bF, \mu)$ is closed under addition. For $f, g \in \L^p(X \to \bF, \mu)$.

  - For $p \in (0, \infty)$. $\|f+g\|_{p}^{p} \leq 2^{p}(\|f\|_{p}^{p}+\|g\|_{p}^{p})$.
    - $|f(x)+g(x)|^{p} \leq(|f(x)|+|g(x)|)^{p} \leq(2 \max \{|f(x)|,|g(x)|\})^{p}\leq 2^{p}(|f(x)|^{p}+|g(x)|^{p})$

  - For $p = \infty$. $\|f + g\|_\infty \le \|f\|_\infty + \|g\|_\infty$ is apparent.

  - For $p \in [1, \infty]$, (**Minkowski**) gives: $\|f+g\|_{p} \leq\|f\|_{p}+\|g\|_{p}$.

- $\L^p(X \to \bF, \mu)$ is closed under scalar multiplication.

  - For $p \in (0, \infty]$. $\forall \alpha \in \bF: \|\alpha f\|_p = |\alpha|\|f\|_p$.

Functions that agree $\mu$-almost everywhere can be treated as one:

- Let $\mathcal Z(\mu) := \{f \in \L^1(\mu):\|f\|_1 = 0\}$. $\mathcal Z(\mu)$ is a linear subspace of any $\L^p(\mu)$.
- Define $L^p(\mu) = \L^p(\mu) / \mathcal Z(\mu)$.
- Define $\|\cdot\|_p: L^p(\mu)\to [0, \infty)$ by $\|f + \mathcal Z\|_p = \|f\|_p$.

For $p \in [1, \infty]$, $\|\cdot \|_p$ is a **seminorm** on $\L^p(\mu)$ and a **norm** on $L^p(\mu)$. 

For $p \in [1, \infty]$. $L^p(X \to \bF, \mu)$ is a **normed vector space** over $\bF$.

##### Hölder’s inequality

Suppose $p \in (1, \infty)$, $p' \in(1, \infty)$ where $1/p + 1/p' = 1$ is the dual of $p$.

- Clearly $p' = p / (p - 1)$.

Suppose $p = 1$, $p' = \infty$, and vice versa.

Suppose $(X, \S, \mu)$ is a measure space. $p \in [1, \infty]$. $f, g \in \L(X \to \bF, \S)$. Then $\|fg\|_1 \le \|f\|_p \|g\|_{p'}$.

- For $p \in [1, \infty]$. Suppose $\|f\|_p$ or $\|g\|_{p'}$ is $0$ or $\infty$, the result is clearly true.
- For $p \in (1, \infty)$ and $\|f\|_p, \|g\|_{p'} \in (0, \infty)$.
  - (Young) $\forall a, b \ge 0: ab \le a^p / p + b^{p'} / p'$.
  - Let $\tilde f = f / \|f\|_p$ and $\tilde g = g / \|g\|_{p'}$.
  - Since $|\tilde f\tilde g| \le |\tilde f|^p/p + |\tilde g|^{p'}/p'$. Integral gives: $\|f g\|_1 \le \|f\|_p\|g\|_{p'}$.
- For $p = 1, p' = \infty$ and $\|f\|_p, \|g\|_{p'} \in (0, \infty)$.
  - Since $|f g| \le |f| \cdot \|g\|_\infty$ $\mu$-a.e. $\|f g\|_1 \le \|f\|_1 \|g\|_\infty$.

##### Ordering $\L^p$ spaces

Suppose $(X, \S, \mu)$ is a finite measure space. Where $0 < \mu(X) < \infty$.

For $0 < q \le p \le \infty$, $\L^p(\mu) \subseteq \L^{q}(\mu)$, and the linear injection $\iota: \L^p \to \L^{q}$ is continuous.

- For $0 < q < p < \infty$. $\forall f \in \L^p(\mu): \|f\|_q \le \mu(X)^{(p - q)/pq}\|f\|_p < \infty$.
  - Let $r = p / q$, $r' = p / (p - q)$. By (**Hölder**), $\||f|^q\|_1 \le \||f|^q\|_r \|1\|_{r'}$.
  - $\mu|f|^q \le (\mu |f|^{qr})^{1/r} \mu(X)^{1/r'}$. Now take $1/p$ power on both sides.
- For $0 < q < p = \infty$. $\forall f \in \L^\infty (\mu): \|f\|_q = (\mu|f|^q)^{1/q} \le \mu(X)^{1/q}\|f\|_\infty < \infty$.
- For $1 \le q < p < \infty$. $\forall f \in \L^p(\mu): \|f\|_q \le (\mu (X) + 1)^{1/q}\|f\|_p < \infty$.
  - For $c > 0$, $|f|^q = |f|^q1(|f| \le c) + |f|^q1(|f| > c \le c^q + c^{q - p}|f|^p)$.
  - Now let $c = \|f\|_p$.
- For $f \in \L^{\infty}(\mu)$, $\lim_{q \to \infty} \n{f}_q = \n{f}_\infty$.
  - $\limsup_{q\to\infty}\n{f}_q \le \n{f}_{\infty}$.
    - $\|f\|_q = (\mu|f|^q)^{1/q} \le \mu(X)^{1/q}\|f\|_\infty < \infty$.

  - $\liminf_{q \to \infty} \n{f}_q \ge \n{f}_\infty$.
    - Take $\epsilon > 0$, $\mu(|f| > \n{f}_\infty - \epsilon) > \delta$.
    - $\n{f}_q \ge (\n{f}_\infty - \epsilon)\delta^{1/p}$.


##### Sequential space

Consider measure space $(\Omega, \P(\Omega), \#)$ with counting measure.

Denote $\ell(\Omega) = \L(\Omega \to \C)$ as the space of all complex sequences.

- $\ell^p(\Omega) := \L^p(\Omega \to \C, \#) = L^p(\Omega \to \C, \#)$ for $p \in (0, \infty]$.
- When $\Omega = \N^+$, define $\ell:= \ell(\N^+)$, $\ell^p := \ell^p(\N^+)$.

