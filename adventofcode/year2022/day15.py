"""Day 15."""

import re
from itertools import chain, tee
from typing import Iterable

import attr


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Position:
    x: int
    y: int


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Sensor:
    spot: Position
    beacon: Position

    @property
    def distance(self):
        return sum(
            [
                abs(self.spot.x - self.beacon.x),
                abs(self.spot.y - self.beacon.y),
            ]
        )

    def coverage(self, y: int) -> Iterable[int]:
        segment = self.distance - abs(self.spot.y - y)
        x1 = self.spot.x - segment
        x2 = self.spot.x + segment
        return range(x1, x2 + 1)

    def overlap(self, y: int) -> Iterable[int]:
        if self.beacon.y == y:
            yield self.beacon.x


def parse_sensor(line: str) -> Sensor:
    match = re.match(
        r'Sensor at x=(?P<spot_x>-?\d+), y=(?P<spot_y>-?\d+): '
        r'closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)',
        line,
    )
    assert match
    return Sensor(
        Position(int(match['spot_x']), int(match['spot_y'])),
        Position(int(match['beacon_x']), int(match['beacon_y'])),
    )


def parse_data(data: str) -> Iterable[Sensor]:
    return map(parse_sensor, data.splitlines())


def part1(data: str, y: int = 2000000) -> int:
    coverage_sensors, overlap_sensors = tee(parse_data(data))
    overlap = len(
        set(chain.from_iterable(s.overlap(y) for s in overlap_sensors))
    )
    coverage = len(
        set(chain.from_iterable(s.coverage(y) for s in coverage_sensors))
    )
    return coverage - overlap


def part2(data: str) -> int:
    parse_data(data)
    return 0
