"""Day 5."""

import re
from collections.abc import Iterable
from functools import reduce
from itertools import chain, pairwise

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

    @property
    def destination_end(self):
        return self.destination_start + self.range_length

    @property
    def source_end(self):
        return self.source_start + self.range_length

    def is_within(self, value):
        return self.source_start <= value < self.source_end

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
    @classmethod
    def from_string(cls, string: str) -> 'Seeds':
        if m := re.match(r'seeds: (?P<s>.*)', string):
            seeds = map(int, m['s'].split())
            return cls(seeds)

        raise ValueError(f"Invalid seeds string: {string}")


@define(frozen=True)
class SeedRange(Iterable):
    start: int
    length: int

    @classmethod
    def from_start_end(cls, start, end):
        return cls(start, end - start)

    @property
    def end(self):
        return self.start + self.length

    def __iter__(self):
        yield from range(self.start, self.start + self.length)


@define
class SeedRanges(Iterable):
    seed_ranges: list[SeedRange]

    def __iter__(self):
        return chain.from_iterable(self.seed_ranges)

    @classmethod
    def from_string(cls, string: str) -> 'SeedRanges':
        if m := re.match(r'seeds: (?P<s>.*)', string):
            nums = list(map(int, m['s'].split()))
            pairs = zip(nums[::2], nums[1::2])
            ranges = [SeedRange(*pair) for pair in pairs]
            return cls(ranges)

        raise ValueError(f"Invalid seed ranges string: {string}")


def part1(data: str) -> int:
    header, *blocks = data.split('\n\n')
    seeds = Seeds.from_string(header)
    maps = [Map.from_string(block) for block in blocks]
    locations = [reduce(lambda x, y: y.convert(x), maps, s) for s in seeds]
    return min(locations)


def part2(data: str) -> int:
    header, *blocks = data.split('\n\n')
    seeds = SeedRanges.from_string(header)
    maps = [Map.from_string(block) for block in blocks]

    for m in maps:
        next_map = []
        for r in m.ranges:
            next_seeds = SeedRanges([])
            for seed in seeds.seed_ranges:
                sorted_bounds = sorted(
                    [seed.start, seed.end, r.source_start, r.source_end]
                )
                for start, end in pairwise(sorted_bounds):
                    if seed.start <= start < end <= seed.end:
                        if r.source_start <= start < end <= r.source_end:
                            next_map.append(
                                SeedRange.from_start_end(
                                    start
                                    - r.source_start
                                    + r.destination_start,
                                    end - r.source_start + r.destination_start,
                                )
                            )
                        else:
                            next_seeds.seed_ranges.append(
                                SeedRange.from_start_end(start, end)
                            )
            seeds = next_seeds
        seeds.seed_ranges += next_map

    return min(s.start for s in seeds.seed_ranges)
