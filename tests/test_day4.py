"""Unit tests for day 4."""

import pytest

from adventofcode.day4 import (
    INPUT,
    Pair,
    Range,
    parse_input,
    part1,
    part2,
)


def test_input():
    assert INPUT.exists()


def test_range_error():
    with pytest.raises(AssertionError):
        Range(1, 0)


@pytest.mark.parametrize(
    'part, expected',
    [
        ('0-0', Range(0, 0)),
        ('1-10', Range(1, 10)),
    ],
)
def test_range_parse(part, expected):
    assert Range.parse(part) == expected


@pytest.mark.parametrize(
    'part',
    [
        '',
        '0',
    ],
)
def test_range_parse_error(part):
    with pytest.raises(AssertionError):
        Range.parse(part)


@pytest.mark.parametrize(
    'left, right, expected',
    [
        (Range(2, 4), Range(6, 8), False),
        (Range(2, 3), Range(4, 5), False),
        (Range(5, 7), Range(7, 9), False),
        (Range(2, 8), Range(3, 7), True),
        (Range(6, 6), Range(4, 6), False),
        (Range(2, 6), Range(4, 8), False),
    ],
)
def test_range_contains(left, right, expected):
    assert left.contains(right) is expected


@pytest.mark.parametrize(
    'left, right, expected',
    [
        (Range(2, 4), Range(6, 8), False),
        (Range(2, 3), Range(4, 5), False),
        (Range(5, 7), Range(7, 9), True),
        (Range(2, 8), Range(3, 7), True),
        (Range(6, 6), Range(4, 6), True),
        (Range(2, 6), Range(4, 8), True),
        (Range(0, 0), Range(1, 1), False),
        (Range(0, 1), Range(1, 1), True),
        (Range(0, 0), Range(0, 1), True),
        (Range(1, 1), Range(0, 2), True),
        (Range(0, 2), Range(1, 1), True),
    ],
)
def test_range_overlaps(left, right, expected):
    assert left.overlaps(right) is expected


def test_pair_parse():
    assert Pair.parse('0-0,1-2') == Pair(Range(0, 0), Range(1, 2))


@pytest.mark.parametrize(
    'line, expected',
    [
        ('2-4,6-8', False),
        ('2-3,4-5', False),
        ('5-7,7-9', False),
        ('2-8,3-7', True),
        ('6-6,4-6', True),
        ('2-6,4-8', False),
    ],
)
def test_pair_has_contains(line, expected):
    assert Pair.parse(line).has_contains is expected


@pytest.mark.parametrize(
    'line, expected',
    [
        ('2-4,6-8', False),
        ('2-3,4-5', False),
        ('5-7,7-9', True),
        ('2-8,3-7', True),
        ('6-6,4-6', True),
        ('2-6,4-8', True),
    ],
)
def test_pair_has_overlap(line, expected):
    assert Pair.parse(line).has_overlap is expected


def test_parse_input(tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8\n')
    pairs = list(parse_input(path))
    assert pairs == [
        Pair(Range(2, 4), Range(6, 8)),
        Pair(Range(2, 3), Range(4, 5)),
        Pair(Range(5, 7), Range(7, 9)),
        Pair(Range(2, 8), Range(3, 7)),
        Pair(Range(6, 6), Range(4, 6)),
        Pair(Range(2, 6), Range(4, 8)),
    ]


def test_part1(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8\n')
    part1(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '2\n'


def test_part2(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8\n')
    part2(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '4\n'
