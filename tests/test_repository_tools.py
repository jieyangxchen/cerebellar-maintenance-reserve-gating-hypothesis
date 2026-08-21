from __future__ import annotations

import math
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import numpy as np
import figures.src.make_figures as figure_module
import scripts.validate_repository as repository_validation

from analysis.sample_size_scenarios import (
    build_sample_size_scenarios,
    continuous_exposure_events_required,
    expected_conversion_events,
    inflate_for_attrition,
    simulate_sca6_stratified_power,
    two_sample_n_per_arm,
)
from figures.src.make_figures import (
    DEFAULT_PARAMETERS,
    gating_components,
    generate_all,
    relative_depletion_pressure,
)
from scripts.validate_repository import (
    find_broken_local_links,
    find_evidence_matrix_errors,
    find_invalid_doi_declarations,
    find_legacy_math_delimiters,
    find_license_metadata_errors,
    find_missing_required_files,
    find_stale_generated_files,
    find_unsafe_claims,
)


class SampleSizeScenarioTests(unittest.TestCase):
    def test_two_sample_size_matches_sca6_one_point_scenario(self) -> None:
        n = two_sample_n_per_arm(effect_size=0.40, power=0.80, alpha=0.05)
        self.assertEqual(n, 100)

    def test_larger_effect_requires_fewer_participants(self) -> None:
        moderate = two_sample_n_per_arm(effect_size=0.58, power=0.80, alpha=0.05)
        large = two_sample_n_per_arm(effect_size=0.82, power=0.80, alpha=0.05)
        self.assertLess(large, moderate)

    def test_attrition_inflation_rounds_up(self) -> None:
        self.assertEqual(inflate_for_attrition(48, attrition=0.15), math.ceil(48 / 0.85))

    def test_scenario_table_contains_cohort_and_disease_specific_trials(self) -> None:
        rows = build_sample_size_scenarios()
        labels = {row["scenario"] for row in rows}
        self.assertIn("cohort-main-continuous-exposure-events", labels)
        self.assertIn("cohort-800-expected-events", labels)
        self.assertIn("sca3-pons-mri-40-percent-slowing", labels)
        self.assertIn("sca6-l-arginine-one-point-sara", labels)
        self.assertTrue(all(row["assumption_status"] == "illustrative" for row in rows))

    def test_continuous_exposure_event_target_matches_documented_scenario(self) -> None:
        events = continuous_exposure_events_required(
            hazard_ratio_per_sd=1.5,
            power=0.90,
            alpha=0.025,
            covariate_r_squared=0.30,
        )
        self.assertGreaterEqual(events, 105)
        self.assertLessEqual(events, 112)

    def test_expected_conversion_events_accounts_for_retention(self) -> None:
        events = expected_conversion_events(
            cohort_sizes=(500, 300),
            conversion_risks=(0.25, 0.10),
            retention=0.85,
        )
        self.assertAlmostEqual(events, 131.75)

    def test_sca6_stratified_simulation_is_deterministic_and_design_specific(self) -> None:
        first = simulate_sca6_stratified_power(simulations=500, seed=20260807)
        second = simulate_sca6_stratified_power(simulations=500, seed=20260807)
        self.assertEqual(first, second)
        self.assertEqual(first["randomized_total"], 240)
        self.assertEqual(first["participants_per_band"], 80)
        self.assertEqual(first["participants_per_arm_per_band"], 40)
        self.assertEqual(first["standardization_weights"], (1 / 3, 1 / 3, 1 / 3))
        self.assertEqual(first["treatment_effects"], (-0.6, -1.0, -1.4))
        self.assertAlmostEqual(first["weighted_input_effect"], -1.0)

    def test_sca6_stratified_base_case_is_near_eighty_percent_power(self) -> None:
        result = simulate_sca6_stratified_power(simulations=10_000, seed=20260807)
        self.assertGreater(result["estimated_power"], 0.78)
        self.assertLess(result["estimated_power"], 0.82)
        self.assertLess(result["monte_carlo_se"], 0.005)
        self.assertGreater(result["mean_effect_estimate"], -1.02)
        self.assertLess(result["mean_effect_estimate"], -0.95)
        self.assertGreater(result["mean_observed_week68"], 210.0)
        self.assertLess(result["mean_observed_week68"], 212.0)
        self.assertGreater(result["mean_observed_week72"], 202.5)
        self.assertLess(result["mean_observed_week72"], 205.0)

        floor_rates = result["floor_rate_by_band"]
        self.assertGreater(floor_rates[0][0], floor_rates[1][0])
        self.assertGreater(floor_rates[1][0], floor_rates[2][0])
        self.assertGreater(floor_rates[0][0], 0.08)
        self.assertLess(floor_rates[0][0], 0.15)
        self.assertLess(floor_rates[2][0], 0.01)

    def test_sca6_stratified_simulation_controls_null_rejection(self) -> None:
        null_rejection = simulate_sca6_stratified_power(
            simulations=10_000,
            seed=20260808,
            treatment_effects=(0.0, 0.0, 0.0),
        )
        self.assertGreater(null_rejection["two_sided_rejection_rate"], 0.04)
        self.assertLess(null_rejection["two_sided_rejection_rate"], 0.06)
        self.assertGreater(null_rejection["estimated_power"], 0.02)
        self.assertLess(null_rejection["estimated_power"], 0.035)
        self.assertGreater(null_rejection["mean_effect_estimate"], -0.03)
        self.assertLess(null_rejection["mean_effect_estimate"], 0.03)


class GatingModelTests(unittest.TestCase):
    def test_illustrative_model_has_idle_danger_and_rebalance_regions(self) -> None:
        x = np.linspace(0.0, 10.0, 1001)
        components = gating_components(x, DEFAULT_PARAMETERS)
        net = components["net_reserve_change"]

        low = net[np.argmin(np.abs(x - 0.1))]
        middle = net[np.argmin(np.abs(x - 2.2))]
        high = net[np.argmin(np.abs(x - 8.0))]

        self.assertLess(middle, low)
        self.assertGreaterEqual(high, 0.0)

        peak_loss_x = x[np.argmax(-net)]
        self.assertGreater(peak_loss_x, 0.5)
        self.assertLess(peak_loss_x, 5.0)

    def test_gate_and_activation_are_bounded(self) -> None:
        x = np.linspace(0.0, 10.0, 101)
        components = gating_components(x, DEFAULT_PARAMETERS)
        for key in ("gate", "activation"):
            self.assertTrue(np.all(components[key] >= 0.0))
            self.assertTrue(np.all(components[key] <= 1.0))

    def test_relative_depletion_pressure_is_nonnegative(self) -> None:
        net = np.array([-0.5, -2.0, 0.0, 3.0])
        pressure = relative_depletion_pressure(net)
        self.assertTrue(np.all(pressure >= 0.0))
        self.assertEqual(int(np.argmax(pressure)), 1)
        self.assertAlmostEqual(float(pressure.max()), 1.0)

    def test_figure_generator_exports_three_figures_in_three_formats(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outputs = generate_all(Path(tmp))
            self.assertEqual(len(outputs), 9)
            self.assertEqual({path.suffix for path in outputs}, {".svg", ".pdf", ".png"})
            self.assertTrue(all(path.stat().st_size > 1_000 for path in outputs))

            for svg in Path(tmp).glob("*.svg"):
                svg_text = svg.read_text(encoding="utf-8")
                self.assertIn("<svg", svg_text[:1_000])
                self.assertFalse(
                    any(line != line.rstrip() for line in svg_text.splitlines()),
                    msg=f"trailing whitespace in {svg.name}",
                )

            for pdf in Path(tmp).glob("*.pdf"):
                self.assertEqual(pdf.read_bytes()[:4], b"%PDF")

    def test_figure_exports_are_byte_reproducible(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_outputs = generate_all(Path(first))
            second_outputs = generate_all(Path(second))
            first_by_name = {path.name: path.read_bytes() for path in first_outputs}
            second_by_name = {path.name: path.read_bytes() for path in second_outputs}
            self.assertEqual(first_by_name, second_by_name)

    def test_figure_three_marks_sca3_primary_and_sca6_as_transport_test(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            generate_all(Path(tmp))
            svg = (Path(tmp) / "fig3-study-program.svg").read_text(encoding="utf-8")
            self.assertIn("SCA3 primary test bed", svg)
            self.assertIn("SCA6 transport test", svg)
            self.assertIn("Known-target examples", svg)

    def test_figure_files_do_not_repeat_caption_titles_inside_artwork(self) -> None:
        titles = {
            "fig1-framework.svg": "A nested, falsifiable maintenance–reserve–gating model",
            "fig2-nonlinear-gating.svg": (
                "Predicted non-monotonic input response under one illustrative parameter set"
            ),
            "fig3-study-program.svg": (
                "Prospective validation and gated early-intervention programme"
            ),
        }
        with tempfile.TemporaryDirectory() as tmp:
            generate_all(Path(tmp))
            for filename, title in titles.items():
                svg = (Path(tmp) / filename).read_text(encoding="utf-8")
                self.assertNotIn(title, svg)

    def test_figure_one_keeps_visible_gutters_between_connected_boxes(self) -> None:
        captured: dict[str, object] = {}

        def retain_figure(fig, _output_dir, _stem):
            captured["figure"] = fig
            return []

        with patch.object(figure_module, "_save", side_effect=retain_figure):
            figure_module._figure_framework(Path("unused"))

        fig = captured["figure"]
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        boxes = [
            artist
            for artist in fig.axes[0].patches
            if artist.__class__.__name__ == "FancyBboxPatch"
        ]
        named = dict(
            zip(
                (
                    "genotype",
                    "known_pressure",
                    "measured",
                    "candidate_score",
                    "baseline_reserve",
                    "bridge",
                    "coupling",
                    "reserve",
                    "candidate_factor",
                    "network",
                    "dysfunction",
                ),
                boxes,
                strict=True,
            )
        )

        minimum_gutter_px = 6.0
        for left_name, right_name in (
            ("candidate_score", "bridge"),
            ("bridge", "coupling"),
            ("network", "dysfunction"),
        ):
            left = named[left_name].get_window_extent(renderer)
            right = named[right_name].get_window_extent(renderer)
            gutter = right.x0 - left.x1
            self.assertGreaterEqual(
                gutter,
                minimum_gutter_px,
                msg=f"{left_name} -> {right_name} gutter is only {gutter:.1f}px",
            )

        figure_module.plt.close(fig)


class RepositoryValidationTests(unittest.TestCase):
    def test_default_required_files_include_the_cerebellum_submission_package(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            errors = find_missing_required_files(Path(tmp))
            self.assertIn(
                "missing required file: submission/the-cerebellum/presubmission-inquiry.md",
                errors,
            )
            self.assertIn(
                "missing required file: submission/the-cerebellum/submission-checklist.md",
                errors,
            )

    def test_the_cerebellum_readiness_flags_format_and_prior_art_failures(self) -> None:
        checker = getattr(
            repository_validation, "find_the_cerebellum_readiness_errors", None
        )
        self.assertIsNotNone(checker)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "manuscript").mkdir()
            overlong_abstract = " ".join(["word"] * 251)
            (root / "manuscript" / "manuscript.md").write_text(
                "# Unfocused title\n\n"
                f"## Abstract\n\n{overlong_abstract}\n\n"
                "**Keywords:** one; two\n\n"
                "#### Too deep\n",
                encoding="utf-8",
            )
            (root / "manuscript" / "references.bib").write_text(
                "@article{unrelated}\n", encoding="utf-8"
            )
            errors = checker(root)
            self.assertTrue(any("target title" in error for error in errors))
            self.assertTrue(any("abstract" in error for error in errors))
            self.assertTrue(any("keywords" in error for error in errors))
            self.assertTrue(any("heading level" in error for error in errors))
            self.assertTrue(any("cerebellar-reserve prior art" in error for error in errors))

    def test_repository_meets_the_cerebellum_readiness_checks(self) -> None:
        checker = getattr(
            repository_validation, "find_the_cerebellum_readiness_errors", None
        )
        self.assertIsNotNone(checker)
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(checker(root), [])

    def test_the_cerebellum_readiness_reports_uncited_numbered_references(self) -> None:
        checker = repository_validation.find_the_cerebellum_readiness_errors
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "manuscript").mkdir()
            (root / "manuscript" / "manuscript.md").write_text(
                "# A Maintenance–Reserve–Gating Framework for Modifier Effects in "
                "Hereditary Cerebellar Ataxia\n\n"
                "## Abstract\n\nShort abstract.\n\n"
                "**Keywords:** one; two; three; four\n\n"
                "## Main text\n\nNo numbered citation.\n\n"
                "## References\n\n1. Uncited reference.\n",
                encoding="utf-8",
            )
            (root / "manuscript" / "references.bib").write_text(
                "10.1007/s12311-019-01091-9\n10.1007/s12311-018-0925-6\n",
                encoding="utf-8",
            )
            errors = checker(root)
            self.assertTrue(any("uncited numbered references" in error for error in errors))

    def test_documented_validator_command_runs_from_repository_root(self) -> None:
        root = Path(__file__).resolve().parents[1]
        environment = os.environ.copy()
        environment.pop("PYTHONPATH", None)
        result = subprocess.run(
            [sys.executable, "scripts/validate_repository.py"],
            cwd=root,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )
        self.assertIn("Repository validation passed.", result.stdout)

    def test_broken_relative_markdown_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "README.md"
            page.write_text("[missing](manuscript/missing.md)\n", encoding="utf-8")
            errors = find_broken_local_links(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("manuscript/missing.md", errors[0])

    def test_existing_relative_markdown_link_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "manuscript").mkdir()
            (root / "manuscript" / "paper.md").write_text("paper\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[paper](manuscript/paper.md)\n", encoding="utf-8"
            )
            self.assertEqual(find_broken_local_links(root), [])

    def test_broken_relative_image_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(
                "![figure](figures/missing.svg)\n", encoding="utf-8"
            )
            errors = find_broken_local_links(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("figures/missing.svg", errors[0])

    def test_unsafe_unknown_x_treatment_claim_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "claim.md").write_text(
                "We propose administering X to patients as treatment.\n", encoding="utf-8"
            )
            errors = find_unsafe_claims(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("administering X", errors[0])

    def test_negated_unknown_x_treatment_warning_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "warning.md").write_text(
                "Clinicians must not administer X to patients.\n", encoding="utf-8"
            )
            self.assertEqual(find_unsafe_claims(root), [])

    def test_missing_required_repository_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            errors = find_missing_required_files(root, required=("README.md", "LICENSE"))
            self.assertEqual(len(errors), 2)
            (root / "README.md").write_text("ready\n", encoding="utf-8")
            errors = find_missing_required_files(root, required=("README.md", "LICENSE"))
            self.assertEqual(errors, ["missing required file: LICENSE"])

    def test_inconsistent_noncommercial_license_metadata_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "LICENSE").write_text(
                "Attribution-NonCommercial 4.0 International\n", encoding="utf-8"
            )
            (root / "README.md").write_text("License: CC BY 4.0\n", encoding="utf-8")
            (root / "CITATION.cff").write_text(
                "license: CC-BY-4.0\n", encoding="utf-8"
            )
            errors = find_license_metadata_errors(root)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("README.md" in error for error in errors))
            self.assertTrue(any("CITATION.cff" in error for error in errors))

    def test_repository_noncommercial_license_metadata_is_consistent(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(find_license_metadata_errors(root), [])

    def test_invalid_declared_doi_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reference.md").write_text(
                "Valid doi:10.1000/example.1\nInvalid DOI: not-a-doi\n",
                encoding="utf-8",
            )
            errors = find_invalid_doi_declarations(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("Invalid DOI", errors[0])

    def test_legacy_math_delimiters_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "paper.md").write_text(
                "Legacy inline \\\\(x\\\\) and display \\\\[y\\\\].\n",
                encoding="utf-8",
            )
            errors = find_legacy_math_delimiters(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("GitHub-incompatible math delimiter", errors[0])

    def test_evidence_matrix_requires_claim_tier_and_unique_ids(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "evidence").mkdir()
            matrix = root / "evidence" / "evidence-matrix.tsv"
            matrix.write_text(
                "claim_id\tclaim\tverdict\nA\tone\tconfirmed\nA\ttwo\tconfirmed\n",
                encoding="utf-8",
            )
            errors = find_evidence_matrix_errors(root)
            self.assertTrue(any("missing columns" in error for error in errors))
            self.assertTrue(any("duplicate claim_id" in error for error in errors))

    def test_checked_in_generated_artifacts_match_sources(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(find_stale_generated_files(root), [])


if __name__ == "__main__":
    unittest.main()
