"""Day 18."""

from collections import Counter
from functools import total_ordering
from itertools import chain, groupby, product, starmap
from operator import attrgetter
from typing import Iterable

import attr


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Position:
    x: int
    y: int
    z: int


@total_ordering
@attr.s(eq=False, frozen=True, slots=True, auto_attribs=True)
class Face:
    a: Position
    b: Position
    c: Position
    d: Position

    @property
    def positions(self) -> Iterable[Position]:
        return sorted(attr.astuple(self))

    def __eq__(self, other) -> bool:
        return self.positions == other.positions

    def __lt__(self, other) -> bool:
        return self.positions < other.positions

    def __hash__(self) -> int:
        return sum(map(hash, self.positions))


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Cube:
    position: Position

    @classmethod
    def from_line(cls: type['Cube'], line: str) -> 'Cube':
        position = Position(*map(int, line.split(',')))  # type: ignore
        return cls(position)

    @property
    def vertices(self) -> Iterable[Position]:
        p = self.position
        return starmap(
            Position, product([p.x - 1, p.x], [p.y - 1, p.y], [p.z - 1, p.z])
        )

    @property
    def faces(self) -> Iterable[Face]:
        return (
            Face(*v)
            for attr in ['x', 'y', 'z']
            for _, v in groupby(
                sorted(self.vertices, key=attrgetter(attr)),
                key=attrgetter(attr),
            )
        )


def parse_data(data: str) -> Iterable[Cube]:
    return map(Cube.from_line, data.splitlines())


def part1(data: str) -> int:
    cubes = parse_data(data)
    faces = Counter(chain.from_iterable(map(lambda c: c.faces, cubes)))
    return sum(v for k, v in faces.items() if v == 1)


def part2(data: str) -> int:
    return 0
