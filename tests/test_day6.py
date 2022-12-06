"""Unit tests for day 6."""

import pytest

from adventofcode.day6 import (
    parse_data,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'data, expected',
    [
        ('aabbccddeeffgghhiijjkkllmmnn', 0),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
    ],
)
def test_parse_marker(data, expected):
    assert parse_data(data, 4) == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
    ],
)
def test_parse_message(data, expected):
    assert parse_data(data, 14) == expected


def test_part1(capsys):
    part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n')
    captured = capsys.readouterr()
    result = captured.out
    assert result == '11\n'


def test_part2(capsys):
    part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n')
    captured = capsys.readouterr()
    result = captured.out
    assert result == '26\n'
