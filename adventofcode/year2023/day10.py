"""Day 10."""

from collections.abc import Container, Iterator
from enum import Enum, auto

from attrs import define


class D(Enum):
    """Direction."""

    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


@define(frozen=True)
class Pipe(Container):
    directions: list[D]

    def __contains__(self, direction):
        return direction in self.directions

    @property
    def is_start(self) -> bool:
        return len(self.directions) == 4


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal;
#   there is a pipe on this tile, but your sketch
#   doesn't show what shape the pipe has.
PIPES = {
    '|': Pipe([D.NORTH, D.SOUTH]),
    '-': Pipe([D.EAST, D.WEST]),
    'L': Pipe([D.NORTH, D.EAST]),
    'J': Pipe([D.NORTH, D.WEST]),
    '7': Pipe([D.SOUTH, D.WEST]),
    'F': Pipe([D.SOUTH, D.EAST]),
    '.': Pipe([]),
    'S': Pipe(list(D)),
}


@define(frozen=True)
class Tile(Container):
    i: int
    j: int
    pipe: Pipe = PIPES['.']

    def __contains__(self, direction):
        return direction in self.pipe

    def is_connected(self, other: 'Tile'):
        return any([
            (D.NORTH in self and D.SOUTH in other and self.i > other.i),
            (D.SOUTH in self and D.NORTH in other and self.i < other.i),
            (D.WEST in self and D.EAST in other and self.j > other.j),
            (D.EAST in self and D.WEST in other and self.j < other.j),
        ])


@define(frozen=True)
class Grid:
    pipes: list[list[Pipe]]

    @classmethod
    def from_data(cls, data) -> 'Grid':
        pipes = [[PIPES[c] for c in line] for line in data.splitlines()]
        return cls(pipes)

    def start(self) -> Tile:
        for i, pipes in enumerate(self.pipes):
            for j, pipe in enumerate(pipes):
                if pipe.is_start:
                    return Tile(i, j, pipe)

        raise ValueError('Start tile not found')

    def surroundings(self, tile: Tile) -> Iterator[Tile]:
        max_i, max_j = len(self.pipes), len(self.pipes[0])
        for i in range(max(0, tile.i - 1), min(max_i, tile.i + 2)):
            for j in range(max(0, tile.j - 1), min(max_j, tile.j + 2)):
                if all([
                    (i == tile.i or j == tile.j),
                    (i != tile.i or j != tile.j),
                ]):
                    pipe = self.pipes[i][j]
                    yield Tile(i, j, pipe)

    def connected(self, tile: Tile) -> Iterator[Tile]:
        for surrounding in self.surroundings(tile):  # pragma: nocover
            if tile.is_connected(surrounding):
                yield surrounding

    def all_connected(self, start: Tile) -> Iterator[Tile]:
        p, n = start, next(self.connected(start))
        while True:
            yield n
            for connected in self.connected(n):  # pragma: nocover
                if connected != p:
                    p, n = n, connected
                    break
            if n == start:
                break


def part1(data: str) -> int:
    grid = Grid.from_data(data)
    start = grid.start()
    total = sum(1 for _ in grid.all_connected(start))
    return int((total + 1) / 2)


def part2(data: str) -> int:
    return 0
