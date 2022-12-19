"""Day 2."""

from enum import IntEnum
from typing import Iterable, TypeVar

import attr


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
    def parse(cls: type[T], line: str) -> T:
        """Parse a line into a round."""
        shape, response = line.split()
        return cls(Shape[shape], Shape[response])


def calculate1(shape: Shape, response: Shape) -> int:
    """
    The score for a single round is the score for the shape you
    selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus
    the score for the outcome of the round (0 if you lost, 3 if the
    round was a draw, and 6 if you won).
    """
    score = response.value
    if shape == response:
        score += 3
    elif (
        (shape == Shape.C and response == Shape.X)
        or (shape == Shape.A and response == Shape.Y)
        or (shape == Shape.B and response == Shape.Z)
    ):
        score += 6

    return score


def calculate2(shape: Shape, response: Shape) -> int:
    """
    X means you need to lose, Y means you need to end the round in
    a draw, and Z means you need to win. Good luck!"
    """
    if response == Shape.X:
        new_response = {
            Shape.A: Shape.Z,
            Shape.B: Shape.X,
            Shape.C: Shape.Y,
        }[shape]
    elif response == Shape.Z:
        new_response = {
            Shape.A: Shape.Y,
            Shape.B: Shape.Z,
            Shape.C: Shape.X,
        }[shape]
    else:
        new_response = shape

    return calculate1(shape, new_response)


def parse_rounds(lines: Iterable[str]) -> Iterable[Round]:
    """Parse lines into rounds."""
    return map(Round.parse, lines)


def parse_data(data: str) -> Iterable[Round]:
    """Parse a path into scores."""
    return parse_rounds(data.splitlines())


def part1(data: str) -> int:
    rounds = parse_data(data)
    result = sum(calculate1(r.shape, r.response) for r in rounds)
    return result


def part2(data: str) -> int:
    rounds = parse_data(data)
    result = sum(calculate2(r.shape, r.response) for r in rounds)
    return result
