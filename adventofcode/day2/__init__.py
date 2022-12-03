"""Day 2."""

from enum import IntEnum
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


T = TypeVar('T', bound='Round')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Round:

    shape: Shape
    response: Shape

    @classmethod
    def parse(cls: Type[T], line: str) -> T:
        """Parse a line into a round."""
        shape, response = line.split()
        return cls(Shape[shape], Shape[response])

    @property
    def score(self):
        """
        The score for a single round is the score for the shape you
        selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus
        the score for the outcome of the round (0 if you lost, 3 if the
        round was a draw, and 6 if you won).
        """
        score = self.response
        if self.shape == self.response:
            score += 3
        elif (
            (self.shape == Shape.C and self.response == Shape.X)
            or (self.shape == Shape.A and self.response == Shape.Y)
            or (self.shape == Shape.B and self.response == Shape.Z)
        ):
            score += 6

        return score


def parse_rounds(lines: Iterable[str]) -> Iterable[Round]:
    """Parse lines into rounds."""
    return map(Round.parse, lines)


def parse_input(path: Path) -> Iterable[Round]:
    """Parse a path into scores."""
    with path.open() as stream:
        lines = split_lines(stream)
        return parse_rounds(lines)


def part1(path: Path = INPUT) -> None:
    rounds = parse_input(path)
    result = sum(r.score for r in rounds)
    print(result)
