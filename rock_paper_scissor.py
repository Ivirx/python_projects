from random import randint


validAnswerList = ['1', '2', '3', 'q', 'quit']
status = {
    'draw': 0,
    'user': 0,
    'computer': 0
}


def rps(choice):
    return 'Rock' if choice == 1 else 'Paper' if choice == 2 else 'Scissor'


def display():
    print(f'\nYour Wins : {status["user"]}')
    print(f'Draws : {status["draw"]}')
    print(f'Losses : {status["computer"]}\n')


def whoWins(uChoice, cChoice):
    diff = uChoice - cChoice
    print(end='\n\t')
    if diff == 0:
        print('__Draw__')
        status['draw'] += 1
    if diff == 1 or diff == -2:
        print('__You win__')
        status['user'] += 1
    if diff == -1 or diff == 2:
        print('__You loss__')
        status['computer'] += 1

    print('Computer Choice :', rps(cChoice))
    print('Your Choice :', rps(uChoice), end='\n\n')


print('--- Game Starts ---\n')
while True:
    computerChoice = randint(1, 3)

    print('1 Rock, 2 Paper, 3 Scissor or Quit')
    userChoice = input('Input : ')

    if userChoice.isalpha() and userChoice.lower() in validAnswerList:
        # # Player wanst to quit
        print('--- Game Ends ---')
        display()
        break
    elif userChoice.isdigit() and userChoice in validAnswerList:
        # # valid choice and now checking for who wins
        whoWins(int(userChoice), computerChoice)
    else:
        # # wrong input
        print('Oops! Wrong Input Entered!', end='\n\n')
