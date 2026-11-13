# Fermionic Nonunitarity Thresholds

**When can weak non-Hermitian evolution be reproduced reliably on an unknown many-fermion state?** The answer depends on the input promise. A single known Gaussian unitary can approximate every unknown Slater determinant in a regime where a processor covering arbitrary correlated inputs must have very small worst-case success.

The model is a known, uniform, open Hatano–Nelson chain with $`N`$ modes, bounded asymmetric hopping and a fixed particle density. The requested evolution is at one explicit time proportional to $`N`$. One unknown specimen is supplied; no occupied-orbital description, extra copies or preparation oracle is given. All converses allow arbitrary quantum processing.

## One transformation, two input promises

Set the hopping asymmetry to $`g_N=N^{-7/4}`$. At the same chain size, filling and prescribed time:

| Unknown input | Supported implementation guarantee |
|---|---|
| Every pure Slater determinant | One input-independent Gaussian unitary succeeds deterministically with trace error $`O(N^{-1/4})\to0`$. |
| Every correlated pure state in the fixed-number sector | Any processor with fixed small conditional trace error has worst-input success at most $`\exp[-cN^{1/4}]`$ for some $`c>0`$. |

The [model](science/model.md) states the precise promises. The [Gaussian approximation](science/gaussian_approximation.md) proves the positive result; [finite-time singular values](science/dynamics.md) and [heralding](science/heralding.md) prove the correlated-input obstruction.

## Thresholds and stronger-asymmetry regimes

For fixed filling and the specified ballistic time, the order of the asymmetry permitting nonvanishing fixed-error success is

```math
g_N\asymp N^{-3/2}\quad\text{for unknown pure Slaters},
\qquad
g_N\asymp N^{-2}\quad\text{for arbitrary correlated pure inputs}.
```

These are matched orders with accuracy- and success-dependent constants, rather than sharp crossover coefficients. The full intermediate Slater success-probability curve remains open.

A Slater promise does not make stronger filtering easy:

| Asymmetry regime | Optimal worst-input success on unknown Slaters |
|---|---|
| Fixed $`g>0`$ | $`\exp[-\Theta_g(N^2)]`$ |
| $`g_N=\beta/N`$, fixed $`\beta>0`$ | $`\exp[-\Theta_\beta(N)]`$ |

At $`g_N=\beta/N`$, single-particle conditioning stays bounded. The many-particle converse uses a hard family of genuine Slaters with ordinary orbital-rotation angles and permits non-Gaussian processors. Its [proof](science/gaussian_converse.md) reduces accurate processing to high-confidence decoding of hidden signs.

For unrestricted correlated inputs, the finite dynamics estimate gives $`\log\kappa(K)=\Theta(gN^2)`$ when the explicit remainder is negligible. Fixed-error heralding has order $`\exp[-\Theta(gN^2)]`$ when that exponent diverges. The finite statement, including $`g=0`$, appears in [dynamics](science/dynamics.md); it is not a claim of a positive exponent below the error scale.

## Read the science

| Question | Authoritative account |
|---|---|
| What quantum input, output and accuracy are required? | [Model and promises](science/model.md) |
| Why is the actual propagator ill conditioned at the chosen time? | [Finite-size dynamics proof](science/dynamics.md) |
| What can any heralded CP instrument accomplish? | [Exact and approximate heralding](science/heralding.md) |
| Does a Gaussian input promise avoid the converse? | [Slater hard family and discrimination](science/gaussian_converse.md) |
| Where does deterministic approximation become possible? | [Polar-unitary and variance proof](science/gaussian_approximation.md) |
| Are gates, helpers and rare-input precision charged? | [Implementation](science/implementation.md) |
| What changes physically, and which tasks are different? | [Interpretation](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [connected scientific route](science/README.md) and [LLM reading guide](llms.txt) give complementary entry points.

## Learn the result

The [learning route](learning/README.md) uses John Watrous, *The Theory of Quantum Information* (2018), as its educational anchor. Start with the [source bridge](learning/WATROUS_BRIDGE.md) and the [four-mode worked experiment](learning/WORKED_EXAMPLE.md), then follow the [30 dependency-ordered milestones](learning/MILESTONES.md) through the complete argument.

## Reproduce the finite checks

```sh
python -m pip install -r verification/requirements.txt
python verification/run_checks.py
```

The [verification guide](verification/README.md) identifies the tested matrix, Fock-space, discrimination and approximation identities and their limits. Finite checks support the analytical arguments; they do not prove asymptotic statements or certify priority.

## Scope and attribution

The positive approximation theorem concerns **pure number-conserving Slaters**. It does not extend by convexity to mixtures, because normalization changes mixture weights. The comparison concerns whole-output conditional trace accuracy, rather than a selected observable or a complete-channel diamond guarantee.

Failure may consume the unknown payload. Interpreting inverse success as a repetition cost requires fresh identical specimens. Known-state preparation and classical Gaussian simulation have different access and output requirements. No computational speedup or impossibility of observing Fermi skin is asserted.

Large Fock-space eigenvector conditioning, imaginary-gauge scales, probabilistic state separation and SVD-based fermionic circuits are prior results. The [comparison](references/RELATED_WORK.md) identifies the added fixed-time, fixed-error input-promise boundary and credits those foundations.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
