#### Set Limits

##### Set limits

Suppose $\Omega$ is a nonempty set. For any $(A_n)_{n = 1}^\infty \in \P(\Omega)$.

- Define $\sup_{n}A_n := \cup_{n}A_n = \{\omega \in \Omega: \sup_n 1_{A_n}(\omega) = 1\}$.
- Define $\inf_n A_n := \cap_n A_n = \{\omega \in \Omega: \inf_n 1_{A_n}(\omega) = 1\}$.

Consider $\omega \in \Omega$ where $A_n$ happens infinitely many times (or happens **infinitely often**, i.o.)

- $A^* = \limsup_n A_n = \cap_{n=1}^\infty \cup_{i = n}^\infty A_i$.
- $1_{A^*} = \limsup_n 1_{A_n}$.
- $A^* = \{\omega \in \Omega: \sum_n 1_{A_n} = \infty\}$.

Consider $\omega \in \Omega$ where $A_n$ happens but finitely many times (or happens **ultimately**, ult.)
- $A_* = \liminf_n A_{n} = \cup_{n=1}^{\infty} \cap_{i=n}^{\infty} A_{i}$. 
- $A_* = (\liminf_n 1_{A_n})^{-1}\{1\}$.
- $1_{A_*} = \liminf_n 1_{A_n}$.
- $A_* = \{\omega \in \Omega: \sum_n 1_{A_n^c} < \infty\}$.

Clearly $A^* \supseteq A_*$. When $A^* = A_*$. $A_n$ is said to **converge** to $A = A^* = A_*$.

- For all $\omega \in \Omega$ $\lim_{n \to \infty} 1_{A_n}(\omega)$ exists. $A = \{\omega \in \Omega: \lim_{n \to \infty} 1_{A_n} (\omega) = 1\}$.

##### Set sequence monotonicity

**Monotonicity** is defined on set sequences:

- $A_n$ is increasing if $\forall n \in \N^+: A_n \subseteq A_{n+1}$.
  - $A_* = A^*$ and $\lim_n A_n = \cup_n A_n$.

- $A_n$ is decreasing if $\forall n \in \N^+: A_n \supseteq A_{n+1}$.
  - $A_* = A^*$ and $\lim_n A_n = \cap_n A_n$.
