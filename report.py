import inquirer

from Controller.Player import load_players
from Controller.Tournament import TournamentController

DIRECTORY = "report/"

# TODO Faire des choices des constante

# TODO voir pour instaure des template html et genere des .html au lie u de point txt.


def manage_report():
    while 1:
        choice = choose_an_action()

        if choice == "All Players":
            generate_report_players()
        elif choice == "All Tournament":
            generate_report_tournaments()
        elif choice == "Name and dates of a Tournament":
            generate_report_dates_name_tournament()
        elif choice == "Players of a tournament":
            generate_report_player_list_tournament()
        elif choice == "Datas rounds and match list of a tournaments":
            generate_report_rounds_match_list()
        elif choice == "Exit":
            break


def choose_an_action():
    action = [
        inquirer.List(
            "action",
            message="What do you want",
            choices=[
                "All Players",
                "All Tournament",
                "Name and dates of a Tournament",
                "Players of a tournament",
                "Datas rounds and match list of a tournaments",
                "Exit",
            ],
        )
    ]
    choices = inquirer.prompt(action)
    return choices["action"]


def generate_report_players():
    players = load_players()

    players = sorted(players, key=get_player_name)

    with open(f"{DIRECTORY}report_all_players.txt", "w") as report:
        report.write("List of player : \n")
        for player in players:
            report.write("\t")
            report.write(f"Last Name : {player.last_name}")
            report.write(" | ")
            report.write(f"First Name : {player.first_name}")
            report.write(" | ")
            report.write(f"Birthday : {player.birthday} ")
            report.write(" | ")
            report.write(f"INE : {player.ine}")
            report.write("\n")


def generate_report_tournaments():
    # TODO Revoir la mise en forme
    # TODO Regen les match round et players (voir tournaments.load())
    # TODO Arreter de repasser par de to_dict utilise les objets
    tournaments = TournamentController.get_tournaments()

    with open(f"{DIRECTORY}report_all_tournaments.txt", "w") as report:
        report.write("List of tournaments \n")

        for tournament in tournaments:
            report.write("\t")
            report.write(f"Name : {tournament.name} \n")
            report.write(f"\tPlace : {tournament.places} \n")
            report.write(f"\tDate Start : {tournament.date_start} \n")
            report.write(f"\tDate End : {tournament.date_end} \n")
            report.write(f"\tNumber of round : {tournament.nb_round_total} \n")
            report.write(f"\tActual round : {tournament.actual_round_index} \n")
            report.write("\tRounds Data:\n")
            for round_data in tournament.rounds_data:
                report.write("\t\t")
                report.write("\tMatch List:\n")
                for match in round_data.match_list:
                    report.write("\t\t\t")
                    report.write(f"\tplayers : {match.player0}/{match.player1}\n")
                    report.write(f"\t\t\t\tplayed: {match.played}\n")
                    report.write(f"\t\t\t\twinner: {match.winner}\n")
                    report.write("\n")
            report.write("\tPlayers :\n")
            for player in tournament.players:
                report.write("\t\t")
                report.write(f"{player.last_name} {player.first_name}\n")
            report.write("\n")
            report.write(f"\tDescription : {tournament.description}\n")
            report.write("\n")
            report.write("\n")


def generate_report_dates_name_tournament():
    tournament = TournamentController.select_tournament()

    with open(f"{DIRECTORY}report_dates_name_{tournament.name}.txt", "w") as report:
        report.write(
            f"Name : {tournament.name} | Date Debut : {tournament.date_start} | Date End : {tournament.date_end}"
        )
        report.write("\n")


def generate_report_player_list_tournament():
    tournament = TournamentController.select_tournament()
    players = sorted(tournament.players, key=get_player_name)

    with open(f"{DIRECTORY}report_player_{tournament.name}.txt", "w") as report:
        report.write(f"List of Player from  {tournament.name}\n")
        for player in players:
            report.write("\t")
            report.write(f"Last Name : {player.last_name}")
            report.write(" | ")
            report.write(f"First Name : {player.first_name}")
            report.write(" | ")
            report.write(f"Birthday : {player.birthday} ")
            report.write(" | ")
            report.write(f"INE : {player.ine}")
            report.write("\n")


def generate_report_rounds_match_list():
    # TODO Ajouter la selection du tournoi
    # TODO Bonus  regen les objet player
    tournament = TournamentController.select_tournament()
    with open(f"{DIRECTORY}report_rounds_datas_{tournament.name}.txt", "w") as report:
        report.write(f"\t{tournament.name} Rounds Data:\n")
        for round_data in tournament.rounds_data:
            report.write("\t\t")
            report.write("\tMatch List:\n")
            for match in round_data.match_list:
                report.write("\t\t\t")
                report.write(f"\tplayers : {match.player0}/{match.player1}\n")
                report.write(f"\t\t\t\tplayed: {match.played}\n")
                report.write(f"\t\t\t\twinner: {match.winner}\n")
                report.write("\n")


def get_player_name(player):
    return player.last_name
