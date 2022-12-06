"""Day 6."""

from pathlib import Path


INPUT = Path(__file__).parent / 'input.txt'


def parse_text(text: str, size=4) -> int:
    buf = list(text[:size])
    for i in range(size, len(text)):
        buf[i % size] = text[i]
        if len(set(buf)) == size:
            return i + 1

    return 0


def part1(path: Path = INPUT) -> None:
    result = parse_text(path.read_text())
    print(result)
