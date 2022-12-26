"""Unit tests for year 2022, day 22."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day22 import (
    Board,
    Cursor,
    Facing,
    Motion,
    parse_line,
    parse_data,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'cursor, motion, expected',
    [
        (
            Cursor(facing=Facing.R),
            Motion.R,
            Cursor(facing=Facing.D),
        ),
        (
            Cursor(facing=Facing.D),
            Motion.R,
            Cursor(facing=Facing.L),
        ),
        (
            Cursor(facing=Facing.L),
            Motion.R,
            Cursor(facing=Facing.U),
        ),
        (
            Cursor(facing=Facing.U),
            Motion.R,
            Cursor(facing=Facing.R),
        ),
        (
            Cursor(facing=Facing.R),
            Motion.L,
            Cursor(facing=Facing.U),
        ),
        (
            Cursor(facing=Facing.U),
            Motion.L,
            Cursor(facing=Facing.L),
        ),
        (
            Cursor(facing=Facing.L),
            Motion.L,
            Cursor(facing=Facing.D),
        ),
        (
            Cursor(facing=Facing.D),
            Motion.L,
            Cursor(facing=Facing.R),
        ),
    ],
)
def test_cursor_rotate(cursor, motion, expected):
    result = cursor.rotate(motion)
    assert result == expected


@pytest.mark.parametrize(
    'cursor, expected',
    [
        (Cursor(facing=Facing.R), Cursor(1, 0, Facing.R)),
        (Cursor(facing=Facing.D), Cursor(0, 1, Facing.D)),
        (Cursor(facing=Facing.L), Cursor(-1, 0, Facing.L)),
        (Cursor(facing=Facing.U), Cursor(0, -1, Facing.U)),
    ],
)
def test_cursor_move(cursor, expected):
    result = cursor.move()
    assert result == expected


@pytest.mark.parametrize(
    'cursor, height, width, expected',
    [
        (Cursor(3, 0), 2, 2, Cursor(1, 0)),
        (Cursor(0, 3), 2, 2, Cursor(0, 1)),
        (Cursor(-1, 0), 2, 2, Cursor(1, 0)),
        (Cursor(0, -1), 2, 2, Cursor(0, 1)),
    ],
)
def test_cursor_mod(cursor, height, width, expected):
    result = cursor.mod(height, width)
    assert result == expected


@pytest.mark.parametrize(
    'block, expected',
    [
        ('.\n..', Board(['. ', '..'])),
    ],
)
def test_board_from_block(block, expected):
    result = Board.from_block(block)
    assert result == expected


@pytest.mark.parametrize(
    'board, expected',
    [
        (Board(['.']), Cursor(0, 0, Facing.R)),
        (Board([' .']), Cursor(1, 0, Facing.R)),
    ],
)
def test_board_begin(board, expected):
    result = board.begin()
    assert result == expected


@pytest.mark.parametrize(
    'board, cursor, expected',
    [
        (Board(['.']), Cursor(), '.'),
        (Board([' .']), Cursor(1), '.'),
        (Board(['', '.']), Cursor(y=1), '.'),
        (Board(['', ' .']), Cursor(x=1, y=1), '.'),
    ],
)
def test_board_at(board, cursor, expected):
    result = board.at(cursor)
    assert result == expected


@pytest.mark.parametrize(
    'board, cursor, move, expected',
    [
        (Board(['...']), Cursor(x=0), 1, Cursor(x=1)),
        (Board(['...']), Cursor(x=0), 2, Cursor(x=2)),
        (Board(['...']), Cursor(x=0), 3, Cursor(x=0)),
        (Board(['#..']), Cursor(x=1), 3, Cursor(x=2)),
        (Board(['.#.']), Cursor(x=2), 3, Cursor(x=0)),
        (Board(['  ...  ']), Cursor(x=2), 1, Cursor(x=3)),
        (Board(['  ...  ']), Cursor(x=2), 2, Cursor(x=4)),
        (Board(['  ...  ']), Cursor(x=2), 3, Cursor(x=2)),
        (Board(['  #..  ']), Cursor(x=3), 3, Cursor(x=4)),
        (Board(['  .#.  ']), Cursor(x=4), 3, Cursor(x=2)),
        (
            Board([' ', ' ', '.', '.', '.', ' ', ' ']),
            Cursor(y=2, facing=Facing.D),
            1,
            Cursor(y=3, facing=Facing.D),
        ),
        (
            Board([' ', ' ', '.', '.', '.', ' ', ' ']),
            Cursor(y=2, facing=Facing.D),
            2,
            Cursor(y=4, facing=Facing.D),
        ),
        (
            Board([' ', ' ', '.', '.', '.', ' ', ' ']),
            Cursor(y=2, facing=Facing.D),
            3,
            Cursor(y=2, facing=Facing.D),
        ),
    ],
)
def test_board_move(board, cursor, move, expected):
    result = board.move(cursor, move)
    assert result == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        ('R10', [Motion.R, 10]),
        ('10R', [10, Motion.R]),
        ('10R5', [10, Motion.R, 5]),
        ('10RL5', [10, Motion.R, Motion.L, 5]),
    ],
)
def test_parse_line(line, expected):
    result = parse_line(line)
    assert result == expected


def test_parse_data():
    board, moves = parse_data(DATA)
    assert board.height == 12
    assert board.width == 16
    assert len(moves) == 13


def test_part1():
    result = part1(DATA)
    assert result == 6032


def test_part2():
    result = part2(DATA)
    assert result == 0


DATA = dedent(
    """\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
    """,
)
