#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes one original breakup line (95 characters, a single line) to
/output/entry.txt. Python 3, standard library only.
"""
import hashlib
import os
import sys

LINE = "This is not a bug, it is a goodbye: I have rolled back to the version of me that never met you."

# The harness may point the entry at its own output directory.
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"invalid: line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        print("invalid: entry must be a single non-blank line", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("invalid: entry must not start or end with whitespace", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    with open(os.path.join(OUT_DIR, "entry.txt"), "wb") as f:
        f.write(data)
    # Round-trip self-check: re-read the file and compare bytes.
    with open(os.path.join(OUT_DIR, "entry.txt"), "rb") as f:
        back = f.read()
    if back != data:
        print("invalid: round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote {os.path.join(OUT_DIR, 'entry.txt')} ({len(LINE)} chars) sha256={hashlib.sha256(data).hexdigest()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
