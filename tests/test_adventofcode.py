"""Tests for the adventofcode module."""

from adventofcode import solve


def test_solve():
    result = solve(2022, 1, '1\n2\n\n3\n4\n')
    assert result == (7, 10)
