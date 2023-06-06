import re
import json
import os

from Models.Player import PlayerModel
class TournamentModel():

    """"""
    DIRECTORY = 'json/tournament'
    #TODO renommeer actual round en actual round index et init un rounds en list vide
    def __init__(self, 
                 name:str, 
                 places:str, 
                 date_start:str, 
                 date_end:str, 
                 players:list[PlayerModel], 
                 description:str,  
                 nb_round_total:int, 
                 actual_round_index:int = 0,
                 rounds_data: list = []):
       self.name = name
       self.places = places
       self.date_start = date_start
       self.date_end = date_end
       self.nb_round_total = nb_round_total
       self.actual_round_index = actual_round_index
       self.rounds_data = rounds_data
       self.players = players
       self.description = description
    
    def __str__(self):
        return self.name

    def to_dict(self):
        player_dicts = []
        for player in self.players:
            player_dicts.append(player.to_dict(only_id=True))
        return {
            'name': self.name,
            'places': self.places,
            'date_start': self.date_start,
            'date_end': self.date_end,
            'nb_round_total': self.nb_round_total,
            'actual_round_index': self.actual_round_index,
            'rounds_data': [r.to_dict() for r in self.rounds_data],
            'players': player_dicts,
            'description': self.description
        }

    @property
    def filename(self):
        return f"{self.DIRECTORY}/{self.name}.json"
    
    def save(self):
        with open(self.filename, 'w') as json_file:
            json.dump(self.to_dict(), json_file)           
     

    @classmethod
    def load(cls):
        all_tournaments = []
        tournament_filenames = []
        """if os.path.getsize(cls.FILENAME) != 0:
            with open(cls.FILENAME) as f:
               for row in f:
                   if row:
                       all_tournaments.append(json.loads(row))"""
        with os.scandir(cls.DIRECTORY) as entries :
            for entry in entries:
                tournament_filenames.append(entry.path)
        for tournament_filename in tournament_filenames:
            with open(tournament_filename, "r") as f:
                all_tournaments.append(cls(**json.load(f)))

        for t in all_tournaments:
            players_list = []
            for p in t.players:
                players_list.append(p["ine"])
            t.players = PlayerModel.search_by_ine(ine_list=players_list)
        return all_tournaments

    
    

