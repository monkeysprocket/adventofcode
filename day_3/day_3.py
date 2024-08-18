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


class Gear:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        self.adjacent_part_numbers: list[PartNumber] = []

    def is_valid_gear(self) -> bool:
        return len(self.adjacent_part_numbers) == 2

    def check_if_part_number_is_adjacent(self, part_number: PartNumber) -> bool:
        return (
                (self.row - 1 <= part_number.row <= self.row + 1)
                and
                (self.column in range(part_number.slice_start - 1, part_number.slice_end + 2, 1))
        )

    def get_gear_ratio(self) -> int:
        if self.is_valid_gear():
            return self.adjacent_part_numbers[0].value * self.adjacent_part_numbers[1].value
        else:
            return 0


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


def find_gear_ratio_sum(engine_schematic_str: str) -> int:
    engine_schematic = input_str_to_array(engine_schematic_str)
    part_numbers = find_part_numbers(engine_schematic)
    gears = find_gears(engine_schematic)
    for gear in gears:
        for part_number in part_numbers:
            if gear.check_if_part_number_is_adjacent(part_number):
                gear.adjacent_part_numbers.append(part_number)
    return sum([g.get_gear_ratio() for g in gears])


def find_gears(engine_schematic: np.ndarray) -> list[Gear]:
    print(engine_schematic.shape)
    result = np.where(engine_schematic == "*")
    print(result)
    gears = []
    for x, y in zip(result[0], result[1]):
        print(x, y)
        print(engine_schematic[x, y])
        gears.append(Gear(x, y))
    return gears



if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    # print(sorted("".join(set(content))))
    # print(get_part_number_sum(content))
    print(find_gear_ratio_sum(content))
