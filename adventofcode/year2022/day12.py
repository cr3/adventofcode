"""Day 12."""

import sys
import math
import string
from itertools import count
from typing import Iterable, Iterator, Type

import attr


HEIGHTS: dict[str, int] = dict(
    [*zip(list(string.ascii_lowercase), count()), ('S', 0), ('E', 25)]
)


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Node:

    row: int
    col: int
    height: str

    def distance(self, other: 'Node') -> float:
        return math.sqrt(
            (self.row - other.row) ** 2 + (self.col - other.col) ** 2
        )

    def elevation(self, other: 'Node') -> int:
        return HEIGHTS[other.height] - HEIGHTS[self.height]


Matrix = list[list[Node]]


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Heightmap:

    rows: Matrix

    @classmethod
    def from_data(cls: Type['Heightmap'], data: str) -> 'Heightmap':
        return cls(
            [
                [
                    Node(row, col, height)
                    for col, height in enumerate(list(line))
                ]
                for row, line in enumerate(data.splitlines())
            ]
        )

    @property
    def nodes(self) -> Iterable[Node]:
        for row in self.rows:
            for node in row:
                yield node

    @property
    def start(self) -> Node:
        return next(self.find('S'))

    @property
    def end(self) -> Node:
        return next(self.find('E'))

    def find(self, height: str) -> Iterator[Node]:
        for node in self.nodes:
            if node.height == height:
                yield node

    def neighbours(self, node: Node) -> Iterable[Node]:
        row_start = max(node.row - 1, 0)
        row_stop = min(node.row + 2, len(self.rows))
        col_start = max(node.col - 1, 0)
        col_stop = min(node.col + 2, len(self.rows[0]))
        for row in range(row_start, row_stop):
            for col in range(col_start, col_stop):
                other = self.rows[row][col]
                if node.distance(other) == 1 and node.elevation(other) <= 1:
                    yield other

    def shortest_path(self) -> int:
        visited = set()
        distances = {n: sys.maxsize for n in self.nodes}
        distances[self.start] = 0

        while True:
            distance, node = min(
                (distance, node)
                for node, distance in distances.items()
                if node not in visited
            )

            visited.add(node)

            for other in self.neighbours(node):
                if other not in visited:
                    new_distance = distance + 1
                    if new_distance < distances[other]:
                        distances[other] = new_distance
                        if other == self.end:
                            return new_distance


def parse_data(data: str) -> Heightmap:
    return Heightmap.from_data(data)


def part1(data: str) -> int:
    heightmap = parse_data(data)
    return heightmap.shortest_path()


def part2(data: str) -> int:
    parse_data(data)
    return 0
