"""Day 15."""

import re
from collections.abc import Iterable
from itertools import chain, starmap, tee

from attrs import define


@define(frozen=True)
class Position:
    x: int
    y: int


@define(frozen=True)
class Sensor:
    spot: Position
    beacon: Position

    @property
    def distance(self):
        return sum([
            abs(self.spot.x - self.beacon.x),
            abs(self.spot.y - self.beacon.y),
        ])

    @property
    def outer_edges(self) -> Iterable[Position]:
        outer = self.distance + 1
        upper = zip(
            range(self.spot.x - outer, self.spot.x + outer + 1),
            [
                *range(self.spot.y, self.spot.y + outer),
                *range(self.spot.y + outer, self.spot.y - 1, -1),
            ],
        )
        lower = zip(
            range(self.spot.x - outer + 1, self.spot.x + outer),
            [
                *range(self.spot.y - 1, self.spot.y - outer, -1),
                *range(self.spot.y - outer, self.spot.y),
            ],
        )
        return starmap(Position, [*upper, *lower])

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


def part1(data: str, y: int = 2_000_000) -> int:
    coverage_sensors, overlap_sensors = tee(parse_data(data))
    overlap = len(
        set(chain.from_iterable(s.overlap(y) for s in overlap_sensors))
    )
    coverage = len(
        set(chain.from_iterable(s.coverage(y) for s in coverage_sensors))
    )
    return coverage - overlap


def part2(data: str, boundary: int = 4_000_000) -> int:
    sensors = list(parse_data(data))
    for sensor in sensors:
        for position in sensor.outer_edges:
            if 0 <= position.x <= boundary and 0 <= position.y <= boundary:
                for s in sensors:
                    if position.x in s.coverage(position.y):
                        break
                else:
                    return position.x * 4_000_000 + position.y
    else:
        raise AssertionError(f'Beacon not found within {boundary}')
