import inquirer

class RoundView():


    def choose_tournament(t):
        question = [inquirer.List('Tournament', message='Choose the tournament', choices=t)]
        choice = inquirer.prompt(question)
        return choice['Tournament']
    
    def display_round(r):
        print(f'Round #{r} \n')

    def ask_for_winner(match):
        choices = [match.player0, match.player1]
        question = [inquirer.List('Winner', message="Who win ? ", choices=choices)]

        answer = inquirer.prompt(question)
        return answer['Winner']
    
    def display_ranking(ranking):

        print('Rankings : \n')
        for i, (player, wins) in enumerate(ranking, 1):
            print(f'{i}. {player}: {wins} wins')
    def display_end_round():
        print('Fin du round \n')

