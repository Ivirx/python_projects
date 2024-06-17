import random


max_centered_characters = 80
max_score = 10


def print_line(char='-'):
    '''Prints a line in a formatted way'''

    print('\n' + ''.center(max_centered_characters, char), end='\n\n')


def print_welcome_message():
    '''Prints the Welcome Message'''

    print("\033c", end="")
    print_line('⁘')
    print('Welcome to Gamble Game'.center(max_centered_characters, ' '))
    print_line('⁘')


def init_players():
    '''Forms a player array'''

    no_of_players = int(input('Enter the number of players : '))
    players = []

    while (True):
        should_name_the_players = input(
            'Wanna name the players? (y) : '
        ).lower()
        if not should_name_the_players or should_name_the_players in ['y', 'yes']:
            for index in range(no_of_players):
                name = input(f'Enter player {index+1} name : ')
                players.append({'name': name, 'score': 0})

            break

        elif should_name_the_players in ['n', 'no']:
            for index in range(no_of_players):
                players.append({'name': f'Player {index+1}', 'score': 0})

            break

        else:
            print('Wrong Input!')
            continue

    return (no_of_players, players)


def print_players(players, display_message='Players\' Score : '):
    print(f'\n{display_message}')
    for player in players:
        print(f'{player['name']} | {player['score']}')
    print()


def start_game(no_of_players, players):
    print_line()
    print('  Game Starts Now  '.center(max_centered_characters, '-'))
    print_line()

    game_turn = 0
    roll_message = 'Do you want to roll the dice? (y) : '

    while (True):
        index = game_turn % no_of_players
        player = players[index]

        print(f'\n{player['name']}\'s turn | Score : {player['score']}')
        user_input = input(roll_message).lower()
        if user_input == 'quit':
            print_players(players, 'Players\' last score : ')
            print(' Thank you for playing! '
                  .center(max_centered_characters, '⁘'), end='\n\n\n')
            break

        if user_input == 'score':
            print_players(players)
            continue

        if not user_input or user_input in ['yes', 'y']:
            dice = random.randint(1, 6)
            print(f'Dice rolled to : {dice}')
            if dice == 1:
                print(
                    '\nBetter Luck next time! '
                    .ljust(int(max_centered_characters/2), '✕')
                )
                player['score'] = 0
                roll_message = 'Do you want to roll the dice? (y) : '
                game_turn += 1

            else:
                player['score'] += dice

                if player['score'] >= max_score:
                    print(
                        f'\n{player['name']} has won the game! '
                        .ljust(max_centered_characters, '-')
                    )
                    print_players(players, 'Scores are : ')
                    print(' Thank you for playing! '
                          .center(max_centered_characters, '⁘'), end='\n\n\n')
                    break

                roll_message = 'Roll again? (y) : '
                continue

        elif user_input in ['no', 'n']:
            roll_message = 'Do you want to roll the dice? (y) : '
            game_turn += 1
            continue

        else:
            print('Wrong Input!')
            continue


def main():
    print_welcome_message()
    no_of_players, players = init_players()

    print_players(players, 'Players are : ')
    start_game(no_of_players, players)


if __name__ == '__main__':
    main()
