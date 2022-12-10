"""Unit tests for year 2022, day 7."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day7 import (
    Directory,
    flatten,
    parse_data,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'directory, expected',
    [
        (Directory(), '/'),
        (Directory().cd('..'), '/'),
        (Directory().mkdir('a'), 'a'),
        (Directory().mkdir('a').cd('..'), '/'),
        (Directory().mkdir('a').mkdir('b').cd('..'), 'a'),
        (Directory().mkdir('a').mkdir('b').cd('/'), '/'),
    ],
)
def test_directory_cd(directory, expected):
    assert directory.name == expected


@pytest.mark.parametrize(
    'root, expected',
    [
        (Directory(), ['/']),
        (Directory().mkdir('a').cd('/'), ['/', 'a']),
        (Directory().mkdir('a').mkdir('b').cd('/'), ['/', 'a', 'b']),
        (Directory().mkdir('a').cd('..').mkdir('b').cd('/'), ['/', 'a', 'b']),
    ],
)
def test_flatten(root, expected):
    result = flatten(root)
    assert [r.name for r in result] == expected


def test_parse_data():
    root = parse_data(
        dedent(
            """\
        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
    """
        )
    )
    names = [d.name for d in flatten(root)]
    assert names == ['/', 'a', 'e', 'd']


def test_part1():
    result = part1(
        dedent(
            """\
        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
    """
        )
    )
    assert result == 95_437


def test_part2():
    result = part2(
        dedent(
            """\
        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
    """
        )
    )
    assert result == 24_933_642
