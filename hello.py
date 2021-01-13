import random
from Day_14_game_data import data
from Day_14_Art import art
from Day_14_Art import vs

score = 0
game_play = False
while not game_play:
    first = random.randint(0,len(data)-1)
    second = random.randint(0,len(data)-1)
    print('Compare A:', end=' ')
    for f in data[first].values():
        print(f, end=',')

    print(f'\n',vs)

    print('Compare B:', end=' ')
    for f in data[second].values():
        print(f, end=',')

    choice = input('\n\nWho has more folloers? Type \'A\' or \'B\': ').lower()
    if choice == 'a':
        if data[first]['follower_count'] > data[second]['follower_count'] :
            score += 1
    elif choice == 'b':
        if data[first]['follower_count'] < data[second]['follower_count'] :
            score += 1 
    else:
        game_play = True
    print(data[first]['follower_count'])
    print(data[second]['follower_count'])
    print(f'Your Final Score is {score}')