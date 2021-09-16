'''
A virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 
'''
import random
number = random.randint(0,1)

if number == 0:
    print("Tails")
else:
    print("Heads")