#### Gaussian Density

##### Gaussian density function

A parameterized probability density for $x \in \R^d$, $\mu \in \R^d$ and positive definite real matrix $\Sigma\in \R^{d \times d}$.
$$
p_{\mu, \Sigma}(x) = \mathcal N(x ; \mu, \Sigma) =\frac{1}{(2 \pi)^{m / 2}(\operatorname{det} \Sigma)^{1 / 2}} \exp\left[{-\frac{1}{2}{(x-\mu)}^T{\Sigma^{-1}(x-\mu)}}\right]
$$

##### Splitting joint Normal distribution

Suppose $X_a \in \L(\Omega \to \R^n)$, $X_b \in \L(\Omega \to \R^m)$ and $X = (X_a, X_b) \sim \mathcal N(\mu, \Sigma)$.
Suppose $\mu=\left(\begin{array}{l}\mu_{a} \\ \mu_{b}\end{array}\right)$ and $\Sigma =\left(\begin{array}{ll} \Sigma _{a a} & \Sigma _{a b} \\ \Sigma _{b a} & \Sigma _{b b}\end{array}\right)$, and $\Lambda =\left(\begin{array}{cc} \Lambda _{a a} & \Lambda _{a b} \\ \Lambda _{b a} & \Lambda _{b b}\end{array}\right)$.

We can immediately see that $p(x_a|x_b)$ is Normal by looking at unnormalized conditional density.

- We can solve for its mean and variance as following:

- Recall that:
  $$
  p(x_a, x_b) = \frac{1}{(2\pi)^{m/2}|\Sigma|^{1/2}} \exp \left (-\frac{1}{2} (x^T \Lambda x - 2x^T \Lambda \mu + \text{const.})\right)
  $$

- Define $\Delta_a = (x_a - \mu_a)$ and $\Delta_b = (x_b - \mu_b)$. Then we have
  $$
  p(x_a, x_b) = \frac{1}{(2\pi)^{m/2}|\Sigma|^{1/2}} \exp \left (-\frac{1}{2}(\Delta_a^T \Lambda_{aa}\Delta_a + 2 \Delta_a^T \Lambda_{ab} \Delta_b + \Delta_b^T \Lambda_{bb} \Delta_b)\right)
  $$

- Now consider $x_b$ as constant, and sort in power of $x_a$ gives:
  $$
  \frac{1}{(2\pi)^{m/2}|\Sigma|^{1/2}} \exp\left (
  -\frac{1}{2}\left(x_{a}^T \Lambda_{aa}x_a + 2 x_a^T(\Lambda_{ab}(x_b - \mu_b) - \Lambda_{aa}\mu_a) + \text{const.}\right)
  \right)
  $$

- Therefore conditional density $p(x_a|x_b)$ is $\mathcal N(x_a;\mu_a - \Lambda_{aa}^{-1} \Lambda_{ab}(x_b - \mu_b), \Lambda_{aa}^{-1})$.

- Recall the partitioned matrix inverse identity:
  $$
  \left(\begin{array}{ll} A & B \\ C & D \end{array}\right)^{-1}=\left(\begin{array}{cc} M & - M B D ^{-1} \\ - D ^{-1} C M & D ^{-1}+ D ^{-1} C M B D ^{-1}\end{array}\right);\quad M =\left( A - B D ^{-1} C \right)^{-1}
  $$

- By definition, we have $\left(\begin{array}{ll} \Sigma _{a a} & \Sigma _{a b} \\ \Sigma _{b a} & \Sigma _{b b}\end{array}\right)^{-1}=\left(\begin{array}{ll} \Lambda _{a a} & \Lambda _{a b} \\ \Lambda _{b a} & \Lambda _{b b}\end{array}\right)$.

- Therefore we can express $\Lambda$ blocks in $\Sigma$:

  - $\Lambda _{a a}=\left( \Sigma _{a a}- \Sigma _{a b} \Sigma _{b b}^{-1} \Sigma _{b a}\right)^{-1}$.
  - $\Lambda _{a b}=-\left( \Sigma _{a a}- \Sigma _{a b} \Sigma _{b b}^{-1} \Sigma _{b a}\right)^{-1} \Sigma _{a b} \Sigma _{b b}^{-1}$.

- Therefore $p(x_a|x_b) = \mathcal N(x_a; \mu _{a}+ \Sigma _{a b} \Sigma _{b b}^{-1}\left( x _{b}- \mu _{b}\right), \Sigma _{a a}- \Sigma _{a b} \Sigma _{b b}^{-1} \Sigma _{b a})$.

Marginal density is $p(x_a) = \mathcal N(x_a; \mu_a, \Sigma_{aa})$ following from the marginal theorem of characteristic functions.

##### Linear Gaussian models

Suppose $X \in \L(\Omega \to \R^m)$ and $Y, Z\in \L(\Omega \to \R^n)$ where $X \sim \mathcal N(\mu, \Lambda^{-1})$.

Suppose $A \in \R^{n \times m}$ and $Z \sim \mathcal N(b, L^{-1})$ where $X \perp Z$.

Define $Y = AX + Z$. Then the joint distribution of $(X, Y)$ is still Gaussian.

- Notice that $\left(\begin{array}{c} X \\ Y\end{array}\right) = \left(\begin{array}{cc}I & O \\ A & I\end{array}\right)\left(\begin{array}{l} X \\ Z\end{array}\right)$.
- Therefore $(X, Y)$ is jointly normal distributed.
  - $E\left(\begin{array}{c} X\\ Y\end{array}\right)= \left(\begin{array}{cc}I & O \\ A & I\end{array}\right)\left(\begin{array}{c}\mu\\ b\end{array}\right) = \left(\begin{array}{c}\mu\\ A\mu + b\end{array}\right)$.
  - $\cov\left(\begin{array}{c}X \\ Y\end{array}\right) = \left(\begin{array}{cc}I & O \\ A & I\end{array}\right)\left(\begin{array}{cc}\Lambda^{-1} & O \\ O & L^{-1}\end{array}\right)\left(\begin{array}{cc}I & A^T \\ O & I\end{array}\right) = \left(\begin{array}{cc}\Lambda^{-1} & \Lambda^{-1}A^T \\ A\Lambda^{-1} & A\Lambda^{-1}A^T + L^{-1}\end{array}\right)$
- So far we have density functions:
  - $p(x) = \mathcal N(x; \mu, \Lambda^{-1})$.
  - $p(y|x) = \mathcal N(y; Ax + b, L^{-1})$.
  - $p(y) = \mathcal N(y; A\mu + b, A \Lambda^{-1}A^T + L^{-1})$.
- We know that $p(x|y) = \mathcal N\left(\Sigma\left\{ A ^{ T } L ( y - b )+ \Lambda \mu \right\}, \Sigma\right)$. Where $\Sigma =\left( \Lambda + A ^{ T } L A \right)^{-1}$.

##### KL-divergence of Gaussian densities

Suppose $p_1(x) = \mathcal N(x; \mu_1, \Sigma_1)$ and $p_2(x) = \mathcal N(x; \mu_2, \Sigma_2)$ are two density on $\R^d$.
$$
\d{p_1(x)}{p_2(x)} = \frac{1}{2} \left [ 
\log \det\Sigma_2 - \log \det \Sigma_1 - n + \operatorname{tr}(\Sigma_2^{-1}\Sigma_1) + (\mu_2 - \mu_1)^T \Sigma_2^{-1}(\mu_2 - \mu_1)
\right]
$$
Further suppose that $p_1$ and $p_2$ are diagonal then
$$
\d{p_1(x)}{p_2(x)} = \frac{1}{2} \left [
2 \sum_{i} \log \sigma_{2,i} - 2 \sum_i \log \sigma_{1, i} - n + \sum_i{\frac{\sigma^2_{1,i}}{\sigma^2_{2,i}}} + \sum_i\frac{(\mu_2 - \mu_1)^2_i}{\sigma^2_{2,i}}
\right]
$$

##### Differential entropy of gaussian density

For single gaussian $X \sim \mathcal N (\mu, \Sigma)$, the entropy would be:
$$
h(X) = -E_{X} \log p(X)  = \frac{1}{2} \log [(2\pi e)^n|\Sigma|] = \frac{1}{2}[\log(2\pi)n + n +  2 \sum_i \log \sigma_{i}]
$$

##### Cross entropy of gaussian densities

$$
h(p,q) = -\int p(x) \log q(x) \dd x = -E_{X\sim p(x)}\log q(X) = h(p) + D(p || q)
$$

For diagonal gaussians, the cross entropy would be:
$$
h(p_1, p_2) = \frac{1}{2}\left [
\log(2\pi) n + 2 \sum_i \log \sigma_{2, i} + \sum_i \frac{\sigma_{1, i}^2}{\sigma_{2, i}^2} + \sum_i \frac{(\mu_2 - \mu_1)_i^2}{\sigma_{2,i}^2}
\right]
$$
