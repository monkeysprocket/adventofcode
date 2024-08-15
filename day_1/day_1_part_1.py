def get_total_from_lines(lines: list[str]) -> int:
    total = 0
    for line in lines:
        number = parse_line(line)
        print(number)
        total += number
    return total


def parse_line(line: str) -> int:
    first_digit = get_first_digit(line)
    last_digit = get_first_digit(reversed(line))
    number = int(first_digit + last_digit)
    return number


def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
    print(get_total_from_lines(lines))
