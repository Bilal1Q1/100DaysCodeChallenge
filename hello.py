import random
import art
print(art.logo)


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
user_cards = []
machine_cards = []
game_over = False
for _ in range(2):
    user_cards.append(deal_card())
    machine_cards.append(deal_card())
print(f'\tyour cards: {user_cards}, current score: {sum(user_cards)}')
print(f'\tcomputer\'s first card: {machine_cards[0]}')
while not game_over:
    continue_or_pass = input('Type \'y\' to get another card, type \'n\' to pass:\t').lower()
    if continue_or_pass == 'y':
        user_cards.append(deal_card())
        machine_cards.append(deal_card())
        print(f'\tyour cards: {user_cards}, current score: {sum(user_cards)}')
        print(f'\tcomputer\'s first card: {machine_cards[0]}')
    else:
        game_over = True

print(user_cards)
print(machine_cards)