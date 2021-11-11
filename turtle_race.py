from turtle import Turtle, Screen, color
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")
colors = ["red","orange","yellow","green","blue","purple"]
new_turtle = []

def instance(color, y_axis):
    tur = Turtle(shape= "turtle")
    tur.color(color)
    tur.penup()
    tur.goto(x=-230, y=(-100+y_axis))
    tur.color(color)
    new_turtle.append(tur)

m=0
for n in range(6):
    instance(colors[n], m), 
    m += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in new_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0,10))
        
            
screen.exitonclick()