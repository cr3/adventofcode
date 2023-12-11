"""Day 9."""

from collections.abc import Iterable
from enum import Enum, auto
from functools import reduce
from itertools import accumulate

import attr


class Direction(Enum):
    U = auto()
    D = auto()
    R = auto()
    L = auto()


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Move:
    """A move consisting of a direction and steps."""

    direction: Direction
    steps: int

    @classmethod
    def from_line(cls: type['Move'], line: str) -> 'Move':
        """Parse a move from a `line`."""
        direction, steps = line.split()
        return cls(Direction[direction], int(steps))

    def apply(self, rope: 'Rope'):
        for _ in range(self.steps):
            rope = rope.move(self.direction)
        return rope


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Knot:
    x: int = 0
    y: int = 0

    def touching(self, other: 'Knot') -> bool:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= 2

    def move(self, direction: Direction) -> 'Knot':
        """Move this knot in the given `direction`."""
        x, y = attr.astuple(self)
        match direction:  # pragma: no cover
            case Direction.U:
                y += 1
            case Direction.D:
                y -= 1
            case Direction.R:
                x += 1
            case Direction.L:
                x -= 1

        return attr.evolve(self, x=x, y=y)

    def follow(self, other: 'Knot') -> 'Knot':
        """Follow some `other` knot if not touching this knot."""
        if self.touching(other):
            return self

        x = follow_coordinate(self.x, other.x)
        y = follow_coordinate(self.y, other.y)
        return attr.evolve(self, x=x, y=y)


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Rope:
    head: Knot = Knot()
    tails: list[Knot] = attr.ib(factory=lambda: [Knot()])
    seen: set[Knot] = attr.ib(
        default=attr.Factory(lambda self: {self.tails[-1]}, takes_self=True)
    )

    @property
    def positions(self):
        return len(self.seen)

    def move(self, direction: Direction):
        """Move the `head` and follow `tails`."""
        knots = accumulate(
            [self.head.move(direction), *self.tails],
            lambda a, b: b.follow(a),
        )
        head = next(knots)
        tails = list(knots)
        seen = self.seen.union({tails[-1]})
        return attr.evolve(self, head=head, tails=tails, seen=seen)


def follow_coordinate(src: int, dst: int):
    """Follow `src` to `dst` by only one step."""
    return src + 1 if src < dst else src - 1 if src > dst else src


def parse_data(data: str) -> Iterable[Move]:
    return map(Move.from_line, data.splitlines())


def part1(data: str) -> int:
    moves = parse_data(data)
    rope = reduce(lambda r, m: m.apply(r), moves, Rope())
    return rope.positions


def part2(data: str) -> int:
    moves = parse_data(data)
    rope = reduce(lambda r, m: m.apply(r), moves, Rope(tails=[Knot()] * 9))
    return rope.positions
