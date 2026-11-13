# What the propagation thresholds mean

The physical task is to receive one unknown fermionic specimen and return its normalized non-Hermitian evolution. A classical description of the input is not supplied. Reliable processing therefore has to preserve the input's quantum information; calculating a density profile or preparing a classically specified output is a different task.

## The same transformation, different promises

Consider the known open chain, fixed filling and specified time in the [model](model.md). In the window

```math
N^{-2}\ll g_N\ll N^{-3/2},
```

the polar unitary has vanishing error on **every pure Slater input**. Its action is fixed by the known propagator, independent of the unknown occupied orbitals. On the same chain, every processor accurate on **all correlated pure inputs** has worst-input success tending to zero.

The example $`g_N=N^{-7/4}`$ makes both sides explicit:

| Promised input | Implementation consequence |
|---|---|
| Unknown pure Slater | A deterministic Gaussian unitary has trace error $`O(N^{-1/4})`$. |
| Arbitrary correlated fixed-number pure state | Fixed conditional error forces worst-input success at most $`\exp[-cN^{1/4}]`$. |

This is an approximate input-promise separation. The Slater statement is stronger than a known-state preparation recipe: the processor does not learn or receive the occupied orbitals. The correlated-input converse allows the processor arbitrary controls, including non-Gaussian ones.

## Why correlations affect the boundary

In polar coordinates $`U=W e^B`$, the nonunitary part on the fixed-number sector is $`e^{d\Gamma(B)}`$. The one-particle logarithmic distortion has size at most $`g(N-1)`$. For a Slater, Wick's rule bounds the variance of $`d\Gamma(B)`$ by $`\min(m,N-m)\Vert B\Vert ^2`$. The resulting normalized-state path has length at most $`\sqrt{\min(m,N-m)}\,g(N-1)`$.

An arbitrary correlated superposition is not constrained by this Slater variance law. The extremal-singular-vector test in [heralding](heralding.md) can turn two almost parallel inputs into orthogonal targets. A physical instrument can accomplish that separation only with a correspondingly small success probability. The [dynamics proof](dynamics.md) establishes enough singular spread at an actual prescribed time for this argument to be consequential.

These ingredients locate nonvanishing-success asymmetry scales of order $`N^{-3/2}`$ for Slaters and $`N^{-2}`$ for unrestricted correlated inputs, at fixed accuracy and success conventions. They do not identify the entire Gaussian probability-versus-error curve or its sharp crossover constants.

## Gaussian inputs also encounter a real barrier

A Gaussian promise does not make every nonunitary transformation easy on an unknown specimen. At $`g_N=\beta/N`$, with fixed $`\beta>0`$, one-particle conditioning is bounded at every time, but optimal fixed-filling unknown-Slater success is $`\exp[-\Theta_\beta(N)]`$ at the specified time. At fixed positive asymmetry it is $`\exp[-\Theta_g(N^2)]`$.

The [Slater converse](gaussian_converse.md) uses independent hidden signs in disjoint orbital pairs. Every input and ideal output is a Slater. A successful accurate processor would decode an entire secret string with high confidence; quantum discrimination bounds limit how frequently it can do so. At $`g_N=\beta/N`$ the preparation angles are ordinary constants, and the final scoring measurement is an orbital change followed by occupation readout.

## Relation to existing skin-effect and circuit results

Large Fock-space eigenvector conditioning and the $`g m(N-m)`$ imaginary-gauge scale were already established in the skin-effect literature. Polynomial-size exterior-power/SVD circuits are also prior constructions. The [related-work comparison](../references/RELATED_WORK.md) credits them explicitly.

The present account concerns singular values of the **propagator at a specified finite time**, arbitrary physical heralded implementations at fixed conditional error, and the distinction between unknown-input promises. Large eigenvector conditioning alone does not imply that every promised input needs rare postselection. The deterministic Slater window is an explicit reason to keep those statements separate.

The obstruction is not a topological invariant. A periodic comparison is part of the proof, and similar amplification can occur without open-boundary skin localization. No statement here excludes observing Fermi skin, unconditional feedback dynamics, or preparing the output of a particular known initial state.

## Specimens, descriptions and repeated access

| Available access | What the present claims establish |
|---|---|
| One unknown specimen | The stated conditional-output and worst-success laws apply. Failure may consume the payload. |
| Classical occupied-orbital description of a Slater | Calculate the transformed occupied subspace and prepare it directly; this is not the unknown-input task. |
| Fresh identical specimens | Repeated attempts may be counted, with their preparation charged. Inverse success is then a sampling overhead. |
| Coherent preparation and reflection access | Amplitude-amplification algorithms have additional resources; the single-specimen CP converse does not price that access model. |
| Only selected local observables requested | Full-state propagation accuracy is unnecessary; the present converses do not establish an observable-estimation lower bound. |

Efficient classical description and simulation of a supplied Gaussian model do not provide the missing description of an unknown physical specimen. Conversely, no computational speedup over classical simulation is claimed. The contribution is a physical state-transformation limit and a constructive approximation under explicit promises.

## Remaining scientific boundary

The full intermediate Slater success-probability frontier remains unresolved. The matched strong/weak-asymmetry regimes, the nonvanishing-success scales and the explicit deterministic-versus-rare promise separation do not require solving it. Disorder, interactions, pairing, mixed-input promises, arbitrary retained-reference guarantees and hardware noise require their own models and arguments.
