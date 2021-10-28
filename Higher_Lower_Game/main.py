import random
import art
from game_data import data

print(art.logo)
one = random.choice(data)
two = random.choice(data)

def guess():
    global two
    two = random.choice(data)
    print(f"Compare A: {one['name']}, a {one['description']}, from {one['country']}")
    print(art.vs)
    print(f"Against B: {two['name']}, a {two['description']}, from {two['country']}\n")
    return input("Who has more followers? Type 'A' or 'B': ")

answer = guess()

def compare():
    one_count = int(one["follower_count"])
    two_count = int(two["follower_count"])
    if one_count > two_count:
        return 'a'
    else:
        return 'b'

n=0
game_over = False
# print(result)
while not game_over:
    result = compare()
    if result == answer:
        n += 1
        print(f"You're right! Current score: {n}.")
        if result == 'b':
            one = two
        answer = guess()
    else:
        print(f"Game Over! Current score: {n}.")
        game_over = True



