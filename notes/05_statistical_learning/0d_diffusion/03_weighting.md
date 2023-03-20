##### Score matching weighting ==TODO==

Forward VPSDE: $dX_t = -\frac{1}{2} \beta(t)X_t dt + \sqrt{\beta(t)} dB_t$ on $t \in [0, 1]$. We have transition kernel:
$$
\bar \alpha(t) := \exp({- \int_0^t \beta(s) \dd s}); \quad p_{0t}(x_t | x_0) = \mathcal N(x_t \mid x_0 \sqrt{\bar \alpha(t)}, \p{1 - \bar \alpha(t)} I) = \mathcal N(x_t \mid \mu_t, \Sigma_t)
$$
Completely analogous to DDPM, $X_t = \sqrt{1-\bar \alpha(t)} E_t + \sqrt{\bar \alpha(t)} x_0$.

DDPM proposes to define neural network $e_\theta(x_t, t)$ and train it with:
$$
L_\theta:= E_{t, x_0, e_t}\norm{e_t - e_\theta(x_t, t)}^2_2
$$
Song proposes to define neural network $s_\theta(x_t, t)$ to directly predict **score** and train it with:
$$
L_\theta:= E_{t, x_0, e_t}(1 - \bar \alpha(t))\n{s_\theta(x_t, t) - \nabla_{x_t} \log p_{0t}(x_t | x_0)}^2_2 = E_{t, x_0, e_t}(1 - \bar \alpha(t))\norm{s_\theta(x_t, t) + \frac{e_t}{\sqrt{1 - \bar \alpha(t)}}}^2_2
$$
The two loss are equivalent up to neural network parameterization:
$$
s_\theta(x_t, t) = - \frac{e_\theta(x_t, t)}{\sqrt{1 - \bar \alpha(t)}} \approx \nabla_{x_t} \log p_t(x_t)
$$
According to Tweedie's formula, 
$$
E[x_0 \mid x_t] = \frac{1}{\sqrt{\bar \alpha(t)}}\p{x_t + (1 - \bar \alpha(t))\nabla_{x_t} \log p_{t}(x_t)}
$$
DALL.E.2 proposes to define neural network $f_\theta(x_t, t)$ to predict the "mean" and train it with:
$$
L_\theta := E_{t, x_0, e_t} \n{f_\theta(x_t, t) - x_0}_2^2 = E_{t, x_0, e_t} \norm{f_\theta(x_t, t) - \frac{x_t - \sqrt{1 - \bar \alpha(t)} e_t}{\sqrt{\bar \alpha(t)}}}_2^2 = \frac{1 - \bar \alpha(t)}{ \bar \alpha(t)} E\norm{\frac{f_\theta(x_t, t) \sqrt{\bar \alpha(t)} - x_t}{\sqrt{1 - \bar \alpha(t)}} + e_t}_2^2
$$
The loss is equivalent to DDPM loss up to neural network parameterization, and an extra reweighing:
$$
-f_\theta(x_t, t)\sqrt{\bar \alpha(t)} + x_t = e_\theta(x_t, t) \sqrt{1 - \bar \alpha(t)} = - \p{1 - \bar \alpha(t)} s_\theta(x_t, t)
$$
