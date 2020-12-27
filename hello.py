import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words_list =['ardvark','baboon','camel']
word = random.choice(words_list)
word_length = len(word)
print(f'The choosen word is {word}')

display = []
for j in range(word_length):
    display.append('-')

game_over = False
while not game_over:
    guess = input("Enter a letter\n").lower()
    for i in range(word_length):
        if guess == word[i]:
            display[i] = word[i]
    print(display)
    if '-' not in display:
        game_over = True
        print('You Win ')