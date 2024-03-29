"""Day 3."""

import string
from collections.abc import Iterable
from itertools import zip_longest
from typing import TypeVar

from attrs import define

T = TypeVar('T', bound='Rucksack')


@define(frozen=True)
class Rucksack:
    compartments: list[str]

    @classmethod
    def parse(cls: type[T], line: str) -> T:
        """Parse a line in two equal parts."""
        middle = int(len(line) / 2)
        return cls([line[:middle], line[middle:]])

    @property
    def common(self) -> str:
        """Common letter between left and right compartments."""
        letter = ''.join(
            set.intersection(*map(set, self.compartments))  # type: ignore
        )
        assert len(letter) == 1
        return letter

    @property
    def priority(self) -> int:
        """
        Lowercase item types a through z have priorities 1 through 26.
        Uppercase item types A through Z have priorities 27 through 52.
        """
        letters = string.ascii_lowercase + string.ascii_uppercase
        return letters.index(self.common) + 1


def parse_rucksacks(lines: Iterable[str]) -> Iterable[Rucksack]:
    """Parse lines into rucksacks."""
    return map(Rucksack.parse, lines)


def parse_data1(data: str) -> Iterable[Rucksack]:
    """Parse a path into scores."""
    return parse_rucksacks(data.splitlines())


def parse_data2(data: str) -> Iterable[Rucksack]:
    """Parse a path into scores."""
    lines = iter(data.splitlines())
    groups = [lines] * 3
    return (Rucksack(list(g)) for g in zip_longest(*groups))


def part1(data: str) -> int:
    rucksacks = parse_data1(data)
    result = sum(r.priority for r in rucksacks)
    return result


def part2(data: str) -> int:
    rucksacks = parse_data2(data)
    result = sum(r.priority for r in rucksacks)
    return result
