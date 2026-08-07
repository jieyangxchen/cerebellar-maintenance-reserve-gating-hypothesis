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

- [ ] Verify each supplied citation against PubMed, PMC, the publisher DOI page, or ClinicalTrials.gov.
- [ ] Record the exact supported claim, model system, sample size, evidence tier, limitation, and direct URL.
- [ ] Correct the SCA3 tDCS discussion by including both mixed-etiology positive trials and the genotype-specific negative trial.
- [ ] Timestamp registry status and distinguish registry status from treatment efficacy.
- [ ] Run `python3 scripts/validate_repository.py` after Task 7; expect `evidence: PASS`.

### Task 2: Formalize the model and figures

**Files:**
- Create: `figures/src/make_figures.py`
- Create: `figures/fig1-framework.svg`, `.pdf`, `.png`
- Create: `figures/fig2-nonlinear-gating.svg`, `.pdf`, `.png`
- Create: `figures/fig3-study-program.svg`, `.pdf`, `.png`

- [ ] Encode the causal architecture with supported and hypothetical edge styles.
- [ ] Encode the Hill-gate, activation, uptake, leak, consumption, and net-reserve equations with an illustrative parameter dictionary in source.
- [ ] Label the four exposure zones and mark all simulated curves as illustrative.
- [ ] Encode cohort-to-validation-to-trial gating and genotype-specific modules.
- [ ] Run `python3 figures/src/make_figures.py`; expect nine non-empty outputs.
- [ ] Rasterize or inspect each PNG at full resolution; confirm no clipped or overlapping text.

### Task 3: Build the prospective cohort protocol

**Files:**
- Create: `protocols/prospective-cohort.md`

- [ ] Specify SCA3, SCA6, preataxic, early symptomatic, and control eligibility and exclusions.
- [ ] Define the four-year visit schedule and core, imaging, remote, and biospecimen measurements.
- [ ] Lock one confirmatory exposure family and one non-linear contrast before outcomes are unblinded.
- [ ] Define the biomarker-state slope estimand, interval-censored phenoconversion estimand, family/site structure, and external validation.
- [ ] State recruitment, retention, measurement-error, ancestry, migration, and reverse-causation safeguards.

### Task 4: Build the early-intervention master protocol

**Files:**
- Create: `protocols/early-intervention-trial.md`

- [ ] Define the prospective go/no-go phenotype and treatment-target validation gate.
- [ ] Specify a randomized, double-blind, sham-controlled, genotype-stratified design with dose selection and withdrawal.
- [ ] Define target engagement as primary and reserve disease modification for a later adequately powered trial.
- [ ] Specify randomization, concealment, blinding checks, safety stopping, intercurrent events, estimand, and sensitivity analyses.
- [ ] Report pooled and genotype-specific detectable-effect scenarios without claiming the study is powered for clinical progression.

### Task 5: Write the statistical analysis plan and sample-size scenarios

**Files:**
- Create: `protocols/statistical-analysis-plan.md`
- Create: `analysis/sample_size_scenarios.py`
- Create: `analysis/sample-size-scenarios.csv`

- [ ] Implement two-sample standardized-effect calculations for the phase Ib/IIa target-engagement endpoint.
- [ ] Implement slope-based scenarios for SCA3 and SCA6 progression using published annual rates as context, with explicitly assumed variance.
- [ ] Include attrition inflation and sensitivity grids; do not output a single context-free sample size.
- [ ] Run `python3 analysis/sample_size_scenarios.py`; expect deterministic CSV output.
- [ ] Define spline degrees of freedom, interaction hierarchy, cross-fitting, missing-data handling, multiplicity, and external validation.

### Task 6: Rewrite the manuscript

**Files:**
- Create: `manuscript/manuscript.md`
- Create: `manuscript/manuscript_zh.md`

- [ ] Replace the residual-onset primary analysis with one-stage survival modelling.
- [ ] Separate established evidence, analogy, prediction, and speculation in every major section.
- [ ] Integrate the three figures and move operational detail to protocol files.
- [ ] Add nested-model comparison, identifiability limits, negative evidence, falsification thresholds, and ethical boundaries.
- [ ] Ensure the abstract states that no evidence currently identifies `X` and that no intervention targets `X`.

### Task 7: Package and validate the repository

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `CITATION.cff`
- Create: `.gitignore`
- Create: `scripts/validate_repository.py`

- [ ] Document scope, evidence date, reproduction commands, and non-treatment disclaimer.
- [ ] Validate required files, generated formats, DOI syntax, Markdown links, and forbidden therapeutic claims.
- [ ] Run `python3 scripts/validate_repository.py`; expect all checks to pass.
- [ ] Run `git diff --check`; expect no whitespace errors.
- [ ] Review all generated artifacts and compare them line by line with the design acceptance criteria.

### Task 8: Publish

**Files:**
- Modify: Git history and GitHub repository metadata only.

- [ ] Inspect `git status -sb` and the full staged diff.
- [ ] Commit the complete scoped package with a concise message.
- [ ] Create `jieyangxchen/cerebellar-maintenance-reserve-gating-hypothesis` as a public repository and push `main`.
- [ ] Query GitHub for repository visibility, default branch, commit SHA, and public URL.
- [ ] Fetch the public README URL without credentials; expect HTTP 200.

