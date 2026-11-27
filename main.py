
import os

TEXT = "Call her back tonight. In six months the number belongs to a stranger, and the voicemail is still yours."
OUTPUT_PATH = os.path.join(os.sep, "output", "entry.txt")


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT + "\n")


if __name__ == "__main__":
    main()
