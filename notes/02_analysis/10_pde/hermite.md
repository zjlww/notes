##### Hermite polynomials

The Hermite polynomials are found in the power series expansion of $\exp\p{\lambda x - \lambda^2 t / 2}$.

- For $n \in \N$, define the $n$-th Hermite polynomial $h_n: \R \times \R \to \R$ as
  $$
  h_n(x, t):=\frac{(-t)^n}{n !} e^{x^2 / 2 t} \frac{\part^n}{\part x^n}\p{e^{-x^2 / 2 t}} \implies \left\{\begin{array}{l}
  h_0(x, t)=1\\h_1(x, t)=x \\
  h_2(x, t)={x^2}/{2}-{t}/{2}\\
  h_3(x, t)={x^3}/{6}-{t x}/{2} \\
  h_4(x, t)={x^4}/{24}-{t x^2}/{4}+{t^2}/{8}\\
  \cdots\cdots
  \end{array}\right.
  $$

- Since
  $$
  \left.\frac{\part^n}{\part \lambda^n}\exp\p{-\frac{(x-\lambda t)^2}{2 t}}\right|_{\lambda=0}=(-t)^n \frac{\part^n}{\part x^n}{\exp\p{-x^2 / 2 t}}
  $$

- We have
  $$
  \left.\frac{\part^n}{\part \lambda^n}\exp\p{\lambda x-\frac{\lambda^2 t}{2}}\right|_{\lambda=0} = (-t)^n \exp\p{x^2 / 2 t} \frac{\part^n}{\part x^n}{\exp\p{-x^2 / 2 t}} = n ! h_n(x, t)
  $$

- We have power series
  $$
  \exp\p{\lambda x - \lambda^2 t / 2} = \sum_{n = 0}^\infty \lambda^n h_n(x, t)
  $$

##### 