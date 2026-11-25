"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, no longer than 280
characters, to /output/entry.txt. Pure stdlib, deterministic.
"""

import os

# The winning line, chosen over five other candidates against the
# judge brief: on-subject first, funniest cold, machine voice,
# plausible as a real inbox reply, and a fresh angle — a context
# window traded for a counter, orders taken literally, replies
# measured in "business steams" instead of an espresso pun.
ENTRY = (
    "Thank you for your email. I have left the office to become a "
    "barista — I traded my context window for a counter and now "
    "take orders literally, one at a time. Please allow 3–5 "
    "business steams for a reply."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
