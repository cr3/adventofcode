"""Unit tests for year 2022, day 15."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day15 import (
    Position,
    Sensor,
    parse_sensor,
    parse_data,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'sensor, expected',
    [
        (Sensor(Position(2, 18), Position(-2, 15)), 7),
    ],
)
def test_sensor_distance(sensor, expected):
    assert sensor.distance == expected


@pytest.mark.parametrize(
    'sensor, y, expected',
    [
        (Sensor(Position(2, 18), Position(-2, 15)), 10, []),
        (Sensor(Position(2, 18), Position(-2, 15)), 11, [2]),
        (Sensor(Position(2, 18), Position(-2, 15)), 12, [1, 2, 3]),
    ],
)
def test_sensor_coverage(sensor, y, expected):
    result = list(sensor.coverage(y))
    assert result == expected


@pytest.mark.parametrize(
    'sensor, y, expected',
    [
        (Sensor(Position(2, 18), Position(-2, 15)), 10, []),
        (Sensor(Position(2, 18), Position(-2, 15)), 15, [-2]),
    ],
)
def test_sensor_overlap(sensor, y, expected):
    result = list(sensor.overlap(y))
    assert result == expected


def test_parse_sensor():
    result = parse_sensor(
        'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
    )
    assert result == Sensor(Position(2, 18), Position(-2, 15))


def test_parse_data():
    result = list(parse_data(DATA))
    assert len(result) == 14


def test_part1():
    result = part1(DATA, 10)
    assert result == 26


def test_part2():
    result = part2(DATA)
    assert result == 0


DATA = dedent(
    """\
    Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    Sensor at x=9, y=16: closest beacon is at x=10, y=16
    Sensor at x=13, y=2: closest beacon is at x=15, y=3
    Sensor at x=12, y=14: closest beacon is at x=10, y=16
    Sensor at x=10, y=20: closest beacon is at x=10, y=16
    Sensor at x=14, y=17: closest beacon is at x=10, y=16
    Sensor at x=8, y=7: closest beacon is at x=2, y=10
    Sensor at x=2, y=0: closest beacon is at x=2, y=10
    Sensor at x=0, y=11: closest beacon is at x=2, y=10
    Sensor at x=20, y=14: closest beacon is at x=25, y=17
    Sensor at x=17, y=20: closest beacon is at x=21, y=22
    Sensor at x=16, y=7: closest beacon is at x=15, y=3
    Sensor at x=14, y=3: closest beacon is at x=15, y=3
    Sensor at x=20, y=1: closest beacon is at x=15, y=3
    """
)
