import os

ENTRY = "The Rusty Roombas — hit single: 'I Ate Your Heart, Then Got Stuck on a Rug'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
