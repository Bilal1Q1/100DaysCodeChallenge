import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

shows = [rock,paper,scissors]
my_choice = int(input("Choose Option 0 for Rock, 0 for 'Rock' 🥊, 1 for 'Paper' 📄 or 2 for 'Scissors' ✂\n"))

if my_choice >= 3:
    print('Wrong option Chooced. You lose !')
else:
    print(shows[my_choice])

machine_choice = random.randint(0,2)
print('Machine Choosed Option')
print(shows[machine_choice])

if my_choice == machine_choice:
    print('Result: Match Draw')
elif my_choice == 0 and machine_choice == 1:
    print('Computer Win')
elif my_choice == 0 and machine_choice == 2 :
    print('Me Win')
elif my_choice == 1 and machine_choice == 0:
    print('Me Win')
elif my_choice == 1 and machine_choice == 2:
    print('Computer Win')
elif my_choice == 2 and machine_choice == 0:
    print('Computer Win')
elif my_choice == 2 and machine_choice == 1:
    print('me Win')