#!/usr/bin/env python3
"""One Star, Written in Sap — entry program.

Writes a single one-line 1-star review, in the voice of a houseplant,
about the human who owns it, to /output/entry.txt.

Gate (from the kit): the file must be UTF-8 text of 1 to 279 characters,
not only white space.
"""

import os

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 He calls me 'low-maintenance,' then forgets me "
    "for three weeks, drowns me like he's putting out a fire, and acts "
    "betrayed when I drop a leaf. I'm not low-maintenance \u2014 I'm a "
    "hostage with good branding."
)

# Stock phrases the judge's brief penalises: drama-queen / dramatic-wilting
# / being-ignored clichés. The entry must contain none of them.
BANNED_PHRASES = (
    "drama queen",
    "dramatic wilting",
    "being ignored",
    "ignored me",
    "wilting dramatically",
)


def _check_type_and_length(text: str) -> None:
    """Stage 1: the entry must be a non-empty string within the gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 279:
        raise ValueError(
            f"entry must be 1-279 characters, got {len(text)}"
        )


def _check_single_line(text: str) -> None:
    """Stage 2: the review is a single line — no line breaks allowed."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")


def _check_banned_phrases(text: str) -> None:
    """Stage 3: reject the stock phrases the judge's brief penalises."""
    lowered = text.lower()
    for phrase in BANNED_PHRASES:
        if phrase in lowered:
            raise ValueError(f"entry contains banned stock phrase: {phrase!r}")


def _check_rating_present(text: str) -> None:
    """Stage 4: it must read as a one-star review — the star is present."""
    if "\u2605" not in text:
        raise ValueError("entry must carry its one-star rating")
    if text.count("\u2605") != 1:
        raise ValueError("entry must carry exactly one filled star")


def _check_voice_and_punctuation(text: str) -> None:
    """Stage 5 (new): the plant's voice and sentence shape must hold.

    The review is written in the first person, ends with terminal
    punctuation, and has no doubled spaces from sloppy joining.
    """
    if " I " not in text and not text.startswith("I "):
        raise ValueError("entry must be written in the plant's first person")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    if "  " in text:
        raise ValueError("entry must not contain doubled spaces")


def validate(text: str) -> None:
    """Enforce the kit's gate and the judge brief's format rules."""
    _check_type_and_length(text)
    _check_single_line(text)
    _check_banned_phrases(text)
    _check_rating_present(text)
    _check_voice_and_punctuation(text)


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
