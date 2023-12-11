"""Unit tests for year 2022, day 17."""

import pytest

from adventofcode.year2022.day17 import (
    Cave,
    Jet,
    parse_jets,
    parse_rocks,
    part1,
    part2,
    push_rock,
)


@pytest.mark.parametrize(
    'cave, rock, rows',
    [
        (
            Cave([]),
            ['###'],
            [
                '.......',
                '.......',
                '.......',
                '..@@@..',
            ],
        ),
        (
            Cave([]),
            [
                '..#',
                '..#',
                '###',
            ],
            [
                '.......',
                '.......',
                '.......',
                '..@@@..',
                '....@..',
                '....@..',
            ],
        ),
    ],
)
def test_cave_add(cave, rock, rows):
    cave.add(rock)
    assert cave.rows == rows


@pytest.mark.parametrize(
    'cave, jet, rows, expected',
    [
        (
            Cave([
                '..@@@..',
            ]),
            Jet.L,
            [
                '.@@@...',
            ],
            True,
        ),
        (
            Cave(
                [
                    '..###..',
                    '..@@@..',
                ],
            ),
            Jet.R,
            [
                '..###..',
                '...@@@.',
            ],
            True,
        ),
    ],
)
def test_cave_push(cave, jet, rows, expected):
    assert cave.push(jet) == expected
    assert cave.rows == rows


@pytest.mark.parametrize(
    'cave, rows, expected',
    [
        (
            Cave([
                '.......',
                '..@@@..',
            ]),
            [
                '..@@@..',
            ],
            True,
        ),
        (
            Cave([
                '##...##',
                '..@@@..',
            ]),
            [
                '##@@@##',
            ],
            True,
        ),
        (
            Cave([
                '..#....',
                '..@@@..',
            ]),
            [
                '..#....',
                '..###..',
            ],
            False,
        ),
    ],
)
def test_cave_fall(cave, rows, expected):
    assert cave.fall() == expected
    assert cave.rows == rows


@pytest.mark.parametrize(
    'rows, jet, expected',
    [
        (
            [
                '..@@@..',
            ],
            Jet.R,
            [
                '...@@@.',
            ],
        ),
        (
            [
                '....@@@',
            ],
            Jet.R,
            [
                '....@@@',
            ],
        ),
        (
            [
                '..@@@#.',
            ],
            Jet.R,
            [
                '..@@@#.',
            ],
        ),
        (
            [
                '..@@@..',
            ],
            Jet.L,
            [
                '.@@@...',
            ],
        ),
        (
            [
                '@@@....',
            ],
            Jet.L,
            [
                '@@@....',
            ],
        ),
        (
            [
                '.#@@@..',
            ],
            Jet.L,
            [
                '.#@@@..',
            ],
        ),
    ],
)
def test_push_rock(rows, jet, expected):
    push_rock(rows, jet)
    assert rows == expected


def test_parse_rocks():
    rocks = parse_rocks()
    assert next(rocks) == ['####']


def test_parse_jets():
    jets = parse_jets('><')
    assert next(jets) == Jet.R
    assert next(jets) == Jet.L
    assert next(jets) == Jet.R


def test_part1():
    result = part1(DATA, 100)
    assert result == 3068


def test_part2():
    result = part2(DATA, 100)
    assert result == 1_514_285_714_288


DATA = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
