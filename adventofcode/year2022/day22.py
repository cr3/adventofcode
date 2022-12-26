"""Day 22."""

import re
from enum import Enum, IntEnum
from typing import Union

import attr

Facing = IntEnum('Facing', {'R': 0, 'D': 1, 'L': 2, 'U': 3})
Motion = Enum('Motion', {'R': 1, 'L': -1})

Move = Union[Motion, int]
Moves = list[Move]


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Cursor:
    x: int = 0
    y: int = 0
    facing: Facing = Facing.R

    def rotate(self, motion: Motion) -> 'Cursor':
        facing = (self.facing + motion.value) % len(Facing)
        return attr.evolve(self, facing=Facing(facing))

    def move(self) -> 'Cursor':
        kwargs = {
            Facing.R: {'x': self.x + 1},
            Facing.D: {'y': self.y + 1},
            Facing.L: {'x': self.x - 1},
            Facing.U: {'y': self.y - 1},
        }[self.facing]
        return attr.evolve(self, **kwargs)

    def mod(self, height: int, width: int) -> 'Cursor':
        x = self.x % width
        y = self.y % height
        return attr.evolve(self, x=x, y=y)


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Board:
    lines: list[str]

    @classmethod
    def from_block(cls: type['Board'], block: str) -> 'Board':
        lines = block.splitlines()
        max_len = max(map(len, lines))
        return cls([line + ' ' * (max_len - len(line)) for line in lines])

    @property
    def height(self):
        return len(self.lines)

    @property
    def width(self):
        return len(self.lines[0])

    def begin(self) -> Cursor:
        x = self.lines[0].index('.')
        return Cursor(x=x)

    def at(self, cursor) -> str:
        return self.lines[cursor.y][cursor.x]

    def next(self, cursor: Cursor):
        next_cursor = cursor.move().mod(self.height, self.width)
        c = self.at(next_cursor)
        if c == '.':
            return next_cursor
        elif c == '#':
            raise KeyError
        else:
            return self.next(next_cursor)

    def move(self, cursor: Cursor, move: Move) -> Cursor:
        if isinstance(move, int):
            for _ in range(move):
                try:
                    next_cursor = self.next(cursor)
                except KeyError:
                    break
                else:
                    cursor = next_cursor
        else:
            cursor = cursor.rotate(move)

        return cursor


def parse_line(line: str) -> Moves:
    return [
        Motion[c] if c in Motion._member_names_ else int(c)
        for c in re.findall(r'\d+|L|R', line)
    ]


def parse_data(data: str) -> tuple[Board, Moves]:
    block, line = data.split('\n\n')
    return Board.from_block(block), parse_line(line)


def part1(data: str) -> int:
    board, moves = parse_data(data)
    cursor = board.begin()
    for move in moves:
        cursor = board.move(cursor, move)

    return 1000 * (cursor.y + 1) + 4 * (cursor.x + 1) + cursor.facing


def part2(data: str) -> int:
    parse_data(data)
    return 0
