$$
\newcommand{D}{{\mathcal D}}
\newcommand{H}{{\mathcal H}}
\newcommand{G}{{\mathcal G}}
\newcommand{loc}{{\operatorname{loc}}}
\newcommand{M}{\mathcal M}
\newcommand{P}{\mathcal P}
\newcommand{B}{\mathbb B}
\newcommand{E}{\mathcal E}
\newcommand{F}{\mathcal F}
\newcommand{J}{\mathcal J}
\newcommand{A}{\mathcal A}
\newcommand{L}{\mathcal L}
\newcommand{S}{\mathcal S}
\newcommand{su}{\operatorname{supp}}
\newcommand{re}{\operatorname{Re}}
\newcommand{im}{\operatorname{Im}}
\newcommand{fp}{\operatorname{Fp}}
\newcommand{pf}{\operatorname{Pf}}
\newcommand{pv}{\operatorname{Pv}}
\newcommand{pd}[2]{\left \langle #1, #2 \right\rangle}
\newcommand{dp}{\mathbf{D}}
\newcommand{ip}{\mathbf{I}}
\newcommand{cas}{\D'_+}
$$

### Convolution Equations

-----

A subset $\A'$​ of $\D'$​ (vector space over $F$) is a **convolution algebra** if

- $\A'$​ is a vector space over $F$​.
- Convolution always exists, and is associative.
- $\A'$ is closed under convolution.

More over, $\A'$ is **commutative**, since the convolution is commutative.

Suppose $\A'$ has $\delta$ in it, it has a **unit element**. The unit is unique if it exists.

Suppose $f \in \A'$ and $g \star f = \delta$ for some $g \in \A'$. $f$ is **invertible**, and $g$ the **inverse is unique**, denoted by $f^{-1}$.

Suppose $f, g \in \A'$ and are invertible, then $(f \star g)^{-1} = g^{-1} \star f^{-1}$.

Common convolutional algebras that are ***integral domains* and $\C$-algebra**.

- Define $\D'_+$ as the set of all **causal** distributions in $\D'$.
- Similarly $\D_-'$ is the set of **anti-causal** distributions in $\D'$.
- Define $\E'$, the set of all compactly supported distributions.
  - $\E'$ is a subalgebra of $\D'_+$ and $\D'_-$.

---

Suppose $f, g \in \D'$. Consider the equation $f \star u = g$. And the solutions in $\D'$.

- $f \star u = 0$ is called the **homogeneous equation**.
- Solutions to the $f \star u = 0$ are **general solutions**.
- Solutions to $f \star u = \delta$ are the **elementary solutions**.
- Solutions to $f \star u = g$ are the **particular solutions**.

----

Suppose $f \in \cas$ and $g \in \cas$. Consider the **equation** $f \star u = g$.

- Suppose $f \star u  = g$ always has a solution in $\cas$ for all $g \in \cas$. Then $f$ is invertible.
- Suppose $f$ is invertible then $u = f^{-1} \star g$ is the unique solution.

----

Suppose $\mathbf f \in (\cas)^{n \times m}$. $\mathbf g \in(\cas)^n$. $\mathbf f \star \mathbf u = \mathbf g$. 

---

Consider the equation in $\D'$, $(\delta' - \delta) \star x = \delta$.

$x = u(t)e^t \in \cas$​ is one solution, $x = -u(-t)e^t$​ is another solution in $\acas$.

----

### Systems of Convolutional Equations

Suppose $f_{ij}, g_i \in \cas$​​ and unknowns $u_j \in \cas$​​. Consider the **simultaneous equations**:
$$
\begin{aligned}
&f_{11} \star u_{1}+f_{12} \star u_{2}+\cdots+f_{1 n} \star u_{n}&=g_{1}\\
&f_{21} \star u_{1}+f_{22} \star u_{2}+\cdots+f_{2 n} \star u_{n}&=g_{2}\\
& \cdots \cdots & =\cdots\\
&f_{n 1} \star u_{1}+f_{n 2} \star u_{2}+\cdots+f_{n n} \star u_{n}&=g_{n}
\end{aligned}
$$

----

In matrix form, denote $\mathbf f \in (\cas)^{n \times m}$. $\mathbf g \in(\cas)^n$. Treat **convolution as product**!

Define **matrix product** and **scalar matrix product** as usual.

- Matrix product is **associative**.

----

Suppose $\mathbf f \in (\cas)^{n \times n}$.

Define **identity matrix** $\mathbf I \in (\cas)^{n \times n}$, with delta on diagonal and zero otherwise.

Define **determinant** $\det \mathbf f$ as usual. Usual rules for determinants applies.

Define **inverse matrix** of $\mathbf f$ as any matrix $\mathbf g \in (\cas)^{n \times n}$, such that $\mathbf f \mathbf g = \mathbf I$. 

- If $\mathbf f$ has an **inverse**, it must be **unique**, and $\mathbf f \mathbf f^{-1} = \mathbf f^{-1}\mathbf f$.
- Any right inverse is also a left inverse.

Define cofactor $c_{ij} \in (\D')^{n \times n}$ as
$$
c_{ij} = (-1)^{i + j} \det \mathbf f_{ij}
$$
Define adjoint matrix of $\mathbf f$ as $\mathbf c^T$.

----

Suppose $\mathbf f \in (\cas)^{n \times n}$.

Suppose $\mathbf f \mathbf u = \mathbf g$ has at least one solution $\mathbf u \in (\cas)^n$ for all $\mathbf g \in(\cas)^n$. $\mathbf f$ has an inverse $\mathbf h$.
$$
\mathbf{
fh = I \implies \det f \det h = \det I = \delta
}
$$
So $\det \mathbf f$ is invertible in $\cas$. Suppose $\mathbf a$ is the adjoint matrix of $\mathbf f$.

Define the following matrix, by standard linear algebra:
$$
\mathbf{q} := (\det \mathbf f) ^{-1} \mathbf a^T \implies \mathbf {fq = qf = I}
$$
So $\mathbf{u = qg}$ gives a solution to $\mathbf{fu = g}$.

----

Suppose $\mathbf f \in (\cas)^{n \times n}$. And $\mathbf f$ is invertible. Then $\mathbf f \mathbf u = \mathbf g$ always has a solution. And the solution is unique.
