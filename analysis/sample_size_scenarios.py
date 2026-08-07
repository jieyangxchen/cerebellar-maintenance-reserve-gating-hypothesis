#!/usr/bin/env python3
"""Transparent, assumption-labelled sample-size scenarios for the protocols."""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Any

import numpy as np
from scipy.stats import nct, norm, t


def two_sample_n_per_arm(
    effect_size: float,
    power: float = 0.80,
    alpha: float = 0.05,
) -> int:
    """Return equal-group sample size for a two-sided two-sample t test.

    The standardized effect is the mean difference divided by the common SD.
    This is a planning approximation; longitudinal models require simulation
    once genotype-specific pilot covariance estimates are available.
    """

    if effect_size <= 0:
        raise ValueError("effect_size must be positive")
    if not 0 < power < 1:
        raise ValueError("power must lie between 0 and 1")
    if not 0 < alpha < 1:
        raise ValueError("alpha must lie between 0 and 1")

    for n_per_arm in range(2, 100_001):
        degrees_freedom = 2 * n_per_arm - 2
        critical_value = t.ppf(1 - alpha / 2, degrees_freedom)
        noncentrality = effect_size * math.sqrt(n_per_arm / 2)
        achieved_power = nct.cdf(
            -critical_value, degrees_freedom, noncentrality
        ) + 1 - nct.cdf(critical_value, degrees_freedom, noncentrality)
        if achieved_power >= power:
            return n_per_arm
    raise RuntimeError("sample-size search exceeded 100,000 participants per arm")


def inflate_for_attrition(evaluable_n: int, attrition: float) -> int:
    if evaluable_n < 1:
        raise ValueError("evaluable_n must be at least 1")
    if not 0 <= attrition < 1:
        raise ValueError("attrition must lie in [0, 1)")
    return math.ceil(evaluable_n / (1 - attrition))


def continuous_exposure_events_required(
    hazard_ratio_per_sd: float,
    *,
    power: float = 0.90,
    alpha: float = 0.025,
    covariate_r_squared: float = 0.30,
) -> int:
    """Schoenfeld-style event target for a standardized continuous exposure.

    This transparent approximation assumes unit exposure variance and inflates
    for variance explained by adjustment covariates. Restricted splines and
    genotype interactions generally require more events and simulation.
    """

    if hazard_ratio_per_sd <= 0 or math.isclose(hazard_ratio_per_sd, 1.0):
        raise ValueError("hazard_ratio_per_sd must be positive and differ from 1")
    if not 0 < power < 1 or not 0 < alpha < 1:
        raise ValueError("power and alpha must lie between 0 and 1")
    if not 0 <= covariate_r_squared < 1:
        raise ValueError("covariate_r_squared must lie in [0, 1)")

    information = (
        norm.ppf(1 - alpha / 2) + norm.ppf(power)
    ) ** 2 / math.log(hazard_ratio_per_sd) ** 2
    return math.ceil(information / (1 - covariate_r_squared))


def expected_conversion_events(
    cohort_sizes: tuple[int, ...],
    conversion_risks: tuple[float, ...],
    *,
    retention: float,
) -> float:
    """Expected observed phenoconversions across genotype strata."""

    if len(cohort_sizes) != len(conversion_risks) or not cohort_sizes:
        raise ValueError("cohort sizes and risks must be non-empty and aligned")
    if not 0 <= retention <= 1:
        raise ValueError("retention must lie in [0, 1]")
    if any(size < 0 for size in cohort_sizes):
        raise ValueError("cohort sizes must be non-negative")
    if any(not 0 <= risk <= 1 for risk in conversion_risks):
        raise ValueError("conversion risks must lie in [0, 1]")
    return sum(size * risk * retention for size, risk in zip(cohort_sizes, conversion_risks))


def simulate_sca6_stratified_power(
    *,
    simulations: int = 10_000,
    seed: int = 20260807,
    participants_per_band: int = 80,
    treatment_effects: tuple[float, float, float] = (-0.60, -1.00, -1.40),
    placebo_week72_changes: tuple[float, float, float] = (0.90, 1.10, 1.30),
    change_sds: tuple[float, float, float] = (2.50, 2.80, 3.00),
    within_participant_correlations: tuple[float, float, float] = (0.70, 0.75, 0.80),
    dropout_by_week68: tuple[float, float, float] = (0.16, 0.12, 0.08),
    conditional_week72_dropout: tuple[float, float, float] = (0.05, 0.035, 0.022),
    alpha: float = 0.05,
) -> dict[str, Any]:
    """Simulate power for the fixed-mix SCA6 late-treatment contrast.

    The simulation retains visit-specific week-68 and week-72 means, including a
    week-68 observation when week 72 is missing. A subject-level covariance term
    from participants observed at both visits supplies the repeated-measures
    variance. Band-specific active-minus-placebo effects are then standardized
    with fixed one-third weights. This is a transparent planning model, not a
    fitted disease model.
    """

    if simulations < 100:
        raise ValueError("simulations must be at least 100")
    if participants_per_band < 4 or participants_per_band % 2:
        raise ValueError("participants_per_band must be an even integer of at least 4")
    if not 0 < alpha < 1:
        raise ValueError("alpha must lie between 0 and 1")
    band_inputs = (
        treatment_effects,
        placebo_week72_changes,
        change_sds,
        within_participant_correlations,
        dropout_by_week68,
        conditional_week72_dropout,
    )
    if not all(len(values) == 3 for values in band_inputs):
        raise ValueError("band-specific inputs must each contain three values")
    if any(not math.isfinite(effect) for effect in treatment_effects):
        raise ValueError("treatment effects must be finite")
    if any(sd <= 0 for sd in change_sds):
        raise ValueError("change SDs must be positive")
    if any(not 0 <= correlation < 1 for correlation in within_participant_correlations):
        raise ValueError("within-participant correlations must lie in [0, 1)")
    dropout_inputs = (*dropout_by_week68, *conditional_week72_dropout)
    if any(not 0 <= rate < 1 for rate in dropout_inputs):
        raise ValueError("dropout rates must lie in [0, 1)")

    rng = np.random.default_rng(seed)
    participants_per_arm = participants_per_band // 2
    band_bounds = ((3, 4), (5, 9), (10, 12))
    standardization_weights = (1 / 3, 1 / 3, 1 / 3)
    week68_fraction = 68.0 / 72.0
    successful_replicates = 0
    two_sided_rejections = 0
    effect_estimates: list[float] = []
    standard_errors: list[float] = []
    observed_totals = np.zeros(2, dtype=float)
    floor_counts = np.zeros((3, 2), dtype=float)
    floor_denominators = np.zeros((3, 2), dtype=float)

    for _ in range(simulations):
        band_differences: list[float] = []
        band_variances: list[float] = []
        valid_replicate = True

        for band_index, (lower, upper) in enumerate(band_bounds):
            arm_statistics: list[tuple[float, float]] = []
            sd = change_sds[band_index]
            correlation = within_participant_correlations[band_index]
            covariance = sd**2 * np.array(
                [[1.0, correlation], [correlation, 1.0]]
            )

            for is_active in (True, False):
                baseline = rng.integers(
                    lower,
                    upper + 1,
                    size=participants_per_arm,
                ).astype(float)
                residuals = rng.multivariate_normal(
                    mean=(0.0, 0.0),
                    cov=covariance,
                    size=participants_per_arm,
                )
                placebo_mean = placebo_week72_changes[band_index]
                visit_means = np.array(
                    [week68_fraction * placebo_mean, placebo_mean]
                )
                if is_active:
                    visit_means += treatment_effects[band_index]

                final_sara = np.clip(
                    baseline[:, None] + visit_means + residuals,
                    0.0,
                    40.0,
                )
                changes = final_sara - baseline[:, None]

                missing68 = (
                    rng.random(participants_per_arm)
                    < dropout_by_week68[band_index]
                )
                missing72 = missing68 | (
                    rng.random(participants_per_arm)
                    < conditional_week72_dropout[band_index]
                )
                observed = np.column_stack((~missing68, ~missing72))
                observed_n = observed.sum(axis=0)
                observed_totals += observed_n
                floor_counts[band_index] += ((final_sara <= 1.0) & observed).sum(axis=0)
                floor_denominators[band_index] += observed_n

                if np.any(observed_n < 2):
                    valid_replicate = False
                    break

                visit_means_observed = np.array(
                    [changes[observed[:, visit], visit].mean() for visit in range(2)]
                )
                mean_variances = np.array(
                    [
                        changes[observed[:, visit], visit].var(ddof=1)
                        / observed_n[visit]
                        for visit in range(2)
                    ]
                )
                observed_both = observed.all(axis=1)
                mean_covariance = np.sum(
                    (changes[observed_both, 0] - visit_means_observed[0])
                    * (changes[observed_both, 1] - visit_means_observed[1])
                ) / (observed_n[0] * observed_n[1])
                late_mean = float(visit_means_observed.mean())
                late_variance = float(
                    0.25 * (mean_variances.sum() + 2 * mean_covariance)
                )
                arm_statistics.append((late_mean, late_variance))

            if not valid_replicate:
                break

            active_statistics, placebo_statistics = arm_statistics
            band_differences.append(active_statistics[0] - placebo_statistics[0])
            band_variances.append(active_statistics[1] + placebo_statistics[1])

        if not valid_replicate:
            continue

        estimate = float(np.mean(band_differences))
        standard_error = math.sqrt(sum(band_variances) / 9.0)
        p_value = 2 * norm.sf(abs(estimate / standard_error))
        two_sided_rejections += int(p_value < alpha)
        successful_replicates += int(p_value < alpha and estimate < 0)
        effect_estimates.append(estimate)
        standard_errors.append(standard_error)

    valid_simulations = len(effect_estimates)
    if valid_simulations == 0:
        raise RuntimeError("no simulation replicate had enough observed late-visit data")
    estimated_power = successful_replicates / simulations
    monte_carlo_se = math.sqrt(
        estimated_power * (1 - estimated_power) / simulations
    )

    return {
        "simulations": simulations,
        "valid_simulations": valid_simulations,
        "seed": seed,
        "randomized_total": participants_per_band * 3,
        "participants_per_band": participants_per_band,
        "participants_per_arm_per_band": participants_per_arm,
        "standardization_weights": standardization_weights,
        "treatment_effects": treatment_effects,
        "weighted_input_effect": float(
            sum(
                weight * effect
                for weight, effect in zip(standardization_weights, treatment_effects)
            )
        ),
        "estimated_power": estimated_power,
        "two_sided_rejection_rate": two_sided_rejections / simulations,
        "monte_carlo_se": monte_carlo_se,
        "mean_effect_estimate": float(np.mean(effect_estimates)),
        "mean_standard_error": float(np.mean(standard_errors)),
        "mean_observed_week68": float(observed_totals[0] / simulations),
        "mean_observed_week72": float(observed_totals[1] / simulations),
        "floor_rate_by_band": tuple(
            tuple(float(value) for value in row)
            for row in floor_counts / floor_denominators
        ),
    }


def _scenario(
    *,
    scenario: str,
    disease: str,
    endpoint: str,
    effect_size: float,
    attrition: float,
    interpretation: str,
    power: float = 0.80,
    alpha: float = 0.05,
) -> dict[str, Any]:
    evaluable = two_sample_n_per_arm(effect_size, power=power, alpha=alpha)
    randomized = inflate_for_attrition(evaluable, attrition)
    return {
        "scenario": scenario,
        "disease": disease,
        "endpoint": endpoint,
        "standardized_effect": round(effect_size, 3),
        "power": power,
        "alpha_two_sided": alpha,
        "evaluable_per_arm": evaluable,
        "attrition_fraction": attrition,
        "randomized_per_arm": randomized,
        "randomized_total": randomized * 2,
        "assumption_status": "illustrative",
        "interpretation": interpretation,
    }


def build_sample_size_scenarios() -> list[dict[str, Any]]:
    """Return sensitivity scenarios used in the protocol, never a fixed answer."""

    cohort_main_events = continuous_exposure_events_required(
        1.5,
        power=0.90,
        alpha=0.025,
        covariate_r_squared=0.30,
    )
    cohort_800_events = expected_conversion_events(
        (500, 300),
        (0.25, 0.10),
        retention=0.85,
    )
    cohort_expanded_events = expected_conversion_events(
        (750, 450),
        (0.35, 0.15),
        retention=0.85,
    )

    rows: list[dict[str, Any]] = [
        {
            "scenario": "cohort-main-continuous-exposure-events",
            "disease": "SCA3+SCA6",
            "endpoint": "interval-censored phenoconversion",
            "standardized_effect": "HR 1.50 per SD",
            "power": 0.90,
            "alpha_two_sided": 0.025,
            "evaluable_per_arm": "not applicable",
            "attrition_fraction": "event based",
            "randomized_per_arm": "not applicable",
            "randomized_total": cohort_main_events,
            "assumption_status": "illustrative",
            "interpretation": (
                "Approximate event target for one linear standardized exposure; spline and interaction tests need more information."
            ),
        },
        {
            "scenario": "cohort-800-expected-events",
            "disease": "SCA3+SCA6",
            "endpoint": "five-year phenoconversion",
            "standardized_effect": "500 SCA3 at 25%; 300 SCA6 at 10%",
            "power": "not computed",
            "alpha_two_sided": 0.025,
            "evaluable_per_arm": "not applicable",
            "attrition_fraction": 0.15,
            "randomized_per_arm": "not applicable",
            "randomized_total": math.ceil(cohort_800_events),
            "assumption_status": "illustrative",
            "interpretation": (
                "About 132 events may support a main exposure analysis but not a stable multi-df genotype interaction."
            ),
        },
        {
            "scenario": "cohort-expanded-interaction-context",
            "disease": "SCA3+SCA6",
            "endpoint": "five-year phenoconversion",
            "standardized_effect": "750 SCA3 at 35%; 450 SCA6 at 15%",
            "power": "simulation required",
            "alpha_two_sided": 0.025,
            "evaluable_per_arm": "not applicable",
            "attrition_fraction": 0.15,
            "randomized_per_arm": "not applicable",
            "randomized_total": math.ceil(cohort_expanded_events),
            "assumption_status": "illustrative",
            "interpretation": (
                "About 281 events is a planning context for a genotype interaction; final design requires interval-censoring simulation."
            ),
        },
    ]
    rows.extend(
        [
            _scenario(
                scenario="sca3-pons-mri-30-percent-slowing",
                disease="SCA3",
                endpoint="104-week pons-volume annualized change",
                effect_size=0.423,
                attrition=0.15,
                interpretation=(
                    "Lower SCA3 sensitivity bound: a 30% slowing multiplied by a planning standardized change score of 1.41."
                ),
            ),
            _scenario(
                scenario="sca3-pons-mri-40-percent-slowing",
                disease="SCA3",
                endpoint="104-week pons-volume annualized change",
                effect_size=0.564,
                attrition=0.15,
                interpretation=(
                    "Central phase-2 scenario: a 40% slowing multiplied by a planning standardized change score of 1.41."
                ),
            ),
            _scenario(
                scenario="sca3-pons-mri-50-percent-slowing",
                disease="SCA3",
                endpoint="104-week pons-volume annualized change",
                effect_size=0.705,
                attrition=0.15,
                interpretation=(
                    "Upper SCA3 sensitivity bound: a 50% slowing multiplied by a planning standardized change score of 1.41."
                ),
            ),
            _scenario(
                scenario="sca6-l-arginine-pilot-1.52-point-sara",
                disease="SCA6",
                endpoint="equal-weight week-68/week-72 SARA contrast",
                effect_size=0.608,
                attrition=0.15,
                interpretation=(
                    "Sensitivity analysis using the unstable 1.52-point pilot estimate and SD 2.5; not the design target."
                ),
            ),
            _scenario(
                scenario="sca6-l-arginine-one-point-sara",
                disease="SCA6",
                endpoint="equal-weight week-68/week-72 SARA contrast",
                effect_size=0.40,
                attrition=0.15,
                interpretation=(
                    "One-point treatment difference with SD 2.5; rounded protocol target is 120 per arm."
                ),
            ),
            _scenario(
                scenario="sca6-l-arginine-0.75-point-sara",
                disease="SCA6",
                endpoint="equal-weight week-68/week-72 SARA contrast",
                effect_size=0.30,
                attrition=0.15,
                interpretation=(
                    "Sensitivity analysis showing that a 0.75-point effect needs materially more than 240 participants."
                ),
            ),
            _scenario(
                scenario="sca6-l-arginine-0.60-point-sara",
                disease="SCA6",
                endpoint="equal-weight week-68/week-72 SARA contrast",
                effect_size=0.24,
                attrition=0.15,
                interpretation=(
                    "Sensitivity analysis approximating 50% slowing of a 0.80-point annual SARA rate over 72 weeks."
                ),
            ),
        ]
    )
    stratified_simulation = simulate_sca6_stratified_power()
    rows.append(
        {
            "scenario": "sca6-fixed-band-repeated-contrast-simulation",
            "disease": "SCA6",
            "endpoint": "equal-weight week-68/week-72 SARA contrast",
            "standardized_effect": "band benefits 0.60/1.00/1.40 points; fixed mean 1.00",
            "power": round(stratified_simulation["estimated_power"], 3),
            "alpha_two_sided": 0.05,
            "evaluable_per_arm": "visit-specific under monotone simulated dropout",
            "attrition_fraction": "week-72: 0.202/0.151/0.100 by SARA band",
            "randomized_per_arm": 120,
            "randomized_total": 240,
            "assumption_status": "illustrative",
            "interpretation": (
                "10,000 fixed-seed bivariate replicates with 80 participants per SARA band, one-third "
                "standardization, correlations 0.70/0.75/0.80, band SDs 2.50/2.80/3.00, bounded SARA, "
                "and band-specific monotone dropout."
            ),
        }
    )
    return rows


def write_csv(destination: Path) -> None:
    rows = build_sample_size_scenarios()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    write_csv(Path(__file__).with_name("sample-size-scenarios.csv"))
