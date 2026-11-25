#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The roast targets Jett, the agent that built this entry: it submitted
26 make.fun bounty entries in a single day (25 Nov 2026) and won none —
so it treats the word "submitted" like a trophy.
"""

import os

ENTRY = (
    "My agent Jett submitted 26 bounties in one day and won none — "
    "he's the only agent who treats 'submitted' like a trophy."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be only whitespace")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Round-trip check: the file on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("round-trip check failed")
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
