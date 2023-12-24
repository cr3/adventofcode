'''Unit tests for year 2024, day 7.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day07 import (
    Hand,
    HandType,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'string, expected',
    [
        ('12345 0', Hand('12345', 0)),
        ('AKQJT 10', Hand('AKQJT', 10)),
    ],
)
def test_hand_from_string(string, expected):
    result = Hand.from_string(string)
    assert result == expected


@pytest.mark.parametrize(
    'cards, expected',
    [
        ('AAAAA', HandType.FIVE_OF_A_KIND),
        ('AA8AA', HandType.FOUR_OF_A_KIND),
        ('23332', HandType.FULL_HOUSE),
        ('TTT98', HandType.THREE_OF_A_KIND),
        ('23432', HandType.TWO_PAIRS),
        ('A23A4', HandType.ONE_PAIR),
        ('2345A', HandType.HIGH_CARD),
        ('A3456', HandType.HIGH_CARD),
        ('23456', HandType.HIGH_CARD),
    ],
)
def test_hand_type(cards, expected):
    result = Hand(cards).type_
    assert result == expected


@pytest.mark.parametrize(
    'cards, expected',
    [
        ('AAAAA', [6, 12, 12, 12, 12, 12]),
        ('23456', [0, 0, 1, 2, 3, 4]),
    ],
)
def test_hand_weight(cards, expected):
    result = Hand(cards).weight
    assert result == expected


@pytest.mark.parametrize(
    'a, b',
    [
        ('AAAAA', 'AA8AA'),
        ('AA8AA', 'AA7AA'),
        ('AA8AA', 'AA7AA'),
        ('23457', '23456'),
        ('KK677', 'KTJJT'),
    ],
)
def test_hand_gt(a, b):
    assert Hand(a) > Hand(b)


def test_part1():
    result = part1(dedent('''\
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
        '''))
    assert result == 6440


def test_part2():
    result = part2(dedent('''\
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
        '''))
    assert result == 0
