import os
import random

# from  utils.load_package import *
from  classes.class_player import player

from utils.load_package import *


def get_players():

    players_names = merge_data(load_json_files("players"), 'names')
    weapons = merge_data(load_json_files(  "weapons"), 'weapons')
    players = []
    for name in players_names:
        players.append(player(name, random.sample(weapons, random.randint(2, 4))))
    return players
