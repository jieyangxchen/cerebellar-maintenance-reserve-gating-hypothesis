# The Cerebellum Submission Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a scientifically tightened manuscript and presubmission package tailored to *The Cerebellum* without overstating the unknown-input mechanism or clinical readiness.

**Architecture:** The English manuscript remains the canonical scientific narrative. The Chinese manuscript, evidence audit, bibliography, README, and journal-facing files mirror its terminology and evidence boundaries; detailed cohort, SAP, and trial documents remain public supporting resources.

**Tech Stack:** Markdown, BibTeX, TSV, Python repository validation, Matplotlib figure generation, Git.

---

### Task 1: Lock the target-journal design

**Files:**
- Create: `docs/superpowers/specs/2026-08-18-the-cerebellum-submission-design.md`
- Create: `docs/superpowers/plans/2026-08-18-the-cerebellum-submission.md`

- [ ] Record the approved title, two-layer claim architecture, prior-reserve distinction, protocol boundary, and journal-facing acceptance criteria.
- [ ] Scan both documents for `TBD`, `TODO`, contradictory article types, or claims that implementation has already occurred.
- [ ] Run `git diff --check`; expect no output.

### Task 2: Reframe the English manuscript

**Files:**
- Modify: `manuscript/manuscript.md`

- [ ] Replace the factor-led title and article label with the approved framework title and *The Cerebellum* new-idea/in-depth-review positioning.
- [ ] Replace the abstract with a single no-more-than-250-word abstract that states novelty, evidence limits, the nested tests, and the conclusion.
- [ ] Reduce keywords to six Index Medicus-compatible terms.
- [ ] Add a prior-framework section distinguishing cerebellar reserve from dynamic reserve `B(t)`.
- [ ] Present the observable modifier layer before the mechanistic gating extension.
- [ ] Add the threshold/hazard observation model and qualitative conditions required for the non-monotonic response.
- [ ] Reframe SCA3 as the primary test bed and SCA6 as transport/heterogeneity testing in the article narrative.
- [ ] Condense intervention details and point readers to the protocols.
- [ ] Add complete journal declarations while explicitly marking author-confirmation fields that cannot be inferred.

### Task 3: Synchronize evidence and references

**Files:**
- Modify: `manuscript/references.bib`
- Modify: `evidence/evidence-audit.md`
- Modify: `evidence/evidence-matrix.tsv`

- [ ] Add and audit Mitoma et al. 2020 cerebellar reserve and Mitoma et al. 2018 “Time Is Cerebellum.”
- [ ] Record that these sources support early reserve and intervention concepts but not `X`, gating, leakage, or a human exposure hump.
- [ ] Verify DOI syntax and direct publisher URLs with the repository validator.

### Task 4: Synchronize supporting narrative

**Files:**
- Modify: `manuscript/manuscript_zh.md`
- Modify: `README.md`
- Modify if terminology appears: `CITATION.cff`

- [ ] Apply the framework title and two-layer hierarchy in the Chinese working manuscript.
- [ ] Add the existing cerebellar-reserve distinction and clinical-transition bridge in Chinese.
- [ ] Reframe rural exposures and intervention modules consistently with the English manuscript.
- [ ] Update the README title, scientific-status table, and target-journal description without claiming acceptance or submission.

### Task 5: Create the journal-facing files

**Files:**
- Create: `submission/the-cerebellum/presubmission-inquiry.md`
- Create: `submission/the-cerebellum/submission-checklist.md`

- [ ] Draft a concise inquiry that identifies the proposed article category, explains fit with cerebellar function and ataxia, acknowledges prior cerebellar-reserve work, and asks the Editor whether a full submission is suitable.
- [ ] Include the public repository as a preprint/supporting-resource disclosure and state that the paper contains no participant-level data or treatment recommendation.
- [ ] Record the journal's 250-word abstract, six-keyword, Word, title-page, declarations, artwork, reviewer-suggestion, and non-simultaneous-submission requirements.
- [ ] Leave personal postal address, ORCID, final funding statement, final conflict statement, and named reviewer suggestions as author-confirmation gates rather than fabricating them.

### Task 6: Validate the optimized package

**Files:**
- Modify if required: `scripts/validate_repository.py`
- Modify if required: `tests/test_repository_tools.py`

- [ ] Add validation for the new title, abstract word limit, keyword count, reserve references, and submission files if current checks do not cover them.
- [ ] Run `python3 figures/src/make_figures.py`; expect all nine figure outputs to be regenerated without error.
- [ ] Run `python3 analysis/sample_size_scenarios.py`; expect deterministic CSV generation.
- [ ] Run `python3 scripts/validate_repository.py`; expect `Repository validation passed.`.
- [ ] Run `python3 -m unittest tests/test_repository_tools.py`; expect all tests to pass.
- [ ] Run `git diff --check`; expect no output.
- [ ] Inspect the final diff and verify that no journal acceptance, funding, conflict status, ORCID, affiliation, or clinical authorization was invented.
