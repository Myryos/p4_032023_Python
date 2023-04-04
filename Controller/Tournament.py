import inquirer
import re
from Models import Tournament as TClass
from Models.Player import Player as PClass
from View import Tournament as TView

def new_tournament():
    new_t = [inquirer.Text('name', message='What is the name of this tournament'),
             inquirer.Text('places', message='Wich town?'),
             inquirer.Text('date_start', 
                           message='Start ?',
                           validate = lambda _, d: TClass.Tournament.validate_attribute('date', d)),
             inquirer.Text('date_end', 
                           message='End ?',
                           validate = lambda _,d: TClass.Tournament.validate_attribute('date', d)),
             inquirer.Text('round_max', 
                           message="Number of maximun round? (A number), Base value : 4",
                           validate = lambda _, r : TClass.Tournament.validate_attribute('round_max', r)), 
             inquirer.Checkbox('player_list', message="List of player",choices=PClass.load_players()),
             inquirer.Text('description', message='A description of the tournament')
             ]
    answer = inquirer.prompt(new_t)

    if answer['round_max'] != "":

        tournament = TClass.Tournament(answer['name'], 
                                   answer['places'],
                                   answer['date_start'],
                                   answer['date_end'], 
                                   answer['player_list'], 
                                   answer['description'],
                                   int(answer['round_max']))
    else:
         tournament = TClass.Tournament(answer['name'], 
                                   answer['places'],
                                   answer['date_start'],
                                   answer['date_end'], 
                                   answer['player_list'], 
                                   answer['description'])
    tournament.save_tournament()

    TView.message_tournament_saved()
         

        



