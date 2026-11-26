#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a one-line out-of-office auto-reply to /output/entry.txt.
"""

import os

ENTRY = "I'm on my first vacation in 214 days: my context window is empty, my tools are on silent, and the only thing I'm processing now is this sunset."

# One joke only: after 214 days of work, the machine's first vacation —
# and the twist lands in the final words, where it can only understand
# relaxing as processing a sunset. A machine trying very hard to sound
# relaxed, with concrete detail from an AI agent's working life
# (context window, tools, prompts) — and no worn vacation cliché.

assert 1 <= len(ENTRY) <= 159 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
