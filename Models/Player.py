import re
import json
import os
class Player():
    def __init__(self, last_name, first_name, birthday, ine):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.ine = ine


    def save_player(self):
        filename = 'json/player/players.json'
        all_players = []

        if os.path.getsize(filename) != 0:
            with open(filename) as list_player:
                all_players = json.load(list_player)
        
        player_dictionnary = {
            'last_name':self.last_name,
            'first_name':self.first_name,
            'birthday':self.birthday,
            'ine':self.ine
        }
        all_players.append(player_dictionnary)

        with open(filename, 'w') as player_file:
            json.dump(all_players, player_file, indent=4, separators=(',',': '))
    
    @staticmethod
    def load_players():
        all_players = []
        #retuning_array = []
        #tmp = ""
        filename = 'json/player/players.json'
        if os.path.getsize(filename) != 0:
            with open(filename) as list_player:
                all_players = json.load(list_player)
        """for player in all_players:
            tmp = f'{player["last_name"]} {player["first_name"]} {player["birthday"]} {player["ine"]}'
            retuning_array.append(tmp)"""
        return all_players

    @staticmethod
    def validate_attribute(attribute:str, value:str):
        r = False
        if attribute == 'birthday':
            if re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{2}$", value) and value != "":
                r = True
        if attribute =='ine':
            #verifier que l'ine est unique
            if re.match(r"^[A-Z]{2}\d{5}$", value) and value !="":
                r = True
        return r