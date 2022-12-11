"""Unit tests for year 2022, day 5."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day05 import (
    Stacks,
    Move,
    parse_data,
    part1,
    part2,
)


def test_move_parse():
    move = Move.parse('move 1 from 2 to 1')
    assert move == Move(1, 2, 1)


def test_stacks_parse():
    stacks = Stacks.parse(
        dedent(
            """
        [V]     [B]                     [C]
        [C]     [N] [G]         [W]     [P]
        [W]     [C] [Q] [S]     [C]     [M]
        [L]     [W] [B] [Z]     [F] [S] [V]
        [R]     [G] [H] [F] [P] [V] [M] [T]
        [M] [L] [R] [D] [L] [N] [P] [D] [W]
        [F] [Q] [S] [C] [G] [G] [Z] [P] [N]
        [Q] [D] [P] [L] [V] [D] [D] [C] [Z]
        1   2   3   4   5   6   7   8   9
    """
        )
    )
    assert stacks == Stacks(
        [
            ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
            ['D', 'Q', 'L'],
            ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
            ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
            ['V', 'G', 'L', 'F', 'Z', 'S'],
            ['D', 'G', 'N', 'P'],
            ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
            ['C', 'P', 'D', 'M', 'S'],
            ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C'],
        ]
    )


def test_stacks_getitem():
    stacks = Stacks([['a']])
    assert stacks[1] == ['a']


@pytest.mark.parametrize(
    'stacks, expected',
    [
        (Stacks([]), 0),
        (Stacks([['a']]), 1),
        (Stacks([['a'], ['b']]), 2),
    ],
)
def test_stacks_len(stacks, expected):
    assert len(stacks) == expected


@pytest.mark.parametrize(
    'stacks, expected',
    [
        (Stacks([]), []),
        (Stacks([['a']]), [1]),
        (Stacks([['a'], ['b']]), [1, 2]),
    ],
)
def test_stacks_keys(stacks, expected):
    assert list(stacks.keys()) == expected


def test_stacks_rearrange():
    stacks = Stacks([['a', 'b'], []])
    stacks.rearrange(Move(2, 1, 2))
    assert stacks == Stacks([[], ['b', 'a']])


def test_stacks_rearrange_multiple():
    stacks = Stacks([['a', 'b'], []])
    stacks.rearrange_multiple(Move(2, 1, 2))
    assert stacks == Stacks([[], ['a', 'b']])


def test_parse_data():
    stacks, moves = parse_data(
        dedent(
            """\
            [D]
        [N] [C]
        [Z] [M] [P]
        1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
    """
        )
    )
    assert stacks == Stacks([['Z', 'N'], ['M', 'C', 'D'], ['P']])
    assert list(moves) == [
        Move(1, 2, 1),
        Move(3, 1, 3),
        Move(2, 2, 1),
        Move(1, 1, 2),
    ]


def test_part1():
    result = part1(
        dedent(
            """\
            [D]
        [N] [C]
        [Z] [M] [P]
        1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
    """
        )
    )
    assert result == 'CMZ'


def test_part2():
    result = part2(
        dedent(
            """\
            [D]
        [N] [C]
        [Z] [M] [P]
        1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
    """
        )
    )
    assert result == 'MCD'
