"""Day 2."""

from enum import Enum, IntEnum
from pathlib import Path
from typing import Iterable, Type, TypeVar

import attr

from adventofcode.day1 import split_lines


INPUT = Path(__file__).parent / 'input.txt'


class Shape(IntEnum):
    """Map shape to score."""

    A = X = 1  # Rock
    B = Y = 2  # Paper
    C = Z = 3  # Scissors


class Response(Enum):
    """Map response to defeating shape."""

    X = Shape.C
    Y = Shape.A
    Z = Shape.B

    @property
    def shape(self) -> Shape:
        return Shape[self.name]

    def defeats(self, shape: Shape) -> bool:
        """
        Rock defeats Scissors, Scissors defeats Paper, and Paper
        defeats Rock.
        """
        return self.value == shape

    def outcome(self, shape: Shape) -> int:
        """
        0 if you lost, 3 if the round was a draw, and 6 if you won.
        """
        if self.defeats(shape):
            return 6
        elif self.shape == shape:
            return 3
        else:
            return 0


T = TypeVar('T', bound='Round')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Round:

    shape: Shape
    response: Response

    @classmethod
    def parse(cls: Type[T], line: str) -> T:
        """Parse a line into a round."""
        shape, response = line.split()
        return cls(Shape[shape], Response[response])

    @property
    def score(self) -> int:
        """
        The score for a single round is the score for the shape you
        selected plus the score for the outcome of the round.
        """
        return self.response.shape + self.response.outcome(self.shape)


def parse_rounds(lines: Iterable[str]) -> Iterable[Round]:
    """Parse lines into rounds."""
    return map(Round.parse, lines)


def parse_input(path: Path) -> Iterable[int]:
    """Parse a path into scores."""
    with path.open() as stream:
        lines = split_lines(stream)
        rounds = parse_rounds(lines)
        return (r.score for r in rounds)


def part1(path: Path = INPUT) -> None:
    scores = parse_input(path)
    result = sum(scores)
    print(result)
