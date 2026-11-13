# A connected route through the propagation thresholds

Start with one physical question: an unknown quantum specimen is already present, and a known non-Hermitian propagator is prescribed. How reliably can a quantum device return its normalized output? The unknown-input condition distinguishes this question from computing or preparing the output of a known Slater determinant.

1. [Model](model.md) fixes the chain, finite filling, chosen ballistic time, one-specimen access, conditional half-trace error and two pure-input promises.
2. [Dynamics](dynamics.md) proves finite-size singular-value bounds. The periodic comparison supplies many growing modes; a finite-rank boundary correction transfers them to the actual open chain. Reciprocal singular values and exterior powers give the many-fermion condition number, with the exponentially small remainder retained.
3. [Heralding](heralding.md) gives exact optimal filtering and a robust arbitrary-CP converse. Two nearly parallel inputs whose ideal outputs are orthogonal prevent a processor from hiding the cost in discarded workspace or state-dependent success.
4. [Slater converse](gaussian_converse.md) constructs a different hard family containing only Slater determinants. Product Helstrom bounds and high-confidence discrimination with rejection give the unknown-Slater obstruction and its nonvanishing-success scale.
5. [Gaussian approximation](gaussian_approximation.md) proves an input-independent polar-unitary construction. Its normalized filtering path stays Slater, so the variance grows with the number of occupied modes rather than its square. This creates the explicit deterministic-versus-rare input-promise window.
6. [Implementation](implementation.md) charges SVD preprocessing, fermionic rotations, empty/occupied helpers, measurements and the precision needed after conditioning on rare success.
7. [Interpretation](interpretation.md) puts the two promises, thresholds, known-state bypass and remaining Gaussian frontier in one physical account.

The [related-work comparison](../references/RELATED_WORK.md) separates the contribution from earlier skin-effect conditioning, nonunitary circuits and discrimination tools. The [verification guide](../verification/README.md) documents finite scientific checks and their reproducibility limits.

Each theorem has one authoritative proof above. The central example is $`g_N=N^{-7/4}`$: deterministic trace error tends to zero on every unknown pure Slater, while fixed-error processing valid on all correlated fixed-number inputs has worst success at most $`\exp[-cN^{1/4}]`$ at the same prescribed time.
