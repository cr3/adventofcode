"""Day 20."""

from functools import partial
from operator import mul
from typing import Iterable, Optional

import attr


@attr.s(repr=False, slots=True, auto_attribs=True)
class Node:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def __repr__(self):
        left = self.left.value if self.left else None
        right = self.right.value if self.right else None
        return f'Node(value={self.value}, left={left}, right={right})'

    def remove(self):
        self.left.right = self.right
        self.right.left = self.left
        self.left = self.right = None
        return self

    def insert_after(self, left):
        self.left = left
        self.right = left.right
        left.right.left = left.right = self
        return self

    def skip(self, index: int) -> 'Node':
        node = self
        if index < 0:
            # Move +1 to the left for the left node.
            for _ in range(-index + 1):
                assert node.left
                node = node.left
        elif index > 0:
            for _ in range(index):
                assert node.right
                node = node.right

        return node

    def move(self, index: int) -> 'Node':
        if index:
            other = self.skip(index)
            self.remove().insert_after(other)

        return self

    def find(self, value: int) -> 'Node':
        current = self
        while True:
            if current.value == value:
                return current

            assert current.right
            current = current.right
            if current == self:
                raise ValueError(f'Value {value} not found')


def shorten_index(index: int, length: int) -> int:
    length -= 1
    index %= length
    if length - index < index:
        index -= length
    return index


def values_to_nodes(values: Iterable[int]) -> list[Node]:
    nodes = list(map(Node, values))
    for i, node in enumerate(nodes):
        node.left = nodes[i - 1]
        node.right = nodes[(i + 1) % len(nodes)]

    return nodes


def node_to_values(node: Node) -> Iterable[int]:
    current = node
    while True:
        yield current.value

        assert current.right
        current = current.right
        if current == node:
            break


def parse_data(data: str) -> Iterable[int]:
    return map(eval, data.splitlines())


def part1(data: str) -> int:
    nodes = values_to_nodes(parse_data(data))
    for node in nodes:
        node.move(shorten_index(node.value, len(nodes)))
    values = list(node_to_values(nodes[0].find(0)))
    return sum(values[index % len(values)] for index in [1000, 2000, 3000])


def part2(data: str) -> int:
    apply_key = partial(mul, 811589153)
    nodes = values_to_nodes(map(apply_key, parse_data(data)))
    for _ in range(10):
        for node in nodes:
            node.move(shorten_index(node.value, len(nodes)))
    values = list(node_to_values(nodes[0].find(0)))
    return sum(values[index % len(values)] for index in [1000, 2000, 3000])
