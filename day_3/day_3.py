import numpy as np


class PartNumber:
    def __init__(self, row: int, slice_start: int, slice_end: int, value: int) -> None:
        self.row = row
        self.slice_start = slice_start
        self.slice_end = slice_end
        self.value = value

    def has_adjacent_symbol(self, engine_schematic: np.ndarray) -> bool:
        adjacent_characters = self._get_adjacent_characters(engine_schematic)
        print(adjacent_characters)
        return symbols_present_in_array(adjacent_characters)

    def _get_adjacent_characters(self, engine_schematic: np.ndarray) -> np.ndarray:
        column_start = max(self.slice_start - 1, 0)
        column_end = min(self.slice_end + 1, engine_schematic.shape[1]) + 1
        row_start = max(self.row - 1, 0)
        row_end = min(self.row + 1, engine_schematic.shape[0]) + 1
        return engine_schematic[row_start:row_end, column_start:column_end]


def get_part_number_sum(engine_schematic_str: str) -> int:
    engine_schematic = input_str_to_array(engine_schematic_str)
    part_numbers = find_part_numbers(engine_schematic)
    return sum([p.value for p in part_numbers if p.has_adjacent_symbol(engine_schematic)])


def input_str_to_array(input_str: str) -> np.ndarray:
    return np.array([list(row) for row in input_str.split("\n")])


def find_part_numbers(engine_schematic: np.ndarray) -> list[PartNumber]:
    schematic_width = engine_schematic.shape[1]
    schematic_height = engine_schematic.shape[0]
    print(f"{schematic_width=} {schematic_height=}")
    part_numbers: list[PartNumber] = []
    for row in range(schematic_height):
        start_index = None
        end_index = None
        for column in range(schematic_width):
            character = str(engine_schematic[row, column])
            print(row, column, character)
            if start_index is None and character.isdigit():
                print(f"found start @ {column}")
                start_index = column
            elif start_index is not None and not character.isdigit():
                print(f"found end @ {column - 1}")
                end_index = column - 1
            elif start_index is not None and column == (schematic_width - 1):
                print("found number at end of line")
                end_index = column
            if start_index is not None and end_index is not None:
                print(f"found number from {start_index}:{end_index}")
                number = PartNumber(
                    row=row,
                    slice_start=start_index,
                    slice_end=end_index,
                    value=get_part_number(engine_schematic[row, start_index:end_index + 1])
                )
                part_numbers.append(number)
                start_index = None
                end_index = None
    return part_numbers


def symbols_present_in_array(array: np.ndarray) -> bool:
    return any(
        (
            "#" in array,
            "$" in array,
            "%" in array,
            "&" in array,
            "*" in array,
            "+" in array,
            "-" in array,
            "/" in array,
            "=" in array,
            "@" in array
        )
    )


def get_part_number(array: np.ndarray) -> int:
    part_number_str = "".join(array)
    return int(part_number_str)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(sorted("".join(set(content))))
    print(get_part_number_sum(content))
