import inquirer
import re


class PlayerView:
    @classmethod
    def ask_info_player(cls):
        new_p = [
            inquirer.Text("First Name", "What is the First-name of the player ?"),
            inquirer.Text("Last Name", "What is the last-name of the player ?"),
            inquirer.Text(
                "Birthday",
                "Waht is the birthday of the player",
                validate=lambda _, b: cls.validate_birthday(b),
            ),
            inquirer.Text(
                "INE",
                "What is the ine of the player",
                validate=lambda _, i: cls.validate_ine(i),
            ),
        ]
        datas = inquirer.prompt(new_p)

        return datas

    @staticmethod
    def message_end_creation_player():
        print("Player saved !")

    @staticmethod
    def validate_birthday(date):
        if re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{2}$", date):
            return True
        return False

    @staticmethod
    def validate_ine(ine):
        return bool(re.match(r"^[A-Z]{2}\d{5}$", ine))
