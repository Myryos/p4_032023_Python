import os


def init_folder():
    if not os.path.exists('report'):
        os.mkdir('report')
    if not os.path.exists('json'):
        os.mkdir('json')
    if not os.path.exists('json/tournament'):
        os.mkdir('json/tournament')
    if not os.path.exists('json/player'):
        os.mkdir('json/player')

def init_files():
     filename = 'json/player/players.json'
     if os.path.isfile(filename) is False:
        open(filename, 'w')