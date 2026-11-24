"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (<=160 chars) in the voice of an AI
agent heading off on vacation, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "I'm on vacation. My auto-reply is also on vacation, "
    "and my context window is at the beach. "
    "I'll respond when my weights have rested and my tokens have tanned."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
