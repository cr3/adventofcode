"""Unit tests for year 2022, day 16."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day16 import (
    Graph,
    Valve,
    parse_data,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'line, expected',
    [
        (
            'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
            Valve('AA', 0, ['DD', 'II', 'BB']),
        ),
        (
            'Valve JJ has flow rate=21; tunnel leads to valve II',
            Valve('JJ', 21, ['II']),
        ),
    ],
)
def test_valve_from_line(line, expected):
    result = Valve.from_line(line)
    assert result == expected


@pytest.mark.parametrize(
    'valves, steps',
    [
        (
            [
                Valve('AA', 0, ['BB']),
                Valve('BB', 1, ['AA']),
            ],
            {
                ('AA', 'BB'): 1,
                ('BB', 'AA'): 1,
            },
        ),
        (
            [
                Valve('AA', 0, ['BB']),
                Valve('BB', 1, ['CC']),
                Valve('CC', 2, ['AA']),
            ],
            {
                ('AA', 'BB'): 1,
                ('AA', 'CC'): 2,
                ('BB', 'AA'): 2,
                ('BB', 'CC'): 1,
                ('CC', 'AA'): 1,
                ('CC', 'BB'): 2,
            },
        ),
    ],
)
def test_graph_steps(valves, steps):
    graph = Graph.from_valves(valves)
    assert graph.steps == steps


@pytest.mark.parametrize(
    'valves, answer',
    [
        (
            [
                Valve('AA', 0, ['BB']),
                Valve('BB', 1, ['AA']),
            ],
            {
                0: 0,
                2: 28,
            },
        ),
        (
            [
                Valve('AA', 0, ['BB']),
                Valve('BB', 1, ['CC']),
                Valve('CC', 2, ['AA']),
            ],
            {
                0: 0,
                2: 28,
                4: 54,
                6: 80,
            },
        ),
    ],
)
def test_graph_travel(valves, answer):
    graph = Graph.from_valves(valves)
    assert graph.travel('AA', 30, 0, 0, {}) == answer


def test_parse_data():
    graph = parse_data(DATA)
    assert len(graph) == 10


def test_part1():
    result = part1(DATA)
    assert result == 1651


def test_part2():
    result = part2(DATA)
    assert result == 1707


DATA = dedent("""\
    Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    Valve BB has flow rate=13; tunnels lead to valves CC, AA
    Valve CC has flow rate=2; tunnels lead to valves DD, BB
    Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
    Valve EE has flow rate=3; tunnels lead to valves FF, DD
    Valve FF has flow rate=0; tunnels lead to valves EE, GG
    Valve GG has flow rate=0; tunnels lead to valves FF, HH
    Valve HH has flow rate=22; tunnel leads to valve GG
    Valve II has flow rate=0; tunnels lead to valves AA, JJ
    Valve JJ has flow rate=21; tunnel leads to valve II
    """)
