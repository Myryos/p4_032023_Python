import inquirer
import re


class TournamentView:
    @classmethod
    def ask_for_info_tournament(cls, players):
        new_t = [
            inquirer.Text("name", message="What is the name of this tournament"),
            inquirer.Text("places", message="Which town?"),
            inquirer.Text(
                "date_start",
                message="Start ?",
                validate=lambda _, d: cls.validate_date(d),
            ),
            inquirer.Text(
                "date_end", message="End ?", validate=lambda _, d: cls.validate_date(d)
            ),
            inquirer.Text(
                "nb_round_total",
                message="Number of maximun round? (A number), Base value : 4",
                validate=lambda _, r: cls.validate_round(r),
            ),
            inquirer.Checkbox("players", message="List of player", choices=players),
            inquirer.Text("description", message="A description of the tournament"),
        ]
        answer = inquirer.prompt(new_t)
        return answer

    def choose_tournament(t):
        question = [
            inquirer.List("Tournament", message="Choose the tournament", choices=t)
        ]
        choice = inquirer.prompt(question)
        return choice["Tournament"]

    def message_tournament_saved():
        print("Tournament Saved !")

    def validate_date(date):
        return re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{2}$", date)

    def validate_round(round: str):
        if round.isdigit() and int(round) >= 1 or round == "":
            return True
        else:
            return False
