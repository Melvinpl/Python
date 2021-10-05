"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
"""
import math
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print (f"You'll need {number_of_cans} cans of paint")

# Define a function called paint_calc() so that the code below works.   

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
