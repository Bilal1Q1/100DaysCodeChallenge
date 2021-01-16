from random import choice
from Day_14_Art import art, vs
from Day_14_game_data import data


def format_data(account):
    user_name = account['name']
    #FIXME Remove it after Completion
    user_follower = account['follower_count'] 
    user_description = account['description']
    user_country = account['country']
    return f'{user_follower} {user_name}, a {user_description}, from {user_country}'

def who_winner(guess, user_a_score, user_b_score):
    if user_a_score > user_b_score :
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
game_over = False
user_b = choice(data)

#TODO from here repated while game_over is False
while not game_over:
    user_a = user_b
    user_b = choice(data)
    user_a_followers = user_a['follower_count']
    user_b_followers = user_b['follower_count']

    if user_a == user_b:
        user_b = choice(data)
    print('Champare A: ',format_data(user_a))
    print(vs)
    print('Against B: ',format_data(user_b))

    guess = input('\nWho has more follwer ? \'a\' or \'b\'').lower()
    if who_winner(guess, user_a_followers, user_b_followers):
        score += 1
        print(f'You are right. Current score is {score}\n')
    else:
        game_over = True
        print(f'Sorry, thats wrong. Final score: {score}')
