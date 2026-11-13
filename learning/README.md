# Learn the result

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [source bridge](WATROUS_BRIDGE.md) gives verified chapter, section and theorem locators from the author's official manuscript, translates fidelity and distance conventions, and identifies the fermionic arguments supplied by this project.

Use one connected route:

1. Read the [model and input promises](../science/model.md): one unknown specimen, a known transformation, a returned quantum state and an explicit success flag.
2. Follow the [Watrous bridge](WATROUS_BRIDGE.md) from operators and CP maps to discrimination and the project-specific Slater geometry.
3. Work through the [four-mode experiment](WORKED_EXAMPLE.md), including its helpers, normalized output, success probability and final measurement. Its diagonal matrix is an illustrative toy, not the actual chain.
4. Use the [30 milestones](MILESTONES.md) for the common dependency-ordered route through the complete scientific account.

## Keep the promises visible

| Statement | Meaning in the learning route |
|---|---|
| Unknown pure Slater | A quantum specimen is supplied; its occupied orbitals are not supplied classically. |
| Arbitrary correlated pure input | Every pure state of the fixed-number sector is allowed, including non-Slater superpositions. |
| Conditional trace error | Compare the retained state after a successful flag with the normalized target. Success probability is a separate resource. |
| Deterministic approximation | One known Gaussian polar unitary always returns an output; its error depends on the promised input class. |
| Heralded converse | Every allowed CP processor is covered, including non-Gaussian controls and input-dependent acceptance. |

The pure-Slater positive theorem does not extend to mixtures by ordinary convexity. The full intermediate Slater success-probability curve and sharp crossover constants remain outside the established results. The finite example and numerical checks illustrate the analytical arguments; they do not prove their asymptotic claims.

The [science overview](../science/README.md) gives the direct proof route. The [verification guide](../verification/README.md) explains what the reproducible finite calculations check and where their scope ends.
