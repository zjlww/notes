#### Signed Measures

(**Signed measure**)

A **set function** $\lambda: \S \to \eR$ on $\S \subseteq \P(X)$ is

- **finitely additive** if for $A, (A_i)_{i = 1}^n \in \S$, and $A = +_i A_i$, then $\lambda(+_iA_i) = \lambda(A)$.
- **subtractive** if $A, B \in \S$ and $A - B \in \S$ and $\lambda(B) \in \R$. Then $\lambda(A - B) = \lambda(A) - \lambda(B)$.
  - $\lambda$ is subtractive if $\lambda$ is finitely additive.
- **countably additive** if for $A, (A_i)_{i = 1}^\infty \in \S$ and $A = +_i A_i$, $\lambda(+_i A_i) = \lambda(A)$.
- **continuous from above** if for $A, (A_i)_{i = 1}^\infty \in \S$ and $A_i \uparrow A$, $\lambda(A_i) \to \lambda(A)$.
- **continuous from below** if for $A, (A_i)_{i = 1}^\infty \in \S$ and $A_i \downarrow A$, $\lambda(A_i) \to \lambda(A)$.
- a **signed proto-measure** if $\lambda(\varnothing) = 0$.

$\lambda$ is a **signed measure**

- a **signed measure** if $\lambda$ is countably additive proto-measure.

(**Signed measures admits extremum values**)

Suppose $\lambda$ is a **signed measure** on measurable space $(\Omega, \F)$.

Then $\lambda$ **obtains its maximum and minimum** value.

- Suppose $a = \sup_{A \in \F} \lambda(A)$.
- It is possible to construct $\p{A_n} \subseteq \F$ where $\lambda(A_n) > a - 1/n$.
- **Fracture** $\p{A_n}$ into disjoint pieces. Pick positive pieces to construct $\p{B_n}$.
- $B = \cup B_n$, then $\lambda(B) > a - 1/n$ so $\lambda(B) = a$.

Immediately $\lambda$ can only has range in $(-\infty, \infty]$ or $[-\infty, \infty)$. Otherwise $+\infty - \infty$ arises.

- Suppose $\lambda(A) = +\infty$ and $\lambda(B) = -\infty$.
- Fracture $A, B$ into disjoint pieces.

(**Hahn decomposition**)

Suppose $\lambda$ is a signed measure on measurable space $(\Omega, \F)$.

Define $\lambda^+(A) = \sup \{\lambda(B): B \in \F, B \subseteq A\}$ and $\lambda^-(A) = -\inf \{\lambda(B): B \in \F, B \subseteq A\}$.

- Clearly $(-\lambda)^+ = \lambda^-$ and $(-\lambda)^- = \lambda^+$.
- $\lambda^+$ is called the **upper variation** / positive part of $\lambda$.
- $\lambda^-$ is called the **lower variation** / negative part of $\lambda$.
- Define **total variation** of $\lambda$ as $|\lambda| = \lambda^+ + \lambda^-$.

$D \in \F$ is a **(negative) stable set** for $\lambda$ if $\forall A \in \F: \lambda(A \cap D) \le 0 \land \lambda (A \cap D^c) \ge 0$.

Suppose a stable set does exist, we can find the value of $\lambda^+$ and $\lambda^-$.
- $\forall A \in\F:\lambda(A \cap D^c) = \lambda^+(A) = \sup \{\lambda(B): B \in \F, B \subseteq A\}$.
    - Since for $\forall B \subseteq A: \lambda(B) \le \lambda(B\cap D^c) \le \lambda(A \cap D^c)$.
- $\forall A \in \F:\lambda(A \cap D) = -\lambda^-(A) = \inf \{\lambda(B): B \in \F, B \subseteq A\}$.
    - Since for $\forall B \subseteq A: \lambda(B) \ge \lambda(B \cap D) \ge \lambda(A \cap D)$.

A stable set always exists for any $\lambda$.
- When $\lambda \F \subseteq (-\infty, +\infty]$, let $D = \arg\min_{F \in \F} \lambda(F)$.
- When $\lambda \F \subseteq [-\infty, +\infty)$, let $D = (\arg\max_{F \in \F} \lambda (F))^c$.
- To show these are indeed stable sets, verify by definition.
- Suppose $D$ and $E$ are both stable sets for $\lambda$. Then $|\lambda|(D \Delta E) = 0$.

So $\lambda^+$ and $\lambda^-$ and $|\lambda|$ are **measures** on $\F$ and $\lambda = \lambda^+ - \lambda^-$.

(**Finiteness of signed measures**)

Suppose $\mu$ is a **signed measure**.

- $\mu$ is finite if $|\mu|$ is finite. $\sigma$-finite similarly.
- $\mu$ is finite iff $|\mu|$ is finite iff $\mu_+$ and $\mu_-$ are finite. $\sigma$-finite similarly.

(**Continuity of measure**)

Suppose $(\Omega, \F)$ is a measurable space and $\mu, \lambda$ are signed measures on $\F$.

- $\lambda$ is **absolutely continuous** with respect to $\mu$ if
  $$
  \forall A \in \F: \mu(A) = 0 \to \lambda(A) = 0
  $$

  - Denoted by $\lambda \ll \mu$.

(**Density of measure**)

Suppose $(\Omega, \F, \mu)$ is a measure space. And $f \in \overline L(X \to \eR)$. Define $\mu_f(A):= \mu(f1_A)$.

- $\mu_f$ is a **signed measure** and $\mu_f \ll \mu$.
- $f$ is called a **Radon-Nikodym derivative / density** of $\mu_f$ with respect to $\mu$.
  - Clearly such $f$ is **unique** up to a $\mu$-null set.
  - Also denoted as $f = \dd\mu_f / \dd\mu$ or $f \dd\mu = \dd\mu_f$.

- $\mu_f^+ = \mu_{f^+}$ and $\mu_f^- = \mu_{f^-}$.
- $f \in L^1(X\to \eR, \mu)$ if and only if $\mu_f$ is finite.

Now suppose $f \in L(X \to [0, \infty], \mu)$ and $g \in L(X \to [0, \infty], \mu)$ then $\mu_f(g) = \mu(fg)$
- Take a sequence $(g_n)$ where $g_n \uparrow g$ pointwise. And apply MCT.
- The result can be generalized to $\R, \eR, \C$.

(**Radon-Nikodym theorem**)

Suppose $(\Omega, \F, \mu)$ is a **$\sigma$-finite** measure space. And $\lambda$ is a signed measure on $\F$ where $\lambda \ll \mu$. Then there exists a unique $g \in \overline L(\Omega \to \eR, \mu)$ such that $g = \dd\lambda / \dd\mu$.

1. Suppose $\lambda$ and $\mu$ are finite measures. $g \in L^1(\Omega \to [0, \infty], \mu)$.
   - $\S:= \{f \in \L^1(\Omega \to [0, \infty], \mu): \mu_f \le \lambda\}$. $0 \in \S \neq \varnothing$.
     - Define $f \le g$ for $f, g \in \S$ if $f \le g$ $\mu$-a.e.
     - $f, g \in \S \implies \max(f, g) \in \S$ (pointwise).
   - Define $s = \sup\{\mu f: f \in \S\} \le \lambda \Omega < \infty$.
   - Let $(f_n)_{n = 1}^\infty \in \S$ and $\mu f_n \uparrow s$. Define $g_n = \max(f_1, \ldots, f_n) \in \S$.
   - Suppose $g_n \uparrow g \in \L^1(\Omega \to [0, \infty], \mu)$, $\mu g_n \uparrow \mu g = s$, and $g \in \S$.
   - Define measure $\gamma = \lambda - \mu_g$. $\gamma \ll \lambda \ll \mu$, and $\gamma \le \lambda$.
   - We now claim that $\gamma = 0$ so $\lambda = \mu_g$. Otherwise...
     - Suppose $\gamma(\Omega) > 0$. $\mu(\Omega) - k \gamma(\Omega) < 0$ for some $k \in (0, \infty)$.
     - Define $\theta = \mu - k \gamma$. Then $\theta$ is a finite signed measure.
     - Suppose $D$ is a negative stable set of $\theta$.
     - Suppose $\mu(D) = 0$ then $\gamma(D) = \lambda(D) = \theta(D) = 0$. Contradiction.
     - So $\mu(D) > 0$. Let $h = 1_D/k + g \in \L^1(\Omega \to [0, \infty], \mu)$.
     - $\mu_A(1_D/k) = \mu(A \cap D)/k \le \gamma(A \cap D) \le \gamma(A) = \lambda(A) - \mu_g(A)$.
     - So $g + 1_D/k \in \S$. Contradiction.
2. Suppose $\mu$ is a finite measure. $\lambda$ is a $\sigma$-finite measure. $g \in L(\Omega \to [0, \infty], \mu)$.
   - Suppose $(A_n)_{n = 1}^\infty \in \F$ and $\Omega = +_n A_n$ and $\mu(A_n) < \infty$.
   - Find $g_n \in \L^1(A_n \to [0, \infty], \mu)$ such that $\lambda|_{A_n} = \mu_{g_n}$.
   - $\lambda = \sum_{n = 1}^\infty \lambda|_{A_n} = \sum_{n = 1}^\infty \mu_{g_n} = \mu_{\sum_n g_n}$.
   - $g = \sum_n g_n \in \L(\Omega \to [0, \infty])$.
3. Suppose $\mu$ is a finite measure, $\lambda$ is a measure. $g \in L(\Omega \to [0, \infty])$.
   - Suppose $\mathcal C \subseteq \F$ where $A \in \mathcal C$ iff $\lambda|_A$ is $\sigma$-finite on $\F|_A$. $\varnothing \in \mathcal C$.
   - Define $s = \sup\{\mu A: A \in \mathcal C\} \ge 0$. Let $(C_n)_{n = 1}^\infty \in \mathcal C$ where $\mu C_n \to s$.
   - Define $C = \cup_n C_n$. Then $C \in \mathcal C$. And $s \ge \mu(C) \ge \mu(C_n) \to s$. So $\mu(C) = s$.
   - By (2), for some $g \in \L(C \to [0, \infty])$, $\forall A \in \F|_C:\lambda(A) = \mu(1_{A }g)$.
   - Now consider any $A \in \F$:
     - Suppose $\mu(A \cap C^c) > 0$. Then $\lambda(A \cap C^c) = \infty$. Otherwise Contradiction.
     - Suppose $\mu(A \cap C^c) = 0$. Then $\lambda(A \cap C^c) = 0$.
     - So $\lambda(A \cap C^c) = \mu(\infty 1_{A \cap C^c})$.
   - Define $g'$ by $g' = 1_{C} g + 1_{C^c} \infty$.
   - Then $\forall A \in \F: \lambda(A) = \lambda(A \cap C) + \lambda(A \cap C^c) = \mu(1_A g')$.
4. Suppose $\mu$ is a $\sigma$-finite measure, $\lambda$ is a measure. $g \in L(\Omega \to [0, \infty])$.
   - Suppose $(A_n)_{n = 1}^\infty \in \F$ and $\Omega = +_n A_n$ and $\mu(A_n) < \infty$.
   - Find $g_n \in \L(A_n \to [0, \infty], \mu)$ such that $\lambda|_{A_n} = \mu_{g_n}$.
   - $\lambda = \sum_{n = 1}^\infty \lambda|_{A_n} = \sum_{n = 1}^\infty \mu_{g_n} = \mu_{\sum_n g_n}$.
   - $g = \sum_n g_n \in \L(\Omega \to [0, \infty])$.
5. Suppose $\mu$ is a $\sigma$-finite measure, $\lambda$ is a signed measure. $g \in \overline L(\Omega \to \eR, \mu)$.
   - Suppose $\lambda = \lambda^+ - \lambda^-$ where $\lambda^-$ is finite.
   - Let $g^+ \in \L(\Omega \to [0, \infty])$ and $\mu_{g^+} = \lambda^+$.
   - Let $g^- \in \L^1(\Omega \to [0, \infty], \mu)$ and $\mu_{g^-} = \lambda^-$.
   - Then define $g = g^+ - g^- \in \overline \L(\Omega \to \eR, \mu)$ almost everywhere, and $\lambda = \mu_g$
6. Suppose $\mu$ is a $\sigma$-finite measure, $\lambda$ is a finite signed measure. $g \in L^1(\Omega \to \eR, \mu)$.
   - Following (5), $\mu(g^\pm) = \lambda^\pm \Omega < \infty$.
7. Suppose $\mu$ is a $\sigma$-finite measure, $\lambda$ is a signed measure where $|\lambda|$ is $\sigma$-finite. $g \in \overline L(\Omega \to \eR, \mu)$ is finite $\mu$-a.e.
   - Suppose $(A_n)_{n = 1}^\infty \in \F$ and $\Omega = +_n A_n$ and $\mu(A_n) < \infty$.
   - $g$ is finite $\mu$-a.e. on each $A_n$ by (6). So $g$ is finite $\mu$-a.e.

(**Mutually singular**) 

Suppose $(\Omega, \F)$ is a measurable space. If $\mu, \nu, \gamma$ are **signed measures** on $\F$.

- $\mu$ and $\nu$ are **mutually singular** if for $A \in \F$, $|\mu|(A) = |\nu|(A^c) = 0$, denoted by $\mu \perp \nu$.
- $\mu \perp \gamma \land \nu \perp \gamma \implies (\mu + \nu) \perp \gamma$. (if the addition makes sense.)

Suppose $\mu$ is a measure and $\lambda, \gamma$ are signed measures on $\F$.

- $\lambda \ll \mu \iff |\lambda| \ll \mu \iff \lambda^+ \ll \mu \land \lambda^- \ll \mu$.
- $\lambda \ll \mu \land \gamma \perp \mu \implies \lambda \perp \gamma$.
- $\lambda \perp \lambda \implies \lambda = 0$.
- $\lambda \ll \mu \land \lambda \perp \mu \implies \lambda = 0$.

(**Lebesgue decomposition**)

Suppose $(\Omega, \F, \mu)$ is a measure space.

Suppose $\lambda$ is a signed measure and $|\lambda|$ is a $\sigma$-finite measure.

Then $\lambda$ has a **unique decomposition** into **signed measures** $\lambda = \lambda_s + \lambda_c$ where $\lambda_c \ll \mu$ and $\lambda_s \perp \mu$.

1. Suppose $\lambda$ is a finite measure. $\lambda_s$ and $\lambda_c$ are finite measures.
   - Define $\sigma$-algebra $\mathcal C = \{A \in \F: \mu A = 0\}$. Define $s = \sup \lambda[\mathcal C] \le \lambda(\Omega) < \infty$.
   - Pick $(A_n)_{n = 1}^\infty \in \mathcal C$ such that $\lambda A_n \uparrow s$, then $A^* = \cup_n A_n \in \mathcal C$. $\lambda(A^*) = s$.
   - Clearly $\forall B \in \mathcal C: \lambda(B - A^*) = 0$. Otherwise $\lambda(B \cap A^*) > s$.
   - For $A \in \F$ define $\lambda_c(A) = \lambda(A - A^*)$ and $\lambda_s(A) = \lambda(A \cap A^*)$. $\lambda = \lambda_s + \lambda_c$.
     - When $\mu(A) = 0$, $A \in \mathcal C$ and $\lambda_c(A) = 0$. So $\lambda_c \ll \mu$.
     - When $\mu(A^*) = 0$, $\lambda_s(A^*)^c = 0$. So $\lambda_s \perp \mu$.
   - The decomposition is unique.
     - Suppose $\lambda = \lambda_s' + \lambda_c'$ as well and $\lambda_c' \ll \mu$ and $\lambda_s' \perp \mu$.
     - $\lambda_c - \lambda_c' \ll \mu$ and $\lambda_s - \lambda_s' \perp \mu$.
     - $0 = (\lambda_c - \lambda_c') + (\lambda_s - \lambda_s')$. So $\lambda_c - \lambda_c' = 0$ and $\lambda_s - \lambda_s' = 0$.
2. Suppose $\lambda$ is a $\sigma$-finite measure. $\lambda_s$ and $\lambda_c$ are $\sigma$-finite measures.
   - Suppose $(F_m)_{m = 1}^\infty \in \F$ and $\lambda(F_m) < \infty$ and $\Omega = +_m F_m$.
   - On each $F_m$ decompose $\lambda(A \cap F_m) = \lambda_c^{(m)}(F_m) + \lambda_s^{(m)}(F_m)$.
   - Let $\lambda_c = \sum_{m } \lambda_c^{(m)}$ and $\lambda_s = \sum_m \lambda_s^{(m)}$. Clearly $\lambda_c \ll \mu$ and $\lambda_s \perp\mu$. And $\lambda = \lambda_s + \lambda_c$.
   - And the decomposition is unique.
3. Suppose $\lambda$ is a finite signed measure. $\lambda_s$ and $\lambda_c$ are finite signed measures.
   - Then $\lambda^+$ and $\lambda^-$ are finite masures.
   - Let $\lambda^+ = \lambda^+_s + \lambda_c^+$ and $\lambda^- = \lambda_s^- + \lambda_c^-$.
   - Let $\lambda_s = \lambda_s^+ - \lambda_s^-$ and $\lambda_c = \lambda_c^+ - \lambda_c^-$. Clealry $\lambda_s \ll \mu$ and $\lambda_c \perp \mu$.
   - The decomposition is unique. See (1).
4. Suppose $\lambda$ is a $\sigma$-finite signed measure. $\lambda_s$ and $\lambda_c$ are $\sigma$-finite signed measures.
   - See (2).

