from Models.Tournament import TournamentModel
from Models.Player import PlayerModel
from View.Tournament import TournamentView


class TournamentController:
    @classmethod
    def new_tournament(cls):
        players = cls.get_players()
        answer = TournamentView.ask_for_info_tournament(players)

        if answer["nb_round_total"] != "":
            answer["nb_round_total"] = int(answer["nb_round_total"])
        else:
            answer["nb_round_total"] = 4

        tournament = TournamentModel(**answer)
        tournament.save()

        TournamentView.message_tournament_saved()

    @staticmethod
    def get_players():
        players = PlayerModel.load_players()
        return players

    @staticmethod
    def get_tournaments():
        tournaments = TournamentModel.load()
        return tournaments

    @classmethod
    def select_tournament(cls):
        tournaments = cls.get_tournaments()
        tournament = TournamentView.choose_tournament(tournaments)
        return tournament

    @staticmethod
    def show_ranking(tournament):
        tournament.calculate_ranking()
        TournamentView.display_ranking(tournament.players)
