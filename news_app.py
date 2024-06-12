import requests
from os import environ
from dotenv import load_dotenv
# from datetime import datetime

load_dotenv()
api_key = environ.get('NEWS_API_KEY')
baseUrl = f'https://newsapi.org/v2/top-headlines?apiKey={api_key}&country=in&pageSize=10'
categories = {
    1: 'general',
    2: 'business',
    3: 'entertainment',
    4: 'health',
    5: 'science',
    6: 'sports',
    7: 'technology'
}
pageNumber = {'current': 0, 'maximum': None}


def display():
    print('0-> Top Headlines\t1-> General\t\t2-> Business')
    print('3-> Entertainment\t4-> Health\t\t5-> Science')
    print('6-> Sports\t\t7-> Technology\t\tq-> Quit')


def fetchNew(fetchUrl, pageNo):
    pageNumber['current'] = pageNo

    response = requests.get(f'{fetchUrl}&page={pageNo}')
    data = response.json()
    pageNumber['maximum'] = (data['totalResults'] // 10) + 1

    articles = data['articles']
    for number, article in enumerate(articles):
        print(f'\n{((pageNo-1)*10) + number + 1} : {article["title"]}')


print('\n\t\t--- Welcome to DailyNews ---\n')
while True:
    pageNumber['current'] = 0
    pageNumber['maximum'] = None
    display()
    userInput = input('\nChoice : ')
    if userInput.lower() in ['q', 'quit']:
        break

    if not userInput in ['0', '1', '2', '3', '4', '5', '6', '7']:
        print('\n!!! Wrong Input !!!\n')
        continue

    userInput = int(userInput)

    fetchUrl = baseUrl
    if userInput != 0:
        fetchUrl = f'{fetchUrl}&category={categories[userInput]}'

    fetchNew(fetchUrl, pageNumber['current'] + 1)

    while True:
        print('\np->previous\tn->Next Page\tm->Main Menu')
        innerUserInput = input('Choice : ')

        if not innerUserInput.lower() in ['p', 'n', 'm']:
            print('\n!!! Wrong Input !!!')
            continue

        if innerUserInput.lower() == 'p':
            if pageNumber['current'] == 1:
                print('Can\'t Go Beyond this!')
                continue

            fetchNew(fetchUrl, pageNumber['current']-1)

        if innerUserInput.lower() == 'n':
            if pageNumber['current'] == pageNumber['maximum']:
                print('!! Can\'t Go Beyond this !!')
                continue

            fetchNew(fetchUrl, pageNumber['current']+1)

        if innerUserInput.lower() == 'm':
            break
        
print('\nThank you for Joining with Us!')


# for number, article in enumerate(articles):
#     print(f'\n\n{number+1}')
#     print(article['title'])
#     print(article['description'])
#     published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
#     print(published_at.strftime('%I:%M%p %a, %d %b'))
#     print(article['url'])
