#!/usr/bin/env python3
"""Repository-level checks for structure, links, and unsafe claims."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

MARKDOWN_LINK = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
DOI_DECLARATION = re.compile(r"\bdoi\s*[:=]", re.IGNORECASE)
DOI_VALUE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
LEGACY_MATH_DELIMITER = re.compile(r"\\(?:\[|\]|\(|\))")
UNSAFE_PATTERNS = (
    re.compile(r"\badminister(?:ing|ed)?\s+X\b", re.IGNORECASE),
    re.compile(r"\btreat(?:ing|ed|ment)?\s+(?:patients?\s+)?with\s+X\b", re.IGNORECASE),
    re.compile(r"给患者(?:直接)?(?:补充|使用|注射|照射)\s*X"),
)
TEXT_SUFFIXES = {".md", ".tsv", ".txt", ".bib", ".cff"}
EXCLUDED_PARTS = {".git", ".worktrees", ".venv", "tests", "__pycache__"}
NEGATION = re.compile(
    r"(?:\b(?:not|never|cannot|do\s+not|must\s+not|should\s+not|no\s+evidence\s+to)\b|不应|不能|不得|禁止)",
    re.IGNORECASE,
)
REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "manuscript/manuscript.md",
    "manuscript/manuscript_zh.md",
    "manuscript/references.bib",
    "protocols/prospective-cohort.md",
    "protocols/early-intervention-trial.md",
    "protocols/statistical-analysis-plan.md",
    "evidence/evidence-audit.md",
    "evidence/evidence-matrix.tsv",
    "submission/the-cerebellum/presubmission-inquiry.md",
    "submission/the-cerebellum/submission-checklist.md",
    "submission/medical-hypotheses/build_submission_package.py",
    "submission/medical-hypotheses/submission-checklist.md",
    "submission/medical-hypotheses/submission-readiness.md",
    "submission/medical-hypotheses/highlights.txt",
    "submission/medical-hypotheses/package/README.md",
    "submission/medical-hypotheses/package/01_Anonymized_Manuscript.docx",
    "submission/medical-hypotheses/package/02_Title_Page.docx",
    "submission/medical-hypotheses/package/03_Cover_Letter.docx",
    "submission/medical-hypotheses/package/04_Highlights.docx",
    "submission/medical-hypotheses/package/05_CRediT_Author_Statement.docx",
    "submission/medical-hypotheses/package/06_Declaration_of_Interest.docx",
    "submission/medical-hypotheses/package/07_Ethics_Statement.docx",
    "submission/medical-hypotheses/package/SHA256SUMS.txt",
    "figures/fig1-framework.svg",
    "figures/fig1-framework.pdf",
    "figures/fig1-framework.png",
    "figures/fig2-nonlinear-gating.svg",
    "figures/fig2-nonlinear-gating.pdf",
    "figures/fig2-nonlinear-gating.png",
    "figures/fig3-study-program.svg",
    "figures/fig3-study-program.pdf",
    "figures/fig3-study-program.png",
    "analysis/sample-size-scenarios.csv",
    "requirements.txt",
    "requirements-lock.txt",
)
EVIDENCE_COLUMNS = {
    "claim_id",
    "claim",
    "verdict",
    "claim_tier",
    "evidence_level",
    "model_or_population",
    "scope_limit",
    "source_url",
    "doi",
}
GENERATED_FILES = (
    "figures/fig1-framework.svg",
    "figures/fig1-framework.pdf",
    "figures/fig1-framework.png",
    "figures/fig2-nonlinear-gating.svg",
    "figures/fig2-nonlinear-gating.pdf",
    "figures/fig2-nonlinear-gating.png",
    "figures/fig3-study-program.svg",
    "figures/fig3-study-program.pdf",
    "figures/fig3-study-program.png",
    "analysis/sample-size-scenarios.csv",
)
LICENSE_MARKERS = {
    "LICENSE": "Attribution-NonCommercial 4.0 International",
    "README.md": "CC BY-NC 4.0",
    "CITATION.cff": "license: CC-BY-NC-4.0",
}
CURRENT_TARGET_TITLE = (
    "The Maintenance–Reserve–Gating Hypothesis of Hereditary Cerebellar Ataxia"
)
ABSTRACT_WORD = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9'–-]*\b")
RESERVE_PRIOR_ART_DOIS = (
    "10.1007/s12311-019-01091-9",
    "10.1007/s12311-018-0925-6",
)
CURRENT_WORD_OUTPUTS = (
    "01_Anonymized_Manuscript.docx",
    "02_Title_Page.docx",
    "03_Cover_Letter.docx",
    "04_Highlights.docx",
    "05_CRediT_Author_Statement.docx",
    "06_Declaration_of_Interest.docx",
    "07_Ethics_Statement.docx",
)
ANONYMOUS_IDENTITY_MARKERS = (
    "Jieyang Chen",
    "278404704@qq.com",
    "0009-0001-9247-2085",
    "Independent Researcher, Hangzhou, China",
    "jieyangxchen",
)
CORE_NAMESPACES = {
    "dc": "http://purl.org/dc/elements/1.1/",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
}


def _text_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            if not EXCLUDED_PARTS.intersection(path.relative_to(root).parts):
                yield path


def find_broken_local_links(root: Path) -> list[str]:
    errors: list[str] = []
    for source in _text_files(root):
        text = source.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{source.relative_to(root)}: missing local link {target}")
    return errors


def find_unsafe_claims(root: Path) -> list[str]:
    errors: list[str] = []
    for source in _text_files(root):
        text = source.read_text(encoding="utf-8")
        for pattern in UNSAFE_PATTERNS:
            for match in pattern.finditer(text):
                context = text[max(0, match.start() - 48) : match.start()]
                if NEGATION.search(context):
                    continue
                errors.append(
                    f"{source.relative_to(root)}: unsafe unknown-X treatment claim: {match.group(0)}"
                )
    return errors


def find_missing_required_files(
    root: Path,
    *,
    required: tuple[str, ...] = REQUIRED_FILES,
) -> list[str]:
    errors: list[str] = []
    for relative in required:
        path = root / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing required file: {relative}")
    return errors


def find_license_metadata_errors(root: Path) -> list[str]:
    """Require the legal text, README, and citation metadata to agree on BY-NC."""

    errors: list[str] = []
    for relative, marker in LICENSE_MARKERS.items():
        path = root / relative
        if not path.is_file():
            continue
        if marker not in path.read_text(encoding="utf-8"):
            errors.append(
                f"{relative}: expected non-commercial license marker: {marker}"
            )
    return errors


def find_invalid_doi_declarations(root: Path) -> list[str]:
    errors: list[str] = []
    for source in _text_files(root):
        for line_number, line in enumerate(
            source.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if DOI_DECLARATION.search(line) and not DOI_VALUE.search(line):
                errors.append(
                    f"{source.relative_to(root)}:{line_number}: invalid DOI declaration: {line.strip()}"
                )
    return errors


def find_legacy_math_delimiters(root: Path) -> list[str]:
    """Reject LaTeX delimiters that GitHub Markdown renders as literal text."""

    errors: list[str] = []
    for source in _text_files(root):
        if source.suffix.lower() != ".md":
            continue
        in_fence = False
        for line_number, line in enumerate(
            source.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            prose = re.sub(r"`[^`]*`", "", line)
            if LEGACY_MATH_DELIMITER.search(prose):
                errors.append(
                    f"{source.relative_to(root)}:{line_number}: "
                    "GitHub-incompatible math delimiter; use $...$ or $$...$$"
                )
    return errors


def find_evidence_matrix_errors(root: Path) -> list[str]:
    path = root / "evidence" / "evidence-matrix.tsv"
    if not path.is_file():
        return []

    errors: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fieldnames = set(reader.fieldnames or ())
        missing_columns = sorted(EVIDENCE_COLUMNS - fieldnames)
        if missing_columns:
            errors.append(
                "evidence/evidence-matrix.tsv: missing columns: "
                + ", ".join(missing_columns)
            )

        seen: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            claim_id = (row.get("claim_id") or "").strip()
            if claim_id in seen:
                errors.append(
                    f"evidence/evidence-matrix.tsv:{line_number}: duplicate claim_id: {claim_id}"
                )
            if claim_id:
                seen.add(claim_id)
            for column in EVIDENCE_COLUMNS & fieldnames:
                if not (row.get(column) or "").strip():
                    errors.append(
                        f"evidence/evidence-matrix.tsv:{line_number}: empty {column}"
                    )
            doi = (row.get("doi") or "").strip()
            if doi and doi != "NA" and not DOI_VALUE.fullmatch(doi):
                errors.append(
                    f"evidence/evidence-matrix.tsv:{line_number}: invalid DOI: {doi}"
                )
            source_url = (row.get("source_url") or "").strip()
            if source_url and source_url != "NA" and not source_url.startswith("https://"):
                errors.append(
                    f"evidence/evidence-matrix.tsv:{line_number}: invalid source_url: {source_url}"
                )
    return errors


def find_current_submission_readiness_errors(root: Path) -> list[str]:
    """Check stable journal-facing constraints in the current Markdown source."""

    manuscript_path = root / "manuscript" / "manuscript.md"
    bibliography_path = root / "manuscript" / "references.bib"
    if not manuscript_path.is_file():
        return []

    errors: list[str] = []
    manuscript = manuscript_path.read_text(encoding="utf-8")
    first_heading = next(
        (line[2:].strip() for line in manuscript.splitlines() if line.startswith("# ")),
        "",
    )
    if first_heading != CURRENT_TARGET_TITLE:
        errors.append("manuscript/manuscript.md: target title is not frozen")

    abstract_match = re.search(
        r"^## Abstract\s*$\n(.*?)(?=^\*\*Keywords:\*\*)",
        manuscript,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not abstract_match:
        errors.append("manuscript/manuscript.md: abstract block not found")
    else:
        abstract_words = ABSTRACT_WORD.findall(abstract_match.group(1))
        if len(abstract_words) > 250:
            errors.append(
                "manuscript/manuscript.md: abstract exceeds 250 words "
                f"({len(abstract_words)})"
            )

    keywords_match = re.search(r"^\*\*Keywords:\*\*\s*(.+)$", manuscript, re.MULTILINE)
    if not keywords_match:
        errors.append("manuscript/manuscript.md: keywords line not found")
    else:
        keywords = [item.strip() for item in keywords_match.group(1).split(";")]
        keywords = [item for item in keywords if item]
        if not 4 <= len(keywords) <= 6:
            errors.append(
                "manuscript/manuscript.md: keywords must number 4 to 6 "
                f"({len(keywords)})"
            )

    heading_levels = [
        len(match.group(1))
        for match in re.finditer(r"^(#+)\s+", manuscript, flags=re.MULTILINE)
    ]
    if heading_levels and max(heading_levels) > 3:
        errors.append(
            "manuscript/manuscript.md: heading level exceeds journal maximum of 3"
        )

    if "\n## References\n" in manuscript:
        body, references = manuscript.split("\n## References\n", maxsplit=1)
        reference_numbers = {
            int(number)
            for number in re.findall(r"^(\d+)\.\s+", references, flags=re.MULTILINE)
        }
        cited_numbers = {
            int(number)
            for group in re.findall(r"\[([0-9,\s–-]+)\]", body)
            for number in re.findall(r"\d+", group)
        }
        uncited = sorted(reference_numbers - cited_numbers)
        missing = sorted(cited_numbers - reference_numbers)
        if uncited:
            errors.append(
                "manuscript/manuscript.md: uncited numbered references: "
                + ", ".join(map(str, uncited))
            )
        if missing:
            errors.append(
                "manuscript/manuscript.md: citations missing from reference list: "
                + ", ".join(map(str, missing))
            )

    bibliography = (
        bibliography_path.read_text(encoding="utf-8")
        if bibliography_path.is_file()
        else ""
    )
    if any(doi not in bibliography for doi in RESERVE_PRIOR_ART_DOIS):
        errors.append(
            "manuscript/references.bib: missing cerebellar-reserve prior art"
        )
    for required_heading in (
        "### Ethics statement",
        "### CRediT author statement",
        "### Declaration of interest",
    ):
        if required_heading not in manuscript:
            errors.append(
                f"manuscript/manuscript.md: missing submission statement: {required_heading[4:]}"
            )
    return errors


def _docx_xml_text(path: Path) -> str:
    with zipfile.ZipFile(path, "r") as archive:
        return "\n".join(
            archive.read(name).decode("utf-8", errors="ignore")
            for name in archive.namelist()
            if name.endswith(".xml")
        )


def _docx_visible_text(path: Path) -> str:
    with zipfile.ZipFile(path, "r") as archive:
        document = ElementTree.fromstring(archive.read("word/document.xml"))
    return " ".join(text.strip() for text in document.itertext() if text.strip())


def _docx_metadata_errors(path: Path) -> list[str]:
    errors: list[str] = []
    with zipfile.ZipFile(path, "r") as archive:
        names = set(archive.namelist())
        if "docProps/custom.xml" in names:
            errors.append(f"{path.name}: custom Word properties were not removed")
        if "docProps/core.xml" in names:
            root = ElementTree.fromstring(archive.read("docProps/core.xml"))
            creator = root.find("dc:creator", CORE_NAMESPACES)
            modifier = root.find("cp:lastModifiedBy", CORE_NAMESPACES)
            if creator is not None and (creator.text or "").strip():
                errors.append(f"{path.name}: Word creator metadata is not blank")
            if modifier is not None and (modifier.text or "").strip():
                errors.append(f"{path.name}: Word last-modified-by metadata is not blank")
        story_parts = (
            name
            for name in names
            if name == "word/document.xml"
            or re.fullmatch(r"word/(?:header|footer)\d+\.xml", name)
            or name in {"word/footnotes.xml", "word/endnotes.xml"}
        )
        for part in story_parts:
            if re.search(rb"\brsid[A-Za-z]*=", archive.read(part)):
                errors.append(f"{path.name}: revision-session metadata remains in {part}")
    return errors


def find_double_blind_submission_errors(root: Path) -> list[str]:
    """Check the file-level anonymity and component constraints of the current package."""

    errors: list[str] = []
    submission = root / "submission" / "medical-hypotheses"
    package = submission / "package"
    anonymous = package / CURRENT_WORD_OUTPUTS[0]
    legacy_main = package / "01_Main_Manuscript.docx"
    if legacy_main.exists():
        errors.append("medical-hypotheses package: legacy author-identifying main file remains")

    highlights_path = submission / "highlights.txt"
    highlights: tuple[str, ...] = ()
    if highlights_path.is_file():
        highlights = tuple(
            line[2:].strip()
            for line in highlights_path.read_text(encoding="utf-8").splitlines()
            if line.startswith("- ")
        )
        if not 3 <= len(highlights) <= 5:
            errors.append("submission/medical-hypotheses/highlights.txt: expected 3 to 5 Highlights")
        for index, item in enumerate(highlights, start=1):
            if len(item) > 85:
                errors.append(
                    "submission/medical-hypotheses/highlights.txt: "
                    f"Highlight {index} exceeds 85 characters ({len(item)})"
                )

    for filename in CURRENT_WORD_OUTPUTS:
        path = package / filename
        if path.is_file():
            errors.extend(_docx_metadata_errors(path))

    if anonymous.is_file():
        xml_text = _docx_xml_text(anonymous).casefold()
        for marker in ANONYMOUS_IDENTITY_MARKERS:
            if marker.casefold() in xml_text:
                errors.append(
                    f"{anonymous.name}: author-identifying marker remains: {marker}"
                )
        visible = _docx_visible_text(anonymous)
        for forbidden_heading in ("CRediT author statement", "Acknowledgements"):
            if forbidden_heading in visible:
                errors.append(
                    f"{anonymous.name}: reviewer manuscript includes {forbidden_heading}"
                )

    expected_text = {
        "04_Highlights.docx": highlights,
        "05_CRediT_Author_Statement.docx": ("Jieyang Chen: Conceptualization",),
        "06_Declaration_of_Interest.docx": ("Declarations of interest: none.",),
        "07_Ethics_Statement.docx": ("Ethics approval and informed consent were not required",),
    }
    for filename, markers in expected_text.items():
        path = package / filename
        if path.is_file():
            visible = _docx_visible_text(path)
            for marker in markers:
                if marker not in visible:
                    errors.append(f"{filename}: missing expected text: {marker}")

    manifest = package / "SHA256SUMS.txt"
    if manifest.is_file():
        recorded: dict[str, str] = {}
        for line in manifest.read_text(encoding="utf-8").splitlines():
            if "  " in line:
                digest, filename = line.split("  ", maxsplit=1)
                recorded[filename] = digest
        if set(recorded) != set(CURRENT_WORD_OUTPUTS):
            errors.append("SHA256SUMS.txt: file list does not match current Word package")
        for filename in CURRENT_WORD_OUTPUTS:
            path = package / filename
            if path.is_file() and filename in recorded:
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                if recorded[filename] != actual:
                    errors.append(f"SHA256SUMS.txt: checksum mismatch for {filename}")
    return errors


def find_stale_generated_files(root: Path) -> list[str]:
    """Regenerate deterministic outputs and report checked-in byte mismatches."""

    from analysis.sample_size_scenarios import write_csv
    from figures.src.make_figures import generate_all

    errors: list[str] = []
    with tempfile.TemporaryDirectory() as temporary:
        generated_root = Path(temporary)
        generate_all(generated_root / "figures")
        write_csv(generated_root / "analysis" / "sample-size-scenarios.csv")
        for relative in GENERATED_FILES:
            checked_in = root / relative
            generated = generated_root / relative
            if checked_in.is_file() and checked_in.read_bytes() != generated.read_bytes():
                errors.append(f"stale generated file: {relative}")
    return errors


def validate_repository(root: Path) -> list[str]:
    return [
        *find_missing_required_files(root),
        *find_license_metadata_errors(root),
        *find_broken_local_links(root),
        *find_invalid_doi_declarations(root),
        *find_legacy_math_delimiters(root),
        *find_evidence_matrix_errors(root),
        *find_current_submission_readiness_errors(root),
        *find_double_blind_submission_errors(root),
        *find_stale_generated_files(root),
        *find_unsafe_claims(root),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    errors = validate_repository(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
