#### Polynomial Rings over UFDs

##### Contents and primitive parts

Suppose $D$ is a **UFD**.

Consider **nonzero** $f(x) \in D[x]$ and $f(x) = a_0 + a_1 x + \cdots + a_n x^n$.

Define $\cont(f) := \GCD_D(a_0, \ldots, a_n)$.

- $a \in \cont(f)$ is called a **content** of $f(x)$.
- $f$ is **primitive** if $\cont(f) = D^*$.
- Denote the set of all primitive polynomials as $D[x]_p$. (This is not a standard notation.)

Define $\pp(f): \c{g(x) \in D[x]_p \mid \exists c \in D: f(x) = cg(x)}$.

- $g(x) \in \pp(f)$ is called a **primitive part** of $f(x)$.

There is a one-to-one correspondence between $\cont(f)$ and $\pp(f)$.

- Given $a \in \cont(f)$, there exists a unique $g(x) \in \pp(f)$ where $f(x) = a g(x)$.
- Given $g(x) \in \pp(f)$, there exists a unique $a \in \cont(f)$ where $f(x) = ag(x)$.

##### Gauss's Lemma I

Suppose $D$ is a **UFD**. A product of two primitive polynomials in $D[x]$ is again primitive.

Or to be more concise, $D[x]_p \cdot D[x]_p = D[x]_p$.

- Consider $f, g \in D[x]_p$.

- Suppose $a(x)=a_{0}+a_{1} x+\cdots+a_{n} x^{n}$ and $b(x)=b_{0}+b_{1} x+\cdots+b_{m} x^{m}$.

- Consider $h(x) := f(x)g(x)$.

- Let $p$ be any irreducible in $D$. Then $p \notin \cont(h)$.

  - $p \notin \cont(f)$ and $p \notin \cont(g)$.

  - Let $a_{r}$ be the lowest coefficient of $f(x)$ not divisible by $p$.

  - Let $b_s$ be the lowest coefficient of $g(x)$ not divisible by $p$.

  - The coefficient of $x^{r+s}$ in $h(x)=f(x) g(x)$ is
    $$
    c_{r+s}=\left(a_{0} b_{r+s}+\cdots+a_{r-1} b_{s+1}\right)+a_{r} b_{s}+\left(a_{r+1} b_{s-1}+\cdots+a_{r+s} b_{0}\right)
    $$

  - Now $p \mid a_{i}$ for $i<r$ implies that $p \mid\left(a_{0} b_{r+s}+\cdots+a_{r-1} b_{s+1}\right)$.

  - Also $p \mid b_{j}$ for $j<s$ implies that $p \mid\left(a_{r+1} b_{s-1}+\cdots+a_{r+s} b_{0}\right)$.

  - But $p \nmid a_r$ and $p \nmid b_s$, so $p \nmid a_rb_s$, otherwise, $p$ must divide one of them (since $p$ is prime.)

  - Consequently $p \nmid c_{r + s}$. So $p \notin \cont(h)$.

- Therefore $\cont(h) = D^*$. So $h(x) \in D[x]_p$.

For nonzero $f, g \in D[x]$, we have:

- $\cont(fg) = \cont(f) \cdot \cont(g)$.
- $\pp(fg) = \pp(f) \cdot \pp(g)$.

##### Gauss's Lemma II

Suppose $D$ is a **UFD** and $D'$ is a fraction field of $D$. Consider non-constant $f(x) \in D[x]$.

($\from$) $f(x)$ reducible in $D'[x]$ is reducible in $D[x]$.

- Since $f(x)$ is reducible in $D'[x]$.
  $$
  \exists r(x), s(x) \in D'[x]:\p{f(x) = r(x) s(x) \land \deg r(x) > 0 \land \deg s(x) > 0}
  $$

- Take $u, v \in D$ large enough, such that $u\cdot r(x), v \cdot s(x) \in D[x]$. Let $d = u v$.

  - Suppose $f(x) = f_c f_p(x)$ where $f_c \in \cont(f(x))$.
  - Suppose $u \cdot r(x) = r_c r_p(x)$ where $r_c \in \cont(u r(x))$.
  - Suppose $v \cdot s(x) = s_c s_p(x)$ where $s_c \in \cont(vs(x))$.

- Then we have
  $$
  df(x) = (u\cdot r(x)) (v\cdot s(x)) \implies df_c f_p(x) = r_c s_c r_p(x) s_p(x)
  $$

- Therefore $df_c = r_c s_cu$ for some $u \in D^*$.
  $$
  f_p(x) = r_p(x) s_p(x) \in D[x]_p
  $$

- So $f(x)$ is reducible in $D[x]$.

($\to$) Primitive $f(x)$ reducible in $D[x]$ is reducible in $D'[x]$.

> Consider this example: $2x + 2$ is irreducible in $\Q[x]$, but reducible in $\Z[x]$ as $2(x + 1)$.

- Since $f(x)$ is reducible, $f(x) = r(x) s(x)$ for some nonzero nonunit $r, s \in D[x]$.
- Since $f(x)$ is primitive, $\deg r(x) > 0$ and $\deg s(x) > 0$.
- Therefore $r(x), s(x)$ are also nonzero nonunit in $D'[x]$.

##### Polynomial rings over UFDs are UFDs

Let $D$ be a **UFD**. Then $D[x]$ is also a **UFD**.

- $f(x) \in D[x]_p$ is a product of primes in $D[x]_p$.
  - Suppose $f(x)$ is reducible, and $f(x) = u(x) v(x)$ where $u, v$ are nonzero nonunit elements.
  - Since $f(x)$ is primitive, $\deg u(x) > 0$ and $\deg v(x) > 0$.
  - We can repeat this factorization process until $f(x)$ is a product of primes.
- For $f(x) \in D[x]_p$, the prime factorization is unique (up to associates).
  - Suppose $f(x) = \prod_{i = 1}^s h_i(x) = \prod_{i = 1}^t g_i(x)$ for $(h_i)_{i = 1}^s, (g_i)_{i = 1}^t \subseteq D[x]_p$.
  - Since $(h_i), (g_i)$ are primitive primes in $D[x]$, they are primes in $D'[x]$.
  - Since $D'$ is a field, $D'[x]$ is a PID and UFD.
  - Since $D'[x]$ is a UFD,
    - we must have $s = t$.
    - and there exists $\sigma \in S_\c{1, \ldots, s}$ such that $h_i \sim g_{\sigma(i)}$ in $D'[x]$.
  - $h_i \sim g_{\sigma(i)}$ in $D'[x]$ implies $h_i \sim g_{\sigma(i)}$ in $D[x]$.
    - Suppose $a / b \in D'$ where $a, b \in D$. And $h_i = a/b g_{\sigma(i)}$.
    - Therefore $bh_i = a g_{\sigma(i)}$.
    - Since $bD^* = \cont_D(b h_i) = \cont_D(a g_{\sigma(i)}) = aD^*$, we have $a \sim_D b$.
    - Therefore $a/d \in D^*$ and $h_i \sim g_{\sigma(i)}$ in $D[x]$.

##### Eisenstein's Criterion

Suppose $D$ is a **UFD**. And $f(x) = \sum_{i=0}^n a_i x^i \in D[x]$ is a **non-constant primitive**.

$f(x)$ is **irreducible** if for some **prime element** $p \in D$.

- $\forall 0 \le i < n: p \mid a_i$. And $p^2 \nmid a_0$.

Proof with contradiction, for $f(x)$ with $\deg f \ge 2$.

- Suppose $f(x) = g(x)h(x)$ where $g, h$ are non-constants in $D[x]$.
- Clearly $g, h$ are both primitives.
- $p \mid g_0 h_0$. so w.l.o.g. assume $p \mid g_0$.
- Since $g$ is primitive, for some $g_k$, $p \nmid g_k$ and $p \mid g_{k-1} ,\ldots, g_0$.
- $a_k = g_0 h_k + \cdots + g_k h_0$.
- Since also $p \mid a_k$, we have $p \mid g_k h_0$, therefore $p \mid h_0$.
- Therefore $p \mid g_0$ and $p \mid h_0$, therefore $p^2 \mid g_0 h_0$, that is $p^2 \mid a_0$.
- This is a contradiction with $p^2 \nmid a_0$.

Suppose $p$ is prime in UFD $D$. $x^n - p \in D[x]$ is irreducible.

##### Polynomial rings over fields are PIDs

Suppose $F$ is a **field**. Then $F[x]$ is a PID.

- Consider $N \sqsubseteq F[x]$.

- Suppose $N = \{0\}$ is the trivial ideal, $N = (0)$.

- Suppose $N$ is nonzero.

  - Let $m = \min\c{\deg f(x) \mid f(x) \in N}$. There exists $g(x) \in N$ where $\deg g(x) = m$.

  - Suppose $m = 0$. Clearly $N = (1) = F[x]$.
  - Suppose $m > 0$. $N = (g(x))$.
    - Consider any $f(x) \in N$. By Euclidean division, $f(x) = q(x) g(x) + r(x)$ where $\deg r < m$.
    - $r(x) = f(x) - q(x) g(x) \in N$. So $r(x) = 0$.

##### GCD in polynomial rings over fields

Suppose $F$ is a **field**. $F[x]$ is a PID.

Recall that for $A \subseteq F[x]$, function $\GCD_{F[x]}(A)$ returns a set of associated polynomials.

Define $\gcd_{F[x]}(A)$ the **monic** polynomial in set $\GCD_{F[x]}(A)$.

##### Exercise 2-2

Suppose $D$ is a UFD, and $F$ is a quotient field of $D$.

Suppose $f(x) \in D[x]$ is monic, $g(x) \in F[x]$ is monic and $g(x) \mid f(x)$ in $F[x]$. Then $g(x) \in D[x]$.

- Suppose $f(x) = g(x) h(x)$ for some monic $h(x) \in F[x]$.
- Take $u, v \in D$ such that $u g \in D[x]$ and $v h \in D[x]$.
- We have $u \in \cont(ug(x))$ and $v \in \cont (vh(x))$ since $g, h$ are monic.
- $g(x) \in D[x]$. (Similarly $h(x) \in D[x]$.)
  - There exists a unique $g_p(x) \in \pp(ug(x))$ where $ug(x) = u g_p(x)$.
  - Therefore $g(x) = g_p(x) \in D[x]$.

