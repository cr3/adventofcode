"""Unit tests for year 2022, day 13."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day13 import (
    compare,
    parse_data,
    parse_packet,
    parse_pair,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'left, right, expected',
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], -1),
        ([[1], [2, 3, 4]], [[1], 4], -1),
        ([9], [[8, 7, 6]], 1),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], -1),
        ([7, 7, 7, 7], [7, 7, 7], 1),
        ([], [3], -1),
        ([[[]]], [[]], 1),
        (
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            1,
        ),
    ],
)
def test_compare(left, right, expected):
    result = compare(left, right)
    assert result == expected


@pytest.mark.parametrize(
    'packet, expected',
    [
        ('[1,1,3,1,1]', [1, 1, 3, 1, 1]),
        ('[[1],[2,3,4]]', [[1], [2, 3, 4]]),
        ('[1,[2,[3,[4,[5,6,7]]]],8,9]', [1, [2, [3, [4, [5, 6, 7]]]], 8, 9]),
    ],
)
def test_parse_packet(packet, expected):
    result = parse_packet(packet)
    assert result == expected


def test_parse_pair():
    result = parse_pair(dedent("""\
        [1,1,3,1,1]
        [1,1,5,1,1]
        """))
    assert result == ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])


def test_parse_data():
    result = parse_data(DATA)
    assert len(list(result)) == 8


def test_part1():
    result = part1(DATA)
    assert result == 13


def test_part2():
    result = part2(DATA)
    assert result == 140


DATA = dedent("""\
    [1,1,3,1,1]
    [1,1,5,1,1]

    [[1],[2,3,4]]
    [[1],4]

    [9]
    [[8,7,6]]

    [[4,4],4,4]
    [[4,4],4,4,4]

    [7,7,7,7]
    [7,7,7]

    []
    [3]

    [[[]]]
    [[]]

    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    """)
