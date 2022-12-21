"""Unit tests for year 2022, day 18."""

from textwrap import dedent

from adventofcode.year2022.day18 import (
    part1,
    part2,
)


def test_part1():
    result = part1(DATA)
    assert result == 64


def test_part2():
    result = part2(DATA)
    assert result == 58


DATA = dedent(
    """\
    2,2,2
    1,2,2
    3,2,2
    2,1,2
    2,3,2
    2,2,1
    2,2,3
    2,2,4
    2,2,6
    1,2,5
    3,2,5
    2,1,5
    2,3,5
    """,
)
