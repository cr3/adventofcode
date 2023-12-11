"""Day 19.

https://nirlipo.github.io/Width-Based-Planning-Resources/
"""

import re
from collections.abc import Iterable
from functools import reduce
from itertools import combinations, islice
from operator import mul
from typing import Literal, Optional

import attr

Material = Literal['ore', 'clay', 'obsidian', 'geode']
Bots = dict[Material, int]
Resources = dict[Material, int]
Costs = dict[Material, Resources]

MATERIALS: list[Material] = ['ore', 'clay', 'obsidian', 'geode']


@attr.s(frozen=True, slots=True, auto_attribs=True)
class State:
    minutes: int
    bots: Bots = attr.ib(factory=dict)
    resources: Resources = attr.ib(factory=dict)
    building: Material | None = None

    @property
    def atoms(self) -> Iterable[str]:
        atoms = [
            f'minutes={self.minutes}',
            *[f'{m}={self.resources.get(m, 0)}' for m in MATERIALS],
            *[f'bot-{m}={self.bots.get(m, 0)}' for m in MATERIALS],
        ]
        if self.building:
            atoms.append(f'bot-{self.building}=1')

        return atoms

    def tick(self) -> 'State':
        minutes = self.minutes - 1
        resources = {
            m: self.resources.get(m, 0) + self.bots.get(m, 0)
            for m in MATERIALS
        }
        bots = self.bots.copy()
        if self.building:
            bots[self.building] = bots.get(self.building, 0) + 1

        return attr.evolve(
            self,
            minutes=minutes,
            bots=bots,
            resources=resources,
            building=None,
        )

    def buy(self, name: Material, costs: Costs) -> Optional['State']:
        cost = costs.get(name, {})
        minutes_limit = cost.get('ore', 0) + 1 if name == 'ore' else 1
        max_cost = (
            float('inf')
            if name == 'geode'
            else max(c.get(name, 0) for c in costs.values())
        )
        if (
            self.minutes <= minutes_limit
            or any(v > self.resources.get(k, 0) for k, v in cost.items())
            or self.bots.get(name, 0) >= max_cost
        ):
            return None

        resources = {
            **self.resources,
            **{k: self.resources[k] - cost[k] for k, v in cost.items()},
        }
        return attr.evolve(self, resources=resources, building=name)

    def prune(self, atoms: set[int], width: int) -> Optional['State']:
        prune = True
        for pairs in combinations(self.atoms, width):
            atom = hash(pairs)
            if atom not in atoms:
                prune = False
                atoms.add(atom)

        if prune:
            return None

        return self


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Blueprint:
    num: int
    costs: Costs

    @classmethod
    def from_line(cls: type['Blueprint'], line: str) -> 'Blueprint':
        (
            num,
            ore_ores,
            clay_ores,
            obsidian_ores,
            obsidian_clays,
            geode_ores,
            geode_obsidians,
        ) = map(int, re.findall(r'\d+', line))
        return cls(
            num,
            {
                'ore': {'ore': ore_ores},
                'clay': {'ore': clay_ores},
                'obsidian': {'ore': obsidian_ores, 'clay': obsidian_clays},
                'geode': {'ore': geode_ores, 'obsidian': geode_obsidians},
            },
        )

    def calculate(self, minutes: int, width: int):
        best = 0
        atoms: set[int] = set()
        state = State(
            minutes,
            {'ore': 1},
        )
        queue = [state]
        while queue:
            state = queue.pop(0)
            if state.minutes == 0:
                best = max(best, state.resources.get('geode', 0))
                continue

            next_state = state.tick()
            materials = reversed(MATERIALS)
            if buy_state := next_state.buy(next(materials), self.costs):
                if novel := buy_state.prune(atoms, width):
                    queue.append(novel)
            else:
                for material in materials:
                    if buy_state := next_state.buy(material, self.costs):
                        novel = buy_state.prune(atoms, width)
                        if novel:
                            queue.append(novel)

                if novel := next_state.prune(atoms, width):
                    queue.append(novel)

        return best

    def evaluate(self, minutes: int) -> int:
        result = -1
        for width in range(1, 4):  # pragma: no cover
            current = self.calculate(minutes, width)
            if current == result:
                break
            result = current

        return result


def parse_data(data: str) -> Iterable[Blueprint]:
    return map(Blueprint.from_line, data.splitlines())


def part1(data: str) -> int:
    blueprints = parse_data(data)
    return sum(bp.num * bp.evaluate(24) for bp in blueprints)


def part2(data: str) -> int:
    blueprints = parse_data(data)
    return reduce(mul, (bp.evaluate(32) for bp in islice(blueprints, 3)), 1)
