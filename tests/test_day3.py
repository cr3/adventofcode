"""Unit tests for day 3."""

import pytest

from adventofcode.day3 import (
    INPUT,
    Rucksack,
    parse_input,
    part1,
)


def test_input():
    assert INPUT.exists()


def test_rucksack_error():
    with pytest.raises(AssertionError):
        Rucksack('a', 'aa')


@pytest.mark.parametrize('line, expected', [
    ('ab', Rucksack('a', 'b')),
    ('abcd', Rucksack('ab', 'cd')),
])
def test_rucksack_parse(line, expected):
    assert Rucksack.parse(line) == expected


@pytest.mark.parametrize('left, right, expected', [
    ('a', 'a', 'a'),
    ('ab', 'ac', 'a'),
    ('ab', 'ca', 'a'),
])
def test_rucksack_common(left, right, expected):
    assert Rucksack(left, right).common == expected


def test_rucksack_common_error():
    with pytest.raises(AssertionError):
        Rucksack('ab', 'ab').common


@pytest.mark.parametrize('rucksack, expected', [
    (Rucksack('p', 'p'), 16),
    (Rucksack('L', 'L'), 38),
    (Rucksack('P', 'P'), 42),
    (Rucksack('v', 'v'), 22),
    (Rucksack('t', 't'), 20),
    (Rucksack('s', 's'), 19),
])
def test_rucksack_priority(rucksack, expected):
    assert rucksack.priority == expected


def test_parse_input(tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text(
        'vJrwpWtwJgWrhcsFMMfFFhFp\n'
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
        'PmmdzqPrVvPwwTWBwg\n'
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
        'ttgJtRGJQctTZtZT\n'
        'CrZsJsPPZsGzwwsLwLmpwMDw\n'
    )
    rounds = list(parse_input(path))
    assert rounds == [
        Rucksack('vJrwpWtwJgWr', 'hcsFMMfFFhFp'),
        Rucksack('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'),
        Rucksack('PmmdzqPrV', 'vPwwTWBwg'),
        Rucksack('wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'),
        Rucksack('ttgJtRGJ', 'QctTZtZT'),
        Rucksack('CrZsJsPPZsGz', 'wwsLwLmpwMDw'),
    ]


def test_part1(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text(
        'vJrwpWtwJgWrhcsFMMfFFhFp\n'
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
        'PmmdzqPrVvPwwTWBwg\n'
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
        'ttgJtRGJQctTZtZT\n'
        'CrZsJsPPZsGzwwsLwLmpwMDw\n'
    )
    part1(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '157\n'
