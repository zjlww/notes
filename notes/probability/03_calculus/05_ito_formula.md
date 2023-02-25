In the following we will always assume $(\Omega, \F, (\F_t), [0, T], P)$.

##### Ito formula I

 ==TODO==

Suppose $(B_t)$ is a standard BM and $(B_t) \in \M_c(T)$, $f \in C^2[\R]$. Then
$$
(**) \quad \forall t \in [0, T]: f(B_t) - f(B_0) = \int_0^t f'(B_s) dB_s + \frac{1}{2} \int_0^t f''(B_s) ds
$$
is true with probability one. Equivalently in differential form $df(B_t) = f'(B_t) dB_t + f''(B_t)/2dt$.

Suppose $(f'(B_t)) \in \V_c(T)$. Then $(f(B_t) - \int_0^t f''(B_t) dt) \in \M_c(T)$.

- $\frac{1}{2}\int_0^t f''(B_s) ds$ is called the **compensator** to $f(B_t)$ in this case.
  - The paths are continuous.
  - The paths has derivative $f''(B_t)$, which is continuous on $[0, T]$.
  - The paths are of bounded variation (bounded derivative).

Unfortunately, we can only give a ***partial proof*** for now.

Assuming $f, f', f''$ are all **bounded**. And $f(x)$ is **smooth enough** s.t. exists $\E: \R^2 \to \R$,
$$
(*)\quad f(x + dx) = f(x) + f'(x)dx + \frac{1}{2} f''(x)dx^2 + \E (x, dx); \quad \E(x, dx) = o(dx)^2
$$

- Consider a **sequence** of **shrinking partition** $P^{(k)} \in P[0, t]$, for a **fixed** $0 < t \le T$.
- Consider a single partition $(t_j)_{j = 0}^n  \in P[0, t]$ in the sequence for now.
- For convenience, use the following notations (also in the rest discussions).
  - $B_j:= B_{t_j}$. $\Delta B_j = B_{j + 1} - B_j$ for $0 \le j < n$.
  - $\Delta t_j = t_{j + 1} - t_j$ for $0 \le j < n$.
- $f(B_{t})-f(B_0) = \sum_{j = 0}^{n - 1} f(B_{j + 1}) - f(B_{j}) = \cdots$, apply $*$ and expand: $$
  \cdots =\sum_{j=0}^{n-1} f'(B_{j})\Delta B_j+\sum_{j=0}^{n-1} \frac{1}{2} f^{\prime \prime}(B_{t_{j}})\Delta B_j^{2}+\sum_{j=0}^{n - 1} \mathcal{E}(B_{j}, B_{j + 1})$$
- The $f'(x) dx$ term, $\sum_{j=0}^{n-1} f'(B_{j})\Delta B_j \to \int_0^t f'(B_s)dB_s$ in $\L_2$.
- The $\frac{1}{2}f''(x) dx$ term, $\sum_{j = 0}^{n - 1} f''(B_j) \Delta B_j^2 \to \int_0^t f''(B_s) ds$ in $\L_2$.
  - $\sum_{j=0}^{n-1}f''(B_j) \Delta t \to \int_0^t f''(B_s) ds$ **pointwise** since $f''(B_t)$ is **continuous**.
    - Since $f''$ is **bounded**, it converge in $\L_2$ norm by (**DCT**).
  - Define $X_j := \Delta B_j ^2 - \Delta t_j$.
  - Define $L_n := E[\sum_{j = 0}^{n - 1} f''(B_j)X_j]^2$.
  - $L_n = \sum_{j, k = 0}^{n - 1} E[f''(B_j)f''(B_k)X_j X_k] = \sum_{j = 0}^{n - 1} E[f''(B_j)^2 X_j^2]$.
  - Similar to (**Ito isometry**) $L_n = 2\sum_j E[f''(B_{t_j})]^2 (t_{j + 1} - t_j)^2$.
  - Since $f''$ is **bounded**, $L_n \to 0$.
  - This gives the rule $dB_t^2 = dt$.

- Error term $\sum_{j = 0}^{n - 1} \mathcal E(B_{j}, B_{j + 1}) \to 0$ in **probability**. ==TODO==
- For some subsequence of $(P^{(k)})$ all convergences are essentially pointwise.
- Notice that the left and right sides of $(**)$ are **continuous**, now consider $[0, T] \cap \Q$.

##### Ito formula II

 ==TODO==

Suppose $(B_t)_{t \ge 0}$ is a standard BM and $(B_t) \in \M_c(T)$. Suppose $f \in C^{2}([0, T] \times \R)$. Then
$$
\forall t \in [0, T]: f(t, B_{t})-f(0, B_{0})=\int_{0}^{t} \partial_{1} f(s, B_{s}) {d} B_{s}+\int_{0}^{t}\{\partial_{0} f(s, B_{s})+\frac{1}{2} \partial_{1}^{2} f(s, B_{s})\} {d} s
$$
is true with probability one. Short handed in differential form:
$$
d f(t, B_t) = \part_0 f(t, B_t)dt + \part_1 f(t, B_t) dB_t + \frac{1}{2}\part_1^2 f(t, B_t) dt
$$
Consider partial differential operator $L = \part_0 + \part_1^2/2$. Suppose $\part_1f(t, B_t) \in \V_c(T)$, then $f(t, B_t) - \int_0^t L f(s, B_s) ds \in \M_c(T)$.

Assuming all $\part_0 f, \part_1 f, \part_0^2 f, \part_0\part_1 f, \part_1^2 f$ are **bounded**. And $f(t, x)$ is **smooth enough** such that:
$$
\begin{aligned}
f(t + dt, x + dx) &- f(t, x) =  \part_0 f(t, x) dt + \part_1 f(t, x) dx \\
& + \frac{1}{2}\part_0^2 f(t, x) dt^2 + \frac{1}{2} \part_1^2 f(t, x) dx^2 + \part_0\part_1f(t, x) dx dt + \E(x, dx, t, dt)
\end{aligned}
$$
where $\E(x, dx, t, dy) = o(dx^2 + dy^2)$. We have following new terms compared to (**Ito formula I**)

- The $\part_0^2 f(t, x)dt^2/2$ term, $\sum_j \part_0^2 f(t_j, B_j) \Delta t_j^2 / 2 \to 0$ **pointwise**.
  - This gives the rule $dt^2 = 0$.
- The $\part_0 \part_1 f(t, x) dtdx$ term, $\sum_{j = 0}^{n - 1} \part_0 \part_1 f(t_j, B_j) \Delta t_j \Delta B_j \to 0$ **pointwise**.
  - Since $\part_0 \part_1 f(t, B_t)$ is bounded, $t$ is of bounded variation and $B_t$ is continuous.
  - This gives the rule $dt dB_t = 0$.

##### Harmonic function

Suppose $O \subseteq \R^d$ is an open set. $f \in C^2(O \to \R)$ is **harmonic** in $O$ if and only if $\forall x \in O: \Delta f(x) = 0$.

- For $d = 1$, the only harmonic functions are linear, $f(x) = ax+ b$.

##### Covariation of independent BM

Suppose $(X_t)$ and $(Y_t)$ are independent standard BM. Then $[X, Y]_t = 0$ in $\L_2$.

Consider any sequence of shrinking partitions with one step as $(t_i)_{i = 0}^n \in P[0, t]$.
$$
E\left[ \sum_{i = 0}^{n - 1} \Delta X_i \Delta Y_i \right]^2 = \sum_{i = 0}^{n - 1} E \Delta X_i^2 E\Delta Y_i^2 = \sum_{i = 0}^{n - 1} \Delta t_i^2 \to 0
$$
##### Ito formula III

 ==TODO==

Suppose $(B_t)_{t \ge 0}$ is a $\R^d$-standard BM adapted to $(\F_t)$. Suppose $f \in C^{2}(\R^d)$. Then
$$
\begin{aligned}
f(B_t) - f(B_0) & = \sum_{i=1}^{d} \int_{0}^{t} \partial_{i} f(B_{s}) {d} B_{s}^{(i)}+\frac{1}{2} \int_{0}^{t} \sum_{i=1}^{d} \partial_{i}^{2} f(B_{s}) {d} s \\& = \int_0^t \nabla f(B_s)^T dB_s + \frac{1}{2} \int_0^t \Delta f(B_s) ds
\end{aligned}
$$
is true with probability one. Equivalently in differential form:
$$
df(B_t) = \nabla f(B_t)^T dB_t + \frac{1}{2} dB_t^T\nabla^2 f(B_t) dB_t = \nabla f(B_t)^T dB_t + \frac{1}{2} \Delta f(B_t) dt
$$

- Suppose $\part_i f(B_t) \in \V_c(T)$ for all $1 \le i \le d$, then $f(B_t) - \int_0^t \Delta f(B_s) ds / 2 \in \M_c(T)$.

We have the following new terms compared to (**Ito formula I**):

- The $\part_i \part_j f(x) dx_i dx_j$ term when $i \neq j$. $\sum_{k = 0}^{n - 1} \part_{ij}f(B_k)\Delta B_k^{(i)} \Delta B_k^{(j)} \to 0$ in $\L_2$.
  - Expand $E[\sum_k \part_{ij} f(B_k) \Delta B_k^{(i)} \Delta B_k^{(j)}]^2$ and the result is immediate.
  - This justifies the rule $dB_t^{(i)} dB_t^{(j)} = 0$ when $i \neq j$.

##### Ito formula IV

 ==TODO==

Suppose $(B_t)$ is a $\R^d$-standard BM adapted to $(\F_t)$. Suppose $f \in C^2([0, T] \times \R^d)$.
$$
f(B_t) - f(B_0) = \int_0^t \nabla f(s, B_s)^T dB_s + \int_0^t (\part_0 f(s, B_s)+\frac{1}{2} \Delta f(s, B_s)) ds
$$
where $\nabla = (\part_{x_1}, \ldots, \part_{x_d})^T$. $\Delta = (\part_{x_1}^2 + \ldots + \part^2_{x_d})$. And $\part_0 = \part/\part t$. Above is true with probability one. In differential form:
$$
df(t, B_t) = \nabla f(t, B_t)^T dB_t + \left(\frac{1}{2} \Delta f(t, B_t) + \part_0 f(t, B_t)\right) dt
$$
##### Ito formula V

 ==TODO==

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered probability space. $(B_t)$ is a standard BM and $(B_t) \in \M_c(T)$. $dX_t = V_t dB_t + U_t dt$ is an Ito process on the space.

Suppose $g(t, x) \in C^{1, 2}([0, T] \times \R)$. Then the following is true with probability one.
$$
\begin{aligned}
d g(t, X_{t}) & = \part_0 g(t, X_t) dt + \part_1 g(t, X_t) dX_t + \frac{1}{2}\part_1^2 g(t, X_t) (dX_t)^2
\\
& = \part_{0} g(t, X_{t})dt+ \left (\part_{1} g(t, X_{t}) V_{t} d B_{t}+ \part_{1} g(t, X_{t}) U_t dt \right)+\frac{1}{2} \partial_{1}^{2} g(t, X_{t}) V_t^2dt 
\end{aligned}
$$

##### Ito formula VI

 ==TODO==

Suppose $(\Omega, \F, (\F_t), [0, T], P)$ is a filtered probability space. $(B_t)$ is a standard BM and $(B_t) \in \M_c(T)$. $dX_t = V_t dB_t + D_t dt$ and $dY_t = U_t dB_t + R_t dt$. Let $f(x, y) \in C^{2, 2}(\R^2)$.
$$
\begin{aligned}
df(X_t, Y_t) & = \part_x f(X_t, Y_t) dX_t + \part_y f(X_t, Y_t) dY_t + \frac{1}{2} \part_x^2 f(X_t, Y_t) dX_t^2 + \frac{1}{2} \part_y^2 f(X_t, Y_t) dY_t^2\\
 & + \part_x \part_y f(X_t, Y_t) dX_t dY_t
\end{aligned}
$$
The differential form is further reduced using rules:

- $dX_t^2 = V_t^2 dt$ and $dY_t^2 = U_t^2 dt$.
- $dX_t dY_t = (V_t dB_t + D_t dt) (U_t dB_t + R_t dt) = V_t U_t dt = d[X, Y]_t$.

##### Integral by part

Continue above discussion. Taking $f(x, y) = xy$ gives the **integral by part** formula:

- $d(X_t Y_t) = Y_t dX_t + X_t dY_t + dX_t dY_t = Y_t dX_t + X_t dY_t + d[X, Y]_t$.

- Suppose $f: [0, T] \to \R$ is continuous and of bounded variation.

  - Treat $f \in \V_c(T)$ and so $d(f(t) B_t) = f(t) dB_t + B_t df(t)$. Writting in the full form gives:
    $$
    \int_0^t f(s) dB_s = f(t) B_t - \int_0^t B_s df(s)
    $$

##### Ito formula VII

 ==TODO==

Continue above discussion. Suppose $d \mathbf X_t = \mathbf V_t d \mathbf B_t + \mathbf U_t dt$.

Suppose $f \in C^{1, 2}([0, T] \times \R^d \to \R)$. Then
$$
d f(t, \mathbf X_t) = \part_0 f(t, \mathbf X_t)dt + \nabla f(t, \mathbf X_t) d \mathbf X_t + \frac{1}{2} d\mathbf X_t^T\nabla^2 f(t, \mathbf X_t) d\mathbf X_t
$$

- $\nabla f(t, \mathbf X_t)d\mathbf X_t = \sum_i\part_i f(t, \mathbf X_t) d X_t^{(i)}$.
- $d\mathbf X_t^T \nabla^2 f(t, \mathbf X_t) d\mathbf X_t = \sum_{i, j}dX_t^{(i)} \part_{ij} f(t, \mathbf X_t) dX_t^{(j)}$.
- $dX_t^{(i)} = V_t^{(i)} dB_t + U_t^{(i)} dt$ and $dX_t^{(i)} dX_t^{(j)} = V_t^{(i)}V_t^{(j)} dt$.

