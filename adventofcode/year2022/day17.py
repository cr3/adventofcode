"""Day 17."""

import re
from collections.abc import Iterator
from enum import Enum
from itertools import cycle, takewhile
from textwrap import dedent

import attr


class Jet(Enum):
    L = '<'
    R = '>'


@attr.s(slots=True, auto_attribs=True)
class Cave:
    """
    A cave is a list of rows that grows towards higher indices.
    """

    rows: list[str]
    space: str = '.' * 7
    rock_counter: int = 0
    height_to_rocks: dict[int, int] = attr.ib(factory=dict)

    def add(self, rock: list[str]) -> 'Cave':
        """Add a rock to the top of the cave."""
        indent = 2
        width = len(self.space)
        i = len(self.rows)
        self.rows[i:] = [self.space] * 3 + [
            '.' * indent
            + row.replace('#', '@')
            + '.' * (width - indent - len(row))
            for row in reversed(rock)
        ]
        return self

    def push(self, jet: Jet) -> bool:
        """Push the latest rock left or right if possible."""
        i, rows = map(
            list, zip(*((i, r) for i, r in enumerate(self.rows) if '@' in r))
        )
        if push_rock(rows, jet):  # type: ignore
            start, end = i[0], i[-1] + 1  # type: ignore
            self.rows[start:end] = rows  # type: ignore
            return True

        return False

    def fall(self) -> bool:
        """Make the latest rock fall one unit if possible."""
        cols = list(map(''.join, zip(*self.rows)))
        if push_rock(cols, Jet.L):
            self.rows[:] = list(map(''.join, zip(*cols)))
            if self.rows[-1] == self.space:
                del self.rows[-1]
            return True
        else:
            cols = [c.replace('@', '#') for c in cols]
            self.rows[:] = list(map(''.join, zip(*cols)))
            self.rock_counter += 1
            self.height_to_rocks[len(self.rows)] = self.rock_counter
            return False

    def push_and_fall(
        self, jets: Iterator[Jet], rocks: Iterator[list[str]], count: int
    ) -> 'Cave':
        for _ in range(count):
            self.add(next(rocks))
            while True:
                self.push(next(jets))
                if not self.fall():
                    break

        return self


def push_rock(rows: list[str], jet: Jet) -> bool:
    if jet == Jet.R:
        if any(re.search(r'@$|@#', r) for r in rows):
            return False
        rows[:] = [re.sub(r'(@+)\.', r'.\1', r) for r in rows]
        return True
    else:  # jet == Jet.L
        if any(re.search(r'^@|#@', r) for r in rows):
            return False
        rows[:] = [re.sub(r'\.(@+)', r'\1.', r) for r in rows]
        return True

    return False


def parse_jets(data: str) -> Iterator[Jet]:
    return cycle(map(Jet, data.strip()))  # type: ignore


def parse_rocks() -> Iterator[list[str]]:
    return cycle(text.splitlines() for text in dedent("""\
                ####

                .#.
                ###
                .#.

                ..#
                ..#
                ###

                #
                #
                #
                #

                ##
                ##
                """).split('\n\n'))


def longest_common_rows(rows: list[str]) -> tuple[int, int]:
    result = (0, 0)
    longest = 0
    n = len(rows)
    for i in range(n):
        for j in range(i + 1, n):
            length = len(
                list(
                    takewhile(lambda x: x[0] == x[1], zip(rows[i:], rows[j:]))
                )
            )
            if length > longest:
                longest = length
                result = (i, j)

    return result


def factor_rocks(data: str, num_rocks: int, sample: int) -> tuple[int, int]:
    cave = Cave([]).push_and_fall(parse_jets(data), parse_rocks(), sample)
    i, j = longest_common_rows(cave.rows)
    repeating_rows = j - i
    repeating_rocks = cave.height_to_rocks[j] - cave.height_to_rocks[i]
    num_rows = (
        (num_rocks - cave.height_to_rocks[i]) // repeating_rocks
    ) * repeating_rows
    remaining_rocks = (
        (num_rocks - cave.height_to_rocks[i]) % repeating_rocks
    ) + cave.height_to_rocks[i]

    return (num_rows, remaining_rocks)


def part1(data: str, sample: int = 2000) -> int:
    num_rows, remaining_rocks = factor_rocks(data, 2022, sample)

    cave = Cave([]).push_and_fall(
        parse_jets(data), parse_rocks(), remaining_rocks
    )
    return len(cave.rows) + num_rows


def part2(data: str, sample: int = 2000) -> int:
    num_rows, remaining_rocks = factor_rocks(data, 1_000_000_000_000, sample)

    cave = Cave([]).push_and_fall(
        parse_jets(data), parse_rocks(), remaining_rocks
    )
    return len(cave.rows) + num_rows
