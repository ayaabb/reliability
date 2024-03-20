from classes.class_player import *
from classes.class_player_exception import *


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
        invalid_places = []
        murder_place = self.choose_murder_place(invalid_places)
        victim = self.choose_victim(murder_place)

        while victim is None:
            try:
                invalid_places.append(murder_place)
                murder_place = self.choose_murder_place(invalid_places)
                victim = self.choose_victim(murder_place)
                if len(invalid_places) == len(self.murderer.last_visited_places):
                    raise NoPlayersInMurderPlaceError("No players in the murder place.")
            except NoPlayersInMurderPlaceError as e:
                print(e)
                return None

        print(f"Murder Details:")
        print(f"Place: {murder_place}")
        print(f"Weapon: {random.choice(self.murderer.fav_weapons)}")
        print(f"Murdered Player: {victim.name}\n")
        self.alive_players.remove(victim)

    def choose_murder_place(self, invalid_places):
        murder_place = random.choice(self.murderer.last_visited_places)
        while murder_place in invalid_places:
            murder_place = random.choice(self.murderer.last_visited_places)
        return murder_place

    def choose_victim(self, murder_place):
        """Choose a player from alive players list to be victim."""
        players_in_murder_place = [player for player in self.alive_players if murder_place in player.last_visited_places]
        if not players_in_murder_place:
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
        print(f"Visited Places: {', '.join(suspected_player1[1])}")
        print(f"Favorite Weapon: {suspected_player1[2]}")
        print("\n")
        print(f"Suspected Player 2: {suspected_player2[0].name}")
        print(f"Visited Places: {', '.join(suspected_player2[1])}")
        print(f"Favorite Weapon: {suspected_player2[2]}")
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

        for player in self.alive_players:
            player.visit_places(self.places)
        try:
            if self.murder() is not None:
                suspected_player1, suspected_player2 = self.suspect_2_players()
                accused_player = self.accuse_player(suspected_player1, suspected_player2)
                if self.check_murderer(accused_player):
                    return 'Game Over'

            else:
                raise TypeError("There is no murder,let's try one more round\n")

        except TypeError as e:
            print(e)
            return "no murder"
        return "continue"

    def Start(self):
        round=1
        try:
            while len(self.alive_players) > 2:
                print(f"Round {round}:")
                if self.play_round() == 'Game Over':
                    raise StopIteration(f"Game Over!! '{self.murderer.name}' is the murderer")

                if len(self.alive_players) == 2:
                    raise StopIteration(f"The game ended and the winner is the murderer '{self.murderer.name}'")
                round+=1
        except StopIteration as e:
            print(e)
            return
