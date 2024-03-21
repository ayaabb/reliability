import unittest
from unittest.mock import patch

from classes.class_game import *
from classes.class_murder_exception import NoPlayersInMurdererPlacesError
from players_init import get_players

weapons = ["w1", "w2", "w3", "w4", "w5"]


class TestGame(unittest.TestCase):
    def test_select_murderer(self):
        alive_players = ["Player1", "Player2", "Player3"]

        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)
        game.select_murderer()
        self.assertTrue(game.murderer in alive_players)

    def test_choose_murder_place(self):
        alive_players = ["Player1", "Player2", "Player3"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)
        game.murderer = alive_players[0]
        game.murderer.last_visited_places = ["Library", "Garden"]
        murder_place = game.choose_murder_place()
        self.assertTrue(murder_place in game.murderer.last_visited_places)

    def test_choose_victim(self):
        alive_players = ["Player1", "Player2", "Player3"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)
        game.murderer = alive_players[0]
        game.murderer.last_visited_places = ["Library", "Garden"]
        victim = game.choose_victim("Library")
        self.assertIsNone(victim)
        game.alive_players[1].last_visited_places = ["Library"]
        victim = game.choose_victim("Library")
        self.assertIsNot(victim, game.murderer)
        self.assertTrue(victim, game.alive_players[1])


    def test_murder_with_no_players_in_murder_place(self):
        alive_players = ["Player1"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]

        game = Game(alive_players, places)
        game.initialize_game()
        game.murderer.visit_places(game.places)
        with self.assertRaises(NoPlayersInMurdererPlacesError):
            game.murder()

    def test_play_round_with_no_murder(self):
        alive_players = ["Player1"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]

        game = Game(alive_players, places)
        game.initialize_game()
        status = game.play_round()
        self.assertTrue(status=='no murder')
