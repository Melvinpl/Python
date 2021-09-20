rock_d = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_d = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_d = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user = input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n All the best !!")
if user == "0":
    print(rock_d)
elif user == "1":
    print(paper_d)
else:
    print(scissors_d)

play = ["rock", "paper", "scissors"]
computer = random.choice(play)

print("Computer Chose: \n")
if computer == "rock":
    print(rock_d)
elif computer == "paper":
    print(paper_d)
else:
    print(scissors_d)

if user == "0" and computer == "rock":
    decision = "Its a Draw"
elif user == "0" and computer == "paper":
    decision = "You Lose"
elif user == "0" and computer == "sicssors":
    decision = "You Win"

if user == "1" and computer == "rock":
    decision = "You Win"
elif user == "1" and computer == "paper":
    decision = "Its a Draw"
elif user == "1" and computer == "sicssors":
    decision = "You Lose"

if user == "2" and computer == "rock":
    decision = "You Lose"
elif user == "2" and computer == "paper":
    decision = "You Win"
elif user == "2" and computer == "sicssors":
    decision = "Its a Draw"

print (f"{decision}\n")

