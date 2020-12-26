import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []
no_of_letters = int(input("How many Lettes your Password have ?\n"))
no_of_numbers = int(input("How many Numbers your Password have ?\n"))
no_of_symbols = int(input("How many Symbols your Password have ?\n"))

for i in range(1, no_of_letters +1):
    password_list += random.choice(letters)
for j in range(1, no_of_numbers +1):
    password_list += random.choice(numbers)
for k in range(1, no_of_symbols +1):
    password_list += random.choice(symbols)

password = ''

random.shuffle(password_list)
for i in password_list:
    password += i
print(password)