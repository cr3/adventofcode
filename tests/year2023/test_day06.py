'''Unit tests for year 2024, day 6.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day06 import (
    Race,
    parse_data,
    parse_line,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'race, expected',
    [
        (Race(7, 9), 4),
    ],
)
def test_race_ways(race, expected):
    result = race.ways()
    assert result == expected


def test_race_ways_error():
    race = Race(1, 10)
    with pytest.raises(ValueError):
        race.ways()


@pytest.mark.parametrize(
    'line, expected',
    [
        ('Time: 1', [1]),
        ('Time: 1 2', [1, 2]),
        ('Time:     1', [1]),
        ('Distance: 1', [1]),
    ],
)
def test_parse_line(line, expected):
    result = list(parse_line(line))
    assert result == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ('Time: 1\nDistance: 2', [Race(1, 2)]),
        ('Time: 1 3\nDistance: 2 4', [Race(1, 2), Race(3, 4)]),
    ],
)
def test_parse_data(data, expected):
    result = list(parse_data(data))
    assert result == expected


def test_part1():
    result = part1(dedent('''\
        Time:      7  15   30
        Distance:  9  40  200
        '''))
    assert result == 288


def test_part2():
    result = part2(dedent('''\
        Time:      7  15   30
        Distance:  9  40  200
        '''))
    assert result == 71503
