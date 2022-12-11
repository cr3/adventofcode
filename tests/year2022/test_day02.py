"""Unit tests for year 2022, day 2."""

import pytest

from adventofcode.year2022.day02 import (
    Round,
    Shape,
    calculate1,
    calculate2,
    parse_data,
    parse_rounds,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'shape, value',
    [
        (Shape.A, 1),
        (Shape.B, 2),
        (Shape.C, 3),
    ],
)
def test_shape_value(shape, value):
    assert shape == value


def test_round_parse():
    result = Round.parse('A Y')
    assert result == Round(Shape.A, Shape.Y)


@pytest.mark.parametrize(
    'shape, response, expected',
    [
        (Shape.A, Shape.X, 4),
        (Shape.B, Shape.X, 1),
        (Shape.C, Shape.X, 7),
        (Shape.A, Shape.Y, 8),
        (Shape.B, Shape.Y, 5),
        (Shape.C, Shape.Y, 2),
        (Shape.A, Shape.Z, 3),
        (Shape.B, Shape.Z, 9),
        (Shape.C, Shape.Z, 6),
    ],
)
def test_calculate1(shape, response, expected):
    assert calculate1(shape, response) == expected


@pytest.mark.parametrize(
    'shape, response, expected',
    [
        (Shape.A, Shape.Y, 4),
        (Shape.B, Shape.X, 1),
        (Shape.C, Shape.Z, 7),
    ],
)
def test_calculate2(shape, response, expected):
    assert calculate2(shape, response) == expected


def test_parse_rounds():
    rounds = list(parse_rounds(['A Y']))
    assert rounds == [Round(Shape.A, Shape.Y)]


def test_parse_data():
    rounds = list(parse_data('A Y\nB X\nC Z\n'))
    assert rounds == [
        Round(Shape.A, Shape.Y),
        Round(Shape.B, Shape.X),
        Round(Shape.C, Shape.Z),
    ]


def test_part1():
    result = part1('A Y\nB X\nC Z\n')
    assert result == 15


def test_part2():
    result = part2('A Y\nB X\nC Z\n')
    assert result == 12
