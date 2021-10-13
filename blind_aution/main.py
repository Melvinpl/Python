from os import system, name
from art import logo

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print(logo)
repeat = "yes"
users = {}
highest = 0
highest_user = {}
highest_bid = ""

while repeat == "yes":
    name = input("What is your name ?")
    bid = input("What's your bid ? : $")
    users[name] = bid
    repeat = input("Are there any other bidders ? Type 'yes' or 'no' ")
    if repeat == "yes":
        clear()

for key in users:
    if int(highest) < int(users[key]):
        highest = users[key]
        highest_user = key
        highest_bid = users[key]

clear()
print(f"The Winner is {highest_user} with a bid of ${highest_bid}")
