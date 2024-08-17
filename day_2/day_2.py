from typing import Self


class Game:
    def __init__(self, game_str: str) -> None:
        self._game_str = game_str
        self._game_id = 0
        self._game_sets: list[GameSet] = []

        self._parse_game_str()

    def _parse_game_str(self) -> None:
        game_id = int(self._game_str.split(":")[0].removeprefix("Game "))
        sets = []
        for set_str in self._game_str.split(":")[1].split(";"):
            game_set = GameSet.from_str(set_str)
            sets.append(game_set)

        self._game_id = game_id
        self._game_sets = sets

    def get_game_id(self) -> int:
        return self._game_id

    def get_max_red_count(self) -> int:
        return max([s.red for s in self._game_sets])

    def get_max_green_count(self) -> int:
        return max([s.green for s in self._game_sets])

    def get_max_blue_count(self) -> int:
        return max([s.blue for s in self._game_sets])


class GameSet:
    def __init__(self, red=0, green=0, blue=0) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def from_str(cls, string: str) -> Self:
        red = 0
        green = 0
        blue = 0
        for colour_str in string.split(","):
            if "red" in colour_str:
                red = int(colour_str.split()[0])
            elif "green" in colour_str:
                green = int(colour_str.split()[0])
            elif "blue" in colour_str:
                blue = int(colour_str.split()[0])
            else:
                raise ValueError(f"unexpected format: {colour_str}")
        return GameSet(red, green, blue)

    def __repr__(self) -> str:
        return f"GameSet(red={self.red}, green={self.green}, blue={self.blue})"


def get_sum_of_possible_game_ids(game_strs: list[str], max_red: int, max_green: int, max_blue: int) -> int:
    games = parse_game_strs(game_strs)
    id_sum = 0
    for game in games:
        if all(
                [
                    game.get_max_red_count() <= max_red,
                    game.get_max_green_count() <= max_green,
                    game.get_max_blue_count() <= max_blue,
                ]
        ):
            id_sum += game.get_game_id()
    return id_sum


def get_minimum_possible_cubes(game_strs: list[str]) -> int:
    games = parse_game_strs(game_strs)
    cub_power_sum = 0
    for game in games:
        power = game.get_max_red_count() * game.get_max_green_count() * game.get_max_blue_count()
        cub_power_sum += power
    return cub_power_sum


def parse_game_strs(game_strs: list[str]) -> list[Game]:
    games = []
    for game_str in game_strs:
        game = Game(game_str)
        games.append(game)
    return games


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.readlines()
    print(get_sum_of_possible_game_ids(lines, max_red=12, max_green=13, max_blue=14))
    print(get_minimum_possible_cubes(lines))
