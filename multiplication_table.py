try:
    userInput = int(input('Enter the number : '))
    table = [userInput * times for times in range(1, 11)]
    print(table)
    # table = [tuple((times, userInput * times)) for times in range(1, 11)]
    # tableDict = dict(table)
    # print(tableDict)
except ValueError:
    print('Enterd Value is not a Integer')
