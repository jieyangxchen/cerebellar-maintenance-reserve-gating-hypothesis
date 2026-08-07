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

The submitted model avoids an unconstrained collection of latent variables. Candidate measured exposures form `E(t)`. A preregistered mapping may define a low-dimensional input score `X(t)`, but an unrestricted post-hoc score is prohibited. Genotype and baseline physiology define coupling `R` without using future onset or progression. Dynamic reserve `B(t)` is the only mechanistic state variable. A biomarker factor `L(t)` is a measurement model for observed readouts, not a second free causal substance.

Three nested models are compared:

- `M0`: genotype, known modifiers, age, ancestry, site, and known exposures.
- `M1`: `M0` plus reserve/biomarker-state dynamics.
- `M2`: `M1` plus preregistered non-linear exposure and genotype-by-exposure terms.

The gating extension survives only if `M2` improves calibration and out-of-sample prediction in an external cohort and reproduces the direction and location of the risk region. Residual age at onset plots may be descriptive, but the confirmatory analysis uses one-stage interval-censored survival models rather than treating residuals as error-free outcomes.

## Figures

Three original, reproducible figures will be generated as SVG, PDF, and 600-dpi PNG:

1. **Causal architecture and evidence tiers.** Genotype, known pathology, measured environment, gate, reserve, biomarker state, multi-cellular network, dysfunction, and degeneration; solid and dashed edges distinguish supported and hypothetical links.
2. **Non-monotonic gating curve.** An explicitly illustrative parameter set shows low-input idle, intermediate-input activation plus leakage and maximal reserve loss, and high-input rebalancing. The caption states that the curves are predictions, not patient data.
3. **Prospective test-and-intervene programme.** A longitudinal SCA3/SCA6 cohort feeds a locked external validation and a gated, biomarker-enriched, sham-controlled proof-of-mechanism trial.

## Cohort protocol

The prospective cohort is multicentre, family-aware, four-year, and genotype-stratified. It targets 360 expansion carriers (240 SCA3, 120 SCA6) plus 120 genetically unaffected relatives or demographically matched controls, with approximately equal preataxic and early symptomatic representation where feasible. The primary estimand is the difference in a preregistered longitudinal biomarker-state slope across exposure regions and genotypes. Phenoconversion is important but secondary because expected event counts are too small for a flexible confirmatory non-linear model.

Core visits occur at baseline and months 6, 12, 18, 24, 36, and 48. Blood NfL, blinded SARA/f-SARA, digital gait and balance, eye movements, medication and exposure updates occur at each core visit. Harmonized structural MRI and genotype-specific MRS occur annually. Dense remote exposure and wearable sampling reduces recall bias. One candidate exposure family and one non-linear contrast are confirmatory; additional exposome analyses are exploratory and use false-discovery-rate control.

## Early-intervention trial

SCA3 and SCA6 do not share a validated disease-modifying agent. The repository therefore specifies a common master protocol and genotype-specific intervention appendices. The executable first module is a phase Ib/IIa, biomarker-enriched, sham-controlled **functional-downshift proof-of-mechanism** study, activated only after the cohort prospectively validates a reproducible, directionally interpretable hyperactivity phenotype and a human-safe modulation method.

The target is mechanism engagement, not a registration claim. A pooled primary analysis is allowed only if the treatment-by-genotype interaction passes the prespecified compatibility criterion; genotype-specific estimates are always reported. The primary endpoint is change in a locked network-hyperactivity composite after four weeks. NfL, genotype-specific MRS, digital balance, SARA/f-SARA, patient-reported function, withdrawal reversibility, and safety are secondary or exploratory. A 48-week extension estimates persistence but is not labelled proof of neuroprotection.

A scenario target of 96 randomized participants (48 per genotype; 1:1 active/sham) is justified for pooled target engagement around standardized effect `d=0.58` with 80% power before attrition, while acknowledging that each genotype-specific contrast is powered only for a larger effect near `d=0.82`. A definitive progression trial requires new pilot variance estimates and substantially larger genotype-specific samples.

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

