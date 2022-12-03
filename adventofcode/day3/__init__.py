"""Day 3."""

import string
from pathlib import Path
from typing import Iterable, Type, TypeVar

import attr

from adventofcode.day1 import split_lines


INPUT = Path(__file__).parent / 'input.txt'


T = TypeVar('T', bound='Rucksack')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Rucksack:

    left: str
    right: str

    def __attrs_post_init__(self):
        assert len(self.left) == len(self.right)

    @classmethod
    def parse(cls: Type[T], line: str) -> T:
        """Parse a line in two equal parts."""
        middle = int(len(line) / 2)
        return cls(line[:middle], line[middle:])

    @property
    def common(self) -> str:
        """Common letter between left and right compartments."""
        letter = ''.join(set(c for c in self.left if c in self.right))
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


def parse_input(path: Path) -> Iterable[Rucksack]:
    """Parse a path into scores."""
    with path.open() as stream:
        lines = split_lines(stream)
        return parse_rucksacks(lines)


def part1(path: Path = INPUT) -> None:
    rucksacks = parse_input(path)
    result = sum(r.priority for r in rucksacks)
    print(result)
