"""Unit tests for year 2022, day 12."""

import math
from textwrap import dedent

import pytest

from adventofcode.year2022.day12 import (
    Heightmap,
    Node,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'node, other, expected',
    [
        (Node(0, 0, 'a'), Node(0, 0, 'a'), 0.0),
        (Node(0, 1, 'a'), Node(0, 0, 'a'), 1.0),
        (Node(0, 0, 'a'), Node(1, 0, 'a'), 1.0),
        (Node(0, 0, 'a'), Node(1, 1, 'a'), math.sqrt(2)),
    ],
)
def test_heigh_distance(node, other, expected):
    result = node.distance(other)
    assert result == expected


@pytest.mark.parametrize(
    'node, other, expected',
    [
        (Node(0, 0, 'a'), Node(0, 0, 'a'), 0),
        (Node(0, 0, 'a'), Node(0, 0, 'S'), 0),
        (Node(0, 0, 'S'), Node(0, 0, 'a'), 0),
        (Node(0, 0, 'z'), Node(0, 0, 'E'), 0),
        (Node(0, 0, 'E'), Node(0, 0, 'z'), 0),
        (Node(0, 0, 'a'), Node(0, 0, 'b'), 1),
        (Node(0, 0, 'b'), Node(0, 0, 'a'), -1),
    ],
)
def test_heigh_elevation(node, other, expected):
    result = node.elevation(other)
    assert result == expected


def test_heightmap_from_data():
    heightmap = Heightmap.from_data('ab\ncd\n')
    assert heightmap == Heightmap([
        [Node(0, 0, 'a'), Node(0, 1, 'b')],
        [Node(1, 0, 'c'), Node(1, 1, 'd')],
    ])


def test_heightmap_rows():
    heightmap = Heightmap.from_data('ab\ncd\n')
    assert heightmap.rows == [
        [Node(0, 0, 'a'), Node(0, 1, 'b')],
        [Node(1, 0, 'c'), Node(1, 1, 'd')],
    ]


def test_heightmap_start():
    node = Heightmap.from_data('Sb\ncE\n').start
    assert node == Node(0, 0, 'S')


def test_heightmap_end():
    node = Heightmap.from_data('Sb\ncE\n').end
    assert node == Node(1, 1, 'E')


@pytest.mark.parametrize(
    'height, expected',
    [
        ('b', [Node(0, 1, 'b')]),
        ('S', [Node(0, 0, 'S')]),
        ('a', []),
        ('e', []),
    ],
)
def test_heightmap_find(height, expected):
    print(Heightmap.from_data('Sb\ncE\n'))
    nodes = list(Heightmap.from_data('Sb\ncE\n').find(height))
    assert nodes == expected


@pytest.mark.parametrize(
    'node, expected',
    [
        (
            Node(0, 0, 'S'),
            [
                Node(0, 1, 'b'),
                Node(1, 0, 'b'),
            ],
        ),
        (
            Node(1, 1, 'a'),
            [
                Node(0, 1, 'b'),
                Node(1, 0, 'b'),
                Node(1, 2, 'b'),
                Node(2, 1, 'b'),
            ],
        ),
    ],
)
def test_heightmap_neighbours(node, expected):
    heightmap = Heightmap.from_data('Sba\nbab\nabE\n')
    neighbours = list(heightmap.neighbours(node))
    assert neighbours == expected


def test_part1():
    result = part1(DATA)
    assert result == 31


def test_part2():
    result = part2(DATA)
    assert result == 29


DATA = dedent("""\
    Sabqponm
    abcryxxl
    accszExk
    acctuvwj
    abdefghi
    """)
