import random

historyDates = [
    ['When did the World War I begin?',  1914],
    ['When did the World War I end?',    1918],
    ['When did the World War II begin?', 1939],
    ['When did the World War II end?',   1945]
]

failedVariants = []

startGame = input('Let the game begin? Y/N')

if startGame == 'N' or startGame == 'n':
    print('Good bye')
elif startGame == 'Y' or 'y':
    userName = input('Input your name:')
    while len(historyDates) > 0:
        ask = random.choice(historyDates)
        inp = int(input(f'{ask[0]}'))
        if inp == ask[1]:
            print(f'Alright, {userName}!')
            historyDates.remove(ask)
        else:
            print('Not right!')
            failedVariants.append(inp)
    else:
        print('This was a good game!')
        if len(failedVariants) > 0:
            print(f'Yor failed answers list, {userName}: ', failedVariants)
