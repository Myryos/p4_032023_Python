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
        players: list[PlayerModel],
        description: str,
        nb_round_total: int,
        actual_round_index: int = 0,
        rounds_data: list = [],
    ):  # TODO Ranking ici, def build_ranking(self/cls)
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
        # TODO Ajouter la logique pour charger les Rounds et les Matchs
        all_tournaments = []
        tournament_filenames = []
        with os.scandir(cls.DIRECTORY) as entries:
            for entry in entries:
                tournament_filenames.append(entry.path)
        for tournament_filename in tournament_filenames:
            if os.path.getsize(tournament_filename) != 0:
                with open(tournament_filename, "r") as f:
                    all_tournaments.append(cls(**json.load(f)))

        for t in all_tournaments:
            players_list = []
            for p in t.players:
                players_list.append(p["ine"])
            t.players = PlayerModel.search_by_ine(ine_list=players_list)

            match_list = []
            round_list = []
            for round in t.rounds_data:
                # print(f'round : {round}')
                for match in round:
                    # print(f'match: {match}')
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
                round = Round(match_list=match_list)
                round_list.append(round)
            t.rounds_data = round_list
        return all_tournaments

    def generate_ranking(self):
        matchs_list = self.get_all_matches()

        ranking_dict = {player: 0 for player in self.players}

        for match in matchs_list:
            if match.played and match.winner is not None:
                ranking_dict[match.winner] += 1
            elif match.played and match.winner is None:
                ranking_dict[match.player0] += 0.5
                ranking_dict[match.player1] += 0.5
        ranking_dict = sorted(ranking_dict.items(), key=lambda i: i[1], reverse=True)
        return ranking_dict

    def get_all_matches(self):
        match_list = []
        for round in self.rounds_data:
            for match in round.match_list:
                match_list.append(match)
        return match_list
