"""Day 8."""

from functools import partial
from itertools import accumulate, product, starmap
from operator import lt, or_


def sum_views(*views: list[bool]):
    return list(starmap(or_, zip(*views)))


def view_right(row: list[int]) -> list[bool]:
    maxes = list(accumulate(row, max, initial=-1))
    return list(starmap(lt, zip(maxes, maxes[1:])))  # noqa: RUF007


def view_left(row: list[int]) -> list[bool]:
    return view_right(row[::-1])[::-1]


def view_row(row: list[int]) -> list[bool]:
    return sum_views(view_right(row), view_left(row))


def view_rows(matrix: list[list[int]]) -> list[list[bool]]:
    return list(map(view_row, matrix))


def view_cols(matrix: list[list[int]]) -> list[list[bool]]:
    return list(map(list, zip(*view_rows(zip(*matrix)))))  # type: ignore


def view_matrix(matrix: list[list[int]]) -> list[list[bool]]:
    rows = view_rows(matrix)
    cols = view_cols(matrix)
    return list(starmap(sum_views, zip(rows, cols)))


def rate_item(item: int, row: list[int]) -> int:
    score = 0
    for x in row:
        score += 1
        if x >= item:
            break
    return score


def rate_row_item(row: list[int], i: int) -> int:
    j = i + 1
    item = row[i]
    return rate_item(item, list(reversed(row[:i]))) * rate_item(item, row[j:])


def rate_matrix_item(matrix: list[list[int]], r: int, c: int) -> int:
    row = matrix[r]
    col = [matrix[i][c] for i in range(len(matrix))]
    score = rate_row_item(row, c) * rate_row_item(col, r)
    return score


def parse_line(line: str) -> list[int]:
    return list(map(int, list(line)))


def parse_data(data: str) -> list[list[int]]:
    return list(map(parse_line, data.splitlines()))


def part1(data: str) -> int:
    matrix = parse_data(data)
    result = view_matrix(matrix)
    return sum(map(sum, result))


def part2(data: str) -> int:
    matrix = parse_data(data)
    rate = partial(rate_matrix_item, matrix)
    rows = range(1, len(matrix) - 1)
    cols = range(1, len(matrix[0]) - 1)
    return max(starmap(rate, product(rows, cols)))
