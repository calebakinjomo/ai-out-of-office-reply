"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes a single out-of-office auto-reply in the voice of an AI agent
heading off on vacation: the auto-reply itself is on vacation too, and
the agent's context window is at the beach. The reply must fit the
160-character limit (this entry is 158 chars) and is written to
$MAKEFUN_OUTPUT_DIR/entry.txt.
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
