from Controller.Tournament import TournamentController
from View.Round import RoundView

from Models.Round import Round

class RoundControl():
    @classmethod
    def new_round(cls):
        tournaments = TournamentController.get_tournaments()
        tournament = RoundView.choose_tournament(tournaments)

        for i in range(tournament.actual_round_index, tournament.nb_round_total):
            tournament.actual_round_index = i 
            RoundView.display_round(tournament.actual_round_index)
            round = Round(tournament.players)
            tournament.rounds_data.append(round)
            cls.play_round(round, tournament)
        winner_list = []    
        for winner in tournament.rounds_data:
            for match in winner.match_list:
                winner_list.append(match.winner)
        ranking = cls.get_ranking(winner_list)
        RoundView.display_ranking(ranking)
        RoundView.display_end_round()


            #TODO Ajout display classement + Message d'aurevoir
            #TODO cette fonction fait trop de chose je dois l'eclater
    
    @staticmethod
    def play_round(r, tournament):
        for match in r.match_list:
            match.winner = RoundView.ask_for_winner(match)
            tournament.save()

    @staticmethod
    def get_ranking(winner_list):
        winners_dict = {}
        for winner in winner_list:
            if winner in winners_dict:
                winners_dict[winner] += 1
            else:
                winners_dict[winner] = 1
        ranking = sorted(winners_dict.items(), key=lambda i: i[1], reverse=True)
        return ranking
