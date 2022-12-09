"""Unit tests for year 2023, day 8."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day8 import (
    sum_views,
    view_left,
    view_right,
    view_row,
    view_rows,
    view_cols,
    view_matrix,
    parse_data,
    parse_line,
    part1,
    part2,
)


def test_sum_views():
    assert sum_views([True, False], [False, True]) == [True, True]


@pytest.mark.parametrize(
    'line, visibility',
    [
        ('30373', [True, False, False, True, False]),
        ('25512', [True, True, False, False, False]),
        ('65332', [True, False, False, False, False]),
        ('33549', [True, False, True, False, True]),
        ('35390', [True, True, False, True, False]),
    ],
)
def test_view_left(line, visibility):
    row = parse_line(line)
    assert view_left(row) == visibility


@pytest.mark.parametrize(
    'line, visibility',
    [
        ('30373', [False, False, False, True, True]),
        ('25512', [False, False, True, False, True]),
        ('65332', [True, True, False, True, True]),
        ('33549', [False, False, False, False, True]),
        ('35390', [False, False, False, True, True]),
    ],
)
def test_view_right(line, visibility):
    row = parse_line(line)
    assert view_right(row) == visibility


@pytest.mark.parametrize(
    'line, visibility',
    [
        ('30373', [True, False, False, True, True]),
        ('25512', [True, True, True, False, True]),
        ('65332', [True, True, False, True, True]),
        ('33549', [True, False, True, False, True]),
        ('35390', [True, True, False, True, True]),
    ],
)
def test_view_row(line, visibility):
    row = parse_line(line)
    assert view_row(row) == visibility


def test_view_rows():
    matrix = parse_data(
        dedent(
            """\
        30373
        25512
        65332
        33549
        35390
    """
        )
    )
    assert view_rows(matrix) == [
        [True, False, False, True, True],
        [True, True, True, False, True],
        [True, True, False, True, True],
        [True, False, True, False, True],
        [True, True, False, True, True],
    ]


def test_view_cols():
    matrix = parse_data(
        dedent(
            """\
        30373
        25512
        65332
        33549
        35390
    """
        )
    )
    assert view_cols(matrix) == [
        [True, True, True, True, True],
        [False, True, True, False, False],
        [True, False, False, False, False],
        [False, False, True, False, True],
        [True, True, True, True, True],
    ]


def test_view_matrix():
    matrix = parse_data(
        dedent(
            """\
        30373
        25512
        65332
        33549
        35390
    """
        )
    )
    assert view_matrix(matrix) == [
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, False, True, True],
        [True, False, True, False, True],
        [True, True, True, True, True],
    ]


def test_part1():
    result = part1(
        dedent(
            """\
        30373
        25512
        65332
        33549
        35390
    """
        )
    )
    assert result == 21


def test_part2():
    assert part2('') == 0
