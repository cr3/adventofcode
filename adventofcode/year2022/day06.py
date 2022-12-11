"""Day 6."""


def parse_data(data: str, size) -> int:
    buf = list(data[:size])
    for i in range(size, len(data)):
        buf[i % size] = data[i]
        if len(set(buf)) == size:
            return i + 1

    return 0


def part1(data: str) -> int:
    result = parse_data(data, 4)
    return result


def part2(data: str) -> int:
    result = parse_data(data, 14)
    return result
