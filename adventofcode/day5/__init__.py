"""Day 5."""

import re
from collections.abc import Mapping
from pathlib import Path
from typing import Iterable, Tuple, Type, TypeVar

import attr


INPUT = Path(__file__).parent / 'input.txt'


MoveType = TypeVar('MoveType', bound='Move')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Move:

    n: int
    src: int
    dst: int

    @classmethod
    def parse(cls: Type[MoveType], procedure: str) -> MoveType:
        match = re.match(r'move (\d+) from (\d+) to (\d+)', procedure)
        return cls(*map(int, match.groups()))  # type: ignore


StacksType = TypeVar('StacksType', bound='Stacks')


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Stacks(Mapping):

    stacks: list[list[str]]

    def __getitem__(self, index: int) -> list[str]:
        # 1-based index
        return self.stacks[index - 1]

    def __iter__(self):
        return iter(range(1, len(self.stacks) + 1))

    def __len__(self) -> int:
        return len(self.stacks)

    def rearrange(self, move: Move) -> None:
        for _ in range(move.n):
            crate = self[move.src].pop()
            self[move.dst].append(crate)

    @classmethod
    def parse(cls: Type[StacksType], drawing: str) -> StacksType:
        lines = filter(None, reversed(drawing.split('\n')))
        n = len(re.findall(r'\d+', next(lines)))
        pattern = re.compile(' ?'.join([r'(?:\[(\w)\]|   )?'] * n))
        rows = [pattern.match(line).groups() for line in lines]  # type: ignore
        cols: list[list[str]] = [list(filter(None, col)) for col in zip(*rows)]
        return cls(cols)


def parse_input(path: Path) -> Tuple[Stacks, Iterable[Move]]:
    with path.open() as stream:
        drawing = []
        while True:
            line = stream.readline()
            if line == '\n':
                break

            drawing.append(line)

        stacks = Stacks.parse(''.join(drawing))
        moves = map(Move.parse, stream.readlines())

        return stacks, moves


def part1(path: Path = INPUT) -> None:
    stacks, moves = parse_input(path)
    for move in moves:
        stacks.rearrange(move)
    result = ''.join(stack[-1] for stack in stacks.values())
    print(result)
