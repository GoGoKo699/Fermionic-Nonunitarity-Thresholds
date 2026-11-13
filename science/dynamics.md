# Ballistic-time singular values of the fermionic propagator

The operational bounds use singular values of the **time propagator**, rather than the condition number of a matrix of Hamiltonian eigenvectors. This file proves the required finite-size estimates for a uniform open Hatano–Nelson chain. The estimates hold uniformly down to vanishing hopping asymmetry, with their additive remainder stated explicitly.

The imaginary-gauge transformation and the many-body scale $`g m(N-m)`$ are established foundations. In particular, [Shimomura and Sato, Physical Review Letters 133, 136502 (2024)](https://arxiv.org/abs/2403.13595) discuss the stronger many-body eigenvector conditioning and its dynamical consequences. The result below supplies a lower bound on the propagator itself at one specified time proportional to chain length. An eigenvector condition number alone is an upper-envelope estimate and does not supply that lower bound.

## Notation and constants

There are $`N\geq 3`$ sites and $`m\in\{0,\ldots,N\}`$ spinless fermions. Set $`\hbar=1`$. The hopping rate is $`J>0`$, and the asymmetry satisfies $`0\leq g\leq g_{\max}`$, where the cap $`g_{\max}\geq 0`$ is fixed independently of $`N`$.

The one-particle Hamiltonian and propagator are

```math
h_g
 =J\sum_{j=1}^{N-1}
 \left(e^g|j+1\rangle\langle j|
       +e^{-g}|j\rangle\langle j+1|\right),
\qquad
U_g(t)=e^{-it h_g}.
```

The propagator on the fixed-number sector is its exterior power:

```math
K_{N,m}(t)=\bigwedge\nolimits^m U_g(t).
```

All norms below are operator two-norms. For an invertible matrix $`A`$, write $`\kappa(A)=\|A\|\|A^{-1}\|`$. Singular values are in descending order.

Use the following numerical constants and finite-size quantities:

```math
\begin{aligned}
\delta&=\frac1{100},
&\alpha&=\frac{\delta}{32\cosh g_{\max}},
&t_N&=\frac{\alpha N}{J},\\
d_N&=\lfloor\delta N\rfloor,
&p_N&=d_N+1,
&x_N&=\frac{\delta N}{16},\\
\eta_N&=e^{x_N}\frac{x_N^{p_N}}{p_N!},
&\lambda&=\delta\left(\log16-\frac{17}{16}\right)>0.
\end{aligned}
```

The number of selected periodic Fourier modes and the number of useful singular values are

```math
\begin{aligned}
H_N&=\left\lfloor\frac{5N}{12}\right\rfloor
     -\left\lceil\frac{N}{12}\right\rceil+1,\\
q_{N,m}&=\min\{m,N-m\},\\
L_{N,m}&=\min\left\{q_{N,m},\,[H_N-2d_N]_+\right\},
\qquad [z]_+=\max\{z,0\}.
\end{aligned}
```

These definitions give an evaluable bound for every permitted $`N,m,g,J`$. The time coefficient is deliberately conservative; its numerical optimization is not part of the claim. Every native hopping amplitude is at most $`J e^{g_{\max}}`$.

## Finite-size theorem

**Theorem 1.** With the definitions above, put $`B_N(g)=\alpha N\sinh g`$. Then

```math
\boxed{
2L_{N,m}\log\!\left(
 \max\left\{1,e^{B_N(g)}-2\eta_N\right\}\right)
\ \leq\
\log\kappa\!\left(K_{N,m}(t_N)\right)
\ \leq\
2g m(N-m).
}
```

In particular, the following slightly weaker bound is convenient:

```math
\boxed{
2L_{N,m}\,[\alpha N\sinh g-4\eta_N]_+
\ \leq\
\log\kappa\!\left(K_{N,m}(t_N)\right)
\ \leq\
2g m(N-m).
}
```

The remainder obeys

```math
0\lt \eta_N
 \leq\left(\frac{e^{17/16}}{16}\right)^{p_N}
 \leq e^{-\lambda N},
\qquad
\eta_N\lt \frac14.
```

For $`g=0`$, the propagator is unitary and both upper and lower condition-number bounds equal zero after taking the logarithm. For $`m=0`$ or $`m=N`$, the sector has dimension one and the condition number is one. No positive-asymmetry asymptotic is imposed on these endpoints.

### 1. Imaginary gauge and the upper bound

Let

```math
S_g=\mathrm{diag}(e^{g},e^{2g},\ldots,e^{Ng}).
```

Direct substitution gives

```math
h_g=S_g h_0 S_g^{-1},
\qquad
U_g(t)=S_g U_0(t)S_g^{-1}.
```

The matrix $`U_0(t)`$ is unitary. On the fixed-number sector, $`S_{g,m}=\bigwedge^m S_g`$ is diagonal, with entries $`\exp(g\sum_{j\in I}j)`$ for occupied sets $`I`$ of size $`m`$. The largest and smallest occupied-position sums differ by $`m(N-m)`$. Consequently,

```math
\kappa(S_{g,m})=e^{g m(N-m)},
\qquad
\|K_{N,m}(t)\|\leq e^{g m(N-m)}.
```

The same estimate holds for the inverse. Hence, at every time,

```math
\kappa(K_{N,m}(t))\leq e^{2g m(N-m)}.
```

For one particle this also gives the useful all-time bound

```math
\kappa(U_g(t))\leq e^{2g(N-1)}.
```

### 2. Reciprocal singular values and exterior powers

The matrix $`h_g`$ is real. Therefore complex conjugation gives

```math
\overline{U_g(t)}=e^{it h_g}=U_g(t)^{-1}.
```

Complex conjugation leaves singular values unchanged, while inversion reciprocates and reverses their order. If $`s_1\geq\cdots\geq s_N`$ are the singular values of $`U_g(t)`$, it follows that

```math
s_j s_{N+1-j}=1
\quad(1\leq j\leq N).
```

Thus $`s_j\geq1`$ for $`j\leq\lfloor N/2\rfloor`$, and a possible middle singular value equals one.

The singular values of an exterior power are all products of the corresponding number of distinct one-particle singular values. In particular,

```math
\left\|\bigwedge\nolimits^m U_g(t)\right\|
 =\prod_{j=1}^m s_j
 =\prod_{j=1}^{q_{N,m}}s_j.
```

The second equality follows by cancelling reciprocal pairs; it includes the empty product when $`m=0`$ or $`m=N`$. Alternatively, the determinant has modulus one and the bottom $`N-m`$ singular values reciprocate the top $`N-m`$ values.

The exterior power also satisfies $`\overline{K_{N,m}(t)}=K_{N,m}(t)^{-1}`$. Hence

```math
\kappa(K_{N,m}(t))=\|K_{N,m}(t)\|^2.
```

It remains to find sufficiently many large one-particle singular values.

### 3. Periodic comparison

Close the chain into a ring with the same directed hopping, writing the resulting circulant matrix as $`h_g^{\mathrm{per}}`$. Choose the Fourier convention for which its eigenvalues are

```math
\zeta_k
 =2J\cosh(g)\cos\left(\frac{2\pi k}{N}\right)
  +2iJ\sinh(g)\sin\left(\frac{2\pi k}{N}\right),
\qquad k=0,\ldots,N-1.
```

A circulant matrix is unitarily diagonalized by the Fourier transform. Thus the periodic propagator is normal, with singular values

```math
\exp\left[
 2Jt\sinh(g)\sin\left(\frac{2\pi k}{N}\right)
\right].
```

For every integer $`k`$ in the interval $`[N/12,5N/12]`$, the sine is at least $`1/2`$. There are exactly $`H_N`$ such integers. At $`t=t_N`$, at least $`H_N`$ periodic singular values are therefore at least $`e^{B_N(g)}`$.

This periodic calculation is a comparison tool. The theorem concerns the open-chain propagator, and the resource obstruction is not asserted to be a topology-specific diagnostic.

### 4. A finite-rank difference plus a controlled tail

Let $`P_d(z)=\sum_{k=0}^d z^k/k!`$. Both open and periodic one-particle Hamiltonians obey

```math
\|h_g\|,\ \|h_g^{\mathrm{per}}\|
 \leq J(e^g+e^{-g})
 \leq 2J\cosh g_{\max}.
```

At $`t_N`$, the product of the last bound and time equals $`x_N`$. The exponential-series remainder therefore gives, for either Hamiltonian,

```math
\left\|e^{-it_N h}-P_{d_N}(-it_N h)\right\|
 \leq e^{x_N}\frac{x_N^{p_N}}{p_N!}
 =\eta_N.
```

For completeness, the scalar majorant follows from

```math
\sum_{k=p}^{\infty}\frac{x^k}{k!}
 \leq \frac{x^p}{p!}\sum_{\ell=0}^{\infty}\frac{x^\ell}{\ell!}
 =e^x\frac{x^p}{p!},
\qquad x\geq0.
```

The difference between the two degree-$`d_N`$ polynomials has rank at most $`2d_N`$. To see this, expand a matrix power as a sum over walks. An open and periodic walk of length at most $`d_N`$ can differ only if the periodic walk crosses the removed edge. Its input site must then lie among the first $`d_N`$ or last $`d_N`$ sites. Every other input column of the polynomial difference is zero. Since $`d_N\lt N/2`$, these boundary sets are disjoint. The argument also covers $`d_N=0`$, when the polynomial difference vanishes.

Consequently,

```math
U_g(t_N)
 =U_g^{\mathrm{per}}(t_N)+R_N+E_N,
\qquad
\mathrm{rank}R_N\leq2d_N,
\qquad
\|E_N\|\leq2\eta_N.
```

The remainder is exponentially small with an explicit rate. Since $`p_N>\delta N`$ and $`x_N=\delta N/16\lt p_N/16`$, the elementary factorial inequality gives

```math
\begin{aligned}
\eta_N
&\leq e^{x_N}\left(\frac{e x_N}{p_N}\right)^{p_N}\\
&\leq\left(\frac{e^{17/16}}{16}\right)^{p_N}
 \leq\exp\left[-\delta N\left(\log16-\frac{17}{16}\right)\right].
\end{aligned}
```

The base $`e^{17/16}/16`$ is less than $`1/4`$, so $`\eta_N\lt 1/4`$ for all $`N\geq3`$.

### 5. Singular-value interlacing and the lower bound

We use the following elementary form of singular-value interlacing. If $`\mathrm{rank}R\leq r`$ and $`\|E\|\leq e`$, then

```math
s_j(A+R+E)\geq s_{j+r}(A)-e,
\qquad 1\leq j\leq N-r.
```

One proof takes the span of the first $`j+r`$ right singular vectors of $`A`$ and intersects it with $`\ker R`$. The intersection has dimension at least $`j`$. On that subspace, $`A+R=A`$, whose least norm is at least $`s_{j+r}(A)`$. The perturbation $`E`$ subtracts at most $`e`$, and the max–min characterization of singular values proves the assertion.

Apply this statement with the periodic propagator as $`A`$. At least $`[H_N-2d_N]_+`$ open-chain singular values satisfy

```math
s_j(U_g(t_N))\geq e^{B_N(g)}-2\eta_N.
```

In the exterior-power norm, at most $`q_{N,m}\leq\lfloor N/2\rfloor`$ factors are needed. Every one of those factors is at least one by reciprocal pairing. At least $`L_{N,m}`$ factors also satisfy the last displayed bound. Therefore

```math
\|K_{N,m}(t_N)\|
 \geq\left(\max\{1,e^{B_N(g)}-2\eta_N\}\right)^{L_{N,m}}.
```

Squaring the norm gives the first lower bound in Theorem 1.

For the simpler bound, write

```math
\log(e^{B_N(g)}-2\eta_N)
 =B_N(g)+\log(1-2\eta_N e^{-B_N(g)})
 \geq B_N(g)-4\eta_N.
```

Here $`0\leq2\eta_N e^{-B_N(g)}\lt 1/2`$, and $`\log(1-z)\geq-2z`$ on that interval. Combining with the exact lower bound of one for the relevant singular values proves the positive-part version. This completes the proof.

## Uniform bounds at finite filling

Fix $`0\lt \nu\leq1/2`$ and restrict to nonempty integer sectors satisfying

```math
\nu N\leq m\leq(1-\nu)N.
```

Define

```math
\theta=\frac13-2\delta,
\qquad
\ell_\nu=\min\left\{\nu,\frac\theta2\right\},
\qquad
c_{\nu,g_{\max}}=2\alpha\ell_\nu>0.
```

The exact Fourier count satisfies $`H_N\geq N/3-1`$, so

```math
H_N-2d_N\geq\theta N-1.
```

For $`N\geq7`$, this is at least $`\theta N/2`$. It follows that $`L_{N,m}\geq\ell_\nu N`$. Theorem 1 then yields the useful uniform estimate

```math
\boxed{
\left[c_{\nu,g_{\max}}\,gN^2-8N\eta_N\right]_+
\ \leq\
\log\kappa(K_{N,m}(t_N))
\ \leq\
\frac12 gN^2,
\qquad N\geq7.
}
```

This formula states precisely what is retained when $`g`$ vanishes. For example, whenever

```math
gN^2\geq\frac{16}{c_{\nu,g_{\max}}}\,N\eta_N,
```

one has

```math
\frac12 c_{\nu,g_{\max}}\,gN^2
\leq\log\kappa(K_{N,m}(t_N))
\leq\frac12 gN^2.
```

Thus $`\log\kappa=\Theta_{\nu,g_{\max}}(gN^2)`$ in every regime covered by this explicit condition, including polynomially vanishing positive asymmetries. The exact finite-size inequality remains the statement at $`g=0`$ or at asymmetries too small to dominate the stated remainder.

The one-particle bound and the finite-filling lower bound have different consequences at $`g=\beta/N`$, for fixed $`\beta>0`$:

```math
\kappa(U_{\beta/N}(t_N))\leq e^{2\beta},
\qquad
\log\kappa(K_{N,m}(t_N))=\Theta_{\nu,\beta,g_{\max}}(N).
```

The first estimate is valid at every time. The second follows at the specified $`t_N`$ for all sufficiently large $`N`$ with $`\beta/N\leq g_{\max}`$.

## The intermediate asymmetry used for the input-promise separation

Set $`g_N=N^{-7/4}`$ and keep finite filling. For all $`N\geq7`$ with $`N^{-7/4}\leq g_{\max}`$, the directly evaluable bound is

```math
\left[c_{\nu,g_{\max}}N^{1/4}-8N\eta_N\right]_+
\leq\log\kappa(K_{N,m}(t_N))
\leq\frac12N^{1/4}.
```

Since $`\eta_N\leq e^{-\lambda N}`$, the remainder is negligible compared with $`N^{1/4}`$. No limit involving a fixed positive asymmetry is used here.

An optional explicit sufficient size bound can be given. Let

```math
M_\lambda=\left(\frac{3}{2e\lambda}\right)^{3/4},
\qquad
N_*=\left\lceil
\max\left\{
 7,\,
 \frac2\lambda\log\left(\frac{16M_\lambda}{c_{\nu,g_{\max}}}\right)
\right\}
\right\rceil.
```

For every $`N\geq N_*`$, the inequality

```math
N^{3/4}e^{-\lambda N}
\leq M_\lambda e^{-\lambda N/2}
\leq\frac{c_{\nu,g_{\max}}}{16}
```

holds. The first step maximizes $`x^{3/4}e^{-\lambda x/2}`$ over $`x>0`$. Consequently, also imposing the asymmetry cap gives

```math
\frac12c_{\nu,g_{\max}}N^{1/4}
\leq\log\kappa(K_{N,m}(t_N))
\leq\frac12N^{1/4}.
```

The success bounds for unrestricted inputs therefore have an $`\exp[-\Theta(N^{1/4})]`$ scale in this window. The separate Slater-input approximation uses its own variance bound; the singular-value result alone does not assert that an approximate simulator on a restricted input manifold must pay the unrestricted condition-number cost.

## Scope of the dynamical statement

The chain is uniform, open, number conserving and noninteracting. Its one-particle Hamiltonian is fully known. The lower bound holds at the displayed time $`t_N`$; it is not a lower bound at every time, and recurrences are not excluded. It concerns the complete fixed-number propagator, rather than a selected density profile or observable. Preparation from a known state, a classical description of a Slater determinant, multiple supplied copies and modified unconditional feedback dynamics are distinct tasks.
