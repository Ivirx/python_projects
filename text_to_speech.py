import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

names = ['Utkarsh', 'Hariom', 'Ayush', 'Ayush', 'Aagman', 'Dhananjay']

for name in names:
    engine.say(f'Shoutout to {name}')

engine.runAndWait()
