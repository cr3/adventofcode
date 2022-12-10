"""Unit tests for year 2022, day 9."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day9 import (
    Direction,
    Move,
    Knot,
    Rope,
    follow_coordinate,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'line, expected',
    [
        ('U 4', Move(Direction.U, 4)),
        ('D 1', Move(Direction.D, 1)),
    ],
)
def test_move_from_line(line, expected):
    assert Move.from_line(line) == expected


@pytest.mark.parametrize(
    'move, expected',
    [
        (Move(Direction.U, 1), Rope(Knot(0, 1), Knot(0, 0))),
        (Move(Direction.D, 2), Rope(Knot(0, -2), Knot(0, -1))),
        (Move(Direction.R, 3), Rope(Knot(3, 0), Knot(2, 0))),
        (Move(Direction.L, 4), Rope(Knot(-4, 0), Knot(-3, 0))),
    ],
)
def test_move_apply(move, expected):
    rope = move.apply(Rope())
    assert Rope(rope.H, rope.T) == expected


@pytest.mark.parametrize(
    'H, T, expected',
    [
        (Knot(), Knot(1, 0), True),
        (Knot(), Knot(0, 1), True),
        (Knot(), Knot(1, 1), True),
        (Knot(), Knot(2, 0), False),
        (Knot(), Knot(0, 2), False),
        (Knot(), Knot(1, 2), False),
    ],
)
def test_knot_touching(H, T, expected):
    assert H.touching(T) is expected


@pytest.mark.parametrize(
    'knot, direction, expected',
    [
        (Knot(), Direction.U, Knot(0, 1)),
        (Knot(), Direction.D, Knot(0, -1)),
        (Knot(), Direction.R, Knot(1, 0)),
        (Knot(), Direction.L, Knot(-1, 0)),
    ],
)
def test_knot_move(knot, direction, expected):
    assert knot.move(direction) == expected


@pytest.mark.parametrize(
    'knot, other, expected',
    [
        (Knot(), Knot(1, 0), Knot(0, 0)),
        (Knot(), Knot(2, 0), Knot(1, 0)),
        (Knot(), Knot(2, 1), Knot(1, 1)),
    ],
)
def test_knot_follow(knot, other, expected):
    assert knot.follow(other) == expected


def test_rope_move():
    rope = Rope().move(Direction.U)
    assert rope == Rope(Knot(0, 1), Knot(), [Knot()])


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (0, 0, 0),
        (0, 1, 1),
        (1, 1, 1),
        (0, 2, 1),
        (1, 2, 2),
        (1, 0, 0),
        (2, 0, 1),
        (2, 1, 1),
    ],
)
def test_follow_coordinate(a, b, expected):
    assert follow_coordinate(a, b) == expected


def test_part1():
    result = part1(
        dedent(
            """\
            R 4
            U 4
            L 3
            D 1
            R 4
            D 1
            L 5
            R 2
            """
        )
    )
    assert result == 13


def test_part2():
    result = part2('')
    assert result == 0
