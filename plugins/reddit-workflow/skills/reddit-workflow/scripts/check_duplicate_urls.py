#!/usr/bin/env python3
"""Distinguish allowed repeated Reddit references from duplicate captured entries."""

from argparse import ArgumentParser
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Optional
from urllib.parse import urlsplit, urlunsplit


URL_RE = re.compile(r"https?://(?:www\.|old\.)?reddit\.com/[^\s)>\]\"']+", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
RRL_RE = re.compile(r"\bRRL-[A-Z0-9]+-\d+\b")
CTU_RE = re.compile(r"\bCTU-[A-Z0-9]+-\d+\b")
ENTRY_ROW_RE = re.compile(r"^\|\s*(RRL-[A-Z0-9]+-\d+)\s*\|")
UPDATE_KEYWORDS = (
    "a2", "a3", "comment", "comment-level", "comment-thread", "ctu",
    "deepening", "evidence update", "batch", "reprocess", "revisit",
    "browser_opened_reddit_page",
)
ENTRY_SECTIONS = ("research queue", "captured entries")


@dataclass
class UrlHit:
    line_number: int
    original_url: str
    normalized_url: str
    line: str
    section: str
    rrl_ids: set[str] = field(default_factory=set)
    ctu_ids: set[str] = field(default_factory=set)
    entry_rrl_id: Optional[str] = None
    is_entry_row: bool = False
    is_update_context: bool = False
    is_entry_section: bool = False


def normalize_url(url: str) -> str:
    parts = urlsplit(url.rstrip(".,;"))
    netloc = parts.netloc.lower()
    if netloc == "old.reddit.com":
        netloc = "www.reddit.com"
    return urlunsplit((parts.scheme.lower(), netloc, parts.path.rstrip("/"), "", ""))


def contains(text: str, keywords: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in keywords)


def warning_reason(hits: list[UrlHit]) -> Optional[str]:
    entry_hits = [hit for hit in hits if hit.is_entry_row]
    entry_ids = {hit.entry_rrl_id for hit in entry_hits if hit.entry_rrl_id}
    if len(entry_ids) > 1:
        return "same URL appears as captured entries under distinct RRL IDs"
    uncaveated_entries = [
        hit for hit in entry_hits if hit.is_entry_section and not hit.is_update_context
    ]
    if len(uncaveated_entries) > 1:
        return "same URL appears multiple times in queue or captured-entry context"
    return None


def allowed_reason(hits: list[UrlHit]) -> str:
    entry_rrl_ids = {hit.entry_rrl_id for hit in hits if hit.entry_rrl_id}
    all_rrl_ids = set().union(*(hit.rrl_ids for hit in hits))
    if len(entry_rrl_ids) == 1 and entry_rrl_ids.issubset(all_rrl_ids):
        return "same thread is revisited under its existing RRL ID"
    if any(hit.ctu_ids or "/comment/" in hit.normalized_url for hit in hits):
        return "same thread is referenced in comment-thread evidence"
    if any(hit.is_update_context for hit in hits):
        return "same thread appears across stage, revisit, or evidence-update sections"
    return "repeated reference does not look like a new captured entry"


def describe(hit: UrlHit) -> str:
    rrl = ", ".join(sorted(hit.rrl_ids)) or "none"
    ctu = ", ".join(sorted(hit.ctu_ids)) or "none"
    kind = "entry" if hit.is_entry_row else "reference"
    return (
        f"  line {hit.line_number}: {kind}; section={hit.section!r}; "
        f"RRL={rrl}; CTU={ctu}; url={hit.original_url}"
    )


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--research-log", required=True)
    args = parser.parse_args()
    path = Path(args.research_log)
    if not path.is_file():
        print(f"Research log not found: {path}")
        return 1

    groups: dict[str, list[UrlHit]] = defaultdict(list)
    section = "document root"
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        heading = HEADING_RE.match(line)
        if heading:
            section = heading.group(2).strip()
        entry = ENTRY_ROW_RE.match(line)
        context = f"{section} {line}"
        for url in URL_RE.findall(line):
            normalized = normalize_url(url)
            groups[normalized].append(
                UrlHit(
                    line_number=number,
                    original_url=url,
                    normalized_url=normalized,
                    line=line,
                    section=section,
                    rrl_ids=set(RRL_RE.findall(line)),
                    ctu_ids=set(CTU_RE.findall(line)),
                    entry_rrl_id=entry.group(1) if entry else None,
                    is_entry_row=entry is not None,
                    is_update_context=contains(context, UPDATE_KEYWORDS),
                    is_entry_section=contains(section, ENTRY_SECTIONS),
                )
            )

    repeated = {url: hits for url, hits in groups.items() if len(hits) > 1}
    allowed = {}
    warnings = {}
    for url, hits in repeated.items():
        reason = warning_reason(hits)
        (warnings if reason else allowed)[url] = (reason or allowed_reason(hits), hits)

    if not repeated:
        print(f"No repeated Reddit URLs found in {path}.")
        return 0

    print(f"Repeated Reddit URL review for {path}")
    print("\nRepeated references allowed")
    if not allowed:
        print("  None")
    for url, (reason, hits) in sorted(allowed.items()):
        print(f"\n{url}\n  Reason: {reason}")
        for hit in hits:
            print(describe(hit))

    print("\nPotential duplicate entries requiring review")
    if not warnings:
        print("  None")
    for url, (reason, hits) in sorted(warnings.items()):
        print(f"\n{url}\n  Warning: {reason}")
        for hit in hits:
            print(describe(hit))

    print("\nSummary")
    print(f"  Repeated URL groups reviewed: {len(repeated)}")
    print(f"  Allowed repeated reference groups: {len(allowed)}")
    print(f"  Potential duplicate entry groups: {len(warnings)}")
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
