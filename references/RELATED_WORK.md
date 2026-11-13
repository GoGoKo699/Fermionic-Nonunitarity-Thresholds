# Relation to earlier work

[Main result](../README.md) · [Scientific account](../science/README.md) · [BibTeX](references.bib)

The question here is how one known nonunitary fermionic propagator can act on **one unknown input specimen**. The required output is the normalized whole state, with a uniform conditional trace-distance guarantee. A classical description of the input, additional copies, and a preparation or reflection oracle are not supplied.

For the uniform open Hatano–Nelson chain, at fixed filling and the stated ballistic time, fix $`0<\epsilon<1/4`$ and $`0<p_0<1`$. The asymmetry scales for conditional trace error at most $`\epsilon`$ and worst-input success at least $`p_0`$ differ:

| Input promise | Asymmetry scale for fixed accuracy and nonvanishing worst-input success | Supported implementation or obstruction |
| --- | --- | --- |
| Unknown Slater determinant | $`N^{-3/2}`$ | A common polar unitary gives the upper bound; a Slater phase ensemble gives the converse. |
| Arbitrary unknown correlated pure state in the fixed-number sector | $`N^{-2}`$ | Filtering gives the upper bound; propagator singular spread and state separation give the converse. |

The constants depend on the fixed accuracy, required success probability, filling interval, and hopping cap. This compares input promises under the same allowed CP processing. It is not a restriction of the converse to Gaussian processors, a classical computational lower bound, or a claim about observing a known prepared skin state.

## Closest comparisons

| Earlier result | What is inherited | Additional question settled here |
| --- | --- | --- |
| [Shimomura–Sato 2024](#ss24) | Fock-space skin effects, the imaginary-gauge $`m(N-m)`$ scale, and superextensive eigenvector conditioning. | Singular spread of the actual propagator at an explicit bounded-hopping time, followed by fixed-error, unknown-input operational thresholds. |
| [Zhu–Bierman–Lu–Li 2025](#zbll25) | Exterior-power SVD circuits, singular-mode ancilla filters, and block-operator approximation. | Optimal success scales over all CP implementations and the different approximate thresholds for Slater and correlated inputs. |
| [Feng–Liu–Zhang–Chen 2025](#flzc25) | The importance of numerical conditioning in Hatano–Nelson evolution and classical Gaussian-state updates. | A physical transformation guarantee for an unknown specimen rather than a numerical representation of a described state. |
| [Kawabata–Numasawa–Ryu 2023](#knr23) and [Chaduteau–Lee–Schindler 2026](#cls26) | Postselected fermionic dynamics and the distinction between a selected trajectory and an unread Lindblad process. | A promise-dependent feasibility boundary that is independent of the chosen loss realization. |
| [Chefles–Barnett 1998](#cb98), [Chefles–Jozsa–Winter 2004](#cjw04), and [Nakahira–Usuda–Kato 2012](#nuk12) | Probabilistic state transformation, state separation, and discrimination with inconclusive outcomes. | Their application to a hard family of unknown Slaters for this propagator; the generic discrimination principles are not new claims. |

### SS24

Kenji Shimomura and Masatoshi Sato, **General Criterion for Non-Hermitian Skin Effects and Application: Fock Space Skin Effects in Many-Body Systems**, *Physical Review Letters* **133**, 136502 (2024). [DOI](https://doi.org/10.1103/PhysRevLett.133.136502) · [arXiv:2403.13595v3](https://arxiv.org/html/2403.13595v3).

Equation (6), Figure 3, and Supplement S6 already identify an $`e^{cN^2}`$ many-body eigenvector-conditioning scale at finite filling. Supplements S7–S8 discuss no-jump survival and singular vectors in a specified dissipative realization. Neither the imaginary-gauge scale nor superextensive Fock-space nonnormality is claimed as a discovery here.

The distinction is between an eigenvector condition number and singular values of the finite-time propagator. A large diagonalizer condition number alone does not lower-bound transient amplification at a prescribed polynomially bounded time. The proof here supplies such a bound, uniformly into weak asymmetry, and compares conditional approximation on two input classes.

### ZBLL25

Guorui Zhu, Joel Bierman, Jianfeng Lu, and Yingzhou Li, **Quantum circuit for non-unitary linear transformation of basis sets**, *npj Quantum Information* **11**, 198 (2025). [DOI](https://doi.org/10.1038/s41534-025-01145-3) · [arXiv:2502.08962v1](https://arxiv.org/html/2502.08962v1) · [published author manuscript](https://yingzhouli.com/download_file/Paper/nonunitarytransQC.pdf).

Section III constructs the exterior-power transformation using the one-body SVD, unitary basis rotations, and ancilla postselection for singular-mode factors. Equation (22) bounds the error from rounding singular values in operator norm. The generic polynomial-size SVD compiler used here is inherited from this construction and earlier fermionic rotation circuits.

An additive block-operator error does not by itself control the normalized conditional output when acceptance amplitudes can be small. Conversely, a block-operator obstruction need not persist on a restricted input manifold. The new comparison concerns that normalized, unknown-Slater guarantee and its separation from arbitrary correlated inputs. The polar approximation is input independent; it does not reconstruct the unknown occupied orbitals.

### FLZC25

Xu Feng, Shuo Liu, Shi-Xin Zhang, and Shu Chen, **Numerical instability of non-Hermitian Hamiltonian evolution**, *Physical Review B* **111**, 224310 (2025). [DOI](https://doi.org/10.1103/g1cw-tk7f) · [arXiv:2504.07812v3](https://arxiv.org/html/2504.07812v3).

This study distinguishes reliable eigenvalues from reliable evolution and examines instability caused by nonnormality. Appendix B propagates an occupied-orbital matrix and reorthogonalizes it by QR decomposition. These are efficient classical descriptions when the initial orbitals are given. They do not provide a physical channel that receives one unknown state and produces its normalized propagated state. The present success bounds do not contradict efficient classical Gaussian simulation.

### KNR23

Kohei Kawabata, Tokiro Numasawa, and Shinsei Ryu, **Entanglement Phase Transition Induced by the Non-Hermitian Skin Effect**, *Physical Review X* **13**, 021007 (2023). [DOI](https://doi.org/10.1103/PhysRevX.13.021007) · [arXiv:2206.05384](https://arxiv.org/abs/2206.05384).

This work studies fermionic entanglement dynamics driven by the skin effect. Appendix A supplies a local-loss realization and discusses the probability of the selected trajectory; Appendix B treats Gaussian-state dynamics. Those physical mechanisms and methods are prior foundations. Here the propagator is a prescribed transformation task, and the lower bounds allow arbitrary heralded CP implementations rather than fixing that loss mechanism.

### CLS26

Alexandre Chaduteau, Derek K. K. Lee, and Frank Schindler, **Lindbladian versus Postselected Non-Hermitian Topology**, *Physical Review Letters* **136**, 016603 (2026). [DOI](https://doi.org/10.1103/ljvt-w6hw) · [arXiv:2507.07187v2](https://arxiv.org/html/2507.07187v2).

The paper explicitly motivates its comparison by the exponential particle-number cost of postselection and relates postselected and full Lindbladian winding numbers. That observation is inherited. Our task keeps the normalized selected propagator as the target and asks how its physical approximation depends on the input promise. No impossibility of unconditional Lindbladian skin effects is inferred.

## Experiments, Gaussian processing, and standard proof ingredients

### SCYL25

Ruizhe Shen, Tianqi Chen, Bo Yang, and Ching Hua Lee, **Observation of the non-Hermitian skin effect and Fermi skin on a digital quantum computer**, *Nature Communications* **16**, 1340 (2025). [DOI](https://doi.org/10.1038/s41467-025-55953-4) · [arXiv:2311.10143v3](https://arxiv.org/abs/2311.10143v3) · [published full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11794467/).

The experiment uses ancilla postselection and optimized circuits to observe spatial propagation and Fermi-skin accumulation from specified initial states. Such demonstrations do not require the uniform unknown-input guarantee studied here. Their feasibility is consistent with the lower bounds; no inference is made that known-state preparation or measurement of selected observables must pay the universal worst-input cost.

### TU05

[Terashima and Ueda, *Nonunitary quantum circuit*, 2005](https://doi.org/10.1142/S0219749905001456) develops measurement-operated nonunitary gates. The standard contraction normalization and heralding interpretation are inherited; this repository gives their short proofs for its exact error convention.

### CB98

[Chefles and Barnett, *Quantum State Separation, Unambiguous Discrimination and Exact Cloning*, 1998](https://doi.org/10.1088/0305-4470/31/50/007) bounds the success of reducing the overlap of two possible pure inputs. Its state-separation principle underlies the robust correlated-input converse.

### CJW04

[Chefles, Jozsa, and Winter, *On the existence of physical transformations between sets of quantum states*, 2004](https://doi.org/10.1142/S0219749904000031) treats transformation of pure-state families through Gram matrices and probabilistic operations. The use of a hard family to constrain a common CP map belongs to this established framework.

### NUK12

Kenji Nakahira, Tsuyoshi Sasaki Usuda, and Kentaro Kato, **Discrimination between geometrically uniform quantum states with inconclusive results**, *Physical Review A* **86**, 032316 (2012). [DOI](https://doi.org/10.1103/PhysRevA.86.032316).

This work solves fixed-inconclusive-rate discrimination for geometrically uniform pure-state sets. Phase-group symmetrization and discrimination with rejection are therefore inherited machinery. The self-contained low-Hamming-subspace and tail bound here applies that machinery to a fermionic propagation witness; it is not presented as a new general discrimination optimum.

### B05, K18, and AA90

[Sergey Bravyi, *Lagrangian representation for fermionic linear optics*, 2005](https://doi.org/10.26421/QIC5.3-3), [arXiv:quant-ph/0404180v2](https://arxiv.org/html/quant-ph/0404180v2), characterizes Gaussian states, maps, measurement updates, and Wick correlations. These supply the standard Gaussian framework. The lower bounds here allow non-Gaussian processing too; they are not Gaussian-operation conversion no-go theorems.

[Ian D. Kivlichan et al., *Quantum Simulation of Electronic Structure with Linear Depth and Connectivity*, 2018](https://doi.org/10.1103/PhysRevLett.120.110501), [arXiv:1711.04789v2](https://arxiv.org/abs/1711.04789v2), supplies efficient fermionic basis rotations and Slater preparation with linear connectivity. Those circuit techniques are inherited. Preparing a state from supplied orbital coefficients is different from transforming one unknown specimen.

[J. Anandan and Y. Aharonov, *Geometry of quantum evolution*, 1990](https://doi.org/10.1103/PhysRevLett.65.1697) relates projective-state path length to quantum uncertainty. The use of Fubini–Study geometry is standard. Here it is applied directly to the normalized nonunitary Slater path; Wick's identity gives the specific variance bound used by the polar approximation.

## Scope of the contribution and comparison

The new account combines an explicit-time singular-value bulk with two operational arguments: high-confidence discrimination of a Slater family, and a polar-unitary approximation controlled by Slater variance. It establishes different constant-success critical powers for the same known process, with the input promise as the changed resource.

At $`g=N^{-7/4}`$, every unknown Slater admits deterministic vanishing-error approximation, while the arbitrary-input task has exponentially small worst-input success. At $`g=\beta/N`$ with fixed $`\beta>0`$, even the unknown-Slater task has exponential success suppression despite bounded single-particle conditioning. The constants in that statement depend on $`\beta`$. The full Gaussian-only success-probability frontier between these regimes is not identified.

These comparisons concern the listed primary sources and their stated models. They do not assert exhaustive priority clearance. The Hatano–Nelson model itself is inherited from [Hatano and Nelson, 1996](https://doi.org/10.1103/PhysRevLett.77.570). All generic linear algebra, Gaussian circuit, state-transformation, and geometric ingredients remain credited above.
