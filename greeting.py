from time import strftime

hourOfTHeDay = int(strftime('%H'))
time = strftime('%H:%M%p').lower()

if (hourOfTHeDay >= 5 and hourOfTHeDay < 12):
    print('Good Morning!', time)
elif (hourOfTHeDay >= 12 and hourOfTHeDay < 16):
    print('Good Afternoon!', time)
elif (hourOfTHeDay >= 16 and hourOfTHeDay < 20):
    print('Good Evening', time)
else:
    print('Good Night!', time)
