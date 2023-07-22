import random as rnd


class Round:
    def __init__(
        self,
        *,
        players=None,
        match_list=None,
        is_first_round=False,
        old_match_list=None
    ):  # L'etoile permet de dire a python que cette fonction demande les paramettre dnas l'ordre specifier
        if players:
            self.match_list = self.generate_rounds(
                players, is_first_round=is_first_round, old_match_list=old_match_list
            )
        elif match_list is not None:
            self.match_list = match_list
        else:
            raise ValueError("No players or Match list provided")

    def to_dict(self):
        if self.match_list is not None:
            return [m.to_dict() for m in self.match_list]
        else:
            return []

    def generate_rounds(self, list_player, is_first_round=False, old_match_list=None):
        def generate_match_object(players: list):
            match_object = self.generate_random_match(players)

            popped_players.extend([match_object.player0, match_object.player1])
            players.remove(match_object.player0)
            players.remove(match_object.player1)
            return match_object

        players = list(list_player)
        match_list = []
        popped_players = []
        while len(players) > 1:
            if is_first_round:
                match_list.append(generate_match_object(players))
            else:
                players = self.get_ranking_players(players)
                new_players_list = [players.pop(0)]

                index_player1 = 0

                if len(players) > 1 and self.is_same_match(
                    old_pairs=old_match_list,
                    new_pair=[new_players_list[0], players[index_player1]],
                ):
                    index_player1 = rnd.randint(1, len(players) - 1)

                new_players_list.append(players.pop(index_player1))
                match_list.append(generate_match_object(new_players_list))
        return match_list

    @staticmethod
    def get_ranking_players(players_list: list) -> list:
        return sorted(
            players_list, key=lambda x: (x.points, rnd.random()), reverse=True
        )

    @classmethod
    def generate_random_match(cls, list_player: list):
        first_player = 0
        second_player = 0
        while first_player == second_player:
            first_player = rnd.randint(0, len(list_player) - 1)
            second_player = rnd.randint(0, len(list_player) - 1)

        match_object = Match(
            player0=list_player[first_player], player1=list_player[second_player]
        )

        return match_object

    def is_same_match(self, old_pairs: list, new_pair: list) -> bool:
        for match in old_pairs:
            if (
                match.player0 == new_pair[0]
                and match.player1 == new_pair[1]
                or match.player0 == new_pair[1]
                and match.player1 == new_pair[0]
            ):
                return True
        return False


class Match:
    def __init__(self, player0, player1, played=False, winner=None):
        self.player0 = player0
        self.player1 = player1
        self.played = played
        self.winner = winner

    def to_dict(self):
        return {
            "player0": self.player0.ine,
            "player1": self.player1.ine,
            "played": self.played,
            "winner": self.winner.ine
            if self.winner is not None or self.winner == "null"
            else None,
        }
