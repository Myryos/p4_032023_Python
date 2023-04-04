import re
import json
import os 
class Tournament():
    """"""
    def __init__(self, 
                 name:str, 
                 places:str, 
                 date_start:str, 
                 date_end:str, 
                 player_list:str, 
                 description:str,  
                 nb_round_max:int = 4, 
                 actual_round:int = 0):
       self.name = name
       self.places = places
       self.date_start = date_start
       self.date_end = date_end
       self.max_round = nb_round_max
       self.actual_round = actual_round
       self.player_list = player_list
       self.description = description
    
    
    def get_attribute(self, attribute):
        pass

    def set_attribute(self, attribute, new_value):
        pass

    
    def save_tournament(self):
        print(self.name)
        tournament_dictionnary = {'name' : self.name,
                                  'places': self.places,
                                  'date_start':self.date_start,
                                  'date_end':self.date_end,
                                  'max_round':self.max_round,
                                  'actual_round':self.actual_round,
                                  'player_list':self.player_list,
                                  'description':self.description}
        json_tournament = json.dumps(tournament_dictionnary, indent=4)
        with open(f'json/tournament/{self.name}.json', 'w') as json_file:
            json_file.write(json_tournament)
    
    @staticmethod
    def validate_attribute(attribute:str, value:str):
        r:bool = False
        if attribute == 'date':
            if re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{2}$", value) and value != "":
                r = True
        if attribute == 'round_max':
            if value.isdigit() or value == "":
                r = True
        return r
    

    
    

    
