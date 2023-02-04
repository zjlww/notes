
(**Series of linear and exponential sequence**)

Suppose we want to find the sum $S = \sum_{n = 1}^\infty (kn+b) p^n$.
- In general, this kind of sums can be found in the following way.
- $S = \sum_{n = 0}^\infty (kn + b + k) p^n p = p\sum_{n= 0}^\infty (kn + b) p^n + p \sum_{n = 0}^\infty k p^n$.
- Now $Q = \sum_{k = 0}^\infty kp^n$ is easy to find. $S = p(S + b) + pkQ$.
- Now solve for $S$ in the above equation and we have:
- $S = \frac{p(b + k(1/(1-p)))}{1 - p} = \frac{p(qb + k)}{q^2}$ where $q = 1 - p$.
