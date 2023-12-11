"""Unit tests for year 2023, day 1."""

from textwrap import dedent

import pytest
from adventofcode.year2023.day01 import (
    parse_line,
    parse_data,
    part1,
)


@pytest.mark.parametrize("line, expected", [
    ("12", 12),
    ("1b2", 12),
    ("a12", 12),
    ("12c", 12),
    ("a1b2c", 12),
    ("a1b2c3d", 13),
])
def test_parse_line(line, expected):
    num = parse_line(line)
    assert num == expected


@pytest.mark.parametrize("data, expected", [
    ("11\n", 11),
    ("11\n22\n", 33),
    ("11\n22\n33\n", 66),
])
def test_parse_data(data, expected):
    total = parse_data(data)
    assert total == expected


def test_part1():
    result = part1(dedent('''\
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        '''))
    assert result == 142
