"""Unit tests for day 1."""

from io import StringIO

from adventofcode.day1 import (
    INPUT,
    group_lines,
    parse_input,
    part1,
    part2,
    split_lines,
    sum_groups,
)


def test_input():
    assert INPUT.exists()


def test_split_lines():
    lines = list(split_lines(StringIO('1\n\n3\n')))
    assert lines == ['1', '', '3']


def test_group_lines():
    groups = list(group_lines(['1', '', '3']))
    assert groups == [['1'], ['3']]


def test_sum_groups():
    sums = list(sum_groups([['1', '2'], ['3', '4']]))
    assert sums == [3, 7]


def test_parse_input(tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('1\n2\n\n3\n4\n')
    sums = list(parse_input(path))
    assert sums == [3, 7]


def test_part1(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('1\n2\n\n3\n4\n')
    part1(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '7\n'


def test_part2(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('1\n\n2\n\n3\n\n4')
    part2(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '9\n'
