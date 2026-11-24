"""One Line, One Chill — make.fun entry.

Writes a single original horror sentence to <output dir>/entry.txt.
Deterministic, stdlib only, no network, no randomness, no clock use.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I lock my front door twice every night, and every morning "
    "it is locked twice — from the inside, by hands that are not mine."
)


def validate(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) >= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be under {MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be blank")
    # One sentence: exactly one sentence-terminating mark, at the very end.
    terminators = sum(text.count(mark) for mark in (".", "!", "?"))
    if terminators != 1 or text[-1] not in ".!?":
        raise ValueError("entry must be a single sentence")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
