"""Day 3."""

import re
from collections.abc import Iterator

from attrs import define


@define(frozen=True)
class Number:
    value: int
    x1: int
    x2: int
    y: int

    def is_within(self, x, y):
        return self.x1 <= x <= self.x2 and self.y == y


@define(frozen=True)
class Gear:
    x: int
    y: int


@define(frozen=True)
class Engine:
    lines: list[str]

    @classmethod
    def from_data(cls, data: str) -> 'Engine':
        lines = data.splitlines()
        return cls(lines)

    def find_gears(self) -> Iterator[Gear]:
        for y, line in enumerate(self.lines):
            for x, symbol in enumerate(line):
                if symbol == '*':
                    yield Gear(x, y)

    def find_numbers(self) -> Iterator[Number]:
        for y, line in enumerate(self.lines):
            for m in re.finditer(r"\d+", line):
                yield Number(int(m.group()), m.start(), m.end() - 1, y)

    def is_part_number(self, n: Number) -> bool:
        for x in range(max(n.x1 - 1, 0), min(n.x2 + 2, len(self.lines[0]))):
            for y in range(max(n.y - 1, 0), min(n.y + 2, len(self.lines))):
                if not self.lines[y][x].isdigit() and self.lines[y][x] != '.':
                    return True

        return False

    def find_gear_numbers(self, g: Gear) -> Iterator[Number]:
        numbers = list(self.find_numbers())
        for x in range(max(g.x - 1, 0), min(g.x + 2, len(self.lines[0]))):
            for y in range(max(g.y - 1, 0), min(g.y + 2, len(self.lines))):
                for i, number in enumerate(numbers):
                    if number.is_within(x, y):
                        yield numbers.pop(i)


def part1(data: str) -> int:
    engine = Engine.from_data(data)
    numbers = engine.find_numbers()
    total = sum(n.value for n in numbers if engine.is_part_number(n))
    return total


def part2(data: str) -> int:
    engine = Engine.from_data(data)
    gears = engine.find_gears()
    numbers = [list(engine.find_gear_numbers(g)) for g in gears]
    total = sum(n[0].value * n[1].value for n in numbers if len(n) == 2)
    return total
