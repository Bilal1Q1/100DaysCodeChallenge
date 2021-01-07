import random
import art
print(art.logo)


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
user_cards = []
machine_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    machine_cards.append(deal_card())

print(user_cards)
print(machine_cards)