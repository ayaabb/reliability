from classes.class_game import Game
from players_init import players_init
from utils.load_package import merge_data, load_json_files


def main():
    places = merge_data(load_json_files("places"), 'places')
    players = players_init()
    game=Game(players,places)
    game.initialize_game()
    game.Start()


if __name__ == "__main__":
    main()
