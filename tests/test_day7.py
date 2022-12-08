"""Unit tests for day 7."""

from textwrap import dedent

import pytest

from adventofcode.day7 import (
    Directory,
    flatten,
    parse_data,
    part1,
)


@pytest.mark.parametrize('directory, expected', [
    (Directory(), '/'),
    (Directory().cd('..'), '/'),
    (Directory().cd('a'), 'a'),
    (Directory().cd('a').cd('..'), '/'),
    (Directory().cd('a').cd('b').cd('..'), 'a'),
    (Directory().cd('a').cd('b').cd('/'), '/'),
])
def test_directory_cd(directory, expected):
    assert directory.name == expected


@pytest.mark.parametrize('root, expected', [
    (Directory(), ['/']),
    (Directory().cd('a').cd('/'), ['/', 'a']),
    (Directory().cd('a').cd('b').cd('/'), ['/', 'a', 'b']),
    (Directory().cd('a').cd('..').cd('b').cd('/'), ['/', 'a', 'b']),
])
def test_flatten(root, expected):
    result = flatten(root)
    assert [r.name for r in result] == expected


def test_parse_data():
    root = parse_data(dedent("""\
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
    """))
    names = [d.name for d in flatten(root)]
    assert names == ['/', 'a', 'e', 'd']


def test_part1(capsys):
    result = part1(dedent("""\
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
    """))
    captured = capsys.readouterr()
    result = captured.out
    assert result == '95437\n'
