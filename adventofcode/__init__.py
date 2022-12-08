import importlib


def solve(year, day, data):
    module_name = f'adventofcode.year{year}.day{day}'
    module = importlib.import_module(module_name)
    part1 = module.part1(data)
    part2 = module.part2(data)
    return part1, part2
