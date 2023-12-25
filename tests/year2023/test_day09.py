'''Unit tests for year 2024, day 9.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day09 import (
    History,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'string, expected',
    [
        ('1', History([1])),
        ('1 2', History([1, 2])),
        ('1 2 3', History([1, 2, 3])),
    ],
)
def test_history_from_string(string, expected):
    result = History.from_string(string)
    assert result == expected


@pytest.mark.parametrize(
    'history, expected',
    [
        (History([]), History()),
        (History([1]), History()),
        (History([1, 1]), History([0])),
        (History([1, 2]), History([1])),
        (History([1, 2, 3]), History([1, 1])),
        (History([0, 3, 6]), History([3, 3])),
    ],
)
def test_history_diffs(history, expected):
    result = history.diffs()
    assert result == expected


@pytest.mark.parametrize(
    'history, expected',
    [
        (History([]), True),
        (History([0]), True),
        (History([0, 0]), True),
        (History([1]), False),
        (History([1, 0]), False),
        (History([0, 1]), False),
    ],
)
def test_history_is_zero(history, expected):
    result = history.is_zero()
    assert result == expected


@pytest.mark.parametrize(
    'history, expected',
    [
        (History([0, 3, 6, 9, 12, 15]), 18),
        (History([1, 3, 6, 10, 15, 21]), 28),
        (History([10, 13, 16, 21, 30, 45]), 68),
    ],
)
def test_history_forward(history, expected):
    result = history.forward()
    assert result == expected


def test_part1():
    result = part1(dedent('''\
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
        '''))
    assert result == 114


def test_part2():
    result = part2(dedent('''\
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
        '''))
    assert result == 2
