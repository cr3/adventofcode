"""Day 10."""

import attr
from abc import ABC, abstractmethod
from functools import reduce
from itertools import starmap
from operator import mul
from typing import Iterable, Type


@attr.s(frozen=True, slots=True, auto_attribs=True)
class State:

    x: int = 1
    cycle: int = 0
    strengths: dict[int, int] = attr.ib(factory=dict)

    @property
    def total_strength(self):
        return sum(starmap(mul, self.strengths.items()))

    def tick(self) -> 'State':
        cycle = self.cycle + 1
        strengths = self.strengths
        if not (cycle - 20) % 40:
            strengths[cycle] = self.x

        return attr.evolve(self, cycle=cycle, strengths=strengths)

    def increase(self, value: int) -> 'State':
        x = self.x + value
        return attr.evolve(self, x=x)


class Instruction(ABC):
    @abstractmethod
    def execute(self, state: State) -> State:
        """Execute this instruction with the given X register."""

    @classmethod
    def from_line(cls: Type['Instruction'], line: str) -> 'Instruction':
        match line.split():  # pragma: no cover
            case ['noop']:
                return Noop()

            case ['addx', value]:
                return Addx(int(value))

            case instruction:
                raise Exception(f'Unsupported instruction: {instruction}')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Noop(Instruction):
    def execute(self, state: State) -> State:
        return state.tick()


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Addx(Instruction):

    value: int

    def execute(self, state: State) -> State:
        return state.tick().tick().increase(self.value)


def parse_data(data: str) -> Iterable[Instruction]:
    return map(Instruction.from_line, data.splitlines())


def part1(data: str) -> int:
    instructions = parse_data(data)
    state = reduce(lambda s, i: i.execute(s), instructions, State())
    return state.total_strength


def part2(data: str) -> int:
    return 0
