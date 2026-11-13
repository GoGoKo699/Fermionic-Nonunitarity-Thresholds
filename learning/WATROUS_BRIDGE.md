# From Watrous to fermionic nonunitarity thresholds

The educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's official source page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies the standard-layout 2018 manuscript and its table of contents. The locators below were checked against that version. Section and theorem numbers are the preferred locators if pagination differs in another printing.

This bridge translates the source's finite-dimensional information tools into the project's unknown-input experiment. The fermionic chain, exterior powers, Slater variance identity and asymmetry thresholds are supplied by the scientific account here; they are not attributed to the textbook.

## A focused source map

| Verified source locator | Tool to bring into this project | Where it is used |
|---|---|---|
| §1.1.3, p.24, [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=24) | Singular values, positive operators and operator norms | [Propagator conditioning](../science/dynamics.md) and [SVD filters](../science/implementation.md) |
| §1.2.3, p.53, [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf#page=53) | Semidefinite-program dual bounds | [Collective sign discrimination](../science/gaussian_converse.md#product-helstrom-bound) |
| §2.1.2, p.61, [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=4) | Pure states and density operators | [The two quantum input promises](../science/model.md#the-two-input-promises) |
| §2.2.2, p.77, [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=20) | Completely positive maps and Kraus representations | [The general success instrument](../science/heralding.md) |
| §2.3.1, p.100, [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf#page=43) | Measurements described by positive effects | [Success followed by sign decoding](../science/gaussian_converse.md#from-accurate-processing-to-discrimination) |
| §3.1.1, p.125; Theorem 3.4, p.128, [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=5) | Binary minimum-error discrimination | [One singular-mode pair](../science/gaussian_converse.md#product-helstrom-bound) |
| §3.1.2, p.132, [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=9) | Discrimination of a state ensemble | [The full hidden sign string](../science/gaussian_converse.md) |
| §3.2, Definition 3.11, p.139; §3.2.3, Theorem 3.27, p.156, [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=33) | Root fidelity and its channel monotonicity | [The two-input heralding converse](../science/heralding.md) |
| §3.3.2, p.166, [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf#page=43) | Completely bounded trace norm | A comparison convention: [our main target is conditional pure-state accuracy](../science/model.md#quantum-input-and-conditional-output), not a diamond-norm claim |

The [verified front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf#page=2) provides the chapter/section navigation. These links point to the author's copies; no textbook copy is redistributed in this repository.

## Translate the notation before using a theorem

| Source notation | Notation and convention here |
|---|---|
| A unit vector $`u`$ and its pure-state operator $`uu^*`$ | $`\lvert\psi\rangle`$ and $`\lvert\psi\rangle\langle\psi\rvert`$ |
| Adjoint $`A^*`$ | $`A^\dagger`$ |
| Trace norm $`\Vert X\Vert _1`$ | The state distance is $`D(\rho,\sigma)=\frac12\Vert \rho-\sigma\Vert _1`$ |
| Fidelity $`F(P,Q)`$ in Definition 3.11 | Root fidelity $`\Vert \sqrt P\sqrt Q\Vert _1`$, without squaring |
| A measurement effect | Distinguish an effect $`E`$ from an accepted Kraus operator $`F`$: its success effect is $`F^\dagger F`$ |

For two pure states, the conventions imply

```math
F(\psi,\phi)=|\langle\psi|\phi\rangle|,
\qquad
D(\psi,\phi)=\sqrt{1-|\langle\psi|\phi\rangle|^2}.
```

A reported overlap of $`0.9`$ is therefore root fidelity $`0.9`$, squared fidelity $`0.81`$, and trace distance $`\sqrt{0.19}`$. The [worked example](WORKED_EXAMPLE.md) keeps these values separate.

## Bridge 1: a normalized filter is a conditional experiment

The project specifies a known invertible many-body operator $`K`$ and asks for the normalized ray $`K\psi/\|K\psi\|`$. That formula does not describe a deterministic linear channel.

Choose an accepted operator $`F=K/C`$ with $`F^\dagger F\preceq I`$, and set $`G=\sqrt{I-F^\dagger F}`$. A complete physical description can retain a classical flag:

```math
\mathcal T(\rho)
=|s\rangle\langle s|\otimes F\rho F^\dagger
 +|f\rangle\langle f|\otimes G\rho G^\dagger.
```

It is trace preserving because $`F^\dagger F+G^\dagger G=I`$. The accepted branch has probability

```math
p_\psi=\|F\psi\|^2.
```

Only after conditioning on that branch does the desired normalized output appear. Keeping the failure branch is essential when applying information monotonicity: throwing it away and declaring every attempt successful changes the experiment.

The [heralding proof](../science/heralding.md) chooses two inputs that are close before filtering but have orthogonal target outputs. It applies information monotonicity to the **complete flagged channel**. Its conclusion bounds what any CP success map can do, even if it uses a more elaborate circuit than this one-Kraus construction.

## Bridge 2: the state space grows, while the one-particle data stay small

For $`N`$ fermionic modes and exactly $`m`$ particles,

```math
\mathcal F_m=\bigwedge^m\mathbb C^N,
\qquad
\dim\mathcal F_m=\binom Nm.
```

An ordered occupation state is $`|i_1\cdots i_m\rangle=e_{i_1}\wedge\cdots\wedge e_{i_m}`$, with increasing indices. A Slater determinant occupies $`m`$ orthonormal orbitals. A one-particle map acts on each orbital, so its many-body action is $`K=\bigwedge^mU`$.

This construction preserves decomposability: an invertible $`U`$ maps a Slater to another Slater after normalization. It also acts on arbitrary coherent superpositions of occupation states, where no single occupied-orbital list suffices. The simulator receives the quantum specimen, not that list.

If the one-particle singular values are $`s_1\ge\cdots\ge s_N`$, the largest $`m`$-particle singular value is their top-$`m`$ product. A bounded one-particle condition number therefore need not give a bounded many-particle condition number. The project still needs its [finite-time chain proof](../science/dynamics.md) to show how many useful singular modes actually occur; an eigenvector-condition upper bound does not establish that fact.

## Bridge 3: unknown Slaters can carry hidden classical signs

Pair a low and a high singular mode. Two different occupied-orbital directions can be nonorthogonal before $`U`$ and orthogonal after normalized filtering. Occupying one orbital in each of several disjoint pairs produces genuine Slaters labelled by a hidden sign string.

A successful approximate processor, followed by a target-basis measurement, would decode the entire string accurately. This converts a physical simulation claim into a discrimination bound. An explicit tensor SDP dual controls collective decoding, while a separate confidence-with-rejection argument retains the cost of rare acceptance. The [Gaussian converse](../science/gaussian_converse.md) supplies both steps rather than assuming that separate binary guesses automatically prove every collective statement.

## Bridge 4: pure-Slater fluctuations permit a deterministic approximation

Write the polar decomposition as $`U=We^B`$. The unitary part $`\Gamma_m(W)`$ is a single known channel. To compare it with the normalized full target, follow the positive path generated by $`d\Gamma(B)`$.

The project-specific identity for a pure Slater with occupied projector $`P`$ is

```math
\mathrm{Var}(d\Gamma(B))
=\mathrm{Tr}[PB(I-P)B]
\le\min(m,N-m)\|B\|^2.
```

Integrating its square-root speed gives a uniform pure-Slater error bound. General correlated inputs can have larger collective fluctuations. This is where the input promise enters the positive theorem; it is not a restriction on the controls allowed in the converse.

The [approximation proof](../science/gaussian_approximation.md) derives the distance estimate and explains why mixtures do not inherit it by convexity. The [implementation account](../science/implementation.md) charges matrix preprocessing, orbital rotations and finite precision.

## Continue through the common route

Use the [worked example](WORKED_EXAMPLE.md) to complete one finite input-to-output calculation, then follow the [30 milestones](MILESTONES.md). The milestone map supplies the dependency order; the linked `science/` pages remain the authoritative definitions and proofs. Neither the finite example nor the textbook tools alone establish the asymptotic threshold laws.
