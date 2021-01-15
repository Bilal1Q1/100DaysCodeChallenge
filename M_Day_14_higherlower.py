import random
from Day_14_game_data import data
from Day_14_Art import art
from Day_14_Art import vs
print(art)
score = 0
game_play = False
while not game_play:
    first = random.randint(0,len(data)-1)
    second = random.randint(0,len(data)-1)
    first_player = data[first]['follower_count']
    second_player = data[second]['follower_count']
    print(f"Compare A: {data[first]['name']}, a {data[first]['description']}, from {data[first]['country']}")
    print(f'\n',vs)
    print(f"Compare B: {data[second]['name']}, a {data[second]['description']}, from {data[second]['country']}")


    choice = input('\n\nWho has more folloers? Type \'A\' or \'B\': \n').lower()
    if choice == 'a' and first_player >= second_player:
        score += 1
    elif choice == 'b' and first_player <= second_player:
        score += 1 
    else:
        game_play = True
        print('Wrong Choice !')
    print(f'Your Final Score is {score} \n')