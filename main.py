from Controller.Tournament import TournamentController
from Controller.Player import new_player
from Controller.Round import RoundControl


from Models.Round import Round
import inquirer
from sys import exit
from utils import init_folder
#import bcolors

def get_user_input(dict):
    r = list(dict.values())[0]
    return r

def main():
    init_folder()
    actions =[
    inquirer.List('action', message='What do you want to do',
                  choices=['Create New Tournament', 'Create Player', 'Test Generate Rounds' ,'Exit'])]
    choices = inquirer.prompt(actions)

    user_input = choices['action']

    if user_input == "Exit":
        exit()
    if user_input == 'Create New Tournament':
        new_t = TournamentController.new_tournament()
    if user_input == 'Create Player':
        new_player()
    if user_input == 'Loading Tournament':
        pass
    if user_input == 'Test Generate Rounds':
        RoundControl.new_round()

        #Round.generate_rounds(TournamentController.get_players())


while True:
    main()
    



   
    