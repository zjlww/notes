(**Review: DDPM**)

The trainable **prior** is **parameterized and factorized** as $p_\theta(x_0, \ldots, x_T) = p_\theta(x_T) \prod_{n = 1}^T p_\theta(x_{n - 1} | x_{n})$.

In the DDPM formulation the **posterior** is **fixed** as a forward Markov chain with $(\beta_n)_{n = 1}^T \in (0, 1)$.
$$
q(x_{1..T}|x_0) = \prod_{n=1}^T q(x_{n} | x_{n-1}) \quad q(x_n | x_{n-1}) = \mathcal N(x_n; \sqrt {1-\beta_n} x_{n-1}, \beta_n I)
$$

- For $n \in 1.. T$ define $\alpha_n = 1 - \beta_n \in (0, 1)$ and $\bar \alpha_n = \prod_{k = 1}^n \alpha_k$. Then
  $$
  q(x_n | x_0) = \mathcal N(x_n ; x_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n )I)
  $$

- $q(x_{n - 1} | x_n, x_0) = \mathcal N(x_{n - 1}; \tilde \mu_n(x_n, x_0), \tilde \beta_n I)$. Where
  $$
  \tilde\mu_{n}\left(x_n, x_0\right)=\frac{\sqrt{\bar{\alpha}_{n-1}} \beta_{n}}{1-\bar{\alpha}_{n}} x_{0}+\frac{\sqrt{\alpha_{n}}\left(1-\bar{\alpha}_{n-1}\right)}{1-\bar{\alpha}_{n}} x_{n}; \quad \tilde{\beta}_{n}=\frac{1-\bar{\alpha}_{n-1}}{1-\bar{\alpha}_{n}} \beta_{n}
  $$

The training loss is derived as
$$
\begin{aligned}
\mathcal L_\theta(x_0) &= E_{q(z|x_0)} \log p_\theta(x_0|z) - \d{q(z|x_0)}{p_\theta(z)}\\
&= E_{q(x_{1..T}|x_0)}
\left [
\log p_\theta (x_0 | x_1)
- \sum_{n=2}^T\d{q(x_{n-1}|x_n, x_0)}{p_\theta(x_{n-1}|x_n)}
\right ] + C
\end{aligned}
$$
(**DDIM**)

In the loss derivation, it seems that $q(x_{n - 1} | x_n, x_0)$ is of importance. Define the following chain:
$$
q_\sigma(x_{1..T} | x_0) := q_\sigma (x_T | x_0) \prod_{n = 2}^T q_\sigma(x_{n - 1} | x_n, x_0)
$$
Consider random variables $X_1, \ldots, X_T$ where $X_{n - 1} = a_n X_n + b_n x_0 + \sigma_n Z_n$ where $Z_n \sim \mathcal N(0, I)$. That is the Markov chain is a **Gaussian Linear Markov chain**.

Viewing $(\sigma_n)_{n=1}^T \in [0, \infty)$ as fixed constants, and solve the parameters $a_n$ and $b_n$ under the constraint:
$$
q_\sigma(x_n | x_0) = \mathcal N \p{x_n; \sqrt{\bar \alpha_n} x_0, (1 - \bar \alpha_n) I} \implies q_\sigma(x_{n - 1} | x_0) = \mathcal N\p{x_{n-1}; \sqrt{\bar \alpha_{n - 1}} x_0, (1 - \bar \alpha_{n - 1}) I}
$$
This gives, for $n = 1..T$, $a_1 = 0$ and $b_1 = 1$, otherwise
$$
a_n = \frac{\sqrt{1 - \bar \alpha_{n - 1} - \sigma_n^2}}{\sqrt{1 - \bar \alpha_n}}; \quad b_n = \sqrt{\bar \alpha_{n - 1}} -  a_n{\sqrt{\bar \alpha_{n}}};\quad \sigma_n^2 \in [0, 1 - \bar \alpha_{n - 1}]
$$
Therefore:
$$
\begin{aligned}
\mu_n(x_n, x_0) &:= b_nx_0 + a_n x_n = \sqrt{\bar \alpha_{n - 1}} x_0 + \sqrt{1 - \bar \alpha_{n - 1} - \sigma_n^2} \cdot \frac{x_n - \sqrt{\bar \alpha_n} x_0}{\sqrt{1 - \bar \alpha_n}} \\
q_\sigma(x_{n - 1} | x_n, x_0) & = \mathcal N \p{x_{n - 1}; \mu_n(x_n, x_0), \sigma_n^2 I}
\end{aligned}
$$
Clearly, when $\sigma_n^2 = \tilde{\beta}_{n}=\frac{1-\bar{\alpha}_{n-1}}{1-\bar{\alpha}_{n}} \beta_{n}$, the **Markov posterior in DDPM** is a special case of the generalized posterior in DDIM.

All marginals for $n = 1..T$ from DDPM are preserved when $q_\sigma(x_T|x_0) = q(x_T | x_0)$ 
$$
q_\sigma(x_n | x_0) = q(x_n | x_0) = \mathcal N(x_n ; x_0 \sqrt{\bar \alpha_n}, (1 - \bar \alpha_n )I)
$$
(**DDIM: The forward transition**)

Furthermore, we can find $q_\sigma(x_n | x_{n - 1}, x_0)$ with Bayes' Rule:
$$
q_\sigma(x_n | x_{n - 1}, x_0) = q_\sigma(x_{n-1} | x_n, x_0) q_\sigma(x_n | x_0)/q_\sigma(x_{n-1} | x_0)
$$

Derivation:
$$
\log \mathcal N(x; \mu, \sigma^2) = -\frac{1}{2\sigma^2} x^2 + \frac{\mu}{\sigma^2} x - \frac{1}{2\sigma^2} \mu^2 + \text{const.}
$$
Expand $\log q_\sigma(x_n | x_{n - 1}, x_0)$ gives the following:
$$
\left [- \frac{1}{2 \sigma_n^2} x_{n - 1}^2 + \frac{\mu_n(x_n, x_0)}{\sigma_n^2} x_{n-1} - \frac{1}{2 \sigma_n^2} \mu_n(x_n, x_0)^2 \right ] + \left [ - \frac{1}{2(1 - \bar \alpha_n)} x_n^2+ \frac{\sqrt{\bar \alpha_n} x_0}{1 - \bar \alpha_n} x_n - \frac{\bar \alpha_n x_0^2}{2(1 - \bar \alpha_n)} \right ] \\
+ \left [ \frac{1}{2(1 - \bar \alpha_{n-1})} x_{n-1}^2 - \frac{\sqrt{\bar \alpha_{n-1}} x_0}{1 - \bar \alpha_{n-1}} x_{n-1} + \frac{\bar \alpha_{n-1} x_0^2}{2(1 - \bar \alpha_{n-1})} \right ]
$$
Leave only the terms that contains $x_{n}$:
$$
\frac{\mu_n(x_n, x_0)}{\sigma_n^2} x_{n-1} - \frac{1}{2 \sigma_n^2} \mu_n(x_n, x_0)^2

- \frac{1}{2(1 - \bar \alpha_n)} x_n^2+ \frac{\sqrt{\bar \alpha_n} x_0}{1 - \bar \alpha_n} x_n
$$
Extract quadratic and linear term in $x_n^2$ gives:
$$
-\frac{1 - \bar \alpha_{n - 1}}{2(1 - \bar\alpha_n)\sigma_n^2} x_n^2 + \frac{\p{x_{n-1} - x_0 \sqrt{\bar \alpha_{n - 1}}}\sqrt{1 - \bar \alpha_{n - 1} - \sigma_n^2}}{\sigma_n^2\sqrt{1 - \bar \alpha_n}} x_n + \frac{\sqrt{\bar \alpha_n} x_0}{1 - \bar \alpha_n} x_n + \text{const.}
$$
Therefore we finally have, for $2 \le n \le T$:
$$
q_\sigma(x_n | x_{n - 1}, x_0) = \mathcal N\p{x_n ; \frac{\p{x_{n-1} - x_0 \sqrt{\bar \alpha_{n - 1}}}\sqrt{\p{1 - \bar \alpha_{n - 1} - \sigma_n^2} \p{1 - \bar \alpha_n}} + \sqrt{\bar \alpha_n} x_0}{(1 - \bar \alpha_{n - 1})}, \frac{(1 - \bar \alpha_n) \sigma_n^2}{(1 - \bar \alpha_{n-1})} I}
$$
(**DDIM: parameterization**)

In DDIM we still have $X_n = x_0 \sqrt{\bar \alpha_n} + Z_n\sqrt{1 - \bar \alpha_n}$ where $Z_n$ is a standard Normal variable.

We ask the neural network $e_\theta(x_n, n)$ to predict Gaussian noise $Z_n$ similar to DDPM. Define the estimated $x_0$ with function $e_\theta$ as $f_\theta$.
$$
f_\theta(x_n, n) := \frac{x_n - \sqrt{1 - \bar \alpha_n} \cdot e_\theta(x_n, n)}{\sqrt{\bar \alpha_n}}
$$
Define the generative process $p_\theta(x_{0..T})$ as a backward Markov chain as in DDPM. The ELBO has a very simple form:
$$
\begin{aligned}
\mathcal L_\theta(x_0) &= E_{q_\sigma(z|x_0)} \log p_\theta(x_0|z) - \d{q_\sigma(z|x_0)}{p_\theta(z)}\\
&= E_{q_\sigma(x_{1..T}|x_0)}
\left [
\log p_\theta (x_0 | x_1)
- \sum_{n=2}^T\d{q_\sigma(x_{n-1}|x_n, x_0)}{p_\theta(x_{n-1}|x_n)}
\right ] + \operatorname{const.}
\end{aligned}
$$
The form of the loss inspires us to define:

- $p_\theta(x_T) = \mathcal N(x_T; 0, I)$.
- $p_\theta(x_{n-1} | x_n) = q_\sigma(x_{n - 1} | x_n, f_\theta(x_n, n))$ for $n = 2..T$.
  - Similar to DDPM, there is the problem of picking the variance. And this is the optimal choice for $q_0(x_0) = \delta(x_0 - c_0)$.

- Similar to DDPM, there is some freedom at $n = 1$ in the choice of $p_\theta(x_0 | x_1)$.

Now, consider the KL terms, recall that $b_n = \sqrt{\bar \alpha_{n - 1}} -  a_n{\sqrt{\bar \alpha_{n}}}$.

- By the analytic KL-divergence of isotropic Gaussians:
  $$
  D_\theta^{(n)}:= \d{q(x_{n - 1} | x_n, x_0)}{p_\theta(x_{n - 1} | x_n)} = C + \frac{\norm{b_n(f_\theta(x_n, n) - x_0)}^2_2}{2\sigma_n^2}
  $$

- Now make substitution and replace $x_0$ with $e_n$.
  $$
  D_\theta^{(n)} = C + \frac{1}{2\sigma_n^2}{\norm{b_n \frac{\sqrt{1 - \bar \alpha_n} (e _n - e_\theta(x_n, n))}{\sqrt{\bar \alpha_n}}}_2^2} = C + \frac{b_n^2 (1 - \bar\alpha_n)}{2\sigma_n^2 \bar \alpha_n}\norm{e_n - e_\theta(x_n, n)}_2^2
  $$

(**Limiting Case**)

Consider the limiting case where $\sigma_n \downarrow 0$ for $n=1..T$. In this case:
$$
a_n = \frac{\sqrt{1 - \bar \alpha_{n - 1}}}{\sqrt{1 - \bar \alpha_n}}; \quad b_n = \sqrt{\bar \alpha_{n - 1}} -  a_n{\sqrt{\bar \alpha_{n}}}
$$
And sampling from $q_\sigma(x_{n-1} | x_n, f_\theta(x_n, n))$ becomes deterministic:
$$
\begin{aligned}
x_{n-1} &= \sqrt{\bar \alpha_{n - 1}} f_\theta(x_n, n) + \sqrt{1 - \bar \alpha_{n - 1}} \cdot e_\theta(x_n, n) \\
&= \sqrt{\bar \alpha_{n - 1}} \frac{x_n - \sqrt{1 - \bar \alpha_n} \cdot e_\theta(x_n, n)}{\sqrt{\bar \alpha_n}} + \sqrt{1 - \bar \alpha_{n - 1}} \cdot e_\theta(x_n, n) \\
\frac{x_{n-1}}{\sqrt{\bar \alpha_{n-1}}} - \frac{x_n}{\sqrt{\bar \alpha_n}} &= \p{\sqrt{\frac{1 - \bar \alpha_{n - 1}}{\bar \alpha_{n - 1}}}- \sqrt{\frac{1 - \bar \alpha_n}{\bar \alpha_{n}}}} \cdot e_\theta(x_n, n)
\end{aligned}
$$
Now assume there exists (same name) continuous time function of their discrete counterparts:

- $x(t): [0, 1] \to \R^d$ where $x\p{n / T} = x_n$.
- $\bar \alpha(t): [0, 1]\to [0, 1)$ where $\bar \alpha(n / T) = \bar \alpha_n$.
  - Therefore $\bar \alpha(0) = 1$. We require it to be smooth and strictly decreasing.
- $\phi(t): [0,1) \to [0, \infty)$ where $\phi(t):= \sqrt{\frac{1 - \bar \alpha(t)}{\bar \alpha(t)}}$.
  - $\phi(t)$ is increasing from $0$ up to $+\infty$.
- $e_\theta(x(t), t): \R^d \times [0, 1] \to \R^d$ where $e_\theta(x_n, n) = e_\theta(x(n/T), n/T)$.
- $y(t): (0, 1) \to \R^d$, $y(t):= x(t) / \bar \alpha(t)$.

Therefore the sampling process can be viewed as backward solving following ODE:
$$
y'(t) = \phi'(t) e_\theta(y(t) \bar \alpha(t), t)
$$
