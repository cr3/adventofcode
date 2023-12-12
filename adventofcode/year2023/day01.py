"""Day 1."""

import re
from collections.abc import Callable

DIGIT_NAMES = 'one two three four five six seven eight nine'.split()


def parse_digit(digit):
    try:
        return DIGIT_NAMES.index(digit) + 1
    except ValueError:
        return int(digit)


def parse_alphanumeric(line: str) -> int:
    pattern = rf'(?=(\d|{"|".join(DIGIT_NAMES)}))'
    matches = re.finditer(pattern, line)
    digits = [parse_digit(m.group(1)) for m in matches]
    return digits[0] * 10 + digits[-1]


def parse_numeric(line: str) -> int:
    digits = [c for c in line if c.isdigit()]
    return int(f'{digits[0]}{digits[-1]}')


def parse_data(data: str, parser: Callable[[str], int]) -> int:
    return sum(map(parser, data.splitlines()))


def part1(data: str) -> int:
    return parse_data(data, parse_numeric)


def part2(data: str) -> int:
    return parse_data(data, parse_alphanumeric)
