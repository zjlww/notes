#### Score Matching

##### The score matching problem

Consider density $p(x): \R^d \to [0, \infty)$ with score $\nabla \log p(x)$. Train a parameterized vector field $s_\theta(x)$ for $\theta \in \Theta$ such that $s_\theta(x) \approx \nabla \log p(x)$. 

The **Fisher divergence** between $s_\theta(x)$ and $\nabla \log p(x)$ is $\frac{1}{2} E_{X \sim p(x)} \left [ \norm{\nabla \log p(X) - s_\theta(X)}_2^2\right]$.

- Is it really good to optimize for the Fisher divergence? It does not optimize "the sampling result".
- Matching directly with fisher divergence is called **explicit score matching** (ESM).

##### Implicit score matching

> Hyvärinen, A. (2005). Estimation of Non-Normalized Statistical Models by Score Matching. *J. Mach. Learn. Res., 6*, 695-709.

**Implicit score matching** demonstrates that optimizing for $E_{X \sim p(x)} \left [\frac{1}{2} \norm{s_\theta(X)}^2_2 + \tr (\nabla s_\theta(X))\right ]$ is equivalent to optimize for the Fisher divergence.
$$
\begin{aligned}
E_{X \sim p(x)} \norm{\nabla \log p(X) - s_\theta(X)}^2_2 & = E\s{(\nabla \log p(X) - s_\theta(X))^T (\nabla \log p(X) - s_\theta(X))}\\
& = E \norm{s_\theta(X)}^2_2 - 2 E [(\nabla \log p(X))^T (s_\theta(X))] + E \norm{\nabla \log p(X)}^2_2\\
& = E \norm{s_\theta(X)}^2_2 - 2\int_\R p(x) \sum_{i = 1}^d \left (\part_i \log p(x) \cdot s_\theta(x)_i\right) \dd x + C\\
& = E \norm{s_\theta(X)}^2_2 - 2\sum_{i = 1}^d \int_\R \left (\part_i p(x) \cdot s_\theta(x)_i\right) \dd x + C\\
& = E \norm{s_\theta(X)}^2_2 + 2 \sum_{i = 1}^d \int_\R p(x) \part_i s_\theta(x)_i \dd x + C\\
& = E \norm{s_\theta(x)}^2_2 + 2E \s{\tr \nabla s_\theta(X)} + C
\end{aligned}
$$

##### Denoising score matching

> Vincent, P. (2011). A Connection Between Score Matching and Denoising Autoencoders. *Neural Computation, 23*, 1661-1674.

Suppose some **Markov density kernel** $p_\sigma(\widetilde x | x)$ is used to perturb the original density, called the **perturbation kernel**.

Denote the **perturbed density** $p_\sigma(\widetilde x, x) = p_\sigma(\widetilde x | x) p(x)$. And the **marginal density** $p_\sigma(\widetilde x)$.

**Denoising score matching** demonstrates that minimizing for 
$$
D_\theta = \frac{1}{2} E_{\widetilde X, X  \sim p_\sigma(\widetilde x, x)} \s{\norm{s_\theta(\widetilde X) - \nabla_{\widetilde X} \log p_\sigma(\widetilde X | X)}^2_2}
$$
is equivalent to explicit score matching.

Recall **explicit score matching** $J_\theta = \frac{1}{2} E_{\widetilde X \sim p_\sigma(\widetilde x)} \s{\norm{\nabla \log p_\sigma(\widetilde X) - s_\theta(\widetilde X)}_2^2}$.

We can show they are equivalent. Expand the square in $J_\theta$ gives:
$$
\begin{aligned}
2J_\theta & = E\s{(\nabla \log p_\sigma(\widetilde X) - s_\theta(\widetilde X))^T (\nabla \log p_\sigma(\widetilde X) - s_\theta(\widetilde X))}\\
& = E \norm{s_\theta(\widetilde X)}^2_2 - 2 E [(\nabla \log p_\sigma(\widetilde X))^T s_\theta(\widetilde X)] + E\norm{\nabla \log p_\sigma(\widetilde X)}^2_2
\end{aligned}
$$
Consider the second term $S_\theta = E [(\nabla \log p_\sigma(\widetilde X))^T s_\theta(\widetilde X)]$:
$$
\begin{aligned}
S_\theta & = E \s{(\nabla \log p_\sigma(\widetilde X))^T (s_\theta(\widetilde X))}\\
& = \int_{\R^d} p_\sigma(\widetilde x) (\nabla \log p_\sigma(\widetilde x))^T s_\theta(\widetilde x) \dd \widetilde x = \int_{\R^d} (\nabla p_\sigma(\widetilde x))^T s_\theta(\widetilde x) \dd \widetilde x\\
& = \int_{\R^d} \left (\nabla_{\widetilde x} \int_{\R^d} p_\sigma(\widetilde x | x) p(x) dx \right)^T s_\theta(\widetilde x) \dd\widetilde x = \int_{\R^d} \left ( \int_{\R^d} p(x)\nabla _{\widetilde x} p_\sigma(\widetilde x | x)  \dd x \right)^T s_\theta(\widetilde x) \dd\widetilde x\\
& = \int_{\R^d} \left ( \int_{\R^d} p(x) p_\sigma(\widetilde x | x) \nabla _{\widetilde x} \log p_\sigma(\widetilde x | x)  \dd x \right)^T s_\theta(\widetilde x) \dd\widetilde x\\
& = E \left [\nabla_{\widetilde x} \log p_\sigma(\widetilde x | x) ^T s_\theta(\widetilde x)\right]
\end{aligned}
$$
So $J_\theta = E\left [ \frac{1}{2} \norm{s_\theta(X)}^2_2 - \nabla_{\widetilde x} \log p_\sigma(\widetilde X | X)^T s_\theta(\widetilde X)\right ] + C$.

Expand the square in $D_\theta$ gives:
$$
D_\theta = E_{p_\sigma(\widetilde x, x)} \left [ \frac{1}{2} \norm{s_\theta(x)}^2_2 - \nabla_{\widetilde x} \log p_\sigma(\widetilde x | x)^T s_\theta(\widetilde x)\right ] + C'
$$
