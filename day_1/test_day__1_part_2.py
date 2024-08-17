import pytest

from day_1_part_2 import get_total_from_lines, parse_line


def test_get_total_from_lines():
    result = get_total_from_lines(
        [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
    )
    assert result == 281


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ["two1nine", 29],
        ["eightwothree", 83],
        ["abcone2threexyz", 13],
        ["xtwone3four", 24],
        ["4nineeightseven2", 42],
        ["zoneight234", 14],
        ["7pqrstsixteen", 76],
    ]
)
def test_parse_line(line: str, expected: int):
    result = parse_line(line)
    assert result == expected
