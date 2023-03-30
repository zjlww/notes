#### Tweedie's formula

> Efron, B. (2011). Tweedie’s Formula and Selection Bias. *Journal of the American Statistical Association, 106*, 1602 - 1614.

##### Tweedie's formula 1D

Suppose $X, Y, Z$ are real random variables. Where $X$ has density $p(x)$ respect to the Lebesgue measure. $Z \sim \mathcal N(0, \sigma^2)$, $X \perp Z$. And $Y = X + Z$.

Assume all densities and conditional densities exists. Then $Y$ has density $p(y) = \int p(x) p(y | x) \dd x$.

We have
$$
p(y | x) = \mathcal N(y - x;0, \sigma^2) = \frac{1}{\sqrt{2\pi} \sigma} \exp \s{-\frac{(x - y)^2}{2 \sigma^2}}
$$
Since the density is of exponential form, note that:
$$
D_y p(y|x) = \frac{y - x}{\sigma^2} p(y|x)
$$
Therefore
$$
\begin{aligned}
E\s{X | Y = y} & = \int_\R x p(x | y) \dd x = \frac{1}{p(y)}\int_\R x {p(y | x) p(x)} \dd x\\
& = \frac{1}{p(y)} \int_\R (x - y) p(y|x) p(x) \dd x + \frac{1}{p(y)} \int _\R y p(y|x) p(x)\dd x\\
& = y - \frac{1}{p(y)} \int _\R \sigma^2 D_y p(y | x) p(x) \dd x\\
& = y - \frac{\sigma^2}{p(y)} D_y p(y) = y - \sigma^2 D_y \log p(y)
\end{aligned}
$$

##### Tweedie's formula nD

Suppose $\mathbf X, \mathbf Y, \mathbf Z$ are $\R^n$ random variables. Where $\mathbf X$ has density $p(\mathbf x)$ respect to the Lebesgue measure. $\mathbf Z \sim \mathcal N(0, \sigma^2 I_n)$, $\mathbf X \perp \mathbf Z$. And $\mathbf Y = \mathbf X + \mathbf Z$. Then we have **tweedie's formula**
$$
E[\mathbf X | \mathbf Y = \mathbf y] = \mathbf y - \sigma^2 \nabla \log p(\mathbf y)
$$
