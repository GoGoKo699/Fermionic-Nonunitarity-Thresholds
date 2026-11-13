# Unknown-state propagation and its input promises

A non-Hermitian one-particle matrix maps occupied orbitals to occupied orbitals. If those orbitals are known classically, the resulting Slater determinant can be calculated and prepared. A different physical task is to receive an **unknown quantum specimen**, transform it coherently, and return the requested quantum output. The latter task is the subject here.

The same prescribed transformation has sharply different approximate implementations on unknown Slater determinants and on arbitrary correlated fermionic inputs. The distinction concerns the **input promise**. Both lower bounds allow arbitrary quantum processing, including non-Gaussian controls.

## Chain, filling and prescribed evolution

There are $`N\geq3`$ fermionic modes and a known particle number $`m`$. Let $`c_j^\dagger,c_j`$ obey the canonical anticommutation relations. With $`J>0`$, $`0\leq g\leq g_{\max}`$ and a fixed cap $`g_{\max}`$, define

```math
h_g=J\sum_{j=1}^{N-1}
\left(e^g|j+1\rangle\langle j|+e^{-g}|j\rangle\langle j+1|\right),
\qquad
\widehat H_g=\sum_{i,j}(h_g)_{ij}c_i^\dagger c_j.
```

The target linear propagator on the $`m`$-particle sector is

```math
U_g(t)=e^{-it h_g},
\qquad
K_{N,m}(t)=e^{-it\widehat H_g}\big|_{\mathcal F_m}
=\bigwedge\nolimits^m U_g(t).
```

The equality follows by differentiating the action on exterior products; a finite check is included in the [verification suite](../verification/README.md). The space $`\mathcal F_m=\bigwedge^m\mathbb C^N`$ has dimension $`\binom Nm`$.

All asymptotic claims use fixed filling: for some fixed $`0\lt \nu\leq1/2`$,

```math
\nu N\leq m\leq(1-\nu)N.
```

The [dynamics theorem](dynamics.md) fixes one explicit time

```math
t_N=\frac{\alpha N}{J},
\qquad
\alpha=\frac{1}{3200\cosh g_{\max}}.
```

This is a theorem at that specified time, with an explicit finite-size remainder. It is not a lower bound at every time: at $`t=0`$ the target is the identity, and later recurrences need not incur the same cost. Native hopping amplitudes are bounded by $`J e^{g_{\max}}`$ independently of chain length.

## Quantum input and conditional output

One unknown normalized pure specimen $`|\psi\rangle\in\mathcal F_m`$ is supplied. The required target state is

```math
|\Psi_K(\psi)\rangle
=\frac{K|\psi\rangle}{\|K|\psi\rangle\|},
\qquad K=K_{N,m}(t_N).
```

The matrix $`K`$ is invertible. The normalization makes the requested state transformation nonlinear as a function of the supplied density operator. A physical implementation therefore includes its success probability; the normalized target by itself is not a trace-preserving quantum channel.

A simulator is a trace-nonincreasing completely positive success map $`\mathcal S`$. It may use arbitrary finite ancillas, measurements, feedback, discarded registers and success records. Its input-dependent success probability and conditional retained output are

```math
p_{\mathcal S}(\psi)=\mathrm{Tr}\mathcal S(|\psi\rangle\langle\psi|),
\qquad
\rho_{\mathcal S|\mathrm{succ}}(\psi)
=\frac{\mathcal S(|\psi\rangle\langle\psi|)}{p_{\mathcal S}(\psi)}.
```

For each promised input with positive success probability, require conditional half-trace error

```math
D\!\left(\rho_{\mathcal S|\mathrm{succ}}(\psi),
|\Psi_K(\psi)\rangle\langle\Psi_K(\psi)|\right)\leq\epsilon,
\qquad
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

Take a fixed $`0\lt \epsilon\lt 1/2`$ for the common statements. Define

```math
p^*_\epsilon(K;\mathcal P)
=\sup_{\mathcal S}\ \inf_{|\psi\rangle\in\mathcal P}
p_{\mathcal S}(\psi),
```

where the supremum is over maps satisfying the uniform conditional-error promise. A map with a zero-success promised input has worst-input success zero. Thus zero-probability branches cannot evade a converse.

This is a pure-input conditional-state criterion. It is not called diamond distance, and a positive approximation theorem is not silently extended to reference-entangled inputs or mixed Gaussian reductions. Lower bounds also apply to stronger tasks that include these pure test inputs.

## The two input promises

| Promise | Supplied quantum states | Supplied classical information |
|---|---|---|
| $`\mathcal P_{\mathrm{all}}`$ | Every pure state in $`\mathcal F_m`$, including correlated superpositions | Chain, time and particle number; no state description |
| $`\mathcal P_{\mathrm{Sl}}`$ | Every pure number-conserving Gaussian state, equivalently every $`m`$-particle Slater determinant | The same chain, time and particle number; occupied orbitals are unknown |

A Slater determinant has the form

```math
|Q\rangle
=a^\dagger(q_1)\cdots a^\dagger(q_m)|\mathrm{vac}\rangle,
\qquad Q^\dagger Q=I_m,
```

with orthonormal occupied orbitals $`q_1,\ldots,q_m`$. This promise does not supply $`Q`$ to the simulator. A convex mixture of Slaters is not covered by a pure-Slater positive theorem: normalized filtering reweights mixture components, so ordinary convexity does not prove the same guarantee.

## Central consequences

The [finite-size dynamics](dynamics.md), [general heralding theorem](heralding.md), [Gaussian converse](gaussian_converse.md) and [Gaussian approximation](gaussian_approximation.md) establish the following.

1. For arbitrary inputs, $`\log\kappa(K)=\Theta(gN^2)`$ up to the explicit negligible finite-size remainder. When $`gN^2\to\infty`$, optimal fixed-error worst-input success has order $`\exp[-\Theta(gN^2)]`$.
2. Unknown Slaters still require success $`\exp[-\Theta_g(N^2)]`$ at fixed positive $`g`$, and $`\exp[-\Theta_\beta(N)]`$ at $`g=\beta/N`$ with fixed $`\beta>0`$. The matching construction is a known singular-mode filter with paid synthesis precision.
3. A single input-independent Gaussian polar unitary approximates every unknown Slater with error at most $`\sqrt{\min(m,N-m)}\,g(N-1)`$.

In particular, choose $`g_N=N^{-7/4}`$. At the same filling and prescribed time, deterministic Slater error is $`O(N^{-1/4})\to0`$, whereas every fixed-error implementation covering arbitrary correlated inputs has worst-input success at most $`\exp[-cN^{1/4}]`$ for some fixed $`c>0`$ and all sufficiently large $`N`$. This explicit promise separation is the central physical consequence.

The complete intermediate Gaussian success-probability versus error tradeoff is not identified. A bound on the scale of nonvanishing success is distinct from a matching formula for that full tradeoff.

## What is charged, and what changes the task

The primary resource is heralding probability **per supplied unknown specimen**. Failure may destroy it. An expected repetition cost $`1/p`$ presupposes a source of fresh identical specimens, and coherent amplitude amplification presupposes additional preparation/reflection access; neither is supplied by this model.

The [implementation account](implementation.md) charges classical matrix preprocessing, basis rotations, helper preparation, measurements, classical records and finite gate precision. Polynomial logical work per attempt does not make an exponentially rare successful attempt efficient. Physical fault-tolerant overhead, noise thresholds and laboratory timing need an additional hardware model.

Known-state preparation, classical Gaussian simulation and estimation of selected local observables are distinct tasks. The [interpretation](interpretation.md) explains these boundaries, and the [related-work account](../references/RELATED_WORK.md) identifies inherited ingredients and the consequential addition.
