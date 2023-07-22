import re
import json
import os


class PlayerModel:
    FILENAME = "json/player/players.jsonl"

    def __init__(self, last_name, first_name, birthday, ine, points=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.ine = ine
        self.points = points

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        if not isinstance(other, PlayerModel):
            return False
        return self.ine == other.ine

    def save_player(self):
        filename = "json/player/players.json"
        with open(filename, "a") as player_file:
            json.dump(self.to_dict(), player_file)
            player_file.write("\n")

    def to_dict(self, only_id=False):
        if only_id:
            return {"ine": self.ine}
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "ine": self.ine,
        }

    @classmethod
    def search_by_ine(cls, ine_list):
        # TODO voir pour ameliore et ne creer que les objets Player des ine demande
        players = cls.load_players()
        player_list = []
        for ine in ine_list:
            for player in players:
                if player.ine == ine:
                    player_list.append(player)
        return player_list

    @classmethod
    def load_players(cls):
        # TODO ajouter option ine_list et si ine_list != => charge tout
        # else charger les player specifique
        players_dicts = []
        if os.path.getsize(cls.FILENAME) != 0:
            with open(cls.FILENAME) as f:
                for row in f:
                    # Faire attention au \n si necessaire rajouter un row.strip("\n")
                    if row:
                        players_dicts.append(json.loads(row))
        players = []
        for player in players_dicts:
            players.append(cls(**player))
        return players

    @staticmethod
    def validate_attribute(attribute: str, value: str):
        r = False
        if attribute == "birthday":
            r = re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{2}$", value)
        if attribute == "ine":
            # verifier que l'ine est unique
            r = bool(re.match(r"^[A-Z]{2}\d{5}$", value))
        return r
