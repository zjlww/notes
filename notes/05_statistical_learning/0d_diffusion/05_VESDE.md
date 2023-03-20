(**SMLD in SDE framework**)

Continue (**Simple Diffusion**).

- Continuous time limit of the forward diffusion:
  - Recall the formulation of SMLD:
    - We choose a strictly increasing $(\sigma_n)_{n = 1}^N \in (0, \infty)$.
    - And the perturbation kernels are $p(x_n | x_0) = \mathcal N(x_n \mid x_0, \sigma_n^2 I)$.
- Consider SDE $X_t = X_0 + \int_0^t \sqrt{{d[\sigma^2(t)]}/{dt}} dB_t$ on $t \in [0, 1]$.
  - We do not need to solve the forward equation in this case.
  - The Wienner integral shows $p_{0t}(x_t|x_0) = \mathcal N(x_t \mid x_0, \sigma^2(t) I)$.

