# Reproduce the finite scientific checks

From the repository root, use Python with the pinned numerical dependencies:

```sh
python -m pip install -r verification/requirements.txt
python verification/run_checks.py
```

The script raises an assertion on a failed scientific identity or inequality and otherwise writes [results.json](results.json). It uses a fixed random seed, records its own SHA-256 and the NumPy/SciPy versions, and emits no timestamps, elapsed-time measurements or machine-specific paths. In the pinned environment, repeated runs produce the same JSON bytes. The computation is small: the largest direct many-body matrix has dimension twenty, and the illustrative one-particle matrix has size sixty-four.

## What is checked

| Check | Failure mode addressed | Finite scope |
|---|---|---|
| Open/periodic Taylor comparison | A hidden bulk difference, an incorrect rank count, a missing exponential tail, or the wrong singular-value interlacing direction | Nontrivial polynomial degrees on 9, 12 and 16 sites; one additional evaluation uses the actual conservative theorem time on 24 sites |
| Exterior power versus direct fermionic evolution | An incorrect exterior-power convention or a fermionic creation/annihilation sign | Minor determinants compared with an independent CAR-sign construction and direct Fock-space exponentiation on 4–6 modes; reciprocal singular pairing and the condition-number identity checked |
| Particle and hole helper filters | A missing normalization for singular values above one, an incorrect auxiliary occupation, or a wrong full-sector success bound | Explicit two-mode beam-splitter accepted blocks, followed by the full SVD-basis filter on finite number sectors; half-filling optimal normalization also checked |
| Wick variance and polar approximation | A missing occupied/unoccupied projector, an incorrect distance convention, or loss of the Slater promise along the positive path | Direct Fock-space variance versus the Wick expression at three path positions; random Slaters and the uniform polar trace bound on 4–6 modes |
| Slater discrimination family | A non-Slater witness, nonorthogonal ideal outputs, invalid collective-discrimination multiplication, or a rejected-outcome loophole in the finite confidence inequalities | Eight hard Slaters from three singular-mode pairs; explicit tensor SDP-dual PSD tests and attained product Helstrom value; nine feasible covariant seeds for the positivity, Cauchy-splitting and confidence bounds |
| Weak-asymmetry illustration | Confusion between bounded one-particle conditioning and the fixed-filling exterior product | One-particle singular values at $`g=1/N`$ for $`N=12,24,36,48,64`$; reciprocal pairing and gauge upper bounds checked |

The direct Fock-space Hamiltonian is assembled from creation/annihilation action and its signs. It is not produced by differentiating the minor-determinant implementation. The helper check includes both empty-helper particle attenuation and occupied-helper hole attenuation. The discrimination check includes exact unambiguous and high-confidence-with-rejection seeds, as well as general positive covariant seeds.

## How to read the output

The JSON records individual parameters and worst residuals. Equality residuals use an absolute assertion tolerance of $`5\times10^{-10}`$; observed residuals are typically much smaller. Inequality fields called `excess` report the maximum positive violation, with zero indicating none among the tested cases. Some tiny signed eigenvalues near zero are floating-point roundoff, not evidence of negative semidefiniteness.

The weak-asymmetry table deliberately uses the illustrative time coefficient $`0.15`$, which is much larger than the conservative coefficient in the proof. Its entries are explicitly marked `uses_conservative_theorem_time: false`. They illustrate finite conditioning at those specified times and do not validate the theorem's asymptotic lower exponent or replace its stated time. The boundary-comparison group separately evaluates the exact theorem time once, while its other cases test the finite-degree lemma with nonzero boundary rank.

## What these computations do not establish

The [dynamics](../science/dynamics.md), [heralding](../science/heralding.md), [Gaussian converse](../science/gaussian_converse.md), [polar approximation](../science/gaussian_approximation.md) and [implementation](../science/implementation.md) contain the analytical arguments. Finite matrix computations do not prove an all-size law, certify external novelty, determine sharp crossover constants, or establish a physical fault-tolerance overhead.

The sampled covariant seeds do not optimize every possible inconclusive discriminator. Their purpose is to test the finite inequalities and the hard-family construction against independently computed matrices. The script also does not model an experiment with an irreplaceable unknown input, calculate laboratory runtime, or treat a Gaussian classical state description as available to the unknown-input processor.

Double precision is adequate for these modest, explicitly bounded conditioning regimes. The script does not use large fixed-positive-asymmetry chains whose exponentially ill-conditioned matrices would make ordinary floating-point results unreliable.
