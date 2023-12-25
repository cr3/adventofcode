"""Day 8."""

import re
from collections.abc import Iterator
from itertools import count
from math import lcm

from attrs import define


@define(frozen=True)
class Node:
    name: str
    left: str
    right: str

    @classmethod
    def from_string(cls, string: str) -> 'Node':
        if m := re.match(r'(?P<n>\w+) = \((?P<l>\w+), (?P<r>\w+)\)', string):
            return cls(m['n'], m['l'], m['r'])

        raise ValueError(f'Invalid node: {string}')

    def follow(self, instruction):
        if instruction == 'L':
            return self.left
        elif instruction == 'R':
            return self.right
        else:
            raise ValueError(f'Invalid instruction: {instruction}')


@define(frozen=True)
class Instructions:
    items: str

    def __iter__(self) -> Iterator[str]:
        for i in count():  # pragma: nocover
            yield self.items[i % len(self.items)]


@define(frozen=True)
class Network:
    instructions: Instructions
    nodes: dict[str, Node]

    @classmethod
    def from_data(cls, data: str) -> 'Network':
        items, other = data.split('\n\n')
        instructions = Instructions(items)
        nodes = {n.name: n for n in map(Node.from_string, other.splitlines())}
        return cls(instructions, nodes)

    def steps(self, start: str, condition) -> int:
        steps = 0
        for instruction in self.instructions:  # pragma: nocover
            steps += 1
            node = self.nodes[start]
            start = node.follow(instruction)
            if condition(start):
                break

        return steps


def part1(data: str) -> int:
    network = Network.from_data(data)
    steps = network.steps('AAA', lambda s: s == 'ZZZ')
    return steps


def part2(data: str) -> int:
    network = Network.from_data(data)
    names = [n for n in network.nodes if n.endswith('A')]
    all_steps = [network.steps(n, lambda s: s.endswith('Z')) for n in names]
    steps = lcm(*all_steps)
    return steps
