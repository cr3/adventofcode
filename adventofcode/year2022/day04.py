"""Day 4."""

import re
from collections.abc import Iterable
from typing import TypeVar

from attrs import define

RangeType = TypeVar('RangeType', bound='Range')


@define(frozen=True)
class Range:
    start: int
    stop: int

    def __attrs_post_init__(self):
        assert self.start <= self.stop

    @classmethod
    def parse(cls: type[RangeType], part: str) -> RangeType:
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


@define(frozen=True)
class Pair:
    left: Range
    right: Range

    @classmethod
    def parse(cls: type[PairType], line: str) -> PairType:
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


def parse_data(data: str) -> Iterable[Pair]:
    return map(Pair.parse, data.splitlines())


def part1(data: str) -> int:
    pairs = parse_data(data)
    result = sum(pair.has_contains for pair in pairs)
    return result


def part2(data: str) -> int:
    pairs = parse_data(data)
    result = sum(pair.has_overlap for pair in pairs)
    return result
