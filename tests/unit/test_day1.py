"""Unit tests for day 1."""

from io import StringIO

from adventofcode.day1 import (
    INPUT,
    group_lines,
    main,
    parse_input,
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
    result = parse_input(path)
    assert result == 7


def test_main(capsys):
    main([])
    captured = capsys.readouterr()
    result = captured.out
    assert result.strip().isdigit()
