'''Unit tests for year 2023, day 2.'''

from textwrap import dedent

import pytest

from adventofcode.year2023.day02 import (
    Game,
    Play,
    part1,
    part2,
)


@pytest.mark.parametrize(
    'string, expected',
    [
        ('1 blue', Play(blue=1)),
        ('1 green', Play(green=1)),
        ('1 red', Play(red=1)),
        ('1 blue, 2 green', Play(blue=1, green=2)),
        ('1 blue, 2 green, 3 red', Play(blue=1, green=2, red=3)),
    ],
)
def test_play_from_string(string, expected):
    result = Play.from_string(string)
    assert result == expected


@pytest.mark.parametrize(
    'play, other, expected',
    [
        (Play(), Play(blue=1), True),
        (Play(blue=1), Play(blue=1), True),
        (Play(blue=2), Play(blue=1), False),
    ],
)
def test_play_le(play, other, expected):
    result = play <= other
    assert result is expected


@pytest.mark.parametrize(
    'play, expected',
    [
        (Play(blue=1), 1),
        (Play(blue=2), 2),
        (Play(blue=2, green=3), 6),
        (Play(blue=2, green=3, red=4), 24),
    ],
)
def test_play_product(play, expected):
    result = play.product
    assert result is expected


@pytest.mark.parametrize(
    'line, expected',
    [
        (
            'Game 1: 1 blue',
            Game(1, [Play(blue=1)]),
        ),
        (
            'Game 2: 1 blue; 1 red',
            Game(2, [Play(blue=1), Play(red=1)]),
        ),
        (
            'Game 10: 1 blue, 1 red; 2 red',
            Game(10, [Play(blue=1, red=1), Play(red=2)]),
        ),
        (
            'Game 1: 1 blue; 2 blue, 2 red',
            Game(1, [Play(blue=1), Play(blue=2, red=2)]),
        ),
    ],
)
def test_game_from_line(line, expected):
    result = Game.from_line(line)
    assert result == expected


def test_game_from_line_error():
    with pytest.raises(ValueError):
        Game.from_line("")


@pytest.mark.parametrize(
    'game, expected',
    [
        (
            Game(1, [Play(blue=1)]),
            Play(blue=1),
        ),
    ],
)
def test_game_minimum(game, expected):
    result = game.minimum
    assert result == expected


@pytest.mark.parametrize(
    'game, limit, expected',
    [
        (Game(1, [Play()]), Play(blue=1), True),
        (Game(1, [Play(blue=1)]), Play(blue=1), True),
        (Game(1, [Play(blue=2)]), Play(blue=1), False),
        (Game(1, [Play(), Play(blue=2)]), Play(blue=1), False),
    ],
)
def test_game_is_within(game, limit, expected):
    result = game.is_within(limit)
    assert result is expected


def test_part1():
    result = part1(dedent('''\
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        '''))
    assert result == 8


def test_part2():
    result = part2(dedent('''\
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        '''))
    assert result == 2286
