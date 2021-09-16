"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

    Take both people's names and check for the number of times the letters in the word TRUE occurs. 
    Then check for the number of times the letters in the word LOVE occurs. 
    Then combine these numbers to make a 2 digit number. 

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

"""
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
combine_name = lower_name1 + lower_name2

T = int(combine_name.count("t"))
R = int(combine_name.count("r"))
U = int(combine_name.count("u"))
E = int(combine_name.count("e"))
true_total = str((T+R+U+E))

L = int(combine_name.count("l"))
O = int(combine_name.count("o"))
V = int(combine_name.count("v"))
love_total = str((L+O+V+E))

Your_score = true_total + love_total

print(f"T occurs {T} times\n")
print(f"R occurs {R} times\n")
print(f"U occurs {U} times\n")
print(f"E occurs {E} times\n")
print(f"Total = {true_total}\n")

print(f"L occurs {L} times\n")
print(f"O occurs {O} times\n")
print(f"V occurs {V} times\n")
print(f"E occurs {E} times\n")
print(f"Total = {love_total}\n")

Your_score = int(Your_score)
if Your_score < 10 and Your_score > 90:
    print(f"Your score is : {Your_score}, you go together like coke and mentos.")
elif Your_score < 50 and Your_score > 40:
    print(f"Your score is {Your_score}, you are alright together.")
else:
    print(f"Your score is : {Your_score}")