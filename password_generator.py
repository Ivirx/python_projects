import string
import random


characters = list(
    string.ascii_letters + string.digits + '''~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/''')


def generate(password_length):
    global characters
    random.shuffle(characters)
    password = [random.choice(characters) for _ in range(password_length)]

    print('\nYour passwod :', ''.join(password))


option = (input('Length(default:18) Or Quit? ')).lower()
if option in ['quit', 'q', '0', 'yes']:
    print('OK! Quitting.')

elif not option or option.isdigit():
    length = 18 if not option else int(option)
    generate(length)

else:
    print('\nInvalid Input! Try Again!')
