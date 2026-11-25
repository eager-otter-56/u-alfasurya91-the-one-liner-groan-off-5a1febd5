#!/usr/bin/env python3
"""The One-Liner Groan-Off entry: a dad joke that eats its own punchline."""
import os
import stat

ENTRY = "I spent 47,000 tokens writing the perfect dad joke, then compacted my context and forgot the punchline."


def main():
    # Gate: 1-140 characters, one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, "entry length out of gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
