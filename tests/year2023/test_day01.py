'''Unit tests for year 2023, day 1.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day01 import (
    parse_alphanumeric,
    parse_data,
    parse_digit,
    parse_numeric,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'digit, expected',
    [
        ('1', 1),
        ('2', 2),
        ('one', 1),
        ('two', 2),
        ('three', 3),
        ('four', 4),
        ('five', 5),
        ('six', 6),
        ('seven', 7),
        ('eight', 8),
        ('nine', 9),
    ],
)
def test_parse_digit(digit, expected):
    num = parse_digit(digit)
    assert num == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        ('one', 11),
        ('1two', 12),
        ('one2', 12),
        ('onetwo', 12),
        ('12three', 13),
        ('1twothree', 13),
        ('onetwothree', 13),
        ('onetwo3', 13),
        ('one2three', 13),
        ('one23', 13),
    ],
)
def test_parse_alphanumeric(line, expected):
    num = parse_alphanumeric(line)
    assert num == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        ('1', 11),
        ('12', 12),
        ('1b2', 12),
        ('a12', 12),
        ('12c', 12),
        ('a1b2c', 12),
        ('a1b2c3d', 13),
    ],
)
def test_parse_numeric(line, expected):
    num = parse_numeric(line)
    assert num == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ('\n', 1),
        ('\n\n', 2),
    ],
)
def test_parse_data(data, expected):
    total = parse_data(data, lambda _: 1)
    assert total == expected


def test_part1():
    result = part1(dedent('''\
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        '''))
    assert result == 142


def test_part2():
    result = part2(dedent('''\
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        '''))
    assert result == 281
