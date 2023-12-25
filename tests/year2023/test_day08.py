'''Unit tests for year 2024, day 8.'''

from itertools import islice
from textwrap import dedent

import pytest

from adventofcode.year2023.day08 import (
    Instructions,
    Network,
    Node,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'string, expected',
    [
        ('AAA = (BBB, CCC)', Node('AAA', 'BBB', 'CCC')),
    ],
)
def test_node_from_string(string, expected):
    result = Node.from_string(string)
    assert result == expected


@pytest.mark.parametrize(
    'string',
    [
        'AAA',
        'AAA = BBB',
        'AAA = (BBB)',
        'AAA = (BBB, )',
    ],
)
def test_node_from_string_error(string):
    with pytest.raises(ValueError):
        Node.from_string(string)


@pytest.mark.parametrize(
    'node, instruction, expected',
    [
        (Node('AAA', 'BBB', 'CCC'), 'L', 'BBB'),
        (Node('AAA', 'BBB', 'CCC'), 'R', 'CCC'),
    ],
)
def test_node_follow(node, instruction, expected):
    result = node.follow(instruction)
    assert result == expected


@pytest.mark.parametrize(
    'instruction',
    [
        '',
        'A',
        'X',
    ],
)
def test_node_follow_error(instruction):
    node = Node('AAA', 'BBB', 'CCC')
    with pytest.raises(ValueError):
        node.follow(instruction)


def test_instructions_iter():
    instructions = Instructions('RL')
    result = "".join(islice(instructions, 4))
    assert result == 'RLRL'


@pytest.mark.parametrize(
    'data, expected',
    [
        (
            dedent('''\
            RL

            AAA = (BBB, CCC)
            BBB = (DDD, EEE)
            '''),
            Network(
                Instructions('RL'),
                {
                    'AAA': Node('AAA', 'BBB', 'CCC'),
                    'BBB': Node('BBB', 'DDD', 'EEE'),
                },
            ),
        )
    ],
)
def test_network_from_data(data, expected):
    result = Network.from_data(data)
    assert result == expected


def test_network_steps():
    network = Network(
        Instructions('RL'),
        {
            'AAA': Node('AAA', 'BBB', 'CCC'),
            'BBB': Node('BBB', 'DDD', 'EEE'),
            'CCC': Node('CCC', 'ZZZ', 'GGG'),
        },
    )
    result = network.steps('AAA', lambda s: s == 'ZZZ')
    assert result == 2


def test_part1():
    result = part1(dedent('''\
        RL

        AAA = (BBB, CCC)
        BBB = (DDD, EEE)
        CCC = (ZZZ, GGG)
        DDD = (DDD, DDD)
        EEE = (EEE, EEE)
        GGG = (GGG, GGG)
        ZZZ = (ZZZ, ZZZ)
        '''))
    assert result == 2


def test_part2():
    result = part2(dedent('''\
        LR

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)
        '''))
    assert result == 6
