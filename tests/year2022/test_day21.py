"""Unit tests for year 2022, day 21."""

from textwrap import dedent

from adventofcode.year2022.day21 import (
    parse_data,
    part1,
    part2,
)


def test_parse_data():
    result = parse_data(DATA)
    assert result['root'] == 'pppw + sjmn'


def test_part1():
    result = part1(DATA)
    assert result == 152


def test_part2():
    result = part2(DATA)
    assert result == 0


DATA = dedent(
    """\
    root: pppw + sjmn
    dbpl: 5
    cczh: sllz + lgvd
    zczc: 2
    ptdq: humn - dvpt
    dvpt: 3
    lfqf: 4
    humn: 5
    ljgn: 2
    sjmn: drzm * dbpl
    sllz: 4
    pppw: cczh / lfqf
    lgvd: ljgn * ptdq
    drzm: hmdt - zczc
    hmdt: 32
    """,
)
