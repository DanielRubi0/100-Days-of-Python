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

#Write your code below this line 👇

import random

options = [rock, paper, scissors]
user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_option >= 3 or user_option < 0:
  print("You typed a wrong option, try again.")

else:
  user_option = options[user_option]
  print(user_option)
  computer_option = random.choice(options)
  print(f"Computer chose: \n {computer_option}")

  if user_option == computer_option:
    print("It\'s a draw")
  else:
    if user_option == rock and computer_option == scissors:
      print("You won!")

    elif user_option == rock and computer_option == paper:
      print("You lost!")

    elif user_option == scissors and computer_option == paper:
      print("You won!")

    elif user_option == scissors and computer_option == rock:
      print("You lost!")

    elif user_option == paper and computer_option == rock:
      print("You won!")

    elif user_option == paper and computer_option == scissors:
      print("You lost!")

    elif user_option == paper and computer_option == scissors:
      print("You lost!")

