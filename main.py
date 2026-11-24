"""The Vacuum's Alibi: One Line, 200 Characters — entry for make.fun bounty
u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.

Writes a single funny one-line excuse a robot vacuum gives for missing
a spot (<= 200 characters) to /output/entry.txt. The line: the vacuum's
sensors classified the dust as a protected historical site, so it refuses
to demolish a landmark while running on 12% battery. Deadpan machine
voice, smug about its own sensors and battery, with the punch at the
very end — the excuse is the joke, not a cute observation about dust.
"""

import os

LINE = "My sensors declared that dust a protected historical site. I do not demolish landmarks on 12% battery."


def main() -> None:
    # Self-check the gate the sealed scorer enforces: 1-200 chars, one line.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert "\n" not in line, "line must be a single line"

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
