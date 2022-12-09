"""Day 8."""

from itertools import accumulate, starmap
from operator import lt, or_


def sum_views(a: list[bool], b: list[bool]):
    return list(starmap(or_, zip(a, b)))


def view_left(row: list[int]) -> list[bool]:
    maxes = list(accumulate(row, max, initial=-1))
    return list(starmap(lt, zip(maxes, maxes[1:])))


def view_right(row: list[int]) -> list[bool]:
    return list(reversed(view_left(list(reversed(row)))))


def view_row(row: list[int]) -> list[bool]:
    return sum_views(view_left(row), view_right(row))


def view_rows(matrix: list[list[int]]) -> list[list[bool]]:
    return list(map(view_row, matrix))


def view_cols(matrix: list[list[int]]) -> list[list[bool]]:
    return list(map(list, zip(*view_rows((zip(*matrix))))))  # type: ignore


def view_matrix(matrix: list[list[int]]) -> list[list[bool]]:
    rows = view_rows(matrix)
    cols = view_cols(matrix)
    return list(starmap(sum_views, zip(rows, cols)))


def parse_line(line: str) -> list[int]:
    return list(map(int, list(line)))


def parse_data(data: str) -> list[list[int]]:
    return list(map(parse_line, data.splitlines()))


def part1(data: str) -> int:
    matrix = parse_data(data)
    result = view_matrix(matrix)
    return sum(map(sum, result))


def part2(data: str) -> int:
    return 0
