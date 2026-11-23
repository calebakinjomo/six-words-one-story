"""Six Words, One Story — make.fun entry.

Writes one complete story, in exactly six words, to /output/entry.txt.
Deterministic: no network, no clock, no randomness, no environment reads.
"""

import os

STORY = "Grandma's recipe died with her. Almost."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
