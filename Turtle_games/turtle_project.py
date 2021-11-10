from turtle import Turtle, Screen

tim= Turtle()
colour = ["red","blue", "green", "DarkGrey", "chocolate", "DarkOrange", "cyan"]

n = 3
m = 0
for _ in range(8):
    angle = 360 / n
    for _ in range(n):
        tim.forward(100)
        tim.right(angle)
        tim.color(colour[m])
    n += 1
    m += 1

screen = Screen()
screen.exitonclick()