##### Sum of independent random variables

Suppose $(\Omega_i, \mathcal F_i, P_i)_{i \in \N}$ and $(\N,\P(\N), P_N)$ are probability spaces.

Suppose $X_i$ are real random variables on $\mathcal F_i$, for $i \in \N$. And $N$ has distribution $P_N$.

By theorem of infinite product. Consider the countable product probability space:
$$
(\Omega, \F, P) := (\N, \P(N), P_N) \times (\times_i \Omega_i, \otimes_i \F_i, \times_i P_i)
$$
Then $X_{N(\omega)}(\omega)$ is a real random variable on $\F$.

- Define $S_n(\omega) = X_1 + \cdots + X_n$ for $n \in \N$. $S_n$ is a random variable.
- Define $S_N(\omega) = S_{N(\omega)}(\omega)$ on $\mathbf \omega \in \Omega$. It is a random variable.
- $E[S_N] = E[E[S_N|N]] = \sum_{n \in \N} E[S_n | N = n] P_N(n)$.
  - Notice that $E[S_N | N = n] = E[S_n]$ requires $E|S_N| < \infty$ or $X_n \ge 0$.


##### Wald's identity

Continue above discussion, assuming $X_i$ are i.i.d. random variables.

- $E[S_N|N=n] = E[S_n] = nE[X]$.

- $E[S_N] = E[E[S_N|N]] = E[NE[X]] = E[N]E[X]$.

- $E[S_N^2] = E[N]\var[X] + E[N^2]E^2[X]$. Since
  $$
  \begin{aligned}
  E[S_N^2] &= E[E[S_N^2 | N]] = \sum_{n \in \N} E[S_n^2] P(N = n) \\
  & = \sum_{n \in \N} \p{nE[X^2] + n^2E^2[X] - n E^2[X]} P(N = n)\\
  & = E[N]\var[X] + E[N^2]E^2[X]
  \end{aligned}
  $$
  
- $\var[S_N] = E[S_N^2] - E^2[S_N] = E[N]\var[X] + E^2[X]\var[N]$.

Suppose $X_i$ are i.i.d. $\N$ valued random variables with the same generating function $X(z) =E[z^X]$.

And discrete index $N$ has generating function $N(z) = E[z^N]$.
$$
S_N(z) = E[z^{S_N}] = \sum_{n=0}^\infty P(N=n) E[z^{S_n}] = \sum_{n=0}^\infty P(N=n) E^n[z^{X}] = N(X(z))
$$

- $S_N'(z) = N'(X(z))X'(z)$ on $z \in [0, 1]$.
  - Suppose $N'(1)$ exists and $E[X] = X'(1)$ exists. Then $E[S_N] = S_N'(1)$ exists.
  - $E[S_N] = E[N]E[X]$.
