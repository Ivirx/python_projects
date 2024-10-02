import string


def is_pangram(input_string):
    input_string = input_string.lower()
    alphabet = set(string.ascii_lowercase)
    letters_in_str = set(input_string)

    return alphabet.issubset(letters_in_str)


input_string = input("Enter the string : ")
print(f'The string is{' ' if is_pangram(input_string) else ' not '}a Pangram.')

# if is_pangram(input_string):
#     print('The string is a Pangram.')
# else:
#     print('The string is not a Pangram.')
