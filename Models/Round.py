import random as rnd


class Round:

    """Revoir la structure pour utilise l'init pour la creation des rounds"""

    def __init__(
        self, *, players=None, match_list=None
    ):  # L'etoile permet de dire a python que cette fonction demande les paramettre dnas l'ordre specifier
        if players:
            self.match_list = self.generate_rounds(players)
        elif match_list:
            self.match_list = match_list
        else:
            raise ValueError("No players or Match list provided")

    def to_dict(self):
        return [m.to_dict() for m in self.match_list]

    # TODO reecrire integralement les fonction generate rounds et match
    def generate_rounds(self, list_player):
        players = []
        for player in list_player:
            players.append(player)
        pairs = []
        popped_players = []

        while len(players) > 1:
            # TODO nettoyer pour rendre tout cela plus clair
            match_tuple = self.generate_match(players)
            player1 = match_tuple[0].player1

            popped_players.append(players.pop(match_tuple[1]))
            # Get the new index of player 1 and pop it

            p1_new_index = players.index(player1)

            popped_players.append(players.pop(p1_new_index))

            pairs.append(match_tuple[0])
            if len(players) == 1:
                rnd.shuffle(popped_players)
                popped_player_index = rnd.randint(0, len(popped_players) - 1)
                players.append(popped_players.pop(popped_player_index))
        return pairs

    @classmethod
    def generate_match(cls, list_player: list):
        first_player = 0
        second_player = 0
        while first_player == second_player:
            first_player = rnd.randint(0, len(list_player) - 1)
            second_player = rnd.randint(0, len(list_player) - 1)

        match_object = Match(
            player0=list_player[first_player], player1=list_player[second_player]
        )

        return (match_object, first_player, second_player)

    def is_same_pair(self, old_pairs, new_pair):  # A renommer
        pass

    """TODO Retravaille la gen pour qu'a chaque appel de la fonction
    renvoi une liste de pairs ou les joueurs ne sont présent qu'une fois"""
    # TODO Ajout d'une logique pour que les joueurs soit différent a chaque fois dans mesure du possible


class Match:
    def __init__(self, player0, player1, played=False, winner=None):
        self.player0 = player0
        self.player1 = player1
        self.played = played
        self.winner = winner

    def to_dict(self):
        print(self.winner)
        return {
            "player0": self.player0.ine,
            "player1": self.player1.ine,
            "played": self.played,
            "winner": self.winner.ine
            if self.winner is not None or self.winner == "null"
            else None,
        }
