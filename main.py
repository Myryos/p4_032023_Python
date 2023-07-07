from Controller.Tournament import TournamentController
from Controller.Player import new_player
from Controller.Round import RoundControl


import inquirer
from sys import exit
from utils import init_folder
from report import manage_report


def get_user_input(dict):
    r = list(dict.values())[0]
    return r


def main():
    init_folder()
    actions = [
        inquirer.List(
            "action",
            message="What do you want to do",
            choices=[
                "Create New Tournament",
                "Create Player",
                "Play a Tournament",
                "Report",
                "Exit",
            ],
        )
    ]
    choices = inquirer.prompt(actions)

    user_input = choices["action"]

    if user_input == "Exit":
        exit()
    if user_input == "Create New Tournament":
        TournamentController.new_tournament()
    if user_input == "Create Player":
        new_player()
    if user_input == "Play a Tournament":
        tournement = TournamentController.select_tournament()
        round_control = RoundControl(tournement)
        round_control.executeRounds(round_control.tournament)
    if user_input == "Report":
        manage_report()


while True:
    main()
