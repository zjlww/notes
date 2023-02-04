### Gaussian Process and Gaussian Distribution

(**Normal distribution**)

$N(a, \sigma^2)$ is a distribution $\mu(x)$ on $\B(\R)$ with density $f(x)$:
$$
f(x)=\frac{1}{\sqrt{2 \pi} \sigma} \exp \left[-\frac{(x-a)^{2}}{2 \sigma^{2}}\right]
$$

- $N(0, 1)$ is called the standard Normal distribution.
- $\widehat N(a, \sigma^2)$ is $\widehat{\mu}(\theta)=\mathrm{e}^{i \theta a} \mathrm{e}^{-\frac{1}{2} \sigma^{2} \theta^{2}}$.
- $N(a, \sigma^2) * N(b, \tau^2) = N(a + b, \sigma^2 + \tau^2)$.

(**Multivariate Normal distribution**)

Suppose $\mu_1, \ldots, \mu_m$ are standard normal distributions. Let $\mu = \times_i \mu_i$. Then $\mu$ has density $f(x): \R^m \to (0, \infty)$.

$$
f(x)=\frac{1}{\sqrt{2 \pi}} {e}^{-x_{1}^{2} / 2} \ldots \frac{1}{\sqrt{2 \pi}} {e}^{-x_{m}^{2} / 2}=\frac{1}{(2 \pi)^{m / 2}} {e}^{-\pd{x}{x}/2}
$$
Suppose $X \sim \mu$ and $Y = AX + a$ where $A \in \R^{n \times m}$ and $a \in \R^n$. Then
- $\varphi_Y(\theta) = e^{i \pd \theta a} e^{-\pd {A^* \theta}{A^* \theta}/2}$.
- Denote $\Sigma = A A^* \in \R^{n \times n}$.
    - Positive $\Sigma$ has unique **positive** square root denoted $\sqrt \Sigma$. $Y = \sqrt \Sigma X + a$.
- $\varphi_Y(\theta) = e^{i \pd \theta a} e^{-\pd {\Sigma\theta}{ \theta}/2}$. 
- Since $\cov(Y) = \cov(AX + a) = AA^* = \Sigma$, $\Sigma$ is the **covariance matrix** of $Y$.
    - Also define the **precision matrix** $\Lambda := \Sigma ^{-1}$.
    - $E[Y^TY] = E[(AX+a)(AX+a)^*] = E[AA^*+aa^*]$.
- Denote the distribution of $X$ as $N(0, I_m)$ and $Y$ as $N(a, \Sigma)$. These are called multivariate Normal distributions.

We have the following results for multivariate Normals:
- $N(a, \Sigma) * N(b, \Lambda) = N(a + b, \Sigma + \Lambda)$.

- Suppose $X \sim N(a, \Sigma)$, then $Y = AX + b \sim N(Aa + b, A\Sigma A^*)$.

- Suppose $X \sim N(a, \Sigma)$, then $X_k \sim N(a_k, \Sigma_{kk})$.

- Suppose $X \sim N(a, \Sigma)$. $\Sigma$ is diagonal if and only if $(X_k)$ are independent.
    - $\Sigma$ is diagonal iff $\varphi_X(\theta) = \times_i \varphi_{X_i}(\theta_i)$ iff $(X_k)$ are independent.
    
- Suppose $X \in \L(\Omega \to \R^d)$. $X \sim N(a, \Sigma)$ iff for all $\Gamma \in \R^d$, $\Gamma^T X$ is Gaussian.
    - The $\to$ direction is apparent. For the other direction...
    - Coordinates $X_k$ are clearly all Gaussian.
    - Define $\cov (X_i, X_j) = \Gamma_{ij} \in \R$. And $E[X_i] = z_i \in \R$.
    - $a = E[\pd \gamma X] = \gamma^T E[X] = \pd \gamma z$.
    - $\sigma^2 = E[\pd{\gamma}{X}^2] - a^2 = \gamma^T \Gamma \gamma$.
    - Therefore $E[e^{i \pd {\gamma}{X}}] = e^{i \pd \gamma z} e^{-\pd{\Gamma \gamma}{\gamma}/2}$. So $X \sim N(a, \Gamma)$.
    
- Suppose $X \sim N(a, \Sigma)$ and $\Sigma$ is not invertible. The distribution is called **degenerate**.
    - $X$ is degenerate if and only if the coordinates $(X_k)$ are linearly dependent (with probability one).
        - Suppose $X_k = +_{i \neq k}c_i X_i$ then $\cov(X_k, X_j) = +_{i \neq k} \cov(X_i, X_j)$. So $\Sigma$ is not invertible.
        - Suppose $\Sigma$ is not invertible, then suppose $\Sigma\theta = 0$. The projection $\pd \theta X$ is a Gaussian with $E[\pd \theta X] = \theta^T E[X]$ and zero variance. So with probability one, $(X_k)$ are linearly dependent.
    
- Consider $\mu = N(a, \Sigma)$ where $\Sigma$ is invertible, then $\mu$ has density function $g(x): \R^n \to [0, \infty)$:
  $$
  g(y)=\frac{1}{(2 \pi)^{m / 2}(\operatorname{det} \Sigma)^{1 / 2}} \exp\left[{-\frac{1}{2}{(y-a)}^T{\Sigma^{-1}(y-a)}}\right]
  $$
  
    - Define quadratic form $\Delta^2 = (y-a)^T \Sigma^{-1}(y-a)$.
  
- (**Convergence in law: TODO**) Suppose $(X_n), X \in \L(\Omega \to \R^d)$ where $X_n$ are Gaussians and $X_n \to X$ in law. Then $X$ is Gaussian.

- (**Convergence in L2: TODO**) Suppose $(X_n), X \in \L(\Omega \to \R^d)$ where $X_n$ are Gaussians and $X_n \to X$ in $\L_2$. Then $X$ is Gaussian.

(**Gaussian family**)

Random variable families $\X, \mathcal Y \subseteq \L^1(\Omega \to \R^d, \F, P)$. $\X$ is called a Gaussian family if all finite subset $(X_1, \ldots, X_m) \in \X$ is $dm$-dimensional Gaussian.

- Suppose $\X, \mathcal Y$ are Gaussian families, and $\X \cap \mathcal Y$ is a Gaussian family. $\mathcal X \perp \mathcal Y$ if and only if $\forall X, Y \in \mathcal X\times \mathcal Y: \cov (X, Y) = 0$.

(**Gaussian process**)

Suppose $(\Omega, \F, P)$ is a probability space. An $\R^d$-valued process $(X_t)_{t \in T}$ is a Gaussian process if it is a Gaussian family.

- Let $b_t = E[X_t]$ be the mean function.
- Let $K_{ij}(s, t) = \cov(X_s^{(i)}, X_t^{(j)})$ where $1 \le i, j \le d$ be the covariance function.
- The covariance function should generate **positive** covariance matrices.
- Then the existence is guaranteed by (**Kolmogrov's extension theorem**).

(**Log-normal Distribution**)

Suppose $X \sim \mathcal N(\mu, \sigma^2)$. Define $Y = \exp X$. Then

- For $y > 0$. $F_Y(y) = P(Y \le y) = P(X \le \ln y) = F_X(\ln y)$.
- Since $F_X \in D[\R]$ and $\ln y \in D(0, \infty)$. $F_Y \in D(0, \infty)$.
- A density function is $f_Y(y) = f_X(\ln y)/y$ for $y > 0$.

(**Chi-square distribution**) Suppose $X \sim \mathcal N(0, 1)$. Then $Y = X^2 \sim \chi^2(1)$.

