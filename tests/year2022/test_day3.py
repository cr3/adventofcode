"""Unit tests for year 2022, day 3."""

import pytest

from adventofcode.year2022.day3 import (
    Rucksack,
    parse_data1,
    parse_data2,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'line, expected',
    [
        ('ab', Rucksack(['a', 'b'])),
        ('abcd', Rucksack(['ab', 'cd'])),
    ],
)
def test_rucksack_parse(line, expected):
    assert Rucksack.parse(line) == expected


@pytest.mark.parametrize(
    'compartments, expected',
    [
        (['a', 'a'], 'a'),
        (['ab', 'ac'], 'a'),
        (['ab', 'ca'], 'a'),
        (['a', 'a', 'a'], 'a'),
        (['ab', 'ac', 'ad'], 'a'),
    ],
)
def test_rucksack_common(compartments, expected):
    assert Rucksack(compartments).common == expected


def test_rucksack_common_error():
    with pytest.raises(AssertionError):
        Rucksack(['ab', 'ab']).common


@pytest.mark.parametrize(
    'rucksack, expected',
    [
        (Rucksack(['p', 'p']), 16),
        (Rucksack(['L', 'L']), 38),
        (Rucksack(['P', 'P']), 42),
        (Rucksack(['v', 'v']), 22),
        (Rucksack(['t', 't']), 20),
        (Rucksack(['s', 's']), 19),
        (Rucksack(['r', 'r', 'r']), 18),
        (Rucksack(['Z', 'Z', 'Z']), 52),
    ],
)
def test_rucksack_priority(rucksack, expected):
    assert rucksack.priority == expected


def test_parse_data1():
    rounds = list(
        parse_data1(
            'vJrwpWtwJgWrhcsFMMfFFhFp\n'
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
            'PmmdzqPrVvPwwTWBwg\n'
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
            'ttgJtRGJQctTZtZT\n'
            'CrZsJsPPZsGzwwsLwLmpwMDw\n'
        )
    )
    assert rounds == [
        Rucksack(['vJrwpWtwJgWr', 'hcsFMMfFFhFp']),
        Rucksack(['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL']),
        Rucksack(['PmmdzqPrV', 'vPwwTWBwg']),
        Rucksack(['wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn']),
        Rucksack(['ttgJtRGJ', 'QctTZtZT']),
        Rucksack(['CrZsJsPPZsGz', 'wwsLwLmpwMDw']),
    ]


def test_parse_data2():
    rounds = list(
        parse_data2(
            'vJrwpWtwJgWrhcsFMMfFFhFp\n'
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
            'PmmdzqPrVvPwwTWBwg\n'
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
            'ttgJtRGJQctTZtZT\n'
            'CrZsJsPPZsGzwwsLwLmpwMDw\n'
        )
    )
    assert rounds == [
        Rucksack(
            [
                'vJrwpWtwJgWrhcsFMMfFFhFp',
                'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                'PmmdzqPrVvPwwTWBwg',
            ]
        ),
        Rucksack(
            [
                'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                'ttgJtRGJQctTZtZT',
                'CrZsJsPPZsGzwwsLwLmpwMDw',
            ]
        ),
    ]


def test_part1():
    result = part1(
        'vJrwpWtwJgWrhcsFMMfFFhFp\n'
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
        'PmmdzqPrVvPwwTWBwg\n'
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
        'ttgJtRGJQctTZtZT\n'
        'CrZsJsPPZsGzwwsLwLmpwMDw\n'
    )
    assert result == 157


def test_part2():
    result = part2(
        'vJrwpWtwJgWrhcsFMMfFFhFp\n'
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n'
        'PmmdzqPrVvPwwTWBwg\n'
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n'
        'ttgJtRGJQctTZtZT\n'
        'CrZsJsPPZsGzwwsLwLmpwMDw\n'
    )
    assert result == 70
