import json
import os

from Models.Player import PlayerModel
from Models.Round import Round, Match


class TournamentModel:

    """"""

    DIRECTORY = "json/tournament"

    def __init__(
        self,
        name: str,
        places: str,
        date_start: str,
        date_end: str,
        players: list,
        description: str,
        nb_round_total: int,
        actual_round_index: int = 0,
        rounds_data: list = None,
    ):  # TODO Ranking ici, def build_ranking(self/cls)
        self.name = name
        self.places = places
        self.date_start = date_start
        self.date_end = date_end
        self.nb_round_total = nb_round_total
        self.actual_round_index = actual_round_index
        self.rounds_data = rounds_data or []
        self.players = players
        self.description = description

    def __str__(self):
        return self.name

    def to_dict(self):
        player_dicts = []
        for player in self.players:
            player_dicts.append(player.to_dict(only_id=True))
        return {
            "name": self.name,
            "places": self.places,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "nb_round_total": self.nb_round_total,
            "actual_round_index": self.actual_round_index,
            "rounds_data": [r.to_dict() for r in self.rounds_data],
            "players": player_dicts,
            "description": self.description,
        }

    @property
    def filename(self):
        return f"{self.DIRECTORY}/{self.name}.json"

    def save(self):
        with open(self.filename, "w") as json_file:
            json.dump(self.to_dict(), json_file, indent=4)

    @classmethod
    def load(cls):
        all_tournaments = []
        with os.scandir(cls.DIRECTORY) as entries:
            for entry in entries:
                if os.path.getsize(entry.path) == 0:
                    continue
                with open(entry.path, "r") as f:
                    all_tournaments.append(cls(**json.load(f)))

        for t in all_tournaments:
            players_list = []
            for p in t.players:
                players_list.append(p["ine"])
            t.players = PlayerModel.search_by_ine(ine_list=players_list)

            round_list = []
            for round_data in t.rounds_data:
                match_list = []
                for match in round_data:
                    match_players_list = PlayerModel.search_by_ine(
                        [match["player0"], match["player1"]]
                    )
                    if match["winner"] == match_players_list[0].ine:
                        match["winner"] = match_players_list[0]
                    elif match["winner"] == match_players_list[1].ine:
                        match["winner"] = match_players_list[1]
                    new_match = Match(
                        match_players_list[0],
                        match_players_list[1],
                        match["played"],
                        match["winner"],
                    )
                    match_list.append(new_match)
                round_list.append(Round(match_list=match_list))
            t.rounds_data = list(round_list)
        return all_tournaments

    def calculate_ranking(self):
        matchs_list = self.get_all_matches()

        for player in self.players:
            player.points = 0

        for match in matchs_list:
            if match.played and match.winner is not None:
                for player in self.players:
                    if player == match.winner:
                        player.points += 1
            elif match.played and match.winner is None:
                for player in self.players:
                    if player == match.player0 or player == match.player1:
                        player.points += 0.5

    def get_all_matches(self):
        match_list = []
        for round in self.rounds_data:
            for match in round.match_list:
                match_list.append(match)
        return match_list
