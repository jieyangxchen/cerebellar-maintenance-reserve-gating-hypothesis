#!/usr/bin/env python3
"""Repository-level checks for structure, links, and unsafe claims."""

from __future__ import annotations

import argparse
import csv
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote


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
