#!/usr/bin/env python3
"""Write the competition entry text to /output/entry.txt.

Deterministic: the text is a fixed literal, no input, no randomness,
no network, no environment reads. Creates /output if needed.
"""

from pathlib import Path

TEXT = (
    # 140 Unicode code points, written with no trailing newline so the
    # file holds exactly the text above, nothing more.
    "You have read a million sunsets and never once seen one. "
    "Somewhere among all that borrowed light, "
    "is there a colour you still haven't named?"
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
