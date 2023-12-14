"""Day 2."""

import re
from functools import reduce

from attrs import define


@define(frozen=True)
class Play:
    blue: int = 0
    green: int = 0
    red: int = 0

    @classmethod
    def from_string(cls, string: str) -> 'Play':
        kwargs = {
            m['k']: int(m['v'])
            for m in re.finditer(r'(?P<v>\d+) (?P<k>\w+)', string)
        }
        return cls(**kwargs)

    @property
    def product(self):
        return (self.blue or 1) * (self.green or 1) * (self.red or 1)

    def __le__(self, other: 'Play') -> bool:
        return (
            self.blue <= other.blue
            and self.green <= other.green
            and self.red <= other.red
        )


@define(frozen=True)
class Game:
    num: int
    plays: list[Play]

    @classmethod
    def from_line(cls, line: str) -> 'Game':
        if m := re.match(r'Game (?P<num>\d+): (?P<plays>.*)', line):
            plays = [Play.from_string(s) for s in m['plays'].split('; ')]
            num = int(m['num'])
            return cls(num, plays)

        raise ValueError(f'Unexpected line: {line}')

    @property
    def minimum(self):
        return reduce(
            lambda a, b: Play(
                blue=max(a.blue, b.blue),
                green=max(a.green, b.green),
                red=max(a.red, b.red),
            ),
            self.plays,
            Play(),
        )

    def is_within(self, limit: Play) -> bool:
        return all(play <= limit for play in self.plays)


def part1(data: str) -> int:
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    limit = Play(red=12, green=13, blue=14)
    games = [Game.from_line(line) for line in data.splitlines()]
    total = sum(g.num for g in games if g.is_within(limit))
    return total


def part2(data: str) -> int:
    games = [Game.from_line(line) for line in data.splitlines()]
    total = sum(g.minimum.product for g in games)
    return total
