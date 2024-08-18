import numpy as np
import pytest

from day_3 import get_part_number_sum, PartNumber, input_str_to_array


@pytest.fixture()
def engine_schematic() -> np.ndarray:
    return input_str_to_array(
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


class TestPartNumber:
    def test_has_adjacent_symbol_with_symbol(self, engine_schematic):
        part_number = PartNumber(0, 0, 2, 467)
        assert part_number.has_adjacent_symbol(engine_schematic) is True

    def test_has_adjacent_symbol_without_symbol(self, engine_schematic):
        part_number = PartNumber(0, 5, 7, 114)
        assert part_number.has_adjacent_symbol(engine_schematic) is False


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
