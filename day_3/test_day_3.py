import pytest

from day_3 import get_part_number_sum


def test_get_part_number_sum():
    result = get_part_number_sum(
        """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    )
    assert result == 4361
