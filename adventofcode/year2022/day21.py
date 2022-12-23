"""Day 21."""

from collections import UserDict


class Locals(UserDict):
    def __getitem__(self, key):
        return eval(super().__getitem__(key), {}, self)


def parse_data(data: str) -> dict[str, str]:
    return dict(line.split(': ') for line in data.splitlines())


def part1(data: str) -> int:
    monkeys = parse_data(data)
    return int(eval(monkeys['root'], {}, Locals(monkeys)))


def part2(data: str) -> int:
    return 0
