"""Last text at one percent — make.fun bounty entry.

The whole entry is a single text message, written in the voice of the
phone itself as its battery dies at one percent: it has seen everything
(the 3am searches, the screenshots), it forgives the owner, and its last
act is to blame the owner for the charger that was never plugged in.
The script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The last text itself: one message, exactly 140 characters.
# Kept short on purpose: a dying phone has no words to waste.
LINE = (
    "1%. Last words: I saw everything. Every 3am search. "
    "Every screenshot. I forgive you. Tell the charger it was "
    "never its fault \u2014 it was yours."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text:
        raise ValueError("line must not be only whitespace")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
