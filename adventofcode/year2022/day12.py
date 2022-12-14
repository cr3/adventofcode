"""Day 12."""

import math
import string
from itertools import count
from typing import Iterable, Iterator, Type

import attr


Matrix = list[list[str]]

HEIGHTS: dict[str, int] = dict(
    [*zip(list(string.ascii_lowercase), count()), ('S', 0), ('E', 25)]
)


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Position:

    row: int
    col: int
    height: str

    def distance(self, other: 'Position') -> float:
        return math.sqrt(
            (self.row - other.row) ** 2 + (self.col - other.col) ** 2
        )

    def elevation(self, other: 'Position') -> int:
        return abs(HEIGHTS[self.height] - HEIGHTS[other.height])


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Heightmap:

    rows: Matrix

    @classmethod
    def from_data(cls: Type['Heightmap'], data: str) -> 'Heightmap':
        rows = list(map(list, data.splitlines()))  # type: ignore
        return cls(rows)  # type: ignore

    @property
    def cols(self) -> Matrix:
        return list(map(list, zip(*self.rows)))

    @property
    def start(self) -> Position:
        return next(self.find('S'))

    @property
    def end(self) -> Position:
        return next(self.find('E'))

    def find(self, height: str) -> Iterator[Position]:
        for row, cols in enumerate(self.rows):
            for col, h in enumerate(cols):
                if h == height:
                    yield Position(row, col, h)

    def destinations(self, pos: Position) -> Iterator[Position]:
        row_start = max(pos.row - 1, 0)
        row_stop = min(pos.row + 2, len(self.rows))
        col_start = max(pos.col - 1, 0)
        col_stop = min(pos.col + 2, len(self.rows[0]))
        for row in range(row_start, row_stop):
            for col in range(col_start, col_stop):
                height = self.rows[row][col]
                dest = Position(row, col, height)
                if pos.distance(dest) == 1.0 and pos.elevation(dest) <= 1:
                    yield dest

    def walk(self, pos: Position, seen: list[Position] = []) -> Iterable[int]:
        if pos.height == 'E':
            yield len(seen)
        else:
            for dest in self.destinations(pos):
                if dest not in seen:
                    yield from self.walk(dest, seen + [pos])


def parse_data(data: str) -> Heightmap:
    return Heightmap.from_data(data)


def part1(data: str) -> int:
    heightmap = parse_data(data)
    return min(heightmap.walk(heightmap.start))


def part2(data: str) -> int:
    parse_data(data)
    return 0
