"""Day 7."""

from abc import ABC, abstractmethod
from typing import Iterable, Iterator

import attr


class Node(ABC):
    @property
    @abstractmethod
    def size(self) -> int:
        """Size of node."""


@attr.s(frozen=True, slots=True, auto_attribs=True)
class File(Node):

    size: int


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Directory(Node, Iterable[Node]):

    name: str = '/'
    nodes: dict[str, Node] = attr.ib(
        default=attr.Factory(lambda self: {'..': self}, takes_self=True)
    )

    def __iter__(self) -> Iterator[Node]:
        return (node for name, node in self.nodes.items() if name != '..')

    @property
    def parent(self) -> 'Directory':
        parent = self.nodes['..']
        assert isinstance(parent, Directory)
        return parent

    @property
    def root(self) -> 'Directory':
        return self if self == self.parent else self.parent.root

    @property
    def size(self) -> int:
        return sum(node.size for node in self)

    def mknode(self, name: str, node: Node) -> Node:
        assert name not in self.nodes
        self.nodes[name] = node
        return node

    def mkfile(self, name: str, size: int) -> File:
        node = self.mknode(name, File(size))
        assert isinstance(node, File)
        return node

    def mkdir(self, name: str) -> 'Directory':
        node = self.mknode(name, Directory(name, {'..': self}))
        assert isinstance(node, Directory)
        return node

    def cd(self, name: str) -> 'Directory':
        if name == '/':
            return self.root

        subdir = self.nodes[name]
        assert isinstance(subdir, Directory)

        return subdir


def flatten(directory: Directory) -> Iterable[Directory]:
    dirs = [directory]
    for node in directory:
        if isinstance(node, Directory):
            dirs.extend(flatten(node))
    return dirs


def parse_data(data: str) -> Directory:
    root = cwd = Directory()
    for line in data.splitlines():  # pragma: no cover
        match line.split():  # noqa: E999
            case ['$', 'cd', name]:
                cwd = cwd.cd(name)
            case ['$', 'ls']:
                pass
            case ['dir', name]:
                cwd.mkdir(name)
            case [size, name]:
                cwd.mkfile(name, int(size))

    return root


def part1(data: str) -> int:
    root = parse_data(data)
    sizes = (d.size for d in flatten(root))
    result = sum(size for size in sizes if size <= 100_000)
    return result


def part2(data: str) -> int:
    root = parse_data(data)
    total_size = root.size
    unused_size = 70_000_000 - total_size
    required_size = 30_000_000 - unused_size
    sizes = (d.size for d in flatten(root))
    result = min(size for size in sizes if size > required_size)
    return result
