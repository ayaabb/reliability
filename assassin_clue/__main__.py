import os
import sys

from classes.class_game import Game
from players_init import get_players
from utils.load_package import merge_data, load_json_files


def main():
    places = merge_data(load_json_files("places"), 'places')
    players = get_players()
    game = Game(players, places)
    game.initialize_game()
    game.Start()


def test():
    f = 0
    while f < 2:
        if f == 2:
            raise TypeError("ok")
        f += 1

    return "R"


if __name__ == "__main__":
    # try:
    #     l = test()
    # except TypeError as e:
    #     print(e)
    main()
