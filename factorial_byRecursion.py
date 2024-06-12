def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num - 1)


number = int(input('Enter the number : '))
print(f'Factorial of {number} is {factorial(number)}')
# this is comment