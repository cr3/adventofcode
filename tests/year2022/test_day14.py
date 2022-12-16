"""Unit tests for year 2022, day 14."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day14 import (
    Rock,
    drop_rock,
    expand_rocks,
    parse_rocks,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'string, expected',
    [
        ('498,4', Rock(498, 4)),
        ('504,4', Rock(504, 4)),
    ],
)
def test_rock_from_string(string, expected):
    result = Rock.from_string(string)
    assert result == expected


@pytest.mark.parametrize(
    'rock, rocks, expected',
    [
        (Rock(500, 0), set(), Rock(500, 1)),
        (Rock(500, 0), set([Rock(500, 1)]), Rock(499, 1)),
        (Rock(500, 0), set([Rock(500, 1), Rock(499, 1)]), Rock(501, 1)),
        (
            Rock(500, 0),
            set([Rock(500, 1), Rock(499, 1), Rock(501, 1)]),
            Rock(500, 0),
        ),
    ],
)
def test_rock_step(rock, rocks, expected):
    result = rock.step(rocks)
    assert result == expected


@pytest.mark.parametrize(
    'rock, rocks, expected',
    [
        (Rock(500, 0), set([Rock(500, 1)]), False),
    ],
)
def test_drop_rock(rock, rocks, expected):
    result = drop_rock(rock, rocks)
    assert result is expected


@pytest.mark.parametrize(
    'start, end, expected',
    [
        (
            Rock(498, 4),
            Rock(498, 6),
            [Rock(498, 4), Rock(498, 5), Rock(498, 6)],
        ),
        (
            Rock(498, 6),
            Rock(496, 6),
            [Rock(498, 6), Rock(497, 6), Rock(496, 6)],
        ),
    ],
)
def test_expand_rocks(start, end, expected):
    result = list(expand_rocks(start, end))
    assert result == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        (
            '498,4 -> 498,6',
            [Rock(498, 4), Rock(498, 5), Rock(498, 6)],
        ),
        (
            '498,4 -> 498,6 -> 496,6',
            [
                Rock(498, 4),
                Rock(498, 5),
                Rock(498, 6),
                Rock(498, 6),
                Rock(497, 6),
                Rock(496, 6),
            ],
        ),
    ],
)
def test_parse_rocks(line, expected):
    result = list(parse_rocks(line))
    assert result == expected


def test_part1():
    result = part1(DATA)
    assert result == 24


def test_part2():
    result = part2(DATA)
    assert result == 93


DATA = dedent(
    """\
    498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9
    """
)
