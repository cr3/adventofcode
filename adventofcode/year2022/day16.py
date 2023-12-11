"""Day 16."""

import re
from collections import UserDict
from collections.abc import Iterable
from functools import cached_property
from itertools import combinations, permutations
from math import inf

import attr


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Valve:
    name: str
    rate: int
    tunnels: list[str]

    @classmethod
    def from_line(cls: type['Valve'], line: str):
        match = re.match(
            r'Valve (?P<name>[A-Z]{2}) has flow rate=(?P<rate>\d+); '
            r'tunnels? leads? to valves? (?P<tunnels>.+)',
            line,
        )
        assert match
        return cls(
            match['name'],
            int(match['rate']),
            match['tunnels'].split(', '),
        )


Answer = dict[int, int]


class Graph(UserDict):
    @classmethod
    def from_valves(cls: type['Graph'], valves: Iterable[Valve]):
        return cls({v.name: v for v in valves})

    @cached_property
    def steps(self):
        s = {
            (x, y): 1 if y in self[x].tunnels else inf
            for x, y in permutations(self, 2)
        }
        for k, x, y in permutations(self, 3):
            s[x, y] = min(s[x, y], s[x, k] + s[k, y])

        return s

    @cached_property
    def states(self):
        return {name: 1 << i for i, name in enumerate(self)}

    def travel(
        self,
        parent: str,
        minutes: int,
        state: int,
        rate: int,
        answer: Answer,
    ) -> Answer:
        answer[state] = max(answer.get(state, 0), rate)
        for name, valve in self.items():
            if valve.rate and parent != name:
                remaining = minutes - self.steps[parent, name] - 1
                if not (self.states[name] & state) and (remaining > 0):
                    self.travel(
                        name,
                        remaining,
                        self.states[name] | state,
                        rate + remaining * valve.rate,
                        answer,
                    )

        return answer


def parse_data(data: str) -> Graph:
    return Graph.from_valves(map(Valve.from_line, data.splitlines()))


def part1(data: str) -> int:
    graph = parse_data(data)
    answer = graph.travel('AA', 30, 0, 0, {})
    return max(answer.values())


def part2(data: str) -> int:
    graph = parse_data(data)
    answer = graph.travel('AA', 26, 0, 0, {})
    return max(
        v1 + v2
        for (k1, v1), (k2, v2) in combinations(answer.items(), 2)
        if not k1 & k2
    )
