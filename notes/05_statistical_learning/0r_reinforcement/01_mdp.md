##### Fully-observed Markov decision process

A Markov decision process (MDP) consists of two processes over discrete time $\I \subseteq \N$.

- The state Markov process $(S_t)_{t \in \I}$ on the state space $\S$.
- The action process $(A_t)_{t \in \I}$ on the action space $\A$.

Consider the following densities:

- $\pi_t(a_t | s_t)$ is a **policy**. $A_t$ only depends on $S_t$.
  - When $\pi_t$ do not depend on $t$, it is called **stationary**, and written as $\pi$.
- $p(s_{t + 1} | s_t, a_t)$ is the **environment**. $S_{t + 1}$ only depends on $(S_t, A_t)$.
- $r(s_t, a_t)$ is the **reward function**.

$\tau = (s_0, a_0, s_1, a_1, \ldots)$ is a **trajectory** of the MDP. Let $\T$ be the space of all trajectories.

- $p_\pi(\tau)$ is the density of trajectories under policy $\pi$.

We have some conventional terms for different $\I$.
- Bandits. $\I = \c{0, 1}$.
- Infinite horizon. $\I=\N$.
- Episodic. $\I = \N$. But the process $(S_t)$ is terminated at stopping time $T$.

##### Partially-observed Markov decision process

A partially-observed Markov decision process (POMDP) consists of three processes.

- $(S_t), (A_t)$ from the MDP.
- The observation process $(O_t)$ on the observation space $\O$.
  - Distribution of $O_t$ only depends on $S_t$. With density $p(o_t | s_t)$.
- Now the policy is $\pi(a_t | o_t)$. $A_t$ only depends on $O_t$.