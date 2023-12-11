"""Day 13."""

from collections.abc import Iterable
from functools import cmp_to_key, reduce
from operator import mul
from typing import Union

Packet = list[Union[int, 'Packet']]
Pair = tuple[Packet, Packet]


def compare(left: Packet, right: Packet) -> int:
    for i in range(max(len(left), len(right))):
        # If the left list runs out of items first,
        # the inputs are in the right order.
        try:
            lvalue = left[i]
        except IndexError:
            return -1

        # If the right list runs out of items first,
        # the inputs are not in the right order.
        try:
            rvalue = right[i]
        except IndexError:
            return 1

        # If both values are integers,
        # the lower integer should come first.
        if isinstance(lvalue, int) and isinstance(rvalue, int):
            # If the left integer is lower than the right integer,
            # the inputs are in the right order.
            if lvalue < rvalue:
                return -1
            # If the left integer is higher than the right integer,
            # the inputs are not in the right order.
            elif lvalue > rvalue:
                return 1
            # Otherwise, the inputs are the same integer;
            # continue checking the next part of the input.
            else:
                continue

        # If exactly one value is an integer,
        # convert the integer to a list which contains that
        # integer as its only value...
        if isinstance(lvalue, int):
            lvalue = [lvalue]
        if isinstance(rvalue, int):
            rvalue = [rvalue]

        # then retry the comparison.
        result = compare(lvalue, rvalue)
        if result:
            return result

    return 0


def parse_packet(line: str) -> Packet:
    return eval(line)


def parse_pair(block: str) -> Pair:
    return tuple(map(parse_packet, block.splitlines()))  # type: ignore


def parse_data(data: str) -> Iterable[Pair]:
    return map(parse_pair, data.split('\n\n'))


def part1(data: str) -> int:
    pairs = parse_data(data)
    return sum(i for i, pair in enumerate(pairs, 1) if compare(*pair) < 0)


def part2(data: str) -> int:
    pairs = parse_data(data)
    dividers = [[[2]], [[6]]]
    packets = sorted(
        list(sum(pairs, ())) + dividers,  # type: ignore
        key=cmp_to_key(compare),  # type: ignore
    )
    return reduce(mul, [packets.index(d) + 1 for d in dividers], 1)
