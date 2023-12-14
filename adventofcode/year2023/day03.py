"""Day 3."""

import re

from attrs import define


@define(frozen=True)
class Number:
    value: int
    x1: int
    x2: int
    y: int


@define(frozen=True)
class Engine:
    lines: list[str]

    @classmethod
    def from_data(cls, data: str) -> 'Engine':
        lines = data.splitlines()
        return cls(lines)

    def find_numbers(self) -> Number:
        for y, line in enumerate(self.lines):
            for m in re.finditer(r"\d+", line):
                yield Number(int(m.group()), m.start(), m.end() - 1, y)

    def is_part_number(self, n: Number) -> bool:
        for x in range(max(n.x1 - 1, 0), min(n.x2 + 2, len(self.lines[0]))):
            for y in range(max(n.y - 1, 0), min(n.y + 2, len(self.lines))):
                if not self.lines[y][x].isdigit() and self.lines[y][x] != '.':
                    return True

        return False


def part1(data: str) -> int:
    engine = Engine.from_data(data)
    total = sum(
        n.value for n in engine.find_numbers() if engine.is_part_number(n)
    )
    return total


def part2(data: str) -> int:
    return 0
