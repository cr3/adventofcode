"""Unit tests for year 2022, day 20."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day20 import (
    Node,
    values_to_nodes,
    node_to_values,
    shorten_index,
    parse_data,
    part1,
    part2,
)


def test_remove():
    node = values_to_nodes([1, 2, 3])[0]
    node.right.remove()
    assert list(node_to_values(node)) == [1, 3]


def test_insert_after():
    node = values_to_nodes([1, 3])[0]
    Node(2).insert_after(node)
    assert list(node_to_values(node)) == [1, 2, 3]


@pytest.mark.parametrize(
    'node, i, expected',
    [
        (values_to_nodes([1, 2, 3])[0], 0, 1),
        (values_to_nodes([1, 2, 3])[0], 1, 2),
        (values_to_nodes([1, 2, 3])[0], 2, 3),
        (values_to_nodes([1, 2, 3])[0], 3, 1),
        (values_to_nodes([1, 2, 3])[0], -1, 2),
        (values_to_nodes([1, 2, 3])[0], -2, 1),
        (values_to_nodes([1, 2, 3])[0], -3, 3),
    ],
)
def test_node_skip(node, i, expected):
    result = node.skip(i).value
    assert result == expected


@pytest.mark.parametrize(
    'node, i, expected',
    [
        (values_to_nodes([1, 2, 3])[0], 0, [1, 2, 3]),
        (values_to_nodes([1, 2, 3])[0], 1, [1, 3, 2]),
    ],
)
def test_node_move(node, i, expected):
    result = list(node_to_values(node.move(i)))
    assert result == expected


def test_node_find_error():
    node = values_to_nodes([1, 2, 3])[0]
    with pytest.raises(ValueError):
        node.find(4)


@pytest.mark.parametrize(
    'index, length, expected',
    [
        (1, 10, 1),
        (9, 10, 0),
        (-9, 10, 0),
        (11, 10, 2),
        (-11, 10, -2),
        (8, 10, -1),
        (-8, 10, 1),
    ],
)
def test_shorten_index(index, length, expected):
    result = shorten_index(index, length)
    assert result == expected


def test_values_to_nodes():
    nodes = values_to_nodes([111, 222, 333])
    assert nodes == [
        Node(111, nodes[2], nodes[1]),
        Node(222, nodes[0], nodes[2]),
        Node(333, nodes[1], nodes[0]),
    ]


def test_parse_data():
    values = list(parse_data('111\n222\n333'))
    assert values == [111, 222, 333]


def test_part1():
    result = part1(DATA)
    assert result == 3


def test_part2():
    result = part2(DATA)
    assert result == 1623178306


DATA = dedent(
    """\
    1
    2
    -3
    3
    -2
    0
    4
    """,
)
