import numpy as np
import pytest

from day_3 import get_part_number_sum, PartNumber, input_str_to_array, Gear, find_gear_ratio_sum


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


class TestGear:
    def test_check_if_part_number_is_adjacent_same_row_before_gear(self):
        part_number = PartNumber(5, 2, 4, 123)
        gear = Gear(5, 5)
        assert gear.check_if_part_number_is_adjacent(part_number) is True

    def test_check_if_part_number_is_adjacent_same_row_after_gear(self):
        part_number = PartNumber(5, 6, 8, 123)
        gear = Gear(5, 5)
        assert gear.check_if_part_number_is_adjacent(part_number) is True

    @pytest.mark.parametrize("column", range(2, 7, 1))
    def test_check_if_part_number_is_adjacent_row_above_gear(self, column: int):
        part_number = PartNumber(4, column, column+2, 123)
        gear = Gear(5, 5)
        assert gear.check_if_part_number_is_adjacent(part_number) is True

    @pytest.mark.parametrize("column", range(2, 7, 1))
    def test_check_if_part_number_is_adjacent_row_below_gear(self, column: int):
        part_number = PartNumber(6, column, column+2, 123)
        gear = Gear(5, 5)
        assert gear.check_if_part_number_is_adjacent(part_number) is True

    def test_check_if_part_number_is_adjacent_false(self):
        part_number = PartNumber(1, 2, 4, 123)
        gear = Gear(5, 5)
        assert gear.check_if_part_number_is_adjacent(part_number) is False


def test_find_gear_ratio_sum():
    result = find_gear_ratio_sum(
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
    assert result == 467835
