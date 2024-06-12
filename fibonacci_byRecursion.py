def fibonacci(secondLastNum, lastNum, position, toDigit):
    print(secondLastNum, end='  ')
    if (position == toDigit or toDigit == 0):
        return
    nextNum = lastNum+secondLastNum
    fibonacci(lastNum, nextNum, position+1, toDigit)


number = int(input('Enter the number : '))
print('Fibonacci Series :')
fibonacci(0, 1, 1, number)
