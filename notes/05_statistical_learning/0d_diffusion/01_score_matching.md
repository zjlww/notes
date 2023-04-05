#### Score Matching

##### The score matching problem

Consider density $p({\symbf x}): \R^d \to [0, \infty)$ with score $\nabla \log p({\symbf x})$. Train a parameterized vector field $S_\theta({\symbf x})$ for $\theta \in \Theta$ such that $S_\theta({\symbf x}) \approx \nabla \log p({\symbf x})$. 

The **Fisher divergence** between $S_\theta({\symbf x})$ and $\nabla \log p({\symbf x})$ is $\frac{1}{2} E_{{\symbf X} \sim p({\symbf x})} \s{ \norm{\nabla \log p({\symbf X}) - S_\theta({\symbf X})}_2^2}$.

- Is it really good to optimize for the Fisher divergence? It does not optimize "the sampling result".
- Matching directly with fisher divergence is called **explicit score matching** (ESM).

##### Implicit score matching

> Hyvärinen, A. (2005). Estimation of Non-Normalized Statistical Models by Score Matching. *J. Mach. Learn. Res., 6*, 695-709.

**Implicit score matching** demonstrates that optimizing for $E_{{\symbf X} \sim p({\symbf x})} \left [\frac{1}{2} \norm{S_\theta({\symbf X})}^2_2 + \tr (\nabla S_\theta({\symbf X}))\right ]$ is equivalent to optimize for the Fisher divergence.
$$
\begin{aligned}
& \quad \,\,E_{{\symbf X} \sim p({\symbf x})} \norm{\nabla \log p({\symbf X}) - S_\theta({\symbf X})}^2_2 = E\s{(\nabla \log p({\symbf X}) - S_\theta({\symbf X}))^T (\nabla \log p({\symbf X}) - S_\theta({\symbf X}))}\\
& = E \norm{S_\theta({\symbf X})}^2_2 - 2 E [(\nabla \log p({\symbf X}))^T (S_\theta({\symbf X}))] + E \norm{\nabla \log p({\symbf X})}^2_2\\
& = E \norm{S_\theta({\symbf X})}^2_2 - 2\int_\R p({\symbf x}) \sum_{i = 1}^d \p{\part_i \log p({\symbf x}) \cdot S_\theta({\symbf x})_i} \dd {\symbf x} + \const\\
& = E \norm{S_\theta({\symbf X})}^2_2 - 2\sum_{i = 1}^d \int_\R \p{\part_i p({\symbf x}) \cdot S_\theta({\symbf x})_i} \dd {\symbf x} + \const\\
& = E \norm{S_\theta({\symbf X})}^2_2 + 2 \sum_{i = 1}^d \int_\R p({\symbf x}) \part_i S_\theta({\symbf x})_i \dd {\symbf x} + \const\\
& = E \norm{S_\theta({\symbf X})}^2_2 + 2E \s{\tr \nabla S_\theta({\symbf X})} + \const
\end{aligned}
$$

##### Denoising score matching

> Vincent, P. (2011). A Connection Between Score Matching and Denoising Autoencoders. *Neural Computation, 23*, 1661-1674.

Suppose some **Markov density kernel** $p_\sigma(\widetilde {\symbf x} | {\symbf x})$ is used to perturb the original density, called the **perturbation kernel**.

Denote the **perturbed density** $p_\sigma(\widetilde {\symbf x}, {\symbf x}) = p_\sigma(\widetilde {\symbf x} | {\symbf x}) p({\symbf x})$. And the **marginal density** $p_\sigma(\widetilde {\symbf x})$.

**Denoising score matching** demonstrates that minimizing for 
$$
D_\theta = \frac{1}{2} E_{\widetilde {\symbf X}, {\symbf X}  \sim p_\sigma(\widetilde {\symbf x}, {\symbf x})} \s{\norm{S_\theta(\widetilde {\symbf X}) - \nabla_{\widetilde {\symbf X}} \log p_\sigma(\widetilde {\symbf X} | {\symbf X})}^2_2}
$$
is equivalent to explicit score matching.

Recall **explicit score matching** $J_\theta = \frac{1}{2} E_{\widetilde {\symbf X} \sim p_\sigma(\widetilde {\symbf x})} \s{\norm{\nabla \log p_\sigma(\widetilde {\symbf X}) - S_\theta(\widetilde {\symbf X})}_2^2}$.

We can show they are equivalent. Expand the square in $J_\theta$ gives:
$$
\begin{aligned}
2J_\theta & = E\s{(\nabla \log p_\sigma(\widetilde {\symbf X}) - S_\theta(\widetilde {\symbf X}))^T (\nabla \log p_\sigma(\widetilde {\symbf X}) - S_\theta(\widetilde {\symbf X}))}\\
& = E \norm{S_\theta(\widetilde {\symbf X})}^2_2 - 2 E [(\nabla \log p_\sigma(\widetilde {\symbf X}))^T S_\theta(\widetilde {\symbf X})] + E\norm{\nabla \log p_\sigma(\widetilde {\symbf X})}^2_2
\end{aligned}
$$
Consider the second term $S_\theta = E [(\nabla \log p_\sigma(\widetilde {\symbf X}))^T S_\theta(\widetilde {\symbf X})]$:
$$
\begin{aligned}
S_\theta & = E \s{(\nabla \log p_\sigma(\widetilde {\symbf X}))^T (S_\theta(\widetilde {\symbf X}))}\\
& = \int_{\R^d} p_\sigma(\widetilde {\symbf x}) (\nabla \log p_\sigma(\widetilde {\symbf x}))^T S_\theta(\widetilde {\symbf x}) \dd \widetilde {\symbf x} = \int_{\R^d} (\nabla p_\sigma(\widetilde {\symbf x}))^T S_\theta(\widetilde {\symbf x}) \dd \widetilde {\symbf x}\\
& = \int_{\R^d} \left (\nabla_{\widetilde {\symbf x}} \int_{\R^d} p_\sigma(\widetilde {\symbf x} | {\symbf x}) p({\symbf x}) dx \right)^T S_\theta(\widetilde {\symbf x}) \dd\widetilde {\symbf x} = \int_{\R^d} \left ( \int_{\R^d} p({\symbf x})\nabla _{\widetilde {\symbf x}} p_\sigma(\widetilde {\symbf x} | {\symbf x})  \dd {\symbf x} \right)^T S_\theta(\widetilde {\symbf x}) \dd\widetilde {\symbf x}\\
& = \int_{\R^d} \left ( \int_{\R^d} p({\symbf x}) p_\sigma(\widetilde {\symbf x} | {\symbf x}) \nabla _{\widetilde {\symbf x}} \log p_\sigma(\widetilde {\symbf x} | {\symbf x})  \dd {\symbf x} \right)^T S_\theta(\widetilde {\symbf x}) \dd\widetilde {\symbf x}\\
& = E \left [\nabla_{\widetilde {\symbf x}} \log p_\sigma(\widetilde {\symbf X} | {\symbf X}) ^T S_\theta(\widetilde {\symbf X})\right]
\end{aligned}
$$
So $J_\theta = E\left [ \frac{1}{2} \norm{S_\theta({\symbf X})}^2_2 - \nabla_{\widetilde {\symbf x}} \log p_\sigma(\widetilde {\symbf X} | {\symbf X})^T S_\theta(\widetilde {\symbf X})\right ] + \const = D_\theta$.

Expand the square in $D_\theta$ gives the same expression.
$$
D_\theta = E_{p_\sigma(\widetilde {\symbf x}, {\symbf x})} \left [ \frac{1}{2} \norm{S_\theta({\symbf x})}^2_2 - \nabla_{\widetilde {\symbf x}} \log p_\sigma(\widetilde {\symbf x} | {\symbf x})^T S_\theta(\widetilde {\symbf x})\right ] + \const
$$
