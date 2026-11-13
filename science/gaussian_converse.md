# A converse using only unknown Slater determinants

The [all-input filtering converse](heralding.md) uses a superposition of two extremal many-body singular vectors. That superposition need not be Gaussian. This page constructs a different hard family consisting entirely of pure Slater determinants and proves bounds for arbitrary heralded quantum processors on that promise.

The simulator receives **one unknown Slater specimen**, without its occupied-orbital description, a preparation oracle, or extra copies. The success map may nevertheless use arbitrary ancillas, non-Gaussian operations, measurements, and feedback. The converse therefore does not restrict the receiver to Gaussian processing.

Accuracy is conditional half-trace distance at most $`0\lt \epsilon\lt 1/2`$ on every allowed input. Success may depend on the input, and $`p_{\min}`$ denotes its infimum over all Slaters in the fixed-number sector.

## Finite singular-mode assumptions

Let $`U`$ be an invertible one-particle transformation on $`N`$ modes, with $`K=\bigwedge^m U`$. Suppose there are $`r`$ disjoint low/high right-singular-mode pairs $`(x_j,y_j)`$ with ratios

```math
k_j=\frac{s_{j,\mathrm{high}}}{s_{j,\mathrm{low}}}>1,
\qquad
r\leq\min\{m,N-m\}.
```

Choose $`m-r`$ fixed spectator singular modes outside these pairs. The displayed bound on $`r`$ makes this possible.

For each sign string $`s\in\{+1,-1\}^r`$, occupy the orbitals

```math
v_{j,s_j}
=\frac{x_j+s_j k_j^{-1}y_j}{\sqrt{1+k_j^{-2}}},
\qquad
q_j=\frac{1}{1+k_j^2}\in(0,1/2),
```

along with the spectators. The pair supports are disjoint, so the occupied orbitals are orthonormal and their exterior product is a normalized Slater.

After applying $`U`$, the two components in pair $`j`$ have equal magnitude. In the left-singular-mode basis the normalized occupied output orbital is

```math
w_{j,s_j}
=\frac{u_{j,\mathrm{low}}+s_j u_{j,\mathrm{high}}}{\sqrt2}.
```

Consequently all $`2^r`$ ideal output Slaters are orthonormal. The common spectator factor cancels on normalization.

The input family, represented in its pair-occupation subspace, is exactly

```math
|\Psi_s\rangle
=\bigotimes_{j=1}^r
 \left(\sqrt{1-q_j}\,|0\rangle
       +s_j\sqrt{q_j}\,|1\rangle\right).
```

This tensor notation is an isometry of the dual-rail fixed-number subspace. It does not replace fermionic antisymmetry by distinguishable-particle physics.

## From accurate processing to discrimination

Follow a putative successful simulator by the orthogonal ideal-output-basis measurement, assigning any outcome in the remaining subspace an arbitrary guessed string. On every hard input, conditional trace accuracy implies a correct full-string outcome with probability at least $`1-\epsilon`$ after acceptance. Thus the composition is a discriminator with a rejection outcome and

```math
Q\geq(1-\epsilon)p,
\qquad
p\geq p_{\min},
```

where $`p`$ and $`Q`$ are its uniform-ensemble acceptance probability and joint correct-and-accepted probability.

This reduction charges no extra resource to the physical simulator: the final measurement is part of an information-theoretic converse. It does not require the simulator to know the secret sign string. Discrimination of geometrically uniform states and fixed-inconclusive-rate discrimination are established tools; the proofs below specify the particular estimates needed here. See [related work](../references/RELATED_WORK.md).

## Product Helstrom bound

For one pair, put $`a=\sqrt{1-q},b=\sqrt q`$. The optimal equal-prior binary correct probability is

```math
h(q)=\frac{(a+b)^2}{2}
=\frac{1+2\sqrt{q(1-q)}}2.
```

The optimal probability of guessing the **entire** independent sign string is

```math
P_{\mathrm{guess}}^\star
=\prod_{j=1}^r h(q_j),
```

including collective measurements. To verify this multiplication, the one-pair discrimination SDP has the feasible dual operator

```math
Y=\frac{a+b}{2}
\begin{pmatrix}a&0\\0&b\end{pmatrix},
\qquad
Y-\frac{|\phi_\pm\rangle\langle\phi_\pm|}{2}
=\frac{ab}{2}
\begin{pmatrix}1&\mp1\\\mp1&1\end{pmatrix}
\succeq0.
```

Its trace is $`h(q)`$. Tensoring the dual operators preserves the required positive-semidefinite domination for each product hypothesis. Product binary Helstrom measurements attain the tensor dual value. Thus collective decoding cannot exceed the product.

Complete any rejection outcomes by arbitrary guesses. This cannot lower the correct probability, so the simulator must obey the finite bound

```math
\boxed{\displaystyle
p_{\min}\leq
\min\left\{1,\frac{\prod_{j=1}^r h(q_j)}{1-\epsilon}\right\}.}
```

In particular, if $`q_j\leq q_{\max}\lt 1/2`$, then

```math
p_{\min}\leq
\min\left\{1,\frac{h(q_{\max})^r}{1-\epsilon}\right\}.
```

This bound is useful when the individual pair asymmetry is weak or constant. It saturates at an $`e^{-\Theta(r)}`$ exponent as $`q_{\max}\to0`$ and therefore does not establish the stronger fixed-positive-$`g`$ law by itself.

## High confidence with abstention

Write $`d=2^r`$, label the pair-occupation basis by $`x\in\{0,1\}^r`$, and define

```math
\lambda_x=\prod_{j=1}^r q_j^{x_j}(1-q_j)^{1-x_j},
\qquad
|\Psi_0\rangle=\sum_x\sqrt{\lambda_x}\,|x\rangle.
```

The inputs form the orbit $`|\Psi_s\rangle=Z_s|\Psi_0\rangle`$ of the phase group $`\mathbb Z_2^r`$. Average the discriminator over that group, translating its guessed label accordingly. This preserves average acceptance and average correct weight, and makes acceptance common to every group-related input. It is a mathematical symmetrization of an unrestricted measurement, not an assumption of free physical controls.

Let its conclusive effects be $`E_s=Z_sE_0Z_s`$. Compression to the hard subspace preserves

```math
\sum_s E_s=d\,\mathrm{diag}(E_0)\preceq I.
```

Writing $`a_x=d(E_0)_{xx}\in[0,1]`$, the two relevant probabilities are

```math
p=\sum_x\lambda_xa_x,
\qquad
Q=\langle\Psi_0|E_0|\Psi_0\rangle
\leq\frac1d
 \left(\sum_x\sqrt{\lambda_xa_x}\right)^2.
```

The inequality follows from positivity, $`|(E_0)_{xy}|\leq\sqrt{(E_0)_{xx}(E_0)_{yy}}`$.

Choose any $`q_{\max}\lt b\lt 1/2`$ and put

```math
L=\{x:|x|\leq\lfloor br\rfloor\},
\qquad
D_L=|L|,
\qquad
R=\sum_{x\notin L}\lambda_x.
```

Cauchy–Schwarz separately on the two sets gives

```math
\sum_{x\in L}\sqrt{\lambda_xa_x}\leq\sqrt{D_Lp},
\qquad
\sum_{x\notin L}\sqrt{\lambda_xa_x}\leq\sqrt{dR}.
```

It follows that

```math
(1-\epsilon)p
\leq Q
\leq\left(\sqrt{\frac{D_L}{d}p}+\sqrt R\right)^2.
```

Whenever $`D_L/d\lt 1-\epsilon`$, this yields the explicit finite bound

```math
\boxed{\displaystyle
p_{\min}\leq p
\leq
\min\left\{1,\,
\frac{R}
 {\left[\sqrt{1-\epsilon}-\sqrt{D_L/2^r}\right]^2}
\right\}.}
```

No equal-success assumption was imposed on the original simulator. Symmetrization uses its average success, which remains at least its worst-input success.

### Explicit dimension and tail estimates

Let binary relative entropy, with natural logarithms, be

```math
d_{\mathrm B}(b\Vert q)
=b\log\frac bq+(1-b)\log\frac{1-b}{1-q}.
```

The low-weight dimension is a fair-binomial lower tail. The weights $`\lambda_x`$ give independent, generally nonidentical Bernoulli variables with parameters at most $`q_{\max}`$. Chernoff bounds and stochastic domination therefore imply

```math
\frac{D_L}{2^r}
\leq e^{-r d_{\mathrm B}(b\Vert 1/2)},
\qquad
R\leq e^{-r d_{\mathrm B}(b\Vert q_{\max})}.
```

The floor in $`L`$ needs no asymptotic replacement: $`|x|\leq\lfloor br\rfloor`$ implies $`|x|\leq br`$, and its complement is exactly $`|x|>br`$. Thus, whenever the displayed denominator is positive,

```math
\boxed{\displaystyle
p_{\min}\leq
\min\left\{1,\,
\frac{e^{-r d_{\mathrm B}(b\Vert q_{\max})}}
 {\left[
 \sqrt{1-\epsilon}
 -e^{-\frac r2d_{\mathrm B}(b\Vert 1/2)}
 \right]^2}
\right\}.}
```

This is the finite high-confidence-with-rejection estimate used below. Ordinary minimum-error discrimination would lose its stronger exponent.

## Apply the singular-mode supply of the chain

The [dynamics theorem](dynamics.md) gives, at the specified ballistic time, the Fourier count $`H_N`$, boundary degree $`d_N`$ and remainder $`\eta_N`$. Put

```math
a_N=e^{\alpha N\sinh g}-2\eta_N,
\qquad
A_N=[H_N-2d_N]_+,
\qquad
0\lt \eta_N\leq e^{-\lambda N},
```

Then at least $`A_N`$ open-chain singular values are at least $`a_N`$. Reciprocal pairing supplies the matching low singular values. Whenever $`a_N>1`$, choose

```math
r=\min\{m,N-m,A_N\}=L_{N,m},
\qquad
k_j\geq a_N^2,
\qquad
q_j\leq q_{\max,N}:=\frac{1}{1+a_N^4}.
```

At fixed filling, $`r=\Theta(N)`$. Here $`p_{\mathrm{Sl}}^\star(\epsilon)=p^*_\epsilon(K;\mathcal P_{\mathrm{Sl}})`$ in the [model](model.md). If $`a_N\leq1`$, this particular lower-bound witness supplies no positive gap; the finite theorem must not be replaced by an artificial asymptotic claim at an exponentially small $`g`$.

### Fixed positive asymmetry

Fix $`g>0`$. Then $`\log(1/q_{\max,N})=\Theta_g(N)`$. Set $`b=1/4`$ for all sufficiently large $`N`$. Since

```math
d_{\mathrm B}(b\Vert q)\geq b\log(1/q)-h_{\mathrm B}(b),
\qquad
h_{\mathrm B}(b)=-b\log b-(1-b)\log(1-b),
```

the rejection tail is $`\exp[-\Omega_g(N^2)]`$, while the denominator tends to $`1-\epsilon>0`$. Therefore every processor accurate on all unknown Slaters has

```math
p_{\min}\leq e^{-c_gN^2}
```

for large $`N`$. The [Gaussian attenuation compiler](implementation.md) attains $`p_{\min}\geq e^{-C_gN^2}`$. Consequently the optimized Slater-promise success has the matching order

```math
p_{\mathrm{Sl}}^\star(\epsilon)
=\exp[-\Theta_{g,\epsilon}(N^2)]
\qquad(g>0\ \text{fixed}).
```

### Asymmetry $`g_N=\beta/N`$

Fix $`\beta>0`$. Now

```math
a_N\longrightarrow e^{\alpha\beta}>1,
\qquad
q_{\max,N}\longrightarrow
q_\beta=\frac{1}{1+e^{4\alpha\beta}}\lt \frac12.
```

The product Helstrom bound already yields $`p_{\min}\leq e^{-c_\beta N}`$. Equivalently, the rejection estimate works with any fixed $`b\in(q_\beta,1/2)`$ for sufficiently large $`N`$. The attenuation compiler gives the reverse exponential order, so

```math
p_{\mathrm{Sl}}^\star(\epsilon)
=\exp[-\Theta_{\beta,\epsilon}(N)].
```

These constants depend on $`\beta`$; this is not a uniform exponent as $`\beta\to0`$.

At the same time, the one-particle similarity bound gives

```math
\kappa(U_g(t))\leq e^{2g(N-1)}\leq e^{2\beta},
```

so exact one-particle worst-input success is at least $`e^{-4\beta}`$. Thus constant one-particle conditioning is compatible with exponentially small finite-density success even for the unknown-Slater promise.

## The constant-success Slater scale

The full Gaussian probability frontier is not established in every vanishing-$`g`$ regime. A matched **constant-success asymmetry scale** nevertheless follows from the product bound and the [polar-unitary construction](gaussian_approximation.md).

For the converse, define

```math
t_{\min,N}
=\frac{a_N^4-1}{a_N^4+1}
=\tanh(2\log a_N).
```

Since $`\sqrt{1-t^2}\leq1-t^2/2`$,

```math
h(q_{\max,N})
=\frac{1+\sqrt{1-t_{\min,N}^2}}2
\leq e^{-t_{\min,N}^2/4}.
```

Every accurate simulator therefore satisfies the unified finite estimate

```math
\boxed{\displaystyle
p_{\min}
\leq\min\left\{1,\,
\frac{\exp[-r\tanh^2(2\log a_N)/4]}{1-\epsilon}
\right\}.}
```

Suppose $`p_{\min}\geq p_0>0`$ and put

```math
L_{\epsilon,p_0}
=\log\frac{1}{(1-\epsilon)p_0}.
```

Whenever $`a_N>1`$ and $`2\sqrt{L_{\epsilon,p_0}/r}\lt 1`$, inversion gives

```math
\log a_N
\leq
\frac12\mathrm{artanh}
 \left(2\sqrt{\frac{L_{\epsilon,p_0}}r}\right).
```

Since $`\eta_N\lt 1/4`$, writing $`x=\alpha N\sinh g`$ gives

```math
\log a_N
=x+\log(1-2\eta_Ne^{-x})
\geq x-4\eta_N.
```

Since $`\sinh g\geq g`$, this yields the explicit necessary condition

```math
g
\leq
\frac{
\frac12\mathrm{artanh}
 \left(2\sqrt{L_{\epsilon,p_0}/r}\right)
+4\eta_N}
{\alpha N}.
```

If $`a_N\leq1`$, then $`x\leq\log(1+2\eta_N)\leq2\eta_N`$, which already gives an exponentially smaller $`g`$. Because $`r=\Theta(N)`$, both cases imply

```math
g_N=O_{\epsilon,p_0}(N^{-3/2})
```

for fixed filling, hopping cap, and ballistic-time coefficient.

Conversely, the polar-unitary channel is deterministic and its uniform Slater trace error is at most

```math
\sqrt{\min\{m,N-m\}}\,g_N(N-1).
```

A sufficiently small $`\epsilon`$-dependent constant times $`N^{-3/2}`$ therefore suffices. Together these statements locate the constant-success scale at $`N^{-3/2}`$. Constants may depend on the required accuracy and success; no sharp coefficient at the crossover is claimed.

For arbitrary correlated fixed-number pure inputs the corresponding scale is $`N^{-2}`$, as shown in [heralding](heralding.md) and [approximation](gaussian_approximation.md). In particular, in the window

```math
N^{-2}\ll g_N\ll N^{-3/2},
```

the polar unitary approximates every Slater with error tending to zero, while every simulator with fixed conditional error on all correlated inputs has worst success tending to zero. For $`g_N=N^{-7/4}`$, the all-input bound is $`\exp[-\Theta(N^{1/4})]`$, whereas the deterministic Slater error is $`O(N^{-1/4})`$.

## Boundaries and attribution

The fixed-positive-$`g`$ and $`\beta/N`$ probability laws are matched in exponential order. In the regime $`g_NN\to0`$, the Helstrom witness has a natural $`g_N^2N^3`$ scale, while generic exact filtering may pay a $`g_NN^2`$ scale. These facts do not establish a matching Gaussian success-probability function between the named regimes. In particular, the all-input polynomial-yield criterion must not be assigned to the Slater promise.

The Slater hard family is prepared by rotations in disjoint singular-mode pairs and a common orbital basis change. At $`g_N=\beta/N`$, all pair angles are constants depending on $`\beta`$ and the chosen modes; no exponentially small coefficient is required. The known basis change, its classical factorization, and gate synthesis remain charged in the [implementation account](implementation.md). The simulator does not receive the secretly selected pair signs or an orbital description.

Product binary Helstrom discrimination, geometrically uniform orbit symmetrization, and discrimination with inconclusive outcomes are prior machinery. Chefles–Barnett and Chefles–Jozsa–Winter supply the probabilistic-transformation framework; Nakahira–Usuda–Kato analyze geometrically uniform discrimination with fixed inconclusive rates. The present application combines those tools with the chain's finite-time singular-mode supply and the input-promise comparison. It is not a new general theory of state discrimination.

