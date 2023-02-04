### Uniform Integrability

(**Uniform integrable**)

Suppose $(\Omega, \A, \mu)$ is a measure space.

Consider family $\F \subset \L^{1}(\Omega \to \bar \R, \mu)$. Then $\F$ is uniformly integrable if
1. $\forall \epsilon > 0, \exists g \in \L^1(\Omega \to [0, \infty], \mu), \forall f \in \F: \mu(|f| - g)^+ \le \epsilon$.
2. $\forall \epsilon > 0, \exists g \in \L^1(\Omega \to [0,\infty], \mu), \forall f \in \F: \mu(1_{|f| > g}|f|) \le \epsilon$.
    - $2 \to 1$ is apparent.
    - $1 \to 2$. Let $g \in \L^1(\Omega \to [0, \infty], \mu)$ such that $\sup_f \mu(|f| - g)^+ \le \epsilon$.
        - $\mu(1_{|f| > 2g} |f|) \le \mu(1_{|f| > 2g}(|f| - g)^+) + \mu(1_{|f| > 2g} g) \le 2\epsilon$.

Suppose $\mu$ is finite. Then $\F$ is uniformly integrable if and only if
3. $\forall \epsilon > 0, \exists a\in[0, \infty), \forall f \in \F: \mu(|f| - a)^+ \le \epsilon$.
    - $3 \to 1$ is apparent.
4. $\forall \epsilon > 0, \exists a\in[0, \infty), \forall f \in \F: \mu(1_{|f| > a}|f|) \le \epsilon$.
    - $4 \to 3$ is apparent.
    - $2 \to 4$. Let $g \in \L^1(\Omega \to [0, \infty], \mu)$ such that $\sup_f \mu(1_{|f| > g}|f|) \le \epsilon$.
        - There exists an $a \in[0,\infty)$ such that $\mu(1_{g > a}g) \le \epsilon$.
        - $\mu(1_{|f| > a}|f|) \le \mu(1_{|f| > g} |f|) + \mu(1_{g > a} g) \le 2 \epsilon$ (Hint: draw a diagram!)

For $\F, \G \in \L^1(\Omega \to \bar \R, \mu)$:
- Suppose $\F$ is a finite set, then $\F$ is uniformly integrable.
- Suppose $\F, \G$ are uniformly integrable. Then $\F \oplus \G: \{f + g: f, g \in \F \times \G\}$, $\F \ominus \G$ and $|\F| = \{|f|: f \in \F\}$ are uniformly integrable.
- Suppose $\F$ is uniformaly integrable and $\forall g \in \G, \exists f \in \F: |g| \le |f|$, then $\G$ is uniformly integrable.

(**Scaled integrable, de la Vallee Poussin Criterion**)

Suppose $(\Omega, \A, \mu)$ is a finite measure space.

$\F \in \L^1(\Omega \to \R, \mu)$ is uniformly integrable **if and only if** there exists $H: [0, \infty) \to [0, \infty)$ where $\lim_{x \to \infty}H(x) / x = \infty$ and $\sup_{f \in \F}\mu H(|f|) < \infty$.

Intuitively speaking, even after $|f|$ is stretched bigger by $H(x)$ which grows faster than $x$, $\mu H|f|$ remains uniformly bounded.

- $\leftarrow$ direction:
    - Define $K_a := \inf_{x \ge a}H(x) / x$. $K_a \to \infty$ as $a \to \infty$.
    - $\mu(1_{|f| > a} |f|) \le \mu(1_{|f| > a}H(|f|)/K_a) \le \mu(H(|f|))/K_a$.
    - Take supremum over $f \in \F$: $\sup \mu(1_{|f| > a} |f|) \le \sup \mu(H(|f|))/K_a$.
    - Take $a \to \infty$ shows that $\sup\mu(H(|f|)) / K_a \to 0$.
- $\to$ direction:
    - Exists increasing $a_n \in [0, \infty)$ where $\sup_{f \in \F} \mu(|f| - a_n)^+ < 2^{-n}$ and $a_n \uparrow \infty$.
    - Define $H(x) = \sum_{n} (x - a_n)^+$ on $[0, \infty)$. $H$ is **convex** and **increasing**.
    - $H(2a_n)/(2a_n) \ge \sum_{k = 1}^n(2a_n - a_k)/(2a_n) \ge n / 2$ so $H(x) / x \to \infty$.
    - For $f \in \F$, $\mu(H(|f|)) = \sum_{n = 1}^\infty \mu(|f| - a_n)^+ \le 1$. So $\sup\mu H(|f|) < \infty$.

(**Bounded $(1, \infty)$ norm and uniform integrability**)

Suppose $(\Omega, \A, \mu )$ is a measure space.

Suppose $\mu$ is **finite** and $p \in (1, \infty)$, and $\F \subset \L^p(\Omega \to \bar \R, \mu)$ with **uniformly bounded norms**. Take $H(x) = x^p$ where $H(x) / x \to \infty$. Clearly $\F$ is **uniformly integrable**.

Notice that this theorem does not work for $p = 1$.

(**Bounded $\L^1$ norm and uniform integrability**)

Suppose $(\Omega, \A, \mu)$ is a $\sigma$-finite measure space.

The family $\F \subset \L^1(\Omega \to \bar \R, \A, \mu)$ is uniformly int. iff following are both true:
1. $\F$ has **uniformly bounded norms**, $\sup_{f \in \F} \mu |f| < \infty$.
2. $|\F|$ is **uniformly absolutely continuous** w/ resp. to $h\cdot \mu$ for some $h \in \L^1(\Omega \to [0, \infty], \mu)$.
   $\exists h \in \L^1(\Omega \to [0, \infty], \mu),\forall \epsilon > 0, \exists \delta > 0, \forall A \in\A: \mu_A(h) < \delta \to \sup_{f \in \F}\mu_A(|f|) \le \epsilon$.

- Since $\mu$ is $\sigma$-finite. There exists $h \in \L^1(\Omega \to [0, \infty], \mu)$ where $h > 0$ everywhere.
- As $\F$ is uniformly integrable. $\forall \epsilon > 0, \exists g \in \L^1(\Omega \to [0,\infty], \mu), \forall f \in \F: \mu(1_{|f| > g}|f|) \le \epsilon$.
    - $C = \sup_{f \in \F} \mu|f| \le \sup_{f \in \F}\mu(1_{|f| > g}|f|) + \mu g < \infty$.
    - Since $\{g > \alpha h\} \downarrow \varnothing$ as $\alpha \uparrow \infty$. There exists a $\alpha \in (0, \infty)$ where $\mu(1_{g > \alpha h} g) < \epsilon$.
    - Let $\delta = \epsilon / \alpha$. When $A \in \A$ and $\mu_A(h) < \delta$.
    - $\mu_A |f| \le \mu_A(1_{|f| > g}|f|) + \mu_A(g)\le \epsilon + \mu_A(1_{g > \alpha h} g) + \mu_A(\alpha h) \le 3 \epsilon$.
- Suppose condition 1 and 2 is true. Then
    - For any $\epsilon > 0$. Define $g = C h / \delta$.
    - $\mu(1_{|f| > g} h) = \delta / C \mu(1_{|f| > g} g)\le \delta / C \mu (|f|) \le \delta$.
    - Let $A = \{|f| > g\}$, then $\forall f \in \F: \mu(1_{|f| > g}|f|) \le \epsilon$.

Suppose $\mu$ is **finite**. The family $\F \subset \L^1(\Omega \to \bar \R, \mu)$ is uniformly int. iff following are both true:

1. $\F$ has **uniformly bounded norms**. $\sup_{f \in \F}\mu |f| < \infty$.
2. $|\F|$ is **uniformly absolutely continuous** with respect to $\mu$.
    - $\forall \epsilon > 0, \exists \delta > 0, \forall A \in \A: \mu(A) < \delta \to \sup_{f \in \F} \mu_A(|f|) \le \epsilon$.

- Suppose $\F$ is uniformly integrable. $\forall \epsilon > 0, \exists a \in [0, \infty), \forall f \in \F: \mu(1_{|f| > a} |f|) \le \epsilon$.
    - $C = \sup_{f \in \F} \mu |f| \le \mu(1_{|f| > a}|f|) + a\mu\Omega < \infty$.
    - Let $\delta = \epsilon / a$. Assume $A \in \A$ and $\mu(A) < \delta$.
    - $\mu_A|f| \le \mu_A(1_{|f| > a}|f|) + a \mu A \le 2 \epsilon$.
- Suppose condition 1 and 2 is true. Then
    - For any $\epsilon > 0$. Define $g = C / \delta$.
    - $\mu(1_{|f| > g}) = \delta / C \mu (1_{|f| > g} g) \le \delta$.
    - Let $A = \{|f| > g\}$, then $\forall f \in \F: \mu(1_{|f| > g}|f|) \le \epsilon$.

(**Uniform Fatou**) ^uniform-fatou

Suppose $(\Omega, \A, \mu)$ is a **finite** measure space. And $(f_n)_{n = 1}^\infty \in \L^1(\Omega \to \R, \mu)$ is **uniformly integrable**.

Then $\mu (\liminf_n f_n) \le \liminf_n \mu f_n \le \limsup_n \mu f_n \le \mu (\limsup_n f_n)$. This generalizes [[05_abstract_integral#^fatou|Fatou's Lemma]] to real valued functions.

- For a fixed $\epsilon > 0$, there exists $c > 0$ such that $\sup_n\mu(1_{|f_n| > c} |f_n|) \le \epsilon$.
- Since $\mu f_n = \mu (1_{f_n < -c} f_n) + \mu(1_{f_n \ge -c} f_n)$. $\mu(f_n) \ge \mu(f_n1_{f_n \ge -c}) - \epsilon$.
- So $\liminf_n \mu f_n \ge \liminf_n \mu(f_n 1_{f_n \ge -c}) - \epsilon$.
- $\mu(\liminf_n f_n) \le \mu(\liminf_n (f_n 1_{f_n \ge -c})) \le \liminf_n \mu(f_n 1_{f_n \ge -c}) \le \liminf_n \mu f_n + \epsilon$.
- Now take $\epsilon \downarrow 0$. The other half follows by symmetry.

(**Uniform integrability and convergence in measure**)

Suppose $(\Omega, \A, \mu)$ is a **finite** measure space. And $(f_n)_{n = 1}^\infty \in \L^1(\Omega \to \R, \mu)$ is **uniformly integrable**.

Suppose $f \in \L(\Omega \to \R)$ and $f_n \to f$ in $\mu$. Then $f \in \L^1(\Omega \to \bar \R, \mu)$ and $\mu f_n \to \mu f$.
- Suppose $\mu f_n \not\to \mu f$. Then there exists a subsequence $(f_k)\subseteq(f_n)$ such that $\exists \epsilon > 0, \forall k: |\mu f_k - \mu f| > \epsilon$.
- Since $f_k \to f$ in $\mu$, according to [[08_convergence#^in-measure-subsequence|Subsequence]] theory, there exists $(f_m) \subseteq (f_k)$ such that $f_m \to f$ $\mu$.a.e.
- Apply [[#^uniform-fatou|Uniform Fatou]] to the sequence $(f_m)$, we have $\mu f_m \to \mu f$. Contradiction!

(**Uniform integrability and convergence in $\L^p$**)

Suppose $(\Omega, \A, \mu)$ is a **finite** measure space.

Suppose $p \in (0, \infty)$, $(f_n)_{n = 1}^\infty, f \in \L(\Omega \to \R, \A)$ and $f_n \to f$ in $\mu$. Suppose $(|f_n|^p)$ is uniformly integrable. Then $f_n \to f$ in $\L_p$.

- Take subsequence $(f_k)$ of $(f_n)$, where $f_k \to f$ essentially pointwise.
- We can show that $(|f_n - f|^p)$ is uniformly integrable.
    - Since $(|f_k|^p)$ is uniformly integrable and $|f_k|^p \to |f|^p$ in $\mu$.
        - $|f|^p \in \L^1(\Omega \to [0, \infty], \mu)$. So $\mu |f|^p < \infty$.
        - And $\mu |f_k|^p \to \mu |f|^p$.
    - For $p \le 1$, $|f_n - f|^p \le |f_n|^p + |f|^p$.
    - For $p \ge 1$, $|f_n - f|^p \le 2^{p - 1} (|f_n|^p + |f|^p)$.
    - So $\mu |f_n - f|^p$ is bounded.
    - Since $\F = (|f_k|^p)$.
- Some subsequence $(f_k)$ of $(f_n)$, $f_k \to f$ essentially pointwise.
- $|f_k - f|^p \to 0$ in $\mu$, so $\mu|f_k - f|^p \to 0$.

