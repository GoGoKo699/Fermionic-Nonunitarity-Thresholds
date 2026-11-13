# Thirty milestones through the input-promise separation

The selected educational anchor is **John Watrous, _The Theory of Quantum Information_ (2018)**, using the author's [official manuscript page](https://cs.uwaterloo.ca/~watrous/TQI/). The verified chapter links used below are [Chapter 1: Mathematical preliminaries](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), [Chapter 2: Basic notions of quantum information](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), and [Chapter 3: Similarity and distance among states and channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

This common map has **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background allocation joins finite-dimensional quantum operations to the extra fermionic and normalized-path ingredients supplied by the project. It progresses from one linear map and one state to the complete unknown-specimen experiment. The narrative allocation assembles the finite-time singular-value mechanism, two information-theoretic converses, the deterministic Gaussian approximation, and their physical comparison. Its final milestones integrate the thresholds with actual compilation costs, attribution, and scope.

The anchor supplies the quantum-information foundations. Exterior powers, Wick variance, the finite-time chain estimate, and the specialized rejection bound are developed in the linked project proofs. Primary research references in [Related work](../references/RELATED_WORK.md) supply attribution and specialist dependencies; they do not introduce another educational anchor.

## Overview

| Milestone | Phase | Understanding target |
|---|---|---|
| [M01](#m01) | Background/preliminaries | Singular axes of one linear transformation |
| [M02](#m02) | Background/preliminaries | Pure states, density operators, and unknown specimens |
| [M03](#m03) | Background/preliminaries | Fermionic modes and the fixed-number sector |
| [M04](#m04) | Background/preliminaries | The pure-Slater input promise |
| [M05](#m05) | Background/preliminaries | Physical operations and success branches |
| [M06](#m06) | Background/preliminaries | Normalization, nonlinearity, and heralding yield |
| [M07](#m07) | Background/preliminaries | Trace distance and root fidelity |
| [M08](#m08) | Background/preliminaries | State separation as a physical restriction |
| [M09](#m09) | Background/preliminaries | Product labels and discrimination certificates |
| [M10](#m10) | Background/preliminaries | Polar decomposition and normalized-state paths |
| [M11](#m11) | Background/preliminaries | Finite-time and weak-asymmetry conventions |
| [M12](#m12) | Background/preliminaries | The complete comparison of input promises |
| [M13](#m13) | Narrative/innovation | Imaginary gauge and the many-body upper envelope |
| [M14](#m14) | Narrative/innovation | Reciprocal singular pairs and exterior products |
| [M15](#m15) | Narrative/innovation | A counted supply of growing periodic modes |
| [M16](#m16) | Narrative/innovation | Boundary rank and the two exponential tails |
| [M17](#m17) | Narrative/innovation | A finite-time open-chain conditioning theorem |
| [M18](#m18) | Narrative/innovation | Exact optimal filtering on all pure inputs |
| [M19](#m19) | Narrative/innovation | The arbitrary-processor fixed-error obstruction |
| [M20](#m20) | Narrative/innovation | The all-input success and asymmetry scales |
| [M21](#m21) | Narrative/innovation | A hard family made entirely of Slaters |
| [M22](#m22) | Narrative/innovation | The complete-string Helstrom bound |
| [M23](#m23) | Narrative/innovation | High confidence with rejection |
| [M24](#m24) | Narrative/innovation | Matched Slater success in two asymmetry regimes |
| [M25](#m25) | Narrative/innovation | One polar unitary for every unknown Slater |
| [M26](#m26) | Narrative/innovation | Why Slater variance changes the sufficient scale |
| [M27](#m27) | Narrative/innovation | Two matched constant-success powers |
| [M28](#m28) | Narrative/innovation | The explicit $`g_N=N^{-7/4}`$ separation |
| [M29](#m29) | Narrative/innovation | Paid compilation and conditional precision |
| [M30](#m30) | Narrative/innovation | The contribution, its meaning, and its remaining boundary |

## Background/preliminaries: M01–M12

### M01

**Singular axes of one linear transformation**

**Phase:** Background/preliminaries.

**Central question:** Which features of an invertible matrix describe how differently it stretches different input directions?

**Understanding target:** Relate an SVD to its right and left singular vectors, operator norm, least singular value, and condition number. Distinguish singular values of a time propagator from eigenvalues of its Hamiltonian.

**Dependencies and story role:** Starting point. This gives a local description of one transformation before introducing the many-fermion space or a physical implementation.

**Conceptual connection:** Relative stretching will later turn almost parallel inputs into distinct normalized outputs; the singular axes identify the inputs that expose that effect.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Dynamics](../science/dynamics.md), “Notation and constants”; [Heralding](../science/heralding.md), definitions of $`\kappa`$.

### M02

**Pure states, density operators, and unknown specimens**

**Phase:** Background/preliminaries.

**Central question:** What information is supplied when a physical pure state is available but its classical vector is unknown?

**Understanding target:** Translate between a normalized ket and its rank-one density operator. Keep one physical specimen distinct from a classical state description, a source of additional copies, and coherent preparation access.

**Dependencies and story role:** Uses [M01](#m01). It turns an algebraic vector transformation into a question about information carried by a supplied quantum system.

**Conceptual connection:** A known matrix can be processed classically while the input state remains unknown; this difference controls which simulation strategies solve the actual task.

**Source pointers:** [Watrous Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Model](../science/model.md), “Quantum input and conditional output”; [Interpretation](../science/interpretation.md), “Specimens, descriptions and repeated access.”

### M03

**Fermionic modes and the fixed-number sector**

**Phase:** Background/preliminaries.

**Central question:** How does a one-particle map act on a system containing exactly $`m`$ fermions?

**Understanding target:** Explain occupation configurations, antisymmetry, and the space $`\mathcal F_m=\bigwedge^m\mathbb C^N`$. Understand why the number-conserving propagator is $`K=\bigwedge^m U`$ and why its sector dimension is $`\binom Nm`$.

**Dependencies and story role:** Uses [M01](#m01) and [M02](#m02). It expands the setting from one vector to the physical many-body input space.

**Conceptual connection:** Exterior powers connect the manageable $`N\times N`$ one-particle matrix to a much larger quantum sector without supplying a classical description of its unknown state.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), for linear and tensor-space foundations; [Model](../science/model.md), “Chain, filling and prescribed evolution”; [Dynamics](../science/dynamics.md), “Reciprocal singular values and exterior powers.” The fermionic exterior-power account is supplied by the project.

### M04

**The pure-Slater input promise**

**Phase:** Background/preliminaries.

**Central question:** Which pure fixed-number states are Slater determinants, and what does that promise leave unknown?

**Understanding target:** Describe a Slater by orthonormal occupied orbitals and its occupied projector $`P`$. Recognize that arbitrary correlated pure states also inhabit the same fixed-number sector, and that a pure-Slater promise does not give the simulator the orbitals or extend automatically to mixtures.

**Dependencies and story role:** Uses [M02](#m02)–[M03](#m03). It identifies the two input sets whose different approximate processing costs form the central comparison.

**Conceptual connection:** The distinction is a geometric restriction on the supplied quantum state, rather than a restriction to Gaussian processing by the receiver.

**Source pointers:** [Watrous Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), for pure and mixed states; [Model](../science/model.md), “The two input promises”; [Gaussian approximation](../science/gaussian_approximation.md), “Definitions” and “Why the theorem does not extend by convexity.”

### M05

**Physical operations and success branches**

**Phase:** Background/preliminaries.

**Central question:** How can a protocol with helpers, measurements, and feedback be represented by one success operation?

**Understanding target:** Use complete positivity, Kraus operators, trace nonincrease, and a classical success flag. Explain why accepting several measurement records still yields one CP success map with an input-dependent acceptance probability.

**Dependencies and story role:** Uses [M02](#m02). It supplies a common operational language broad enough for every processor allowed by either input promise.

**Conceptual connection:** An information-theoretic converse can cover arbitrary adaptive physical implementations by bounding their induced success map.

**Source pointers:** [Watrous Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Model](../science/model.md), “Quantum input and conditional output”; [Heralding](../science/heralding.md), opening definitions.

### M06

**Normalization, nonlinearity, and heralding yield**

**Phase:** Background/preliminaries.

**Central question:** Why does specifying the normalized ray $`K|\psi\rangle/\Vert K\psi\Vert `$ leave a physical implementation incomplete?

**Understanding target:** Separate the linear, subnormalized success output from its normalized conditional state. Define uniform conditional error and worst-input success, including the consequence of a zero-success promised input.

**Dependencies and story role:** Uses [M01](#m01), [M04](#m04), and [M05](#m05). It combines the matrix target and the physical operation into the project's performance criterion.

**Conceptual connection:** Normalization can change distinguishability, while the acceptance probability records the physical price of that change.

**Source pointers:** [Watrous Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Model](../science/model.md), “Quantum input and conditional output”; [Heralding](../science/heralding.md), “What success probability measures.”

### M07

**Trace distance and root fidelity**

**Phase:** Background/preliminaries.

**Central question:** How does conditional state accuracy constrain the statistics of a subsequent measurement?

**Understanding target:** Use half-trace distance $`D=\tfrac12\Vert \rho-\sigma\Vert _1`$ and root fidelity $`F=\Vert \sqrt\rho\sqrt\sigma\Vert _1`$. Explain their pure-state meanings and the direction of fidelity monotonicity under channels and measurements.

**Dependencies and story role:** Uses [M02](#m02), [M05](#m05), and [M06](#m06). It connects output accuracy to a testable information statement.

**Conceptual connection:** The same distance convention supports both the nearly parallel input converse and the conversion of Slater simulation into high-confidence decoding.

**Source pointers:** [Watrous Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Heralding](../science/heralding.md), “A nearly parallel input pair” and “Include failures before applying information monotonicity”; [Gaussian converse](../science/gaussian_converse.md), “From accurate processing to discrimination.”

### M08

**State separation as a physical restriction**

**Phase:** Background/preliminaries.

**Central question:** What prevents a physical device from turning two almost identical unknown inputs into reliably orthogonal outputs every time?

**Understanding target:** Include success and failure in one trace-preserving description before applying information monotonicity. Understand how a successful branch can increase separation while its probability remains constrained.

**Dependencies and story role:** Uses [M05](#m05)–[M07](#m07). It introduces the converse mechanism in its smallest useful setting.

**Conceptual connection:** A nonunitary target may demand greater separation than a deterministic quantum channel can provide; heralding reconciles the target with quantum mechanics.

**Source pointers:** [Watrous Chapters 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Heralding](../science/heralding.md), Proposition 2; [Related work](../references/RELATED_WORK.md), CB98 and CJW04.

### M09

**Product labels and discrimination certificates**

**Phase:** Background/preliminaries.

**Central question:** How can a bound on guessing one hidden binary label become a bound on guessing a complete string?

**Understanding target:** Represent an independent product ensemble, distinguish full-string success from average bit accuracy, and interpret positive-semidefinite discrimination dual certificates. Recognize why collective decoding needs its own proof rather than an assumed product restriction.

**Dependencies and story role:** Uses [M03](#m03), [M05](#m05), and [M07](#m07). It prepares the information tools for a hard family that stays inside the Slater manifold.

**Conceptual connection:** Independent orbital choices can encode many hidden labels in valid fermionic states, while quantum discrimination constrains their simultaneous recovery.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), for positive operators and optimization foundations, and [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), for state discrimination; [Gaussian converse](../science/gaussian_converse.md), “Product Helstrom bound.”

### M10

**Polar decomposition and normalized-state paths**

**Phase:** Background/preliminaries.

**Central question:** How can the nonunitary part of a known map be separated from a candidate deterministic unitary implementation?

**Understanding target:** Write $`U=W e^B`$ with $`W`$ unitary and $`B`$ Hermitian. Interpret normalized filtering by $`e^{s\,d\Gamma(B)}`$ as a path whose speed is a standard deviation, and connect pure-state angle to trace distance.

**Dependencies and story role:** Uses [M01](#m01), [M03](#m03), [M04](#m04), and [M07](#m07). It introduces the constructive route that complements the converse arguments.

**Conceptual connection:** The input promise can control path variance even when the same global matrix has a large condition number.

**Source pointers:** [Watrous Chapters 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian approximation](../science/gaussian_approximation.md), “The uniform pure-Slater bound.” The normalized-path and Wick-variance derivations are supplied there.

### M11

**Finite-time and weak-asymmetry conventions**

**Phase:** Background/preliminaries.

**Central question:** Which quantities remain fixed when chain length grows and the hopping asymmetry shrinks?

**Understanding target:** Keep the filling window, hopping cap, accuracy, and required success fixed. Identify the particular time

```math
t_N=\frac{\alpha N}{J},
\qquad
\alpha=\frac{1}{3200\cosh g_{\max}},
```

and distinguish a finite inequality with an explicit remainder from an asymptotic law in a stated regime.

**Dependencies and story role:** Uses [M01](#m01), [M03](#m03), and [M06](#m06). It fixes the limiting framework before the global model and proof narrative are assembled.

**Conceptual connection:** Weak one-particle asymmetry can accumulate differently with particle number; the chosen time and order of limits determine what the resulting threshold means.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), for finite-dimensional estimates; [Model](../science/model.md), “Chain, filling and prescribed evolution”; [Dynamics](../science/dynamics.md), “Notation and constants” and “Uniform bounds at finite filling.”

### M12

**The complete comparison of input promises**

**Phase:** Background/preliminaries.

**Central question:** What exact experiment is held fixed when unknown Slaters are compared with arbitrary correlated inputs?

**Understanding target:** State the known chain and prescribed time, one unknown pure specimen, two input promises, arbitrary receiver processing, conditional half-trace error, and worst-input success in one account. Explain which extra access would change that experiment.

**Dependencies and story role:** Integrates [M01](#m01)–[M11](#m11). It closes the background phase by turning the local prerequisites into the complete operational question.

**Conceptual connection:** Matrix dynamics, physical channels, fermionic input geometry, and information access now refer to one common model.

**Source pointers:** [Watrous Chapters 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Model](../science/model.md); [Interpretation](../science/interpretation.md), “The same transformation, different promises” and “Specimens, descriptions and repeated access.”

## Narrative/innovation: M13–M30

### M13

**Imaginary gauge and the many-body upper envelope**

**Phase:** Narrative/innovation.

**Central question:** What does the known imaginary-gauge similarity control before a finite-time lower bound is proved?

**Understanding target:** Derive $`h_g=S_gh_0S_g^{-1}`$ and the occupied-position-sum range $`m(N-m)`$. Obtain the upper bound on $`\log\kappa(K)`$ and explain why it does not by itself force growth at a specified time.

**Dependencies and story role:** Uses [M01](#m01), [M03](#m03), [M11](#m11), and [M12](#m12). It starts the narrative with one inherited, local algebraic mechanism and identifies the missing direction of the proof.

**Conceptual connection:** A simple one-particle gauge produces an extensive many-body envelope, but an envelope is different from an attained dynamical obstruction.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Dynamics](../science/dynamics.md), “Imaginary gauge and the upper bound”; [Related work](../references/RELATED_WORK.md), SS24.

### M14

**Reciprocal singular pairs and exterior products**

**Phase:** Narrative/innovation.

**Central question:** How do real hopping coefficients let a supply of large one-particle singular values control the entire fixed-number propagator?

**Understanding target:** Explain $`\overline U=U^{-1}`$, reciprocal singular pairs, products of singular values in exterior powers, and $`\kappa(K)=\Vert K\Vert ^2`$. Reduce the needed product to $`\min(m,N-m)`$ factors.

**Dependencies and story role:** Uses [M01](#m01), [M03](#m03), and [M13](#m13). It prepares the exact transfer from a local mode estimate to the many-body condition number.

**Conceptual connection:** Particle–hole symmetry of the singular-value product keeps the argument valid throughout the stated filling window.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Dynamics](../science/dynamics.md), “Reciprocal singular values and exterior powers.”

### M15

**A counted supply of growing periodic modes**

**Phase:** Narrative/innovation.

**Central question:** Where can growing singular values be calculated explicitly before dealing with the open boundary?

**Understanding target:** Diagonalize the periodic comparison in Fourier modes and identify the interval where the sine is at least one half. Retain its exact count

```math
H_N=
\left\lfloor\frac{5N}{12}\right\rfloor
-\left\lceil\frac{N}{12}\right\rceil+1.
```

**Dependencies and story role:** Uses [M11](#m11), [M13](#m13), and [M14](#m14). It supplies the computable bulk ingredient for the open-chain lower bound.

**Conceptual connection:** Normal periodic dynamics provide singular-value information even though the scientific target remains the prescribed open chain.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Dynamics](../science/dynamics.md), “Periodic comparison.”

### M16

**Boundary rank and the two exponential tails**

**Phase:** Narrative/innovation.

**Central question:** How can changing the boundary be controlled without assuming its effect is small in operator norm?

**Understanding target:** Use a degree-$`d_N`$ exponential polynomial and the support of short walks to obtain boundary rank at most $`2d_N`$. Track one truncation error for each propagator, yielding

```math
U_{\mathrm{open}}
=U_{\mathrm{per}}+R_N+E_N,
\quad
\mathrm{rank}R_N\leq2d_N,
\quad
\Vert E_N\Vert \leq2\eta_N.
```

**Dependencies and story role:** Uses [M01](#m01), [M11](#m11), and [M15](#m15). It isolates the exact boundary mechanism before applying a global spectral estimate.

**Conceptual connection:** Low rank and small norm are different controls; their combination preserves many bulk singular directions at the chosen time.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Dynamics](../science/dynamics.md), “A finite-rank difference plus a controlled tail.”

### M17

**A finite-time open-chain conditioning theorem**

**Phase:** Narrative/innovation.

**Central question:** How many growing directions survive the boundary correction, and what do they prove for $`K`$?

**Understanding target:** Apply singular-value interlacing and retain the useful mode count

```math
L_{N,m}
=\min\{m,N-m,[H_N-2d_N]_+\}.
```

Explain the lower factor $`\max\{1,e^{B_N(g)}-2\eta_N\}`$, reciprocal pairing, and the condition under which the finite bounds give $`\log\kappa(K)=\Theta(gN^2)`$.

**Dependencies and story role:** Integrates [M13](#m13)–[M16](#m16). It closes the dynamical proof thread with a theorem about the actual propagator at its specified time.

**Conceptual connection:** The finite-size remainder and actual mode count make the weak-asymmetry limit usable rather than extrapolated from fixed positive $`g`$.

**Source pointers:** [Watrous Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Dynamics](../science/dynamics.md), “Finite-size theorem,” “Singular-value interlacing and the lower bound,” and “Uniform bounds at finite filling.”

### M18

**Exact optimal filtering on all pure inputs**

**Phase:** Narrative/innovation.

**Central question:** What is the best worst-input success probability for realizing the normalized $`K`$ transformation exactly?

**Understanding target:** Show that every exact successful Kraus operator is proportional to $`K`$, use trace nonincrease, and obtain $`p^\star_{\mathrm{all}}(0;K)=\kappa(K)^{-2}`$. Identify the attaining normalized filter and its inherited status.

**Dependencies and story role:** Uses [M05](#m05), [M06](#m06), [M12](#m12), and [M17](#m17). It turns dynamical stretching into an exact physical yield statement.

**Conceptual connection:** Optimal normalization is constrained by the strongest singular direction, while the least-stretched input fixes the worst success.

**Source pointers:** [Watrous Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Heralding](../science/heralding.md), “Exact optimal success on all pure inputs”; [Related work](../references/RELATED_WORK.md), TU05.

### M19

**The arbitrary-processor fixed-error obstruction**

**Phase:** Narrative/innovation.

**Central question:** Why does allowing a fixed conditional error still leave a conditioning-dependent success penalty?

**Understanding target:** Construct the extremal nearly parallel input pair, show that its ideal outputs are orthogonal, and include failures before applying fidelity monotonicity. Obtain the factor $`1-2\sqrt{\epsilon(1-\epsilon)}`$ for $`0\lt \epsilon\lt 1/2`$ and recognize the bound's worst-input meaning.

**Dependencies and story role:** Uses [M07](#m07), [M08](#m08), and [M18](#m18). It strengthens the exact statement to the approximation criterion used in the central comparison.

**Conceptual connection:** Successful-state accuracy, retained information, and state-dependent acceptance can be bounded together without specifying a particular circuit.

**Source pointers:** [Watrous Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Heralding](../science/heralding.md), Proposition 2; [Related work](../references/RELATED_WORK.md), CB98 and CJW04.

### M20

**The all-input success and asymmetry scales**

**Phase:** Narrative/innovation.

**Central question:** What operational conclusion follows after combining finite-time conditioning with the robust success bound?

**Understanding target:** Derive the $`\exp[-\Theta(g_NN^2)]`$ success order when $`g_NN^2\to\infty`$, with the appropriate fixed parameters. Distinguish constant success, inverse-polynomial success, and a full finite-error formula; locate the all-input constant-success scale at $`N^{-2}`$.

**Dependencies and story role:** Integrates [M17](#m17)–[M19](#m19), using the deterministic sufficiency prepared in [M10](#m10). It closes the unrestricted-input thread before restricting the input manifold.

**Conceptual connection:** A large condition number becomes a physical processing limitation only after the accuracy, success, and access conventions are combined.

**Source pointers:** [Watrous Chapters 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Heralding](../science/heralding.md), “Consequences for the chain”; [Gaussian approximation](../science/gaussian_approximation.md), “Deterministic sufficiency for arbitrary pure inputs.”

### M21

**A hard family made entirely of Slaters**

**Phase:** Narrative/innovation.

**Central question:** Can an information-theoretic obstruction be exposed without leaving the pure-Slater input promise?

**Understanding target:** Occupy one orbital in each disjoint low/high singular pair, add the required spectators, and choose amplitudes using each singular-value ratio. Explain why hidden signs label valid input Slaters and why their ideal outputs are mutually orthogonal Slaters.

**Dependencies and story role:** Uses [M04](#m04), [M09](#m09), [M14](#m14), and [M17](#m17). It starts a new converse thread inside the restricted input manifold.

**Conceptual connection:** Quantum information can be hidden in independent orbital signs even when all inputs have an efficient Gaussian description that remains undisclosed to the simulator.

**Source pointers:** [Watrous Chapters 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian converse](../science/gaussian_converse.md), “Finite singular-mode assumptions” and “From accurate processing to discrimination.”

### M22

**The complete-string Helstrom bound**

**Phase:** Narrative/innovation.

**Central question:** Why can a collective decoder not recover the entire hidden sign string more successfully than the stated product bound?

**Understanding target:** Reconstruct the one-pair positive-semidefinite dual certificate, tensor its domination inequalities, and identify the matching product measurement. Convert conditional simulation accuracy into $`p_{\min}\leq\prod_j h(q_j)/(1-\epsilon)`$.

**Dependencies and story role:** Uses [M09](#m09), [M19](#m19), and [M21](#m21). It supplies a rigorous collective-measurement converse useful at weak asymmetry.

**Conceptual connection:** The Gaussian promise constrains the input family but leaves the receiver unrestricted; a tensor dual proves the bound without imposing local decoding.

**Source pointers:** [Watrous Chapters 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian converse](../science/gaussian_converse.md), “Product Helstrom bound.”

### M23

**High confidence with rejection**

**Phase:** Narrative/innovation.

**Central question:** What stronger restriction appears when accepted decoding must be highly reliable even if most attempts are rejected?

**Understanding target:** Symmetrize the phase ensemble, separate low- and high-Hamming-weight components, and interpret the finite bound in terms of $`q_{\max}`$, $`b`$, tail weight, and a positive denominator. Explain the separate roles of low-subspace dimension and the Poisson-binomial tail.

**Dependencies and story role:** Uses [M07](#m07), [M09](#m09), [M21](#m21), and [M22](#m22). It resolves the loss of the stronger exponent in ordinary minimum-error decoding.

**Conceptual connection:** A rejection outcome can improve conditional confidence, but acceptance must then draw sufficient weight from a small tail of the input ensemble.

**Source pointers:** [Watrous Chapters 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian converse](../science/gaussian_converse.md), “High confidence with abstention” and “Explicit dimension and tail estimates”; [Related work](../references/RELATED_WORK.md), NUK12.

### M24

**Matched Slater success in two asymmetry regimes**

**Phase:** Narrative/innovation.

**Central question:** Which probability laws are actually matched for unknown Slater inputs?

**Understanding target:** Combine the singular-pair supply and rejection bound to obtain $`\exp[-\Theta_g(N^2)]`$ at fixed positive $`g`$, and $`\exp[-\Theta_\beta(N)]`$ at $`g=\beta/N`$ for fixed $`\beta>0`$. Identify the matching filter construction and explain the bounded one-particle conditioning in the latter regime.

**Dependencies and story role:** Integrates [M17](#m17), [M21](#m21)–[M23](#m23). It closes the Slater-converse thread in its two matched probability regimes.

**Conceptual connection:** Bounded single-particle conditioning does not guarantee efficient finite-density processing, even on unknown Gaussian specimens.

**Source pointers:** [Watrous Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian converse](../science/gaussian_converse.md), “Apply the singular-mode supply of the chain”; [Implementation](../science/implementation.md), “A uniform success bound.”

### M25

**One polar unitary for every unknown Slater**

**Phase:** Narrative/innovation.

**Central question:** Can a deterministic approximation use the Gaussian promise without learning the input orbitals?

**Understanding target:** Apply the known polar factor $`\Gamma_m(W)`$, represent the remaining discrepancy by a normalized filtering path, and show that every state along that path remains a pure Slater.

**Dependencies and story role:** Uses [M04](#m04), [M10](#m10), and [M12](#m12). It begins the positive construction needed to compare promises rather than reporting only an obstruction.

**Conceptual connection:** A single channel fixed by the known propagator can exploit the geometry shared by all promised inputs.

**Source pointers:** [Watrous Chapters 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian approximation](../science/gaussian_approximation.md), “The uniform pure-Slater bound.”

### M26

**Why Slater variance changes the sufficient scale**

**Phase:** Narrative/innovation.

**Central question:** Which property of Slaters reduces the accumulated normalized-state distortion?

**Understanding target:** Use Wick's identity to express variance as $`\mathrm{Tr}[PB(I-P)B]`$, bound its rank by $`\min(m,N-m)`$, and integrate the path speed. Compare the resulting square-root particle-number factor with the unrestricted pure-state norm bound.

**Dependencies and story role:** Uses [M10](#m10), [M13](#m13), and [M25](#m25). It identifies the specific mathematical reason the positive approximation distinguishes the promises.

**Conceptual connection:** Restricted many-body fluctuations, rather than classical knowledge of the occupied orbitals, control the deterministic error.

**Source pointers:** [Watrous Chapters 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian approximation](../science/gaussian_approximation.md), proof of the uniform bound and “Deterministic sufficiency for arbitrary pure inputs.”

### M27

**Two matched constant-success powers**

**Phase:** Narrative/innovation.

**Central question:** At what asymmetry scale can a fixed success probability and fixed conditional accuracy remain possible under each promise?

**Understanding target:** Combine the product-Helstrom necessity with the polar-unitary sufficiency to locate the Slater scale at $`N^{-3/2}`$. Compare it with the all-input scale $`N^{-2}`$, retaining fixed accuracy, required success, filling, and the finite $`2\eta_N`$ correction.

**Dependencies and story role:** Integrates [M20](#m20), [M22](#m22), [M25](#m25), and [M26](#m26). It turns the two proof threads into a matching order comparison for one common operational requirement.

**Conceptual connection:** A constant-success boundary can be located even while the full intermediate Gaussian success-probability curve remains unresolved.

**Source pointers:** [Watrous Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Gaussian converse](../science/gaussian_converse.md), “The constant-success Slater scale”; [Gaussian approximation](../science/gaussian_approximation.md), “Deterministic sufficiency for arbitrary pure inputs.”

### M28

**The explicit $`g_N=N^{-7/4}`$ separation**

**Phase:** Narrative/innovation.

**Central question:** What happens between the two constant-success scales on the same prescribed chain and at the same time?

**Understanding target:** Insert $`g_N=N^{-7/4}`$ into both bounds and obtain deterministic Slater trace error $`O(N^{-1/4})`$ and all-input worst success at most $`\exp[-cN^{1/4}]`$. Explain the wider window $`N^{-2}\ll g_N\ll N^{-3/2}`$.

**Dependencies and story role:** Uses [M17](#m17), [M20](#m20), and [M27](#m27). It expresses the global promise comparison in one concrete asymptotic example.

**Conceptual connection:** The many-body information carried by correlated inputs changes physical implementability even when the one-particle dynamics and output target are held fixed.

**Source pointers:** [Watrous Chapters 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Dynamics](../science/dynamics.md), “The intermediate asymmetry used for the input-promise separation”; [Gaussian approximation](../science/gaussian_approximation.md), “A strict separation of input promises.”

### M29

**Paid compilation and conditional precision**

**Phase:** Narrative/innovation.

**Central question:** Which resources are required to make the matching constructions concrete, especially when success is rare?

**Understanding target:** Account for classical matrix preprocessing, orbital rotations, empty or occupied helpers, acceptance records, and logical gate synthesis. Explain why conditional accuracy needs absolute accepted-operator error small relative to its least accepted amplitude, and why its logarithmic precision cost is still polynomial.

**Dependencies and story role:** Uses [M05](#m05), [M06](#m06), [M18](#m18), [M24](#m24), and [M25](#m25). It integrates the positive constructions with the resource criterion used by the converse.

**Conceptual connection:** A polynomial circuit per attempt and a rare accepted specimen are separate resource facts; finite checks validate specified identities while the analytical proofs establish the general laws.

**Source pointers:** [Watrous Chapters 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) and [2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Implementation](../science/implementation.md), “Logical resources per attempt,” “Why rare inputs require more precision,” and “Backward-accurate SVD is sufficient”; [Verification guide](../verification/README.md).

### M30

**The contribution, its meaning, and its remaining boundary**

**Phase:** Narrative/innovation.

**Central question:** What complete scientific statement survives after inherited ingredients, all access assumptions, and the unfinished Gaussian frontier are made explicit?

**Understanding target:** Explain the specified finite-time propagator law, arbitrary-processor heralding converses, deterministic unknown-Slater approximation, and the $`N^{-3/2}`$ versus $`N^{-2}`$ constant-success scales as one connected result. Keep known-state preparation, selected observables, mixed-input guarantees, skin topology, and the unresolved full intermediate Gaussian probability curve within their actual scopes.

**Dependencies and story role:** Integrates [M12](#m12)–[M29](#m29). It closes the narrative with the contribution's physical meaning, resource obligations, attribution, and precise limits.

**Conceptual connection:** The relevant distinction is how an unknown quantum specimen may be processed under an input promise; neither a compact classical Gaussian model nor a large eigenvector condition number alone resolves that question.

**Source pointers:** [Watrous Chapters 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) and [3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Science route](../science/README.md); [Interpretation](../science/interpretation.md); [Related work](../references/RELATED_WORK.md), “Scope of the contribution and comparison.”

