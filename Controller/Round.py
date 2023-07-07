from View.Round import RoundView

from Models.Round import Round


class RoundControl:
    # TODO ajout d'un init
    def __init__(self, tournament):
        self.tournament = tournament

    @staticmethod
    def play_matchs(match_list: list, tournament):
        for match in match_list:
            choice = RoundView.ask_for_winner(match)
            if choice == match.player0 or choice == match.player1:
                match.played = True
                match.winner = choice
                tournament.save()
            if choice == "Draw":
                match.played = True
                tournament.save()
            if choice == "Exit":
                break

    @classmethod
    def play_round(cls, tournament):
        while 1:
            unplayed_match = cls.get_unplayed_matches(tournament)
            if len(unplayed_match) > 0:
                cls.play_matchs(unplayed_match, tournament)

            RoundView.display_round(tournament.actual_round_index)
            round = Round(
                players=tournament.players
            )  # TODO Voir pour bouger la gen des rounds a la création du tournaments
            tournament.rounds_data.append(round)
            print(tournament.rounds_data[0].match_list[0].winner)
            tournament.save()
            cls.play_matchs(round.match_list, tournament)
            tournament.actual_round_index += 1
            tournament.save()
            RoundView.display_end_round()
            action = RoundView.continue_exit()
            if tournament.actual_round_index == tournament.nb_round_total - 1:
                break
            if action == "Exit":
                break

    def executeRounds(self, tournament):
        while 1:
            action = RoundView.choose_actions()
            if (
                action == "Play Round"
                and tournament.actual_round_index < tournament.nb_round_total - 1
            ):
                self.play_round(tournament)
            if action == "Display Ranking":
                pass
            if action == "Exit":
                break
        # TODO RAJOUTER LE CALCUL DE RANKING ET LE DISPLAY

    @staticmethod
    def get_unplayed_matches(tournament) -> list:
        match_list = []

        for round in tournament.rounds_data:
            for match in round.match_list:
                if match.played is False:
                    match_list.append(match)
        return match_list
