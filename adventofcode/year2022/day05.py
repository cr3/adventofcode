"""Day 5."""

import re
from collections.abc import Iterable, Mapping
from typing import TypeVar

from attrs import define

MoveType = TypeVar('MoveType', bound='Move')


@define(frozen=True)
class Move:
    n: int
    src: int
    dst: int

    @classmethod
    def parse(cls: type[MoveType], procedure: str) -> MoveType:
        match = re.match(r'move (\d+) from (\d+) to (\d+)', procedure)
        return cls(*map(int, match.groups()))  # type: ignore


StacksType = TypeVar('StacksType', bound='Stacks')


@define(frozen=True)
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

    def rearrange_multiple(self, move: Move) -> None:
        i = -move.n
        crates = self[move.src][i:]
        del self[move.src][i:]
        self[move.dst].extend(crates)

    @classmethod
    def parse(cls: type[StacksType], drawing: str) -> StacksType:
        lines = filter(None, reversed(drawing.split('\n')))
        n = len(re.findall(r'\d+', next(lines)))
        pattern = re.compile(' ?'.join([r'(?:\[(\w)\]|   )?'] * n))
        rows = [pattern.match(line).groups() for line in lines]  # type: ignore
        cols: list[list[str]] = [list(filter(None, col)) for col in zip(*rows)]
        return cls(cols)


def parse_data(data: str) -> tuple[Stacks, Iterable[Move]]:
    drawing = []
    lines = iter(data.splitlines())
    for line in lines:  # pragma: no cover
        if line == '':
            break

        drawing.append(line)

    stacks = Stacks.parse('\n'.join(drawing))
    moves = map(Move.parse, lines)

    return stacks, moves


def part1(data: str) -> str:
    stacks, moves = parse_data(data)
    for move in moves:
        stacks.rearrange(move)
    result = ''.join(stack[-1] for stack in stacks.values())
    return result


def part2(data: str) -> str:
    stacks, moves = parse_data(data)
    for move in moves:
        stacks.rearrange_multiple(move)
    result = ''.join(stack[-1] for stack in stacks.values())
    return result
