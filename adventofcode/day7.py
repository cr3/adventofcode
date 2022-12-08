"""Day 7."""

import re
from abc import ABC, abstractmethod
from typing import Iterable

import attr
from aocd import get_data


DATA = get_data(day=7, year=2022)


class Node(ABC):

    @property
    @abstractmethod
    def size(self) -> int:
        """Size of node."""


@attr.s(frozen=True, slots=True, auto_attribs=True)
class File(Node):

    size: int


@attr.s(frozen=True, slots=True, auto_attribs=True)
class Directory(Node):

    name: str = '/'
    children: dict[str, Node] = attr.ib(factory=dict)
    parent: 'Directory' = attr.ib(default=attr.Factory(
        lambda self: self, takes_self=True))

    @property
    def root(self):
        return self if self == self.parent else self.parent.root

    @property
    def size(self):
        return sum(child.size for child in self.children.values())

    def mknode(self, name: str, node: Node) -> Node:
        assert name not in self.children
        self.children[name] = node
        return node

    def mkfile(self, name: str, size: int) -> File:
        node = self.mknode(name, File(size))
        assert isinstance(node, File)
        return node

    def mkdir(self, name: str) -> 'Directory':
        node = self.mknode(name, Directory(name, parent=self))
        assert isinstance(node, Directory)
        return node

    def cd(self, name: str) -> 'Directory':
        if name == '/':
            return self.root

        if name == '..':
            return self.parent

        if name not in self.children:
            return self.mkdir(name)

        subdir = self.children[name]
        assert isinstance(subdir, Directory)
        assert subdir.parent == self
        return subdir


def flatten(directory: Directory) -> Iterable[Directory]:
    dirs = [directory]
    for child in directory.children.values():
        if isinstance(child, Directory):
            dirs.extend(flatten(child))
    return dirs


def parse_data(data: str) -> Directory:
    root = cwd = Directory()
    pattern = re.compile(
        r'(\$ cd (?P<cd>(?:.+))'
        r'|\$ ls'
        r'|dir .+'
        r'|(?P<size>\d+) (?P<name>[\w\.]+))$'
    )
    for line in data.splitlines():
        match = pattern.match(line)
        assert match

        if match.group('cd'):
            cwd = cwd.cd(match.group('cd'))
        elif match.group('name'):
            cwd.mkfile(match.group('name'), int(match.group('size')))

    return root


def part1(data: str = DATA) -> None:
    root = parse_data(data)
    sizes = (d.size for d in flatten(root))
    result = sum(size for size in sizes if size <= 100000)
    print(result)
