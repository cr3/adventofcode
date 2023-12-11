"""Day 1."""


def parse_line(line: str) -> int:
    digits = [c for c in line if c.isdigit()]
    return int(f"{digits[0]}{digits[-1]}")


def parse_data(data: str) -> int:
    return sum(map(parse_line, data.splitlines()))


def part1(data: str) -> int:
    return parse_data(data)


def part2(data: str) -> int:
    return 0
