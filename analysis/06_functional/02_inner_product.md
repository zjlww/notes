(**Continuity of inner product**)

Suppose $V$ is an inner product space over $\bF$.

The inner product function $(x, y) \mapsto \pd{x}{y}$ is continuous under the induced norm.
$$
\begin{aligned}
\abs{\pd{x_n}{y_n} - \pd{x_m}{y_m}} &\le \abs{\pd{x_n}{y_n} - \pd{x_n}{y_m} + \pd{x_n}{y_m} - \pd{x_m}{y_m}}\\
& \le \abs{\pd{x_n}{y_n} - \pd{x_n}{y_m}} + \abs{\pd{x_n}{y_m} - \pd{x_m}{y_m}}\\
& \le \n{x_n} \n{y_n - y_m} +  \n{x_n - x_m} \n{y_m}
\end{aligned}
$$
Therefore the sequence is Cauchy and convergent.

(**Generalized inner product in $L^p$ spaces**)

For $f \in L^p(X \to \C, \mu)$ and $g \in L^q(X \to \C, \mu)$. Define the Lp inner product:
$$
\pd{f}{g} := \int_{X} f(x)\overline{g(x)} \dd x
$$
The Lp inner product is continuous on $L^p \times L^q$. The proof is identical to traditional inner products.