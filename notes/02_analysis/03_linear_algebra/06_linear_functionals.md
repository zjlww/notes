#### Linear Functionals

##### Dual space

- Suppose $V$ is a vector space over $\symbf F$. A **linear functional** on $V$ is a linear map from $V$ to $\symbf{F}$.
  - $V' = \L(V, \symbf F)$ is the **algebraic dual space** of $V$, it is a vector space over $\symbf F$.
  - We default $V'$ to algebraic when $V$ has no special topology.
- Suppose $V$ is a **topological vector space (e.g. normed space)** over $\bF$.
  - $V' = \mathcal B(V, \bF)$ is the set of all **continuous linear functionals**, called the **continuous dual space** / **topological dual space**.
  - We default $V'$ to topological when $V$ is topological.

##### Norm and dual space

Suppose $V$ is a normed vector space over $\bF$.

- $V' = \mathcal B(V, \bF)$ is **always Banach since $\bF$ is Banach.**
- For $\varphi \in \L(v, \bF)$. $\varphi \in \mathcal B(V, \bF)$ if and only if $\null \varphi$ is closed.
  - $\to$ direction follows from above.
  - $\leftarrow$ direction: Suppose $\varphi$ is not bounded, $(f_k)_{k = 1}^\infty \in V$ and $\|f_k\| = 1$, $\|\varphi(f_k)\| \ge k$.
    - $f_1 / \varphi(f_1) - f_k / \varphi(f_k) \in \null \varphi$.
    - $f_1 / \varphi(f_1) - f_k / \varphi(f_k) \to f_1 / \varphi(f_1) \notin \null \varphi$.
- For $\varphi \in \L(V, \bF)$. $\null \varphi$ is **not dense** implies $\null \varphi$ is closed.
  - Suppose $\null \varphi$ is not closed. Let $v \in \overline {\null \varphi}  - \null \varphi$.
  - Now we can show any $u \in V$ is also in $\overline {\null \varphi}$.
  - Notice that $u - v \varphi(u) / \varphi(v) \in \null \varphi$.
  - And that $v \varphi(u) / \varphi(v) \in \overline{\null \varphi}$.
  - So $u = (u - v\varphi(u) / \varphi(v)) + v\varphi(u)/\varphi(v) \in \overline{\null \varphi}$.
  - So $V = \overline{\null \varphi}$.
- Suppose $V$ is finite-dimensional. $\L(V, \bF) = \mathcal B(V, \bF)$.
- Suppose $V$ is infinite-dimensional. $\L(V, \bF) \neq \mathcal B(V, \bF)$.
  - Suppose $E$ is a Hamel basis of $V$.
  - Take a countble subset of $E$. Let $F = \{e_k\}_{k = 1}^\infty \subseteq E$.
  - Define $\varphi(e_k/\norm{e_k}) = k$, and $\varphi(f) = 0$ where $f \in E \backslash F$.
  - This uniquely defines a linear functional.
  - Clearly $\varphi$ is not bounded / continuous.

#### Hahn-Banach Theorem

##### Real extension lemma

Let $V$ is a **semi-normed space** over $\R$ and $U$ is a subspace of $V$.

Let $\psi \in \mathcal B(U, \R)$. And $h \in V - U$. $\psi$ can be extended to $\varphi \in \mathcal B(U + \R h, \R)$ where $\norm{\varphi} = \norm{\psi}$.

- Define $\varphi(u + \alpha h) = \psi(u) + \alpha \varphi(h)$. Let $\varphi(h) = c \in \R$.
- Since $\varphi|_U = \psi$, clearly $\norm{\varphi} \ge \norm{\psi}$.
- Only need $\forall f\in U, \forall \alpha \in \R:|\psi(f) + \alpha c| \le \norm{\psi}\norm{f + \alpha h}$.
- Only need $\forall f \in U: |\psi(f) + c| \le \norm{\psi}\norm{f + h}$ by merge $\alpha$ into $f$.
- Only need $\forall f \in U: -\norm{\psi} \norm{f + h} - \psi(f) \le c \le \norm{\psi}\norm{f + h} -\psi(f)$.
- Enhance this to $\forall f, g \in U: -\norm{\psi} \norm{f + h} - \psi(f) \le c \le \norm{\psi}\norm{g + h} - \psi(g)$.
  $$
  \begin{aligned}
   -\norm{\psi}\norm{f + h}  - \psi (f) &\le \norm{\psi}(\norm{g + h} - 
  \norm{g - f}) -   \psi(f)\\
  & = \norm{\psi}(\norm{g + h} - \norm{g - f}) + \psi(g - f) - \psi(g)\\
  & \le \norm{\psi}\norm{g + h} - \psi(g)
  \end{aligned}
  $$
- So there must exists a $c$ that satisfies the condition.

##### Hahn-Banach theorem: real case

Suppose $V$ is a **seminormed space** over $\R$ and $U$ is a subspace of $V$.

Suppose $\psi \in \mathcal B(U, \R)$. Then there is a $\widehat \psi \in \mathcal B(V, \R)$ extending $\psi$ with $\n{\widehat \psi} = \n{\psi}$.

- Define $\A := \{\phi \in \mathcal B(W, \R): \norm{\phi} = \norm{\psi},\phi \supseteq \psi, U \le W \le V\}$.
- All chains $\mathcal C$ in $\A$ has upper bound $\cup \mathcal C$.
- So there is a maximal element $\varphi$ in $\A$. $\varphi \in \mathcal B(V, \R)$, otherwise extend it by above lemma.

##### Re: operator

Suppose $V$ is a vector space over $\C$.

- For $\psi \in \L(V, \C)$, define its **real part** $\re \psi \in \L(V, \R)$.
  - $\re$ is clearly linear.
- Any $\psi \in \L(V, \C)$ is completely determined by $\re \psi$. And $\psi(v) = \re \psi(v) - i \re \psi(iv)$.
  - $\psi(v) = \re \psi(v) + i \im \psi(v) = \re\psi (v) - i \re \psi(iv)$.
- For $\varphi \in \L(V, \R)$, define $\re^{-1} \varphi(v) = \varphi(v) - i\varphi(iv) \in \L(V, \C)$.
  - $\re^{-1}$ is linear, since $\re^{-1} \varphi(i v) = \varphi(i v) - i \varphi(- v) = i \re^{-1} \varphi(v)$.
- Clearly $\re$ and $\re^{-1}$ are inverse of each other.

Suppose $V$ is a **seminormed space** over $\C$. Then $\re$ and $\re^{-1}$ **preserves seminorms**.

- For $\psi \in \mathcal B(V, \C)$, $\norm{\re \psi} = \norm{\psi}$.
  - Clearly $\norm{\re \psi} \le \norm{\psi}$.
  - We can show that $\norm{\re \psi} \ge \norm{\psi}$.
    - Suppose $|\psi(v)| = A$. There exists $\psi(v)e^{i \theta} \in \R$ for $\theta \in [0, 2\pi)$.
    - Then $\psi(v e^{i \theta}) \in \R$ and $\norm{\psi(v e^{i \theta})} = \norm{\re \psi(v e^{i \theta})}$.
    - So $\norm{\re \psi} \ge \norm{\psi}$.
- For $\varphi \in \mathcal B(V, \R)$, $\norm{\re^{-1} \varphi} = \norm{\varphi}$.
  - $\n{\re \re^{-1} \varphi} = \n{\re^{-1} \varphi} = \n{\varphi}$.

Suppose $V$ is a **normed space** over $\C$. $\re$ and $\re^{-1}$ are **isometric isomorphisms**.

##### Hahn-Banach theorem: complex case

Let $V$ be a **seminormed space** over $\C$ and $U$ is a subspace of $V$.

Suppose $\psi \in \mathcal B(U, \C)$. Then there is a $\widehat \psi \in \mathcal B(V, \C)$ extending $\psi$ with $\n{\widehat \psi} = \n{\psi}$.

- Extend $\re \psi \in \mathcal B(U, \R)$ to $\widehat \psi \in \mathcal B(V, \R)$ where $\n{\widehat \psi} = \norm{\re \psi} = \norm{\psi}$.
- Define $\varphi = \re^{-1} \widehat \psi$ where $\n{\varphi} = \n{\widehat \psi} = \n \psi$.
- Clearly $\varphi$ indeed extends $\psi$.

##### Unit functional

Suppose $X$ is a normed space over $\bF$.

Suppose $x \in X$ is nonzero. There exists $f \in X'$ such that $\n f  = 1$ and $|f(x)| = \n x$.

- Define $f_0 \in \L(\bF f, \bF)$ as $f_0(x) = \n x$. Now apply (**Hahn-Banach**).
- So $\n x = \max_{f \in X', \n f = 1} f(x)$.

#### Dual Operators

##### Dual map of a linear map

Suppose $V, W$ are vector spaces over $\symbf F$.

If $T \in \L(V, W)$, then define $T': W' \to V'$ by $T'(\varphi) = \varphi \circ T$.

- $T' \in \L(W', V')$.
  - $(S+T)^{\prime}=S^{\prime}+T^{\prime}$ for all $S, T \in \mathcal{L}(V, W)$.
  - $(\lambda T)^{\prime}=\lambda T^{\prime}$ for all $\lambda \in \symbf{F}$ and all $T \in \mathcal{L}(V, W)$.
- $(S T)^{\prime}=T^{\prime} S^{\prime}$ for all $T \in \mathcal{L}(U, V)$ and all $S \in \mathcal{L}(V, W)$.
- $I_V' = I_{V'}$.

Suppose $V, W$ are normed vector spaces over $\bF$. Define $T'$ similarly for $T \in \mathcal B(V, W)$.

- $T' \in \mathcal B(W', V')$. And $\n{T'} = \n T$.

> TODO: Finish video from Lecture 7 in the middle.

##### Annihilator

 Suppose $V, W$ are vector spaces over $\symbf F$.

For $U \subset V,$ the **annihilator** of $U,$ denoted $U^{0},$ is defined by $U^{0}=\left\{\varphi \in V^{\prime}: \varphi[U] = \{0\}\right\}$. The set of functionals in $V'$ that are maps entire $U$ to zero.

- $U^{0}$ is a subspace of $V^{\prime}$.
- Suppose $V$ is **finite-dimensional**, $\dim U + \dim U^{0} = \dim V$.
  - Extend the basis of $U$ to a basis of $V$. Create the dual basis of this basis.

##### Finite dual basis

 Suppose $V$ is a **finite-dimensional** vector space over $\bF$.

- If $v_{1}, \ldots, v_{n}$ is a basis of $V$, define $\varphi_k \in V'$  as $\varphi_k(v_j) = \delta_{kj}$ for $1 \le k, j \le n$.
- Then $\varphi_1, \ldots, \varphi_n$ is a basis of $V'$. So $\dim V' = \dim V$.

##### Riesz: finite case

 Suppose $V$ is a **finite dimensional inner product space** over $\bF$. And $\varphi \in \L(V, \bF)$.

Suppose $\{e_1, \ldots, e_n\}$ is a orhtonormal basis of $V$. Then $u = \sum_i\overline{\varphi(e_i)} e_i \in V$ where $\varphi(v) = \pd u v$.
$$
\begin{aligned}
\varphi(v) &=\varphi\left(\left\langle v, e_{1}\right\rangle e_{1}+\cdots+\left\langle v, e_{n}\right\rangle e_{n}\right) =\left\langle v, e_{1}\right\rangle \varphi\left(e_{1}\right)+\cdots+\left\langle v, e_{n}\right\rangle \varphi\left(e_{n}\right) \\
&=\left\langle v, \overline{\varphi\left(e_{1}\right)} e_{1}+\cdots+\overline{\varphi\left(e_{n}\right)} e_{n}\right\rangle
\end{aligned}
$$

The vector $u$ is unique. Suppose there are two such vectors. $\langle v, u_1 \rangle = \langle v, u_2\rangle$ for all $v\in V$. Then $\pd v {u_1 - u_2} = 0$ for all $v \in V$. The only such vector is $0$.

##### Range and null space of dual map

 Suppose $V, W$ are vector spaces over $\symbf F$. $T \in \L(V, W)$.

- $\null T' = (\range T)^0$. The following are equivalent.
  - $\varphi \in \null T' \subseteq W'$.
  - $T'(\varphi) = 0 \in V'$.
  - $\forall v \in V: \varphi \circ T(v) = 0$.
  - $\forall w \in \range T: \varphi(w) = 0$.
  - $\varphi \in (\range T)^0$.
- $\range T' \subseteq (\null T)^0$. Since
  - $\theta \in \range T' \subseteq V'$ iff $\exists \varphi \in W': \theta = \varphi \circ T \in V'$.
  - Implies $\forall v \in \null T: \theta(v) = \varphi\circ T(v) = 0$ iff $\theta \in (\null T)^0$.

Suppose $V$ and $W$ are **finite-dimensional** vector spaces over $\bF$.

- The following are equal:
  - $\dim \null T'$.
  - $\dim (\range T)^0$.
  - $\dim W - \dim \range T$.
  - $\dim W - \dim V + \dim \null T$
- $T$ is surjective if and only if $T'$ is injective. Since $\dim W - \dim \range T = \dim \null T'$.
- $\dim \range T' = \dim \range T$. Since $\dim \range T = \dim W' - \dim \null T'$.
- $\range T' = (\null T)^0$. Since $\dim \range T' = \dim \range T = \dim (\null T)^0$.
- $T$ is injective if and only if $T'$ is surjective. Since $\dim \null T = \dim V' - \dim \range T'$.

##### Transpose of matrix and duality

 Suppose $A \in \bF^{m \times n}$. It has the transpose $A^t \in \bF^{n \times m}$.

- For $C \in \bF^{n \times p}$, $(AC)^t = C^t A^t$.
- $(A^t)^t = A$.

Suppose $V$ and $W$ are **finite-dimensional** vector spaces over $\bF$. And $T \in \L(V, W)$.

- Suppose $(v_i)_{i = 1}^m$ and $(w_j)_{j = 1}^n$ are **basis** of $V, W$.
- Construct the dual basis $(\varphi_i)_{i = 1}^m$ and $(\theta_j)_{j = 1}^n$.
- Suppose $T(v_i) = A_{ij} v_i$, i.e. $\M(T, v_i, w_i) = A$. Then $\M(T') = A^t$.
  - $T'(\theta_j) = \theta_j \circ T = B_{ji}\varphi_i$.
  - $\theta_j \circ T(v_k) = \theta_j (A_{ik}v_k) = A_{jk} = B_{ji}\delta_{ik} = B_{jk}$.
  - $T'(\theta_j) = A_{ji} \varphi_i$. So $\M(T') = \M(T)^t$.
- $\dim \operatorname{Col}(A) = r(A)$ is called the **column rank** of $A$.
- $\dim \operatorname{Row}(A) = r(A^t)$ is called the **row rank** of $A$.
- Since $r(A) = \dim \range T = \dim \range T' = r(A^t)$. So $r(A) = r(A^t)$.
- We can unify the column rank and row rank into $r(A)$ the **rank** of $A$.
