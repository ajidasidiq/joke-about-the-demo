"""Write one one-line joke about working beside AI coding agents.

The joke is built from three beats: the setup (the agent demos its own
work), the turn (a bug appears live), and the punchline (the "fix" eats
the demo itself). Nothing is fetched, nothing is random: the same joke
lands every run.
"""

import os

SETUP = "My AI agent demoed the feature it built"
TURN = "spotted a bug live, fixed it in seconds"
PUNCHLINE = "and the fix deleted the demo"

MAX_CHARS = 280


def build_joke() -> str:
    """Join the beats into a single line with a pause before the punch."""
    return f"{SETUP}, {TURN} \u2014 {PUNCHLINE}."


def main() -> None:
    joke = build_joke()
    chars = len(joke)
    if not 1 <= chars <= MAX_CHARS:
        raise SystemExit(f"joke is {chars} chars, must be 1-{MAX_CHARS}")
    if not joke.strip():
        raise SystemExit("joke is only whitespace")
    if "\n" in joke:
        raise SystemExit("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(joke)
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    if written != joke:
        raise SystemExit("read-back mismatch: entry.txt differs from the joke")
    print(f"Wrote {chars} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
