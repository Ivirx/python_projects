number_sub = '₀₁₂₃₄₅₆₇₈₉'


def print_board(board_state):
    for index, state in enumerate(board_state, 1):
        if state:
            print(f' {state} ', end='')
        else:
            print(f' {number_sub[index]} ', end='')

        if (not index % 3) and index != 9:
            print('\n---|---|---')
        elif index != 9:
            print('|', end='')


def handle_position(player_turn, symbol, state):
    choice = input(f'\n\nPlayer {player_turn} ({symbol}\'s) turn : ')
    print('\n')
    if choice and choice.isdigit() and int(choice) <= 9 and int(choice) >= 1:
        choice = int(choice)

        if not state[choice-1]:
            state[choice-1] = symbol
            return True
        else:
            print('!!! Position is already taken, enter a different position !!!\n')
            return False

    else:
        print('!!! Wrong Position, enter a valid position !!!\n')
        return False


def check_if_three(index_one, index_two, index_three, state):
    one = state[index_one-1]
    two = state[index_two-1]
    three = state[index_three-1]
    if (
            one != 0 and two != 0 and three != 0  # all have value, either '@' or '#'
            and one == two and two == three and three == one  # check if all match or not
    ):
        return {
            'win': True,
            'message': f'Winner : Player {"1" if one == "@" else "2"} ({one})'
        }

    return {
        'win': False,
        'message': 'Not Yet!'
    }


def who_wins(state):
    for i in range(1, 10):
        if i == 2 or i == 5 or i == 8:  # horizontal checking
            result = check_if_three(i-1, i, i+1, state)
            if result['win']:
                break

        if i == 4 or i == 5 or i == 6:  # verticall checking
            result = check_if_three(i-3, i, i+3, state)
            if result['win']:
                break

        if i == 5:  # diagonal checking
            result = check_if_three(i-4, i, i+4, state)  # left diagonal
            if result['win']:
                break

            result = check_if_three(i-2, i, i+2, state)  # right diagonal
            if result['win']:
                break

    if result['win']:
        return result

    return {'win': False}


def main():
    state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player_turn = 1  # 1 for '@' & 2 for '#'

    while True:
        print_board(state)

        result = who_wins(state)
        if result['win']:
            print('\n\n', result['message'])
            break
        if all(state):
            print('\n\n', "It's a Tie!")
            break

        is_position_correct = handle_position(
            1, '@', state) if player_turn == 1 else handle_position(2, '#', state)
        if is_position_correct:
            player_turn = 1 if player_turn == 2 else 2

    print('--- Thanks for Playing! ---')


if __name__ == '__main__':
    main()
