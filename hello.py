from art import logo

print('Welcome to "Blink Auction Program"')


def highest_bid(bidding_record):
    highest = 0
    bidder = ''
    # print(bidding_record)
    for key in bidding_record:
        if highest < bidding_record[key]:
            highest = bidding_record[key]
            bidder = key
    print(f'{bidder} won the bid with {highest}$')
print(logo)
bidder = {}
bidding_continue = False
while not bidding_continue:
    name = input('What is your name ?\n')
    bid = int(input('Enter Your Bid Amount. $'))
    bidder[name] = bid
    bid_contnue = input('Are there any other bidders ? type\'yes\' or \'no\' : ').lower()
    if bid_contnue == 'no':
        bidding_continue = True
        highest_bid(bidder)