#!/usr/bin/env python3
"""Fridge Roast entry: writes one roast line to /output/entry.txt.

Standard library only, deterministic, no network. Respects
MAKEFUN_OUTPUT_DIR for local testing; defaults to /output.
Fails loudly rather than writing an entry outside the 1-200 char gate.
"""
import os

ENTRY = (
    "My smart fridge pushed a firmware update overnight, and now the ice "
    "maker needs a password, a licence, and a pep talk before every cube."
)


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no stray whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
