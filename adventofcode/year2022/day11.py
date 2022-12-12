"""Day 11."""

import re
from collections import UserList
from functools import reduce
from operator import mul
from typing import Callable

import attr


@attr.s(slots=True, auto_attribs=True)
class Monkey:

    counter: int = 0
    divisor: int = 3
    items: list[int] = attr.ib(factory=list)
    operation: Callable[[int], int] = lambda old: old
    test: Callable[[int], int] = lambda level: -1

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

        def operation(old):
            return eval(m['expr'])

        def test(level):
            return int(m['false'] if level % int(m['divisor']) else m['true'])

        return cls(
            items=[int(i) for i in m['items'].split(', ')],
            operation=operation,
            test=test,
        )

    def inspect(self, monkeys: list['Monkey']) -> list['Monkey']:
        self.counter += len(self.items)
        while self.items:
            item = self.items.pop(0)
            level = int(self.operation(item) / 3)
            n = self.test(level)
            monkeys[n].items.append(level)

        return monkeys


class Monkeys(UserList):
    @property
    def level(self):
        counters = sorted((m.counter for m in self), reverse=True)
        return reduce(mul, counters[:2])

    def inspect(self, rounds: int):
        for _ in range(rounds):
            for m in self:
                m.inspect(self)

        return self


def parse_data(data: str) -> Monkeys:
    return Monkeys(map(Monkey.from_block, data.split('\n\n')))


def part1(data: str) -> int:
    monkeys = parse_data(data).inspect(20)
    return monkeys.level


def part2(data: str) -> int:
    parse_data(data)
    return 0
