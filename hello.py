import random
words_list =['ardvark','baboon','camel']
word = random.choice(words_list)
word_length = len(word)
print(f'The choosen word is {word}')

display = []
for j in range(word_length):
    display.append('-')

while '-' in display:
    guess = input("Enter a letter\n").lower()
    for i in range(word_length):
        if guess == word[i]:
            display[i] = word[i]
    print(display)
print('You win')

