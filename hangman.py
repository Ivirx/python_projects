from hangman_utils import words, lives_visual_dict
import random
import string


def select_random():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word


word = select_random().upper()
word_letters = set(word)
alphabets = set(string.ascii_uppercase)
letters_used = set()

word_len = len(word)
_word = ' '.join(word)
guessed_word = \
    ' '.join([letter if letter in letters_used else '-' for letter in word])
lives = len(lives_visual_dict) - 1

print("\033c", end="")

while True:
    print(lives_visual_dict[lives])
    print(f'You have {lives} lives left. {guessed_word} ({word_len})')

    user_input = input('Enter your guess letter : ').upper()
    print()

    if user_input in letters_used:
        print(f'You have already used letter \'{user_input}\'.')
        continue

    if user_input not in alphabets:
        print(' Wrong Input! '.center(32, '✕'))

        continue

    letters_used.add(user_input)

    if user_input not in word_letters:
        print(' Wrong Guess! '.center(32, '*'))
        lives -= 1

        if lives <= 0:
            print('\n----------------------------')
            print(lives_visual_dict[lives])
            print('You have lost all you lives.')
            print(f'Word was : {_word}')
            print('\n----------------------------\n')

            break

        continue

    # letter is correct and in word_letter
    guessed_word = \
        ' '.join([letter if letter in letters_used else '-' for letter in word])

    if _word == guessed_word:
        print('\n----------------------------\n')
        print('you guessed it!'.upper())
        print(f'Word was : {guessed_word}')
        print('\n----------------------------\n')

        break
