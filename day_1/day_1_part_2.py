WORD_REPLACER = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def get_total_from_lines(lines: list[str]) -> int:
    total = 0
    for line in lines:
        number = parse_line(line)
        total += number
    return total


def parse_line(line: str) -> int:
    parsed = ""
    i = 0
    while i < len(line):
        char = line[i]
        if char.isdigit():
            parsed += char
            i += 1
            continue
        word_found = False
        for potential_number_word in [k for k in WORD_REPLACER.keys() if k.startswith(char)]:
            if line[i:].startswith(potential_number_word):
                parsed += WORD_REPLACER[potential_number_word]
                i += 1
                word_found = True
                break
        if word_found is False:
            i += 1

    # this gives the answer that the website considers correct (53348) where "7mntc" returns 77
    number = int(parsed[0] + parsed[-1])

    # however, think this gives the correct answer (50118) as this "7mntc" will return 7
    # if len(parsed) == 0:
    #     number = 0
    # elif len(parsed) == 1:
    #     number = int(parsed)
    # else:
    #     number = int(parsed[0] + parsed[-1])
    return number


def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        print(get_total_from_lines(file.readlines()))
