# Paid compilation and conditional accuracy

The heralding laws concern success probability, but a matching construction must also have a finite, explicitly charged circuit. Here the one-particle matrix is known and has size $`N\times N`$. Dense classical linear algebra, Gaussian orbital rotations, helper preparation, measurements and the precision needed on rare inputs all count. No QRAM, unknown-state description or free data-loading oracle is assumed.

## Inherited circuit primitive

An SVD followed by one-mode nonunitary factors is an established fermionic construction. Zhu, Bierman, Lu and Li, *Quantum circuit for non-unitary linear transformation of basis sets*, npj Quantum Information **11**, 198 (2025), develop an exterior-algebra/SVD circuit with quadratic gate count, linear depth in their circuit model and approximately one helper per orbital ([paper](https://doi.org/10.1038/s41534-025-01145-3), [arXiv:2502.08962](https://arxiv.org/abs/2502.08962)). Gaussian orbital changes by Givens rotations are also standard; see Kivlichan et al., *Quantum Simulation of Electronic Structure with Linear Depth and Connectivity*, Physical Review Letters **120**, 110501 (2018), for the linear-connectivity construction ([paper](https://doi.org/10.1103/PhysRevLett.120.110501), [arXiv:1711.04789](https://arxiv.org/abs/1711.04789)). These compilation ideas are credited as prior work.

The account below applies that primitive to the present propagator, accommodates singular values above one using hole attenuation, and supplies a conservative finite-precision budget for **uniform conditional** output accuracy. Quadratic per-attempt gate count does not remove the separately charged heralding probability.

## An explicit Gaussian success operator

Take an SVD of the known one-particle propagator,

```math
U=V\mathrm{diag}(s_1,\ldots,s_N)R^\dagger,
\qquad s_j>0.
```

In the occupation basis of its right singular modes, use the one-mode filters

```math
f_j=
\begin{cases}
\mathrm{diag}(1,s_j),&s_j\le1,\\
\mathrm{diag}(s_j^{-1},1),&s_j>1.
\end{cases}
```

Both are contractions. A concrete number-preserving realization uses one auxiliary fermionic mode and a beam splitter:

- For $`s_j\le1`$, initialize the helper empty, use beam-splitter amplitude $`s_j`$, and accept only if it is still empty.
- For $`s_j>1`$, initialize the helper occupied, use beam-splitter amplitude $`s_j^{-1}`$, and accept only if it is still occupied.

The second operation attenuates a hole. On success every helper returns to its supplied occupation; on failure the attempt is discarded. Preparing the helpers again is part of another attempt.

Let

```math
C=\prod_{j=1}^N\max(1,s_j).
```

Apply $`\Gamma(R^\dagger)`$, all the filters, and then $`\Gamma(V)`$. The joint accepted Kraus operator on full Fock space is

```math
F=\frac{\Gamma(U)}{C},
```

so on the fixed-number sector it is $`F_m=K/C`$. The conditional output is exactly the desired normalized $`K`$ output for every input of that sector. This construction is valid on arbitrary correlated inputs, not only on Slaters.

### A uniform success bound

Put

```math
a=g(N-1),\qquad
\Lambda=(N+m)a,\qquad
\mu=e^{-\Lambda}.
```

The gauge bound gives $`e^{-a}\le s_j\le e^a`$. Consequently

```math
1\le C\le e^{Na},\qquad
\sigma_{\min}(K)\ge e^{-ma},\qquad
\sigma_{\min}(F_m)\ge\mu.
```

Thus every input succeeds with probability at least

```math
p_F\ge e^{-2\Lambda}=\exp[-O(gN^2)].
```

Together with the lower bounds, this suffices for the matching exponential order and the universal polynomial-success crossover. It does not claim that $`C`$ is the optimal normalization for every filling. At half filling, reciprocal singular-value pairs make $`C`$ equal to the product of the largest $`m`$ singular values, so this filter attains the exact optimal normalization. The abstract exact optimum at other fillings is established separately; an optimal-normalization circuit is unnecessary for the matching-order resource statement.

## Logical resources per attempt

| Resource | Charged amount and convention |
|---|---|
| Supplied input | One unknown $`m`$-fermion state on $`N`$ modes; no state description and no extra copies |
| Known classical data | Explicit banded Hamiltonian and requested time/accuracy, read and processed classically |
| Dense classical work | Form the $`N\times N`$ propagator, compute a backward-accurate SVD, and factor the orbital unitaries; polynomial in $`N`$ and the charged precision |
| Data register | $`N`$ occupation qubits under Jordan–Wigner encoding |
| Helpers | At most $`N`$ empty or occupied auxiliary modes, prepared and measured in the occupation basis |
| Ideal continuous logical gates | $`O(N^2)`$ Givens/phase rotations for the orbital changes and $`O(N)`$ filter rotations |
| Finite gate alphabet | $`O(N^2P)`$ elementary logical gates using standard $`O(P)`$-cost single-angle synthesis, with $`P=O(gN^2+\log(N/\epsilon))`$ below |
| Repetition | Count failed attempts; inverse success is a sampling overhead only when the input source can be prepared again |

Adjacent-mode Givens rotations have constant-size occupation-qubit realizations. Their usual nearest-neighbor decomposition avoids an uncharged long Jordan–Wigner string. If a data/helper pair is not adjacent in the chosen ordering, an $`O(N^2)`$ fermionic-swap network can bring the pairs together and restore the ordering, preserving the quoted gate-count order. Any further hardware-specific routing, measurement latency, reset duration or fault-tolerant physical-qubit overhead must be added for the chosen architecture. No laboratory runtime or hardware crossover is inferred from this logical account.

## Why rare inputs require more precision

Absolute approximation to a subnormalized operator is not automatically conditional accuracy. If $`\widetilde F_m`$ is one accepted Kraus operator with

```math
\Vert \widetilde F_m-F_m\Vert \le\delta,
```

then for any unit vector $`\psi`$,

```math
\left\Vert 
\frac{\widetilde F_m\psi}{\Vert \widetilde F_m\psi\Vert }
-
\frac{F_m\psi}{\Vert F_m\psi\Vert }
\right\Vert 
\le\frac{2\delta}{\Vert F_m\psi\Vert }
\le\frac{2\delta}{\mu}.
```

The pure-state half-trace distance is no larger than this vector-norm bound. Choosing, for example,

```math
\delta=\frac{\epsilon\mu}{8}
```

leaves margin for conditional error $`\epsilon`$ on **all** inputs. The implemented success probability is at least $`(\mu-\delta)^2`$, so the same exponential order survives.

The required accuracy can be exponentially small, but its bit cost is

```math
\log(1/\delta)
=\Lambda+\log(8/\epsilon)
=O\!\left(gN^2+\log(1/\epsilon)\right).
```

It is polynomial precision for the bounded-$`g`$, ballistic-time families considered here. Calling the per-attempt circuit polynomial must include this cost.

## Backward-accurate SVD is sufficient

Exact singular vectors and a promise of separated singular values are unnecessary. Compute positive $`\widetilde s_j`$ and unitaries $`\widetilde V,\widetilde R`$ for which

```math
\widehat U
=\widetilde V\mathrm{diag}(\widetilde s_j)\widetilde R^\dagger,
\qquad
\Vert \widehat U-U\Vert \le\eta.
```

This is an approximate factorization of the matrix itself. Degenerate singular subspaces may use any orthonormal basis. Let $`\widehat C=\prod_j\max(1,\widetilde s_j)`$ and let $`\widehat F_m=\bigwedge^m\widehat U/\widehat C`$ be its exact filter.

For $`\eta\le1/(2N)`$, telescoping the tensor products and restricting to the exterior sector gives

```math
\left\Vert \bigwedge^m\widehat U-\bigwedge^mU\right\Vert 
\le m\max(\Vert U\Vert ,\Vert \widehat U\Vert )^{m-1}\eta
\le N e^{am+1}\eta.
```

Singular-value perturbation gives $`|\widetilde s_j-s_j|\le\eta`$. The scalar function $`s\mapsto\log\max(1,s)`$ is one-Lipschitz on $`[0,\infty)`$, hence

```math
|\log\widehat C-\log C|\le N\eta,
\qquad
|C/\widehat C-1|\le2N\eta.
```

Because $`\Vert F_m\Vert \le1`$ and $`\widehat C\ge1`$,

```math
\boxed{
\Vert \widehat F_m-F_m\Vert 
\le N(e^{am+1}+2)\eta.
}
```

A sufficient precomputation choice is

```math
\eta\le
\min\!\left\{
\frac1{2N},\ \frac{e^{-a}}4,
\frac{\delta}{2N(e^{am+1}+2)}
\right\}.
```

This spends at most $`\delta/2`$ of the accepted-operator error. The remaining $`\delta/2`$ is assigned to coherent gate synthesis. For $`G=O(N^2)`$ elementary continuous rotations, operator-norm error at most $`\delta/(2G)`$ per gate is sufficient by telescoping the unitary circuit and then taking its accepted block.

The required matrix and rotation bit lengths are therefore bounded by

```math
P=O\!\left(gN^2+\log(N/\epsilon)\right),
```

with conservative guard bits included. Computing filter angles near zero or one may require increasing the amplitude precision by a constant factor; it does not change this order.

### Classical specification and computation

The polynomial statement assumes that the known real parameters are supplied with an explicit finite description from which the required coefficients can be computed to $`P`$ bits in polynomial time. Reading that description counts. One explicit route avoids diagonalizing an ill-conditioned non-Hermitian eigenbasis: diagonalize the Hermitian open chain by its known sine matrix,

```math
T_{jk}=\sqrt{\frac{2}{N+1}}\sin\frac{\pi jk}{N+1},
\qquad
E_k=2J\cos\frac{\pi k}{N+1},
\qquad
U_g=S_g T\mathrm{diag}(e^{-itE_k})T^\mathsf{T}S_g^{-1}.
```

The unit-modulus phases at $`t=O(N/J)`$ require logarithmic-in-$`N`$ argument guard bits. Sums have only $`N`$ bounded terms, and the largest gauge ratio is $`e^a`$, so $`O(a+\log N)`$ additional absolute-accuracy guard bits suffice. These are included in the displayed precision order. Polynomial-precision dense SVD and Givens factorization then use polynomial classical time and memory in $`N`$, $`P`$ and the input description length. An unscaled Taylor summation with uncontrolled cancellation is not assumed, in particular at $`g=0`$.

This is neither an oracle for an unknown matrix nor a claim that arbitrary uncomputable real couplings can be loaded. The circuit can be prepared anew for each explicitly specified $`N,g,t`$; the unknown quantum input itself is never classically reconstructed.

## Deterministic polar-unitary compilation

For the [pure-Slater approximation](gaussian_approximation.md), compile only $`\Gamma_m(W)`$, where $`W`$ is the known one-particle polar factor. If $`\widetilde W`$ is unitary and $`\Vert \widetilde W-W\Vert \le\xi`$, then

```math
\left\Vert \bigwedge^m\widetilde W-\bigwedge^mW\right\Vert \le m\xi.
```

Thus an additional output tolerance $`\zeta`$ is met by one-particle unitary accuracy $`O(\zeta/m)`$ and a corresponding gate-synthesis budget. Invertibility with $`\sigma_{\min}(U)\ge e^{-a}`$ controls the polar computation; arbitrary singular-value gaps need not be resolved. Polynomial-precision matrix arithmetic and $`O(N^2)`$ Givens rotations give a polynomial circuit. It always succeeds and uses no nonunitary filter or postselection helpers.

Its total error is the analytical Slater bound plus the selected compilation tolerance. In the separation window, a tolerance tending to zero, such as $`\zeta=N^{-1/4}`$ for $`g=N^{-7/4}`$, preserves the claimed vanishing-error order.

## Limits of the accuracy and cost account

The gate-synthesis estimate models coherent logical-unitary approximation, for which the accepted branch is still one Kraus operator. If an implementation instead has a general process error of diamond norm $`\eta_{\rm proc}`$, conditioning can amplify that error by order $`1/p`$. A sufficient uniform budget is then $`\eta_{\rm proc}=O(\epsilon\mu^2)`$, rather than $`O(\epsilon\mu)`$. Its logarithmic precision remains polynomial, but realizing it on noisy hardware requires an explicit fault-tolerance analysis.

A single irreplaceable unknown specimen may be lost on failure. Neither the exact filter nor a small per-attempt circuit gives a deterministic simulator for that specimen. Conversely, a classical description of a particular Slater permits deterministic input-dependent output preparation, which is a different access model and is not ruled out by the success converse.
