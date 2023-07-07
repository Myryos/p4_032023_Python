from Models.Player import PlayerModel
from View.Player import PlayerView


def new_player():
    datas = PlayerView.ask_info_player()

    player = PlayerModel(
        datas["Last Name"], datas["First Name"], datas["Birthday"], datas["INE"]
    )

    player.save_player()
    PlayerView.message_end_creation_player()


def load_players():
    return PlayerModel.load_players()
