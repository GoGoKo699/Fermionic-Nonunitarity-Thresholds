# Heralding a normalized nonunitary transformation

The [model](model.md) supplies one unknown input specimen and a known invertible operator $`K`$. A simulator must return, on a flagged success branch, a state close to

```math
\tau_\psi
=\frac{K|\psi\rangle\langle\psi|K^\dagger}
       {\langle\psi|K^\dagger K|\psi\rangle}.
```

The input's classical description, a preparation oracle, and additional specimens are not supplied. The success operation may use arbitrary ancillas, measurements, classical records, and adaptive control. All such processing induces one completely positive, trace-nonincreasing map $`\mathcal T`$ on the supplied specimen. Write

```math
p_\psi=\operatorname{Tr}\mathcal T(\psi),\qquad
\rho_\psi=\frac{\mathcal T(\psi)}{p_\psi},\qquad
p_{\min}=\inf_\psi p_\psi.
```

A claim with $`p_{\min}>0`$ requires the conditional accuracy promise on every allowed pure input. If the worst success probability is zero, all upper bounds below are already satisfied.

Throughout, trace distance means $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. Fidelity means the **root** fidelity $`F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1`$; thus pure-state fidelity is the absolute overlap, without squaring. Put

```math
\kappa=\frac{s_{\max}(K)}{s_{\min}(K)}\geq1.
```

## Exact optimal success on all pure inputs

**Proposition 1.** If the allowed inputs are all pure states of the finite-dimensional input space, then

```math
p_{\mathrm{all}}^\star(0;K)=\kappa^{-2}.
```

This is the standard optimal normalized-filter law, included here to make the accuracy and access conventions explicit. The filter construction and its normalization are inherited from Terashima and Ueda; probabilistic state transformation and separation provide the wider framework. See [related work](../references/RELATED_WORK.md).

To prove the converse, let $`A_\ell`$ be success Kraus operators. For every pure input, the successful output has rank one and lies on the ray of $`K|\psi\rangle`$. Each $`A_\ell|\psi\rangle`$ must therefore lie on that ray. If the success probability is zero on a vector, every success Kraus operator annihilates it, so the same collinearity statement still holds. Consequently $`K^{-1}A_\ell`$ sends every vector into its own linear span. Applying this property to basis vectors and their pairwise sums gives

```math
A_\ell=c_\ell K.
```

Trace nonincrease now implies

```math
\left(\sum_\ell|c_\ell|^2\right)K^\dagger K\preceq I,
\qquad
\sum_\ell|c_\ell|^2\leq s_{\max}(K)^{-2}.
```

The worst success probability is at most $`s_{\min}(K)^2/s_{\max}(K)^2`$. Equality is attained by the one-Kraus filter

```math
A=\frac{K}{\|K\|}.
```

A unitary dilation realizes this contraction. Its efficient fermionic implementation is a separate [resource question](implementation.md); an abstract dilation alone would not establish a small circuit.

The proposition is stated for all pure inputs. A promise restricted to Slater determinants requires its own converse and must not simply inherit this optimality argument.

## Fixed conditional error does not remove the conditioning penalty

**Proposition 2.** Suppose that, on every pure input,

```math
D(\rho_\psi,\tau_\psi)\leq\epsilon,
\qquad 0<\epsilon<\frac12.
```

Then every success map satisfies

```math
p_{\min}
\leq
\min\left\{
1,\,
\frac{2}
 {(\kappa^2+1)\bigl[1-2\sqrt{\epsilon(1-\epsilon)}\bigr]}
\right\}.
```

The exact filter remains an admissible construction. Hence, with $`\epsilon`$ fixed,

```math
\kappa^{-2}
\leq p_{\mathrm{all}}^\star(\epsilon;K)
\leq
\min\{1,C_\epsilon\kappa^{-2}\},
\qquad
C_\epsilon=\frac{2}{1-2\sqrt{\epsilon(1-\epsilon)}}.
```

This is a worst-input bound. It does not upper-bound the success probability of every individual state.

### A nearly parallel input pair

In dimension one the bound is trivial because $`\kappa=1`$. Otherwise choose orthonormal right singular vectors $`x,y`$ with singular values $`s_{\min},s_{\max}`$. The two normalized inputs

```math
|\psi_\pm\rangle
=\frac{|x\rangle\pm\kappa^{-1}|y\rangle}
       {\sqrt{1+\kappa^{-2}}}
```

have root fidelity

```math
r=|\langle\psi_+|\psi_-\rangle|
 =\frac{\kappa^2-1}{\kappa^2+1}.
```

Their ideal normalized outputs are orthogonal: their two left-singular-vector components have equal magnitude and opposite relative signs.

Let $`\rho_+,\rho_-`$ be the actual successful outputs. Measuring the projector onto the positive ideal output gives probabilities $`a\geq1-\epsilon`$ and $`b\leq\epsilon`$. Fidelity cannot decrease under this binary measurement. Since $`a>b`$ for $`\epsilon<1/2`$,

```math
\begin{aligned}
F(\rho_+,\rho_-)
&\leq \sqrt{ab}+\sqrt{(1-a)(1-b)}\\
&\leq 2\sqrt{\epsilon(1-\epsilon)}
=:f_\epsilon<1.
\end{aligned}
```

The second inequality is attained at $`a=1-\epsilon,b=\epsilon`$. This direct binary-measurement argument permits the entire interval $`0<\epsilon<1/2`$.

### Include failures before applying information monotonicity

Let $`p,q`$ be the two success probabilities. Complete the success operation to a trace-preserving channel and replace every failure output by one fixed failure flag. Root fidelity of the resulting flagged states, together with fidelity monotonicity, gives

```math
r\leq
\sqrt{pq}\,F(\rho_+,\rho_-)
+\sqrt{(1-p)(1-q)}.
```

This step permits arbitrary state-dependent success probabilities and arbitrary physical failure records; discarding the latter only increases fidelity. Arithmetic-geometric mean bounds imply

```math
\begin{aligned}
f_\epsilon\sqrt{pq}+\sqrt{(1-p)(1-q)}
&\leq 1-\frac{p+q}{2}(1-f_\epsilon)\\
&\leq 1-\min\{p,q\}(1-f_\epsilon).
\end{aligned}
```

Therefore

```math
p_{\min}\leq\min\{p,q\}
\leq\frac{1-r}{1-f_\epsilon}
=\frac{2}{(\kappa^2+1)(1-f_\epsilon)}.
```

This is the familiar probabilistic state-separation obstruction, used with a fixed-error output promise. It does not assume a particular block encoding, Gaussian processor, no-jump implementation, or number of accepted measurement records.

## Consequences for the chain

For $`K=\bigwedge^m U_g(t_N)`$, the [finite-time dynamics theorem](dynamics.md) supplies the lower and upper conditioning bounds. At fixed filling and bounded asymmetry, they give

```math
\log\kappa(K)=\Theta(g_NN^2)
```

when $`g_NN^2\to\infty`$, with the stated exponentially small finite-size correction retained in the finite theorem. Propositions 1–2 consequently imply

```math
p_{\mathrm{all}}^\star(\epsilon;K)
=\exp[-\Theta_\epsilon(g_NN^2)]
```

in that regime. Constants also depend on the fixed filling window, hopping cap, and chosen ballistic-time coefficient.

For finite error, a small conditioning cost can be absorbed into an accurate deterministic approximation. The robust statement is therefore a logarithmic cost up to an additive $`O_\epsilon(1)`$, rather than a nonzero exponential penalty uniformly down to $`g_NN^2=0`$.

At a fixed required success probability $`p_0>0`$ and fixed $`\epsilon<1/2`$, the all-input asymmetry scale is $`N^{-2}`$: a sufficiently small constant times $`N^{-2}`$ is sufficient by the [deterministic approximation](gaussian_approximation.md), while any uniformly accurate simulator with success at least $`p_0`$ must have $`g_N=O_{\epsilon,p_0}(N^{-2})`$. The analogous Slater-input scale is proved separately in the [Gaussian converse](gaussian_converse.md).

## What success probability measures

These theorems concern the yield of one attempt on one unknown specimen. Failure may destroy that specimen. Interpreting $`1/p`$ as a repetition cost requires a source that can supply fresh specimens, and every such preparation must be charged. Neither an input-state preparation oracle nor amplitude amplification of an unknown specimen is supplied by the model.

The [interpretation](interpretation.md) distinguishes this processing task from preparing a classically described state, estimating a few observables, or numerically evolving an orbital matrix. The mathematical obstruction does not assert that those different tasks are inefficient.

