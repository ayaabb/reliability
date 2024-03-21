import random

from .class_player_exception import *
from .class_player import *



class Game:
    def __init__(self, alive_players, places):
        self.alive_players = alive_players
        self.places = places
        self.murderer = None

    def initialize_game(self):
        """
         Initializes the game state by calling method that selects the murderer from the list of alive players.
         No parameters.
         Returns: None
        """
        self.select_murderer()

    def select_murderer(self):
        """
          Chooses a murderer from the list of alive players and saves it in the game variables.
          No parameters.
          Returns:None
          """
        self.murderer = random.choice(self.alive_players)

    def murder(self):
        """
        Chooses a victim from the list of alive players and murder him
        based on a random place of the murderer last visited places.
        Deletes the victim from the list of alive players and prints the murder details.
        No parameters.
        Returns: bool: True if murder is successful, False raises No Players In Murder Place Error.
        """

        murder_place = self.choose_murder_place()
        victim = self.choose_victim(murder_place)

        while victim is None:

            self.murderer.last_visited_places.remove(murder_place)
            if len(self.murderer.last_visited_places) == 0:
                raise NoPlayersInMurderPlaceError("No players in the murder place.")

            murder_place = self.choose_murder_place()
            victim = self.choose_victim(murder_place)

        print(f"Murder Details:")
        print(f"Place: {murder_place}")
        print(f"Weapon: {random.choice(self.murderer.fav_weapons)}")
        print(f"Murdered Player: {victim.name}\n")
        self.alive_players.remove(victim)
        return True

    def choose_murder_place(self):
        """
            Chooses a murder place randomly from the last visited places of the murderer.
            No parameters.
            Returns: str: The chosen murder place.
        """
        murder_place = random.choice(self.murderer.last_visited_places)
        return murder_place

    def choose_victim(self, murder_place):
        """
        Chooses a victim from the list of alive players based on the murder place.
        Parameters: murder_place (str): The murder place.
        Returns:  Player or None: The chosen victim if found, None otherwise.
        """
        players_in_murder_place = [player for player in self.alive_players if
                                   murder_place in player.last_visited_places and player != self.murderer]
        if len(players_in_murder_place) == 0:
            return None
        return random.choice(players_in_murder_place)

    def check_murderer(self, accused_player):
        """
        Checks if the accused player is the murderer.
        Parameters: accused_player (Player)
        Returns: bool: True if the accused player is the murderer, False otherwise.
        """
        return accused_player == self.murderer

    def suspect_2_players(self):
        """
        Allows the user to suspect two players and choosing random places and weapons of them.
        Returns:  A list containing information about the suspected players, places, and weapons.
        """
        print("These are the alive players:")
        for i in range(len(self.alive_players)):
            print(f"{i + 1}.{self.alive_players[i].name}")
        print("\n")
        invalid_choice = True
        while invalid_choice:
            try:
                player1 = int(input(f"Choose the first player to suspect (1-{len(self.alive_players)}): "))
                player2 = int(input(f"Choose the second player to suspect (1-{len(self.alive_players)}): "))
                if player1 == player2:
                    raise ValueError("You can't choose the same player twice.\n")
                elif not (1 <= player1 <= len(self.alive_players)) or not (1 <= player2 <= len(self.alive_players)):
                    raise ValueError("Invalid input. Please enter a valid player number.\n")
                else:
                    invalid_choice = False
            except ValueError as e:
                print(e)

        player1 = self.alive_players[player1 - 1]
        player2 = self.alive_players[player2 - 1]

        return [player1, player1.suspect()], [player2, player2.suspect()]

    def accuse_player(self, suspected_player1, suspected_player2):
        """
            Allows the user to accuse one of the suspected players based on their visited places and weapons.
            Parameters: suspected_player1 (nested list): Information about the first suspected player,
            suspected_player2 (nested list): Information about the second suspected player.
            Returns: Player: The accused player.
        """

        print(f"Suspected Player 1: {suspected_player1[0].name}")
        print(f"Visited Places: {', '.join(suspected_player1[1][0])}")
        print(f"Favorite Weapon: {suspected_player1[1][1]}")
        print("\n")
        print(f"Suspected Player 2: {suspected_player2[0].name}")
        print(f"Visited Places: {', '.join(suspected_player2[1][0])}")
        print(f"Favorite Weapon: {suspected_player2[1][1]}")
        print("\n")
        invalid_choice = True
        while invalid_choice:
            try:
                choice = input(
                    f"Choose the suspected player to accuse (1: {suspected_player1[0].name}, 2: {suspected_player2[0].name}): ")
                if choice not in ["1", "2"]:
                    raise ValueError("Invalid input. Please enter 1 or 2.\n")
                else:
                    invalid_choice = False
            except ValueError as e:
                print(e)

        if choice == "1":
            return suspected_player1[0]
        else:
            return suspected_player2[0]

    def play_round(self):
        """Simulates a game round, allowing players to visit places and handle murder accusations.
        Iterates over each alive player, allowing them to visit places. Checks if a murder has occurred.
        If so, prompts user player to suspect and accuse players . Returns 'Game Over' if the accused
        player is the murderer, 'no murder' if no murder occurred, or 'continue' to indicate the game
        should proceed.
        Returns: str: 'Game Over', 'no murder', or 'continue'.
        """

        for player in self.alive_players:
            player.visit_places(self.places)
        try:
            murder = self.murder()
            if murder:
                if len(self.alive_players) == 1:
                    return "end"
                suspected_player1, suspected_player2 = self.suspect_2_players()
                accused_player = self.accuse_player(suspected_player1, suspected_player2)
                if self.check_murderer(accused_player):
                    return 'Game Over'

        except NoPlayersInMurderPlaceError as e:
            print(e)
            return "no murder"

        return "continue"

    def Start(self):
        """Starts the game simulation.
         Initiates the game simulation by running rounds until there are only two players and one of them the murderer.
         Each round is played using the play_round method. If only two players remained the game will end
          and the murderer is the winner.If the play_round returns a Game Over message the game ends with game over message.
         """
        round = 1
        try:
            while len(self.alive_players) > 1:
                print(f"Round {round}:")
                round_status = self.play_round()
                if round_status == 'Game Over':
                    raise StopIteration(
                        f"Game Over!! Your accusation is correct and '{self.murderer.name}' is the murderer")
                elif round_status == 'continue':
                    print("Your accusation is incorrect, the game continues")
                elif round_status == "no murder":
                    print("let's try one more round")
                else:
                    print(f"The game has ended and the winner is the murderer '{self.murderer.name}'")
                    break
                round += 1
                print("\n")
        except StopIteration as e:
            print(e)
