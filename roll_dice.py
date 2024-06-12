import random


dice_drawing = {
    1: (
        '-------',
        '|  1  |',
        '|  •  |',
        '|     |',
        '-------'
    ),
    2: (
        '-------',
        '|•    |',
        '|  2  |',
        '|    •|',
        '-------'
    ),
    3: (
        '-------',
        '|• 3  |',
        '|  •  |',
        '|    •|',
        '-------'
    ),
    4: (
        '-------',
        '|•   •|',
        '|  4  |',
        '|•   •|',
        '-------'
    ),
    5: (
        '-------',
        '|• 5 •|',
        '|  •  |',
        '|•   •|',
        '-------'
    ),
    6: (
        '-------',
        '|•   •|',
        '|• 6 •|',
        '|•   •|',
        '-------'
    )
}

option = input('Roll Dice? ')
while True:
    if option.lower() in ['yes', 'y']:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'Dices are {dice1} and {dice2}')
        print('\n'.join(dice_drawing[dice1]))
        print('\n'.join(dice_drawing[dice2]))

    elif option.lower() in ['no', 'n']:
        print('Thanks For Joining!')
        break

    else:
        print('Invalid Input!')

    option = input('\nRoll Again? ')
