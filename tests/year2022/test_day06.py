"""Unit tests for year 2022, day 6."""

import pytest

from adventofcode.year2022.day06 import (
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


def test_part1():
    result = part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n')
    assert result == 11


def test_part2():
    result = part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n')
    assert result == 26
