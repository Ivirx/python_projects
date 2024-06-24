import random


def guess(min_limit, max_limit):

    print(f"""
**************************************

Hey there! Let's play a guessing game. Think of a number between {min_limit} and {max_limit}.

I'll try my best to guess what it is with some yes or no questions.

Ready? Press Enter to start!

**************************************""")
    input('')

    min = min_limit
    max = max_limit

    while True:
        guess_number = random.randint(min, max)

        user_feedback = input(f'Is {guess_number} the number? Low (L), High (H) or Correct (C) : ')\
            .lower()
        if user_feedback == 'c':
            print(f'The number you\'r are thinking of is \'{guess_number}\'.')
            break

        if user_feedback == 'l':
            min = guess_number + 1
        elif user_feedback == 'h':
            max = guess_number - 1
        else:
            print('Wrong Input!\n')
            continue

        if (min > max_limit or max < min_limit):
            min = random.randint(min_limit, max_limit)
            max = random.randint(min_limit, max_limit)
        if (min > max):
            min, max = max, min


guess(1, 99)
