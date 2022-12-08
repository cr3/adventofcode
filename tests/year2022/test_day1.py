"""Unit tests for year 2022, day 1."""

from adventofcode.year2022.day1 import (
    group_lines,
    parse_data,
    part1,
    part2,
    sum_groups,
)


def test_group_lines():
    groups = list(group_lines(['1', '', '3']))
    assert groups == [['1'], ['3']]


def test_sum_groups():
    sums = list(sum_groups([['1', '2'], ['3', '4']]))
    assert sums == [3, 7]


def test_parse_data():
    sums = list(parse_data('1\n2\n\n3\n4\n'))
    assert sums == [3, 7]


def test_part1():
    result = part1('1\n2\n\n3\n4\n')
    assert result == 7


def test_part2():
    result = part2('1\n\n2\n\n3\n\n4')
    assert result == 9
