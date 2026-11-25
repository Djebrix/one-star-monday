#!/usr/bin/env python3
"""One Star for Monday — writes a one-star review of Monday to entry.txt.

Stdlib only, no network, deterministic.
"""

import os

LINE = "One star. Monday sat me by the fire exit, served my coffee cold, and charged me for the weekend I never got."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
