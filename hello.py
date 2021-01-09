import random
from art import logo
def deal_card():  #This Function give me a random card
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def compare(my_score,computer_score): # returning the appropriate print satatement according to user and computer score
    if my_score == computer_score:
        return 'Draw!'
    if my_score == 0:
        return 'Win with a BlackJack 😂'
    elif computer_score == 0:
        return 'Lose ! opponent has Blackjack 😥'
    elif my_score > 21:
        return 'You went over, you lose 😮'
    elif computer_score > 21:
        return 'Win ! opponent has went over 😛'    
    elif  my_score > computer_score:
        return 'Win !🤩' 
    else:
        return 'lose !'

def calculate_score(cards): #give cards of user or computer and calculate the score using sum() function
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

print(logo)
user_cards = []
machine_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    machine_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    machine_score = calculate_score(machine_cards)
    print(f"\tYour cards: {user_cards}, current score: {user_score}")
    print(f"\tComputer's first card: {machine_cards[0]}")
    if user_score == 0 or machine_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
while machine_score != 0 and machine_score < 17:
    machine_cards.append(deal_card)
    machine_acore = calculate_score(machine_cards)
print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {machine_cards}, final score: {machine_score}")
print(compare(user_score, machine_score))

