import inquirer


class RoundView:
    def choose_actions():
        actions = [
            inquirer.List(
                "action",
                message="What do you want to do",
                choices=["Play Round", "Display Ranking", "Exit"],
            )
        ]
        choices = inquirer.prompt(actions)
        return choices["action"]

    def continue_exit():
        actions = [
            inquirer.List(
                "action",
                message="Do you want to continue ?",
                choices=["Continue", "Exit"],
            )
        ]
        choices = inquirer.prompt(actions)
        return choices["action"]

    def choose_tournament(t):
        question = [
            inquirer.List("Tournament", message="Choose the tournament", choices=t)
        ]
        choice = inquirer.prompt(question)
        return choice["Tournament"]

    def display_round(r):
        print(f"Round #{r} \n")

    def ask_for_winner(match):
        choices = [match.player0, match.player1, "Draw", "Exit"]
        question = [inquirer.List("Winner", message="Who win ? ", choices=choices)]

        answer = inquirer.prompt(question)
        return answer["Winner"]

    def display_ranking(ranking):

        print("Rankings : \n")

        """for i, (player, wins) in enumerate(ranking, 1):
            print(f'{i}. {player}: {wins} wins')"""
        for (key, value) in ranking:
            print(f" {key} : {value} wins")

    def display_end_round():
        print("Fin du round \n")
