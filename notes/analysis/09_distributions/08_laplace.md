$$
\newcommand{D}{{\mathcal D}}
\newcommand{H}{{\mathcal H}}
\newcommand{G}{{\mathcal G}}
\newcommand{loc}{{\operatorname{loc}}}
\newcommand{M}{\mathcal M}
\newcommand{P}{\mathcal P}
\newcommand{B}{\mathbb B}
\newcommand{E}{\mathcal E}
\newcommand{F}{\mathcal F}
\newcommand{J}{\mathcal J}
\newcommand{A}{\mathcal A}
\newcommand{L}{\mathcal L}
\newcommand{S}{\mathcal S}
\newcommand{su}{\operatorname{supp}}
\newcommand{re}{\operatorname{Re}}
\newcommand{im}{\operatorname{Im}}

\newcommand{pf}{\operatorname{Pf}}
\newcommand{pv}{\operatorname{Pv}}
\newcommand{pd}[2]{\left \langle #1, #2 \right\rangle}
\newcommand{dp}{\mathbf{D}}
\newcommand{ip}{\mathbf{I}}
\newcommand{cas}{\D'_+}
\newcommand{acas}{\D'_-}
\newcommand{f}{\mathfrak F}
\newcommand{fi}{\mathfrak F^{-1}}
\newcommand{Fi}{\mathcal F^{-1}}
\newcommand{l}{\mathfrak L}
\newcommand{li}{\mathfrak L^{-1}}
\newcommand{Li}{\mathcal L^{-1}}
$$

### Laplace Transform on $\cas$

----

##### Fourier representation

 Suppose $f(t) \in \cas(\R)$. Define the **abscissa of convergence**:
$$
\sigma_1 = \inf\{c \in \R: f(t) e^{-ct} \in \S'(\R)\}
$$
The open half-plane $\re s > \sigma_1$ is the **half-plane of convergence** (or just ROC).

> For $f \in L_\loc$, ROC might be larger than ROAC. ROC can not be smaller than ROAC.

The distributional Laplace transform is defined using Fourier transform in $\S'$ and $\S$:
$$
\forall \sigma > \sigma_1:F(\sigma + i\omega) = \F[e^{-\sigma t} f(t)](\omega)
$$
Denote this as $\L[f](\sigma + i\omega) = F(\sigma + i\omega) = \F[e^{-\sigma t}f(t)](\omega)$.

---

##### Direct representation

 Suppose $\lambda(t)$ is a soft indicator on $\su f(t)$.

For any $\phi(\omega) \in \S(\R)$, and $\sigma > \sigma - h = c >  \sigma_1$:
$$
\begin{aligned}
\pd{F(\sigma + i\omega)}{\phi(\omega)} & = \pd{\F[f(t) e^{-\sigma t}]}{\phi(\omega)} = \pd{f(t) e^{-\sigma t}}{\F[\phi](t)}\\
& = \pd{f(t) e^{-\sigma t}}{\int_{-\infty}^\infty \phi(\omega)e^{-i\omega t} d\omega}\\
& = \pd{f(t) e^{-\sigma t + h t}}{\int_{-\infty}^\infty \lambda(t)\phi(\omega)e^{-ht}e^{-i\omega t} d\omega}\\
& = \int_{-\infty}^\infty  \pd{f(t) e^{-\sigma t + h t}}{\lambda(t)e^{-ht}e^{-i\omega t}}  \phi(\omega) d\omega\\

\end{aligned}
$$
Make the substitution $c = (\sigma - h)$ and $h = \sigma - c$, 
$$
F(s) = F(\sigma + i\omega) = \L[f(t)](s) = \pd{e^{-ct} f(t)}{\lambda(t) e^{-(s- c)t}}
$$
And the above works for only $\re s > c$ case, and $c > \sigma_1$. And can be **short handed** into
$$
F(s) = \L[f](s) = \pd{f(t)}{e^{-st}}
$$

- When $f \in L_{\loc, +}$, the distribution Laplace transform = standard transform.
- $F(\sigma + i \omega)$ is a complex function of $\omega$.

----

##### Zero Laplace transform

 Suppose $f \in \cas(\R)$ and $F(c + i\omega) = 0$ for some verticle line in ROC. For any $\phi \in \S(\R)$, therefore for all $\hat \phi \in \S(\R)$.
$$
\pd{F(c + i\omega)}{\phi(\omega)} = \pd{\F[e^{-ct}f(t)](\omega)}{\phi(\omega)} = \pd{e^{-ct} f(t)}{\hat \phi(t)}
$$
So $e^{-ct}f(t) = 0$ in $\S'$, so $f(t) = 0$ in $\D'$.

----

##### Uniqueness theorem

 Suppose $f, g \in \cas(\R)$ and $F(s) =G(s)$ on some vertical line $s = c + i\omega$ in their ROC.

Then $F(s) - G(s) = \L[f-g](s) = 0$ on $s = c + i\omega$. So $f = g$ in $\D'$.

----

##### Analyticity theorem

 Suppose $f \in \cas(\R)$ and is Laplace transformable, with abscissa $\sigma_1$.

Then $F(s) = \L[f(t)](s)$ is analytic on ROC $\re s > \sigma_1$. And
$$
F'(s) = \pd{e^{-ct} f(t)}{\lambda(t)(-t) e^{-(s- c)t}} = \pd{-t f(t)}{e^{-s t}}
$$

----

##### Linearity

 Suppose $f, g \in \cas$ are Laplace transformable, and has abscissa $\sigma_f, \sigma_g$. Then 
$$
\L[\alpha f  + \beta g] = \alpha F(s) + \beta G(s); \quad \re s > \max(\sigma_f, \sigma_g)
$$

----

Suppose $f \in \E'(\R)$, notice that $f e^{-\sigma t} \in \E'(\R)$ for all $\sigma \in \R$.
$$
F(s) = F(\sigma + i \omega) \L[f(t)](s) = \F[f(t) e^{-\sigma t}](\omega)
$$
$F(s)$ is analytic everywhere.

----

##### Laplace transform of Dirac functionals

 
$$
\L[\delta] = 1; \quad \L[\delta(t - \tau)] = e^{-s\tau}; \quad \L[\delta^{(k)}] = s^k;\quad \L[u(t)] = 1 / s;
$$

----

##### Common operations on Laplace transform

 Suppose $f,g  \in \cas(\R)$ are Laplace transformable. 

- (**Frequency derivative**) Since $\L[-tf(t)] = F'(s)$,  we immediately have $\L[t^k f(t)] = (-1)^k F^{(k)}(s)$ for 
  $$
  \L[t^k f(t)] = (-1)^k F^{(k)}(s);\quad \re s > \sigma_f
  $$

- (**Time derivative**) Suppose $f(t) e^{-\sigma t} \in \S'(\R)$, then
  $$
  \dp (f(t) e^{-\sigma t})  = \dp f(t) e^{-\sigma t} + f(t) (-\sigma) e^{-\sigma t} \in \S'(\R)
  $$
  So $\dp f(t) e^{-\sigma t} \in \S'(\R)$.  So taking derivative does not shrink ROC. Also
  $$
  \L[f^{[k]}(t)] = s^k F(s); \quad \re s > \sigma_f
  $$

- (**Time shifting**) Suppose $f(t) e^{-\sigma t} \in \S'(\R)$, then $f(t - \tau) e^{-\sigma t} e^{\tau \sigma} \in \S'(\R)$. So time shift does not change ROC. Also
  $$
  \L[f(t - \tau)] = e^{-s \tau} F(s); \quad\re s > \sigma_f
  $$

- (**Frequence shifting**)
  $$
  \L[e^{-\alpha t} f(t)] = F(s + \alpha); \quad \re s > \sigma_f - \re \alpha
  $$

- (**Time scaling**) Suppose $a > 0$:
  $$
  \L[f(at)](s) = \frac{1}{a}F\left(\frac{s}{a}\right)
  $$

----

##### Continuity of right-sided Laplace transform

 Suppose $f_k \in \cas(\R)$​, and suppose $\Omega = \bigcup \su f_k$​ is causal. Then
$$
e^{-ct} f_k(t) \to e^{-ct}f(t) \text{ in }\S'(\R) \implies F_k(s) \to_{\re s > c} F(s) \text{ pointwise}
$$

> Recall that $\S'$ is closed under convergence, so $e^{-ct} f(t) \in \S'(\R)$.

### Classical Half-sided Laplace Transform

Suppose $f: (0, \infty) \to \C$, and for some $\sigma \in \R$, $f(t) e^{-\sigma t} \in L^1(0, \infty)$.

The classical Laplace transform for $f(t)$ is the Laplace transform of the extended function $u(t) f(t) = f_e(t): \R \to \C$.
$$
\l_+[f(t)] = \l[f_e(t)] = \l[f(t) u(t)] = \int_0^\infty f(t) e^{-s t} dt
$$

----

Suppose $f(t) \in C^1(0, \infty)$ and $f(0+)$ exists. Suppose:
$$
\l[f_e(t)] = \L[f_e(t)] = \l_+[f(t)] = F(s)
$$
Proceed in distributional Laplace transform:
$$
\dp f_e(t) = u(t) D f(t) + f(0+)\delta(t) \implies \\
\L[\dp f_e (t)](s) = \L[u(t) Df(t)](s) + f(0+) = s\L[f_e(t)](s)
$$
So we have the well known formula in classical definition:
$$
\l_+[f'(t)] = sF(s) - f(0+)
$$

### Inversion of Laplace Transformation in $\cas$

---

Suppose $F(s): \S \subseteq \C \to \C$ is analytic on $\re s \ge c$ and is bounded in norm by $P(|s|)$, where $P$ is a real polynomial.

So we can define $G(s) = F(s) / s^m$ such that $|G(s)| \le C / |s|^2$ for $\re s \ge a \ge c$.

Suppose $g(t)$ is the **unique causal and continuous** function such that $G(s) = \L[g](s)$.
$$
\L[g(t)] = G(s) \implies \L[\dp^m g(t)] = s^m G(s) = F(s); \quad \re s > a
$$
So $f(t) = g^{[m]}(t)$ in $\cas(\R)$ gives $F(s)$ for at least $\re s > a$.

So every **rational function** of $s$ is the Laplace transform of a right-sided distribution, when taking the ROC on the far-right.

----

**Enhancement of above result:**

Suppose $F(s): S \subseteq \C \to \C$ is analytic on $\re s \ge c$ and is bounded in norm by $e^{\re s T}P(|s|)$. Where $T > 0$ and $P$ is a real polynomial. 

Then define $G(s) = F(s) / (e^{s T} s^m)$, such that $|G(s)|\le C / |s|^2$ for $\re s \ge a \ge c$.

Suppose $g(t)$ is the **unique causal and continuous** function such that $G(s) = \L[g](s)$.
$$
\L[g(t)] = G(s) \implies \L[\dp^m g(t - T)] = s^m e^{sT} G(s) = F(s); \quad \re s >  a
$$
So $f(t) = g^{[m]}(t - T)$ in $\cas(\R)$ gives $F(s)$ for $\re s > a$.

----

##### Partial fraction and rational Laplace transform

Suppose $F(s): \C \to \C$ is of the form:
$$
F(s)=\frac{\alpha_{n} s^{n}+\alpha_{n-1} s^{n-1}+\cdots+\alpha_{0}}{\beta_{m} s^{m}+\beta_{m-1} s^{m-1}+\cdots+\beta_{0}}
$$
Suppose $n > m$, divide using long division and obtain:
$$
F(s)=\sum_{\nu=0}^{n-m} \xi_{\nu} s^{\nu}+\frac{\rho_{p} s^{p}+\rho_{p-1} s^{p-1}+\cdots+\rho_{0}}{\beta_{m} s^{m}+\beta_{m-1} s^{m-1}+\cdots+\beta_{0}}; \quad p < m
$$
Now do partial-fraction expansion, suppose there are $q$ different roots and each with degree $k_\mu$.
$$
F(s)=\sum_{\nu=0}^{n-m} \xi_{\nu} s^{\nu}+\sum_{\mu=1}^{q} \sum_{\nu=1}^{k_{\mu}} \frac{\zeta_{\mu \nu}}{\left(s-\gamma_{\mu}\right)^{\nu}}; \quad \sum_{\mu=1}^{q} k_{\mu}=m
$$
Take the ROC on the far-right,
$$
f(t)=\sum_{\nu=0}^{n-m} \xi_{\nu} \delta^{(\nu)}(t)+\sum_{\mu=1}^{q} \sum_{\nu=1}^{k_{\mu}} \frac{\zeta_{\mu \nu}}{(\nu-1) !} t^{\nu-1} e^{\gamma_{\mu} t} u(t)
$$
When $n \le m - 2$, $f(t)$ must be continuous everywhere.

----

**Convolution in $\cas(\R)$ and Laplace Transform:**

Suppose $f, g \in \cas(\R)$ and are Laplace transformable with abscissa $\sigma_f$ and $\sigma_g$. 

Notice that for all $\phi \in \D(\R)$:
$$
\begin{aligned}
\pd{[e^{-c t} f(t)] *[e^{-c t} g(t)]}{\phi(t)}
&=\pd{e^{-c t} f(t)}{\pd{e^{-c r} g(\tau)}{\phi(t+\tau)}} \\
&=\pd{f(t)}{\pd{g(\tau)}{e^{-c(t+r)}\phi(t+\tau)}} \\
&=\pd{f(t) * g(t)}{e^{-c t} \phi(t)} \\
&= \pd{e^{-c t}[f(t) * g(t)]}{\phi(t)}
\end{aligned}
$$
Then $f \star g \in \cas(\R)$. And
$$
\L[f \star g](s)=\pd{e^{-c t} f(t) \times e^{-c \tau} g(\tau)}{\lambda(t+\tau) e^{-(s-c)(t+\tau)}}; \quad \re s > c
$$
Replace $\lambda(t + \tau)$ with $\lambda(t)\cdot \lambda(\tau)$.
$$
E (f * g) =\left\langle e^{-c t} f(t), \lambda(t) e^{-(s-c) t}\right\rangle\left\langle e^{-c \tau} g(\tau), \lambda(\tau) e^{-(s-c) r}\right\rangle=F(s) G(s) \quad \operatorname{Re} s > \max(\sigma_f, \sigma_g)
$$

### Anti-causal Laplace Transform

The results are exactly symmetric of the right-sided version.

Suppose $f(t) \in \acas(\R)$. Suppose $\lambda(t)$ is a soft indicator on $\su f(t)$.

- Define the **abscissa of convergence**: $\sigma_2 = \sup\{c \in \R: f(t) e^{-ct} \in \S'(\R)\}$.

- Define the Laplace transform: $\forall \sigma < \sigma_2:F(\sigma + i\omega) = \F[e^{-\sigma t} f(t)](\omega)$.

- $F(s) = \L[f](s) = \pd{f(t)}{e^{-st}} = \pd{e^{-ct} f(t)}{\lambda(t) e^{-(s- c)t}}$ for $\re s < c < \sigma_2$.

  - $F(s)$ is a complex-valued function of $s \in \C$.

- (**Uniqueness**) Suppose $f, g \in \acas(\R)$ and $F(s) = G(s)$ on some vertical line $s = c + i\omega$ in their ROC. Then $f = g$ in $\D'$.

- (**Analyticity**) $F(s)$​ is analytic on ROC. And the derivative is given by
  $$
  F'(s) = \pd{e^{-ct} f(t)}{\lambda(t)(-t) e^{-(s- c)t}} = \pd{-t f(t)}{e^{-s t}}
  $$

- (**Linearity**) Suppose $f, g \in \cas$ are Laplace transformable, and has abscissa $\sigma_f, \sigma_g$. Then
  $$
  \L[\alpha f  + \beta g] = \alpha F(s) + \beta G(s); \quad \re s < \min(\sigma_f, \sigma_g)
  $$

----

The following formulas works for left-sided Laplace transforms as well:

- $\L[t^k f(t)] = (-1)^k F^{(k)}(s);\quad \re s < \sigma_f$.
- $\L[f^{[k]}(t)] = s^k F(s); \quad \re s < \sigma_f$.
- $\L[f(t - \tau)] = e^{-s \tau} F(s); \quad\re s < \sigma_f$.
- $\L[e^{-\alpha t} f(t)] = F(s + \alpha); \quad \re s > \sigma_f - \re \alpha$.
- $\L[f(at)](s) = \frac{1}{a}F\left({s}/{a}\right); \quad \re {s}/{a} < \sigma_2$.

----

### Double-sided Laplace Transform

Suppose $f(t) \in \D'(\R)$​ is in general unbounded distribution. 

Suppose $\theta(t), 1 - \theta(t) \in C^\infty$​​​​ such that $f_+(t) = f(t) \theta(t)$​​ is causal and $f_-(t) = f(t) (1 - \theta(t))$​​ is anti-causal, with abscissa $\sigma_1$​​ and $\sigma_2$​​.

The absiccas are **independent** of the soft partition $\theta(t)$​. Since all bounded distributions in $\E'(\R)$​ are also in $\S'(\R)$​.

Suppose $\sigma_1 < \sigma_2$, the funciton is double-sided Laplace transformable.

The open region $\sigma_1 < \re s< \sigma_2$​​ is called the region of convergence (ROC) in this case.

Under the following definition, the Laplace transform $F(s)$ is also **independent** of the soft partition $\theta(t)$.
$$
F(s) = \L[f(t)](s) = \L[f_+](s) + \L[f_-](s) = F_+(s) + F_-(s);\quad \sigma_1 < \re s < \sigma_2
$$
Further, this can be represented using Fourier transform:
$$
F(\sigma + i\omega) = F_+(\sigma + i\omega) + F_-(\sigma + i \omega) = \F[e^{-\sigma t}f_+(t)] + \F[e^{-\sigma t}f_-(t)] = \F[e^{-\sigma t}f(t)];
$$
Suppose $f(t), g(t) \in \D'(\R)$​​ are double sided laplace transformable. Then

- (**Linearity**) $\L[\alpha f  + \beta g] = \alpha F(s) + \beta G(s); \quad \max(\sigma^-_f, \sigma^-_g) < \re s < \min(\sigma^+_f, \sigma^+_g)$.
- (**Uniqueness**) $F(s) = G(s)$ on some verticle line $\sigma + i\omega$ implies $f = g$ in $\D'$​.

----

##### Analyticity

 $F(s)$​ is analytic on its ROC. The derivative is given by $F_+(s)$ and $F_-(s)$.
$$
F_+'(s) = \pd{e^{-ct} f_+(t)}{\lambda_+(t)(-t) e^{-(s- c)t}} = \pd{-t f_+(t)}{e^{-s t}}\\
F_-'(s) = \pd{e^{-ct} f_-(t)}{\lambda_-(t)(-t) e^{-(s- c)t}} = \pd{-t f_-(t)}{e^{-s t}}
$$

-----

##### Continuity

 

Let $\left\{f_{\nu}\right\}_{\nu=1}^{\infty} \in \D'(\R)$ and $f_{\nu} = f_{\nu, +} + f_{\nu, -}$​.

Suppose $\Omega_+ =\bigcup_\nu f_{\nu, +}$ and $\Omega_-$ are causal and anti-causal.

Suppose for $c_2 \in \R$​, $e^{-c_2 t}f_{\nu, -} \to e^{-c_2 t}f_{-}$​ in $\D'$​. So $F_{\nu, -} (s) \to F_-(s)$ in $\re s < c_2$.

Suppose for $c_1 \in \R$​, $e^{-c_1 t}f_{\nu, +} \to e^{-c_1 t}f_{+}$​ in $\D'$​.  So $F_{\nu, +} (s) \to F_+(s)$​ in $\re s > c_1$​.

And $c_1 < c_2$. Then $F_\nu(s) \to F(s)$​ for $c_1 < \re s < c_2$.
