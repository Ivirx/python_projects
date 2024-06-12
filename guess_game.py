import random

randomGuess = random.randint(0, 99)
numberOfGuesses = 0
guessedCorrectly = False

print('---- Welcome to Guessing Game ----')
while True:
    userGuess = input('\nEnter Your Guess : ')
    
    if not userGuess.isdigit() and userGuess.lower() in ['q', 'quit']:
        print('\n--- < Thank You for Joining! > ---')
        break

    if not userGuess.isdigit():
        print('!!!  Entered value must be a Number  !!!')
        continue

    numberOfGuesses += 1
    
    userGuess = int(userGuess)
    difference = abs(randomGuess - userGuess)

    if difference == 0:
        print('\n--- You Guessed it correctly! ---')
        guessedCorrectly = True
        break
    elif difference <= 5:
        print('Close')
    elif difference <= 15:
        print('Far')
    else:
        print('Way Far')

print()

if guessedCorrectly:
    with open('high_score.txt') as fileRead:
        highScore = fileRead.read()
        if (not highScore) or int(highScore) > numberOfGuesses:
            print('--- YOU BROKE THE HIGH SCORE ---')
            with open('high_score.txt', 'w') as fileWrite:
                fileWrite.write(str(numberOfGuesses))

print(f'Number was {randomGuess}')
print(f'You took {numberOfGuesses} guesses!')
