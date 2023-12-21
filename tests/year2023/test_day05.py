'''Unit tests for year 2023, day 5.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day05 import (
    Map,
    Range,
    Seeds,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'string, expected',
    [
        ('0 0 0', Range(0, 0, 0)),
        ('1 2 3', Range(1, 2, 3)),
    ],
)
def test_range_from_string(string, expected):
    r = Range.from_string(string)
    assert r == expected


@pytest.mark.parametrize(
    'r, value, expected',
    [
        (Range(0, 0, 1), 0, True),
        (Range(0, 1, 1), 0, False),
    ],
)
def test_range_is_within(r, value, expected):
    result = r.is_within(value)
    assert result is expected


@pytest.mark.parametrize(
    'string, expected',
    [
        ('a-to-b map:', Map('a', 'b', [])),
        ('a-to-b map:\n0 0 0', Map('a', 'b', [Range(0, 0, 0)])),
        (
            'a-to-b map:\n0 0 0\n1 2 3',
            Map('a', 'b', [Range(0, 0, 0), Range(1, 2, 3)]),
        ),
    ],
)
def test_map_from_string(string, expected):
    m = Map.from_string(string)
    assert m == expected


def test_map_from_string_error():
    with pytest.raises(ValueError):
        Map.from_string("")


@pytest.mark.parametrize(
    'm, value, expected',
    [
        (Map('', '', [Range(0, 0, 1)]), 0, 0),
        (Map('', '', [Range(1, 0, 1)]), 0, 1),
        (Map('', '', [Range(1, 1, 1)]), 0, 0),
    ],
)
def test_map_convert(m, value, expected):
    result = m.convert(value)
    assert result == expected


@pytest.mark.parametrize(
    'string, expected',
    [
        ('seeds: ', Seeds()),
        ('seeds: 1', Seeds([1])),
        ('seeds: 1 2', Seeds([1, 2])),
    ],
)
def test_seeds_from_string(string, expected):
    m = Seeds.from_string(string)
    assert m == expected


def test_seeds_from_string_error():
    with pytest.raises(ValueError):
        Seeds.from_string("")


def test_part1():
    result = part1(dedent('''\
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
        '''))
    assert result == 35


def test_part2():
    result = part2(dedent('''\
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
        '''))
    assert result == 0
