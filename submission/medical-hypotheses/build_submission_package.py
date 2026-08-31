#!/usr/bin/env python3
"""Build the deterministic Word package for Medical Hypotheses."""

from __future__ import annotations

import importlib.util
import re
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt


ROOT = Path(__file__).resolve().parents[2]
PACKAGE_DIR = Path(__file__).resolve().parent / "package"
LEGACY_BUILDER = ROOT / "submission" / "the-cerebellum" / "build_submission_package.py"

spec = importlib.util.spec_from_file_location("legacy_submission_builder", LEGACY_BUILDER)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Unable to load shared document helpers from {LEGACY_BUILDER}")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


TITLE = "The Maintenance–Reserve–Gating Hypothesis of Hereditary Cerebellar Ataxia"
SUBTITLE = "A testable model of non-linear modifier effects and delayed phenoconversion"
RUNNING_TITLE = "Maintenance–reserve–gating hypothesis in hereditary ataxia"
VERSION = "0.3.0"
PACKAGE_DATE = "31 August 2026"
EVIDENCE_CUTOFF = "19 August 2026"
FIXED_TIME = datetime(2026, 8, 31, 0, 0, 0, tzinfo=timezone.utc)

MAIN_DOCX = PACKAGE_DIR / "01_Main_Manuscript.docx"
TITLE_DOCX = PACKAGE_DIR / "02_Title_Page.docx"
COVER_DOCX = PACKAGE_DIR / "03_Cover_Letter.docx"
OUTPUTS = (MAIN_DOCX, TITLE_DOCX, COVER_DOCX)


def _extract_main_sections(text: str) -> tuple[str, str, str]:
    abstract_marker = "## Abstract"
    body_marker = "## Hypothesis and evidentiary boundary"
    abstract_start = text.index(abstract_marker) + len(abstract_marker)
    body_start = text.index(body_marker)
    abstract_and_keywords = text[abstract_start:body_start].strip()
    keyword_match = re.search(r"\*\*Keywords:\*\*\s*(.+)$", abstract_and_keywords, re.MULTILINE)
    if keyword_match is None:
        raise ValueError("Keywords not found in manuscript")
    keywords = keyword_match.group(1).strip()
    abstract = abstract_and_keywords[: keyword_match.start()].strip()
    body = text[body_start:].strip()
    return abstract, keywords, body


def _add_main_title_page(doc: Document) -> None:
    paragraph = doc.add_paragraph(style="Title")
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    base._add_inline_runs(paragraph, TITLE, size=14, default_bold=True)
    base._add_centered(doc, SUBTITLE, size=11, italic=True, after=10)
    base._add_centered(doc, base.AUTHOR, size=11, bold=True, after=4)
    base._add_centered(doc, f"ORCID: {base.ORCID}", size=10, after=2)
    base._add_centered(doc, base.AFFILIATION, size=10, after=2)
    base._add_centered(doc, f"Correspondence: {base.EMAIL}", size=10, after=10)
    base._add_centered(doc, "Article type: Hypothesis", size=9.5, after=3)
    base._add_centered(doc, f"Running title: {RUNNING_TITLE}", size=9.5, italic=True, after=3)
    base._add_centered(
        doc,
        f"Manuscript version {VERSION}; evidence cut-off {EVIDENCE_CUTOFF}",
        size=9.5,
        after=3,
    )
    base._add_centered(
        doc,
        f"Public preprint and research-planning repository: {base.REPOSITORY}",
        size=9.5,
        after=10,
    )
    base._add_centered(
        doc,
        "This hypothesis article reports no original human-participant or animal research.",
        size=9.5,
        italic=True,
        after=8,
    )
    doc.add_page_break()


def _configure_shared_globals() -> None:
    base.PACKAGE_DIR = PACKAGE_DIR
    base.TITLE = TITLE
    base.RUNNING_TITLE = RUNNING_TITLE
    base.VERSION = VERSION
    base.PACKAGE_DATE = PACKAGE_DATE
    base.EVIDENCE_CUTOFF = EVIDENCE_CUTOFF
    base.FIXED_TIME = FIXED_TIME
    base.MAIN_DOCX = MAIN_DOCX
    base.TITLE_DOCX = TITLE_DOCX
    base.COVER_DOCX = COVER_DOCX
    base.OUTPUTS = OUTPUTS
    base._extract_main_sections = _extract_main_sections
    base._add_main_title_page = _add_main_title_page


def _normalize_footer(doc: Document) -> None:
    """Use a centered numeric field so every rendered page number stays visible."""

    for section in doc.sections:
        for paragraph in section.footer.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.right_indent = Inches(0)
            for node in paragraph._p.iter():
                if node.tag.endswith("}t") and node.text == "Page ":
                    node.text = ""


def build_main_manuscript() -> Document:
    doc = base.build_main_manuscript()
    doc.core_properties.subject = "Hypothesis article for Medical Hypotheses"
    _normalize_footer(doc)
    return doc


def build_title_page() -> Document:
    doc = Document()
    base._configure_document(
        doc,
        title=f"Title page - {TITLE}",
        subject="Separate submission title page",
        header_text="Title page",
    )
    paragraph = doc.add_paragraph(style="Title")
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    base._add_inline_runs(paragraph, TITLE, size=14, default_bold=True)
    base._add_centered(doc, SUBTITLE, size=11, italic=True, after=10)
    base._add_centered(doc, base.AUTHOR, size=11, bold=True, after=3)
    base._add_centered(doc, f"ORCID: {base.ORCID}", size=10, after=2)
    base._add_centered(doc, base.AFFILIATION, size=10, after=2)
    base._add_centered(
        doc,
        f"Corresponding author: {base.AUTHOR} | {base.EMAIL}",
        size=10,
        after=12,
    )

    entries = (
        ("Running title", RUNNING_TITLE),
        ("Proposed article type", "Hypothesis"),
        ("Research status", "Hypothesis and critical review; no original participant-level or animal research"),
        ("Manuscript version", VERSION),
        ("Evidence cut-off", EVIDENCE_CUTOFF),
        ("Public preprint and repository", base.REPOSITORY),
        ("Funding", "This work received no external funding."),
        (
            "Competing interests",
            "The author declares no competing interests. The author retains copyright in the associated public repository and may consider future commercial-licensing requests. No commercial funding or payment was received for this work.",
        ),
        (
            "Author contribution",
            "Jieyang Chen conceived the hypothesis, performed the literature organization and claim audit, designed the proposed research programme, prepared the figures and reproducibility materials, and drafted and revised the manuscript.",
        ),
        ("Acknowledgements", "None."),
        (
            "AI-assisted tools",
            "During preparation, the author used OpenAI Codex for manuscript organization, language and readability editing, figure and repository-check code, and internal consistency review. The author reviewed and edited the output and remains fully responsible for the submitted work. OpenAI Codex is not an author.",
        ),
    )
    for label_text, value in entries:
        paragraph = doc.add_paragraph()
        label = paragraph.add_run(f"{label_text}: ")
        base._set_run_font(label, size=10, bold=True)
        base._add_inline_runs(paragraph, value, size=10)
    _normalize_footer(doc)
    return doc


def build_cover_letter() -> Document:
    doc = Document()
    base._configure_document(
        doc,
        title=f"Cover letter - {TITLE}",
        subject="Cover letter to Medical Hypotheses",
        header_text="Cover letter | Medical Hypotheses",
    )

    for line in (PACKAGE_DATE, "Editor-in-Chief and Editors", "Medical Hypotheses"):
        paragraph = doc.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(2)
        base._add_inline_runs(paragraph, line, size=10)
    doc.add_paragraph()
    salutation = doc.add_paragraph()
    base._add_inline_runs(salutation, "Dear Editor-in-Chief and Editors,", size=10)

    paragraphs = (
        f"I am submitting the manuscript entitled “{TITLE}” for consideration as a hypothesis article in Medical Hypotheses.",
        "The article proposes a nested, falsifiable explanation for timing heterogeneity in hereditary cerebellar ataxia. Its directly testable layer asks whether one outcome-blind, prospectively frozen measured exposure score shows a reproducible non-linear and genotype-specific association with phenoconversion and biomarker trajectories. Its optional mechanistic extension posits an unidentified input, activation/exchange gating, and dynamic reserve. The manuscript states explicitly that a statistical hump alone would not demonstrate gating.",
        "The hypothesis builds on established structural and functional concepts of cerebellar reserve. Its narrower novelty is the proposed activation–supply mismatch, the observation model linking dynamic reserve to phenoconversion, and layer-specific rejection rules. SCA3 is the primary proposed test bed and SCA6 a stringent transport test. The full protocol and statistical-analysis concepts remain in the public repository rather than being presented as validated methods or implementation-ready trials.",
        "The article reports no participant-level data and no new human or animal experiments. Current evidence supports component premises but does not demonstrate the unknown input, a gate, outward loss, or a hump-shaped human exposure curve. Those limitations, competing explanations, and results that would reject each layer are stated in the abstract and main text. The manuscript is a research hypothesis, not a treatment recommendation.",
        f"A preprint and supporting research-planning package are publicly available under a non-commercial licence at {base.REPOSITORY}. This history is disclosed transparently. The version submitted here is not under consideration by another journal.",
        "No external funding was received. The author declares no competing interests and no acknowledgements. The manuscript includes a declaration of the use of OpenAI Codex during preparation; the named author has reviewed the complete article and takes full responsibility for all scientific claims, references, figures, and wording.",
        "Thank you for considering this hypothesis.",
    )
    for text in paragraphs:
        paragraph = doc.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        base._add_inline_runs(paragraph, text, size=10)

    signature = doc.add_paragraph()
    signature.paragraph_format.space_before = Pt(5)
    signature.paragraph_format.space_after = Pt(0)
    signature.paragraph_format.keep_together = True
    for index, line in enumerate(
        ("Sincerely,", base.AUTHOR, base.AFFILIATION, base.EMAIL, f"ORCID: {base.ORCID}")
    ):
        if index:
            signature.add_run().add_break()
        base._add_inline_runs(signature, line, size=10)
    _normalize_footer(doc)
    return doc


def build_all() -> tuple[Path, ...]:
    _configure_shared_globals()
    builders = (
        (build_main_manuscript, MAIN_DOCX),
        (build_title_page, TITLE_DOCX),
        (build_cover_letter, COVER_DOCX),
    )
    for builder, destination in builders:
        base._deterministic_save(builder(), destination)
    base._write_hashes(OUTPUTS)
    return OUTPUTS


if __name__ == "__main__":
    for output in build_all():
        print(output.relative_to(ROOT))
