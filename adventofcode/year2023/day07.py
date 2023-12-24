"""Day 7."""

from enum import IntEnum
from functools import total_ordering
from itertools import groupby

from attrs import define


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
class Hand1:
    cards: str
    bid: int = 0
    labels: str = '23456789TJQKA'

    @classmethod
    def from_string(cls, string: str) -> 'Hand1':
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
        elif groups[0] + groups[1] == 5:
            return HandType.FULL_HOUSE
        elif groups[0] == 3:
            return HandType.THREE_OF_A_KIND
        elif groups[0] + groups[1] == 4:
            return HandType.TWO_PAIRS
        elif groups[0] == 2:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD

    @property
    def weight(self) -> list[int]:
        return [self.type_, *map(self.labels.index, self.cards)]

    def __lt__(self, other) -> bool:
        return self.weight < other.weight


@total_ordering
@define(frozen=True, order=False)
class Hand2(Hand1):
    labels: str = 'J23456789TQKA'

    @property
    def jokers(self):
        return ''.join(c for c in self.cards if c == 'J')

    @property
    def non_jokers(self):
        return ''.join(c for c in self.cards if c != 'J')

    @property
    def type_(self) -> HandType:
        njokers = len(self.jokers)
        groups = sorted(
            (len(list(g[1])) for g in groupby(sorted(self.non_jokers))),
            reverse=True,
        ) or [0]
        if groups[0] + njokers == 5:
            return HandType.FIVE_OF_A_KIND
        elif groups[0] + njokers == 4:
            return HandType.FOUR_OF_A_KIND
        elif groups[0] + groups[1] + njokers == 5:
            return HandType.FULL_HOUSE
        elif groups[0] + njokers == 3:
            return HandType.THREE_OF_A_KIND
        elif groups[0] + groups[1] + njokers == 4:
            return HandType.TWO_PAIRS
        elif groups[0] + njokers == 2:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD


def part1(data: str) -> int:
    hands = sorted(map(Hand1.from_string, data.splitlines()))
    total = sum(i * h.bid for i, h in enumerate(hands, start=1))
    return total


def part2(data: str) -> int:
    hands = sorted(map(Hand2.from_string, data.splitlines()))
    total = sum(i * h.bid for i, h in enumerate(hands, start=1))
    return total
