"""Unit tests for year 2022, day 11."""

from textwrap import dedent

from adventofcode.year2022.day11 import (
    Monkey,
    parse_data,
    part1,
    part2,
)


def test_monkey_init():
    monkey = Monkey()
    assert monkey.counter == 0
    assert monkey.items == []
    assert monkey.operation(1) == 1
    assert monkey.test(1) == 1


def test_monkey_from_block():
    monkey = Monkey.from_block(dedent("""\
            Monkey 0:
              Starting items: 79, 98
              Operation: new = old * 19
              Test: divisible by 23
                If true: throw to monkey 2
                If false: throw to monkey 3
            """))
    assert monkey.items == [79, 98]
    assert monkey.operation(2) == 38
    assert monkey.test(22) == 3
    assert monkey.test(23) == 2
    assert monkey.test(24) == 3


def test_monkey_inspect():
    monkey = Monkey(
        items=[79, 98],
        operation=lambda old: old * 19,
        test=lambda level: 3 if level % 23 else 2,
    )
    monkeys = monkey.inspect([Monkey() for _ in range(4)])

    assert monkey.counter == 2
    assert monkeys[3] == Monkey(items=[500, 620])


def test_monkeys_inspect():
    monkeys = parse_data(DATA).inspect(1)
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []


def test_parse_data():
    result = parse_data(DATA)
    assert len(result) == 4


def test_part1():
    result = part1(DATA)
    assert result == 10_605


def test_part2():
    result = part2(DATA)
    assert result == 2_713_310_158


DATA = dedent("""\
    Monkey 0:
      Starting items: 79, 98
      Operation: new = old * 19
      Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3

    Monkey 1:
      Starting items: 54, 65, 75, 74
      Operation: new = old + 6
      Test: divisible by 19
        If true: throw to monkey 2
        If false: throw to monkey 0

    Monkey 2:
      Starting items: 79, 60, 97
      Operation: new = old * old
      Test: divisible by 13
        If true: throw to monkey 1
        If false: throw to monkey 3

    Monkey 3:
      Starting items: 74
      Operation: new = old + 3
      Test: divisible by 17
        If true: throw to monkey 0
        If false: throw to monkey 1
    """)
