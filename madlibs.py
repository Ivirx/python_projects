story = '''Rain lashed the window as <name> munched on a soggy <adjective> sandwich. A glint of <color> caught their eye - a tiny spaceship nestled in their flowerpot! A message flickered: "Help! Trapped on <place>! Bring a <noun>!" <name> rummaged in their toolbox, grabbing a <adjective> wrench. With a grin, they squeezed into the ship and blasted off, ready for an adventure!'''


def extract_placeholders(story):
    placeholders = set()
    starts_at = 0

    for i, word in enumerate(story):
        if word == '<':
            starts_at = i
        if word == '>':
            placeholders.add(story[starts_at:i+1])

    return sorted(placeholders, key=lambda word: story.find(f"{word}"))


def take_user_inputs(placeholders):
    answers = {}

    print('\n----------------------------\n')
    print('Enter the following inputs : ')
    for word in placeholders:
        answers[word] = input(f'{word} : ')

    return answers


def replace_words(story: str, answers):
    new_story = story

    for answer in answers:
        new_story = new_story.replace(answer, answers[answer])

    return new_story


placeholders = extract_placeholders(story)
answers = take_user_inputs(placeholders)
new_story = replace_words(story, answers)
print('\n----------------------------\n')
print(new_story)
print('\n----------------------------\n')
