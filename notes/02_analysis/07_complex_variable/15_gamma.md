##### Gamma function

For $s > 0$, the Gamma function is defined by:
$$
\Gamma(s) := \int_0^\infty e^{-t}t^{s - 1} \dd t
$$

- First, we have $\Gamma(1) = 1 = 0!$

- $\Gamma(s + 1) = s \Gamma(s)$.
  $$
  \Gamma(s + 1) = \lim_{\epsilon \downarrow 0} \int_\epsilon^{1/\epsilon} e^{-t} t^s \dd t =  \left. -e^{-t}t^s \right|_{t=\epsilon}^{1/\epsilon} + s \int_{\epsilon}^{1 / \epsilon} e^{-t} t^{s-  1} \dd t = s\Gamma(s)
  $$

- Therefore $\Gamma(n + 1) = n!$ for $n \in \N$.