# Four modes: one complete filter experiment

This finite example follows a supplied quantum input through a known filter, a success flag and a final measurement. It also shows why the input promise matters. **The diagonal matrix below is a teaching toy, not the uniform Hatano–Nelson propagator.** It proves no chain-length threshold or asymptotic exponent.

Use four fermionic modes and exactly two particles. Write $`|ij\rangle=e_i\wedge e_j`$ for $`i\lt j`$. The six occupation states span the sector.

## 1. Specify the known transformation

Choose the positive one-particle matrix

```math
U=\mathrm{diag}
\left(\sqrt2,\frac1{\sqrt2},\sqrt2,\frac1{\sqrt2}\right).
```

Its polar unitary is $`W=I`$. Put $`b=\frac12\log2`$, so its positive logarithm is $`B=\mathrm{diag}(b,-b,b,-b)`$. The two-particle map is $`K=\bigwedge^2U`$: each occupation amplitude is multiplied by the product of its occupied one-particle factors.

| Occupation | $`K`$ amplitude | Accepted $`F=K/2`$ amplitude | Success probability on that occupation |
|---|---:|---:|---:|
| $`\lvert12\rangle`$ | $`1`$ | $`1/2`$ | $`1/4`$ |
| $`\lvert13\rangle`$ | $`2`$ | $`1`$ | $`1`$ |
| $`\lvert14\rangle`$ | $`1`$ | $`1/2`$ | $`1/4`$ |
| $`\lvert23\rangle`$ | $`1`$ | $`1/2`$ | $`1/4`$ |
| $`\lvert24\rangle`$ | $`1/2`$ | $`1/4`$ | $`1/16`$ |
| $`\lvert34\rangle`$ | $`1`$ | $`1/2`$ | $`1/4`$ |

The largest singular value of $`K`$ is two and the smallest is one half. Thus $`\kappa(K)=4`$. The exact universal filtering theorem gives optimal **zero-error** worst-input success $`\kappa(K)^{-2}=1/16`$. This is a worst-input statement, not the success on every input.

## 2. Build the physical accepted branch

The full-Fock SVD normalizer is the product of one-particle singular values above one:

```math
C=\sqrt2\,\sqrt2=2.
```

Apply these four one-mode filters in the occupation basis:

| Mode | Filter on $`(\lvert0\rangle,\lvert1\rangle)`$ | Supplied helper | Accepted helper outcome |
|---|---|---|---|
| 1 and 3 | $`\mathrm{diag}(1/\sqrt2,1)`$ | Occupied | Occupied |
| 2 and 4 | $`\mathrm{diag}(1,1/\sqrt2)`$ | Empty | Empty |

Each is a beam-splitter interaction with angle $`\pi/4`$ and its helper, followed by occupation measurement. The first type attenuates a hole; the second attenuates a particle. Accept only if all four helper outcomes match the last column. The accepted data operator is exactly $`F=K/2`$.

On acceptance the helpers return to their supplied occupations. Other records are failures and may consume the unknown payload. In a qubit occupation encoding this requires four data qubits and up to four helper qubits for this direct construction; helper preparation, gates and all four measurements count.

## 3. Supply an unknown Slater carrying two signs

A source secretly chooses $`s_1,s_2\in\{+1,-1\}`$ independently and uniformly and supplies the two occupied orbitals

```math
v_{1,s_1}=\frac{s_1e_1+2e_2}{\sqrt5},
\qquad
v_{2,s_2}=\frac{s_2e_3+2e_4}{\sqrt5}.
```

They are normalized and have disjoint supports. Their exterior product is therefore a genuine Slater:

```math
|\psi_{s_1,s_2}\rangle
=\frac{
 s_1s_2|13\rangle+2s_1|14\rangle
 +2s_2|23\rangle+4|24\rangle}{5}.
```

The processor knows $`U`$ but is not told the two signs or the occupied-orbital description. The family is used to specify a possible hidden input; the processor does not learn it before acting.

Applying the accepted filter gives

```math
F|\psi_{s_1,s_2}\rangle
=\frac{
 s_1s_2|13\rangle+s_1|14\rangle
 +s_2|23\rangle+|24\rangle}{5}.
```

The four components are orthogonal, so the success probability is

```math
p_{\rm succ}=\frac4{25}=0.16.
```

After normalization, the retained output is

```math
|\omega_{s_1,s_2}\rangle
=\frac{s_1e_1+e_2}{\sqrt2}
 \wedge
 \frac{s_2e_3+e_4}{\sqrt2}.
```

The conditional trace error is zero. A target-basis rotation in each mode pair, followed by occupation measurement, returns both signs perfectly on every accepted run. The four $`\omega`$ states are orthogonal. The unconditional probability of both acceptance and a correct full string is still only $`4/25`$.

## 4. Check that information was not obtained for free

The two sign choices within one input pair have root overlap $`3/5`$. Their equal-prior binary minimum-error success is $`9/10`$. For the independent two-sign ensemble, even collective decoding has full-string guessing probability $`(9/10)^2=81/100`$; the project proves this product statement with an explicit SDP dual.

The filter's perfect conditional decoding accepts only $`16\%`$ of attempts, so it does not contradict that $`81\%`$ unconditional guessing limit. In fact, exact unambiguous decoding of this four-state product family has success $`(1-3/5)^2=4/25`$, matching this filter on the family. For the standard Gram-matrix criterion, the one-pair Gram eigenvalues are $`1\pm3/5`$; the two-pair tensor Gram matrix therefore has minimum eigenvalue $`(2/5)^2=4/25`$.

These numbers illustrate the distinction between confidence after acceptance and the probability of obtaining an accepted answer. They do not assert the optimum for every allowed nonzero error.

## 5. Compare the deterministic polar approximation

Here $`W=I`$, so the polar-unitary construction simply returns the supplied state and always succeeds. For the Slater family above,

```math
|\langle\psi_{s_1,s_2}|\omega_{s_1,s_2}\rangle|
=\left(\frac3{\sqrt{10}}\right)^2
=\frac9{10}.
```

With the project's half-trace convention, its error is

```math
D(\psi_{s_1,s_2},\omega_{s_1,s_2})
=\sqrt{1-\left(\frac9{10}\right)^2}
=\frac{\sqrt{19}}{10}
\approx0.435890.
```

The uniform theorem for **every** pure two-particle Slater gives the valid upper bound

```math
\sqrt{\min(2,4-2)}\,\|B\|
=\frac{\log2}{\sqrt2}
\approx0.490129.
```

The exact heralded filter and the deterministic approximation solve different accuracy/success requirements. The latter can be useful at a chosen error tolerance; its vanishing-error chain regime requires the separate asymptotic proof.

## 6. An allowed correlated input outside the Slater promise

Let $`x=|24\rangle`$ and $`y=|13\rangle`$. Consider

```math
|\chi_\pm\rangle
=\frac{4x\pm y}{\sqrt{17}}.
```

These are valid two-fermion states, but not Slaters. Their one-particle density matrix has eigenvalues $`1/17,1/17,16/17,16/17`$, whereas a pure Slater's one-particle density is a projector.

The input overlap and normalized target outputs are

```math
\langle\chi_+|\chi_-\rangle=\frac{15}{17},
\qquad
\frac{K|\chi_\pm\rangle}{\|K\chi_\pm\|}
=\frac{x\pm y}{\sqrt2}.
```

The targets are orthogonal. The same filter accepts these two inputs with probability $`2/17\approx0.117647`$, and its conditional output is exact. This is the familiar probabilistic state-separation mechanism behind the general converse.

Returning the input unchanged instead has error

```math
D\!\left(\chi_\pm,\frac{x\pm y}{\sqrt2}\right)
=\frac3{\sqrt{34}}
\approx0.514496.
```

That exceeds the pure-Slater upper bound above without contradicting it: these inputs do not satisfy its promise. This one toy does not prove that every deterministic approximate processor fails at that tolerance. The project's universal converse and its large-$`N`$ promise separation require their own quantifiers and proofs.

## What carries over to the chain

The example makes the accepted operator, helper normalization, conditional output, success probability and final measurement explicit. In the actual chain, singular modes replace these four diagonal orbitals, and known Gaussian basis changes must be compiled and charged. The many-mode proof determines how many singular-mode pairs exist at its specified time.

The source may supply an unknown pure Slater or an arbitrary correlated state; it does not supply a classical state description. Failure can destroy that specimen. Reading inverse success as a repetition cost requires fresh identical specimens and is a different source-access assumption.

Continue with the [Watrous bridge](WATROUS_BRIDGE.md), the [30-milestone route](MILESTONES.md), or the [scientific model](../science/model.md).
