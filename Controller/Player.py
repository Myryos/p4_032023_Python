import inquirer
from Models import Player as PClass

def new_player():
    new_p = [inquirer.Text('First Name',
                           'What is the First-name of the player ?'),
             inquirer.Text('Last Name', 
                           'What is the last-name of the player ?'),
             inquirer.Text('Birthday', 
                           'Waht is the birthday of the player', 
                           validate= lambda _, b: PClass.Player.validate_attribute('birthday', b)),
             inquirer.Text('INE', 
                           'What is the ine of the player', 
                           validate= lambda _, i: PClass.Player.validate_attribute('ine', i))]
    datas = inquirer.prompt(new_p)
        
        
    player = PClass.Player(datas['Last Name'], datas['First Name'], datas['Birthday'], datas['INE'])


    player.save_player()

