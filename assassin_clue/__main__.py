import os
import sys

from utils.save_docstring import save_class_docstrings
from classes.class_game import Game
from players_init import get_players
from utils.load_package import merge_data, load_json_files


def main():
    places = merge_data(load_json_files("places"), 'places')
    players_names = merge_data(load_json_files("players"), 'names')
    weapons = merge_data(load_json_files("weapons"), 'weapons')
    players = get_players(players_names, weapons)
    game = Game(players, places)
    game.initialize_game()
    game.Start()


def save_docstring_to_file(class_, output_file_path):
    save_class_docstrings(class_, output_file_path)


if __name__ == "__main__":
    save_docstring_to_file(Game, 'docstring_file.txt')
    # main()
