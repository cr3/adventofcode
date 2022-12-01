"""Day 1."""

import argparse
from functools import partial
from io import TextIOBase
from itertools import groupby
from operator import eq
from pathlib import Path
from typing import Iterable


INPUT = Path(__file__).parent / 'input.txt'


def split_lines(stream: TextIOBase) -> Iterable[str]:
    """Split stream into lines without the trailing newline."""
    return map(str.strip, stream.readlines())


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


def parse_input(path: Path) -> int:
    with path.open() as stream:
        lines = split_lines(stream)
        groups = group_lines(lines)
        sums = sum_groups(groups)
        result = max(sums)

    return result


def main(argv: list[str] = []) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default=INPUT)
    args = parser.parse_args(argv)
    result = parse_input(args.input)
    print(result)


if __name__ == '__main__':  # pragma: no cover
    main()
