allQuestions = [
    {
        'question': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias ab error laborum?',
        'options': ['Aliquam', 'Obcaecati', 'Deserunt', 'Voluptateveniam'],
        'answer': 'a'
    },
    {
        'question': 'Dolores dolorum ab recusandae, autem quidem doloribus magnam sint unde officia quo accusantium error?',
        'options': ['Exercitationem', 'Voluptatibus', 'Soluta', 'Cupiditate'],
        'answer': 'b'
    },
    {
        'question': 'Fugiat corrupti a pariatur dolore voluptates deserunt cupiditate ea autem temporibus placeat, eveniet iusto fuga architecto?',
        'options': ['Laboriosam', 'Nesciunt', 'Voluptatem', 'Distinctio'],
        'answer': 'a'
    },
    {
        'question': 'Sapiente expedita dolorum quae similique error quas qui explicabo aspernatur repudiandae sed vero consequatur natus?',
        'options': ['Temporibus', 'Assumenda', 'Consequatur', 'Dolore'],
        'answer': 'c'
    },
    {
        'question': 'Quos iste natus voluptatem maxime. Voluptatibus nobis sed itaque fugit laudantium animi, esse hic obcaecati ipsam impedit?',
        'options': ['Ipsum', 'Itaque', 'Laudantium', 'Quaerat'],
        'answer': 'd'
    }
]

valid_answers = ['a', 'b', 'c', 'd']

moneyWon = 0
correctAnswers = 0

print('--- Game Starts ---')

quesNo = 0
while quesNo < len(allQuestions):
    question = allQuestions[quesNo]['question']
    options = allQuestions[quesNo]['options']
    answer = allQuestions[quesNo]['answer']

    print(question)
    for optNo in range(len(options)):
        print(chr(97 + optNo), ':', options[optNo])

    choice = input('Enter the choice(a-d): ').lower()
    if choice not in valid_answers:
        print('\n!!! -- Please type a valid choice -- !!!\n')
        continue

    if choice == answer:
        correctAnswers += 1
        moneyWon += (500 * correctAnswers)
        print('\n₹₹ Correct Answer ₹₹')
    else:
        print('\n!!! -- Wrong Answer -- !!!')

    print('\nTill Now >>')
    print('Total Prize Money : ', moneyWon,)
    print('Total Correct Answers: ', correctAnswers, end='\n\n\n')

    if quesNo != len(allQuestions) - 1:
        print('Next Question : ')

    quesNo += 1

print('--- Game Ends ---')
print('You Won : ₹', moneyWon)
print('With', correctAnswers, 'correct answers!')
