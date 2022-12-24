"""Day 21."""

from collections import UserDict


ME = 'humn'

Monkeys = dict[str, str]


class Locals(UserDict):
    def __getitem__(self, key):
        return eval(super().__getitem__(key), {}, self)


def eval_monkey(name: str, monkeys: Monkeys) -> int:
    return int(eval(monkeys[name], {}, Locals(monkeys)))


def listens_to_me(name: str, monkeys: Monkeys) -> bool:
    a = eval_monkey(name, {**monkeys, ME: '0'})
    b = eval_monkey(name, {**monkeys, ME: '100'})
    return a != b


def my_value(monkey: str, value: int, step: int, monkeys: Monkeys) -> int:
    attempt1 = 0
    result1 = eval_monkey(monkey, {**monkeys, ME: str(attempt1)})
    for _ in range(100):
        attempt2 = attempt1 + step
        result2 = eval_monkey(monkey, {**monkeys, ME: str(attempt2)})
        if result2 == value:
            return attempt2

        if (result2 > result1 and result2 > value) or (
            result2 < result1 and result2 < value
        ):
            step = -(step - int(step / 2))

        attempt1, result1 = attempt2, result2

    raise Exception('Not found')


def parse_data(data: str) -> dict[str, str]:
    return dict(line.split(': ') for line in data.splitlines())


def part1(data: str) -> int:
    monkeys = parse_data(data)
    return eval_monkey('root', monkeys)


def part2(data: str, step: int = 2**40) -> int:
    monkeys = parse_data(data)
    left, _, right = monkeys['root'].split()
    listen_monkey = left if listens_to_me(left, monkeys) else right
    target_monkey = left if listen_monkey == right else right
    target_value = eval_monkey(target_monkey, monkeys)
    return my_value(listen_monkey, target_value, step, monkeys)
