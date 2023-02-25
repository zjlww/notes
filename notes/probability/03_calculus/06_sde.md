$$
\newcommand{M}{\mathcal M}
\newcommand{P}{\mathcal P}
\newcommand{B}{\mathbb B}
\newcommand{E}{\mathcal E}
\newcommand{F}{\mathcal F}
\newcommand{G}{\mathcal G}
\newcommand{J}{\mathcal J}
\newcommand{A}{\mathcal A}
\newcommand{U}{\mathcal U}
\newcommand{L}{\mathcal L}
\newcommand{T}{\mathcal T}
\newcommand{S}{\mathcal S}
\newcommand{X}{\mathcal X}
\newcommand{V}{\mathcal V}
\newcommand{re}{\operatorname{Re}}
\newcommand{im}{\operatorname{Im}}
\newcommand{null}{\operatorname{null}}
\newcommand{span}{\operatorname{span}}
\newcommand{cov}{\operatorname{Cov}}
\newcommand{pd}[2]{\left \langle {#1},{#2} \right \rangle}
$$

### Stochastic Differential Equations

##### Stochastic Differential Equations

Suppose $(B_t)$ are $\R^m$-valued standard BM.

Suppose $\sigma(t, x) \in \L([0, T] \times \R^n \to \R^{n \times m})$ and $\mu(t, x) \in \L([0, T] \times \R^n \to \R^n)$.

$(\sigma, \mu)$ defines an stochastic differential equation of the following form:
$$
dX_t = \sigma(t, X_t) dB_t + \mu(t, X_t)dt, \quad t \in [0, T]
$$

##### Strong and weak solution to SDE

Consider **SDE** $dX_t = \sigma(t, X_t) dB_t + \mu (t, X_t) dt$, $t \in [0, T]$.

Given $(\Omega, \F, P)$ and $(B_t)$ a standard BM and $Z \in \L(\Omega \to \R^n, \F)$ the initial value.

$(\Omega, \F, (\F_t), [0, T], P)$ with $(X_t), (B_t)$ is a **strong solution** to the SDE if:

1. $(B_t) \in \M_c^m(T)$.
2. $(X_t)$ is adapted to $(\F_t)$ and progressively measurable.
3. Integrals $\sigma(t, X_t) dB_t$ and $\mu(t, X_t) dt$ are well-defined.
4. $X_0 = Z$. And $\forall t \in [0, T]: P\left(X_t = X_0 + \int_0^t \sigma(s, X_s) dB_s + \int_0^t \mu(s, X_s)ds\right) = 1$.

Given **initial distribution** $\mu$. (And functions $\sigma, \mu$ of course.)

$(\widetilde \Omega, \widetilde \F, (\widetilde \F_t), [0, T], \widetilde P)$ with $(X_t), (B_t)$ is a **weak solution** to the SDE if:

1. $(B_t) \in \M_c^m(T)$ is a standard BM.
2. $(X_t)$ is adapted to $(\widetilde F_t)$.
3. Integral $\sigma(t, X_t) dB_t$ and $\mu(t, X_t) dt$ are well-defined.
4. $\widetilde P_{X_0} \sim \mu$. And $\forall t \in [0, T]: P\left(X_t = X_0 + \int_0^t \sigma(s, X_s) dB_s + \int_0^t \mu(s, X_s)ds\right) = 1$.

Clearly a strong solution is also a weak solution.

Due to different definitions, the uniqueness has different definitions as well:

- A **strong solution** is called **pathwise unique** if any other strong solution $(Y_t)$, $P(\forall t \in [0, T]: X_t = Y_t) = 1$.
- A **weak solution** is called **weakly unique** if any other weak solution $(Y_t)$ has the same finite dimensional distirbutions.

##### Strong condition I: Oksendal

 ==TODO==

Suppose $\sigma(t, x) \in \L([0, T] \times \R^n \to \R^{n \times m})$ and $\mu(t, x) \in \L([0, T] \times \R^n \to \R^n)$.

Consider SDE: $dX_t = \sigma(t, X_t) dB_t + \mu(t, X_t)dt, (*)$ on $t \in [0, T]$.

- Given $(\Omega, \F, P)$ and $(B_t)$ a $\R^m$ valued standard BM.
- Define $\F^B = \sigma(B_t^{(j)}, 1 \le j \le m, t \in [0, T])$.
- Given $Z \in \L^2(\Omega \to \R^n, P)$ where $Z \perp \F^B$. Define $\F_t = \sigma(Z, B_{\le t}) \le \F_t$.
- $\exists C \ge 0,\forall x \in \R^n, t \in [0, T]: \|b(t, x)\| + \|\sigma(t, x)\| \le C(1 + \|x\|)$.
- $\exists D \ge 0, \forall x, y \in \R^n, t \in [0, T]: \|b(t,x) - b(t, y)\| + \|\sigma(t, x) - \sigma(t, y)\| \le D\|x - y\|$.

Consider filtered space $(\Omega, \F, (\F_t), [0, T], P)$. We claim:

- There exists $(X_t) \in \V_c(T)$ that is a **strong solution** to the SDE.
- $(X_t)$ is **pathwise unique** in $\V_c(T)$.
  - Any other $(Y_t) \in \V_c(T)$, $P(\forall t \in [0, T]: X_t = Y_t) = 1$.
- All weak solutions of $*$ are **weakly unique**.
- $(X_t)$ is Markov with respect to $(\F_t)$.

##### OU process

A real valued **Gaussian process** $(B_t)_{t \ge 0}$ on $(\Omega, \F, P)$ with zero mean and covariance function $\cov(B_s, B_t) = {e^{-2(t-s)}}(1-e^{-2 s})/2$ for $s \le t$ is an **zero-starting Ornstein-Uhlenbeck process**.

A real valued Gaussian process $(B_t)_{t \in \R}$ with zero mean and covariance $\cov(B_s, B_t) = e^{-2(t - s)}/2$ for $s \le t$ is an **stationary Ornstein-Uhlenbeck process**.

- $(B_t)$ has a **continuous** modification.
- Since $\cov(B_s, B_t)$ only depends on $(t - s)$, the process is **stationary**.

##### Langevin SDE and OU process

Let $\alpha, \sigma \ge 0$, $dX_t = -\alpha X_t dt + \sigma dB_t$ is an **Langevin SDE**.

- $X_t$ is the momentum physically, and $-\alpha X_t$ is the impedence, $\sigma dB_t$ is the pertubation.
- Suppose $X_0 = x_0$ and $\sigma = 0$, the ODE has unique solution $X_t = x_0e^{-\alpha t}$.
- Let $Y_t = X_t e^{\alpha t}$. $dY_t = d(X_t e^{\alpha t}) = \alpha X_t e^{\alpha t} dt + e^{\alpha t} dX_t = \sigma e^{\alpha t} dB_t$.
- So $Y_t - Y_0 = \int_0^t \sigma e^{\alpha s} dB_s$.

The solution to the Langevin equation is a **scaled OU process**. $X_t = X_0 + e^{-\alpha t}\int_0^t \sigma e^{\alpha s} dB_s$.

Define $Y_t = e^{-t} \int_0^t e^s dB_s$. Then $Y_t$ is an **OU process** started at zero.

- Clearly $Y_t$ is a Gaussian process with zero mean.
- ${E}[Y_{t} Y_{s}]=e^{-t-s} \int_{0}^{s} e^{2 u} d u=\frac{1}{2}(e^{-(t-s)}-e^{-(t+s)})$.

