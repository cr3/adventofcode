"""Unit tests for day 2."""

import pytest

from adventofcode.day2 import (
    INPUT,
    Round,
    Shape,
    calculate1,
    calculate2,
    parse_input,
    parse_rounds,
    part1,
    part2,
)


def test_input():
    assert INPUT.exists()


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


def test_parse_input(tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('A Y\nB X\nC Z\n')
    rounds = list(parse_input(path))
    assert rounds == [
        Round(Shape.A, Shape.Y),
        Round(Shape.B, Shape.X),
        Round(Shape.C, Shape.Z),
    ]


def test_part1(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('A Y\nB X\nC Z\n')
    part1(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '15\n'


def test_part2(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('A Y\nB X\nC Z\n')
    part2(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '12\n'
