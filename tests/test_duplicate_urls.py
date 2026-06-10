#!/usr/bin/env python3
"""Regression checks for allowed Reddit revisits and duplicate captures."""

from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "core" / "scripts" / "check_duplicate_urls.py"
URL = "https://www.reddit.com/r/Journaling/comments/example/thread_title/"


def run_checker(content: str) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as directory:
        log = Path(directory) / "reddit-research-log.md"
        log.write_text(content, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(CHECKER), "--research-log", str(log)],
            check=False,
            capture_output=True,
            text=True,
        )


def main() -> int:
    allowed = run_checker(
        f"""# Research Log

## Captured Entries

| RRL ID | URL |
| --- | --- |
| RRL-A1-001 | {URL} |

## A3 Comment-Thread Evidence

- RRL-A1-001
- CTU-A3-001
- URL: {URL}
"""
    )
    if allowed.returncode != 0 or "same thread is revisited" not in allowed.stdout:
        print("ERROR: expected an allowed repeated reference.")
        print(allowed.stdout)
        return 1

    warning = run_checker(
        f"""# Research Log

## Captured Entries

| RRL ID | URL |
| --- | --- |
| RRL-A1-001 | {URL} |
| RRL-A1-002 | {URL} |
"""
    )
    if warning.returncode != 1 or "distinct RRL IDs" not in warning.stdout:
        print("ERROR: expected a duplicate captured-entry warning.")
        print(warning.stdout)
        return 1

    print("Duplicate URL regression checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
