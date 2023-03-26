#### Discrete Smooth Transforms

The design of the smooth transforms can be quite complex, requiring careful engineering to ensure they remain invertible and differentiable. In this section, we discuss some of the most important smooth transforms found in application.

##### Autoregressive flow

Autoregressive flow is one of the basic ways to construct a **smooth** function $f \in C^1(\R^d \to \R^d)$.

- Let $\p{h_i(x_{<i})}_{i = 1}^{d} \in D(\R^{i - 1} \to \R^m)$  be a sequence of differentiable functions.
- Let $\tau(x, h) \in C(\R \times \R^m \to \R)$ be a function smooth in $x$ and differentiable in $h$.

Then $f_i(x) = \tau(x_{i}, h_i(x_{<i}))$ for all $i \in \c{1, \ldots, n}$ gives a smooth function, called an autoregressive flow.

The Jacobian matrix of $f$ is a $\R^{d \times d}$ matrix:
$$
J_f(x)=\left[\begin{array}{cccc}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_d} \\
\frac{\partial x_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_d} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_d}{\partial x_1} & \frac{\partial f_d}{\partial x_2} & \cdots & \frac{\partial f_d}{\partial x_d}
\end{array}\right]
$$
For the diagonal elements, we have:
$$
\frac{\partial f_i}{\partial x_i}=\frac{\partial \tau\left(x_i, h_i\left(x_{<i}\right)\right)}{\partial x_i}
$$
For elements in the lower triangular matrix, we have:
$$
\frac{\partial f_i}{\partial x_j}=\frac{\partial \tau\left(x_i, h_i\left(x_{<i}\right)\right)}{\partial x_j}=\frac{\partial \tau\left(x_i, h_i\left(x_{<i}\right)\right)}{\partial h_i\left(x_{<i}\right)} \cdot \frac{\partial h_i\left(x_{<i}\right)}{\partial x_j}
$$
Putting it all together, the triangular Jacobian matrix of the autoregressive flow is:
$$
J_f(x)=\left[\begin{array}{cccc}
\frac{\partial \tau\p{x_1, h_1()}}{\partial x_1} & 0 & \cdots & 0 \\
\frac{\partial \tau\p{x_2, h_2\p{x_1}}}{\partial h_2\p{x_1}} \cdot \frac{\partial h_2\p{x_1}}{\partial x_1} & \frac{\partial \tau\p{x_2, h_2\p{x_1}}}{\partial x_2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial \tau\p{x_d h_d\p{x_{<d}}}}{\partial h_d\p{x_{<d}}} \cdot \frac{\partial h_d\p{x_{<d}}}{\partial x_1} & \frac{\partial \tau\p{x_d h_d\p{x_{<d}}}}{\partial h_d\p{x_{<d}}} \cdot \frac{\partial h_d\p{x_{<d}}}{\partial x_2} & \cdots & \frac{\partial \tau\p{x_d, h_d\p{x_{<d}}}}{\partial x_d}
\end{array}\right]
$$
And the log absolute determinant is given by:
$$
\log \left|\det J_f(x)\right|=\sum_{i=1}^d \log \left|\frac{\partial \tau\left(x_i, h_i\left(x_{<i}\right)\right)}{\partial x_i}\right|
$$
Now let's consider the efficiency of the Autoregressive flow:

- Computing $f(x)$ is efficient, since $(h_i)_{i = 1}^n$ can be computed in parallel.
- Computing $f^{-1}(y)$ is slow, and autoregressive.
  - In this case, we must sequentially compute $x_i$ from $y_i$ using the relation $x_i = \tau^{-1}(y_i, h_i(x_{<i}))$.
  - We start from $x_1 = \tau^{-1}(y_1, h_1())$ and proceed sequentially.

##### Glow

