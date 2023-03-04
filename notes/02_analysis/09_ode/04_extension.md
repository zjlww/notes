##### IVP: The maximal solution

Consider the following non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:

$$
x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n), \quad (*)
$$

where $U$ is open and $(t_0, x_0) \in U$. And $f$ is Lipschitz in $x$ uniformly in $t$.

Suppose $x_1, x_2$ are two solutions of the IVP defined on the open intervals $I_1, I_2$ containing $t_0$. And $I = I_1 \cap I_2 = (T_-, T_+) \neq \varnothing$. Then $\forall t \in I: x_1(t) = x_2(t)$.

- Take the longest interval $(t_-, t_+) \ni t_0$ where $x_1 = x_2$.
  - Picard-Lindelof guarantees the existence of such interval.
- Then $t_+ = T_+$ and $t_- = T_-$.
  - Suppose $t_+ < T_+$. $x_1(t_+) = x_2(t_+)$.
  - Now an application of Picard-Lindelof at $(t_+, x_1(t_+))$ leads to a contradiction.
- $x = x_1 \cup x_2$ is a solution to the IVP on $I_1 \cup I_2$.

Suppose $(x_a)_{a \in A}$ is the set of all solutions of the IVP on open intervals containing $t_0$.

- For $x_a(t)$, let $I_a$ be its open interval domain.
- Define open interval $I = \cup_{a \in A} I_a = (T_-, T_+)$.
  - $I$ is called the **maximal interval**.
- Define $x = \cup_{a \in A} x_a$. $x$ is called the (unique) **maximal solution**.
  - No other IVP solution exists on a larger open interval.

##### IVP: limit extension test

Suppose $x(t)$ is a solution of $(*)$ on $(t_-, t_+)$. Suppose there exists $(t_n, x(t_n))_{n = 1}^\infty \to (t_+, x_+) \in U$, $x(t)$ is not maximal and can be extended on the right.

- The limit $x(t_+-) = x_+$. Define $x(t_+) = x_+$.
  - If the limit is not $x_+$, or it does not exist, $x(t)$ will oscillate near $t_+$.
  - $f(t, x(t)) = x'(t)$ is bounded in some rectangle $V = [t_+ - \delta, t_+] \times \overline{B(x_+; \delta)}$.
  - With some further analysis, there will be a contradiction.
- $x'_-(t_+) = f(t_+, x_+)$.
  - Since $f(t, x)$ is uniformly continuous on $V$.
- Now apply Picard-Lindelof at $(t_+, x_+)$ to get the unique solution $r(t)$ on $[t_+, t_+ + \epsilon)$.
  - $r'_+(t_+) = f(t_+, x_+)$ and $r(t_+) = x_+$.
- Define $\tilde x = x \cup r$ on $(t_-, t_+ + \epsilon)$.
  - $\tilde x \in C^1((t_-, t_+ + \epsilon) \to \R^n)$.
  - $\tilde x$ is a solution to the ODE.

##### IVP: bounded extension test

Suppose $x(t)$ is a solution of $(*)$ on $(t_-, t_+)$. Suppose there is a compact set $[t_0, t_+] \times C \subset U$ and sequence $(t_n) \in [t_0, t_+)$ such that $t_n \to t_+$ and $(\phi(t_n)) \in C$. Then $x(t)$ is not maximal and can be extended on the right.

- Since $C$ is compact, there is a subsequence $(t_m,\phi(t_m)) \to (t_+, x_+)$ where $x_+ \in C$.
- Now apply previous result.

(Corollary) Suppose $x(t)$ is the maximal solution of $(*)$ on $(T_-, T_+)$ and $T_+ < \infty$. Then for every compact set $C \subseteq \R^n$, $x(t)$ must eventually leave $[t_0, T_+) \times C$. So $x(T_+-) = \pm \infty$.

##### IVP: existence of global solution

Consider IVP $(*)$. Suppose $U = \R \times \R^n$ and
$$
\exists (M, L) \in \R^+ \to \R^+, \forall T > 0, \forall (t, x) \in [-T, T] \times \R^n: \n{f(t, x)} \le M(T) + L(T)\n{x}
$$
then all maximal solutions of $(*)$ are defined on $\R$.

- W.L.O.G. take $t_0 = 0$ and only consider positive time.
- Recall that $x(t) = x_0 + \int_0^t f(s, x(s)) \dd s$.
  - $\n{x(t)} \le \n{x_0} + \int_0^t \n{f(s, x(s))} \dd s$.
  - $\n{x(t)} \le \n{x_0} + \int_0^t M + L\n{x(s)}\dd s$ when $t \in [0, T]$.
  - Linear Gronwall's inequality gives $\n{x(t)} \le \n{x_0}e^{LT} + M(e^{LT} - 1)/L$.
- Now apply the bounded extension test.

