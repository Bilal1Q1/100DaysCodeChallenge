import random
from Day_14_game_data import data
from Day_14_Art import art
from Day_14_Art import vs


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
