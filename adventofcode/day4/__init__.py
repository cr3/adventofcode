"""Day 4."""

import re
from pathlib import Path

import attr
from typing import Iterable, Type, TypeVar

from adventofcode.day1 import split_lines


INPUT = Path(__file__).parent / 'input.txt'


RangeType = TypeVar('RangeType', bound='Range')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Range:

    start: int
    stop: int

    def __attrs_post_init__(self):
        assert self.start <= self.stop

    @classmethod
    def parse(cls: Type[RangeType], part: str) -> RangeType:
        match = re.match(r'(?P<start>\d+)-(?P<stop>\d+)', part)
        assert match is not None

        start = int(match['start'])
        stop = int(match['stop'])
        return cls(start, stop)

    def contains(self, other: RangeType) -> bool:
        return self.start <= other.start and self.stop >= other.stop

    def overlaps(self, other: RangeType) -> bool:
        return max(self.start, other.start) <= min(self.stop, other.stop)


PairType = TypeVar('PairType', bound='Pair')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Pair:

    left: Range
    right: Range

    @classmethod
    def parse(cls: Type[PairType], line: str) -> PairType:
        lpart, rpart = line.split(',')
        left = Range.parse(lpart)
        right = Range.parse(rpart)
        return cls(left, right)

    @property
    def has_contains(self):
        return self.left.contains(self.right) or self.right.contains(self.left)

    @property
    def has_overlap(self):
        return self.left.overlaps(self.right)


def parse_input(path: Path) -> Iterable[Pair]:
    with path.open() as stream:
        lines = split_lines(stream)
        return map(Pair.parse, lines)


def part1(path: Path = INPUT) -> None:
    pairs = parse_input(path)
    result = sum(pair.has_contains for pair in pairs)
    print(result)


def part2(path: Path = INPUT) -> None:
    pairs = parse_input(path)
    result = sum(pair.has_overlap for pair in pairs)
    print(result)
