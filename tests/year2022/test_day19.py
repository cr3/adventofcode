"""Unit tests for year 2022, day 19."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day19 import (
    Blueprint,
    State,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'state, costs, expected',
    [
        (
            State(2, {}, {}),
            {'ore': {'ore': 1}},
            None,
        ),
        (
            State(3, {}, {'ore': 1}),
            {'ore': {'ore': 1}},
            State(3, {}, {'ore': 0}, building='ore'),
        ),
    ],
)
def test_state_buy(state, costs, expected):
    result = state.buy('ore', costs)
    assert result == expected


@pytest.mark.parametrize(
    'line, expected',
    [
        (
            dedent("""\
                Blueprint 1: \
                Each ore robot costs 4 ore. \
                Each clay robot costs 2 ore. \
                Each obsidian robot costs 3 ore and 14 clay. \
                Each geode robot costs 2 ore and 7 obsidian.
                """),
            Blueprint(
                1,
                {
                    'ore': {'ore': 4},
                    'clay': {'ore': 2},
                    'obsidian': {'ore': 3, 'clay': 14},
                    'geode': {'ore': 2, 'obsidian': 7},
                },
            ),
        ),
        (
            dedent("""\
                Blueprint 2: \
                Each ore robot costs 2 ore. \
                Each clay robot costs 3 ore. \
                Each obsidian robot costs 3 ore and 8 clay. \
                Each geode robot costs 3 ore and 12 obsidian. \
                """),
            Blueprint(
                2,
                {
                    'ore': {'ore': 2},
                    'clay': {'ore': 3},
                    'obsidian': {'ore': 3, 'clay': 8},
                    'geode': {'ore': 3, 'obsidian': 12},
                },
            ),
        ),
    ],
)
def test_blueprint_from_line(line, expected):
    result = Blueprint.from_line(line)
    assert result == expected


def test_part1():
    result = part1(DATA)
    assert result == 33


def test_part2():
    result = part2(DATA)
    assert result == 3472


DATA = dedent(
    """\
    Blueprint 1:\
     Each ore robot costs 4 ore.\
     Each clay robot costs 2 ore.\
     Each obsidian robot costs 3 ore and 14 clay.\
     Each geode robot costs 2 ore and 7 obsidian.\

    Blueprint 2:\
     Each ore robot costs 2 ore.\
     Each clay robot costs 3 ore.\
     Each obsidian robot costs 3 ore and 8 clay.\
     Each geode robot costs 3 ore and 12 obsidian.\

    """,
)
