"""Day 9."""

from itertools import pairwise, starmap


class History(list):
    @classmethod
    def from_string(cls, string: str) -> 'History':
        sequence = map(int, string.split())
        return cls(sequence)

    def diffs(self) -> 'History':
        sequence = starmap(lambda a, b: b - a, pairwise(self))
        return History(sequence)

    def is_zero(self) -> bool:
        return not any(self)

    def forward(self) -> int:
        next_history = self.diffs()
        if next_history.is_zero():
            return self[-1]
        else:
            return self[-1] + next_history.forward()

    def backward(self) -> int:
        next_history = self.diffs()
        if next_history.is_zero():
            return self[0]
        else:
            return self[0] - next_history.backward()


def part1(data: str) -> int:
    histories = [History.from_string(s) for s in data.splitlines()]
    total = sum(h.forward() for h in histories)
    return total


def part2(data: str) -> int:
    histories = [History.from_string(s) for s in data.splitlines()]
    total = sum(h.backward() for h in histories)
    return total
