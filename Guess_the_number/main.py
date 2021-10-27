from art import logo
import random

def again():
    choice = int(random.randint(1,101))
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # print(f"Pssst, the corect answer is {choice}")   ===> For debugging 

    level = input("Choose a difficulty. Type 'easy' or 'hard':  ")

    if level == "easy":
        retry = 9
        print("You have 10 attempts remaining to guess the number.")

    if level == "hard":
        retry = 4
        print("You have 5 attempts remaining to guess the number.")

    guess = int(input("Make a guess:  "))
    if guess == choice:
        print(f"You got it on the first try! The answer was {choice}.")
        retry = 0

    while not retry == 0:
        if guess > choice:
            print(f"You have {retry} attempts remaining to guess the number.")
            print("Too high.")
        if guess < choice:
            print(f"You have {retry} attempts remaining to guess the number.")
            print("Too Low.")
        guess = int(input("Guess again:  "))
        retry -= 1
        if retry == 0:
            print("You've run out of guesses, you lose.")
        if guess == choice:
            print(f"You got it! The answer was {choice}.")
            retry = 0
    repeat = input("Do you want to play again? Type 'y' for yes and 'n' for no: ")
    if repeat == "y":
        again()

again()
