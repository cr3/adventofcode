"""Day 7."""

from enum import IntEnum
from functools import total_ordering
from itertools import groupby

from attrs import define

CARDS = '23456789TJQKA'


class HandType(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


@total_ordering
@define(frozen=True, order=False)
class Hand:
    cards: str
    bid: int = 0

    @classmethod
    def from_string(cls, string: str) -> 'Hand':
        cards, bid = string.split()
        return cls(cards, int(bid))

    @property
    def type_(self) -> HandType:
        groups = sorted(
            (len(list(g[1])) for g in groupby(sorted(self.cards))),
            reverse=True,
        )
        if groups[0] == 5:
            return HandType.FIVE_OF_A_KIND
        elif groups[0] == 4:
            return HandType.FOUR_OF_A_KIND
        elif groups[0] == 3 and groups[1] == 2:
            return HandType.FULL_HOUSE
        elif groups[0] == 3:
            return HandType.THREE_OF_A_KIND
        elif groups[0] == 2 and groups[1] == 2:
            return HandType.TWO_PAIRS
        elif groups[0] == 2:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD

    @property
    def weight(self) -> list[int]:
        return [self.type_, *map(CARDS.index, self.cards)]

    def __lt__(self, other) -> bool:
        return self.weight < other.weight


def part1(data: str) -> int:
    hands = sorted(map(Hand.from_string, data.splitlines()))
    total = sum(i * h.bid for i, h in enumerate(hands, start=1))
    return total


def part2(data: str) -> int:
    return 0
