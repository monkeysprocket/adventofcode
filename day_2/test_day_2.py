import pytest

from day_2 import GameSet, Game, get_sum_of_possible_game_ids, get_minimum_possible_cubes


@pytest.mark.parametrize(
    ["set_str", "red", "green", "blue"],
    [
        ("3 blue, 4 red", 4, 0, 3),
        ("1 red, 2 green, 6 blue", 1, 2, 6),
        ("2 green", 0, 2, 0),
    ]
)
def test_game_set_from_str_constructor(set_str: str, red: int, green: int, blue: int):
    game_set = GameSet.from_str(set_str)
    assert game_set.red == red
    assert game_set.green == green
    assert game_set.blue == blue


@pytest.mark.parametrize(
    "game_str",
    [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
)
def test_game_constructor(game_str: str):
    game = Game(game_str)

    assert len(game._game_sets) > 0
    for game_set in game._game_sets:
        assert isinstance(game_set, GameSet)


def test_get_sum_of_possible_game_ids():
    result = get_sum_of_possible_game_ids(
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ],
        max_red=12,
        max_green=13,
        max_blue=14,
    )
    assert result == 8


def test_get_minimum_possible_cubes():
    result = get_minimum_possible_cubes(
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
    )
    assert result == 2286
