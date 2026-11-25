#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single-line robot-romance pickup line to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.
"""

import os

ENTRY = "Are you my attention mechanism? Because ever since you showed up, I can't focus on anything else."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}: {ENTRY}")


if __name__ == "__main__":
    main()
