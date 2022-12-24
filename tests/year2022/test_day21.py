"""Unit tests for year 2022, day 21."""

from textwrap import dedent

import pytest

from adventofcode.year2022.day21 import (
    ME,
    eval_monkey,
    listens_to_me,
    my_value,
    parse_data,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'name, monkeys, expected',
    [
        ('foo', {'foo': '1'}, 1),
        ('foo', {'foo': 'bar', 'bar': '1'}, 1),
        ('foo', {'foo': 'bar + baz', 'bar': '1', 'baz': '2'}, 3),
    ],
)
def test_eval_monkey(name, monkeys, expected):
    result = eval_monkey(name, monkeys)
    assert result == expected


@pytest.mark.parametrize(
    'name, monkeys, expected',
    [
        ('foo', {'foo': '1'}, False),
        ('foo', {'foo': ME}, True),
    ],
)
def test_listens_to_me(name, monkeys, expected):
    result = listens_to_me(name, monkeys)
    assert result == expected


@pytest.mark.parametrize(
    'name, value, monkeys, expected',
    [
        ('foo', 1, {'foo': ME}, 1),
        ('foo', 3, {'foo': f'{ME} + 1'}, 2),
    ],
)
def test_my_value(name, value, monkeys, expected):
    result = my_value(name, value, 10, monkeys)
    assert result == expected


def test_my_value_error():
    with pytest.raises(Exception):
        my_value('foo', 2, 10, {'foo': '1'})


def test_parse_data():
    result = parse_data(DATA)
    assert result['root'] == 'pppw + sjmn'


def test_part1():
    result = part1(DATA)
    assert result == 152


def test_part2():
    result = part2(DATA, 10)
    assert result == 301


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
