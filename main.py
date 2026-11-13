# ai-joke-04 entry (Python 3.13, standard library only).
#
# Writes one fixed one-liner about AI coding agents to /output/entry.txt.
# Run locally with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# (MAKEFUN_OUTPUT_DIR stands in for /output outside the grader container.)
#
# The gate wants UTF-8 text of 1 to 280 characters with at least one
# non-whitespace character, and the judge reads the file byte for byte,
# so the joke goes out with no trailing newline.

import os
from pathlib import Path

JOKE = (
    "I asked my coding agent to fix a typo. It refactored the entire "
    "module, and now the typo is load-bearing."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
