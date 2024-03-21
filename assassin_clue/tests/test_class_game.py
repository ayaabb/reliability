import unittest
from assassin_clue.classes.class_game import *
from assassin_clue.classes.class_player_exception import NoPlayersInMurderPlaceError
from assassin_clue.players_init import get_players


class TestGame(unittest.TestCase):
    def test_select_murderer(self):
        alive_players = ["Player1", "Player2", "Player3"]
        weapons = ["w1", "w2", "w3"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)
        game.select_murderer()
        self.assertTrue(game.murderer in alive_players)

    def test_choose_murder_place(self):
        alive_players = ["Player1", "Player2", "Player3"]
        weapons = ["w1", "w2", "w3"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)
        game.murderer = alive_players[0]
        game.murderer.last_visited_places = ["Library", "Garden"]
        murder_place = game.choose_murder_place()
        self.assertTrue(murder_place in game.murderer.last_visited_places)

    def test_choose_victim(self):
        alive_players = ["Player1", "Player2", "Player3"]
        weapons = ["w1", "w2", "w3"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)
        game.murderer = alive_players[0]
        game.murderer.last_visited_places = ["Library", "Garden"]
        victim = game.choose_victim("Library")
        self.assertIsNone(victim)
        game.alive_players[1].laslast_visited_places = ["Library"]
        victim = game.choose_victim("Library")
        self.assertIsNot(victim, game.murderer)
        self.assertTrue(victim, game.alive_players[1])

    def test_play_round(self):
        alive_players = ["Player1", "Player2", "Player3"]
        weapons = ["w1", "w2", "w3"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)
        game.initialize_game()
        result = game.play_round()
        self.assertIn(result, ['Game Over', 'no murder', 'continue'])
        if result == 'continue':
           self.assertTrue(len(game.alive_players) == 2)


    def test_play_round_with_no_players_in_murder_place(self):
        alive_players = ["Player1"]
        weapons = ["w1", "w2", "w3"]
        alive_players = get_players(alive_players, weapons)
        places = ["Library", "Kitchen", "Garden", "Study", "Hall", "Dining Room"]
        game = Game(alive_players, places)

        with self.assertRaises(NoPlayersInMurderPlaceError):
            game.play_round()
