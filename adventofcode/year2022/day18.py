"""Day 18."""

from collections.abc import Iterable

from attrs import define


@define(frozen=True)
class Cube:
    x: int
    y: int
    z: int

    @classmethod
    def from_line(cls: type['Cube'], line: str) -> 'Cube':
        return cls(*map(int, line.split(',')))  # type: ignore

    @property
    def neighbours(self) -> list['Cube']:
        return [
            Cube(self.x - 1, self.y, self.z),
            Cube(self.x + 1, self.y, self.z),
            Cube(self.x, self.y - 1, self.z),
            Cube(self.x, self.y + 1, self.z),
            Cube(self.x, self.y, self.z - 1),
            Cube(self.x, self.y, self.z + 1),
        ]


def parse_data(data: str) -> Iterable[Cube]:
    return map(Cube.from_line, data.splitlines())


def part1(data: str) -> int:
    cubes = list(parse_data(data))
    return 6 * len(cubes) - sum(
        n in cubes for c in cubes for n in c.neighbours
    )


def part2(data: str) -> int:
    cubes = list(parse_data(data))
    min_x, min_y, min_z = (
        min(getattr(c, attr) - 1 for c in cubes) for attr in ['x', 'y', 'z']
    )
    max_x, max_y, max_z = (
        max(getattr(c, attr) + 1 for c in cubes) for attr in ['x', 'y', 'z']
    )
    outside = set()
    queue = [Cube(min_x, min_y, min_z)]
    while queue:
        cube = queue.pop()
        outside.add(cube)
        for n in cube.neighbours:
            if (
                (min_x <= n.x <= max_x)
                and (min_y <= n.y <= max_y)
                and (min_z <= n.z <= max_z)
                and n not in cubes
                and n not in outside
            ):
                queue.append(n)

    return sum(n in outside for c in cubes for n in c.neighbours)
