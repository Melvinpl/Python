from turtle import Turtle, Screen
import random

tim= Turtle()
screen = Screen()
tim.speed("fastest")
screen.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    colour = (r, g, b)
    return colour

n = 0
angle = 360
while not angle == 0:
    angle = 360 - n
    tim.color(random_colour())
    tim.circle(100)
    tim.left(angle)
    n += 1
    angle += 1

screen = Screen()
screen.exitonclick()