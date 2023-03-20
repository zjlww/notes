#### Extensibility of Solutions to IVPs

##### IVP: The maximal solution

Consider the following non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:

$$
\boxed{x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n)}, \quad (*)
$$

where $U$ is open and $(t_0, x_0) \in U$. And $f$ is Lipschitz in $x$ and continuous in $t$.

Suppose $x_1, x_2$ are two solutions of the IVP defined on the open intervals $I_1, I_2$ containing $t_0$. And $I = I_1 \cap I_2 = (T_-, T_+) \neq \varnothing$. Then $\forall t \in I: x_1(t) = x_2(t)$.

- Take the longest interval $(t_-, t_+) \ni t_0$ where $x_1 = x_2$.
  - Picard-Lindelof guarantees the existence of such interval.
- Then $t_+ = T_+$ and $t_- = T_-$.
  - Suppose $t_+ < T_+$. $x_1(t_+) = x_2(t_+)$.
  - Now an application of Picard-Lindelof at $(t_+, x_1(t_+))$ leads to a contradiction.
- $x = x_1 \cup x_2$ is a solution to the IVP on $I_1 \cup I_2$.

Suppose $x_a: I_a \to \R^n$ for $a \in A$ are all the solutions of the IVP on open interval $I_a$ containing $t_0$.

- Define open interval $I = \cup_{a \in A} I_a = (T_-, T_+)$.
  - $I$ is called the **maximal interval**.
- Define $x = \cup_{a \in A} x_a$. $x$ is called the **maximal solution**.
  - No other IVP solution exists on a larger open interval.

##### IVP: A limit test of extensibility

Consider the following non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:

$$
\boxed{x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n)}, \quad (*)
$$

where $U$ is open and $(t_0, x_0) \in U$. And $f$ is Lipschitz in $x$ and continuous in $t$.

Suppose $x(t): (t_-, t_+) \to \R^n$ is a solution of $(*)$ for the initial value $(t_0, x_0)$.

$x(t)$ is not maximal on the right side if and only if there exists $(t_n, x(t_n))_{n = 1}^\infty \to (t_+, x_+) \in U$.

- ($\from$)
  - We must have $\lim_{n \to \infty} x(t_n) = x_+$ for any $t_n \uparrow t_+$.
  - Otherwise $x(t)$ oscillates violently arounds $t_+$ while $x'(t)$ is bounded. A contradiction.
  - By Picard-Lindelof, there exists a unique solution $r$ in $(t_+ - \epsilon, t_+ + \epsilon)$ where $r(t_+) = x_+$.
  - Therefore we can glue $x, r$ together and $x \cup r$ extends $x$ on the right.

- ($\to$) Clearly, if there is an extension, then any $t_n \uparrow t_+$ converges to $(t_+, x(t_+))$.

##### IVP: bounded extension test

Consider the following non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:

$$
\boxed{x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(U \subseteq \R \times \R^{n} \to \R^n)}, \quad (*)
$$

where $U$ is open and $(t_0, x_0) \in U$. And $f$ is Lipschitz in $x$ and continuous in $t$.

Suppose $x(t): (t_-, t_+) \to \R^n$ is a solution of $(*)$ for the initial value $(t_0, x_0)$.

Further suppose there is a compact set $[t_0, t_+] \times C \subset U$ and sequence $(t_n) \in [t_0, t_+)$ such that $t_n \to t_+$ and $(\phi(t_n)) \subseteq C$. Then $x(t)$ is not maximal.

- Since $C$ is compact, there is a subsequence $(t_m,\phi(t_m)) \to (t_+, x_+)$ where $x_+ \in C$.
- Now the limit test says $x(t)$ is not maximal and can be extended on the right.

For maximal $x(t)$, and every compact set $C \subseteq \R^n$, $x(t)$ must eventually leave $[t_0, t_+) \times C$. So $x(t_+-) = \pm \infty$.

##### IVP: a test for the existence of a unique global solution

Consider the following non-autonomous IVP for $x \in C^1(J \subseteq \R \to \R^n)$:

$$
\boxed{x'(t) = f(t, x(t)), \quad x(t_0) = x_0, \quad f \in C(\R \times \R^{n} \to \R^n)}, \quad (*)
$$

where $(t_0, x_0) \in \R \times \R^n$. And $f$ is Lipschitz in $x$ and continuous in $t$.

Now suppose there bounding functions $M(t): \R^+ \to \R^+$ and $L(t): \R^+ \to \R^+$ such that
$$
\forall T > 0, \forall (t, x) \in [-T, T] \times \R^n: \n{f(t, x)} \le M(T) + L(T)\n{x}
$$
then all maximal solutions of $(*)$ are defined on $\R$.

- W.L.O.G. take $t_0 = 0$ and only consider positive time.
- Recall that $x(t) = x_0 + \int_0^t f(s, x(s)) \dd s$.
  - $\n{x(t)} \le \n{x_0} + \int_0^t \n{f(s, x(s))} \dd s$.
  - $\n{x(t)} \le \n{x_0} + \int_0^t M + L\n{x(s)}\dd s$ when $t \in [0, T]$.
  - Linear Gronwall's inequality gives $\n{x(t)} \le \n{x_0}e^{LT} + M(e^{LT} - 1)/L$.
- Now apply the bounded extension test.

