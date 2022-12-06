"""Unit tests for day 6."""

import pytest

from adventofcode.day6 import (
    INPUT,
    parse_text,
    part1,
    part2,
)


def test_input():
    assert INPUT.exists()


@pytest.mark.parametrize(
    'text, expected',
    [
        ('aabbccddeeffgghhiijjkkllmmnn', 0),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
    ],
)
def test_parse_marker(text, expected):
    assert parse_text(text, 4) == expected


@pytest.mark.parametrize(
    'text, expected',
    [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
    ],
)
def test_parse_message(text, expected):
    assert parse_text(text, 14) == expected


def test_part1(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n')
    part1(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '11\n'


def test_part2(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw\n')
    part2(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '26\n'
