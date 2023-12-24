"""Day 6."""

import re
from collections.abc import Iterator
from itertools import starmap
from math import prod

from attrs import define


@define(frozen=True)
class Race:
    time: int
    distance: int

    def ways(self):
        for i in range(1, self.time):
            if i * (self.time - i) > self.distance:
                break
        else:
            raise ValueError("Cannot find ways")

        for j in range(i, self.time)[::-1]:  # pragma: nocover
            if j * (self.time - j) > self.distance:
                break

        return j - i + 1


def parse_line(line: str) -> Iterator[int]:
    return map(int, re.findall(r"\d+", line))


def parse_data(data: str) -> Iterator[Race]:
    inputs = map(parse_line, data.splitlines())
    return starmap(Race, zip(*inputs))


def part1(data: str) -> int:
    races = parse_data(data)
    return prod(r.ways() for r in races)


def part2(data: str) -> int:
    times, distances = map(parse_line, data.splitlines())
    time = int("".join(str(t) for t in times))
    distance = int("".join(str(d) for d in distances))
    race = Race(time, distance)
    return race.ways()
