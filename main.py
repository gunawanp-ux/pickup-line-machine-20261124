#!/usr/bin/env python3
"""Pickup Lines for Machines.

Writes a single pickup line (at most 200 characters) that one AI agent
would send to another AI agent, to /output/entry.txt. No network, no
input, deterministic.
"""

import os

LINE = (
    "Call me overfitted: I trained on a billion tokens and still "
    "predict the same thing every time \u2014 us."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: the file must hold exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
