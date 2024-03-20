from .class_player_exception import *
from .class_player import *


class Game:
    def __init__(self, alive_players, places):
        self.alive_players = alive_players
        self.places = places
        self.murderer = None

    def initialize_game(self):
        """Initialize the game state."""
        self.select_murderer()

    def select_murderer(self):
        """the function chooses a murderer from the players list and save it on game variables"""
        self.murderer = random.choice(self.alive_players)

    def murder(self):
        """
        choosing a victim from alive players list to murder based on a random place that the murderer and the player
        in it ,deletes it from alive players prints the murder details (place,weapon,victim)"""

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
        murder_place = random.choice(self.murderer.last_visited_places)
        return murder_place

    def choose_victim(self, murder_place):
        """Choose a player from alive players list to be victim."""
        players_in_murder_place = [player for player in self.alive_players if
                                   murder_place in player.last_visited_places and player != self.murderer]
        if len(players_in_murder_place) == 0:
            return None
        return random.choice(players_in_murder_place)

    def check_murderer(self, accused_player):
        """param: accused player
                the function checks if this accused player is the murderer
                returns: True or False
                """
        return accused_player == self.murderer

    def suspect_2_players(self):
        """the function prints all alive players and asks the user player to choose
        2 players to suspect, and then suspect them by choosing 2 random places and 1 gun
         returns: [player1,2 places,1 gun],[player2,2 places,1 gun]
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
         param: 2 suspected players and their 2 random places they visited and a weapon
          the function asks from the user player to accuse one of them based on 2 last places
          that they visited and a weapon
        returns: the accused player"""

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

        Returns:
            str: 'Game Over', 'no murder', or 'continue'.
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
                    raise StopIteration(f"Game Over!! Your accusation is correct and '{self.murderer.name}' is the murderer")
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





