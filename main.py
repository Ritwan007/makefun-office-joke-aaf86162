#!/usr/bin/env python3
"""One-Line Office Joke entry for make.fun.

Writes a single one-line joke about office life to /output/entry.txt.
Competition: u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162
"""

import os

JOKE = "The printer only jams when a deadline is five minutes away. I'm starting to think it's in middle management."


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-200 chars of UTF-8 text,
    # not only whitespace, on exactly one line.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
