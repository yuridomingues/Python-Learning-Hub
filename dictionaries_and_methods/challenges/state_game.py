"""Create a "state game". In this game, the player needs to answer
the name of the capital of each state in Brazil. The game should ask
the user "What is the capital of State X?" and check if the user
answered correctly. After each question, the user can choose
to stop the game or continue to the next question. When the user
decides to stop or when all questions have been answered,
the code shows the raw number and percentage of correct answers."""

def state_game():
    """
    State game
    """
    count = 0  # Total number of questions
    correct = 0  # Number of correct answers
    state_capitals = {
        'Acre': 'Rio Branco',
        'Alagoas': 'Maceio',
        'Amapa': 'Macapa',
        'Amazonas': 'Manaus',
        'Bahia': 'Salvador',
        'Ceara': 'Fortaleza',
        'Distrito Federal': 'Brasilia',
        'Espirito Santo': 'Vitoria',
        'Goias': 'Goiania',
        'Maranhao': 'Sao Luis',
        'Mato Grosso': 'Cuiaba',
        'Mato Grosso do Sul': 'Campo Grande',
        'Minas Gerais': 'Belo Horizonte',
        'Para': 'Belem',
        'Paraiba': 'Joao Pessoa',
        'Parana': 'Curitiba',
        'Pernambuco': 'Recife',
        'Piaui': 'Teresina',
        'Rio de Janeiro': 'Rio de Janeiro',
        'Rio Grande do Norte': 'Natal',
        'Rio Grande do Sul': 'Porto Alegre',
        'Rondonia': 'Porto Velho',
        'Roraima': 'Boa Vista',
        'Santa Catarina': 'Florianopolis',
        'Sao Paulo': 'Sao Paulo',
        'Sergipe': 'Aracaju',
        'Tocantins': 'Palmas'
    }

    for state, capital in state_capitals.items():
        print(f"What is the capital of {state}?")
        answer = input()
        count += 1
        if answer == capital:
            correct += 1
            print("Correct!")
        else:
            print("Wrong!")

        print("Do you want to stop the program? 's' for yes, anything else for no")
        stop_game_input = input()
        if stop_game_input == 's':
            stop_game(count, correct)
            break

    stop_game(count, correct)


def stop_game(count, correct):
    """
    Function to end the game
    """
    percentage = (correct / count) * 100 if count > 0 else 0

    print('Thank you for playing!')
    print(f'Your final score is: {correct} correct answer(s) and the percentage of {percentage}%')
    exit()


if __name__ == "__main__":
    state_game()
