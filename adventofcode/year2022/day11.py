"""Day 11."""

import math
import re
from collections import UserList
from collections.abc import Callable
from functools import reduce
from operator import mul

from attrs import define, field

Transform = Callable[[int], int]


def identity(level: int):
    return level


def normalize(level: int):
    return int(level / 3)


@define(slots=True)
class Monkey:
    counter: int = 0
    divisor: int = 1
    items: list[int] = field(factory=list)
    operation: Transform = identity
    test: Transform = identity

    @classmethod
    def from_block(cls: type['Monkey'], block: str) -> 'Monkey':
        m = re.match(
            r'Monkey \d+:\n'
            r'  Starting items: (?P<items>.*)\n'
            r'  Operation: new = (?P<expr>.*)\n'
            r'  Test: divisible by (?P<divisor>\d+)\n'
            r'    If true: throw to monkey (?P<true>\d+)\n'
            r'    If false: throw to monkey (?P<false>\d+)',
            block,
        )
        assert m

        divisor = int(m['divisor'])

        def operation(old):
            return eval(m['expr'])

        def test(level):
            return int(m['false'] if level % divisor else m['true'])

        return cls(
            items=[int(i) for i in m['items'].split(', ')],
            divisor=divisor,
            operation=operation,
            test=test,
        )

    def inspect(
        self, monkeys: list['Monkey'], normalize: Transform = normalize
    ) -> list['Monkey']:
        self.counter += len(self.items)
        while self.items:
            item = self.items.pop(0)
            level = normalize(self.operation(item))
            n = self.test(level)
            monkeys[n].items.append(level)

        return monkeys


class Monkeys(UserList):
    @property
    def divisor(self):
        return reduce(math.lcm, (m.divisor for m in self))

    @property
    def level(self):
        counters = sorted((m.counter for m in self), reverse=True)
        return reduce(mul, counters[:2])

    def inspect(self, rounds: int, normalize: Transform = normalize):
        for _ in range(rounds):
            for m in self:
                m.inspect(self, normalize)

        return self


def parse_data(data: str) -> Monkeys:
    return Monkeys(map(Monkey.from_block, data.split('\n\n')))


def part1(data: str) -> int:
    monkeys = parse_data(data).inspect(20)
    return monkeys.level


def part2(data: str) -> int:
    monkeys = parse_data(data)
    monkeys.inspect(10_000, lambda level: level % monkeys.divisor)
    return monkeys.level
