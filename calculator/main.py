from art import logo
#Add
def add(n1,n2):
    return n1 + n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

Operations = {"+":add, "*":multiply, "/":divide, "-":subtract,}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? : "))
    repeat = "y"
    while repeat == "y":
        for symbol in Operations:
            print(symbol)
        opeartion_symbol = input("Pick the operation: ")
        num2 = float(input("What's the Next number? : "))
        calulation_function = Operations[opeartion_symbol]
        answer = calulation_function(num1,num2)

        print(f"{num1} {opeartion_symbol} {num2} = {answer}")
        repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over:  ")
        if repeat == "y":
            num1 = answer
        elif repeat == "n":
            calculator()

calculator()