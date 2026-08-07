# Cerebellar Maintenance–Reserve–Gating Publication Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a rigorously sourced hypothesis manuscript, three reproducible mechanism figures, and concrete SCA3/SCA6 cohort and early-intervention protocols in a new public GitHub repository.

**Architecture:** The manuscript is the narrative entrypoint; protocols and the statistical analysis plan hold operational detail; an evidence matrix separates established results from analogy and speculation. Python scripts generate figures and sample-size scenarios, while one validator checks artifact completeness, links, DOI formatting, and safety language.

**Tech Stack:** Markdown, BibTeX, Python 3, NumPy, SciPy, Matplotlib, Git, GitHub CLI.

---

### Task 1: Lock the evidence base

**Files:**
- Create: `evidence/evidence-audit.md`
- Create: `evidence/evidence-matrix.tsv`
- Create: `manuscript/references.bib`

- [x] Verify each supplied citation against PubMed, PMC, the publisher DOI page, or ClinicalTrials.gov.
- [x] Record the exact supported claim, model system, sample size, evidence tier, limitation, and direct URL.
- [x] Correct the SCA3 tDCS discussion by including both mixed-etiology positive trials and the genotype-specific negative trial.
- [x] Timestamp registry status and distinguish registry status from treatment efficacy.
- [x] Run `python3 scripts/validate_repository.py` after Task 7; expect `Repository validation passed.`.

### Task 2: Formalize the model and figures

**Files:**
- Create: `figures/src/make_figures.py`
- Create: `figures/fig1-framework.svg`, `.pdf`, `.png`
- Create: `figures/fig2-nonlinear-gating.svg`, `.pdf`, `.png`
- Create: `figures/fig3-study-program.svg`, `.pdf`, `.png`

- [x] Encode the causal architecture with supported and hypothetical edge styles.
- [x] Encode the Hill-gate, activation, uptake, leak, consumption, and net-reserve equations with an illustrative parameter dictionary in source.
- [x] Label the four exposure zones and mark all simulated curves as illustrative.
- [x] Encode cohort-to-validation-to-trial gating and genotype-specific modules.
- [x] Run `python3 figures/src/make_figures.py`; expect nine non-empty outputs.
- [x] Rasterize or inspect each PNG at full resolution; confirm no clipped or overlapping text.

### Task 3: Build the prospective cohort protocol

**Files:**
- Create: `protocols/prospective-cohort.md`

- [x] Specify SCA3, SCA6, preataxic, early symptomatic, and control eligibility and exclusions.
- [x] Define the five-year six-monthly visit schedule and core, imaging, remote, and biospecimen measurements.
- [x] Lock one confirmatory exposure family and one non-linear contrast before outcomes are unblinded.
- [x] Define the biomarker-state slope estimand, interval-censored phenoconversion estimand, family/site structure, and external validation.
- [x] State recruitment, retention, measurement-error, ancestry, migration, and reverse-causation safeguards.

### Task 4: Build the early-intervention programme

**Files:**
- Create: `protocols/early-intervention-trial.md`

- [x] Specify separate SCA3 molecular-lowering and SCA6 L-arginine protocols without a pooled pharmacologic primary analysis.
- [x] Gate SCA3 activation on SCA3-specific safety, RP2D, and CSF target engagement; delay preataxic enrolment.
- [x] Define the 72-week SCA6 clinical endpoint, 12-week blinded withdrawal, and enhanced safety monitoring.
- [x] Specify randomization, concealment, blinding checks, safety stopping, intercurrent events, estimands, and sensitivity analyses.
- [x] Keep circuit phase 0 inactive until reliability, temporal-precedence, normalization, and washout criteria all pass.

### Task 5: Write the statistical analysis plan and sample-size scenarios

**Files:**
- Create: `protocols/statistical-analysis-plan.md`
- Create: `analysis/sample_size_scenarios.py`
- Create: `analysis/sample-size-scenarios.csv`

- [x] Implement event-driven cohort calculations and expected-conversion scenarios.
- [x] Implement SCA3 pons-MRI and SCA6 SARA treatment-effect scenarios with explicit variance assumptions.
- [x] Include attrition inflation and sensitivity grids; do not output a single context-free sample size.
- [x] Run `python3 analysis/sample_size_scenarios.py`; expect deterministic CSV output.
- [x] Define spline degrees of freedom, interaction hierarchy, cross-fitting, missing-data handling, multiplicity, and external validation.

### Task 6: Rewrite the manuscript

**Files:**
- Create: `manuscript/manuscript.md`
- Create: `manuscript/manuscript_zh.md`

- [x] Replace the residual-onset primary analysis with one-stage survival modelling.
- [x] Separate established evidence, analogy, prediction, and speculation in every major section.
- [x] Integrate the three figures and move operational detail to protocol files.
- [x] Add nested-model comparison, identifiability limits, negative evidence, falsification thresholds, and ethical boundaries.
- [x] Ensure the abstract states that no evidence currently identifies `X` and that no intervention targets `X`.

### Task 7: Package and validate the repository

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `CITATION.cff`
- Create: `.gitignore`
- Create: `scripts/validate_repository.py`

- [x] Document scope, evidence date, reproduction commands, and non-treatment disclaimer.
- [x] Validate required files, generated formats, DOI syntax, Markdown links, and forbidden therapeutic claims.
- [x] Run `python3 scripts/validate_repository.py`; expect all checks to pass.
- [x] Run `git diff --check`; expect no whitespace errors.
- [x] Review all generated artifacts and compare them line by line with the design acceptance criteria.

### Task 8: Publish

**Files:**
- Modify: Git history and GitHub repository metadata only.

- [ ] Inspect `git status -sb` and the full staged diff.
- [ ] Commit the complete scoped package with a concise message.
- [ ] Create `jieyangxchen/cerebellar-maintenance-reserve-gating-hypothesis` as a public repository and push `main`.
- [ ] Query GitHub for repository visibility, default branch, commit SHA, and public URL.
- [ ] Fetch the public README URL without credentials; expect HTTP 200.
