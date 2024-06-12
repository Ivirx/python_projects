import random


def randNo():
    return random.randint(97, 122)


def encode(word):
    moveBy = randNo()

    newWord = []
    for char in word:
        if char.isalpha():
            newWord.append(chr((((ord(char) + moveBy) % 97) % 26) + 97))

    return chr(randNo())+(''.join(newWord))+chr(moveBy)


def decode(word):
    movedBy = word[-1]
    wordWithout = word[1:-1]

    newWord = []
    for char in wordWithout:
        if char.isalpha():
            if (ord(char) - ord(movedBy)) >= 0:
                newWord.append(chr((abs(ord(char) - ord(movedBy)) + 97)))
            else:
                newWord.append(chr(123 - (abs(ord(movedBy) - ord(char)))))

    return ''.join(newWord)


choiceParameters = ['encode',  'e', 'decode', 'd']

string = (input('Enter the string : ')).lower()
choice = (input('Encode or Decode ? ')).lower()

if choice in choiceParameters:
    strArr = string.split()
    mutatedStr = []

    for word in strArr:
        mutatedStr.append(encode(word)) if choice in choiceParameters[:2] else mutatedStr.append(decode(word))

    print(' '.join(mutatedStr))
else:
    print('!!-- Failed --!!')
