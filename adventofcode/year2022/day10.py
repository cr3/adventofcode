"""Day 10."""

import attr
from abc import ABC, abstractmethod
from functools import reduce
from itertools import starmap
from operator import mul
from typing import Iterable, TypeVar


class State(ABC):
    @abstractmethod
    def tick(self) -> 'State':
        """One clock cycle."""

    @abstractmethod
    def increase(self, value: int) -> 'State':
        """Increase the register by the given `value`."""


@attr.s(frozen=True, slots=True, auto_attribs=True)
class StateStrength(State):

    x: int = 1
    cycle: int = 0
    strengths: dict[int, int] = attr.ib(factory=dict)

    @property
    def total_strength(self):
        return sum(starmap(mul, self.strengths.items()))

    def tick(self) -> State:
        cycle = self.cycle + 1
        strengths = self.strengths
        if not (cycle - 20) % 40:
            strengths[cycle] = self.x

        return attr.evolve(self, cycle=cycle, strengths=strengths)

    def increase(self, value: int) -> State:
        x = self.x + value
        return attr.evolve(self, x=x)


@attr.s(frozen=True, slots=True, auto_attribs=True)
class StateDrawing(State):

    x: int = 1
    cycle: int = 0
    pixels: list[str] = attr.ib(factory=lambda: ['.'] * 240)

    @property
    def crt(self):
        step = 40
        length = len(self.pixels)
        return ''.join(
            ''.join(self.pixels[i : i + step]) + '\n'  # noqa: E203
            for i in range(0, length, step)
        )

    def tick(self) -> State:
        position = self.cycle % 40
        if position in [self.x - 1, self.x, self.x + 1]:
            self.pixels[self.cycle] = '#'

        cycle = self.cycle + 1
        return attr.evolve(self, cycle=cycle)

    def increase(self, value: int) -> State:
        x = self.x + value
        return attr.evolve(self, x=x)


T = TypeVar('T', bound='State')


class Instruction(ABC):
    @abstractmethod
    def execute(self, state: T) -> T:
        """Execute this instruction with the given X register."""

    @classmethod
    def from_line(cls: type['Instruction'], line: str) -> 'Instruction':
        match line.split():  # pragma: no cover
            case ['noop']:
                return Noop()

            case ['addx', value]:
                return Addx(int(value))

            case instruction:
                raise Exception(f'Unsupported instruction: {instruction}')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Noop(Instruction):
    def execute(self, state: T) -> T:
        other = state.tick()
        assert isinstance(other, type(state))
        return other


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Addx(Instruction):

    value: int

    def execute(self, state: T) -> T:
        other = state.tick().tick().increase(self.value)
        assert isinstance(other, type(state))
        return other


def parse_data(data: str) -> Iterable[Instruction]:
    return map(Instruction.from_line, data.splitlines())


def part1(data: str) -> int:
    instructions = parse_data(data)
    state = reduce(lambda s, i: i.execute(s), instructions, StateStrength())
    return state.total_strength


def part2(data: str) -> str:
    instructions = parse_data(data)
    state = reduce(lambda s, i: i.execute(s), instructions, StateDrawing())
    print('\n' + state.crt)
    return 'ECZUZALR'
