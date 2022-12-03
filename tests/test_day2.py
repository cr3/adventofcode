"""Unit tests for day 2."""

import pytest

from adventofcode.day2 import (
    INPUT,
    Response,
    Round,
    Shape,
    parse_input,
    parse_rounds,
    part1,
)


def test_input():
    assert INPUT.exists()


@pytest.mark.parametrize('shape, score', [
    (Shape.A, 1),
    (Shape.B, 2),
    (Shape.C, 3),
])
def test_shape_score(shape, score):
    assert shape == score


@pytest.mark.parametrize('response, shape', [
    (Response.X, Shape.A),
    (Response.Y, Shape.B),
    (Response.Z, Shape.C),
])
def test_response_shape(response, shape):
    assert response.shape == shape


@pytest.mark.parametrize('response, shape, expected', [
    (Response.X, Shape.A, False),
    (Response.X, Shape.B, False),
    (Response.X, Shape.C, True),
    (Response.Y, Shape.A, True),
    (Response.Y, Shape.B, False),
    (Response.Y, Shape.C, False),
    (Response.Z, Shape.A, False),
    (Response.Z, Shape.B, True),
    (Response.Z, Shape.C, False),
])
def test_response_defeats(response, shape, expected):
    assert response.defeats(shape) is expected


@pytest.mark.parametrize('response, shape, expected', [
    (Response.X, Shape.A, 3),
    (Response.X, Shape.B, 0),
    (Response.X, Shape.C, 6),
    (Response.Y, Shape.A, 6),
    (Response.Y, Shape.B, 3),
    (Response.Y, Shape.C, 0),
    (Response.Z, Shape.A, 0),
    (Response.Z, Shape.B, 6),
    (Response.Z, Shape.C, 3),
])
def test_response_outcome(response, shape, expected):
    assert response.outcome(shape) == expected


def test_round_parse():
    result = Round.parse('A Y')
    assert result == Round(Shape.A, Response.Y)


@pytest.mark.parametrize('shape, response, score', [
    (Shape.A, Response.Y, 8),
    (Shape.B, Response.X, 1),
    (Shape.C, Response.Z, 6),
])
def test_round_score(shape, response, score):
    result = Round(shape, response)
    assert result.score == score


def test_parse_rounds():
    rounds = list(parse_rounds(['A Y']))
    assert rounds == [Round(Shape.A, Response.Y)]


def test_parse_input(tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('A Y\nB X\nC Z\n')
    sums = list(parse_input(path))
    assert sums == [8, 1, 6]


def test_part1(capsys, tmp_path):
    path = tmp_path / 'input.txt'
    path.write_text('A Y\nB X\nC Z\n')
    part1(path)
    captured = capsys.readouterr()
    result = captured.out
    assert result == '15\n'
