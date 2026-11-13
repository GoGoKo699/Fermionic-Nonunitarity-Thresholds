# A deterministic approximation for unknown Slater inputs

The input promise changes the operational task. A single known Gaussian unitary approximates the normalized non-Hermitian transformation on **every unknown pure Slater determinant** when $`gN^{3/2}`$ is small. The same approximation need not work on correlated states or mixtures of Slaters.

## Definitions

Let $`U=\exp(-it h_g)`$ be the known one-particle propagator of the [model](model.md), and let

```math
K=\bigwedge^m U
```

act on the sector of exactly $`m`$ fermions. A normalized pure Slater determinant has the form

```math
|\Psi\rangle=v_1\wedge\cdots\wedge v_m,
\qquad \langle v_i,v_j\rangle=\delta_{ij}.
```

Its occupied one-particle projector is $`P=\sum_{j=1}^m|v_j\rangle\langle v_j|`$. Write $`\Gamma_m(W)=\bigwedge^m W`$ for a number-preserving Gaussian unitary. All trace distances below use the half-trace convention

```math
D_{\rm tr}(\rho,\sigma)=\frac12\Vert \rho-\sigma\Vert _1.
```

The input is supplied as a quantum specimen. The simulator is not given its occupied orbitals or a classical state description.

## The uniform pure-Slater bound

Take the one-particle polar decomposition

```math
U=W e^B,
\qquad W^\dagger W=I,
\qquad B=\log|U|=B^\dagger.
```

For every pure $`m`$-fermion Slater $`\Psi`$,

```math
\boxed{
D_{\rm tr}\!\left(
 \Gamma_m(W)|\Psi\rangle\langle\Psi|\Gamma_m(W)^\dagger,
 \frac{K|\Psi\rangle\langle\Psi|K^\dagger}{\Vert K\Psi\Vert ^2}
\right)
\le
\min\!\left\{1,\sqrt{\min(m,N-m)}\,\Vert B\Vert \right\}.
}
```

This is a deterministic channel: apply $`\Gamma_m(W)`$ and always return the output. It works uniformly without learning the input Slater.

For the open Hatano–Nelson chain, the exact gauge relation is

```math
U=S_g U_0 S_g^{-1},
\qquad
S_g=\mathrm{diag}(e^g,e^{2g},\ldots,e^{Ng}),
```

with $`U_0`$ unitary. Hence

```math
\Vert U\Vert ,\ \Vert U^{-1}\Vert \le e^{g(N-1)},
\qquad
\Vert B\Vert \le g(N-1).
```

Therefore the deterministic worst-Slater error obeys

```math
\boxed{\epsilon_{\rm Slater}
\le
\min\!\left\{1,\sqrt{\min(m,N-m)}\,g(N-1)\right\}.}
```

No assumption about a special occupied momentum band or a particular initial density profile enters this bound.

### Proof

Second quantization gives

```math
K=\Gamma_m(W)e^{\widehat B},
\qquad
\widehat B=d\Gamma(B)=\sum_{i,j}B_{ij}c_i^\dagger c_j.
```

Consider the normalized path

```math
|\Phi_s\rangle
=\frac{e^{s\widehat B}|\Psi\rangle}
       {\Vert e^{s\widehat B}\Psi\Vert },
\qquad 0\le s\le1.
```

Every $`\Phi_s`$ remains a pure Slater: the invertible one-particle map $`e^{sB}`$ acts on each occupied orbital, and normalization restores an orthonormal occupied basis. Differentiating the normalized vector yields

```math
\frac{d}{ds}|\Phi_s\rangle
=\bigl(\widehat B-\langle\widehat B\rangle_s\bigr)|\Phi_s\rangle.
```

With the Fubini–Study distance defined as $`\arccos|\langle\phi|\psi\rangle|`$, the path speed is $`\sqrt{\mathrm{Var}_{\Phi_s}(\widehat B)}`$. Wick's identity for a pure Slater with occupied projector $`P_s`$ gives

```math
\mathrm{Var}_{\Phi_s}(d\Gamma(B))
=\mathrm{Tr}\bigl[P_sB(I-P_s)B\bigr]
=\Vert (I-P_s)BP_s\Vert _{\rm HS}^2.
```

The matrix on the right has rank at most both $`m`$ and $`N-m`$, and operator norm at most $`\Vert B\Vert `$. Thus

```math
\mathrm{Var}_{\Phi_s}(d\Gamma(B))
\le \min(m,N-m)\Vert B\Vert ^2.
```

The endpoint Fubini–Study angle is at most the integrated path length. The half-trace distance between two pure states equals the sine of that angle and is at most the angle itself. Integration over $`s\in[0,1]`$ proves the claim, and applying the common unitary $`\Gamma_m(W)`$ leaves the distance unchanged.

## Deterministic sufficiency for arbitrary pure inputs

For comparison, the same polar unitary has a weaker bound on the full fixed-number pure-state space. Put $`D=d\Gamma(B)`$. The normalized filtering path has speed $`\sqrt{\mathrm{Var}(D)}`$ for every pure state. The elementary estimates $`\Vert D\Vert \leq m\Vert B\Vert `$ and $`\mathrm{Var}(D)\leq\Vert D\Vert ^2`$ therefore give

```math
D_{\mathrm{tr}}\!\left(
\Gamma_m(W)|\psi\rangle\langle\psi|\Gamma_m(W)^\dagger,
\frac{K|\psi\rangle\langle\psi|K^\dagger}{\Vert K\psi\Vert ^2}
\right)
\leq\min\{1,m g(N-1)\}.
```

This paragraph uses neither Wick's rule nor a Gaussian promise. Thus a sufficiently small accuracy-dependent multiple of $`N^{-2}`$ permits deterministic uniform approximation on all pure inputs at fixed filling. The [heralding converse](heralding.md) proves necessity in order for nonvanishing fixed-error success. The Slater variance bound improves the sufficient scale to $`N^{-3/2}`$; the [Slater converse](gaussian_converse.md) proves the corresponding necessity. These are order statements with constants depending on the fixed accuracy and success, not sharp crossover coefficients.

## A strict separation of input promises

Fix a filling bounded away from zero and one and use the ballistic time of the propagation theorem. The [conditioning result](dynamics.md) and [heralding bound](heralding.md) imply that universal fixed-error simulation on arbitrary unknown states has worst-input success at most

```math
p_{\rm all}\le C_\epsilon\exp[-c\,g_NN^2]
```

when $`g_NN^2`$ grows. In the window

```math
N^{-2}\ll g_N\ll N^{-3/2},
```

that universal success vanishes faster than a constant, while the deterministic Slater error above tends to zero. An explicit choice is

```math
g_N=N^{-7/4}:
\qquad
\epsilon_{\rm Slater}=O(N^{-1/4}),
\qquad
p_{\rm all}\le C_\epsilon e^{-cN^{1/4}}.
```

The statements compare the same known Hamiltonian, time, filling and returned-state error convention. The difference is whether the unknown input is promised to be a pure Slater. They establish a process-simulation distinction; they do not assert a computational advantage over classical Gaussian simulation.

The Gaussian promise does not make the task easy at every nonreciprocity. At $`g_N=\beta/N`$ with fixed $`\beta>0`$, the [Gaussian-input converse](gaussian_converse.md) still forces exponentially small worst-Slater success at fixed error. No matching complete Gaussian frontier between these regimes is claimed.

## Why the theorem does not extend by convexity

The target $`\rho\mapsto K\rho K^\dagger/\mathrm{Tr}(K\rho K^\dagger)`$ reweights mixture components. It is not an affine map of the input state, so the pure-Slater bound cannot simply be averaged.

For a direct counterexample, let $`x,y`$ be the minimum and maximum right singular Slaters of $`K`$, and let $`\kappa=\sigma_{\max}(K)/\sigma_{\min}(K)`$. For

```math
\rho=\frac12\bigl(|x\rangle\langle x|+|y\rangle\langle y|\bigr),
```

$`\Gamma_m(W)\rho\Gamma_m(W)^\dagger`$ retains equal weights on the corresponding left singular rays. The normalized filtered mixture instead has weights $`1/(1+\kappa^2)`$ and $`\kappa^2/(1+\kappa^2)`$. Their half-trace distance is

```math
\frac{\kappa^2-1}{2(\kappa^2+1)},
```

which tends to one half as $`\kappa\to\infty`$. Thus even the convex hull of pure Slaters is outside this deterministic approximation theorem. Reference-entangled inputs, extra copies, state-learning strategies and input descriptions are also separate promises.

## Implementation and scope

The polar factor is a known $`N\times N`$ unitary. Its classical precomputation, finite-precision orbital rotations and their synthesis are charged in the [implementation account](implementation.md). The guarantee above is for ideal logical operations; a specified circuit approximation adds its own trace error.

The proof uses standard polar decomposition, fermionic second quantization, Wick variance and pure-state geometry. The contribution here is the uniform unknown-input consequence in the stated chain and its comparison with the separately proved universal heralding law. It does not identify a new Gaussian compilation primitive or claim an optimal intermediate Gaussian crossover.
