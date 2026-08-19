# The Cerebellum Upload Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a locally reviewable, journal-compliant Word submission package for *The Cerebellum* from the validated v0.2.1 repository sources.

**Architecture:** Keep `manuscript/manuscript.md` and the three protocol Markdown files as canonical sources. A deterministic Python builder creates four Word deliverables with journal-plain typography, embedded original figures, editable Word-equation objects, declarations, automatic page numbering, and a shared evidence cut-off; rendered PNGs are QA intermediates only.

**Tech Stack:** Markdown, Python, python-docx, OOXML/OMML, LibreOffice headless rendering, repository validation, Git worktree.

---

### Task 1: Record the inquiry and package state

**Files:**
- Modify: `submission/the-cerebellum/presubmission-inquiry.md`
- Modify: `submission/the-cerebellum/submission-checklist.md`
- Create: `submission/the-cerebellum/package/README.md`

- [x] Change the inquiry status from draft to submitted on 19 August 2026 through the Springer Nature journal contact form, with the editor reply still pending.
- [x] Mark only the presubmission-send item complete; retain article-category and GitHub-policy confirmation as pending editorial decisions.
- [x] Add a package manifest that distinguishes upload-ready files, author-confirmation gates, and files that remain supporting repository resources rather than clinical protocols ready for use.
- [x] Run `git diff --check`; expect no output.

### Task 2: Build the Word deliverables deterministically

**Files:**
- Create: `submission/the-cerebellum/build_submission_package.py`
- Create: `submission/the-cerebellum/package/01_Main_Manuscript.docx`
- Create: `submission/the-cerebellum/package/02_Title_Page.docx`
- Create: `submission/the-cerebellum/package/03_Cover_Letter.docx`
- Create: `submission/the-cerebellum/package/04_Supplementary_Protocols.docx`

- [x] Implement the journal-plain design: US Letter, 1-inch margins, Times New Roman 10 pt body, no more than three heading levels, black text, restrained spacing, and inline figures.
- [x] Convert display equations into editable OMML equation paragraphs and keep short inline mathematical variables editable in text.
- [x] Add automatic page numbering and quiet running headers without decorative manuscript styling.
- [x] Build the main manuscript from the English canonical source, excluding repository-only metadata from the article body while retaining title-page facts, abstract, six keywords, declarations, figure captions, and references.
- [x] Build a separate title page with author, ORCID, affiliation, correspondence email, funding, competing interests, contribution, and repository/preprint disclosure.
- [x] Build a cover letter that keeps the requested article category conditional on the presubmission reply, states the falsifiable novelty and evidence limits, discloses the public GitHub history, and confirms no original participant or animal research.
- [x] Build a supplementary protocol document containing the prospective cohort, SAP, and early-intervention concepts with a prominent non-clinical-use notice.
- [x] Re-run the builder and compare SHA-256 hashes; expect identical output from identical sources.

### Task 3: Prepare publication-grade figure files

**Files:**
- Modify: `figures/src/make_figures.py`
- Create: `figures/Fig1.eps`
- Create: `figures/Fig2.eps`
- Create: `figures/Fig3.eps`

- [x] Configure embedded TrueType fonts for PDF/PS output and export each original figure as EPS in addition to SVG, PDF, and PNG.
- [x] Regenerate all figure formats from source and verify that no patient data or external copyrighted artwork is introduced.
- [x] Check that the Word manuscript uses high-resolution PNGs inline while the package manifest identifies EPS/PDF/SVG as editable submission alternatives.

### Task 4: Render and inspect every Word page

**Files:**
- Create as QA intermediates only: `submission/the-cerebellum/qa-render/*/page-*.png`

- [x] Render all four Word files with the packaged `render_docx.py` to QA page images.
- [x] Inspect every page image at full scale for clipping, overlaps, broken equations, bad page breaks, missing glyphs, detached captions, and unreadable figures.
- [x] Run the images audit on the main manuscript and supplementary protocols; expect only inline images.
- [x] Fix defects and repeat rendering until the latest render passes visual inspection.

### Task 5: Validate and hand off without publishing

**Files:**
- Modify if required by generated-package checks: `submission/the-cerebellum/submission-checklist.md`

- [x] Confirm the abstract remains at most 250 words and the keyword count remains six after Word conversion.
- [x] Run `.venv/bin/python scripts/validate_repository.py`; expect `Repository validation passed.`.
- [x] Run `.venv/bin/python -m unittest tests/test_repository_tools.py`; expect 32 passing tests.
- [x] Run `git diff --check`; expect no output.
- [x] Review `git status` and the complete diff, and leave all changes uncommitted for author inspection because no commit or push was requested.
