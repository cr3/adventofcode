"""Day 1."""

from functools import partial
from itertools import groupby
from operator import eq
from typing import Iterable


def group_lines(lines: Iterable[str], separator='') -> Iterable[list[str]]:
    """Group lines on separator."""
    return (
        list(group)
        for key, group in groupby(lines, partial(eq, separator))
        if not key
    )


def sum_groups(groups: Iterable[list[str]]) -> Iterable[int]:
    """Sum groups."""
    return (sum(map(int, group)) for group in groups)


def parse_data(data: str) -> Iterable[int]:
    lines = data.splitlines()
    groups = group_lines(lines)
    return sum_groups(groups)


def part1(data: str) -> int:
    sums = parse_data(data)
    result = max(sums)
    return result


def part2(data: str) -> int:
    sums = parse_data(data)
    result = sum(sorted(sums, reverse=True)[0:3])
    return result
