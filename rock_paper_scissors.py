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
user = int(input("Enter your choice:"
             "Rock: 0, Paper: 1 or scissors:2 "))
game_image = [rock,paper,scissors]
print(game_image[user])
import random

com = random.randint(0,2)
print("Computer chose:")
print(game_image[com])
if user == 0 :
    if com == 2:
        print("You Win")
    elif com == 1:
        print("You Lose")
    elif com == 0:
        print("Tie")
if user == 1:
    if com == 0:
        print("You Win")
    elif com == 2:
        print("You Lose")
    elif com == 1:
        print("Tie")
if user == 2:
    if com == 1:
        print("You Win")
    elif com == 0 :
        print("You Lose")
    elif com == 2:
        print("Tie")