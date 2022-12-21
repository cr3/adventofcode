"""Unit tests for year 2022, day 18."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day18 import (
    Cube,
    Face,
    Position,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'position, expected',
    [
        (
            Position(1, 1, 1),
            {
                Position(0, 0, 0),
                Position(0, 0, 1),
                Position(0, 1, 0),
                Position(0, 1, 1),
                Position(1, 0, 0),
                Position(1, 0, 1),
                Position(1, 1, 0),
                Position(1, 1, 1),
            },
        ),
    ],
)
def test_cube_vertices(position, expected):
    result = set(Cube(position).vertices)
    assert len(result) == 8
    assert result == expected


@pytest.mark.parametrize(
    'position, expected',
    [
        (
            Position(1, 1, 1),
            {
                Face(
                    Position(0, 0, 0),
                    Position(0, 0, 1),
                    Position(0, 1, 0),
                    Position(0, 1, 1),
                ),
                Face(
                    Position(1, 0, 0),
                    Position(1, 0, 1),
                    Position(1, 1, 0),
                    Position(1, 1, 1),
                ),
                Face(
                    Position(0, 0, 0),
                    Position(0, 0, 1),
                    Position(1, 0, 0),
                    Position(1, 0, 1),
                ),
                Face(
                    Position(0, 1, 0),
                    Position(0, 1, 1),
                    Position(1, 1, 0),
                    Position(1, 1, 1),
                ),
                Face(
                    Position(0, 0, 0),
                    Position(0, 1, 0),
                    Position(1, 0, 0),
                    Position(1, 1, 0),
                ),
                Face(
                    Position(0, 0, 1),
                    Position(0, 1, 1),
                    Position(1, 0, 1),
                    Position(1, 1, 1),
                ),
            },
        ),
    ],
)
def test_cube_faces(position, expected):
    result = set(Cube(position).faces)
    assert len(result) == 6
    assert result == expected


def test_part1():
    result = part1(DATA)
    assert result == 64


def test_part2():
    result = part2(DATA)
    assert result == 0


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
