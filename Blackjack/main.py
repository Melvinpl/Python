############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from art import logo
from os import system, name

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def random_card():
        return random.choice(cards)

    user_cards = []
    computer_cards = []
    def deal_card():
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    deal_card()
    deal_card()
    def calculate_score(n):
        score = sum(n)
        if score > 21:
            if 11 in n:
                n.remove(11)
                n.append(1)
            score = sum(n)
        return score

    game_ended = False
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    #print(f"Your Cards: {user_cards}, current score: {user_score}")
    #print(f"Computer's First card: {computer_cards[0]} ")


    def check(user_score):
        if user_score == 21:
            print(f"Your Final hand: {user_cards} , final score: 21")
            print ("BlackJack !!  YOU WIN")
            return True
        if user_score < 21:
            print(f"Your hand: {user_cards} , final score:{user_score}")
            print(f"Computer's First card: {computer_cards[0]} ")
            return False
        if user_score > 21:
            print(f"Your Final hand: {user_cards} , final score:{user_score}")
            print(f"Computer's Final hand: {computer_cards} , final score:{computer_score}")
            print ("You went over. You Loose")
            return True

    check(user_score)
    while not game_ended:
        play = input("Type 'y' to get another card, type 'n' to pass:  ")
        if play == 'y':
            deal_card()
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            game_ended = check(user_score)
        if play == 'n':
            if user_score == computer_score and user_score > 21:
                print(f"Your Final hand: {user_cards} , final score:{user_score}")
                print(f"Computer's Final hand: {computer_cards} , final score:{computer_score}")
                print ("Draw")
                game_ended = True
            elif user_score > computer_score and user_score < 21:
                print(f"Your Final hand: {user_cards} , final score:{user_score}")
                print(f"Computer's Final hand: {computer_cards} , final score:{computer_score}")
                print ("You Win !!")
                game_ended = True
            elif user_score < computer_score and computer_score > 21:
                print(f"Your Final hand: {user_cards} , final score:{user_score}")
                print(f"Computer's Final hand: {computer_cards} , final score:{computer_score}")
                print ("You Win !!")
                game_ended = True
            else:
                print(f"Your Final hand: {user_cards} , final score:{user_score}")
                print(f"Computer's Final hand: {computer_cards} , final score:{computer_score}")
                print ("You Loose !!")
                game_ended = True            


    repeat = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if repeat == "y":
        clear()
        game()

game()