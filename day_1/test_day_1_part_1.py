import pytest

from day_1_part_1 import get_total_from_lines, parse_line


def test_get_total_from_lines():
    result = get_total_from_lines(
        [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
        ]
    )
    assert result == 142


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ["1abc2", 12],
        ["pqr3stu8vwx", 38],
        ["a1b2c3d4e5f", 15],
        ["treb7uchet", 77],
    ]
)
def test_parse_line(line: str, expected: int):
    result = parse_line(line)
    assert result == expected