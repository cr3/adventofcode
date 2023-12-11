"""Day 14."""

from collections.abc import Iterable
from functools import partial
from itertools import chain, pairwise, repeat, starmap, takewhile
from operator import attrgetter, truth

import attr


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Rock:
    x: int
    y: int

    @classmethod
    def from_string(cls: type['Rock'], string: str) -> 'Rock':
        return cls(*map(int, string.split(',')))  # type: ignore

    def with_y(self, y: int) -> 'Rock':
        return attr.evolve(self, y=y)

    def with_x(self, x: int) -> 'Rock':
        return attr.evolve(self, x=x)

    def step(self, rocks: set['Rock']) -> 'Rock':
        # If the tile immediately below is blocked (by rock or sand), the
        # unit of sand attempts to instead move diagonally one step
        # down and to the left. If that tile is blocked, the unit of
        # sand attempts to instead move diagonally one step down and to
        # the right.
        for other in [
            attr.evolve(self, y=self.y + 1),
            attr.evolve(self, x=self.x - 1, y=self.y + 1),
            attr.evolve(self, x=self.x + 1, y=self.y + 1),
        ]:
            if other not in rocks:
                return other

        return self


Rocks = set['Rock']


def drop_rock(rock: Rock, rocks: Rocks):
    bottom = max(map(attrgetter('y'), rocks))
    while True:
        current = rock.step(rocks)
        if current == rock:
            if current in rocks:
                return False
            else:
                rocks.add(current)
                return True

        if current.y == bottom:
            return False

        rock = current


def expand_rocks(start: Rock, end: Rock) -> Iterable[Rock]:
    if start.x == end.x:
        step = 1 if start.y < end.y else -1
        yield from map(start.with_y, range(start.y, end.y + step, step))
    else:
        step = 1 if start.x < end.x else -1
        yield from map(start.with_x, range(start.x, end.x + step, step))


def parse_rocks(line: str) -> Iterable[Rock]:
    return chain.from_iterable(
        starmap(
            expand_rocks,
            pairwise(map(Rock.from_string, line.split(' -> '))),
        )
    )


def parse_data(data: str) -> Rocks:
    return set(chain.from_iterable(map(parse_rocks, data.splitlines())))


def part1(data: str) -> int:
    rocks = parse_data(data)
    drop = partial(drop_rock, rocks=rocks)
    return sum(takewhile(truth, map(drop, repeat(Rock(500, 0)))))


def part2(data: str) -> int:
    rocks = parse_data(data)
    floor = max(map(attrgetter('y'), rocks)) + 2
    rocks = rocks.union(
        list(expand_rocks(Rock(500 - floor, floor), Rock(500 + floor, floor)))
    )
    drop = partial(drop_rock, rocks=rocks)
    return sum(takewhile(truth, map(drop, repeat(Rock(500, 0)))))
