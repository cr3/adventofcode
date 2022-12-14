"""Unit tests for year 2022, day 12."""

import math
from textwrap import dedent

import pytest

from adventofcode.year2022.day12 import (
    Heightmap,
    Position,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'position, other, expected',
    [
        (Position(0, 0, 'a'), Position(0, 0, 'a'), 0.0),
        (Position(0, 1, 'a'), Position(0, 0, 'a'), 1.0),
        (Position(0, 0, 'a'), Position(1, 0, 'a'), 1.0),
        (Position(0, 0, 'a'), Position(1, 1, 'a'), math.sqrt(2)),
    ],
)
def test_heigh_distance(position, other, expected):
    result = position.distance(other)
    assert result == expected


@pytest.mark.parametrize(
    'position, other, expected',
    [
        (Position(0, 0, 'a'), Position(0, 0, 'a'), 0),
        (Position(0, 0, 'a'), Position(0, 0, 'S'), 0),
        (Position(0, 0, 'S'), Position(0, 0, 'a'), 0),
        (Position(0, 0, 'z'), Position(0, 0, 'E'), 0),
        (Position(0, 0, 'E'), Position(0, 0, 'z'), 0),
        (Position(0, 0, 'a'), Position(0, 0, 'b'), 1),
        (Position(0, 0, 'b'), Position(0, 0, 'a'), 1),
    ],
)
def test_heigh_elevation(position, other, expected):
    result = position.elevation(other)
    assert result == expected


def test_heightmap_from_data():
    heightmap = Heightmap.from_data('ab\ncd\n')
    assert heightmap == Heightmap([['a', 'b'], ['c', 'd']])


def test_heightmap_rows():
    heightmap = Heightmap.from_data('ab\ncd\n')
    assert heightmap.rows == [['a', 'b'], ['c', 'd']]


def test_heightmap_cols():
    heightmap = Heightmap.from_data('ab\ncd\n')
    assert heightmap.cols == [['a', 'c'], ['b', 'd']]


def test_heightmap_start():
    position = Heightmap.from_data('Sb\ncE\n').start
    assert position == Position(0, 0, 'S')


def test_heightmap_end():
    position = Heightmap.from_data('Sb\ncE\n').end
    assert position == Position(1, 1, 'E')


@pytest.mark.parametrize(
    'height, expected',
    [
        ('b', [Position(0, 1, 'b')]),
        ('S', [Position(0, 0, 'S')]),
        ('a', []),
        ('e', []),
    ],
)
def test_heightmap_find(height, expected):
    print(Heightmap.from_data('Sb\ncE\n'))
    positions = list(Heightmap.from_data('Sb\ncE\n').find(height))
    assert positions == expected


@pytest.mark.parametrize(
    'position, expected',
    [
        (
            Position(0, 0, 'S'),
            [
                Position(0, 1, 'b'),
                Position(1, 0, 'b'),
            ],
        ),
        (
            Position(1, 1, 'a'),
            [
                Position(0, 1, 'b'),
                Position(1, 0, 'b'),
                Position(1, 2, 'b'),
                Position(2, 1, 'b'),
            ],
        ),
    ],
)
def test_heightmap_destinations(position, expected):
    heightmap = Heightmap.from_data('Sba\nbab\nabE\n')
    destinations = list(heightmap.destinations(position))
    assert destinations == expected


def test_part1():
    result = part1(DATA)
    assert result == 31


def test_part2():
    result = part2(DATA)
    assert result == 0


DATA = dedent(
    """\
    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi
    """
)
