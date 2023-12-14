'''Unit tests for year 2023, day 3.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day03 import (
    Engine,
    Number,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'number, x, y, expected',
    [
        (Number(0, 1, 2, 0), 0, 0, False),
        (Number(0, 1, 2, 0), 1, 0, True),
        (Number(0, 1, 2, 0), 2, 0, True),
        (Number(0, 1, 2, 0), 3, 0, False),
    ],
)
def test_number_is_within(number, x, y, expected):
    result = number.is_within(x, y)
    assert result == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ('123...', [Number(123, 0, 2, 0)]),
        ('...123', [Number(123, 3, 5, 0)]),
        ('......\n...123\n', [Number(123, 3, 5, 1)]),
    ],
)
def test_engine_find_numbers(data, expected):
    engine = Engine.from_data(data)
    result = list(engine.find_numbers())
    assert result == expected


@pytest.mark.parametrize(
    'data, number, expected',
    [
        ('123...', Number(123, 0, 2, 0), False),
        ('123...\n......', Number(123, 0, 2, 0), False),
        ('123...\n*.....', Number(123, 0, 2, 0), True),
        ('123...\n.*.....', Number(123, 0, 2, 0), True),
        ('123...\n..*....', Number(123, 0, 2, 0), True),
        ('123...\n...*...', Number(123, 0, 2, 0), True),
        ('123...\n....*..', Number(123, 0, 2, 0), False),
    ],
)
def test_engine_is_part_number(data, number, expected):
    engine = Engine.from_data(data)
    result = engine.is_part_number(number)
    assert result == expected


def test_part1():
    result = part1(dedent('''\
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        '''))
    assert result == 4361


def test_part2():
    result = part2(dedent('''\
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        '''))
    assert result == 467835
