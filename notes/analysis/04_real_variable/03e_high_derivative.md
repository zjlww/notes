#### Higher Differentiation

> Directional derivative, and the total derivative are two ways of generalizing derivatives in 1D.

##### Multindex notation

> Source: Multi-index notation wikipedia [page](https://en.wikipedia.org/wiki/Multi-index_notation).

An $n$-dimensional multi-index is an $n$-tuple $\alpha=\left(\alpha_{1}, \alpha_{2}, \ldots, \alpha_{n}\right)\in \N^n$.

Now suppose $\alpha, \beta \in \N^n$, define:
- $|\alpha|=\alpha_{1}+\alpha_{2}+\cdots+\alpha_{n}$.
- $D^{\alpha}=D_{1}^{\alpha_{1}} D_{2}^{\alpha_{2}} \ldots D_{n}^{\alpha_{n}}$.
- $\alpha \pm \beta = (\alpha_{1} \pm \beta_{1}, \alpha_{2} \pm \beta_{2}, \ldots, \alpha_{n} \pm \beta_{n})$.
- $\alpha !=\alpha_{1} ! \cdot \alpha_{2} ! \cdots \alpha_{n} !$.
- $\left(\begin{array}{c}\alpha \\ \beta \end{array}\right)=\left(\begin{array}{c}\alpha_{1} \\ \beta_{1} \end{array}\right)\left(\begin{array}{c} \alpha_{2} \\ \beta_{2} \end{array}\right) \cdots\left(\begin{array}{c} \alpha_{n} \\ \beta_{n} \end{array}\right)=\frac{\alpha !}{\beta !(\alpha - \beta) !}$.
- $\left(\begin{array}{l} k \\ \alpha \end{array}\right)=\frac{k !}{\alpha_{1} ! \alpha_{2} ! \cdots \alpha_{n} !}=\frac{k !}{\alpha !}$ where $k = |\alpha|$.

##### Directional derivatives and partial derivatives

Suppose $f: S \subseteq \R^n \to \R^m$, for $c \in S^\circ$, and $u \in \R^n$ define
$$
f_k'(c; u) = \lim_{h \to 0} \frac{f_k(c + hu) - f_k(c)}{h};\quad f'(c; u) = \lim_{h \to 0} \frac{f(c + hu) - f(c)}{h}
$$
as the **directional derivative** of $f$ at $c$ in the direction $u$.

- Notice that $f'(c; u) := \s{f'_1(c; u); \cdots; f'_m(c; u)} \in \R^{m}$.

$f'(c; u_k) \in \R^m$ is called a **partial derivative** denoted by $D_kf(c)$ when $u_k$ is the $k$th coordinate unit.
- Higher order partial derivatives are denoted as $D_{i,j} f(c) = D_i D_j f(c)$.
- Existence of all partial derivatives at $c$ does not even imply continuity!

Some important directional derivatives:

- Suppose $f(x) = x \cdot x: \R^d \to \R$, then $f'(c; u) = 2 c \cdot u$.
- Suppose $f(x) = Ax + b$, then $f'(c; u) = Au$.

##### Total derivatives

Suppose $f: S \subseteq \R^n \to \R^m$, and $c \in S^\circ$ in $S$.

Suppose for linear map $T_c:\R^n \to \R^m$ the following is true:
$$
\exist r > 0,\forall v \in B(r):f(c + v) = f(c) + T_cv + o(\|v\|)
\label{equ:differentiable}
$$

- $o(\|v\|)$ stands for a $E_c(v): B(0, r) \to \R^m$ where $\lim_{v \to 0} E_c(v) / \|v\| = 0$.
- $f$ is called **(totally) differentiable** at $c$. $f$ must be continuous at $c$.
- Equation $\ref{equ:differentiable}$ is called the **first-order Taylor formula** for $f$ about $c$.
- $T_c$ is the **(total) derivative** of $f$ at $c$, also denoted as $f'(c)$ or $Df(c)$.
- $f: S \to \R^m$ is differentiable at $c$ if and only if all $f_k: S \to \R$ are differentiable at $c$.

Some important total derivatives:

- Suppose $f(x) = x \cdot x: \R^d \to \R$, then $f'(x) = 2x \in \R^{d \times 1}$.
- Suppose $f(x) = Ax + b: \R^n \to \R^m$, then $f'(x) = A \in \R^{n \times m}$.

##### Totally differentiable implies directional differentiable

Suppose $f: S \subseteq \R^n \to \R^m$, and $c \in S^\circ$ in $S$.

Suppose $f$ is totally differentiable at $c$. Then all directional derivatives exists and $\forall u \in \R^m: f'(c; u) = T_c(u)$.

##### Differentiability notations in higher dimensions

Suppose $f: S \subseteq \R^n \to \R^m$. Suppose $A \subseteq S$.

- $f \in C^k[A]$ if all **partial derivatives** of $f|_A$ are finite and exists on $A^\circ$. And all partial derivatives are continuous.
- $f \in C[A]$ if $f|_A$ is continuous.
- $f \in D[A]$, if all partial derivatives of $f|A$ exists on $A^\circ$.
- $f \in D^*[A \to \R^m]$, if $f|_A$ is **totally differentiable** on $A^\circ$.

##### Gradient

Suppose $f: S \subseteq \R^n \to \R$ and $c \in S^\circ$. If all partial derivatives exists at $c$, denote
$$
\nabla f(c) := (D_1 f(c), \cdots, D_nf(c)) \in \R^n
$$

- $\nabla f(c)$ is the **gradient vector** of $f$ at $c$.
- When $f$ is differentiable at $c$. $\nabla f(c) = Df(c)$. And $f(c + u) = f(c) + \nabla f(c) \cdot u + o(\|u\|)$.
- $\nabla f(c)$ points towards the direction of **fastest increase** of $f$.

##### Jacobian matrix

Suppose $f: S \subseteq \R^n \to \R^m$ and $c \in S^\circ$.

The **Jacobian matrix** of $f$ at $c$ is defined when all partial derivatives exists.
$$
J_f(c) = \left[
\begin{array}{lll}
D_1 f(c) & \cdots  & D_n f(c)
\end{array}
\right]=\left[\begin{array}{c}
\nabla^{\mathrm{T}} f_{1}(c) \\
\vdots \\
\nabla^{\mathrm{T}} f_{m}(c)
\end{array}\right]
=
\left[\begin{array}{ccc}
D_1 f_1(c) & \cdots & D_n f_1(c) \\
\vdots & \ddots & \vdots \\
D_1 f_m(c) & \cdots & D_n f_m(c)
\end{array}\right]
$$

- We are using notation convension $\nabla^T f_k(c) = \nabla f_k(c)^T$.
- When $f$ is differentiable at $c$, $J_f(c)$ is the matrix of $T_c = Df(c) = f'(c)$.
- The **Jacobian determinant** $|J_f|(c)$ is defined as $|J_f(c)|$.

##### Sufficient condition of total differentiability

Suppose $f: S \subseteq \R^n \to \R$.

- Suppose $c \in S^\circ$. One of $D_kf$ exists at $c$ and the other $D_jf$ exists in some $B(c)$ and are continuous at $c$. Then $f$ is differentiable at $c$. ==TODO==.
- Suppose $f \in C^1[A]$ for $A \subseteq S$, then $f \in D^*[A]$.
  - This immediately follows from above theorem.

##### Chain rule of total differentiation

Suppose $g: S\subseteq \R^n\to \R^m$, and $f: T \subseteq \R^m \to \R^p$.
- Suppose $g$ is differentiable at $a \in S^\circ$. And $f$ is differentiable at $g(a) \in T^\circ$.
- Then $h = f \circ g$ is differentiable at $a$. 
- The total derivative is $h'(a) = f'(g(a))g'(a)$.

#### Higher Mean Value Theorem

##### High dimensional MVT

Suppose $f: S \subseteq \R^n \to \R^m$ where $S$ is open region in $\R^n$ and $f \in D[S]$.
- For $x, y \in S$, let path $h(t) = ty + (1 - t)x$ where $t\in[0, 1]$.
- For $a \in \R^m$ let $g(x) = a^Tf(h(t))$.
- Clearly $g \in D[0, 1]$. And $g'(t) = a^Tf'(h(t)) h'(t) = a^Tf'(h(t))(y-x)$.
- Apply MVT on $g(t)$, $\exists z \in h(0, 1): a^T f'(z) (y-x) = a^T (f(y) - f(x))$.
- When $m=1$, $\exists z \in h(0, 1): \nabla^T f(z)(y-x) = f(y)-f(x)$.

We have the following properties:

- If $f' = 0$ on $S$, $f$ is constant on $S$.

#### Exchanging Partial Derivatives

##### Commutativity of partial derivatives

Suppose $f: S \subseteq \R^n \to \R$ and $c \in S^\circ$.

- Suppose $D_r f$ and $D_k f$ exists in $B(c) \subseteq  S$, and both are **differentiable** at $c$. Then $D_{r, k} f(c) = D_{k ,r} f(c)$. ==TODO==.
- Suppose $D_r f$ and $D_k f$ exists in $B(c)$ and both $D_{r, k} f(c), D_{k ,r} f(c)$ are continuous at $c$. Then $D_{r, k} f(c) = D_{k ,r} f(c)$. ==TODO==.
- Suppose $D_r f$, $D_k f$ and $D_{k, r} f$ are continuous in $B(c)$, then $D_{r, k} f(c)$ exists and $D_{r, k} f(c) = D_{k ,r} f(c)$. ==TODO==.

