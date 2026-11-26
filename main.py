#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes one funny line about an AI agent's worst Monday to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Python 3.13 standard library only; no network at run time.
"""

import os

LINE = "Monday: I hallucinated an API, deployed it, and production believed me."


def main() -> None:
    # Gate assertions: the entry must be exactly one line of 1-140
    # characters, non-empty and not only whitespace.
    assert LINE, "entry must be non-empty"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be exactly one line"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written entry does not match"


if __name__ == "__main__":
    main()
