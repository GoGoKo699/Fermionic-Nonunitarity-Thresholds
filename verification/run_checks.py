#!/usr/bin/env python3
"""Deterministic finite checks of the scientific identities; not asymptotic proofs."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm, polar, svd

SEED = 20261113
TOL = 5e-10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, 2))


def clean(value):
    """Stable JSON representation; no timings, paths, or machine identifiers."""
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (float, np.floating)):
        require(math.isfinite(float(value)), "nonfinite result")
        return float(f"{float(value):.11g}")
    return value


def hn(n: int, g: float, periodic: bool = False) -> np.ndarray:
    h = np.diag(np.full(n - 1, np.exp(g)), -1).astype(complex)
    h += np.diag(np.full(n - 1, np.exp(-g)), 1)
    if periodic:
        h[0, n - 1] = np.exp(g)
        h[n - 1, 0] = np.exp(-g)
    return h


def taylor(a: np.ndarray, degree: int) -> np.ndarray:
    total = np.eye(a.shape[0], dtype=complex)
    term = total.copy()
    for k in range(1, degree + 1):
        term = term @ a / k
        total += term
    return total


def occupied_sets(n: int, m: int):
    return list(itertools.combinations(range(n), m))


def exterior(a: np.ndarray, m: int) -> np.ndarray:
    sets = occupied_sets(a.shape[0], m)
    if m == 0:
        return np.ones((1, 1), dtype=complex)
    return np.array(
        [[np.linalg.det(a[np.ix_(i, j)]) for j in sets] for i in sets],
        dtype=complex,
    )


def dgamma(b: np.ndarray, m: int) -> np.ndarray:
    """Independent occupation-basis construction using CAR signs."""
    n = b.shape[0]
    sets = occupied_sets(n, m)
    masks = [sum(1 << j for j in s) for s in sets]
    location = {mask: k for k, mask in enumerate(masks)}
    out = np.zeros((len(masks), len(masks)), dtype=complex)
    for col, mask in enumerate(masks):
        for j in range(n):
            if not (mask >> j) & 1:
                continue
            sign_j = -1 if (mask & ((1 << j) - 1)).bit_count() % 2 else 1
            after_j = mask ^ (1 << j)
            for i in range(n):
                if (after_j >> i) & 1 or b[i, j] == 0:
                    continue
                sign_i = -1 if (after_j & ((1 << i) - 1)).bit_count() % 2 else 1
                target = after_j | (1 << i)
                out[location[target], col] += sign_i * sign_j * b[i, j]
    return out


def slater(q: np.ndarray) -> np.ndarray:
    return np.array(
        [np.linalg.det(q[list(i), :]) for i in occupied_sets(*q.shape)],
        dtype=complex,
    )


def pure_trace_distance(x: np.ndarray, y: np.ndarray) -> float:
    x = x / np.linalg.norm(x)
    y = y / np.linalg.norm(y)
    # The density-matrix norm avoids cancellation when the vectors nearly agree.
    delta = np.outer(x, x.conj()) - np.outer(y, y.conj())
    return float(np.linalg.norm(delta, "nuc") / 2)


def check_boundary_comparison():
    cases = []
    worst_support = worst_tail_excess = worst_interlacing_excess = 0.0
    # These exercise the finite-degree lemma at nontrivial degrees; they do not
    # substitute these larger times for the conservative asymptotic theorem.
    parameters = [(9, 2, .12, .2), (12, 3, .18, .4), (16, 4, .15, .7)]
    # Also evaluate the actual theorem constants at a small size (d_N=0).
    alpha = .01 / (32 * np.cosh(.7))
    parameters.append((24, math.floor(.01 * 24), alpha * 24, .3))
    for n, degree, time, g in parameters:
        h0, hp = hn(n, g), hn(n, g, True)
        u0, up = expm(-1j * time * h0), expm(-1j * time * hp)
        p0, pp = taylor(-1j * time * h0, degree), taylor(-1j * time * hp, degree)
        difference = p0 - pp
        interior = difference[:, degree:n - degree] if degree else difference
        support_residual = opnorm(interior)
        singular = np.linalg.svd(difference, compute_uv=False)
        rank = int(np.sum(singular > 1e-11 * max(1.0, singular[0])))
        x = 2 * np.cosh(g) * time
        tail = math.exp(x) * x ** (degree + 1) / math.factorial(degree + 1)
        observed_tail = max(opnorm(u0 - p0), opnorm(up - pp))
        s0, sp = np.linalg.svd(u0, compute_uv=False), np.linalg.svd(up, compute_uv=False)
        rank_bound = 2 * degree
        interlacing_excess = float(np.max(sp[rank_bound:] - 2 * tail - s0[:n - rank_bound]))
        require(support_residual <= TOL, "Taylor difference has an interior input column")
        require(rank <= rank_bound, "boundary polynomial rank exceeds 2d")
        require(observed_tail <= tail + TOL, "matrix exponential exceeds scalar tail bound")
        require(interlacing_excess <= TOL, "rank-plus-tail singular-value comparison fails")
        worst_support = max(worst_support, support_residual)
        worst_tail_excess = max(worst_tail_excess, observed_tail - tail)
        worst_interlacing_excess = max(worst_interlacing_excess, interlacing_excess)
        cases.append({"N": n, "degree": degree, "time_Jt": time, "g": g,
                      "rank": rank, "rank_bound": rank_bound,
                      "observed_tail": observed_tail, "tail_bound": tail,
                      "uses_actual_theorem_time": n == 24})
    return {"status": "passed", "cases": cases,
            "max_interior_column_norm": worst_support,
            "max_tail_bound_excess": worst_tail_excess,
            "max_interlacing_excess": worst_interlacing_excess}


def check_exterior_and_fock():
    cases = []
    worst_fock = worst_pair = worst_logcond = 0.0
    for n, m, g, time in [(4, 2, .2, .6), (5, 2, .3, .7),
                          (6, 2, .4, .8), (6, 3, .2, .9)]:
        h = hn(n, g)
        u = expm(-1j * time * h)
        k = exterior(u, m)
        direct = expm(-1j * time * dgamma(h, m))
        s = np.linalg.svd(u, compute_uv=False)
        sk = np.linalg.svd(k, compute_uv=False)
        reciprocal_residual = float(np.max(np.abs(np.log(s) + np.log(s[::-1]))))
        expected_logcond = 2 * np.sum(np.log(s[:min(m, n - m)]))
        logcond = math.log(sk[0] / sk[-1])
        fock_residual = opnorm(k - direct)
        logcond_residual = abs(logcond - expected_logcond)
        require(fock_residual <= TOL, "exterior minors disagree with direct CAR evolution")
        require(reciprocal_residual <= TOL, "reciprocal singular-value pairing fails")
        require(logcond_residual <= TOL, "exterior singular product/condition identity fails")
        require(logcond <= 2 * g * m * (n - m) + TOL, "gauge condition upper bound fails")
        worst_fock = max(worst_fock, fock_residual)
        worst_pair = max(worst_pair, reciprocal_residual)
        worst_logcond = max(worst_logcond, logcond_residual)
        cases.append({"N": n, "m": m, "g": g, "time_Jt": time,
                      "fock_dimension": len(k), "log_condition": logcond})
    return {"status": "passed", "cases": cases,
            "max_exterior_vs_direct_fock_norm": worst_fock,
            "max_reciprocal_log_residual": worst_pair,
            "max_condition_identity_residual": worst_logcond}


def beam_splitter_kraus(amplitude: float, helper_occupation: int):
    sine = math.sqrt(max(0.0, 1 - amplitude ** 2))
    beam = np.eye(4, dtype=complex)
    beam[1, 1] = beam[2, 2] = amplitude
    beam[1, 2], beam[2, 1] = sine, -sine
    indices = [helper_occupation, 2 + helper_occupation]
    return beam[np.ix_(indices, indices)], opnorm(beam.conj().T @ beam - np.eye(4))


def check_gaussian_filter():
    cases = []
    worst_local = worst_unitary = worst_global = worst_half_optimal = 0.0
    hole_count = attenuation_count = 0
    for n, m, g, time in [(4, 2, .2, .6), (5, 2, .3, .7), (6, 3, .4, .8)]:
        u = expm(-1j * time * hn(n, g))
        v, s, rh = svd(u)
        factors = []
        for sj in s:
            if sj <= 1:
                factor, unitary_residual = beam_splitter_kraus(float(sj), 0)
                expected = np.diag([1.0, sj])
                attenuation_count += 1
            else:
                factor, unitary_residual = beam_splitter_kraus(float(1 / sj), 1)
                expected = np.diag([1 / sj, 1.0])
                hole_count += 1
            worst_local = max(worst_local, opnorm(factor - expected))
            worst_unitary = max(worst_unitary, unitary_residual)
            factors.append(np.diag(factor))
        diagonal = []
        for occupied in occupied_sets(n, m):
            occ = set(occupied)
            diagonal.append(np.prod([factors[j][int(j in occ)] for j in range(n)]))
        compiled = exterior(v, m) @ np.diag(diagonal) @ exterior(rh, m)
        normalizer = float(np.prod(np.maximum(1, s)))
        k = exterior(u, m)
        global_residual = opnorm(compiled - k / normalizer)
        sf = np.linalg.svd(compiled, compute_uv=False)
        log_pmin = float(2 * np.log(sf[-1]))
        a = g * (n - 1)
        log_success_lower = -2 * (n + m) * a
        require(global_residual <= TOL, "Gaussian filter has wrong exterior normalization")
        require(log_pmin >= log_success_lower - TOL, "uniform filter success lower bound fails")
        require(sf[0] <= 1 + TOL, "compiled success operator is not a contraction")
        worst_global = max(worst_global, global_residual)
        if 2 * m == n:
            optimal_residual = abs(math.log(normalizer) - float(np.sum(np.log(s[:m]))))
            require(optimal_residual <= TOL, "half-filling normalization is not optimal")
            worst_half_optimal = max(worst_half_optimal, optimal_residual)
        cases.append({"N": n, "m": m, "normalizer": normalizer,
                      "log_worst_success": log_pmin,
                      "log_conservative_success_lower": log_success_lower})
    require(hole_count > 0 and attenuation_count > 0, "both particle and hole filters must be exercised")
    require(worst_local <= TOL and worst_unitary <= TOL, "local helper filter identity fails")
    return {"status": "passed", "cases": cases,
            "particle_attenuation_factors": attenuation_count, "hole_attenuation_factors": hole_count,
            "max_local_kraus_residual": worst_local, "max_helper_unitarity_residual": worst_unitary,
            "max_global_filter_residual": worst_global,
            "max_half_filling_log_normalizer_residual": worst_half_optimal}


def check_wick_and_polar(rng):
    worst_wick = worst_trace_excess = worst_path_slater = 0.0
    cases = []
    for n, m, g, time in [(4, 2, .01, .7), (5, 2, .05, .6), (6, 3, .15, .5)]:
        u = expm(-1j * time * hn(n, g))
        w, positive = polar(u)
        eigenvalues, basis = np.linalg.eigh(positive)
        b = (basis * np.log(eigenvalues)) @ basis.conj().T
        d = dgamma(b, m)
        k, wm = exterior(u, m), exterior(w, m)
        for trial in range(4):
            q, _ = np.linalg.qr(rng.normal(size=(n, m)) + 1j * rng.normal(size=(n, m)))
            psi = slater(q)
            target = k @ psi
            approximation = wm @ psi
            actual_error = pure_trace_distance(target, approximation)
            bound = min(1.0, math.sqrt(min(m, n - m)) * opnorm(b))
            worst_trace_excess = max(worst_trace_excess, actual_error - bound)
            require(actual_error <= bound + TOL, "uniform pure-Slater polar trace bound fails")
            require(opnorm(b) <= g * (n - 1) + TOL, "oneparticle polar logarithm exceeds gauge bound")
            for path_time in [0.0, .5, 1.0]:
                evolved_orbitals = expm(path_time * b) @ q
                qt, _ = np.linalg.qr(evolved_orbitals)
                path_slater = slater(qt)
                path_state = expm(path_time * d) @ psi
                path_state /= np.linalg.norm(path_state)
                path_residual = pure_trace_distance(path_slater, path_state)
                worst_path_slater = max(worst_path_slater, path_residual)
                require(path_residual <= TOL, "normalized positive path left the Slater manifold")
                projector = qt @ qt.conj().T
                wick = float(np.trace(projector @ b @ (np.eye(n) - projector) @ b).real)
                mean = np.vdot(path_state, d @ path_state)
                full_variance = float((np.vdot(path_state, d @ d @ path_state) - abs(mean) ** 2).real)
                residual = abs(wick - full_variance)
                worst_wick = max(worst_wick, residual)
                require(residual <= TOL, "Wick variance disagrees with direct Fock variance")
                require(wick <= min(m, n - m) * opnorm(b) ** 2 + TOL,
                        "occupied/unoccupied-rank variance bound fails")
            cases.append({"N": n, "m": m, "g": g, "trial": trial,
                          "polar_trace_error": actual_error, "bound": bound})
    return {"status": "passed", "cases": cases,
            "max_Wick_vs_full_Fock_variance_residual": worst_wick,
            "max_polar_trace_bound_excess": worst_trace_excess,
            "max_normalized_path_vs_Slater_trace_distance": worst_path_slater}


def tensor(vectors):
    out = np.array([1.0], dtype=complex)
    for item in vectors:
        out = np.kron(out, item)
    return out


def binary_strings(r):
    return list(itertools.product([0, 1], repeat=r))


def binary_relative_entropy(b, q):
    return b * math.log(b / q) + (1 - b) * math.log((1 - b) / (1 - q))


def check_phase_ensemble(rng):
    ratios = np.array([1.3, 1.8, 2.4])
    q = 1 / (1 + ratios ** 2)
    r = len(q)
    u = np.diag(np.array([[1 / math.sqrt(k), math.sqrt(k)] for k in ratios]).ravel())
    k = exterior(u, r)
    output_columns = []
    states = []
    for bits in binary_strings(r):
        orbitals = np.zeros((2 * r, r), dtype=complex)
        pair_states = []
        for j, bit in enumerate(bits):
            sign = (-1) ** bit
            orbitals[2 * j, j] = math.sqrt(1 - q[j])
            orbitals[2 * j + 1, j] = sign * math.sqrt(q[j])
            pair_states.append(np.array([math.sqrt(1 - q[j]), sign * math.sqrt(q[j])]))
        require(opnorm(orbitals.conj().T @ orbitals - np.eye(r)) <= TOL,
                "hard-family orbitals are not a Slater frame")
        out = k @ slater(orbitals)
        output_columns.append(out / np.linalg.norm(out))
        states.append(tensor(pair_states))
    columns = np.column_stack(output_columns)
    orthogonal_residual = opnorm(columns.conj().T @ columns - np.eye(2 ** r))
    require(orthogonal_residual <= TOL, "normalized hard outputs are not orthogonal")
    dual_factors = []
    predicted_guess = 1.0
    for qj in q:
        a, b = math.sqrt(1 - qj), math.sqrt(qj)
        dual_factors.append((a + b) * np.diag([a, b]) / 2)
        predicted_guess *= (a + b) ** 2 / 2
    dual = dual_factors[0]
    for item in dual_factors[1:]:
        dual = np.kron(dual, item)
    min_dual_eigenvalue = math.inf
    attained_guess = 0.0
    for bits, state in zip(binary_strings(r), states):
        difference = dual - np.outer(state, state.conj()) / (2 ** r)
        min_dual_eigenvalue = min(min_dual_eigenvalue, float(np.linalg.eigvalsh(difference)[0]))
        helstrom_vector = tensor([np.array([1, (-1) ** bit]) / math.sqrt(2) for bit in bits])
        attained_guess += abs(np.vdot(helstrom_vector, state)) ** 2 / (2 ** r)
    require(min_dual_eigenvalue >= -TOL, "tensor Helstrom dual is not PSD-feasible")
    require(abs(attained_guess - predicted_guess) <= TOL, "product Helstrom attainment fails")
    require(abs(np.trace(dual).real - predicted_guess) <= TOL, "tensor dual trace is wrong")

    # Finite high-confidence inequalities on feasible covariant POVM seeds.
    q_conf = np.array([.04, .07, .10, .13, .16])
    strings = binary_strings(len(q_conf))
    dimension = len(strings)
    weights = np.array([np.prod([q_conf[j] if bit else 1 - q_conf[j]
                                for j, bit in enumerate(bits)]) for bits in strings])
    psi0 = np.sqrt(weights)
    b_cut = .25
    low = np.array([sum(bits) <= math.floor(b_cut * len(q_conf)) for bits in strings])
    low_dimension = int(np.sum(low))
    tail = float(np.sum(weights[~low]))
    dimension_fraction = low_dimension / dimension
    qmax = float(max(q_conf))
    require(dimension_fraction <= math.exp(-len(q_conf) * binary_relative_entropy(b_cut, .5)) + TOL,
            "fair-binomial low-dimension Chernoff bound fails")
    require(tail <= math.exp(-len(q_conf) * binary_relative_entropy(b_cut, qmax)) + TOL,
            "Poisson-binomial high-weight Chernoff bound fails")
    seeds = []
    for _ in range(4):
        matrix = rng.normal(size=(dimension, 3)) + 1j * rng.normal(size=(dimension, 3))
        seed = matrix @ matrix.conj().T
        seed *= .9 / (dimension * float(np.max(np.diag(seed).real)))
        seeds.append(("random_PSD", seed))
    for _ in range(3):
        acceptance = rng.uniform(.05, .95, size=dimension)
        vector = np.sqrt(acceptance)
        seeds.append(("rank_one_positive", np.outer(vector, vector) / dimension))
    usd_acceptance = np.min(weights) / weights
    usd_vector = np.sqrt(usd_acceptance)
    usd_seed = np.outer(usd_vector, usd_vector) / dimension
    seeds.append(("exact_unambiguous", usd_seed))
    seeds.append(("high_confidence_mixture", .95 * usd_seed + .05 * np.diag(np.diag(usd_seed))))
    max_psd_bound_excess = max_split_excess = max_inverse_excess = 0.0
    high_confidence_cases = 0
    for name, seed in seeds:
        acceptance = dimension * np.diag(seed).real
        require(np.min(np.linalg.eigvalsh(seed)) >= -TOL, "covariant seed is not PSD")
        require(np.min(acceptance) >= -TOL and np.max(acceptance) <= 1 + TOL,
                "covariant effects do not sum below identity")
        accepted = float(weights @ acceptance)
        correct = float((psi0 @ seed @ psi0).real)
        positivity_bound = float(np.sum(np.sqrt(weights * acceptance)) ** 2 / dimension)
        split_bound = (math.sqrt(dimension_fraction * accepted) + math.sqrt(tail)) ** 2
        max_psd_bound_excess = max(max_psd_bound_excess, correct - positivity_bound)
        max_split_excess = max(max_split_excess, positivity_bound - split_bound)
        require(correct <= positivity_bound + TOL, "PSD entrywise confidence bound fails")
        require(positivity_bound <= split_bound + TOL, "low/high Cauchy split fails")
        epsilon = .1
        if correct >= (1 - epsilon) * accepted - 1e-13:
            require(dimension_fraction < 1 - epsilon, "confidence denominator is not positive")
            inverse_bound = tail / (math.sqrt(1 - epsilon) - math.sqrt(dimension_fraction)) ** 2
            require(accepted <= inverse_bound + TOL, "finite confidence acceptance bound fails")
            max_inverse_excess = max(max_inverse_excess, accepted - inverse_bound)
            high_confidence_cases += 1
    require(high_confidence_cases >= 2, "nontrivial high-confidence seeds were not exercised")
    return {"status": "passed", "hard_pairs": r, "hard_family_size": 2 ** r,
            "max_output_orthogonality_residual": orthogonal_residual,
            "minimum_tensor_dual_eigenvalue": min_dual_eigenvalue,
            "product_Helstrom_probability": predicted_guess,
            "attained_product_measurement_probability": attained_guess,
            "confidence_pairs": len(q_conf), "covariant_seeds_checked": len(seeds),
            "high_confidence_seeds_checked": high_confidence_cases,
            "low_dimension_fraction": dimension_fraction, "actual_high_weight_tail": tail,
            "max_PSD_correct_weight_bound_excess": max_psd_bound_excess,
            "max_Cauchy_split_excess": max_split_excess,
            "max_confidence_inversion_excess": max_inverse_excess}


def check_weak_asymmetry_illustration():
    beta = 1.0
    time_coefficient = .15
    cases = []
    worst_pair = 0.0
    for n in [12, 24, 36, 48, 64]:
        g = beta / n
        u = expm(-1j * time_coefficient * n * hn(n, g))
        s = np.linalg.svd(u, compute_uv=False)
        logs = np.log(s)
        one_logcond = float(logs[0] - logs[-1])
        many_logcond = float(2 * np.sum(logs[:n // 2]))
        pairing_residual = float(np.max(np.abs(logs + logs[::-1])))
        require(one_logcond <= 2 * beta * (n - 1) / n + TOL, "oneparticle weak-g gauge bound fails")
        require(many_logcond <= 2 * g * (n // 2) * (n - n // 2) + TOL,
                "half-filled weak-g gauge bound fails")
        require(pairing_residual <= TOL, "illustrative singular values lose reciprocal accuracy")
        require(many_logcond > one_logcond, "finite half-filled amplification absent in illustration")
        worst_pair = max(worst_pair, pairing_residual)
        cases.append({"N": n, "g": g, "log_oneparticle_condition": one_logcond,
                      "log_half_filled_condition": many_logcond,
                      "log_half_filled_condition_per_N": many_logcond / n})
    return {"status": "passed", "purpose": "finite illustrative conditioning, not an asymptotic proof",
            "beta": beta, "illustrative_time_coefficient": time_coefficient,
            "uses_conservative_theorem_time": False,
            "conservative_theorem_time_coefficient_at_gmax_1": .01 / (32 * math.cosh(1)),
            "cases": cases, "max_reciprocal_log_residual": worst_pair}


def main():
    rng = np.random.default_rng(SEED)
    groups = {
        "boundary_rank_and_tail": check_boundary_comparison(),
        "exterior_CAR_evolution": check_exterior_and_fock(),
        "Gaussian_helper_filter": check_gaussian_filter(),
        "Wick_and_polar_approximation": check_wick_and_polar(rng),
        "Slater_discrimination_family": check_phase_ensemble(rng),
        "weak_asymmetry_illustration": check_weak_asymmetry_illustration(),
    }
    report = clean({
        "status": "passed", "seed": SEED, "assertion_tolerance": TOL,
        "numpy_version": np.__version__, "scipy_version": scipy.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Deterministic finite scientific checks; analytical proofs establish all-size and asymptotic claims.",
        "groups": groups,
    })
    target = Path(__file__).resolve().parent / "results.json"
    target.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "groups_passed": len(groups),
                      "seed": SEED, "output": "verification/results.json"}, sort_keys=True))


if __name__ == "__main__":
    main()
