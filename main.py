from Controller import Tournament as CMethod
from Controller.Player import new_player
import inquirer
from sys import exit
from utils import init_folder, init_files
#import bcolors

def get_user_input(dict):
    r = list(dict.values())[0]
    return r

def main():
    init_folder()
    init_files()
    actions =[
    inquirer.List('action', message='What do you want to do',
                  choices=['Create New Tournament', 'Create Player', 'Exit'])]
    choices = inquirer.prompt(actions)

    user_input = choices['action']

    if user_input == "Exit":
        exit()
    if user_input == 'Create New Tournament':
        new_t = CMethod.new_tournament()
    if user_input == 'Create Player':
        new_player()
    if user_input == 'Loading Tournament':
        pass

while True:
    main()
    



   
    