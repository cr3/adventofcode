"""Day 4."""

import re

from attrs import define


class Numbers(set):
    @classmethod
    def from_string(cls, string: str) -> 'Numbers':
        return cls(set(map(int, string.split())))


@define
class Card:
    num: int
    winning: Numbers
    chosen: Numbers
    count: int = 1

    @classmethod
    def from_string(cls, string: str) -> 'Card':
        if m := re.match(
            r'Card\s+(?P<n>\d+): (?P<w>[\d ]+) \| (?P<m>[\d ]+)', string
        ):
            return cls(
                num=int(m['n']),
                winning=Numbers.from_string(m['w']),
                chosen=Numbers.from_string(m['m']),
            )

        raise ValueError(f"Invalid card string: {string}")

    def matches(self):
        return self.winning.intersection(self.chosen)

    def points(self):
        count = len(self.matches())
        return int(2 ** (count - 1))


def part1(data: str) -> int:
    cards = map(Card.from_string, data.splitlines())
    total = sum(c.points() for c in cards)
    return total


def part2(data: str) -> int:
    cards = list(map(Card.from_string, data.splitlines()))
    for card in cards:
        for i, _ in enumerate(card.matches(), start=card.num):
            cards[i].count += card.count

    total = sum(c.count for c in cards)
    return total
