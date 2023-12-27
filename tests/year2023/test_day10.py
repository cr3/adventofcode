'''Unit tests for year 2024, day 10.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day10 import (
    PIPES,
    D,
    Grid,
    Tile,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'pipe, direction, expected',
    [
        (PIPES['|'], D.NORTH, True),
        (PIPES['|'], D.SOUTH, True),
        (PIPES['|'], D.EAST, False),
        (PIPES['|'], D.WEST, False),
    ],
)
def test_pipe_contains(pipe, direction, expected):
    result = direction in pipe
    assert result is expected


@pytest.mark.parametrize(
    'c, expected',
    [
        ('|', False),
        ('-', False),
        ('L', False),
        ('J', False),
        ('7', False),
        ('F', False),
        ('.', False),
        ('S', True),
    ],
)
def test_pipe_is_start(c, expected):
    result = PIPES[c].is_start
    assert result is expected


@pytest.mark.parametrize(
    'tile, other, expected',
    [
        (Tile(0, 0, PIPES['|']), Tile(1, 0, PIPES['|']), True),
        (Tile(0, 0, PIPES['|']), Tile(1, 0, PIPES['J']), True),
        (Tile(0, 0, PIPES['|']), Tile(1, 0, PIPES['L']), True),
        (Tile(1, 0, PIPES['|']), Tile(0, 0, PIPES['7']), True),
        (Tile(1, 0, PIPES['|']), Tile(0, 0, PIPES['F']), True),
        (Tile(0, 0, PIPES['|']), Tile(0, 1, PIPES['|']), False),
        (Tile(0, 0, PIPES['-']), Tile(0, 1, PIPES['-']), True),
        (Tile(0, 0, PIPES['-']), Tile(0, 1, PIPES['J']), True),
        (Tile(0, 0, PIPES['-']), Tile(0, 1, PIPES['7']), True),
        (Tile(0, 1, PIPES['-']), Tile(0, 0, PIPES['L']), True),
        (Tile(0, 1, PIPES['-']), Tile(0, 0, PIPES['F']), True),
        (Tile(0, 0, PIPES['-']), Tile(1, 0, PIPES['-']), False),
    ],
)
def test_tile_is_connected(tile, other, expected):
    result = tile.is_connected(other)
    assert result is expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ('S', Tile(0, 0, PIPES['S'])),
        ('.S\n..', Tile(0, 1, PIPES['S'])),
        ('..\n.S', Tile(1, 1, PIPES['S'])),
    ],
)
def test_grid_start(data, expected):
    result = Grid.from_data(data).start()
    assert result == expected


def test_grid_start_error():
    grid = Grid.from_data('.')
    with pytest.raises(ValueError):
        grid.start()


@pytest.mark.parametrize(
    'data, tile, expected',
    [
        ('.', Tile(0, 0), []),
        ('..', Tile(0, 0), [Tile(0, 1)]),
        ('..\n..', Tile(0, 0), [Tile(0, 1), Tile(1, 0)]),
        ('..\n..', Tile(1, 1), [Tile(0, 1), Tile(1, 0)]),
        (
            '...\n...\n...',
            Tile(1, 1),
            [Tile(0, 1), Tile(1, 0), Tile(1, 2), Tile(2, 1)],
        ),
    ],
)
def test_grid_surroundings(data, tile, expected):
    grid = Grid.from_data(data)
    result = list(grid.surroundings(tile))
    assert result == expected


def test_part1():
    result = part1(dedent('''\
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...
        '''))
    assert result == 8


@pytest.mark.parametrize(
    'data, expected',
    [
        (
            dedent('''\
            ...........
            .S-------7.
            .|F-----7|.
            .||.....||.
            .||.....||.
            .|L-7.F-J|.
            .|..|.|..|.
            .L--J.L--J.
            ...........
            '''),
            4,
        ),
        (
            dedent('''\
            ..........
            .S------7.
            .|F----7|.
            .||....||.
            .||....||.
            .|L-7F-J|.
            .|..||..|.
            .L--JL--J.
            ..........
            '''),
            4,
        ),
        (
            dedent('''\
            .F----7F7F7F7F-7....
            .|F--7||||||||FJ....
            .||.FJ||||||||L7....
            FJL7L7LJLJ||LJ.L-7..
            L--J.L7...LJS7F-7L7.
            ....F-J..F7FJ|L7L7L7
            ....L7.F7||L7|.L7L7|
            .....|FJLJ|FJ|F7|.LJ
            ....FJL-7.||.||||...
            ....L---J.LJ.LJLJ...
            '''),
            8,
        ),
        (
            dedent('''\
            FF7FSF7F7F7F7F7F---7
            L|LJ||||||||||||F--J
            FL-7LJLJ||||||LJL-77
            F--JF--7||LJLJ7F7FJ-
            L---JF-JLJ.||-FJLJJ7
            |F|F-JF---7F7-L7L|7|
            |FFJF7L7F-JF7|JL---7
            7-L-JL7||F7|L7F-7F7|
            L.L7LFJ|||||FJL7||LJ
            L7JLJL-JLJLJL--JLJ.L
            '''),
            10,
        ),
    ],
)
def test_part2(data, expected):
    result = part2(data)
    assert result == expected
