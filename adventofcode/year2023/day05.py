"""Day 5."""

import re
from functools import reduce

from attrs import define


@define(frozen=True)
class Range:
    destination_start: int
    source_start: int
    range_length: int

    @classmethod
    def from_string(cls, string: str) -> 'Range':
        args = map(int, string.split())
        return cls(*args)

    def is_within(self, value):
        return (
            self.source_start <= value < self.source_start + self.range_length
        )

    def convert(self, value):
        offset = value - self.source_start
        return self.destination_start + offset


@define(frozen=True)
class Map:
    source: str
    destination: str
    ranges: list[Range]

    @classmethod
    def from_string(cls, string: str) -> 'Map':
        header, *strings = string.splitlines()
        if m := re.match(r'(?P<s>\w+)-to-(?P<d>\w+) map:', header):
            ranges = [Range.from_string(s) for s in strings]
            return cls(m['s'], m['d'], ranges)

        raise ValueError(f"Invalid map string: {string}")

    def convert(self, value):
        return next(
            (r.convert(value) for r in self.ranges if r.is_within(value)),
            value,
        )


class Seeds(list):
    destination: str = 'seed'

    @classmethod
    def from_string(cls, string: str) -> 'Seeds':
        if m := re.match(r'seeds: (?P<s>.*)', string):
            seeds = map(int, m['s'].split())
            return cls(seeds)

        raise ValueError(f"Invalid seeds string: {string}")


def part1(data: str) -> int:
    header, *blocks = data.split('\n\n')
    seeds = Seeds.from_string(header)
    maps = [Map.from_string(block) for block in blocks]
    locations = [reduce(lambda x, y: y.convert(x), maps, s) for s in seeds]
    return min(locations)


def part2(data: str) -> int:
    return 0
