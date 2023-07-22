from View.Round import RoundView

from Models.Round import Round

from Controller.Tournament import TournamentController


class RoundControl:
    def __init__(self, tournament):
        self.tournament = tournament

    @staticmethod
    def play_matchs(match_list: list, tournament):
        for match in match_list:
            choice = RoundView.ask_for_winner(match)
            if choice == match.player0 or choice == match.player1:
                match.played = True
                match.winner = choice
                tournament.calculate_ranking()
                tournament.save()
            if choice == "Draw":
                match.played = True
                tournament.calculate_ranking()
                tournament.save()
            if choice == "Exit":
                break

    @classmethod
    def play_round(cls, tournament):
        while 1:
            unplayed_match = []
            if tournament.actual_round_index > 0:
                unplayed_match = cls.get_unplayed_matches(tournament)
            if len(unplayed_match) > 0:
                cls.play_matchs(unplayed_match, tournament)

            RoundView.display_round(tournament.actual_round_index + 1)
            if tournament.actual_round_index == 0:
                round = Round(players=tournament.players, is_first_round=True)
            else:
                old_match_list = tournament.get_all_matches()
                round = Round(players=tournament.players, old_match_list=old_match_list)
            tournament.rounds_data.append(round)
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
                TournamentController.show_ranking(tournament)
            if action == "Exit":
                break

    @staticmethod
    def get_unplayed_matches(tournament) -> list:
        match_list = []

        for round in tournament.rounds_data:
            for match in round.match_list:
                if match.played is False:
                    match_list.append(match)
        return match_list
