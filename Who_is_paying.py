'''
A program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 
easiler way would be to use random.choice 
'''

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_of_ppl = len(names)
random_num = random.randint(0,(number_of_ppl-1))
print(f"{names[random_num]} is going to buy the meal today!")

