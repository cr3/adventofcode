'''Unit tests for year 2023, day 4.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day04 import (
    Card,
    Numbers,
    part1,
    part2,
)


@pytest.mark.parametrize('string, expected', [
    ('', Numbers(set())),
    ('1', Numbers({1})),
    ('1 2', Numbers({1, 2})),
    ('1 2 3', Numbers({1, 2, 3})),
])
def test_numbers_from_string(string, expected):
    result = Numbers.from_string(string)
    assert result == expected


@pytest.mark.parametrize('string, expected', [
    ('Card 1: 2 | 3', Card(1, Numbers({2}), Numbers({3}))),
    ('Card 1: 20 | 300', Card(1, Numbers({20}), Numbers({300}))),
    ('Card 1: 2 3 | 3 4', Card(1, Numbers({2, 3}), Numbers({3, 4}))),
])
def test_card_from_string(string, expected):
    result = Card.from_string(string)
    assert result == expected


@pytest.mark.parametrize('string', [
    "",
    "Card: 2 | 3",
    "Card 1: 2",
    "Card 1: | 3",
])
def test_card_from_string_error(string):
    with pytest.raises(ValueError):
        Card.from_string(string)


@pytest.mark.parametrize('card, expected', [
    (Card(1, set(), set()), set()),
    (Card(1, {1}, {2}), set()),
    (Card(1, {1}, {1}), {1}),
    (Card(1, {1, 2}, {1}), {1}),
    (Card(1, {1, 2}, {2}), {2}),
    (Card(1, {1, 2}, {1, 2}), {1, 2}),
])
def test_card_matches(card, expected):
    result = card.matches()
    assert result == expected


@pytest.mark.parametrize('card, expected', [
    (Card(1, {1}, {}), 0),
    (Card(1, {1}, {1}), 1),
    (Card(1, {1, 2}, {1, 2}), 2),
    (Card(1, {1, 2, 3}, {1, 2, 3}), 4),
])
def test_card_points(card, expected):
    result = card.points()
    assert result == expected


def test_part1():
    result = part1(dedent('''\
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        '''))
    assert result == 13


def test_part2():
    result = part2(dedent('''\
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        '''))
    assert result == 0
