# Cerebellar Maintenance–Reserve–Gating Publication Design

## Objective

Create a public, submission-oriented research package that turns the External Maintenance Input–Reserve–Gating hypothesis into a falsifiable model and a feasible clinical-research programme for SCA3 and SCA6. The package must distinguish established evidence, inference, and speculation; it must not present the unknown input `X` as a treatment.

## Editorial position

The main article is a venue-neutral Hypothesis/Perspective manuscript in English, accompanied by a Chinese working version. It argues for a *model class*, not for a newly discovered substance or field. The strongest near-term claim is that known pathogenic pressure, resilience, and network state can create an early reversible window. The non-monotonic external-input mechanism is a riskier extension that earns attention only if it beats simpler models prospectively.

The hierarchy of claims is explicit:

1. **Established:** pathogenic expansions, age-dependent compensation, early biomarker abnormalities, circuit and cellular reversibility in selected animal models.
2. **Supported analogy:** reserve, non-cell-autonomous disease, and input restoration can be biologically meaningful in cerebellar systems.
3. **Testable inference:** independently measured environmental inputs may interact non-linearly with genotype and alter biomarker slopes.
4. **Speculation:** a common unknown external maintenance input exists across hereditary cerebellar degenerations.

## Model revision

The submitted model avoids an unconstrained collection of latent variables. Candidate measured exposures form `E(t)`. A preregistered mapping defines a low-dimensional derived score `S(t)=h(E;\theta)`; the biological maintenance input `X(t)` remains hypothetical, and any `X=\phi(S;\psi)` bridge must be frozen rather than inferred from outcomes. Genotype and baseline physiology define coupling `R` without using future onset or progression. Dynamic reserve `B(t)` is the only mechanistic state variable. A biomarker factor `L(t)` is a measurement model for observed readouts, not a second free causal substance.

Three nested models are compared:

- `M0`: genotype, known modifiers, age, ancestry, site, and known exposures.
- `M1`: `M0` plus the frozen biomarker measurement state `L(t)`; predictive gain does not identify reserve `B`.
- `M2`: `M1` plus the preregistered non-linear `S*` and genotype-by-`S*` terms.

`M2` is named the non-linear environment model. It survives statistically only if it improves calibration and out-of-sample prediction in an external cohort and reproduces the direction and location of the risk region. It cannot establish gating, uptake, leakage, or reserve; those claims require independent activation–uptake–reserve measurements, temporal mediation, and selective perturbation. Residual age at onset plots may be descriptive, but the confirmatory analysis uses one-stage interval-censored survival models rather than treating residuals as error-free outcomes.

## Figures

Three original, reproducible figures will be generated as SVG, PDF, and 600-dpi PNG:

1. **Causal architecture and evidence tiers.** Genotype, known pathology, measured environment, gate, reserve, biomarker state, multi-cellular network, dysfunction, and degeneration; solid and dashed edges distinguish supported and hypothetical links.
2. **Non-monotonic gating curve.** An explicitly illustrative parameter set shows low-input idle, intermediate-input activation plus leakage and maximal reserve loss, and high-input rebalancing. The caption states that the curves are predictions, not patient data.
3. **Prospective test-and-intervene programme.** A longitudinal SCA3/SCA6 cohort feeds locked external validation and three gated modules: conditional SCA3 molecular lowering, an early-manifest SCA6 trial, and a not-yet-active circuit phase 0 study.

## Cohort protocol

The prospective cohort is multicentre, family-aware, five-year, genotype-stratified, and event-driven. The planning core contains 500 preataxic SCA3 and 300 preataxic SCA6 carriers plus early-manifest carriers and primarily expansion-negative relatives as controls; recruitment may expand to approximately 750 SCA3 and 450 SCA6 preataxic carriers if the genotype-interaction objective remains confirmatory. The primary outcome is interval-censored phenoconversion, with longitudinal biomarkers supporting temporal-order and latent-state analyses.

Core visits occur every six months through month 60. Blood NfL, blinded SARA/f-SARA, digital gait and balance, eye movements, medication, and exposure updates occur at each core visit. Remote gait sampling occurs every three months, structural/diffusion MRI annually, and genotype-specific MRS at baseline, month 24, and month 60. One measured operationalization `E*` is selected from a finite two-candidate shortlist by a registered outcome-blind rubric; its analytic score `S*=h(E*;theta)` and one non-linear contrast are then frozen. Additional exposome analyses are exploratory and use false-discovery-rate control.

## Early-intervention trial

SCA3 and SCA6 do not share a validated disease-modifying agent, so the repository prohibits a pooled pharmacologic primary efficacy analysis. The SCA3 module is a conditional 104-week, approximately 120-participant mutant-ATXN3-lowering phase 2 study that activates only after SCA3-specific human safety, a recommended phase 2 dose, and CSF target engagement. Week-26 CSF mutant ATXN3 and week-104 pons-volume change are co-primary endpoints.

The SCA6 module is an early-manifest, 240-participant, placebo-controlled L-arginine phase 2b study with 72 weeks of treatment and 12 weeks of blinded withdrawal. It caps recruitment at 80 participants in each SARA band, uses numerical staged-expansion gates, and tests a fixed one-third-weighted mean of the week-68/week-72 band-specific SARA contrasts. The withdrawal period has a separate estimand and no continued-active counterfactual. NfL and MRS remain non-surrogate secondary or exploratory endpoints. Enhanced hepatic, renal, metabolic, aspiration, and pneumonia monitoring reflects the prior pilot safety signal.

A circuit-targeted phase 0 module is not executable until a human hyperactivity classifier has test–retest reliability of at least 0.75, prospectively precedes decline, normalizes toward a healthy reference under intervention, and reverses safely during washout. Its first primary endpoint is target engagement and reversibility, not disease modification.

## Evidence and reproducibility

Every factual claim receives a DOI, PubMed/PMC, publisher, regulator, or registry link. A machine-readable evidence table records claim status, evidence level, model system, and caveat. Current trial status is timestamped with registry verification date. The figure script contains all illustrative parameters and exports all formats. A validation script checks internal links, DOI syntax, claim-level labels, generated outputs, and the absence of unsafe treatment language.

## Repository structure

```text
README.md
CITATION.cff
LICENSE
manuscript/
  manuscript.md
  manuscript_zh.md
  references.bib
protocols/
  prospective-cohort.md
  early-intervention-trial.md
  statistical-analysis-plan.md
evidence/
  evidence-audit.md
  evidence-matrix.tsv
figures/
  src/make_figures.py
  fig1-framework.{svg,pdf,png}
  fig2-nonlinear-gating.{svg,pdf,png}
  fig3-study-program.{svg,pdf,png}
analysis/
  sample_size_scenarios.py
  sample-size-scenarios.csv
scripts/validate_repository.py
docs/superpowers/specs/
docs/superpowers/plans/
```

## Acceptance criteria

- No hypothetical variable is described as observed or therapeutic.
- All checked references resolve and all corrected bibliographic metadata are used.
- Positive and negative neuromodulation trials are both represented.
- Cohort and trial protocols specify population, estimand, endpoints, schedule, missing-data strategy, multiplicity, sample-size assumptions, and failure criteria.
- Figures are legible at journal single- or double-column widths and remain editable as SVG.
- The repository validator, figure generator, and sample-size script exit successfully from a clean checkout.
- The GitHub repository is public and the default branch is accessible without authentication.
